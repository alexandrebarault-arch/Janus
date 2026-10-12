"""Independent Lagos-Ferreira scalar benchmark helpers for JANUS Gate 2B.

This module starts from the one-matter massive-bigravity notation of
Lagos & Ferreira (arXiv:1410.0207) and maps its interaction combinations
onto the JANUS/Comelli background variables.  It is intentionally kept
separate from the Comelli reduction so it can act as an independent audit.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LagosInteractionCoefficients:
    """Interaction combinations used by the Lagos scalar equations."""

    Z: float
    Z_tilde: float


def lagos_interaction_coefficients(
    beta,
    *,
    xi: float,
    c: float,
    m2: float = 1.0,
) -> LagosInteractionCoefficients:
    """Return the Lagos ``Z`` and ``Z_tilde`` interaction combinations.

    With ``N=xi`` and ``X=c`` in arXiv:1410.0207,

        Z       = m^2 (beta1 + 2 beta2 xi + beta3 xi^2),
        Z_tilde = m^2 (beta1 + beta2 xi (1+c) + beta3 xi^2 c).

    Thus ``Z=m^2 J`` and ``xi*Z_tilde=m^2 Gamma`` in JANUS notation.
    """
    if len(beta) != 5:
        raise ValueError("beta must contain beta_0 through beta_4")
    if not (xi > 0.0 and math.isfinite(xi)):
        raise ValueError("xi must be finite and positive")
    if not (math.isfinite(c) and math.isfinite(m2)):
        raise ValueError("c and m2 must be finite")

    b1 = float(beta[1])
    b2 = float(beta[2])
    b3 = float(beta[3])
    Z = m2 * (b1 + 2.0 * b2 * xi + b3 * xi**2)
    Z_tilde = m2 * (b1 + b2 * xi * (1.0 + c) + b3 * xi**2 * c)
    return LagosInteractionCoefficients(Z=float(Z), Z_tilde=float(Z_tilde))
