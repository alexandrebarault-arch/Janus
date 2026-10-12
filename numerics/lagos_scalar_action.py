"""Scalar quadratic action for Hassan-Rosen massive bigravity.

Transcribes the scalar metric terms of Lagos & Ferreira, arXiv:1610.00553,
Eqs. (3.6)-(3.8), specialized to massive bigravity: constant Planck masses
and alpha_L=0.  Matter perturbation actions are intentionally not included yet.

All returned Lagrangians use the common normalization M1^2 a^3 and Fourier
convention partial^2 -> -k^2.
"""

from __future__ import annotations

import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_action_bridge import lagos_bigravity_parameters


INTERACTION_STATE_ORDER = (
    "Psi1", "Psi2", "E1", "E2", "Phi1", "Phi2", "B1", "B2",
)
RATE_ORDER = ("Psi1_dot", "Psi2_dot", "E1_dot", "E2_dot")


def _state(x):
    arr = np.asarray(x, dtype=float)
    if arr.shape != (8,):
        raise ValueError("scalar state must have length 8")
    return arr


def _rates(v):
    arr = np.asarray(v, dtype=float)
    if arr.shape != (4,):
        raise ValueError("scalar rate vector must have length 4")
    return arr


def interaction_lagrangian_raw(bg: ScalarBackground, state) -> float:
    x = _state(state)
    Psi1, Psi2, E1, E2, Phi1, Phi2, B1, B2 = x
    p = lagos_bigravity_parameters(bg)
    r, Nbar, Z, Zt = p.r, p.Nbar, p.Z, p.Z_tilde
    a, b, k2 = bg.a, bg.a*p.r, bg.k2
    nu2 = 1.0/bg.kappa
    H = bg.H/bg.a
    Hb = bg.c*H
    if r == 0.0 or Nbar == 0.0 or Nbar+r == 0.0:
        raise ValueError("singular Lagos background")
    if abs(H-Hb) <= 1e-13*max(1.0, abs(H), abs(Hb)):
        ratio = 0.0 if H == 0.0 else -r/H
    else:
        ratio = (Nbar-r)/(H-Hb)

    l1 = (
        r*Z/(2.0*(Nbar+r))*k2*B1*B1
        + 2.0*r*Zt*Psi1*(1.5*Psi1+a*a*k2*E1)
        + ratio*H*Z*Phi1*(3.0*Psi1+a*a*k2*E1)
    )
    factor2 = Nbar*r**3/nu2
    shift2 = nu2*Nbar*Z/(2.0*r**3*(Nbar+r))*k2*B2*B2
    zt2 = 2.0*nu2*Nbar*r*r*Zt*Psi2*(1.5*Psi2+b*b*k2*E2)
    if abs(H-Hb) > 1e-13*max(1.0, abs(H), abs(Hb)):
        lapse2 = Hb*nu2*Z*(Nbar-r)/(Nbar*r**3*(H-Hb))*Phi2*(3.0*Psi2+b*b*k2*E2)
    elif H == 0.0:
        lapse2 = 0.0
    else:
        lapse2 = -(Hb*nu2*Z)/(Nbar*r**2*H)*Phi2*(3.0*Psi2+b*b*k2*E2)
    l2 = factor2*(shift2+zt2+lapse2)
    l12 = (
        -2.0*r*Zt*(3.0*Psi2*Psi1+a*a*k2*Psi2*E1+b*b*k2*Psi1*E2)
        - Z*Nbar/(Nbar+r)*k2*B2*B1
        - Z*ratio*(H*Phi1*(3.0*Psi2+b*b*k2*E2)+Hb*Phi2*(3.0*Psi1+a*a*k2*E1))
    )
    return float(l1+l2+l12)


