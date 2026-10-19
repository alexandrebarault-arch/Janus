"""Reproduce Step33c radially smeared dual-dust bracket and steps33a/b.

Usage: python scripts/verify_gate2b_step33c.py report.json
Focused scientific suite, NOT full radial EH+HR+BD constraint proof.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
TESTS=(
    'tests/test_hr_spherical_adm_primary.py',
    'tests/test_hr_homogeneous_poisson_secondary.py',
    'tests/test_hr_spherical_dust_smeared_bracket.py',
)
SOURCES=(
    'numerics/hr_spherical_adm_primary.py',
    'numerics/hr_homogeneous_poisson_secondary.py',
    'numerics/hr_spherical_dust_smeared_bracket.py',
    'scripts/verify_gate2b_step33c.py',
    'research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md',
)
EXACT_PRIOR={
    'numerics/hr_spherical_adm_primary.py':'c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41',
    'tests/test_hr_spherical_adm_primary.py':'f71b687e9a9027dd0ce6b41553bcad68ba2b1133',
    'numerics/hr_homogeneous_poisson_secondary.py':'43e03d01da57ddc23acb75db0ae660c001ea8e38',
    'tests/test_hr_homogeneous_poisson_secondary.py':'0c09ae4ae470a7e8b96dabac4909b1dfa7b8510d',
}

def _git(*args):
    try:
        v=subprocess.run(['git',*args],cwd=ROOT,check=False,capture_output=True,text=True,timeout=6)
        return v.stdout.strip() if v.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired):
        return None

def main():
    paths=TESTS+SOURCES
    missing=[x for x in paths if not (ROOT/x).is_file()]
    if missing:raise SystemExit('Missing Step33c source/tests: '+', '.join(missing))
    blobs={x:_git('hash-object',x) for x in paths}
    exact={x:blobs[x]==sha for x,sha in EXACT_PRIOR.items()}
    if not all(exact.values()):
        raise SystemExit('Required Step33a/b source blobs differ from published GitHub')
    data={
      'gate':'JANUS-Step33c-radial-dust-functional-Poisson',
      'workspace_origin':'git_worktree' if _git('rev-parse','--show-toplevel') else 'focused_non_git_workspace',
      'git_head':_git('rev-parse','HEAD'),
      'exact_prior_source_provenance':exact,
      'file_sha256':{x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in paths},
      'git_blob_sha':blobs,
      'full_repository_regression':False,
      'old_step32e_93_tests_rerun':False,
      'two_independent_radial_dust_brackets':'TESTED',
      'radial_dust_hypersurface_deformation_bracket':'TESTED_ANALYTICALLY_AND_CANONICALLY',
      'full_EH_HR_spherical_functional_brackets':'NOT_DERIVED',
      'local_spherical_HR_BD_secondary':'NOT_DERIVED',
      'DeFelice_Aoki_physical_oracles':'NOT_RUN',
      'genuine_nonhomothetic_on_shell':'NOT_ESTABLISHED',
      'GATE_2B':'OPEN',
      'python':sys.version.split()[0],
    }
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    proc=subprocess.run([sys.executable,'-m','pytest','-q',*TESTS],cwd=ROOT,
      env=env,capture_output=True,text=True,check=False)
    out=(proc.stdout+'\n'+proc.stderr).strip()
    n=re.search(r'(\d+) passed',out)
    data.update(test_exit_code=proc.returncode,tests_passed_count=int(n.group(1)) if n else 0,tests_output=out[-2500:])
    output=json.dumps(data,indent=2,ensure_ascii=False,sort_keys=True)+'\n'
    print(output)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(output,encoding='utf-8')
    return proc.returncode

if __name__=='__main__':raise SystemExit(main())
