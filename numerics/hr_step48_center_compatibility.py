"""Exact Frobenius leading coefficient of the physical secondary at spherical center.

Uses Step45 ORIGINAL six-canonical-pair algebra. For the smooth conformally
flat local leading metric and regular spherical momenta pLi=r² Ui,
pSi=r Vi, it derives the coefficient of r² in C=K00-(K01)'.
The f radial primary fixes V_f=2 U_f at leading order, producing a
NECESSARY center compatibility equation for U_f(0). It is not a
global existence proof or proof of Dirac time preservation.
"""
from functools import lru_cache
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward


@lru_cache(maxsize=1)
def center_relation():
    d=exact_physical_ward()
    q=dict(zip(d['Q'],d['q']))
    qr=dict(zip(d['Q'],d['dq']))
    r,a,b,Pg,U,V,G,k,Z=sp.symbols('r a b Pg U V G k Z',real=True)
    leading={
        q['Lg']:a,q['Lf']:b,q['Sg']:a*r,q['Sf']:b*r,
        q['pLg']:Pg*r**2,q['pLf']:U*r**2,
        q['pSg']:2*Pg*r,q['pSf']:V*r,
        q['pg']:G*r**2,
        qr['Lg']:0,qr['Lf']:0,qr['Sg']:a,qr['Sf']:b,
        qr['pLg']:2*Pg*r,qr['tg']:k*a*r,
        d['parameters'][-3]:Z*r,d['parameters'][-2]:Z,
    }
    first=sp.factor(sp.limit(d['C_exact'].subs(leading)/r**2,r,0))
    mg,mf,m2,b0,b1,b2,b3,b4=d['parameters'][:8]
    A=a*a*b1+2*a*b*b2+b*b*b3
    expected=-m2*A*(6*mf*mg*Z*a*b-3*mf*Pg*b+mg*a*(U+V))/(2*mf*a*b)
    if sp.simplify(first-expected)!=0:
        raise AssertionError('wrong centre coefficient of physical C')
    # D_f=-D_g and pSf=(Df+Lf pLf'-pf theta_f')/Sf'.
    # D_f=O(r^3), p_f theta_f'=O(r^3) at a smooth two-dust centre,
    # so pSf/r -> 2 U_f when pLf=r² U_f(r²).
    constrained=sp.factor(first.subs(V,2*U))
    U0=mf*b*(Pg/(mg*a)-2*Z)
    if sp.cancel(constrained.subs(U,U0))!=0:
        raise AssertionError('regular centre U0 incompatible with C')
    slope=sp.factor(sp.diff(constrained,U))
    V_rhs=sp.solve(first,V)[0]
    if sp.simplify(V_rhs-(3*U0-U))!=0:
        raise AssertionError('regular-singular V equation incorrect')
    Csing=sp.Symbol('C_singular_mode')
    P=U0*r**2+Csing/r
    if sp.cancel(sp.diff(P,r)+P/r-3*U0*r)!=0:
        raise AssertionError('near-centre 1/r mode invalid')
    if slope==0:
        raise AssertionError('no nondegenerate center condition')
    return {'C_over_r2_leading':first,'C_over_r2_after_f_primary':constrained,
            'necessary_Uf_0':U0,'C_center_U_coefficient':slope,
            'nearcenter_dP_over_r':V_rhs,
            'formal_regular_singular_solution':P,
            'shift_correction_to_baseline_Pf':-2*mf*b*Z,
            'variables':(r,a,b,Pg,U,V,G,k,Z),
            'parameters':(mg,mf,m2,b0,b1,b2,b3,b4)}


def benchmark_center_gap():
    """Numeric illustration only, not a rigorous constraint certificate."""
    import math
    a=.4;y=.5787707228025044;b=a*y;z=.004
    mf=.10879548725**2;mg=1.;m2=23.3348939346
    b0,b1,b2,b3,b4=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)
    H=math.sqrt(.9/(3*a**3)+m2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3)
    Pg=-2*a*a*H
    necessary=mf*b*(Pg/(mg*a)-2*z)
    frozen=-2*mf*b*a*H-2.1921905214999423e-5
    return {'necessary_Uf_0':necessary,'old_frozen_Uf_0':frozen,
            'old_minus_necessary':frozen-necessary,
            'remark':'Near agreement of ~3.2e-15 does not prove a smooth global extension'}


if __name__=='__main__':
    import json
    d=center_relation()
    print(json.dumps({'step':48,'center_Uf_0_symbolic':str(d['necessary_Uf_0']),
        'C_over_r2_symbolic':str(d['C_over_r2_after_f_primary']),
        'numerical_benchmark':benchmark_center_gap(),
        'regular_global_center':'NOT_PROVED','GATE_2B':'OPEN',
        'JANUS_R':'NOT_VALIDATED'},indent=2))
