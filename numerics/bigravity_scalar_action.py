"""Independent scalar quadratic-action reconstruction for massive bigravity.

This module is intentionally independent of the old Comelli perturbation
reduction.  It starts from Lagos & Ferreira, arXiv:1610.00553, Eqs. (3.6)-(3.8)
and will be extended by TDD slices.
"""

from __future__ import annotations

import numpy as np


RAW_FIELD_ORDER = (
    "Phi1", "B1", "Psi1", "E1",
    "Phi2", "B2", "Psi2", "E2",
)


def shift_interaction_lagrangian(bg, *, k: float, B1: float, B2: float) -> float:
    """Return the complete quadratic shift-interaction block.

    With Fourier convention ``partial^2 -> -k^2``, the B1^2, B2^2 and B1 B2
    terms from Lagos-Ferreira Eqs. (3.6)-(3.8) combine exactly into

        a^3 M1^2 Z k^2 / [2(Nbar+r)] * (r B1 - Nbar B2)^2.
    """
    if bg.Nbar + bg.r == 0.0:
        raise ValueError("Nbar+r must be non-zero")
    pref = (
        bg.a**3 * bg.M1sq * bg.Z * k**2
        / (2.0 * (bg.Nbar + bg.r))
    )
    return float(pref * (bg.r * B1 - bg.Nbar * B2) ** 2)


def raw_kinetic_hessian(bg, *, k: float) -> np.ndarray:
    """Velocity Hessian of the raw metric action, before constraint reduction.

    The order is ``RAW_FIELD_ORDER``.  For massive bigravity with
    ``alpha_L=0`` and constant Planck masses, Lagos-Ferreira Eqs. (3.6)-(3.7)
    contain velocities only for ``Psi_A`` and ``E_A``.  Lapses ``Phi_A`` and
    shifts ``B_A`` therefore have identically zero velocity rows/columns.
    """
    K = np.zeros((8, 8), dtype=float)

    i_p1 = RAW_FIELD_ORDER.index("Psi1")
    i_e1 = RAW_FIELD_ORDER.index("E1")
    i_p2 = RAW_FIELD_ORDER.index("Psi2")
    i_e2 = RAW_FIELD_ORDER.index("E2")

    pref1 = bg.a**3 * bg.M1sq
    K[i_p1, i_p1] = -6.0 * pref1
    cross1 = -2.0 * k**2 / bg.a**2 * pref1
    K[i_p1, i_e1] = K[i_e1, i_p1] = cross1

    pref2 = bg.Nbar * bg.b**3 * bg.M2sq
    K[i_p2, i_p2] = -6.0 / bg.Nbar**2 * pref2
    cross2 = -2.0 * k**2 / (bg.b**2 * bg.Nbar**2) * pref2
    K[i_p2, i_e2] = K[i_e2, i_p2] = cross2

    return K
