"""Exact conditional center Step58 affine-holonomic gap from certified Step68ad-B2.

No original physical engine is run here. The archived B2 U_ss continuum bounds
and original Step58 dA_M/dU_ss identity are imported as prior certificates.
The physical historical mixed affine already carries the ODE first jet;
'affine' here means a genuinely holonomic affine U(s) with U_ss=0.
"""
from fractions import Fraction as F

B2_ARCHIVE_BLOB = 'ac961b5b83667a83497497d22a701c24584cb561'
STEP58_ORIGINAL_BLOB = '802c23aebd41780d8c462f1aa1711707fe4ee88f'
SENSITIVITY_SOURCE_BLOB = 'd7530900082696d7b4fc6f1bd720010da71c37f0'
U_SS_LO = F('-1414170375015186192017477/69938619264706447051250697260')
U_SS_HI = F('-281308311835510868820846/14012170704330665327521777975')
A = F('0.4')
B = A * F('.5787707228025044')
CG, CF = F('.0015'), F('-.0012')
Z1, KF = F('.004'), F('-.0016')
M2, MF = F('23.3348939346'), F('.10879548725')**2
B1, B2, B3 = F(1), F('-4.2383993109'), F('13.6801214252')
S = F(1, 1024)


def global_center_bound(uss_lo=U_SS_LO, uss_hi=U_SS_HI):
    """Return rigorous lo,hi of (A_M(actual)-A_M(affine))/r**6.

    Valid for every 0<r<=1/32 on the historical Step55 shell, conditional
    on the archived B2 continuous U_ss bounds and Step55 U barrier.
    """
    if not uss_lo <= uss_hi < 0:
        raise ValueError('requires strictly negative certified U_ss interval')
    lg_lo, lg_hi = A, A*(1+CG*S)**2
    lf_lo, lf_hi = B*(1+CF*S)**2, B
    sfr_lo, sfr_hi = B*(1+CF*S)*(1+5*CF*S), B
    t_lo = B1*lg_lo**2 + 2*B2*lg_hi*lf_hi + B3*lf_lo**2
    t_hi = B1*lg_hi**2 + 2*B2*lg_lo*lf_lo + B3*lf_hi**2
    assert F(1,10) < t_lo <= t_hi < F(1,9)
    assert 0 < lf_lo <= lf_hi and 0 < sfr_lo <= sfr_hi
    q_max = S * (-F(67,12500)) * KF/(2*MF*sfr_lo)
    assert 0 < q_max < F(1,500)
    c_lo = 2*Z1*M2*t_lo/(MF*lf_hi*sfr_hi) * (1-Z1**2*S)/(1+q_max)
    c_hi = 2*Z1*M2*t_hi/(MF*lf_lo*sfr_lo)
    assert 0 < c_lo < c_hi
    # dA_M/dU_ss = -r**6*c, c in (c_lo,c_hi).
    # A_M(actual)-A_M(holonomic_affine) = U_ss*(-r**6*c) > 0.
    lo = (-uss_hi)*c_lo
    hi = (-uss_lo)*c_hi
    assert F(63,100000) < lo <= hi < F(13,20000)
    return lo, hi


def certify_at(r):
    r = F(r)
    if not 0 < r <= F(1,32):
        raise ValueError('outside certified B2 center domain 0<r<=1/32')
    lo,hi = global_center_bound()
    return {'r':str(r),
            'A_M_actual_minus_holonomic_affine_strict': [str(lo*r**6),str(hi*r**6)],
            'normalized_simple_strict':['63/100000','13/20000'],
            'scope':'CONDITIONAL_CONTINUUM_CENTER_ONLY_NOT_SIX_COEFFICIENT_ENCLOSURES',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__ == '__main__':
    import json
    print(json.dumps(certify_at(F(1,32)),indent=2))
