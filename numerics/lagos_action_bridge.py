"""Bridge JANUS/Comelli background variables to Lagos-Ferreira action parameters.

For the Hassan-Rosen massive-bigravity specialization of Lagos & Ferreira
(arXiv:1610.00553, Eqs. 3.13-3.15), their background variables map to the
JANUS/Comelli conventions as

    r = xi,
    Nbar = xi*c,
    Z = m^2 J = m^2 f2/xi,
    Z_tilde = m^2 Gamma/xi = m^2 f1/xi.

This module is deliberately algebraic.  It does not use the Comelli scalar
field equations and is therefore an independent action-level convention
bridge for Gate 2B.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from numerics.comelli_dae import ScalarBackground


@dataclass(frozen=True)
class LagosBigravityParameters:
    r: float
    Nbar: float
    Z: float
    Z_tilde: float


def lagos_bigravity_parameters(bg: ScalarBackground) -> LagosBigravityParameters:
    """Return the Lagos-Ferreira massive-bigravity interaction parameters."""
    if not all(math.isfinite(v) for v in (bg.xi, bg.c, bg.m2, bg.f1, bg.f2)):
        raise ValueError("background quantities must be finite")
    if bg.xi == 0.0:
        raise ValueError("xi must be non-zero")

    r = bg.xi
    nbar = bg.xi * bg.c
    z = bg.m2 * bg.f2 / bg.xi
    z_tilde = bg.m2 * bg.f1 / bg.xi
    return LagosBigravityParameters(
        r=float(r),
        Nbar=float(nbar),
        Z=float(z),
        Z_tilde=float(z_tilde),
    )
