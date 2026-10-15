"""Linear mixed Einstein tensor in Aoki's spherical areal gauge.

The perturbed metric is

    ds^2 = a(eta)^2[-exp(2 phi)deta^2 + exp(2 psi)dr^2 + r^2 dOmega^2].

Only terms linear in ``phi`` and ``psi`` are returned. Derivatives are with
respect to conformal time ``eta`` and are evaluated at one ``(eta,r)`` point.
"""
from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LinearizedMixedEinstein:
    tt: float
    tr: float
    rt: float
    rr: float
    angular: float


def linearized_mixed_einstein(
    *,
    a: float,
    a_prime: float,
    a_second: float,
    r: float,
    phi: float,
    phi_t: float,
    phi_r: float,
    phi_rr: float,
    psi: float,
    psi_t: float,
    psi_tt: float,
    psi_r: float,
) -> LinearizedMixedEinstein:
    """Return ``delta G^mu_nu`` for the spherical areal-gauge scalar metric."""
    vals = (
        a, a_prime, a_second, r,
        phi, phi_t, phi_r, phi_rr,
        psi, psi_t, psi_tt, psi_r,
    )
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if a <= 0.0 or r <= 0.0:
        raise ValueError("a and r must be positive")

    a2 = a*a
    a3 = a2*a
    a4 = a2*a2
    r2 = r*r
    ap = a_prime
    app = a_second

    tt = -2.0*(
        -3.0*r2*phi*ap*ap
        + r2*a*psi_t*ap
        + r*a2*psi_r
        + psi*a2
    )/(r2*a4)

    tr = -2.0*(r*phi_r*ap + a*psi_t)/(r*a3)
    rt = +2.0*(r*phi_r*ap + a*psi_t)/(r*a3)

    rr = 2.0*(
        2.0*r2*phi*a*app
        - r2*phi*ap*ap
        + r2*a*phi_t*ap
        + r*a2*phi_r
        - psi*a2
    )/(r2*a4)

    angular = (
        4.0*r*phi*a*app
        - 2.0*r*phi*ap*ap
        + r*a2*phi_rr
        - r*a2*psi_tt
        + 2.0*r*a*phi_t*ap
        - 2.0*r*a*psi_t*ap
        + a2*phi_r
        - a2*psi_r
    )/(r*a4)

    return LinearizedMixedEinstein(
        tt=float(tt), tr=float(tr), rt=float(rt), rr=float(rr), angular=float(angular)
    )
