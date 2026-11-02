"""JANUS b3c3d6: exact necessary boundary lapse ratio + four-box countermodel.

This file is a symbolic/rational *logical consequence* of the already-published
Step58 A_N/A_M boxes (2026-11-02 commit f3d7422), NOT a new enclosure of the
original physical operator, nor a solution of its full Dirac system.
"""
from fractions import Fraction as Q

# Strict, outward-rounded rational integer boxes previously certified on Step55.
# Scientific input: research/reports/gate2b-b3c3d6-step58-physical-ANAM-four-radii-sign.json
# Source Git blob: c502b9779056e8a493c43d330696515a661128c4
PHYSICAL_RATIONAL_BOXES = {
    Q(1, 4): ((214, 223), (-430, -413)),
    Q(1, 2): ((847, 883), (-1697, -1634)),
    Q(7, 10): ((1639, 1709), (-3279, -3157)),
    Q(17, 20): ((2385, 2489), (-4768, -4588)),
}
CENTER_RHO_OPEN = Q(1037, 2000), Q(2593, 5000)


def ratio_open_bounds(an, am):
    """If a_lo<A_N<a_hi and m_lo<A_M<m_hi<0, bound -A_N/A_M.

    Signs are validated; all comparisons are exact integers/rational.
    """
    alo, ahi = an
    mlo, mhi = am
    if not (0 < alo < ahi and mlo < mhi < 0):
        raise ValueError('positive A_N and negative A_M required')
    return Q(alo, -mlo), Q(ahi, -mhi)


def certified_pointwise_ratios():
    return {str(r): ratio_open_bounds(*box) for r, box in PHYSICAL_RATIONAL_BOXES.items()}


def necessary_boundary_ratio(r, n_value, m_value):
    """Test compatibility with *necessary* pointwise ratio bounds.

    True does NOT establish a physical Step55 lapse pair; false excludes one
    assuming the original A_N/A_M certification and full shell B/E=0.
    """
    if n_value <= 0 or m_value <= 0:
        return False
    lo, hi = ratio_open_bounds(*PHYSICAL_RATIONAL_BOXES[Q(r)])
    return lo < Q(m_value) / Q(n_value) < hi


def toy_coefficients(r):
    """Independent synthetic r-even polynomial coefficients, *not* Step58."""
    s = Q(r) ** 2
    return s * (3500 - 175 * s), -s * (6750 - 375 * s)


def toy_ratio(r):
    """Positive even analytic lapse M, with N=1, on [0,17/20]."""
    s = Q(r) ** 2
    return (3500 - 175 * s) / (6750 - 375 * s)


def toy_ratio_derivative_s_numerator():
    """d/ds [(3500-175s)/(6750-375s)] = result/(6750-375s)^2."""
    return 375 * 3500 - 175 * 6750


def compatible_two_boundary_dirichlet(center_n, center_m, outer_n, outer_m,
                                      rho_center, rho_outer):
    """Exact compatibility for algebraic A_N N + A_M M = 0 on a closed interval.

    With A_M != 0 inside and a positive continuous rho=-A_N/A_M on [0,R],
    there exists a strictly positive C^k lapse pair satisfying arbitrary
    positive Dirichlet amplitudes at both edges iff the four values are
    positive and center_m/center_n=rho(0), outer_m/outer_n=rho(R).
    Smoothness k of the pair requires rho C^k and positive C^k interpolation N.
    For radial even-analytic rho, choose N(r)=N(0)+(N(R)-N(0))*r**2/R**2,
    a strictly positive even-analytic interpolation on 0<=r<=R.
    The claim is about this single algebraic preservation equation ONLY.
    """
    vals = (center_n, center_m, outer_n, outer_m, rho_center, rho_outer)
    if not all(Q(v) > 0 for v in vals):
        return False
    return Q(center_m) / Q(center_n) == Q(rho_center) and Q(outer_m) / Q(outer_n) == Q(rho_outer)


def audit():
    ratios = certified_pointwise_ratios()
    assert ratios['17/20'][0] > Q(1, 2)
    assert ratios['17/20'][1] < Q(11, 20)
    assert all(Q(49, 100) < l < h < Q(11, 20) for l, h in ratios.values())
    assert CENTER_RHO_OPEN[0] < toy_ratio(0) < CENTER_RHO_OPEN[1]
    assert toy_ratio_derivative_s_numerator() == 131250 > 0
    for r, ((alo, ahi), (mlo, mhi)) in PHYSICAL_RATIONAL_BOXES.items():
        an, am = toy_coefficients(r)
        assert alo < an < ahi and mlo < am < mhi
        assert an + am < 0 and an + am * toy_ratio(r) == 0
        assert necessary_boundary_ratio(r, 1, toy_ratio(r))
    assert toy_ratio(Q(17, 20)) != 1
    return ratios


if __name__ == '__main__':
    for r, (lo, hi) in audit().items():
        print(f'{r}: {lo} < M/N < {hi}')
    print('CONDITIONAL NECESSARY RATIO CERTIFICATE; SYNTHETIC POSITIVE TWO-BOUNDARY COUNTERMODEL PASS')
