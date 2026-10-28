"""Conditional positive-lapse reachability for ONE first-order temporal row.

NOT the original Step55/Step58 coefficient profile, Dirac preservation, or
an existence theorem at the degenerate center.  Works on an annulus with
B_N and B_M strictly positive and E_N=E_M=0 identically.
"""
from fractions import Fraction
import sympy as sp


def symbolic_certificate():
    a_n, a_m, b_n, b_m, k, kp, n = sp.symbols('A_N A_M B_N B_M k kp N')
    den = b_n + b_m * k
    h = (a_n + a_m*k + b_m*kp)/den
    nprime = -h*n
    mprime = kp*n + k*nprime
    residual = sp.factor(a_n*n + a_m*k*n + b_n*nprime + b_m*mprime)
    assert residual == 0
    assert sp.factor((mprime-k*nprime)/n-kp) == 0
    assert sp.factor(h*den-(a_n+a_m*k+b_m*kp)) == 0
    return {'algebraic_residuals_passed':3, 'generic_residual':str(residual)}


def exact_example():
    r = sp.symbols('r', real=True)
    r0, R = sp.Rational(1,4), sp.Rational(17,20)
    k0 = sp.Rational(10371,20000)
    slope = sp.factor((1-k0)/(R-r0))
    k = sp.factor(k0+slope*(r-r0))
    den = 2+3*k
    den0 = den.subs(r,r0)
    exponent = -sp.factor((5+9*slope)/(9*slope))
    n = sp.exp((r-r0)/3)*(den/den0)**exponent
    m = k*n
    dlogn = sp.Rational(1,3)+exponent*3*slope/den
    resid = sp.factor((1-k)+(2+3*k)*dlogn+3*slope)
    assert resid == 0
    assert sp.simplify(n.subs(r,r0)-1)==0
    assert sp.simplify(m.subs(r,r0)-k0)==0
    assert sp.simplify(k.subs(r,R)-1)==0
    assert slope>0 and k0>0 and den0>0 and den.subs(r,R)>0
    return {'r0':str(r0),'R':str(R),'k0':str(k0),'slope':str(slope),
            'kR':str(k.subs(r,R)),'den0':str(den0),
            'denR':str(den.subs(r,R)),'exponent':str(exponent),
            'exact_example_residuals_passed':5,
            'analytic_positive_on_closed_interval':True,
            'N_at_R_approx':str(sp.N(n.subs(r,R),18)),
            'M_at_R_approx':str(sp.N(m.subs(r,R),18))}


def certificate():
    return {'stage':'b3c3d6_PARTIAL','status':'CONDITIONAL_ANNULAR_RATIO_REACHABILITY_NOT_STEP55',
            'symbolic':symbolic_certificate(),'example':exact_example(),
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))
