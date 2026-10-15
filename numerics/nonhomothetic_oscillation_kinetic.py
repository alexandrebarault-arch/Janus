"""Homogeneous kinetic audit for the nonlinear Stueckelberg oscillation mode.

This is deliberately a kinetic-sign oracle only.  It does not determine the
spatial-gradient coefficient or a full propagation speed.
"""
from __future__ import annotations

import math
import numpy as np

from numerics.nonhomothetic_hr_spherical import square_root_invariants


def aoki_homothetic_kinetic_coefficient(*, beta1, beta2, beta3, K, w, mu):
    vals = (beta1, beta2, beta3, K, w, mu)
    if not all(math.isfinite(float(x)) for x in vals) or K <= 0.0 or mu <= -1.0:
        raise ValueError("invalid homothetic kinetic inputs")
    D = beta1*K + 2.0*beta2*K*K + beta3*K**3
    scale = max(1.0, abs(beta1*K), abs(2.0*beta2*K*K), abs(beta3*K**3))
    if abs(D) <= 1.0e-14*scale:
        raise np.linalg.LinAlgError("interaction normalization is singular")
    B2 = (beta2*K*K + beta3*K**3)/D
    B3 = beta3*K**3/D
    KS = 0.75*(3.0*w - 1.0)*(2.0 + mu)*(1.0 + 2.0*B2*mu + B3*mu*mu)
    return float(KS), float(D)


def _reduced_action_general(
    beta, a, b, c, mu, mu_dot, sigma_r_coeff, sigma_t_coeff,
    radius, mu_dot_delta, sigma_dot_delta,
):
    nodes, weights = np.polynomial.legendre.leggauss(64)
    rr = 0.5*radius*(nodes + 1.0)
    ww = 0.5*radius*weights
    total = 0.0
    for r, qw in zip(rr, ww):
        inv = square_root_invariants(
            a=a, b=b, c_background=c, r=float(r),
            sigma_dot=0.5*r*r*(sigma_t_coeff + sigma_dot_delta),
            sigma_prime=r*sigma_r_coeff,
            mu=mu, mu_dot=mu_dot + mu_dot_delta, mu_prime=0.0,
        )
        total += qw*r*r*float(np.dot(beta, inv.elementary_symmetric))
    return float(total)


def uniform_velocity_hessian(
    *, betas, a, b, c, mu, mu_dot,
    sigma_prime_coefficient, sigma_dot_coefficient,
    radius=0.02, step=1.0e-3,
):
    """Return the local 2x2 Hessian in ``(delta mu_dot, delta sigma_dot)``.

    The caller supplies the actual nonlinear background map.  This helper is
    intentionally kinematic: it diagnoses the homogeneous velocity sector of
    the exact HR pullback, not the spatial-gradient term or the metric-constraint
    corrections required for a complete scalar stability calculation.
    """
    if radius <= 0.0 or step <= 0.0:
        raise ValueError("radius and step must be positive")
    beta = np.asarray(betas, dtype=float)
    if beta.shape != (5,) or not np.all(np.isfinite(beta)):
        raise ValueError("betas must be a finite length-5 vector")

    def L(x, y):
        return _reduced_action_general(
            beta, a, b, c, mu, mu_dot,
            sigma_prime_coefficient, sigma_dot_coefficient,
            radius, x, y,
        )

    h = float(step)
    L00 = L(0.0, 0.0)
    H = np.empty((2, 2), dtype=float)
    H[0, 0] = (L(h, 0.0) - 2.0*L00 + L(-h, 0.0))/h**2
    H[1, 1] = (L(0.0, h) - 2.0*L00 + L(0.0, -h))/h**2
    H[0, 1] = H[1, 0] = (
        L(h, h) - L(h, -h) - L(-h, h) + L(-h, -h)
    )/(4.0*h**2)
    return 0.5*(H + H.T)


def homothetic_uniform_velocity_hessian(
    *, beta1, beta2, beta3, K, w, mu, radius=0.02, step=1.0e-3,
):
    """Homothetic dust/nonlinear-branch oracle for the velocity Hessian.

    The usually easy-to-miss background ``sigma_dot`` is retained.  On the
    nonlinear Aoki roots with positive effective interaction normalization
    ``D``, the single non-null velocity eigenvalue has the same sign as Aoki's
    ``K_S``.  The separate linear ``mu=0`` branch is not covered by this oracle.
    """
    e = -1.5*(1.0 + w)
    M = mu*(2.0 + mu)
    return uniform_velocity_hessian(
        betas=(0.0, beta1, beta2, beta3, 0.0),
        a=1.0, b=K, c=1.0, mu=mu, mu_dot=0.0,
        sigma_prime_coefficient=-M,
        sigma_dot_coefficient=-(1.0 + e)*M,
        radius=radius, step=step,
    )
