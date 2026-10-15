"""Leading non-homothetic compact Stueckelberg map from the radial HR square root."""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LeadingPiMapCoefficients:
    A: float
    B: float
    C: float
    D: float


def leading_nonhomothetic_pi_map_coefficients(
    *, a: float, conformal_H: float, c: float,
    mu: float, mu_prime: float, r: float,
) -> LeadingPiMapCoefficients:
    """Return coefficients in

    ``delta_eta = A*pi_eta + B*pi_r`` and
    ``delta_r   = D*pi_eta + C*pi_r``.

    They are the first-order-in-background-gradient map obtained from the
    radial principal square root. ``mu_prime`` is d mu / d eta.
    """
    vals=(a,conformal_H,c,mu,mu_prime,r)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("pi-map inputs must be finite")
    if a <= 0.0 or c <= 0.0 or mu <= -1.0 or r < 0.0:
        raise ValueError("require a,c>0, mu>-1, r>=0")
    q=1.0+mu
    inva2=1.0/(a*a)
    theta=inva2*(c*r/q)*(conformal_H*mu + mu_prime/(c+q))
    return LeadingPiMapCoefficients(
        A=-inva2,
        B=theta,
        C=inva2*c/q,
        D=theta,
    )
