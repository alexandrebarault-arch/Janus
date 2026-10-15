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


def _reduced_action(beta, K, w, mu, radius, mu_dot_delta, sigma_dot_delta):
    # Normalize the control instant to a=H=1. Only the Hessian sign is used.
    e = -1.5*(1.0 + w)
    M = mu*(2.0 + mu)
    sigma_r_coeff = -M
    # sigma_bg=-(a H/2) M r^2, hence d_eta sigma_bg=-(1+e)M r^2/2.
    sigma_t_coeff = -(1.0 + e)*M
    nodes, weights = np.polynomial.legendre.leggauss(64)
    rr = 0.5*radius*(nodes + 1.0)
    ww = 0.5*radius*weights
    total = 0.0
    for r, qw in zip(rr, ww):
        inv = square_root_invariants(
            a=1.0, b=K, c_background=1.0, r=float(r),
            sigma_dot=0.5*r*r*(sigma_t_coeff + sigma_dot_delta),
            sigma_prime=r*sigma_r_coeff,
            mu=mu, mu_dot=mu_dot_delta, mu_prime=0.0,
        )
        total += qw*r*r*float(np.dot(beta, inv.elementary_symmetric))
    return float(total)


def homothetic_uniform_velocity_hessian(
    *, beta1, beta2, beta3, K, w, mu, radius=0.02, step=1.0e-3,
):
    """Return the 2x2 velocity Hessian for uniform ``(delta mu, delta sigma)``.

    The background includes both ``sigma_r`` and the usually easy-to-miss
    ``sigma_dot`` implied by the adiabatic Aoki map.  On a positive-effective-
    mass dust branch the single non-null eigenvalue has the same ghost sign as
    Aoki's ``K_S``.  This function is not a gradient/sound-speed diagnostic.
    """
    if radius <= 0.0 or step <= 0.0:
        raise ValueError("radius and step must be positive")
    beta = np.array([0.0, beta1, beta2, beta3, 0.0], dtype=float)

    def L(x, y):
        return _reduced_action(beta, K, w, mu, radius, x, y)

    h = float(step)
    L00 = L(0.0, 0.0)
    H = np.empty((2, 2), dtype=float)
    H[0, 0] = (L(h, 0.0) - 2.0*L00 + L(-h, 0.0))/h**2
    H[1, 1] = (L(0.0, h) - 2.0*L00 + L(0.0, -h))/h**2
    H[0, 1] = H[1, 0] = (
        L(h, h) - L(h, -h) - L(-h, h) + L(-h, -h)
    )/(4.0*h**2)
    return 0.5*(H + H.T)
