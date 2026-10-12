"""Independent matter-action identities from De Felice et al. 1404.0008.

The scalar matter sectors are kept separate from the Lagos-Ferreira metric
action until the variable-normalization bridge is fully closed.  This module
therefore uses the De Felice lapse convention directly:

    g_00 = -N^2 (1 + 2 Phi).

For a P(X) matter sector, Eq. (54) gives the pure-lapse quadratic coefficient
when matter, shift and spatial-metric perturbations are set to zero.
"""

from __future__ import annotations

import math


def kessence_lapse_quadratic_coefficient(
    *, rho: float, pressure: float, cs2: float
) -> float:
    """Coefficient of ``Phi^2`` in De Felice's matter Lagrangian Eq. (54).

    The result is the bracket-level coefficient before multiplication by the
    background volume factor ``N a^3`` (or its f-sector analogue):

        -P/2 + (1+c_s^2)/(2 c_s^2) * (rho+P).

    ``cs2=0`` is singular in the P(X) representation and is intentionally not
    hidden here; a dust limit must be taken only after the constrained action
    has been reduced.
    """
    if not all(math.isfinite(v) for v in (rho, pressure, cs2)):
        raise ValueError("rho, pressure and cs2 must be finite")
    if cs2 <= 0.0:
        raise ValueError("cs2 must be positive in the unreduced P(X) action")
    return float(
        -0.5 * pressure
        + 0.5 * (1.0 + cs2) / cs2 * (rho + pressure)
    )


def kessence_pure_lapse_quadratic_density(
    *, rho: float, pressure: float, cs2: float, Phi: float
) -> float:
    """Pure-lapse quadratic matter density in De Felice lapse normalization."""
    if not math.isfinite(Phi):
        raise ValueError("Phi must be finite")
    coeff = kessence_lapse_quadratic_coefficient(
        rho=rho, pressure=pressure, cs2=cs2
    )
    return float(coeff * Phi * Phi)
