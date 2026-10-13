"""Regular phase-space form of the De Felice scalar matter action."""
from __future__ import annotations

import math


def _validate_common(*values: float) -> None:
    if not all(math.isfinite(float(v)) for v in values):
        raise ValueError("all phase-action inputs must be finite")


def finite_cs2_phase_density(
    *, rho: float, pressure: float, cs2: float, lapse: float,
    scale_factor: float, k: float, Phi: float, B: float, psi: float, E: float,
    q: float, momentum: float,
) -> float:
    """Return ell(q,p) such that the first-order density is p*qdot + ell.

    This is the exact Legendre transform of De Felice Eq. (54) with respect
    to qdot at finite sound speed. The canonical p*qdot term is deliberately
    not included because qdot is not an argument of this function.
    """
    _validate_common(
        rho, pressure, cs2, lapse, scale_factor, k,
        Phi, B, psi, E, q, momentum,
    )
    if cs2 <= 0.0:
        raise ValueError("cs2 must be positive before the analytic dust limit")
    if lapse <= 0.0 or scale_factor <= 0.0:
        raise ValueError("lapse and scale_factor must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")
    enthalpy = rho + pressure
    if enthalpy == 0.0:
        raise ValueError("rho+pressure must be non-zero")

    tr_h = 6.0 * psi
    hij_hij = 12.0 * psi * psi + (2.0 / 3.0) * k**4 * E * E
    metric_pressure = pressure * (
        -0.5 * Phi * Phi
        + 0.5 * k * k * B * B
        + 0.125 * (tr_h * tr_h - 2.0 * hij_hij)
        + 0.5 * tr_h * Phi
    )
    spatial = (
        -0.5 * lapse**2 * enthalpy / scale_factor**2 * k**2
        * (q + scale_factor * B / lapse) ** 2
    )
    shifted = momentum - 3.0 * enthalpy * psi
    h_temporal = (
        momentum * Phi
        + cs2 * shifted * shifted / (2.0 * enthalpy)
        - 0.5 * enthalpy * Phi * Phi
    )
    return float(-h_temporal + metric_pressure + spatial)


def dust_phase_density(
    *, rho: float, lapse: float, scale_factor: float, k: float,
    Phi: float, B: float, psi: float, E: float, q: float, momentum: float,
) -> float:
    """Exact P=0, cs2->0 non-canonical phase density."""
    _validate_common(rho, lapse, scale_factor, k, Phi, B, psi, E, q, momentum)
    if lapse <= 0.0 or scale_factor <= 0.0:
        raise ValueError("lapse and scale_factor must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")
    spatial = (
        -0.5 * lapse**2 * rho / scale_factor**2 * k**2
        * (q + scale_factor * B / lapse) ** 2
    )
    return float(-momentum * Phi + 0.5 * rho * Phi * Phi + spatial)


def physical_density_from_phase_momentum(
    *, momentum_local: float, rho: float, psi: float,
) -> float:
    """Return delta_rho from p=delta_rho+3 rho psi for pressureless matter."""
    _validate_common(momentum_local, rho, psi)
    return float(momentum_local - 3.0 * rho * psi)


def common_normalized_momentum(*, momentum_local: float, prefactor: float) -> float:
    _validate_common(momentum_local, prefactor)
    if prefactor == 0.0:
        raise ValueError("prefactor must be non-zero")
    return float(prefactor * momentum_local)


def local_momentum_from_common(*, momentum_common: float, prefactor: float) -> float:
    _validate_common(momentum_common, prefactor)
    if prefactor == 0.0:
        raise ValueError("prefactor must be non-zero")
    return float(momentum_common / prefactor)
