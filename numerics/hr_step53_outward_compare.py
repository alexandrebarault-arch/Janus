"""Numerical independent IVP check of exact quadratic-field U2 initial term.

The true original spherical primary equations are rebuilt at each radius,
while pLf' is the Step46 symbolic secondary RHS; C by construction is NOT
an independent full action/Dirac check. No continuum positivity certification.
"""
from __future__ import annotations
from functools import lru_cache
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode
from .hr_step53_exact_center_u2 import exact_u2,H2,rational_interval,F

A=.4;Y=.5787707228025044;B=A*Y;CG=.0015;CF=-.0012;KG=.0012;KF=-.0016
MG2=1.;MF2=.10879548725**2;M2=23.3348939346
BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)

@lru_cache(maxsize=1)
def compiled_rhs():
    expr=exact_f_momentum_ode()['pLf_prime_rhs'];symbols=sorted(expr.free_symbols,key=str)
    return symbols,sp.lambdify(symbols,expr,'numpy',cse=True)

def numerical_fields(r,P):
    a=A;b=B;s=r*r;g=1+CG*s;f=1+CF*s;Lg=a*g*g;Lf=b*f*f;Sg=r*Lg;Sf=r*Lf
    Lgr=4*a*CG*r*g;Lfr=4*b*CF*r*f;Sgr=a*g*(1+5*CG*s);Sfr=b*f*(1+5*CF*s)
    y=Y;b0,b1,b2,b3,b4=BETA
    H=math.sqrt(.9/(3*a**3)+M2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3)
    Pg=-2*a*a*H;plg=Pg*s*(1+2.5*CG*s);plgr=2*r*(1+5*CG*s)*Pg
    tg=KG*r*Lg;tf=KF*r*Lf;z=.004*r;root=math.sqrt(1-z*z)
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf;b0,b1,b2,b3,b4=BETA
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    Dg=M2*MG2*Lg*Lf*At*z/root
    Wg=M2*MG2*(Lg*A0+Lf*At*root);Wf=M2*MG2*(Lf*Af+Lg*At*root)
    Rg=-48*CG/(a*a*g**5);Rf=-48*CF/(b*b*f**5)
    fac=plg/(2*MG2*Sg*Sgr);kin=Lg*plg**2/(4*MG2*Sg*Sg)
    curvature=-MG2*Lg*Sg*Sg*Rg/2
    pg=-(kin-fac*(Dg+Lg*plgr)+curvature+z*Dg/Lg+Wg)/(math.sqrt(1+(tg/Lg)**2)+fac*tg)
    psg=(Dg+Lg*plgr-pg*tg)/Sgr
    fields={'Lg':Lg,'Lf':Lf,'Sg':Sg,'Sf':Sf,'pLg':plg,'pLf':P,'pSg':psg,
        'pg':pg,'Lgr':Lgr,'Lfr':Lfr,'Sgr':Sgr,'Sfr':Sfr,'pLgr':plgr,'tgr':tg,'tfr':tf,
        'Mg2':MG2,'Mf2':MF2,'m2':M2,'z':z,'zr':.004,'zrr':0.,'Dg_original':Dg,
        'Wf_original':Wf,'R3f_original':Rf,
        **{f'beta{i}':v for i,v in enumerate(BETA)}}
    return fields

def rhs(r,p):
    fields=numerical_fields(r,p);syms,fn=compiled_rhs()
    return float(fn(*[fields[str(s)] for s in syms]))

@lru_cache(maxsize=1)
def coeffs():
    from . import hr_step53_exact_center_u2 as source
    exact=source.exact_u2();h2=source.H2
    H=math.sqrt(float(h2))
    out=[]
    for n in ('U0','U1','U2'):
        q=exact[n]
        out.append(float(q.a)+float(q.b)*H)
    return tuple(out)

def solve_cutoff(eps=.05, degree=2,stop=.85,rtol=2e-12,atol=1e-18,max_step=.012):
    if degree not in (0,1,2) or not (0<eps<stop<=.85):raise ValueError('invalid cutoff/degree')
    u0,u1,u2=coeffs();p0=u0*eps*eps
    if degree>=1:p0+=u1*eps**4
    if degree>=2:p0+=u2*eps**6
    solution=solve_ivp(lambda r,y:[rhs(r,float(y[0]))],(eps,stop),[p0],
         method='DOP853',rtol=rtol,atol=atol,max_step=max_step,dense_output=True)
    if not solution.success:raise ArithmeticError(solution.message)
    return solution

def compare(cutoffs=(.05,.025,.0125,.00625),reference_eps=.001):
    reference=solve_cutoff(reference_eps,2)
    target=float(reference.y[0,-1]);rows=[]
    for eps in cutoffs:
        row={'eps':eps}
        for degree in (0,1,2):
            sol=solve_cutoff(eps,degree)
            row[f'degree{degree}_endpoint']=float(sol.y[0,-1])
            row[f'degree{degree}_abs_error_from_reference']=abs(float(sol.y[0,-1])-target)
        rows.append(row)
    return {'step':53,'reference_eps':reference_eps,'reference_endpoint':target,
            'coefficients':dict(zip(('U0','U1','U2'),coeffs())),'rows':rows,
            'qualifier':'NUMERICAL_OEDE_VALIDATION_NOT_RIGOROUS_GLOBAL_ERROR_BOUND',
            'center_regular_global_solution':'NOT_PROVED',
            'both_dust_continuum_signs':'NOT_CERTIFIED',
            'Dirac_time_preservation':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(compare(),indent=2))
