"""Independent matter-action identities from De Felice et al. 1404.0008.

The scalar matter sectors are kept separate from the Lagos-Ferreira metric
action until the variable-normalization bridge is fully closed.  This module
therefore uses the De Felice lapse convention directly:

    g_00 = -N^2 (1 + 2 Phi).

For a P(X) matter sector, Eq. (54) supplies the quadratic matter action.  The
scalar specialization below uses flat-space Fourier convention ``Delta ->
-k^2`` together with

    V_i = D_i B,
    H_ij = 2 psi delta_ij + (D_i D_j - delta_ij Delta/3) E.

The density helper returns the bracket-level coefficient before multiplication
by the background volume factor ``N a^3``.  The Lagrangian helper includes
that factor explicitly, so it can be applied independently to the g and f
matter sectors with ``(N,a)=(1,a)`` and ``(Nbar,b)`` respectively.
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
    field_ratio: float,
    field_velocity_ratio: float,
) -> float:
    """Scalar specialization of the P(X) quadratic matter action, Eq. (54).

    ``field_ratio`` is ``delta_phi / phi_dot_0`` and
    ``field_velocity_ratio`` is ``delta_phi_dot / phi_dot_0``.  They are kept
    independent here because Eq. (54) is an instantaneous quadratic action;
    background-time-derivative terms enter only when a chosen dynamical
    variable is differentiated later.

    The spatial scalar identities used here are

        Tr(H) = 6 psi,
        H_ij H^ij = 12 psi^2 + (2/3) k^4 E^2,
        V_i V^i = k^2 B^2.

    With all metric perturbations set to zero, the principal matter terms are

        (rho+P)/(2 c_s^2) * u_dot^2
        - N^2 (rho+P) k^2/(2 a^2) * u^2,

    so the coordinate-time dispersion is
    ``omega^2 = c_s^2 N^2 k^2/a^2`` as required.
    """
    values = (
        rho,
        pressure,
        cs2,
        lapse,
        scale_factor,
        k,
        Phi,
        B,
        psi,
        E,
        field_ratio,
        field_velocity_ratio,
    )
    if not all(math.isfinite(v) for v in values):
        raise ValueError("all matter-action inputs must be finite")
    if cs2 <= 0.0:
        raise ValueError("cs2 must be positive in the unreduced P(X) action")
    if lapse <= 0.0 or scale_factor <= 0.0 or k < 0.0:
        raise ValueError(
            "lapse and scale_factor must be positive and k non-negative"
        )

    enthalpy = rho + pressure
    q = field_velocity_ratio
    trace_h = 6.0 * psi
    h_norm_sq = 12.0 * psi**2 + (2.0 / 3.0) * k**4 * E**2

    metric_piece = pressure * (
        -0.5 * Phi**2
        + 0.5 * k**2 * B**2
        + 0.125 * (trace_h**2 - 2.0 * h_norm_sq)
        + 0.5 * trace_h * Phi
    )
    matter_time = (
        metric_piece
        + 0.5 * enthalpy * q**2
        + 0.5 * (1.0 - cs2) / cs2 * enthalpy * (q - Phi)**2
        + 0.5 * enthalpy * (Phi - q) * (2.0 * Phi - trace_h)
    )

    shifted_field = field_ratio + scale_factor * B / lapse
    gradient = (
        -0.5
        * lapse**2
        * enthalpy
        / scale_factor**2
        * k**2
        * shifted_field**2
    )
    return float(matter_time + gradient)


def kessence_scalar_quadratic_lagrangian(**kwargs) -> float:
    """Eq. (54) scalar bracket multiplied by ``N a^3``.

    Keeping this factor outside the density helper makes the g/f duplication
    explicit.  In the f sector use its own lapse and scale factor, e.g.
    ``lapse=Nbar`` and ``scale_factor=b=a*r``.
    """
    lapse = float(kwargs["lapse"])
    scale_factor = float(kwargs["scale_factor"])
    density = kessence_scalar_quadratic_density(**kwargs)
    return float(lapse * scale_factor**3 * density)
