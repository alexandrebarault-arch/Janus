"""Exact local C=0 ODE for f radial gravitational momentum on primary data.

Start from the symbolic ORIGINAL six-pair spherical mixed Poisson bracket
(C=K00-(K01)') and solve both f-dust lapse and radial momentum primaries
ALGEBRAICALLY. The remaining local C is AFFINE in V=pLf'(r), with a
provably nonvanishing coefficient on the regular positive-dust, J>0 chart.
It gives a local first-order equation V=F(r,pLf,other prescribed fields).
Global solution, spherical-centre regularity, coupled g evolution and
Dirac time preservation are NOT established by this reduction.
"""
from functools import lru_cache
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward


@lru_cache(maxsize=1)
def exact_f_momentum_ode():
    data=exact_physical_ward()
    q=dict(zip(data['Q'],data['q']))
    dq=dict(zip(data['Q'],data['dq']))
    Lf=q['Lf'];Sf=q['Sf'];Sg=q['Sg'];plf=q['pLf'];psf=q['pSf']
    Sfr=dq['Sf'];tfr=dq['tf'];z=data['parameters'][-3]
    mg,mf,m2,b0,b1,b2,b3,b4=data['parameters'][:8]
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    root=sp.sqrt(1-z*z)
    v=sp.Symbol('V_pLf_prime')
    Dg,Wf,R3f=sp.symbols('Dg_original Wf_original R3f_original')
    fac=plf/(2*mf*Sf*Sfr)
    beta=sp.sqrt(1+tfr**2/Lf**2)
    denom=beta+fac*tfr
    kinetic=Lf*plf**2/(4*mf*Sf**2)
    curvature=-mf*Lf*Sf**2*R3f/2
    # f unsmeared lapse Hf=0 after eliminating f radial momentum pSf.
    # The shift term z*Dg/Lf has its ORIGINAL sign, Fz=0 separately.
    pf=-(kinetic-fac*(-Dg+Lf*v)+curvature+z*Dg/Lf+Wf)/denom
    pSf=(-Dg+Lf*v-pf*tfr)/Sfr
    expression=sp.cancel(sp.together(data['C_exact'].subs(psf,pSf)))
    coefficient=sp.cancel(sp.diff(expression,v))
    expected=-m2*mg*At*root/(2*mf*Sf)*Lf*beta/(Sfr*denom)
    c0=sp.cancel(expression.subs(v,0))
    rhs=-c0/coefficient
    checks={
        'primary_substitution_linear_in_pLf_prime':sp.cancel(sp.diff(expression,v,2)),
        'affine_coefficient_exact_factorization':sp.cancel(sp.together(coefficient-expected)),
        'exact_C_restored_after_ODE_substitution':sp.cancel(sp.together(expression.subs(v,rhs))),
        'C_partial_pSf_exact':sp.cancel(sp.together(sp.diff(data['C_exact'],psf)+m2*mg*At*root/(2*mf*Sf))),
        'coefficient_independent_of_pLf_prime':sp.diff(coefficient,v),
    }
    return {'equation':expression,'coefficient':coefficient,
            'coefficient_factored':expected,'constant':c0,'pLf_prime_rhs':rhs,
            'p_f':pf,'pS_f':pSf,'V':v,'original_primary_f_shift':Dg,
            'original_primary_f_potential':Wf,'original_R3f':R3f,
            'f_dust_beta':beta,'f_dust_denominator':denom,'At':At,
            'symbols':{'q':q,'dq':dq,'params':data['parameters']},
            'identity_residuals':checks}


def exact_ode_certificate():
    out=exact_f_momentum_ode()
    bad={k:str(v) for k,v in out['identity_residuals'].items() if v!=0}
    if bad:raise AssertionError(f'exact primary-reduced C ODE failed: {bad}')
    if out['coefficient_factored']==0:raise AssertionError('ODE coefficient must not vanish identically')
    return {'step':46,'symbolic_C_affine_in_pLf_prime':'EXACT',
            'ODE_on_regular_chart':'pLf_prime=-C0/C1 with C1= -(m2 Mg2 At sqrt(1-z²)/(2 Mf2 Sf))*Lf beta_f/(Sf_prime dust_denom_f)',
            'coefficient_nonzero_conditions':'m2,Mg2,Mf2,Lf,Sf,Sf_prime,At,beta_f,dust_denom_f positive; |z|<1; r>0',
            'proof_scope':'fixed original spherical two-dust constrained primary ansatz and external algebraic shift Fz=0; ordinary local IVP away from r=0',
            'global_center_regular_C_solution':'NOT_PROVED',
            'full_Dirac_time_preservation':'NOT_DERIVED',
            'lapse_fixing':'NOT_DERIVED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(exact_ode_certificate(),indent=2))
