"""Reproduce Step33f local mixed Poisson and radial primary-surface witness.

Includes the 31 original exact-byte Step33e tests and all new Step33f tests.
This is NOT a complete clone or a full HR BD Dirac rank proof.
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
 'numerics/hr_spherical_local_mixed_kernel.py',
 'numerics/hr_spherical_radial_primary_surface.py',
 'tests/test_hr_spherical_local_primary_kernel.py',
 'scripts/verify_gate2b_step33f.py',
)
PREVIOUS_EXACT_GIT_BLOBS={
 'numerics/hr_spherical_mixed_hamiltonian_bracket.py':'6e7a91b0ff4b63c4442b1ba3a05a06cafc585d81',
 'tests/test_hr_spherical_mixed_hamiltonian_bracket.py':'ed3525383bc61b6b1cc838f29139df9663add918',
}

def git_blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def main():
    missing=[path for path in FILES if not (ROOT/path).is_file()]
    if missing:raise SystemExit('Missing source: '+', '.join(missing))
    digests={p:{'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),
                'git_blob_sha1':git_blob((ROOT/p).read_bytes())} for p in FILES}
    nonmatching=[p for p,sha in PREVIOUS_EXACT_GIT_BLOBS.items()
                 if digests[p]['git_blob_sha1']!=sha]
    if nonmatching:raise SystemExit('Previous exact GitHub sources changed: '+', '.join(nonmatching))
    env=os.environ.copy();env['PYTHONPATH']=str(ROOT)+os.pathsep+env.get('PYTHONPATH','')
    env['OPENBLAS_NUM_THREADS']='1'
    run=subprocess.run([sys.executable,'-m','pytest','-q','tests/test_hr_spherical_mixed_hamiltonian_bracket.py',
                        'tests/test_hr_spherical_local_primary_kernel.py'],
                      cwd=ROOT,env=env,capture_output=True,text=True,check=False)
    report={
      'stage':'JANUS-Step33f-local-mixed-Poisson-kernel-on-restricted-radial-primary-surface',
      'workspace_origin':'standalone_focused_non_git_workspace',
      'full_repository_regression':False,
      'prior_step33d_95_tests_rerun':False,
      'includes_original_step33e_31_tests':True,
      'original_step33e_git_blobs_verified':True,
      'source_digests':digests,
      'python':sys.version.split()[0],
      'test_exit_code':run.returncode,
      'pytest_output':(run.stdout+run.stderr).strip()[-5000:],
      'radial_mixed_poisson_kernel':'COMPUTED_ON_ARBITRARY_OFFSHELL_RADIAL_DATA',
      'local_primary_constraint_surface':'CONSTRUCTED_FOR_FLAT_SPATIAL_SLICES_AND_RADIAL_MOMENTA',
      'primary_surface_Hg_Hf_Ddiag':'SATISFIED_IN_EXPLICIT_RADIAL_POLYNOMIAL_FAMILY',
      'secondary_local_candidate':'VERIFIED_ONLY_ON_EXPLICIT_RESTRICTED_PRIMARY_SURFACE',
      'general_local_BD_secondary':'NOT_DERIVED',
      'Dirac_secondary_preservation_and_lapse_fixing':'NOT_DERIVED',
      'physical_nonhomothetic_on_shell_solution':'NOT_ESTABLISHED',
      'physical_DeFelice_Aoki_oracles':'NOT_RUN',
      'GATE_2B':'OPEN',
    }
    if run.returncode==0:
       from numerics.hr_spherical_local_mixed_kernel import (
          local_mixed_kernel,integrate_kernel)
       from numerics.hr_spherical_mixed_hamiltonian_bracket import mixed_smeared_poisson
       from numerics.hr_spherical_radial_primary_surface import (
           radial_primary_witness,primary_residuals,local_secondary_candidate)
       off=local_mixed_kernel(r=.43).coefficients
       unconstrained_integrated=integrate_kernel(order=40).sum()
       w=radial_primary_witness(a=.4);r=.43
       constrained=local_mixed_kernel(w.fields,r,betas=w.betas,
                         m2=w.m2,mg2=w.mg2,mf2=w.mf2).coefficients
       constrained_int=integrate_kernel(w.fields,order=40,betas=w.betas,
                         m2=w.m2,mg2=w.mg2,mf2=w.mf2).sum()
       baseline=mixed_smeared_poisson(w.fields,order=40,betas=w.betas,
                         m2=w.m2,mg2=w.mg2,mf2=w.mf2)
       report['benchmarks']={
         'off_shell_local_kernel_r043':off.tolist(),
         'off_shell_integrated':float(unconstrained_integrated),
         'radial_primary_a':w.a,
         'radial_primary_y':w.b/w.a,
         'radial_primary_r':r,
         'radial_primary_residuals':primary_residuals(w,r).tolist(),
         'g_and_f_dust_positive':bool(w.fields['pg'](r)>0 and w.fields['pf'](r)>0),
         'restricted_primary_kernel_r043':constrained.tolist(),
         'restricted_primary_secondary_formula':float(local_secondary_candidate(w,r)),
         'restricted_primary_bracket_integrated':float(constrained_int),
         'original_full_integrated_bracket':baseline.bracket,
         'relative_shift_equation_max':baseline.shift_equation_max,
       }
    result=json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+'\n'
    print(result)
    if len(sys.argv)>1:Path(sys.argv[1]).write_text(result,encoding='utf-8')
    return run.returncode

if __name__=='__main__':raise SystemExit(main())
