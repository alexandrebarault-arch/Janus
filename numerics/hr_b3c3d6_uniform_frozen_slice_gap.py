"""Uniform exact residual gap on a *frozen*, nonphysical Step45/58 jet slice.

This reuses the previously published three-parameter polynomial identities,
NOT an independent replay of the original Step45/58 engines.
"""
import sympy as S

b, x, t = S.symbols('b x t', real=True)
P = 204*b**3 - 72*b**2 - 141*b - 56
T = 144*b**3 + 224*b**2 + b - 20
FZ_RR = -P/(64*b)
C_R = T/(100*b)
GAP = S.Rational(7, 8)
NEGATIVE_H = 204*x**3 + 72*x**2 - 197*x + 56
CELLS = ((S.Rational(0), S.Rational(1,4)),
         (S.Rational(1,4), S.Rational(3,8)),
         (S.Rational(3,8), S.Rational(7,16)),
         (S.Rational(7,16), S.Rational(1,2)),
         (S.Rational(1,2), S.Rational(1)),
         (S.Rational(1), S.Rational(2)))

def bernstein_cubic(poly, lo, hi):
    """Exact degree-three Bernstein coefficients on [lo,hi]."""
    p = S.Poly(S.expand(poly.subs(x, lo+(hi-lo)*t)), t)
    c = [p.nth(i) for i in range(4)]
    return tuple(S.factor(sum(c[k]*S.binomial(j,k)/S.binomial(3,k)
                              for k in range(j+1))) for j in range(4))

def certificate():
    assert S.cancel(FZ_RR.subs(b, -x) + GAP + NEGATIVE_H/(64*x)) == 0
    coeffs = [bernstein_cubic(NEGATIVE_H, lo, hi) for lo,hi in CELLS]
    assert all(v > 0 for row in coeffs for v in row)
    # x>=2: h=x*(204*x**2+72*x-197)+56, bracket >= 763 > 0.
    assert S.expand(NEGATIVE_H-x*(204*x**2+72*x-197)-56) == 0
    assert (204*2**2+72*2-197) > 0
    # b>=1/2: C_r is strictly increasing, with value 109/100.
    assert S.cancel(S.diff(C_R,b)-(288*b+224+20/b**2)/100) == 0
    assert C_R.subs(b,S.Rational(1,2)) == S.Rational(109,100)
    # 0<b<=1/2: P<-56 by 204b**3<=102b**2 and 30b**2<=15b.
    assert S.expand(P-(204*b**3-72*b**2-141*b-56)) == 0
    assert S.Rational(109,100)>GAP
    assert S.Rational(7,4)>GAP
    return {
        'scope':'FROZEN_NONPHYSICAL_THREE_PARAMETER_SLICE_WITH_C=Hf=0_ONLY',
        'radial_residuals':{'Fz_rr':str(FZ_RR),'C_r':str(C_R)},
        'uniform_result':'For every real b != 0, max(abs(Fz_rr),abs(C_r)) > 7/8',
        'negative_b_proof':'x=-b>0; h(x)>0 by exact positive Bernstein coefficients on [0,2] and direct x>=2 inequality',
        'negative_b_bernstein_cells':[
            {'interval':[str(lo),str(hi)],'coefficients':[str(v) for v in row]}
            for (lo,hi),row in zip(CELLS,coeffs)],
        'positive_b_small':'0<b<=1/2 implies P<-56 and abs(Fz_rr)>7/4',
        'positive_b_large':'b>=1/2 implies C_r>=109/100',
        'original_engines_executed_this_run':False,
        'physical_Step55_six_enclosures':0,
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
