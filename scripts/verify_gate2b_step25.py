"""Reproducible *targeted* Gate 2B step-25 scientific verification.

Usage: python scripts/verify_gate2b_step25.py [output.json]
Focused 41-test suite; not a full repository suite, independent peer replication or physical oracle.
The script never silently upgrades a manually reconstructed workspace into
an asserted clean Git checkout. All required test files are explicit.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (
    'tests/test_hr_full_scalar_eh_homothetic.py',
    'tests/test_hr_full_scalar_eh_two_dust_untilted.py',
    'tests/test_hr_full_scalar_eh_two_dust_real.py',
    'tests/test_hr_eh_spacetime_ward.py',
    'tests/test_hr_eh_full_scalar_chart_ward.py',
    'tests/test_hr_eh_full_scalar_quadratic_chart.py',
)
SOURCES = (
    'numerics/hr_native_stueckelberg_jet.py',
    'numerics/hr_native_field_sampling.py',
    'numerics/hr_compact_radial_interaction.py',
    'numerics/hr_native_sampling_compact.py',
    'numerics/hr_two_dust_preconstraint.py',
    'numerics/hr_full_scalar_eh_homothetic.py',
    'numerics/hr_full_scalar_eh_two_dust_untilted.py',
    'numerics/hr_eh_spacetime_ward.py',
    'numerics/hr_eh_full_scalar_chart_ward.py',
    'numerics/hr_eh_full_scalar_quadratic_chart.py',
    'numerics/spherical_flat_adm_eh.py',
)


def _git(*args):
    try:
        x=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,text=True,
                         check=False,timeout=8)
    except (FileNotFoundError,subprocess.TimeoutExpired):
        return None
    return x.stdout.strip() if x.returncode==0 else None


def main():
    missing=[x for x in TARGETS+SOURCES if not (ROOT/x).is_file()]
    if missing:
        raise SystemExit('Cannot verify: missing required files: '+', '.join(missing))
    manifest={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest()
              for x in TARGETS+SOURCES}
    git_root=_git('rev-parse','--show-toplevel')
    clean_git=git_root is not None and Path(git_root).resolve()==ROOT
    status=_git('status','--porcelain') if clean_git else None
    data={
      'gate':'Gate2B-step25-EH-chart-quadratic-and-HR-relative-interaction',
      'full_repository_regression':False,
      'physical_stability_oracles':{'DeFelice':'NOT_RUN','Aoki':'NOT_RUN'},
      'gate2b':'OPEN',
      'workspace_origin':'git_checkout' if clean_git else 'non_git_workspace_reconstruction',
      'git_head':_git('rev-parse','HEAD') if clean_git else None,
      'git_worktree_dirty':bool(status) if clean_git else None,
      'python':sys.version.split()[0],
      'sha256':manifest,
    }
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env.setdefault('OPENBLAS_NUM_THREADS','1')
    command=[sys.executable,'-m','pytest','-q',*TARGETS]
    proc=subprocess.run(command,cwd=ROOT,env=env,capture_output=True,
                        text=True,check=False)
    report=(proc.stdout+proc.stderr).strip()
    match=re.search(r'(\d+) passed',report)
    data.update({'tests_exit_code':proc.returncode,
                 'tests_passed_count':int(match.group(1)) if match else 0,
                 'tests_stdout':report[-5000:]})
    result=json.dumps(data,indent=2,sort_keys=True,ensure_ascii=False)
    print(result)
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(result+'\n',encoding='utf-8')
    return proc.returncode


if __name__=='__main__':
    raise SystemExit(main())
