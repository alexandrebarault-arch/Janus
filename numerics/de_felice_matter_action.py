"""Independent matter-action identities from De Felice et al. 1404.0008.

The scalar matter sectors are kept separate from the Lagos-Ferreira metric
action until the variable-normalization bridge is fully closed.  This module
therefore uses the De Felice lapse convention directly:

    g_00 = -N^2 (1 + 2 Phi),
    V_i = D_i B,
    H_ij = 2 gamma_ij psi
           + (D_i D_j - gamma_ij Delta/3) E.

For a P(X) matter sector, Eq. (54) gives the complete quadratic scalar matter
action.  The functions below return the bracket-level density before the
background volume factor ``N a^3`` (or its f-sector analogue) is applied.
"""

from __future__ import annotations

import math


def _validate_kessence_inputs(*values: float, cs2: float) -> None:
    if not all(math.isfinite(v) for v in (*values, cs2)):
        raise ValueError("all matter-action inputs must be finite")
    if cs2 <= 0.0:
        raise ValueError("cs2 must be positive in the unreduced P(X) action")


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
    _validate_kessence_inputs(rho, pressure, cs2=cs2)
    return float(
        -0.5 * pressure
        + 0.5 * (1.0 + cs2) / cs2 * (rho + pressure)
    )


def kessence_pure_lapse_quadratic_density(
    *, rho: float, pressure: float, cs2: float, Phi: float
) -> float:
    """Pure-lapse quadratic matter density in De Felice lapse normalization."""
    _validate_kessence_inputs(rho, pressure, Phi, cs2=cs2)
    coeff = kessence_lapse_quadratic_coefficient(
        rho=rho, pressure=pressure, cs2=cs2
    )
    return float(coeff * Phi * Phi)


def kessence_scalar_quadratic_density(
    *,
    rho: float,
    pressure: float,
    cs2: float,
    lapse: float,
    scale_factor: float,
    k: float,
    Phi: float,
    B: float,
    psi: float,
    E: float,
    delta_phi_over_phidot: float,
    delta_phidot_over_phidot: float,
) -> float:
    """Flat-Fourier scalar form of De Felice et al. Eq. (54).

    ``delta_phi_over_phidot`` denotes ``delta phi / dot(phi_0)`` and
    ``delta_phidot_over_phidot`` denotes ``delta dot(phi) / dot(phi_0)`` at
    the evaluation time.  No slow-background replacement of one by the time
    derivative of the other is made inside this algebraic action block.

    The return value is ``L_matter^(2)`` before multiplication by ``N a^3``.
    In flat Fourier space,

        Tr H = 6 psi,
        H_ij H^ij = 12 psi^2 + (2/3) k^4 E^2,
        V_i V^i = k^2 B^2.

    The P(X) representation requires ``cs2 > 0``.  Dust is obtained only as a
    controlled limit after the full lapse/shift-constrained action is reduced.
    """
    _validate_kessence_inputs(
        rho,
        pressure,
        lapse,
        scale_factor,
        k,
        Phi,
        B,
        psi,
        E,
        delta_phi_over_phidot,
        delta_phidot_over_phidot,
        cs2=cs2,
    )
    if lapse <= 0.0 or scale_factor <= 0.0:
        raise ValueError("lapse and scale_factor must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")

    enthalpy = rho + pressure
    tr_h = 6.0 * psi
    hij_hij = 12.0 * psi * psi + (2.0 / 3.0) * k**4 * E * E
    v2 = k * k * B * B
    q = delta_phi_over_phidot
    qdot = delta_phidot_over_phidot

    metric_pressure_block = pressure * (
        -0.5 * Phi * Phi
        + 0.5 * v2
        + 0.125 * (tr_h * tr_h - 2.0 * hij_hij)
        + 0.5 * tr_h * Phi
    )
    temporal_matter_block = (
        0.5 * enthalpy * qdot * qdot
        + 0.5 * (1.0 - cs2) / cs2 * enthalpy * (qdot - Phi) ** 2
        + 0.5 * enthalpy * (Phi - qdot) * (2.0 * Phi - tr_h)
    )
    spatial_matter_block = (
        -0.5
        * lapse**2
        * enthalpy
        / scale_factor**2
        * k**2
        * (q + scale_factor * B / lapse) ** 2
    )
    return float(metric_pressure_block + temporal_matter_block + spatial_matter_block)
