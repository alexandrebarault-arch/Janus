"""Independent scalar quadratic-action reconstruction for massive bigravity.

This module is intentionally independent of the old Comelli perturbation
reduction. It starts from Lagos & Ferreira, arXiv:1610.00553, Eqs. (3.6)-(3.8)
and is extended by TDD slices.
"""

from __future__ import annotations

import math
import numpy as np


RAW_FIELD_ORDER = (
    "Phi1", "B1", "Psi1", "E1",
    "Phi2", "B2", "Psi2", "E2",
)


def shift_interaction_lagrangian(bg, *, k: float, B1: float, B2: float) -> float:
    """Return the complete quadratic shift-interaction block."""
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
    """Velocity-dependent sector-1 Einstein-Hilbert scalar block."""
    bracket = (
        -3.0 * Psi1_dot**2
        - 6.0 * bg.H * Psi1_dot * Phi1
        - 2.0 * k**2 * E1_dot * (Psi1_dot + bg.H * Phi1)
        + 2.0 * k**2 / bg.a**2 * Psi1_dot * B1
    )
    return float(bg.a**3 * bg.M1sq * bracket)


def sector2_eh_velocity_lagrangian(
    bg,
    *,
    k: float,
    Phi2: float,
    B2: float,
    Psi2_dot: float,
    E2_dot: float,
) -> float:
    """Velocity-dependent sector-2 Einstein-Hilbert scalar block.

    Lagos-Ferreira Eq. (3.7) is written in g-sector cosmic time, so lapse
    factors remain explicit. The sector-2 spatial Laplacian obeys
    ``partial_2^2 -> -k^2/b^2`` for comoving k.
    """
    bracket = (
        -3.0 * Psi2_dot**2 / bg.Nbar**2
        - 6.0 * bg.Hb * Psi2_dot * Phi2 / bg.Nbar**2
        - 2.0 * k**2 * E2_dot * (Psi2_dot + bg.Hb * Phi2) / bg.Nbar**2
        + 2.0 * k**2 * Psi2_dot * B2 / (bg.Nbar * bg.b**2)
    )
    return float(bg.Nbar * bg.b**3 * bg.M2sq * bracket)


def _elementary_symmetric_4(eigenvalues: tuple[float, float, float, float]) -> tuple[float, ...]:
    l0, l1, l2, l3 = eigenvalues
    e0 = 1.0
    e1 = l0 + l1 + l2 + l3
    e2 = (
        l0*l1 + l0*l2 + l0*l3
        + l1*l2 + l1*l3 + l2*l3
    )
    e3 = l0*l1*l2 + l0*l1*l3 + l0*l2*l3 + l1*l2*l3
    e4 = l0*l1*l2*l3
    return e0, e1, e2, e3, e4


def hr_diagonal_scalar_potential_density(
    *,
    a: float,
    r: float,
    Nbar: float,
    m2: float,
    M1sq: float,
    betas,
    k: float,
    Psi1: float,
    E1: float,
    Psi2: float,
    E2: float,
) -> float:
    """Exact HR potential density for diagonal scalar spatial perturbations.

    The Fourier wave vector is aligned with x.  Lapses and shifts are kept at
    their background values, while

        g_xx/a^2 = 1-2 Psi1-2 k^2 E1,
        g_yy/a^2 = g_zz/a^2 = 1-2 Psi1,

    and similarly for f with ``b/a=r``.  Because both metrics are diagonal,
    the square-root matrix eigenvalues are obtained exactly.  The returned
    quantity is the positive-convention interaction density

        m^2 M1^2 sqrt(-g) sum_n beta_n e_n(sqrt(g^{-1} f)).

    No precomputed J, Gamma, Z or Ztilde enters this evaluator.
    """
    betas = tuple(float(x) for x in betas)
    if len(betas) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    if not all(math.isfinite(v) for v in (a, r, Nbar, m2, M1sq, k)):
        raise ValueError("background parameters must be finite")
    if a <= 0.0 or r <= 0.0 or Nbar <= 0.0:
        raise ValueError("a, r and Nbar must be positive")

    gx = 1.0 - 2.0*Psi1 - 2.0*k*k*E1
    gy = 1.0 - 2.0*Psi1
    fx = 1.0 - 2.0*Psi2 - 2.0*k*k*E2
    fy = 1.0 - 2.0*Psi2
    if min(gx, gy, fx, fy) <= 0.0:
        raise ValueError("diagonal spatial metric factors must stay positive")

    lam_t = Nbar
    lam_x = r * math.sqrt(fx / gx)
    lam_y = r * math.sqrt(fy / gy)
    eigenvalues = (lam_t, lam_x, lam_y, lam_y)
    es = _elementary_symmetric_4(eigenvalues)

    sqrt_minus_g = a**3 * math.sqrt(gx) * gy
    potential = sum(beta * en for beta, en in zip(betas, es))
    return float(m2 * M1sq * sqrt_minus_g * potential)


def raw_kinetic_hessian(bg, *, k: float) -> np.ndarray:
    """Velocity Hessian of the raw metric action, before constraint reduction."""
    K = np.zeros((8, 8), dtype=float)

    i_p1 = RAW_FIELD_ORDER.index("Psi1")
    i_e1 = RAW_FIELD_ORDER.index("E1")
    i_p2 = RAW_FIELD_ORDER.index("Psi2")
    i_e2 = RAW_FIELD_ORDER.index("E2")

    pref1 = bg.a**3 * bg.M1sq
    K[i_p1, i_p1] = -6.0 * pref1
    K[i_p1, i_e1] = K[i_e1, i_p1] = -2.0 * k**2 * pref1

    pref2 = bg.Nbar * bg.b**3 * bg.M2sq
    K[i_p2, i_p2] = -6.0 / bg.Nbar**2 * pref2
    K[i_p2, i_e2] = K[i_e2, i_p2] = -2.0 * k**2 / bg.Nbar**2 * pref2

    return K