def interaction_lagrangian_healthy(bg: ScalarBackground, state) -> float:
    x = _state(state)
    Psi1, Psi2, E1, E2, Phi1, Phi2, B1, B2 = x
    p = lagos_bigravity_parameters(bg)
    r, Nbar, Z, Zt = p.r, p.Nbar, p.Z, p.Z_tilde
    c, a, b, k2 = bg.c, bg.a, bg.a*p.r, bg.k2
    return float(
        r*Z/(2.0*(Nbar+r))*k2*B1*B1
        + Nbar*Nbar*Z/(2.0*(Nbar+r))*k2*B2*B2
        - Z*Nbar/(Nbar+r)*k2*B1*B2
        + 2.0*r*Zt*Psi1*(1.5*Psi1+a*a*k2*E1)
        + 2.0*Nbar*Nbar*r**5*Zt*Psi2*(1.5*Psi2+b*b*k2*E2)
        - 2.0*r*Zt*(3.0*Psi2*Psi1+a*a*k2*Psi2*E1+b*b*k2*Psi1*E2)
        + r*Z*Phi1*(3.0*(Psi2-Psi1)+k2*(b*b*E2-a*a*E1))
        + c*r*Z*Phi2*(3.0*(Psi1-Psi2)+k2*(a*a*E1-b*b*E2))
    )


def einstein_hilbert_lagrangian(bg: ScalarBackground, state, rates) -> float:
    """Pure EH scalar self-actions, common-normalized by M1^2 a^3.

    This is the non-interaction metric part of Lagos Eqs. (3.6)-(3.7) for
    constant Planck masses. The explicit metric-1 matter-background correction
    to Phi1^2 is not included here; matter is added separately later.
    """
    Psi1, Psi2, E1, E2, Phi1, Phi2, B1, B2 = _state(state)
    P1d, P2d, E1d, E2d = _rates(rates)
    p = lagos_bigravity_parameters(bg)
    r, Nbar = p.r, p.Nbar
    a, b, k2 = bg.a, bg.a*r, bg.k2
    H = bg.H/bg.a
    Hb = bg.H_omega/bg.a
    if Nbar == 0.0:
        raise ValueError("Nbar must be non-zero")

    l1 = (
        -3.0*P1d*P1d - 6.0*H*P1d*Phi1
        - 2.0*a*a*k2*E1d*(P1d+H*Phi1)
        + 2.0*k2*P1d*B1
        + k2*Psi1*Psi1 - 2.0*k2*Phi1*Psi1
        + 2.0*H*k2*Phi1*B1 - 3.0*H*H*Phi1*Phi1
    )
    l2_inner = (
        -3.0*P2d*P2d/(Nbar*Nbar)
        - 6.0*Hb*P2d*Phi2/(Nbar*Nbar)
        - 2.0*b*b*k2*E2d*(P2d+Hb*Phi2)/(Nbar*Nbar)
        + 2.0*k2*P2d*B2/Nbar
        + k2*Psi2*Psi2 - 2.0*k2*Phi2*Psi2
        + 2.0*Hb*k2*Phi2*B2/Nbar
        - 3.0*Hb*Hb*Phi2*Phi2/(Nbar*Nbar)
    )
    factor2 = Nbar*r**3*bg.kappa
    return float(l1 + factor2*l2_inner)


def pure_metric_lagrangian_healthy(bg: ScalarBackground, state, rates) -> float:
    return float(
        einstein_hilbert_lagrangian(bg, state, rates)
        + interaction_lagrangian_healthy(bg, state)
    )


def velocity_hessian(bg: ScalarBackground) -> np.ndarray:
    """Hessian d^2 L/d(rate_i)d(rate_j) at zero fields/rates."""
    zero_s = np.zeros(8, dtype=float)
    n = len(RATE_ORDER)
    Hmat = np.empty((n, n), dtype=float)
    basis = np.eye(n)
    Lbasis = [pure_metric_lagrangian_healthy(bg, zero_s, e) for e in basis]
    for i in range(n):
        Hmat[i, i] = 2.0*Lbasis[i]
        for j in range(i+1, n):
            mixed = pure_metric_lagrangian_healthy(bg, zero_s, basis[i]+basis[j])
            hij = mixed-Lbasis[i]-Lbasis[j]
            Hmat[i, j] = Hmat[j, i] = hij
    return Hmat
