"""Exact spherical Stueckelberg pullback kinematics on a non-homothetic FLRW pair.

Use g conformal coordinates ``(eta,r)``.  The natural f conformal time has
background derivative ``d eta_f_bar / d eta = c(eta)`` and the nonlinear
relative-coordinate map is

    eta_f = eta_f_bar(eta) + sigma(eta,r),
    r_f   = (1 + mu(eta,r)) r.

This is the non-homothetic generalization of Aoki-Maeda-Namba Eq. (4.18).
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class PulledBackFMetric:
    radial_block: np.ndarray
    angular_coefficient: float
    jacobian: np.ndarray


def stueckelberg_jacobian(
    *,
    c_background: float,
    r: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> np.ndarray:
    """Return d(eta_f,r_f)/d(eta,r) for the nonlinear spherical map."""
    vals = (
        c_background, r, sigma_dot, sigma_prime,
        mu, mu_dot, mu_prime,
    )
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if c_background <= 0.0 or r < 0.0 or mu <= -1.0:
        raise ValueError("require c_background>0, r>=0 and mu>-1")

    return np.array([
        [c_background + sigma_dot, sigma_prime],
        [r*mu_dot, 1.0 + mu + r*mu_prime],
    ], dtype=float)


def pullback_f_metric(
    *,
    b: float,
    c_background: float,
    r: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> PulledBackFMetric:
    """Pull back ``b^2(-deta_f^2+dr_f^2+r_f^2 dOmega^2)`` to g coordinates."""
    if not (math.isfinite(b) and b > 0.0):
        raise ValueError("b must be finite and positive")

    J = stueckelberg_jacobian(
        c_background=c_background,
        r=r,
        sigma_dot=sigma_dot,
        sigma_prime=sigma_prime,
        mu=mu,
        mu_dot=mu_dot,
        mu_prime=mu_prime,
    )
    minkowski_radial = np.diag([-1.0, 1.0])
    radial = b*b*(J.T @ minkowski_radial @ J)
    angular = (b*(1.0 + mu)*r)**2

    return PulledBackFMetric(
        radial_block=np.asarray(radial, dtype=float),
        angular_coefficient=float(angular),
        jacobian=J,
    )
