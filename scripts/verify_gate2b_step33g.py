#!/usr/bin/env python3
"""Step33g source-provenance verifier: two independent execution groups.

The primary group (22 tests) and bracket group (3 heavier symbolic tests)
are deliberately invoked in SEPARATE top-level executions due time limits.
Never claim a completed single all-25 run.
"""
from __future__ import annotations
import hashlib,json,os,pathlib,re,subprocess,sys,time

ROOT=pathlib.Path(__file__).resolve().parents[1]
FILES=(
 'numerics/hr_curved_moving_dust_primary.py',
 'numerics/hr_curved_primary_mixed_kernel.py',
 'tests/test_hr_curved_moving_dust_primary.py',
 'tests/test_hr_curved_primary_mixed_kernel.py',
 'tests/test_hr_curved_flat_reference.py',
 'scripts/verify_gate2b_step33g.py',
)
GROUPS={
  'primary':('tests/test_hr_curved_moving_dust_primary.py',
             'tests/test_hr_curved_flat_reference.py'),
  'bracket':('tests/test_hr_curved_primary_mixed_kernel.py',),
}


def main():
    if len(sys.argv) not in (2,3) or sys.argv[1] not in GROUPS:
        raise SystemExit('Usage: python scripts/verify_gate2b_step33g.py primary|bracket [report.json]')
    group=sys.argv[1]
    out=pathlib.Path(sys.argv[2]) if len(sys.argv)==3 else ROOT/f'gate2b-step33g-{group}-report.json'
    if not out.is_absolute():out=ROOT/out
    env={**os.environ,'PYTHONPATH':str(ROOT),'OPENBLAS_NUM_THREADS':'1',
         'PYTEST_DISABLE_PLUGIN_AUTOLOAD':'1'}
    manifest=[]
    for p in FILES:
        bs=(ROOT/p).read_bytes()
        h=hashlib.sha256(bs).hexdigest()
        git=subprocess.run(['git','hash-object','--stdin'],input=bs,capture_output=True,check=True).stdout.decode().strip()
        manifest.append({'path':p,'sha256':h,'git_blob':git,'bytes':len(bs)})
    runs=[]
    for name in GROUPS[group]:
        cmd=[sys.executable,'-m','pytest','-vv','-s',name]
        t=time.monotonic()
        z=subprocess.run(cmd,cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,timeout=120)
        m=re.search(r'([0-9]+) passed',z.stdout)
        runs.append({'test':name,'passed':int(m.group(1)) if m else 0,
                     'exit_code':z.returncode,'seconds':round(time.monotonic()-t,2),
                     'output':z.stdout[-2400:]})
    # Independent primary-surface metrics, computed AFTER the isolated tests.
    from numerics.hr_curved_moving_dust_primary import build_primary,assert_regular
    metrics=assert_regular(build_primary())
    status=all(r['exit_code']==0 for r in runs)
    rep={
        'step':'33g','test_group':group,'date':'2026-10-19','branch':'research/gate2b-nonhomothetic-transfer',
        'python':sys.version.split()[0],'workspace_origin':'new_standalone_non_git_workspace',
        'runs':runs,'tests_total_across_separate_processes':sum(r['passed'] for r in runs),
        'all_passed':status,'curved_noncomoving_primary_witness':metrics,
        'sources':manifest,'full_repository_regression':False,
        'old_step33f_52_tests_rerun':False,
        'general_local_BD_secondary':'NOT_DERIVED',
        'Dirac_secondary_time_preservation':'NOT_DERIVED',
        'Dirac_lapse_fixing':'NOT_DERIVED',
        'genuine_nonhomothetic_evolving_on_shell_background':'NOT_FOUND',
        'DeFelice_finite_H_oracle':'NOT_RUN','Aoki_homothetic_KS_cs2_oracle':'NOT_RUN',
        'gate2b':'OPEN','JANUS_R_cosmological_validation':False,
        'note':'Run primary and bracket groups in SEPARATE top-level invocations. Hosted symbolic cache accumulation made an all-in-one verification time out. No full joint 25-test run and no sum with Step33f 52.'
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n',encoding='utf8')
    print(f"Step33g group {group}: {sum(r['passed'] for r in runs)} tests / {len(runs)} isolated processes; status={status}; report={out}")
    for r in runs:print(f"  {r['test']} => {r['passed']} passed ({r['seconds']}s), exit={r['exit_code']}")
    return 0 if status else 1

if __name__=='__main__':raise SystemExit(main())
