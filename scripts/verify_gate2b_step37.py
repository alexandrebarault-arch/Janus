"""Reproduce Step37 curved two-dust near-secondary collocation and non-IBP PB.

Run from a full JANUS repository checkout: PYTHONPATH=. OPENBLAS_NUM_THREADS=1
python scripts/verify_gate2b_step37.py research/reports/gate2b-step37-report.json
No implied time evolution/Dirac BD proof. This script does NOT run GitHub CI.
"""
import hashlib,json,pathlib,sys
from numerics.hr_curved_moving_dust_primary import build_primary
from numerics.hr_step37_curved_solver import solve_even_center,local_candidate
from numerics.hr_step37_original_nonibp_oracle import original_pb


def digest(path):
    p=pathlib.Path(path)
    b=p.read_bytes()
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def main():
    r=solve_even_center(scale=.1,degree=4,iterations=5,h=.001)
    k=r['history'][-1]['f_delta']
    def case(**kwargs):
        return build_primary(curv_g=.0015,curv_f=-.0012,
            z_slope=.004,theta_g=.0012,theta_f=-.0016,
            grav_g=0.,grav_f=0.,**kwargs)
    base=case()
    corrected=case(f_delta=tuple(k))
    independent=[{'n':n, 'before':original_pb(base,n=n),
                   'after':original_pb(corrected,n=n)}
                 for n in (81,161,321,641)]
    fixed_stencils=[{'r':q,'C_h1e3':local_candidate(corrected,q,.001)[0],
                     'C_h5e4':local_candidate(corrected,q,.0005)[0]}
                    for q in (.04,.1,.2,.43,.7,.83)]
    files=['numerics/hr_curved_moving_dust_primary.py',
           'numerics/hr_curved_primary_mixed_kernel.py',
           'numerics/hr_step37_curved_solver.py',
           'numerics/hr_step37_original_nonibp_oracle.py',
           'tests/test_hr_step37_curved_solver.py']
    out={'step':'37','date':'2026-10-20','branch':'research/gate2b-nonhomothetic-transfer',
         'phase_space':'two positive canonical dust pairs; curved noncomoving spherical ADM',
         'solver':r,'original_nonibp_nodal_finite_variation':independent,
         'derivative_stencils':fixed_stencils,
         'git_blob_shas':{p:digest(p) for p in files if pathlib.Path(p).exists()},
         'full_repository_regression':False,'github_actions':False,
         'continuous_secondary_exactly_zero':False,
         'BD_Dirac_preservation':'NOT_COMPUTED','lapse_fixing':'NOT_COMPUTED',
         'on_shell_nonhomothetic':'NOT_COMPUTED',
         'same_action_DeFelice_Aoki':'NOT_COMPUTED',
         'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    steps=r['history']
    assert steps[0]['max_C']>.7 and steps[-1]['max_C']<2e-7
    assert steps[-1]['max_primary']<1e-12 and steps[-1]['min_pf']>0
    assert abs(independent[-1]['after']['bracket'])<5e-8
    p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'step37-report.json')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2)+'\n')
    print('STEP37 RESTRICTED COLLOCATION GREEN / FULL DIRAC OPEN',p)
    print('C_max: %.9g -> %.9g' %(steps[0]['max_C'],steps[-1]['max_C']))
    print('PB_nonIBP n641: %.9g -> %.9g' %(independent[-1]['before']['bracket'],independent[-1]['after']['bracket']))
    return 0


if __name__=='__main__':raise SystemExit(main())
