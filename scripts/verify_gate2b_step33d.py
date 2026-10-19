"""Focused Gate2B step33d diagonal radial ADM/HR/dust Ward verification.

Usage: python scripts/verify_gate2b_step33d.py [report.json]
This cannot establish the full HR radial BD secondary or physical stability.
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
 'tests/test_hr_spherical_radial_diffeo_ward.py',
 'tests/test_hr_spherical_diagonal_primary_ward.py',
)
SOURCES=(
 'numerics/hr_spherical_adm_primary.py',
 'numerics/hr_homogeneous_poisson_secondary.py',
 'numerics/hr_spherical_dust_smeared_bracket.py',
 'numerics/hr_spherical_radial_diffeo_ward.py',
 'numerics/hr_spherical_diagonal_primary_ward.py',
 'scripts/verify_gate2b_step33d.py',
 'research/SPHERICAL_DUST_SMEARED_POISSON_STEP33C_AUDIT.md',
 'research/SPHERICAL_RADIAL_DIAGONAL_WARD_STEP33D_AUDIT.md',
)
EXACT_PRIOR={
 'numerics/hr_spherical_adm_primary.py':'c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41',
 'tests/test_hr_spherical_adm_primary.py':'f71b687e9a9027dd0ce6b41553bcad68ba2b1133',
 'numerics/hr_homogeneous_poisson_secondary.py':'43e03d01da57ddc23acb75db0ae660c001ea8e38',
 'tests/test_hr_homogeneous_poisson_secondary.py':'0c09ae4ae470a7e8b96dabac4909b1dfa7b8510d',
 'numerics/hr_spherical_dust_smeared_bracket.py':'d64ba7f790e63e21c626bb93763d971bb50b8fc2',
 'tests/test_hr_spherical_dust_smeared_bracket.py':'3a986c01c1ef1cd25d9ad2f9314719fe82233772',
 'numerics/hr_spherical_radial_diffeo_ward.py':'89e7f6eab35d28317f2f7a4330601736525487e5',
 'tests/test_hr_spherical_radial_diffeo_ward.py':'62282904a78af356121fb2fc1dc8046d7f92e0d7',
}

def git(*args):
    try:
        x=subprocess.run(['git',*args],cwd=ROOT,text=True,capture_output=True,
                         timeout=7,check=False)
        return x.stdout.strip() if x.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired):return None


def main():
    paths=TESTS+SOURCES
    missing=[p for p in paths if not (ROOT/p).is_file()]
    if missing:raise SystemExit('Missing focused sources: '+', '.join(missing))
    hashes={p:git('hash-object',p) for p in paths}
    exact={p:hashes[p]==sha for p,sha in EXACT_PRIOR.items()}
    if not all(exact.values()):raise SystemExit('Historical Step33a/b blobs DO NOT match live GitHub reference')
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','');env['OPENBLAS_NUM_THREADS']='1'
    process=subprocess.run([sys.executable,'-m','pytest','-q',*TESTS],
                           cwd=ROOT,env=env,text=True,capture_output=True,check=False)
    log=(process.stdout+'\n'+process.stderr).strip()
    count=re.search(r'(\d+) passed',log)
    report={
      'gate':'JANUS-Step33d-spherical-diagonal-radial-Noether-momentum-closure',
      'test_exit_code':process.returncode,
      'tests_passed_count':int(count.group(1)) if count else 0,
      'tests_output':log[-2500:],
      'exact_step33a_b_provenance':exact,
      'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
      'git_blob_sha':hashes,
      'workspace_origin':'git_worktree' if git('rev-parse','--show-toplevel') else 'focused_non_git_workspace',
      'git_head':git('rev-parse','HEAD'),
      'python':sys.version.split()[0],
      'full_repository_regression':False,
      'step32e_93_test_suite_rerun':False,
      'spherical_radial_diagonal_momentum_D_D_bracket':'TESTED',
      'spherical_full_primary_spatial_diffeo_ward':'TESTED_IN_FINITE_POLYNOMIAL_FAMILY',
      'two_dust_radial_hamiltonian_brackets':'TESTED',
      'spherical_full_mixed_H_g_H_f_poisson_bracket':'NOT_DERIVED',
      'spherical_HR_BD_secondary':'NOT_DERIVED',
      'genuine_nonhomothetic_on_shell':'NOT_ESTABLISHED',
      'DeFelice_Aoki_physical_oracles':'NOT_RUN',
      'GATE_2B':'OPEN'
    }
    output=json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
    print(output)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(output,encoding='utf-8')
    return process.returncode

if __name__=='__main__':raise SystemExit(main())
