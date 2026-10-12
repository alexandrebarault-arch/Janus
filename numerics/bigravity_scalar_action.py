"""Independent scalar quadratic-action reconstruction for massive bigravity.

This module is intentionally independent of the old Comelli perturbation
reduction. It starts from Lagos & Ferreira, arXiv:1610.00553, Eqs. (3.6)-(3.8)
and is extended by TDD slices.
"""

from __future__ import annotations

import numpy as np


RAW_FIELD_ORDER = (
    "Phi1", "B1", "Psi1", "E1",
    "Phi2", "B2", "Psi2", "E2",
)


def shift_interaction_lagrangian(bg, *, k: float, B1: float, B2: float) -> float:
    """Return the complete quadratic shift-interaction block.

    Lagos raises spatial indices with the background spatial metric of the
    corresponding sector. For a comoving Fourier wave number k, combining
    the B1^2, B2^2 and B1 B2 pieces of Eqs. (3.6)-(3.8) gives

        a M1^2 Z k^2 / [2(Nbar+r)]
        * (r B1 - (Nbar/r) B2)^2.
    """
    if bg.Nbar + bg.r == 0.0 or bg.r == 0.0:
        raise ValueError("Nbar+r and r must be non-zero")
    pref = (
        bg.a * bg.M1sq * bg.Z * k**2
        / (2.0 * (bg.Nbar + bg.r))
    )
    return float(pref * (bg.r * B1 - (bg.Nbar / bg.r) * B2) ** 2)


def sector1_eh_velocity_lagrangian(
    bg,
    *,
    k: float,
    Phi1: float,
    B1: float,
    Psi1_dot: float,
    E1_dot: float,
) -> float:
    """Velocity-dependent sector-1 Einstein-Hilbert scalar block.

    This is the unambiguous velocity family in Lagos-Ferreira Eq. (3.6),
    evaluated on a comoving Fourier mode. Their spatial Laplacian obeys
    ``partial_1^2 -> -k^2/a^2``.
    """
    bracket = (
        -3.0 * Psi1_dot**2
        - 6.0 * bg.H * Psi1_dot * Phi1
        - 2.0 * k**2 * E1_dot * (Psi1_dot + bg.H * Phi1)
        + 2.0 * k**2 / bg.a**2 * Psi1_dot * B1
    )
    return float(bg.a**3 * bg.M1sq * bracket)


def raw_kinetic_hessian(bg, *, k: float) -> np.ndarray:
    """Velocity Hessian of the raw metric action, before constraint reduction.

    The order is ``RAW_FIELD_ORDER``. For massive bigravity with
    ``alpha_L=0`` and constant Planck masses, Lagos-Ferreira Eqs. (3.6)-(3.7)
    contain velocities only for ``Psi_A`` and ``E_A``. Lapses ``Phi_A`` and
    shifts ``B_A`` therefore have identically zero velocity rows/columns.

    Their ``partial^2`` uses the spatial background metric. Thus
    ``a^2 partial_1^2 -> -k^2`` and ``b^2 partial_2^2 -> -k^2`` for comoving k.
    """
    K = np.zeros((8, 8), dtype=float)

    i_p1 = RAW_FIELD_ORDER.index("Psi1")
    i_e1 = RAW_FIELD_ORDER.index("E1")
    i_p2 = RAW_FIELD_ORDER.index("Psi2")
    i_e2 = RAW_FIELD_ORDER.index("E2")

    pref1 = bg.a**3 * bg.M1sq
    K[i_p1, i_p1] = -6.0 * pref1
    cross1 = -2.0 * k**2 * pref1
    K[i_p1, i_e1] = K[i_e1, i_p1] = cross1

    pref2 = bg.Nbar * bg.b**3 * bg.M2sq
    K[i_p2, i_p2] = -6.0 / bg.Nbar**2 * pref2
    cross2 = -2.0 * k**2 / bg.Nbar**2 * pref2
    K[i_p2, i_e2] = K[i_e2, i_p2] = cross2

    return K
