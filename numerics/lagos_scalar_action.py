"""Scalar interaction action for Hassan-Rosen massive bigravity.

This module transcribes the non-derivative scalar interaction terms of
Lagos & Ferreira, arXiv:1610.00553, Eqs. (3.6)-(3.8), specialized to massive
bigravity (their Eqs. 3.13-3.15): constant Planck masses and alpha_L=0.

Only the interaction potential is implemented here. The Einstein-Hilbert
self-actions and matter actions are added in later Gate-2B steps. The purpose
of this module is to pin the Z/Z_tilde structure independently of Comelli.
"""

from __future__ import annotations

import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_action_bridge import lagos_bigravity_parameters


INTERACTION_STATE_ORDER = (
    "Psi1", "Psi2", "E1", "E2", "Phi1", "Phi2", "B1", "B2",
)


def _state(x):
    arr = np.asarray(x, dtype=float)
    if arr.shape != (8,):
        raise ValueError("interaction state must have length 8")
    return arr


def interaction_lagrangian_raw(bg: ScalarBackground, state) -> float:
    """Return L_int/(M1^2 a^3) from Lagos-Ferreira Eqs. (3.6)-(3.8).

    The raw expression keeps r, Nbar, H and Hb in the form appearing in the
    paper, after substituting the Hassan-Rosen specialization and Fourier
    convention partial^2 -> -k^2. On the healthy branch Hb=c H and
    Nbar=r c.
    """
    x = _state(state)
    Psi1, Psi2, E1, E2, Phi1, Phi2, B1, B2 = x
    p = lagos_bigravity_parameters(bg)

    r = p.r
    Nbar = p.Nbar
    Z = p.Z
    Zt = p.Z_tilde
    a = bg.a
    b = a*r
    k2 = bg.k2
    nu2 = 1.0/bg.kappa
    H = bg.H/bg.a
    Hb = bg.c*H

    if r == 0.0 or Nbar == 0.0 or Nbar + r == 0.0:
        raise ValueError("singular Lagos background")

    # Healthy-branch ratio. For c -> 1 both numerator and denominator vanish;
    # its continuous limit is -r/H because Nbar=r*c and Hb=c*H.
    if abs(H-Hb) <= 1e-13*max(1.0, abs(H), abs(Hb)):
        if H == 0.0:
            ratio = 0.0
        else:
            ratio = -r/H
    else:
        ratio = (Nbar-r)/(H-Hb)

    # Metric-1 interaction terms from Eq. (3.6), alpha_L=0 and d ln M1^2=0.
    l1 = (
        r*Z/(2.0*(Nbar+r))*k2*B1*B1
        + 2.0*r*Zt*Psi1*(1.5*Psi1 + a*a*k2*E1)
        + ratio*H*Z*Phi1*(3.0*Psi1 + a*a*k2*E1)
    )

    # Eq. (3.7) is multiplied by Nbar*b^3*M2^2. Relative to M1^2*a^3
    # this gives Nbar*r^3/nu^2. For constant M1 its Z_tilde coefficient is
    # nu^2*Nbar*r^2*(2 Z_tilde), not nu^2*Nbar*r/2; the second '2' in the
    # PDF text extraction is the exponent on r.
    factor2 = Nbar*r**3/nu2
    shift2 = nu2*Nbar*Z/(2.0*r**3*(Nbar+r))*k2*B2*B2
    zt2 = 2.0*nu2*Nbar*r*r*Zt*Psi2*(1.5*Psi2 + b*b*k2*E2)
    if abs(H-Hb) > 1e-13*max(1.0, abs(H), abs(Hb)):
        lapse2 = (
            Hb*nu2*Z*(Nbar-r)/(Nbar*r**3*(H-Hb))
            * Phi2*(3.0*Psi2 + b*b*k2*E2)
        )
    elif H == 0.0:
        # Continuous proportional-background limit is handled directly in
        # interaction_lagrangian_healthy; keep raw expression finite here.
        lapse2 = 0.0
    else:
        lapse2 = (
            -(Hb*nu2*Z)/(Nbar*r**2*H)
            * Phi2*(3.0*Psi2 + b*b*k2*E2)
        )
    l2 = factor2*(shift2+zt2+lapse2)

    # Cross-interaction Eq. (3.8), alpha_L=0 and d ln M1^2=0.
    l12 = (
        -2.0*r*Zt*(
            3.0*Psi2*Psi1
            + a*a*k2*Psi2*E1
            + b*b*k2*Psi1*E2
        )
        - Z*Nbar/(Nbar+r)*k2*B2*B1
        - Z*ratio*(
            H*Phi1*(3.0*Psi2 + b*b*k2*E2)
            + Hb*Phi2*(3.0*Psi1 + a*a*k2*E1)
        )
    )
    return float(l1+l2+l12)


def interaction_lagrangian_healthy(bg: ScalarBackground, state) -> float:
    """Same interaction action after imposing Nbar=r*c and Hb=c*H."""
    x = _state(state)
    Psi1, Psi2, E1, E2, Phi1, Phi2, B1, B2 = x
    p = lagos_bigravity_parameters(bg)

    r = p.r
    Nbar = p.Nbar
    Z = p.Z
    Zt = p.Z_tilde
    c = bg.c
    a = bg.a
    b = a*r
    k2 = bg.k2

    # Direct healthy-branch simplification of the raw transcription.
    return float(
        r*Z/(2.0*(Nbar+r))*k2*B1*B1
        + Nbar*Nbar*Z/(2.0*(Nbar+r))*k2*B2*B2
        - Z*Nbar/(Nbar+r)*k2*B1*B2
        + 2.0*r*Zt*Psi1*(1.5*Psi1 + a*a*k2*E1)
        + 2.0*Nbar*Nbar*r**5*Zt*Psi2*(1.5*Psi2 + b*b*k2*E2)
        - 2.0*r*Zt*(
            3.0*Psi2*Psi1
            + a*a*k2*Psi2*E1
            + b*b*k2*Psi1*E2
        )
        + r*Z*Phi1*(
            3.0*(Psi2-Psi1) + k2*(b*b*E2-a*a*E1)
        )
        + c*r*Z*Phi2*(
            3.0*(Psi1-Psi2) + k2*(a*a*E1-b*b*E2)
        )
    )
