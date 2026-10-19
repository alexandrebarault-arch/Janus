"""Reproduce Step33c spatial-diffeomorphism functional bracket, with provenance.

    OPENBLAS_NUM_THREADS=1 PYTHONPATH=. python scripts/verify_gate2b_step33c_spatial.py report.json

This verifies {D[eta],D[xi]} and scalar density Ward. It DOES NOT compute
{Hg,Hf} as a functional field-theory bracket or the HR BD secondary.
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
TESTS=("tests/test_hr_spherical_adm_primary.py",
       "tests/test_hr_homogeneous_poisson_secondary.py",
       "tests/test_hr_spherical_radial_diffeo_ward.py")
SOURCES=("numerics/hr_spherical_adm_primary.py",
         "numerics/hr_homogeneous_poisson_secondary.py",
         "numerics/hr_spherical_radial_diffeo_ward.py",
         "scripts/verify_gate2b_step33c_spatial.py",
         "research/HAMILTONIAN_SPATIAL_DIFF_STEP33C_AUDIT.md")
PRIOR_BLOBS={
 "numerics/hr_spherical_adm_primary.py":"c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41",
 "tests/test_hr_spherical_adm_primary.py":"f71b687e9a9027dd0ce6b41553bcad68ba2b1133",
 "numerics/hr_homogeneous_poisson_secondary.py":"43e03d01da57ddc23acb75db0ae660c001ea8e38",
 "tests/test_hr_homogeneous_poisson_secondary.py":"0c09ae4ae470a7e8b96dabac4909b1dfa7b8510d",
}

def git(*args):
    try:
        p=subprocess.run(['git',*args],cwd=ROOT,capture_output=True,
                         text=True,timeout=5)
        return p.stdout.strip() if p.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired):return None


def main():
    paths=TESTS+SOURCES
    absent=[p for p in paths if not (ROOT/p).is_file()]
    if absent:raise SystemExit("Missing necessary files: "+", ".join(absent))
    blobs={p:git('hash-object',p) for p in paths}
    prior_match={p:blobs[p]==s for p,s in PRIOR_BLOBS.items()}
    if not all(prior_match.values()):
        raise SystemExit('Previous Step33a/33b GitHub published source SHA mismatch')
    env=os.environ.copy()
    env['OPENBLAS_NUM_THREADS']='1'
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    p=subprocess.run([sys.executable,'-m','pytest','-q',*TESTS],cwd=ROOT,
                     env=env,capture_output=True,text=True,check=False)
    stdout=(p.stdout+'\n'+p.stderr).strip()
    found=re.search(r'(\d+) passed',stdout)
    git_root=git('rev-parse','--show-toplevel')
    worktree=git_root is not None and Path(git_root).resolve()==ROOT
    report={
      'stage':'GATE2B-STEP33C-SPATIAL-DIFFEOMORPHISM-BRACKET-ONLY',
      'test_exit_code':p.returncode,
      'tests_passed_count':int(found.group(1)) if found else 0,
      'tests_output':stdout[-3000:],
      'python':sys.version.split()[0],
      'workspace_origin':'git_worktree' if worktree else 'focused_non_git_workspace',
      'git_head':git('rev-parse','HEAD') if worktree else None,
      'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
      'git_blob':blobs,
      'prior_step33a_33b_exact_source_matches':prior_match,
      'full_repository_regression':False,
      'earlier_step32e_93_tests_reexecuted':False,
      'scientific_gates':{
        'smeared_radial_momentum_PB_closure':'TESTED',
        'twelve_canonical_variation_functional_gradients':'TESTED',
        'both_canonical_dust_pairs':'PRESERVED',
        'two_local_Hamiltonian_density_spatial_Ward':'TESTED',
        'relative_shift_root_radial_scalar_covariance':'TESTED',
        'inhomogeneous_mixed_Hg_Hf_functional_PB':'NOT_DERIVED',
        'inhomogeneous_HR_BD_secondary_and_preservation':'NOT_DERIVED',
        'genuinely_nonhomothetic_on_shell_solution':'NOT_FOUND',
        'DeFelice_physical_scalar':'NOT_RUN',
        'Aoki_physical_scalar':'NOT_RUN',
        'GATE_2B':'OPEN',
      },
    }
    serialized=json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    print(serialized)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(serialized,encoding='utf-8')
    return p.returncode

if __name__=='__main__':raise SystemExit(main())
