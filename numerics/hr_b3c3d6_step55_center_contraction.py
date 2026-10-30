"""Exact-rational conditional center-adapted Step55 defect-to-error bound.

For 2*s*U_s=G(s,U)-2*U, s=r**2>0, if G_U<=1 along
all line segments joining an exact solution U to a C1 approximate v,
then f_U=(G_U-2)/(2*s)<=-1/(2*s). With |v_s-f(s,v)|<=D
continuously on [ra**2,rb**2] and initial error <=e,

 |U(rb**2)-v(rb**2)| <= (ra/rb)*e + (2*D/3)*(rb**2-ra**3/rb).

This follows from the scalar upper Dini derivative inequality
D+|error| <= -|error|/(2*s)+D and multiplying by sqrt(s).
The coefficient G_U<=1, continuous D, exact initial error and tube
must be independently certified for physical Step55. This module DOES
NOT claim those hypotheses, nor any Step58 six-coefficient enclosure.
"""
from fractions import Fraction as Q


def half_contractive_cell(error_in, defect_bound, r_left, r_right, g_u_upper):
    """Exact bound at rational radii; caller must certify the hypotheses."""
    e, d, a, b, gamma = map(Q, (error_in, defect_bound, r_left, r_right, g_u_upper))
    if a <= 0 or b <= a:
        raise ValueError('radii must satisfy 0<r_left<r_right')
    if e < 0 or d < 0:
        raise ValueError('error and defect bounds must be nonnegative')
    if gamma > 1:
        raise ValueError('G_U<=1 not certified: no half-contraction conclusion')
    return (a/b)*e + Q(2, 3)*d*(b*b-a*a*a/b)


def half_contractive_chain(error_in, cells):
    """cells: (r_left,r_right,D,certified_G_U_upper); exact continuity."""
    e = Q(error_in)
    if e < 0:
        raise ValueError('initial error bound must be nonnegative')
    previous = None
    for a, b, d, gamma in cells:
        if previous is not None and Q(a) != previous:
            raise ValueError('radial cells must be contiguous')
        e = half_contractive_cell(e, d, a, b, gamma)
        previous = Q(b)
    return e


def four_radius_example(error_in, defect_bounds, g_u_upper):
    """Exact illustrative chain; not physical bounds or a numerical replay."""
    if len(defect_bounds) != 4:
        raise ValueError('four defect bounds required')
    radii = [Q(1, 100), Q(1, 4), Q(1, 2), Q(7, 10), Q(17, 20)]
    return half_contractive_chain(error_in, [
        (radii[i], radii[i+1], defect_bounds[i], g_u_upper)
        for i in range(4)
    ])
