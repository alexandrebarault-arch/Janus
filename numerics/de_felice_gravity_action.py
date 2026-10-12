"""Scalar Einstein-Hilbert quadratic action in De Felice variables.

This is a direct flat-FLRW scalar specialization of De Felice et al.
arXiv:1404.0008 Eq. (44). It deliberately contains neither the Hassan-Rosen
mixing potential nor matter. Those pieces are added separately so that the
full two-matter action never inherits the one-matter background specialization
used by the Lagos-Ferreira audit module.
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
    """Return ``L_EH^(2)`` of Eq. (44) for one flat scalar Fourier mode.

    Conventions are exactly those of De Felice Eq. (41) and Eq. (67):
    ``V_i=D_i B`` and
    ``H_ij=2 gamma_ij psi+(D_iD_j-gamma_ij Delta/3)E``.
    The full Einstein-Hilbert action contributes
    ``(M^2/2) * lapse * a^3 * L_EH^(2)``.
    """
    vals = (
        lapse, scale_factor, H, Hdot_over_lapse, k,
        Phi, B, psi, E, psi_dot, E_dot,
    )
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all EH scalar inputs must be finite")
    if lapse <= 0.0 or scale_factor <= 0.0:
        raise ValueError("lapse and scale_factor must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")

    N = lapse
    a = scale_factor
    k2 = k*k
    k4 = k2*k2
    k6 = k4*k2

    # 1/(4N^2) (gamma^ik gamma^jl-gamma^ij gamma^kl)
    # Hdot_ij Hdot_kl.
    kinetic = (
        -6.0*psi_dot*psi_dot/N**2
        + k4*E_dot*E_dot/(6.0*N**2)
    )

    lapse_kinetic = 12.0*H*Phi*psi_dot/N

    # Shift couplings from Vi=D_i B and the scalar traceless H_ij piece.
    shift = (
        (2.0/3.0)*k4*B*E_dot/(N*a)
        - 4.0*k2*psi_dot*B/(N*a)
        + 4.0*H*k2*Phi*B/a
    )

    # Spatial derivative terms in Eq. (44), K=0.
    spatial = (
        4.0*k2*Phi*psi
        - (2.0/3.0)*k4*Phi*E
        + 2.0*k2*psi*psi
        - (2.0/3.0)*k4*psi*E
        + (1.0/18.0)*k6*E*E
    ) / (a*a)

    background = (
        -9.0*H*H*Phi*Phi
        + 3.0*H*H*(6.0*Phi*psi + k2*B*B)
        + (9.0*H*H + 6.0*Hdot_over_lapse)*psi*psi
        + (-H*H - (2.0/3.0)*Hdot_over_lapse)*k4*E*E
    )

    return float(kinetic + lapse_kinetic + shift + spatial + background)
