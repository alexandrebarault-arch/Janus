"""Raw De Felice scalar-action building blocks.

This module follows De Felice et al. arXiv:1404.0008 directly rather than the
background-reduced Lagos action. The scalar decomposition is

    V_i = D_i B
    H_ij = 2 psi delta_ij + (D_i D_j - delta_ij Delta/3) E

with flat-space Fourier convention ``Delta -> -k^2``. The function below
returns the bracket ``L_EH^(2)`` of Eq. (44), before the overall factor
``(M^2/2) * lapse * scale_factor^3``.
"""

from __future__ import annotations

import math


def eh_scalar_quadratic_density_flat(
    *,
    lapse: float,
    scale_factor: float,
    H: float,
    Hdot_over_lapse: float,
    k: float,
    Phi: float,
    B: float,
    psi: float,
    E: float,
    psi_dot: float,
    E_dot: float,
) -> float:
    """Scalar specialization of De Felice Eq. (44) for ``K=0``.

    ``Hdot_over_lapse`` means background ``dot(H)/lapse``. Dots on ``psi``
    and ``E`` are coordinate-time derivatives, exactly as in Eq. (44).

    No background equation is used here.
    """
    vals = (
        lapse, scale_factor, H, Hdot_over_lapse, k, Phi, B,
        psi, E, psi_dot, E_dot,
    )
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all EH scalar inputs must be finite")
    if lapse <= 0.0 or scale_factor <= 0.0 or k < 0.0:
        raise ValueError(
            "lapse and scale_factor must be positive and k non-negative"
        )

    N = lapse
    a = scale_factor
    k2 = k*k
    k4 = k2*k2
    k6 = k4*k2
    Hd = Hdot_over_lapse

    # Direct contraction of Eq. (44), using
    # Tr H = 6 psi and H^T_ij H_T^ij = 2 k^4 E^2 / 3.
    kinetic = (
        -6.0 * psi_dot**2 / N**2
        + k4 * E_dot**2 / (6.0 * N**2)
        + 12.0 * H * Phi * psi_dot / N
        + B * (
            2.0 * k4 * E_dot / (3.0 * N * a)
            - 4.0 * k2 * psi_dot / (N * a)
        )
    )

    spatial = (
        4.0 * H * k2 * Phi * B / a
        + 4.0 * k2 * Phi * psi / a**2
        + 2.0 * k2 * psi**2 / a**2
        + 2.0 * k4 * Phi * E / (3.0 * a**2)
        + 2.0 * k4 * psi * E / (3.0 * a**2)
        + k6 * E**2 / (18.0 * a**2)
    )

    background = (
        -9.0 * H**2 * Phi**2
        + 18.0 * H**2 * Phi * psi
        + 3.0 * H**2 * k2 * B**2
        + (9.0 * H**2 + 6.0 * Hd) * psi**2
        + (-H**2 - (2.0/3.0) * Hd) * k4 * E**2
    )
    return float(kinetic + spatial + background)
