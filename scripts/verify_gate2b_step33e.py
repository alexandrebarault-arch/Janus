"""Reproduce the Step33e mixed spherical functional Poisson bracket acceptance gate.

Run from any directory:
 OPENBLAS_NUM_THREADS=1 python scripts/verify_gate2b_step33e.py report.json
Reports exact tested source fingerprints and preserves all unpassed physics gates.
Standalone focused suite, not a clean checkout or full repository regression.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
FILES=(
    'numerics/hr_spherical_mixed_hamiltonian_bracket.py',
    'tests/test_hr_spherical_mixed_hamiltonian_bracket.py',
    'scripts/verify_gate2b_step33e.py',
)

def main():
    missing=[p for p in FILES if not (ROOT/p).is_file()]
    if missing:raise SystemExit('Missing Step33e sources: '+', '.join(missing))
    env=os.environ.copy()
    env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    args=[sys.executable,'-m','pytest','-q','tests/test_hr_spherical_mixed_hamiltonian_bracket.py']
    completed=subprocess.run(args,cwd=ROOT,env=env,capture_output=True,text=True,check=False)
    report={
      'stage':'JANUS-Step33e-spherical-mixed-Hg-Hf-smeared-functional-Poisson',
      'workspace_origin':'standalone_focused_non_git_workspace',
      'full_repository_regression':False,
      'prior_step33d_95_tests_rerun':False,
      'physical_genuine_nonhomothetic_onshell':'NOT_ESTABLISHED',
      'spatial_mixed_Hg_Hf_functional_bracket':'COMPUTED_ON_RADIAL_OFFSHELL_FAMILY',
      'radial_HR_relative_shift_auxiliary':'ELIMINATED_ON_REGULAR_K_BRANCH',
      'Dirac_primary_secondary_time_preservation':'NOT_DERIVED',
      'BD_secondary_and_lapse_fixing':'NOT_DERIVED',
      'physical_DeFelice_and_Aoki_oracles':'NOT_RUN',
      'GATE_2B':'OPEN',
      'python':sys.version.split()[0],
      'sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in FILES},
      'test_exit_code':completed.returncode,
      'pytest_output':(completed.stdout+completed.stderr).strip()[-5000:],
    }
    if completed.returncode==0:
        from numerics.hr_spherical_mixed_hamiltonian_bracket import (
          mixed_smeared_poisson,compact_smearings,Poly)
        N,M=compact_smearings()
        benchmark=mixed_smeared_poisson(order=48)
        alternate=mixed_smeared_poisson(N=M,M=N,order=48)
        fixed=mixed_smeared_poisson(z_mode='fixed',z_fixed=Poly([.08,.035,-.01]),order=48)
        report['benchmark']={
          'mixed_Hg_N_Hf_M':benchmark.bracket,
          'canonical_pair_contributions':benchmark.sector_contributions,
          'hg_integral':benchmark.hg_integral,
          'hf_integral':benchmark.hf_integral,
          'max_shift_equation_residual':benchmark.shift_equation_max,
          'swapped_radial_smearings':alternate.bracket,
          'externally_fixed_z_not_same':fixed.bracket,
        }
    data=json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    print(data)
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(data,encoding='utf-8')
    return completed.returncode

if __name__=='__main__':raise SystemExit(main())
