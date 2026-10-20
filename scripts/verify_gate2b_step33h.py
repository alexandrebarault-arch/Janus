#!/usr/bin/env python3
"""Step33h independent nodal finite-difference PB reproducibility control."""
from __future__ import annotations
import hashlib,json,os,pathlib,subprocess,sys,time
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parents[1]
SOURCES=(
 'numerics/hr_independent_collocation_bracket.py',
 'tests/test_hr_independent_collocation_bracket.py',
 'scripts/verify_gate2b_step33h.py',
)

def main():
    out=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'gate2b-step33h-report.json')
    manifest=[]
    for p in SOURCES:
        raw=(ROOT/p).read_bytes()
        git=subprocess.run(['git','hash-object','--stdin'],input=raw,capture_output=True,check=True).stdout.decode().strip()
        manifest.append({'path':p,'sha256':hashlib.sha256(raw).hexdigest(),
                         'git_blob':git,'bytes':len(raw)})
    env={**os.environ,'OPENBLAS_NUM_THREADS':'1','PYTHONPATH':str(ROOT),
         'PYTEST_DISABLE_PLUGIN_AUTOLOAD':'1'}
    start=time.monotonic()
    ps=subprocess.run([sys.executable,'-m','pytest','-q',
        'tests/test_hr_independent_collocation_bracket.py'],cwd=ROOT,
        env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,
        timeout=75)
    from numerics import hr_independent_collocation_bracket as v
    nums=[]
    for n in (16,26,40):
        w=v.witness(n)
        nums.append(dict(n=n,bracket=w['bracket'],primary_residual=w['primary_residual'],
                         pg_min=w['minimum_pg'],pf_min=w['minimum_pf'],
                         six_pair_contributions=w['pairs'].tolist()))
    x,w,D=v.grid(32);q=v.curved_primary_arrays(x,D)
    N=v.smear(x);M=v.smear(x,kind='M')
    b1,_=v.bracket(q,D,w,N,M);b2,_=v.bracket(q,D,w,M,N)
    off={k:a.copy() for k,a in q.items()};off['pg']+=.02*x*x
    b3,_=v.bracket(off,D,w,N,M);b4,_=v.bracket(off,D,w,M,N)
    localized=[]
    for n,width in ((80,.03),(128,.015)):
        x,w,D=v.grid(n);q=v.curved_primary_arrays(x,D)
        shape=v.smear(x)*np.exp(-((x-.43)/width)**2)
        B,_=v.bracket(q,D,w,shape,shape)
        localized.append({'n':n,'width':width,'bracket_over_norm':B/float(w@(shape*shape))})
    success=ps.returncode==0 and '21 passed' in ps.stdout and all(i['primary_residual']<1e-12 for i in nums)
    result={
      'step':'33h','date':'2026-10-20','branch':'research/gate2b-nonhomothetic-transfer',
      'execution':'independent nodal Gauss-Legendre finite-difference Poisson gradients',
      'test_result':ps.stdout[-2500:],'test_exit':ps.returncode,'new_tests_passed':21 if success else None,
      'test_run_seconds':round(time.monotonic()-start,2),
      'spatial_resolution_controls':nums,
      'primary_smear_swap_difference':b1-b2,
      'off_primary_smear_swap_difference':b3-b4,
      'localized_coefficients':localized,
      'sources':manifest,
      'previous_step33g_reference_git_blobs':{
       'numerics/hr_curved_moving_dust_primary.py':'4266227a3a09bad229cb1da583b9a77706ef1838',
       'numerics/hr_curved_primary_mixed_kernel.py':'45ccd73177cc1588efaf1d53e3dd0179d41ec30b',
      },
      'prior_step33g_22_plus_3_tests_rerun':False,
      'full_repository_regression':False,
      'primary_plus_secondary_surface_solving':'NOT_DERIVED',
      'full_Dirac_secondary_time_preservation':'NOT_DERIVED',
      'lapse_fixing':'NOT_DERIVED',
      'genuinely_nonhomothetic_time_evolved_Candidate_C':'NOT_DERIVED',
      'DeFelice_oracle':'NOT_RUN','Aoki_oracle':'NOT_RUN',
      'gate2b':'OPEN','JANUS_R_validated':False,
      'status':'PASS' if success else 'FAIL'
    }
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(f'Step33h: {result["status"]}; new tests=21; report={out}')
    print(ps.stdout[-800:])
    return 0 if success else 1

if __name__=='__main__':raise SystemExit(main())
