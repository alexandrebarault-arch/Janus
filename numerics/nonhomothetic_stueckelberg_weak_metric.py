"""Weak Newtonian-gauge metrics with exact spherical Stueckelberg pullback.

The metric potentials are treated in the weak-field Newtonian-gauge ansatz,
while the relative-coordinate fields ``mu`` and ``sigma`` are kept fully
nonlinear.  This is the kinematic layer needed before solving the weak metric
constraints in the Aoki-Maeda-Namba style reduction on a non-homothetic
Candidate-C background.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class PulledBackWeakFMetric:
    radial_block: np.ndarray
    angular_coefficient: float
    jacobian: np.ndarray


def _finite(*values: float) -> bool:
    return all(math.isfinite(float(value)) for value in values)


def weak_g_inverse_radial(*, a: float, Phi_g: float, Psi_g: float) -> np.ndarray:
    """Return the exact inverse radial block of the weak g Newtonian metric."""
    if not _finite(a, Phi_g, Psi_g) or a <= 0.0:
        raise ValueError("a must be positive and inputs finite")
    if 1.0 + 2.0*Phi_g <= 0.0 or 1.0 - 2.0*Psi_g <= 0.0:
        raise ValueError("weak g metric must keep Lorentzian signature")
    return np.diag([
        -1.0/(a*a*(1.0 + 2.0*Phi_g)),
        1.0/(a*a*(1.0 - 2.0*Psi_g)),
    ])


def pullback_weak_f_metric(
    *,
    b: float,
    c_background: float,
    r: float,
    Phi_f: float,
    Psi_f: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> PulledBackWeakFMetric:
    """Pull back the weak f metric through the exact nonlinear spherical map."""
    vals = (
        b, c_background, r, Phi_f, Psi_f,
        sigma_dot, sigma_prime, mu, mu_dot, mu_prime,
    )
    if (
        not _finite(*vals) or b <= 0.0 or c_background <= 0.0
        or r < 0.0 or mu <= -1.0
    ):
        raise ValueError("invalid weak f/Stueckelberg inputs")
    if 1.0 + 2.0*Phi_f <= 0.0 or 1.0 - 2.0*Psi_f <= 0.0:
        raise ValueError("weak f metric must keep Lorentzian signature")

    J = np.array([
        [c_background + sigma_dot, sigma_prime],
        [r*mu_dot, 1.0 + mu + r*mu_prime],
    ], dtype=float)
    native_radial = np.diag([
        -(1.0 + 2.0*Phi_f),
        1.0 - 2.0*Psi_f,
    ])
    radial = b*b*(J.T @ native_radial @ J)
    angular = b*b*(1.0 - 2.0*Psi_f)*(1.0 + mu)**2*r*r

    return PulledBackWeakFMetric(
        radial_block=np.asarray(radial, dtype=float),
        angular_coefficient=float(angular),
        jacobian=J,
    )
