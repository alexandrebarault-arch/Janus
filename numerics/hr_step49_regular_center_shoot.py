"""Step49 regular-center shooting for the ORIGINAL Step46 algebraic radial C ODE.

New point: from exact Step48 center-leading identity, P=pLf=r^2 U(s), s=r^2,
2*s*dU/ds=G(s,U)-2*U, G=F(sqrt(s),s*U)/sqrt(s),
G(0,U)=3*U0-U. Therefore the homogeneous indicial root is -3/2,
corresponding to an excluded P~C/r mode. If the nonsingular remainder
is analytic, Taylor matching yields U1=[partial_s G(0,U0)]/5.

This module ESTIMATES U1 by convergent binary64 sampling and integrates
from eps>0, never from the singular center itself. These are experiments,
not existence proofs or validated continuum interval bounds. The g-sector
and other source data remain prescribed, not dynamical 4D solutions.
"""
from __future__ import annotations
import math
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp
from .hr_step48_center_compatibility import center_relation,benchmark_center_gap
from .hr_step47_interior_ivp import source_data,compiled_rhs


def exact_indicial_data():
    e=center_relation()
    r,a,b,Pg,U,V,G,k,Z=e['variables']
    U0=e['necessary_Uf_0']
    assert sp.simplify(e['nearcenter_dP_over_r']-(3*U0-U))==0
    s=sp.symbols('s',positive=True)
    c=sp.symbols('C_homogeneous')
    homogeneous=c*s**sp.Rational(-3,2)
    assert sp.simplify(2*s*sp.diff(homogeneous,s)+3*homogeneous)==0
    u1,F1=sp.symbols('U1 F1')
    # 2s U_s = 3(U0-U)+s F1+O(s^2)
    coefficient=sp.factor(2*u1+3*u1-F1)
    assert sp.solve(coefficient,u1)==[F1/5]
    return {'U0':U0,'indicial_exponent_s':sp.Rational(-3,2),
            'homogeneous_U(s)':homogeneous,
            'homogeneous_pLf(r)':c/r,
            'first_even_coefficient_formula':F1/5,
            'scope':'conditional on analyticity of the regularized source remainder'}


def benchmark_u0():
    return benchmark_center_gap()['necessary_Uf_0']


def ode_rhs(r,p):
    _,rhs,_=compiled_rhs()
    values,_=source_data(float(r),float(p))
    v=float(rhs(*values))
    if not math.isfinite(v):raise ArithmeticError('nonfinite secondary ODE')
    return v


def finite_radius_F1(r=.008):
    """Finite-r estimator of F1=partial_s G(0,U0), not an exact limit."""
    if not 0<r<=.05:raise ValueError('choose an interior small positive radius')
    u0=benchmark_u0()
    return (ode_rhs(r,u0*r*r)/r-2*u0)/(r*r)


def estimate_u1(r=.008):
    """Cancel leading O(r^2) bias of F1(r) via Richardson, purely numeric."""
    f1_r=finite_radius_F1(r)
    f1_half=finite_radius_F1(r/2)
    return (4*f1_half-f1_r)/15  # F1(0)/5, NOT proof by extrapolation


def initial_pLf(eps,order=1,u1=None):
    if not (0<eps<=.05 and order in (0,1)):
        raise ValueError('regular-center cutoff and polynomial order required')
    if u1 is None:u1=estimate_u1()
    u0=benchmark_u0()
    return u0*eps*eps+(u1*eps**4 if order else 0.)


def solve_cutoff(eps=.01,order=1,*,stop=.85,rtol=2e-12,atol=1e-18,
                 max_step=.012,u1=None):
    if not (0<eps<stop<=.85 and 0<rtol<=1e-8 and 0<atol<=1e-12 and max_step>0):
        raise ValueError('unsupported numerical regular-center shooting controls')
    p0=initial_pLf(eps,order,u1)
    def v(r,x):return [ode_rhs(r,x[0])]
    sol=solve_ivp(v,(eps,stop),[p0],rtol=rtol,atol=atol,
                  max_step=max_step,dense_output=True)
    if not sol.success:raise ArithmeticError('failed center-to-interior IVP: '+sol.message)
    return sol


def sample_dust(sol,lo=.05,hi=.85,n=129):
    if not(isinstance(n,int) and 16<=n<=2001 and sol.t[0]<=lo<hi<=sol.t[-1]):
        raise ValueError('sample range outside numerical IVP')
    x=np.linspace(lo,hi,n)
    _,rhs,matter=compiled_rhs()
    pg=[];pf=[];c_res=[]
    for r in x:
        values,background=source_data(float(r),float(sol.sol(r)[0]))
        v=float(rhs(*values))
        p_f,p_s_f,c_val=map(float,matter(*values,v))
        pg.append(float(background['pg'])/r**2)
        pf.append(p_f/r**2)
        c_res.append(abs(c_val))
    return {'sample_count':n,
            'min_pg_over_r2_sample':min(pg),
            'min_pf_over_r2_sample':min(pf),
            'max_abs_analytic_C_substitution':max(c_res),
            'NOT_CONTINUOUS_CERTIFICATION':True}


def center_shooting_study(cutoffs=(.05,.025,.0125,.00625),reference_eps=.001):
    if any(e<=reference_eps for e in cutoffs) or not all(cutoffs[i]>cutoffs[i+1]
                                        for i in range(len(cutoffs)-1)):
        raise ValueError('cutoffs strictly decreasing above reference')
    u1=estimate_u1()
    baseline=solve_cutoff(reference_eps,1,u1=u1)
    target=float(baseline.sol(.85)[0])
    rows=[]
    for eps in cutoffs:
        old=solve_cutoff(eps,0,u1=u1)
        new=solve_cutoff(eps,1,u1=u1)
        rows.append({'eps':eps,
                     'order0_endpoint':float(old.sol(.85)[0]),
                     'order1_endpoint':float(new.sol(.85)[0]),
                     'order0_abs_delta_from_reference':abs(float(old.sol(.85)[0])-target),
                     'order1_abs_delta_from_reference':abs(float(new.sol(.85)[0])-target),
                     'order1_nfev':int(new.nfev)})
    return {'step':49,'benchmark_u0':benchmark_u0(),'u1_numerical_estimate':u1,
            'u1_estimate_r':.008,
            'reference_eps':reference_eps,'reference_order1_endpoint':target,
            'cutoff_results':rows,
            'positive_dust_sample':sample_dust(baseline),
            'indicial_exponent_s':str(exact_indicial_data()['indicial_exponent_s']),
            'NOT_PROVED':['analytic existence at center','certified uniform IVP error',
                          'continuous new-IVP dust positivity','Dirac time preservation',
                          'lapse fixing','full 4D on-shell evolution'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(center_shooting_study(),indent=2))
