"""Exact necessary interval screen for a conditional two-lapse annular BVP.

This is NOT an evaluation of the physical Step58 coefficients.  It assumes
B_M != 0 on [epsilon,R] and the already established W'+p W=h N reduction.
"""
import sympy as sp


def screen_constant_p_q_h(epsilon, radius, p, q, h, w0, nlo, nhi, nr):
    """Exact rational constant-coefficient interval bounds, p=0 only.

    For p!=0 the full integrating factor is required; this intentionally
    narrow exact certificate never approximates exponential weights.
    """
    vals = tuple(map(sp.sympify, (epsilon, radius, p, q, h, w0, nlo, nhi, nr)))
    epsilon, radius, p, q, h, w0, nlo, nhi, nr = vals
    if p != 0:
        raise ValueError('p!=0: use exact exponential integrating factor')
    if not all(v.is_Rational for v in vals):
        raise ValueError('Rational inputs required for exact certificate')
    if not (0 < epsilon < radius and 0 < nlo <= nhi and nr > 0):
        raise ValueError('Invalid annulus or positive lapse bounds')
    length = radius - epsilon
    lower = sp.expand(w0 + length * h * (nlo if h >= 0 else nhi))
    upper = sp.expand(w0 + length * h * (nhi if h >= 0 else nlo))
    target = sp.expand((1 + q) * nr)
    return {'lower': lower, 'upper': upper, 'target': target,
            'excluded': bool(target < lower or target > upper),
            'status': 'NECESSARY_ONLY_NOT_SUFFICIENT_FOR_POSITIVE_M_OR_DIRAC'}


def exact_checks():
    e, R = sp.Rational(1,4), sp.Rational(17,20)
    bad = screen_constant_p_q_h(e,R,0,-1,-1,-sp.Rational(1,2),sp.Rational(1,2),2,1)
    good = screen_constant_p_q_h(e,R,0,-1,1,-sp.Rational(1,2),sp.Rational(1,2),2,sp.Rational(5,6))
    assert (bad['lower'],bad['upper'],bad['target']) == (sp.Rational(-17,10),sp.Rational(-4,5),0)
    assert bad['excluded'] and not good['excluded']
    assert (good['lower'],good['upper']) == (sp.Rational(-1,5),sp.Rational(7,10))
    r=sp.symbols('r',real=True)
    N=sp.Rational(5,6)
    M=sp.Rational(1,3)+N*(r-e)
    assert sp.simplify(sp.diff(M,r)-N)==0
    assert sp.simplify(M.subs(r,R)-N)==0
    assert sp.simplify(M.subs(r,e)-sp.Rational(1,3))==0
    assert M.subs(r,e)>0 and M.subs(r,R)>0
    # Sign-changing h=r-1/2: negative and positive areas are both 1/32.
    r=sp.symbols('r',real=True)
    neg=sp.integrate(r-sp.Rational(1,2),(r,sp.Rational(1,4),sp.Rational(1,2)))
    pos=sp.integrate(r-sp.Rational(1,2),(r,sp.Rational(1,2),sp.Rational(3,4)))
    assert (neg,pos)==(-sp.Rational(1,32),sp.Rational(1,32))
    assert 2*neg+pos == -sp.Rational(1,32)
    assert neg+2*pos == sp.Rational(1,32)
    return {'exact_assertions': 10, 'bad':{k:str(v) for k,v in bad.items()},
            'good':{k:str(v) for k,v in good.items()},
            'scope':'CONDITIONAL_ANNULAR_INTERVAL_NECESSARY_SCREEN_NOT_ORIGINAL_STEP58',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(exact_checks(),indent=2))
