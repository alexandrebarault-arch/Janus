"""Experimental initial-value continuation of the exact C=0 spherical ODE.

Numerically integrate on 0.05<=r<=0.85, with all prescribed g-sector,
metric and dust phase profiles fixed to the rationalized Step41 benchmark.
At every RHS evaluation f lapse and radial primaries are solved algebraically,
then the analytically derived C is solved for pLf'. No spatial finite-h
secondary difference is used. This is a finite-error NUMERICAL example,
not a rigorous globally regular Einstein/Dirac solution or ghost test.
"""
from functools import lru_cache
from fractions import Fraction as F
from scipy.integrate import solve_ivp
import numpy as np
import sympy as sp
from .hr_step45_secondary_point_certificate import frozen_primary_at
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode

BETA=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
MG2=1.; MF2=.10879548725**2; M2=23.3348939346
A=.4; Y=.5787707228025044; B=A*Y; CF=-.0012; CG=.0015


@lru_cache(maxsize=1)
def compiled_rhs():
    s=exact_f_momentum_ode();v=s['V']
    all_sym=sorted(set().union(*(x.free_symbols for x in
       (s['pLf_prime_rhs'],s['p_f'],s['pS_f'],s['equation']))) - {v},key=str)
    rhs=sp.lambdify(all_sym,s['pLf_prime_rhs'],'numpy',cse=True)
    matter=sp.lambdify(all_sym+[v],[s['p_f'],s['pS_f'],s['equation']],'numpy',cse=True)
    return all_sym,rhs,matter


def source_data(r,P):
    """Independent spherical primary data for an arbitrary current pLf(r)."""
    q={k:float((v.lo+v.hi)/2) for k,v in frozen_primary_at(F(str(float(r)))).items()}
    q['pLf']=float(P)
    Sg,Sf,Lg,Lf,z=q['Sg'],q['Sf'],q['Lg'],q['Lf'],q['z']
    b0,b1,b2,b3,b4=BETA
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    root=np.sqrt(1-z*z)
    q['Dg_original']=M2*MG2*Lg*Lf*At*z/root
    q['Wf_original']=M2*MG2*(Lf*Af+Lg*At*root)
    q['Wg_original']=M2*MG2*(Lg*A0+Lf*At*root)
    q['R3f_original']=-48*CF/(B**2*(1+CF*r*r)**5)
    q['R3g_original']=-48*CG/(A**2*(1+CG*r*r)**5)
    q['At_original']=At
    syms,_,_=compiled_rhs()
    return [q[str(sym)] for sym in syms],q


def local_diagnostics(r,P):
    inputs,q=source_data(r,P)
    syms,rhs,matter=compiled_rhs()
    V=float(rhs(*inputs))
    pf,psf,c_resid=map(float,matter(*inputs,V))
    q['pf']=pf;q['pSf']=psf;q['pLf_prime']=V
    Lg,plg,Sg,psg,pg,Lf,plf,Sf=q['Lg'],q['pLg'],q['Sg'],q['pSg'],q['pg'],q['Lf'],q['pLf'],q['Sf']
    z=q['z'];Dg=q['Dg_original']
    Cg=(Lg*plg**2/(4*MG2*Sg**2)-plg*psg/(2*MG2*Sg)
        -MG2*Lg*Sg**2*q['R3g_original']/2+pg*np.sqrt(1+(q['tgr']/Lg)**2))
    Cf=(Lf*plf**2/(4*MF2*Sf**2)-plf*psf/(2*MF2*Sf)
        -MF2*Lf*Sf**2*q['R3f_original']/2+pf*np.sqrt(1+(q['tfr']/Lf)**2))
    Hg=Cg+z*Dg/Lg+q['Wg_original']
    Hf=Cf+z*Dg/Lf+q['Wf_original']
    Dg_nodal=psg*q['Sgr']-Lg*q['pLgr']+pg*q['tgr']
    Df_nodal=psf*q['Sfr']-Lf*V+pf*q['tfr']
    Fz=Dg_nodal-q['At_original']*M2*MG2*Lg*Lf*z/np.sqrt(1-z*z)
    old=frozen_primary_at(F(str(float(r))))['pLf']
    return {'r':float(r),'pLf':float(P),'pLf_prime_analytic':V,
        'original_frozen_pLf':float((old.lo+old.hi)/2),
        'pf_over_r2':pf/r**2,'pg_over_r2':pg/r**2,
        'C_analytic_substitution':float(c_resid),
        'Hg_original':float(Hg),'Hf_original':float(Hf),
        'Ddiag_original':float(Dg_nodal+Df_nodal),
        'Fz_original':float(Fz)}


def integrate_interior(*,start=.05,stop=.85,rtol=1e-10,atol=1e-14,max_step=.02):
    if not (.025<start<stop<=.85 and 0<rtol<=1e-6 and 0<atol<=1e-10):
        raise ValueError('validated interior chart and precision only')
    p0=frozen_primary_at(F(str(float(start))))['pLf']
    initial=float((p0.lo+p0.hi)/2)
    _,rhs,_=compiled_rhs()
    def ode(r,y):
        inputs,_=source_data(r,y[0]);return [float(rhs(*inputs))]
    sol=solve_ivp(ode,(start,stop),[initial],rtol=rtol,atol=atol,
                  dense_output=True,max_step=max_step)
    if not sol.success:raise ArithmeticError(f'ODE integration failed: {sol.message}')
    rr=np.linspace(start,stop,33)
    records=[local_diagnostics(float(r),float(sol.sol(r)[0])) for r in rr]
    maxima={k:max(abs(p[k]) for p in records) for k in
       ('C_analytic_substitution','Hg_original','Hf_original','Ddiag_original','Fz_original')}
    out={'step':47,'mode':'NUMERICAL_INTERIOR_IVP_NOT_GLOBAL_EXACT_OR_DIRAC',
         'r_interval':[start,stop],'relative_tolerance':rtol,'absolute_tolerance':atol,
         'nfev':sol.nfev,'pLf_initial':initial,'pLf_final':float(sol.y[0,-1]),
         'min_pf_over_r2':min(p['pf_over_r2'] for p in records),
         'min_pg_over_r2':min(p['pg_over_r2'] for p in records),
         'max_residuals':maxima,'samples':records,
         'limitations':['finite tolerance numeric integration','center r=0 not reached',
          'independent action test uses analytically reconstructed original densities, not full unreduced external solver',
          'not a proof of 4D evolution, Dirac time preservation, lapse fixing or ghost freedom'],
         'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    return out


if __name__=='__main__':
    import json
    report=integrate_interior()
    print(json.dumps({k:v for k,v in report.items() if k!='samples'},indent=2))
