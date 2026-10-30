"""Exact rational endpoint error screen from a *continuous* normalized Step55 residual.

Conditional on the archived Step63 physical G_U<=-99/100 and both exact and
candidate curves remaining in the Step55 tube. This does not compute a DOP853
residual, initial error, or Step58 coefficients.
"""
from fractions import Fraction as Q

GU_UPPER = Q(-99, 100)
R_PHYSICAL_STRICT = Q(295653233337826329055403, 2000000000000000000000000000)
R_MAX = Q(17, 20)


def endpoint_bound_rational(ra, rb, initial_error, normalized_residual,
                            gu_upper=GU_UPPER):
    """Rigorous rational upper bound on |v(rb²)-U(rb²)|.

    On the tube, G_U<=g<2 and |2s v_s-G(s,v)+2v|<=R continuously.
    With alpha=(2-g)/2>0, exact Gronwall bound is
      q**(2*alpha)*e0 + R/(2*alpha)*(1-q**(2*alpha)), q=ra/rb.
    For alpha>=1, replace q**(2*alpha) by q**2 ONLY when its
    coefficient is positive; otherwise drop the nonpositive term.
    Returns a rational bound (not the irrational-power expression).
    """
    a,b,e,r,g=map(Q,(ra,rb,initial_error,normalized_residual,gu_upper))
    if not Q(0)<a<b<=R_MAX or e<0 or r<0 or g>0:
        raise ValueError('require 0<ra<rb<=17/20, nonnegative e,R and g<=0')
    alpha=(2-g)/2
    equilibrium=r/(2*alpha)
    bound=equilibrium+max(e-equilibrium,Q(0))*(a/b)**2
    return {'bound':bound,'equilibrium':equilibrium,'alpha':alpha,
            'radius_square_ratio':(a/b)**2}


def archived_strict_residual_screen(ra,rb,initial_error,normalized_residual):
    """Combine the historical strict residual gate with a conditional error.

    The caller MUST independently certify: candidate starts in tube,
    continuous residual on every dense-output cell, initial error, and
    archived physical tube/Step63 G_U bound. A numerical sample is NOT enough.
    """
    r=Q(normalized_residual)
    if r>=R_PHYSICAL_STRICT:
        raise ValueError('continuous normalized residual exceeds strict physical gate')
    return endpoint_bound_rational(ra,rb,initial_error,r)
