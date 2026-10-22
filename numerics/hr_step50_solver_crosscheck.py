"""Step50 independent numerical integrator cross-check for center-outward C ODE.

Three qualitatively distinct SciPy ODE integrators solve the SAME original
Step46 symbolic primary-reduced radial equation: RK45, DOP853, and implicit
Radau. Dense sample comparisons at 2049 sites check solver sensitivity and
two dust signs. This is NOT a verified-interval ODE continuation, and the
small analytic C residual is a consequence of solving C algebraically.

Historical Step45/46/47 provider sources must be byte-checked separately.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp
from .hr_step49_regular_center_shoot import estimate_u1, initial_pLf, ode_rhs
from .hr_step47_interior_ivp import compiled_rhs, source_data

METHODS=('RK45','DOP853','Radau')


def crosscheck(*,eps=.00625,stop=.85,rtol=2e-11,atol=1e-17,
               max_step=.012,samples=2049,methods=METHODS):
    if not (0<eps<=.05 and eps<.01<stop<=.85 and 0<rtol<=1e-8
            and 0<atol<=1e-12 and 0<max_step<=.1):
        raise ValueError('invalid interior regular-center IVP controls')
    if not isinstance(samples,int) or samples<129 or samples>8193:
        raise ValueError('invalid number of validation sites')
    if not isinstance(methods,(list,tuple)) or not methods or len(set(methods))!=len(methods) or any(m not in METHODS for m in methods):
        raise ValueError('allowed distinct integrators: RK45/DOP853/Radau')
    u1=estimate_u1()
    p0=initial_pLf(eps,order=1,u1=u1)
    x=np.linspace(.01,stop,samples)
    syms,rhs,matter=compiled_rhs()
    traces={}
    for method in methods:
        sol=solve_ivp(lambda r,y:[ode_rhs(r,float(y[0]))],(eps,stop),[p0],
                      method=method,rtol=rtol,atol=atol,max_step=max_step,
                      dense_output=True)
        if not sol.success:
            raise ArithmeticError(f'{method} did not reach endpoint: {sol.message}')
        moments=np.asarray(sol.sol(x)[0],float)
        if not np.isfinite(moments).all():
            raise ArithmeticError(f'{method}: nonfinite momentum samples')
        minimum_pg=math.inf; minimum_pf=math.inf; maximum_substituted_C=0.
        for r,p in zip(x,moments):
            vals,fields=source_data(float(r),float(p))
            dp=float(rhs(*vals))
            pf,psf,C=map(float,matter(*vals,dp))
            if not all(map(math.isfinite,(dp,pf,psf,C))):
                raise ArithmeticError(f'{method}: nonfinite dust/secondary')
            minimum_pg=min(minimum_pg,fields['pg']/r**2)
            minimum_pf=min(minimum_pf,pf/r**2)
            maximum_substituted_C=max(maximum_substituted_C,abs(C))
        traces[method]={'success':True,'nfev':int(sol.nfev),
                        'endpoint_pLf':float(sol.y[0,-1]),
                        'min_sampled_pg_div_r2':float(minimum_pg),
                        'min_sampled_pf_div_r2':float(minimum_pf),
                        'max_sampled_C_by_construction':float(maximum_substituted_C),
                        '_sampled_momentum':moments}
    ref=traces[methods[0]]['_sampled_momentum']
    deviations={m:float(np.max(np.abs(v['_sampled_momentum']-ref)))
                for m,v in traces.items()}
    for v in traces.values():v.pop('_sampled_momentum')
    return {'step':50,'experiment':'independent SciPy RK45 DOP853 Radau near-center outward numerical shooting',
            'eps':float(eps),'stop':float(stop),'u1_estimate_not_certified':float(u1),
            'pLf_start':float(p0),'n_validation_sites':samples,
            'relative_tolerance':rtol,'absolute_tolerance':atol,
            'max_step':max_step,'integrators':traces,
            'max_abs_pLf_against_first_method':deviations,
            'main_scope':'cross-integrator numerical sensitivity, not rigorous error enclosure',
            'not_proved':['historical source byte-authentic step45/46/47 full regression',
                          'global exact secondary solution',
                          'continuous dust positivity between sampling sites',
                          'regular global 4D time evolution',
                          'Dirac secondary time preservation and lapse fixing'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(crosscheck(),indent=2))
