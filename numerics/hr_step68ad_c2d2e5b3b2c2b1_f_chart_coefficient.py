"""Exact Step46 f-momentum ODE coefficient chart bound, conditional |U|<=1.

No original G or physical f solution is executed/certified here.
"""
from fractions import Fraction as Q
from math import comb
import json

S = Q(289, 400)
A = Q('0.4')
B = A * Q('0.5787707228025044')
MF = Q('0.10879548725') ** 2
M2 = Q('23.3348939346')
CG = Q('0.0015')
CF = Q('-0.0012')
KF = Q('-0.0016')
Z1 = Q('0.004')
BETA1, BETA2, BETA3 = Q(1), Q('-4.2383993109'), Q('13.6801214252')


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def add(*parts):
    out = [Q(0)] * max(map(len, parts))
    for part in parts:
        for i, x in enumerate(part):
            out[i] += x
    return out


def scale(a, x):
    return [v*x for v in a]


def bernstein_on_closed_interval(coeff, right):
    n = len(coeff)-1
    return [sum(coeff[i]*right**i*Q(comb(j,i), comb(n,i))
                for i in range(j+1)) for j in range(n+1)]


def certificate():
    lg = scale(mul([Q(1), CG], [Q(1), CG]), A)
    lf = scale(mul([Q(1), CF], [Q(1), CF]), B)
    t = add(scale(mul(lg, lg), BETA1),
            scale(mul(lg, lf), 2*BETA2),
            scale(mul(lf, lf), BETA3))
    bern = bernstein_on_closed_interval(t, S)
    tlo, thi = min(bern), max(bern)
    sfrlo = B*(1+CF*S)*(1+5*CF*S)
    sfrhi = B
    # Step46: beta_f+fac*t_f = sqrt(1+KF^2*s) + KF*s*U/(2*MF*Sfr).
    # For |U|<=1: beta>=1, beta<=1+KF^2*S; Sfr>=sfrlo.
    dmin = 1-S*abs(KF)/(2*MF*sfrlo)
    dmax = 1+KF**2*S+S*abs(KF)/(2*MF*sfrlo)
    rootlo = 1-S*Z1**2  # sqrt(1-Z1^2*s)>=1-Z1^2*s
    # Step46 C_V = -r*m2*Mg2*T*root*beta/(2*Mf2*Sfr*denom).
    cv_over_r_abs_lower = M2*tlo*rootlo/(2*MF*sfrhi*dmax)
    assert tlo > Q(1, 10) and thi < Q(11, 100)
    assert sfrlo > Q(23, 100) and sfrhi < Q(1, 4)
    assert dmin > Q(3, 4)
    assert rootlo > Q(999, 1000)
    assert cv_over_r_abs_lower > Q(372)
    return dict(scope='0<=s<=289/400; |U|<=1; Step46 regular chart; Mg2=1',
                source='original Step46 affine coefficient and Step55 geometry',
                T_bernstein=[str(v) for v in bern],
                T_lower=str(tlo), T_upper=str(thi),
                Sfr_lower=str(sfrlo), Sfr_upper=str(sfrhi),
                f_dust_denom_lower=str(dmin), f_dust_denom_upper=str(dmax),
                sqrt_1_minus_z2_lower=str(rootlo),
                minus_CV_over_r_lower=str(cv_over_r_abs_lower),
                conclusions=['T>1/10', 'T<11/100', 'f_dust_denom>3/4',
                             'C_V/r<-372 for r>0', 'J_temporal_not_computed',
                             'authentic_G_not_executed', 'f_dust_not_certified',
                             'GATE_2B_OPEN', 'JANUS_R_NOT_VALIDATED'])


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2, sort_keys=True, ensure_ascii=False))
