"""Convention bridge between JANUS-R Hassan-Rosen beta_n notation and
Comelli-Crisostomi-Pilo (2014), arXiv:1403.5679.

This module is intentionally algebraic. It exists to make the Gate-2B
perturbation implementation auditable before any transfer integration is
attempted.
"""

from __future__ import annotations

from math import factorial
from typing import Sequence


def beta_to_comelli_a(beta: Sequence[float]) -> tuple[float, ...]:
    """Map standard Hassan-Rosen beta_n to Comelli's a_n.

    Comelli uses V_n = n! e_n, while JANUS-R uses the standard elementary
    symmetric-polynomial coefficients beta_n. Therefore beta_n = n! a_n.
    """
    if len(beta) != 5:
        raise ValueError("beta must contain beta_0 ... beta_4")
    return tuple(float(beta[n]) / factorial(n) for n in range(5))


def comelli_f1_f2(y: float, c: float, a: Sequence[float]) -> tuple[float, float]:
    """Return Comelli et al. Eq. (A.13) functions f1 and f2."""
    if len(a) != 5:
        raise ValueError("a must contain a_0 ... a_4")
    _, a1, a2, a3, _ = map(float, a)
    f1 = y * (2.0 * y * (3.0 * a3 * c * y + a2 * (c + 1.0)) + a1)
    f2 = y * (6.0 * a3 * y**2 + 4.0 * a2 * y + a1)
    return f1, f2


def janus_J_Gamma(y: float, c: float, beta: Sequence[float]) -> tuple[float, float]:
    """Return JANUS-R J and Gamma in the conventions of flrw_two_matter.py."""
    if len(beta) != 5:
        raise ValueError("beta must contain beta_0 ... beta_4")
    _, beta1, beta2, beta3, _ = map(float, beta)
    J = beta1 + 2.0 * beta2 * y + beta3 * y**2
    Jp = 2.0 * beta2 + 2.0 * beta3 * y
    Gamma = y * J + 0.5 * (c - 1.0) * y**2 * Jp
    return J, Gamma


def comelli_branch_lhs(y: float, kappa: float, a: Sequence[float]) -> float:
    """Potential-only left-hand side of Comelli et al. Eq. (3.8)."""
    if len(a) != 5:
        raise ValueError("a must contain a_0 ... a_4")
    if kappa <= 0.0 or y <= 0.0:
        raise ValueError("kappa and y must be positive")
    a0, a1, a2, a3, a4 = map(float, a)
    return (
        y**2 * (8.0 * a4 / kappa - 2.0 * a2)
        + y * (6.0 * a3 / kappa - a1)
        + a1 / (3.0 * kappa * y)
        + 2.0 * a2 / kappa
        - 2.0 * a3 * y**3
        - a0 / 3.0
    )


def janus_branch_potential_lhs(y: float, kappa: float, beta: Sequence[float]) -> float:
    """(U_g - y^2 U_f/kappa)/3 in standard beta_n notation."""
    if len(beta) != 5:
        raise ValueError("beta must contain beta_0 ... beta_4")
    if kappa <= 0.0 or y <= 0.0:
        raise ValueError("kappa and y must be positive")
    beta0, beta1, beta2, beta3, beta4 = map(float, beta)
    U_g = beta0 + 3.0 * beta1 * y + 3.0 * beta2 * y**2 + beta3 * y**3
    U_f = beta4 + 3.0 * beta3 / y + 3.0 * beta2 / y**2 + beta1 / y**3
    return (U_g - y**2 * U_f / kappa) / 3.0
