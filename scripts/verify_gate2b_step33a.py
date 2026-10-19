"""Focused Step33a spherical ADM/HR primary interface regression and provenance.

Not a full repo suite; no BD secondary, scalar physical speeds, or on-shell
nonhomothetic cosmology. Command: python scripts/verify_gate2b_step33a.py out.json
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
TARGETS=['numerics/hr_spherical_adm_primary.py',
         'tests/test_hr_spherical_adm_primary.py',
         'scripts/verify_gate2b_step33a.py',
         'research/SPHERICAL_ADM_HR_PRIMARY_STEP33A_AUDIT.md']

def _git(*args):
    try:
        p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,text=True,timeout=6)
        return p.stdout.strip() if p.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired):return None

def main():
    if any(not (ROOT/x).is_file() for x in TARGETS):
        raise SystemExit('Step33a source, test, runner or audit missing')
    data={
        'gate':'Gate2B-Step33a-spherical-ADM-HR-lapse-affine-primary',
        'date':'2026-10-19',
        'source':'focused_spherical_field_density',
        'full_repository_regression':False,
        'historical_step32e_93_tests_rerun':False,
        'true_adm_spherical_legendre':'TESTED',
        'HR_lapse_affine_relative_shift':'TESTED',
        'two_dust_independent_canonical_momenta':'TESTED',
        'HR_BD_secondary':'NOT_DERIVED',
        'full_4D_scalar_gauge_closure':'NOT_DERIVED',
        'DeFelice_Aoki_physical_oracles':'NOT_RUN',
        'genuinely_nonhomothetic_on_shell':'NOT_FOUND',
        'Gate2B':'OPEN',
        'python_version':sys.version.split()[0],
        'git_head':_git('rev-parse','HEAD'),
        'git_worktree_status':_git('status','--porcelain'),
        'file_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in TARGETS},
    }
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    proc=subprocess.run([sys.executable,'-m','pytest','-q','tests/test_hr_spherical_adm_primary.py'],
                        cwd=ROOT,env=env,capture_output=True,text=True)
    data.update(test_exit_code=proc.returncode,test_output=(proc.stdout+proc.stderr).strip())
    out=json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    print(out)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(out,encoding='utf8')
    return proc.returncode

if __name__=='__main__':raise SystemExit(main())
