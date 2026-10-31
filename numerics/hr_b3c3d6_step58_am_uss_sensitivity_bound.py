"""Exact rational physical bounds on Step58 d(A_M)/d(U_ss) on Step55.

Uses the previously derived ORIGINAL Step58 sensitivity identity; does not
execute the original engine or enclose A_M itself. The global U bounds are
conditional on the previously certified Step55 256-cell barrier.
"""
from fractions import Fraction as F

A = F('0.4')
B = A * F('.5787707228025044')
CG, CF = F('.0015'), F('-.0012')
Z1, KF = F('.004'), F('-.0016')
M2, MG, MF = F('23.3348939346'), F(1), F('.10879548725')**2
B1, B2, B3 = F(1), F('-4.2383993109'), F('13.6801214252')
S = F(289, 400)
U_GLOBAL_LO, U_GLOBAL_HI = -F(67, 12500), -F(229, 50000)
RADII = (F(1,4), F(1,2), F(7,10), F(17,20))
USS_BUDGETS_FROM_PREVIOUS_ARCHIVE = (F(1,10), F(1,160), F(1,590), F(1,1200))


def geometry(s):
    if not F(0) <= s <= S:
        raise ValueError('outside previously certified physical radial domain')
    lg = A*(1+CG*s)**2
    lf = B*(1+CF*s)**2
    sfr = B*(1+CF*s)*(1+5*CF*s)
    t = B1*lg**2+2*B2*lg*lf+B3*lf**2
    return lg, lf, sfr, t


def global_guards():
    """Prove T>1/10 and q<qmax using only rational endpoint bounds."""
    lglo, lghi = A, A*(1+CG*S)**2
    lflo, lfhi = B*(1+CF*S)**2, B
    sfrlo, sfrhi = B*(1+CF*S)*(1+5*CF*S), B
    tlo = B1*lglo**2+2*B2*lghi*lfhi+B3*lflo**2
    thi = B1*lghi**2+2*B2*lglo*lflo+B3*lfhi**2
    assert F(1,10)<tlo<=thi<F(1,9)
    assert 0<lflo<=lfhi and 0<sfrlo<=sfrhi
    assert U_GLOBAL_LO<U_GLOBAL_HI<0 and KF<0 and Z1**2*S<1
    qmax = S*U_GLOBAL_LO*KF/(2*MF*sfrlo)
    assert 0<qmax<F(1,500)
    return {'T_lo':tlo,'T_hi':thi,'qmax':qmax}


def sensitivity_magnitude_bounds(r):
    """Strict bounds lo < -dA_M/dU_ss < hi at exact physical radius.

    On Fz=Hg=0 original Step58: dA_M/dU_ss =
      -2 r^4 z sqrt(1-z²) K beta/(Lg Lf MF Sf Sfr den).
    On Step55, z=Z1*r, K=M2*MG*Lg*Lf*r²*T, Sf=r*Lf,
    beta=sqrt(1+KF²*r²), den=beta+r²*U*KF/(2*MF*Sfr).
    Thus the magnitude equals C(r)*sqrt(1-Z1²*s)/(1+q), where
    C=2*Z1*M2*MG*r^6*T/(MF*Lf*Sfr), 0<q<qmax(s).
    sqrt(1-x)>1-x for 0<x<1 and beta>=1 give rational bounds.
    """
    r=F(r)
    if not 0<r<=F(17,20):
        raise ValueError('requires strictly positive exact radius')
    global_guards()
    s=r*r
    _,lf,sfr,t=geometry(s)
    assert t>0 and sfr>0
    c=2*Z1*M2*MG*r**6*t/(MF*lf*sfr)
    qmax=s*U_GLOBAL_LO*KF/(2*MF*sfr)
    assert qmax>0
    lo=c*(1-Z1**2*s)/(1+qmax)
    assert 0<lo<c
    return lo,c


def four_point_budgets():
    """U_ss input limits are PREVIOUS certified archive bounds, not replayed."""
    thresholds=(F(1,1000),F(1,300),F(1,150),F(1,100))
    out=[]
    for r,uss,threshold in zip(RADII,USS_BUDGETS_FROM_PREVIOUS_ARCHIVE,thresholds):
        lo,hi=sensitivity_magnitude_bounds(r)
        assert hi*uss<threshold
        out.append({'r':str(r),'minus_dAM_dUss_strict':(str(lo),str(hi)),
                    'conditional_abs_AM_Uss_contribution_less_than':str(threshold)})
    return out

if __name__=='__main__':
    import json
    print(json.dumps({'scope':'STEP58_SENSITIVITY_ONLY_NOT_A_M_ENCLOSURE',
                      'four_radii':four_point_budgets(),
                      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'},indent=2))
