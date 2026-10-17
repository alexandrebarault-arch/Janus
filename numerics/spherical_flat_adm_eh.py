"""Einstein-Hilbert ADM density for a spatially-flat spherical scalar chart."""
from __future__ import annotations
import math


def flat_spherical_adm_eh_density(*, scale_factor: float, scale_rate: float,
                                  background_lapse: float, r: float,
                                  Phi: float, shift: float, shift_r: float) -> float:
    """Return ``N sqrt(h) (K_ij K^ij-K^2)`` per ``sin(theta)``.

    The native metric convention is

    ``g_tt=-n^2(1+2 Phi)``, ``g_tr=n a U``,
    ``h_ij=a^2 diag(1,r^2,r^2 sin^2 theta)``.

    ``shift`` is ``U`` and ``shift_r`` is its native radial derivative.
    The three-curvature is exactly zero. Overall ``M^2/2`` is not included.
    """
    vals=(scale_factor,scale_rate,background_lapse,r,Phi,shift,shift_r)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all flat-ADM inputs must be finite")
    a=float(scale_factor); adot=float(scale_rate); n=float(background_lapse); rr=float(r)
    phi=float(Phi); U=float(shift); Ur=float(shift_r)
    if a<=0.0 or n<=0.0 or rr<=0.0:
        raise ValueError("require positive scale factor, lapse and radius")
    lapse_sq=1.0+2.0*phi+U*U
    if lapse_sq<=0.0:
        raise ValueError("ADM lapse left the real positive branch")
    N=n*math.sqrt(lapse_sq)
    hcoord=adot/a
    kr=(hcoord-n*Ur/a)/N
    kt=(hcoord-n*U/(a*rr))/N
    invariant=-4.0*kr*kt-2.0*kt*kt
    return float(N*a**3*rr**2*invariant)
