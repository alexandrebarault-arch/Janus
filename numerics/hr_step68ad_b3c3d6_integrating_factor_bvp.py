"""Exact integrating-factor reduction for a first-order lapse constraint.

A_N N + A_M M + B_N N' + B_M M' = 0, B_M != 0.
This is a CONDITIONAL mathematical lemma, not a Step58 evaluation.
"""
import json
import sympy as sp


def transform(AN, AM, BN, BM, r):
    """Return q,p,a,h in W=M+q*N, W'+p*W=h*N."""
    if sp.simplify(BM) == 0:
        raise ValueError('B_M identically zero: change chart')
    q, p, a = [sp.cancel(sp.sympify(x) / sp.sympify(BM)) for x in (BN, AM, AN)]
    h = sp.factor(sp.diff(q, r) + p*q - a)
    return q, p, a, h


def certificate():
    r, k = sp.symbols('r k', real=True, positive=True)
    N = sp.Function('N')(r)
    M = sp.Function('M')(r)
    AN, AM, BN, BM = [sp.Function(s)(r) for s in ('AN','AM','BN','BM')]
    q, p, a, h = transform(AN, AM, BN, BM, r)
    W = M + q*N
    original = AN*N + AM*M + BN*sp.diff(N,r) + BM*sp.diff(M,r)
    identity = sp.factor(sp.diff(W,r) + p*W - h*N - original/BM)
    R = sp.Rational(17,20)
    rho = sp.Rational(10371,20000)
    S, D = 1+rho, 1-rho
    phi = (r/R)**2
    Ng = sp.factor((S + D*(1-phi))/2)
    Mg = sp.factor((S - D*(1-phi))/2)
    kappa = sp.factor(2*D/(S*R**2))
    qb, pb, ab, hb = transform(0,0,1,-1,r)
    qg, pg, ag, hg = transform(kappa*r,kappa*r,1,-1,r)
    Wg = sp.factor(Mg + qg*Ng)
    checks = {
        'operator_identity': identity,
        'bad_q': qb+1, 'bad_p':pb, 'bad_h':hb,
        'good_q':qg+1, 'good_p_plus_kappa_r':pg+kappa*r,
        'good_h_minus_2kappa_r':hg-2*kappa*r,
        'good_solution_W_equation':sp.diff(Wg,r)+pg*Wg-hg*Ng,
        'good_center_difference':Wg.subs(r,0)+D,
        'good_outer_difference':Wg.subs(r,R),
        'good_original_operator':sp.diff(Ng,r)-sp.diff(Mg,r)+kappa*r*(Ng+Mg),
        'bad_integral_obstruction':sp.factor((rho-1) - (-D)),
        'variable_q_test':None,
    }
    # Independent polynomial check with nonconstant q, to catch missing q'.
    Nv=1+r*r; Mv=sp.Rational(1,2)+r*r/2
    BNv=2+r; BMv=sp.Integer(3); AMv=sp.Integer(0)
    ANv=sp.cancel(-(BNv*sp.diff(Nv,r)+BMv*sp.diff(Mv,r))/Nv)
    qv,pv,av,hv=transform(ANv,AMv,BNv,BMv,r)
    checks['variable_q_test']=sp.factor(sp.diff(Mv+qv*Nv,r)+pv*(Mv+qv*Nv)-hv*Nv)
    bad={key:str(sp.simplify(val)) for key,val in checks.items() if sp.simplify(val)!=0}
    if bad:raise AssertionError(bad)
    signs={'center_difference_positive':D>0,'kappa_positive':kappa>0,
           'good_N_positive_lower':S/2>0,'good_M_positive_lower':rho>0}
    if not all(signs.values()):raise AssertionError(signs)
    return {'step':'b3c3d6','scope':'CONDITIONAL_INTEGRATING_FACTOR_BVP_NOT_STEP58',
            'identity':'W=M+qN, q=B_N/B_M, p=A_M/B_M, a=A_N/B_M, h=qprime+p*q-a, Wprime+pW=hN',
            'endpoint_identity':'(1+q(R))*N(R)=exp(-P(R))*(M(0)+q(0)*N(0))+integral_0^R exp(-(P(R)-P(s)))*h(s)*N(s) ds, P(r)=integral_0^r p',
            'validity':'B_M nonzero on closed interval; C1 coefficients; N,M C1; endpoint M(R)=N(R)',
            'center_caveat':'Step58 b3c2 B_N,B_M=O(r^4); cannot divide at r=0 without a separate limit or epsilon matching',
            'toy_bad':'q=-1,p=0,h=0 gives W(R)=W(0)=rho-1<0, contradicts W(R)=0',
            'toy_good':'q=-1,p=-kappa*r,h=2*kappa*r; exact positive even polynomial solution',
            'symbolic_zero_residuals':len(checks),'exact_sign_checks':len(signs),
            'original_step58_probe_executed':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))
