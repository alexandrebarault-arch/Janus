"""Reproduce the *homogeneous* HR secondary-bracket audit, with provenance.

    OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step33b.py [report.json]

A finite-dimensional homogeneous Poisson condition is NOT the radial HR BD
secondary, full constrained scalar speed or new nonhomothetic cosmology.
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
TARGETS=("tests/test_hr_spherical_adm_primary.py",
         "tests/test_hr_homogeneous_poisson_secondary.py")
SOURCES=("numerics/hr_spherical_adm_primary.py",
         "numerics/hr_homogeneous_poisson_secondary.py",
         "scripts/verify_gate2b_step33b.py")
PRIOR_GIT_BLOBS={
    "numerics/hr_spherical_adm_primary.py":"c04aae4cadcefe1dcf6d937b7f3a2d37573f5d41",
    "tests/test_hr_spherical_adm_primary.py":"f71b687e9a9027dd0ce6b41553bcad68ba2b1133",
}


def git(*args):
    try:
        r=subprocess.run(["git",*args],cwd=ROOT,text=True,
                         capture_output=True,timeout=5,check=False)
        return r.stdout.strip() if r.returncode==0 else None
    except (OSError,subprocess.TimeoutExpired):
        return None


def main():
    files=TARGETS+SOURCES+("research/HOMOGENEOUS_POISSON_SECONDARY_STEP33B_AUDIT.md",)
    missing=[p for p in files if not (ROOT/p).is_file()]
    if missing:raise SystemExit("Missing research source files: "+", ".join(missing))
    hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files}
    blobs={p:git("hash-object",p) for p in files}
    provenance={p:blobs[p]==h for p,h in PRIOR_GIT_BLOBS.items()}
    if not all(provenance.values()):
        raise SystemExit("Prior Step33a source bytes differ from GitHub-provenance blobs")
    env=os.environ.copy()
    env["PYTHONPATH"]=str(ROOT)+os.pathsep+env.get("PYTHONPATH","")
    env["OPENBLAS_NUM_THREADS"]="1"
    command=[sys.executable,"-m","pytest","-q",*TARGETS]
    p=subprocess.run(command,cwd=ROOT,env=env,text=True,
                     capture_output=True,check=False)
    summary=(p.stdout+"\n"+p.stderr).strip()
    n=re.search(r"(\d+) passed",summary)
    root=git("rev-parse","--show-toplevel")
    in_git=root is not None and Path(root).resolve()==ROOT
    result={
      "stage":"JANUS-GATE2B-STEP33B-HOMOGENEOUS-POISSON-ONLY",
      "tests_exit_code":p.returncode,
      "tests_passed_count":int(n.group(1)) if n else 0,
      "tests_summary":summary[-3500:],
      "executed_together":True,
      "python":sys.version.split()[0],
      "workspace_origin":"git_worktree" if in_git else "focused_non_git_workspace",
      "git_head":git("rev-parse","HEAD") if in_git else None,
      "prior_step33a_exact_git_blob_matches":provenance,
      "sha256":hashes,
      "git_blob_sha":blobs,
      "scientific_acceptance":{
        "homogeneous_primary_poisson_factorization":"TESTED",
        "homogeneous_secondary_preservation_lapse_ratio":"TESTED",
        "independent_dual_dust_canonical_pairs":"TESTED",
        "homogeneous_dirac_matrix_rank":"TESTED",
        "spatially_dependent_spherical_BD_secondary":"NOT_DERIVED",
        "full_4d_HR_BD_constraint":"NOT_DERIVED",
        "on_shell_genuine_nonhomothetic_background":"NOT_FOUND",
        "DeFelice_finite_H_oracle":"NOT_RUN",
        "Aoki_nonlinear_homothetic_oracle":"NOT_RUN",
        "GATE_2B":"OPEN",
      },
      "full_repository_regression":False,
      "earlier_step32e_93_tests_reexecuted":False,
    }
    out=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
    print(out)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(out,encoding="utf-8")
    return p.returncode

if __name__=="__main__":
    raise SystemExit(main())
