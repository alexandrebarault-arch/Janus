"""Published Aoki-Maeda-Namba oscillation-mode control formulas.

This module is an independent acceptance oracle for the six-field nonlinear
Stueckelberg reduction. It does not implement the reduction itself.
"""
from __future__ import annotations
import math
import numpy as np


def _finite(*values: float) -> bool:
    return all(math.isfinite(float(v)) for v in values)


def linear_branch_coefficients(*, w: float) -> tuple[float, float]:
    """Return (K_S, c_S^2) for the mu=0 branch, Aoki Eqs. (4.53)-(4.54)."""
    if not _finite(w):
        raise ValueError("w must be finite")
    denom = 1.0 + 3.0*w
    if abs(denom) <= 1e-14:
        raise ZeroDivisionError("linear Aoki scalar coefficient is singular at w=-1/3")
    return 0.75*denom, (w - 1.0)/denom


def nonlinear_branch_coefficients(*, w: float, beta2: float, beta3: float, mu: float) -> tuple[float, float]:
    """Return (K_S, c_S^2) for a nonlinear mu_+-/mu_- branch.

    ``beta2`` and ``beta3`` are Aoki's normalized couplings entering Eqs.
    (4.55)-(4.56), not raw Hassan-Rosen beta_n coefficients.
    """
    if not _finite(w, beta2, beta3, mu) or mu <= -1.0:
        raise ValueError("inputs must be finite and mu>-1")
    common = (3.0*w - 1.0)*(2.0 + mu)*(1.0 + 2.0*beta2*mu + beta3*mu*mu)
    K = 0.75*common
    if abs(common) <= 1e-14:
        raise ZeroDivisionError("nonlinear Aoki kinetic normalization is singular")
    numerator = 2.0*(3.0*(1.0-w) + (1.0-(3.0*w-1.0)*beta2)*mu)
    cs2 = numerator/(3.0*common)
    return float(K), float(cs2)


def pi_to_stueckelberg(*, a: float, H: float, r: float, mu: float, pi_eta: float, pi_r: float) -> np.ndarray:
    """Return (delta_eta, delta_r) from Aoki Eqs. (4.50)-(4.51) at O(epsilon)."""
    if not _finite(a, H, r, mu, pi_eta, pi_r) or a <= 0.0 or r < 0.0 or mu <= -1.0:
        raise ValueError("invalid Aoki pi-map inputs")
    inva2 = 1.0/(a*a)
    mix = a*r*H*mu/(1.0 + mu)
    delta_eta = inva2*(-pi_eta + mix*pi_r)
    delta_r = inva2*(pi_r/(1.0 + mu) + mix*pi_eta)
    return np.asarray([delta_eta, delta_r], dtype=float)
