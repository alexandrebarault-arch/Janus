"""Exact Candidate-C background adapter for Gate 2B scalar transfer work.

The perturbation equations use g-sector conformal time. This module evaluates
the Candidate-C algebraic FLRW branch and converts the background quantities
from ``flrw_two_matter.py`` into the Comelli scalar conventions, including
analytic first conformal-time derivatives needed by the acceleration system.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.flrw_two_matter import (
    candidate_c,
    positive_real_roots,
    friedmann_g,
)
from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives


_HUBBLE_DISTANCE_MPC_OVER_H = 2997.92458


@dataclass(frozen=True)
class CandidateCBackgroundPoint:
    y: float
    y_N: float
    y_NN: float
    metric: ScalarBackground
    derivatives: ScalarBackgroundDerivatives
    rho_g_m: float
    rho_g_r: float
    rho_f_m: float


def k_hmpc_to_h0(k_hmpc: float) -> float:
    """Convert comoving k in h/Mpc to dimensionless k/(H0/c)."""
    if k_hmpc < 0.0:
        raise ValueError("k_hmpc must be non-negative")
    return float(k_hmpc) * _HUBBLE_DISTANCE_MPC_OVER_H


def _candidate_c_y(a: float) -> float:
    p = candidate_c()
    roots = positive_real_roots(float(a), p)
    if roots.size == 0:
        raise RuntimeError(f"Candidate C has no positive branch root at a={a}")
    # The Candidate-C branch containing y0 is the largest positive root at
    # late times; it becomes the unique positive root at higher redshift.
    return float(roots[-1])


def _y_log_derivatives(a: float, y: float) -> tuple[float, float]:
    """Return dy/dN and d2y/dN2 from the implicit Candidate-C quartic."""
    p = candidate_c()
    m2 = p.m2_over_H02
    a2 = p.alpha**2

    c4 = a2 * m2 * p.beta3 / 3.0
    c3 = a2 * m2 * p.beta2 - m2 * p.beta4 / 3.0
    c2 = a2 * m2 * p.beta1 - m2 * p.beta3
    omega_m = p.omega_g_m0 * a**-3
    omega_r = p.omega_g_r0 * a**-4

    c1_N = a2 * (-3.0 * omega_m - 4.0 * omega_r)
    c0_N = 3.0 * p.omega_f_m0 * p.y0**3 * a**-3
    c1_NN = a2 * (9.0 * omega_m + 16.0 * omega_r)
    c0_NN = -9.0 * p.omega_f_m0 * p.y0**3 * a**-3

    # Only the y and constant quartic coefficients depend explicitly on N.
    p_y = 4.0*c4*y**3 + 3.0*c3*y**2 + 2.0*c2*y + (
        a2*(omega_m+omega_r) - m2*p.beta2
    )
    if abs(p_y) < 1e-14:
        raise RuntimeError("Candidate-C branch derivative is singular")
    p_N = c1_N*y + c0_N
    y_N = -p_N/p_y

    p_yy = 12.0*c4*y**2 + 6.0*c3*y + 2.0*c2
    p_Ny = c1_N
    p_NN = c1_NN*y + c0_NN
    y_NN = -(p_NN + 2.0*p_Ny*y_N + p_yy*y_N**2)/p_y
    return float(y_N), float(y_NN)


def candidate_c_background_point(
    a: float,
    *,
    k_hmpc: float,
) -> CandidateCBackgroundPoint:
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")

    p = candidate_c()
    y = _candidate_c_y(float(a))
    y_N, y_NN = _y_log_derivatives(float(a), y)

    c = 1.0 + y_N/y
    c_N = y_NN/y - (y_N/y)**2

    J = p.beta1 + 2.0*p.beta2*y + p.beta3*y**2
    J_y = 2.0*p.beta2 + 2.0*p.beta3*y
    J_yy = 2.0*p.beta3
    f2 = y*J
    f2_N = y_N*(J + y*J_y)
    f1 = y*J + 0.5*(c-1.0)*y**2*J_y
    f1_N = (
        f2_N
        + 0.5*c_N*y**2*J_y
        + 0.5*(c-1.0)*y_N*(2.0*y*J_y + y**2*J_yy)
    )

    E2 = float(friedmann_g(float(a), y, p))
    if E2 <= 0.0:
        raise RuntimeError("Candidate-C H^2 is non-positive")
    E_phys = math.sqrt(E2)
    omega_m = p.omega_g_m0*a**-3
    omega_r = p.omega_g_r0*a**-4
    E2_N = -3.0*omega_m - 4.0*omega_r + p.m2_over_H02*J*y_N
    E_phys_N = E2_N/(2.0*E_phys)

    # H below is the conformal Hubble rate calH=a H_phys in H0 units.
    H = a*E_phys
    H_N = H + a*E_phys_N
    H_prime = H*H_N
    H_omega = c*H
    H_omega_N = c_N*H + c*H_N
    H_omega_prime = H*H_omega_N

    xi_prime = H*y_N
    c_prime = H*c_N
    f1_prime = H*f1_N
    f2_prime = H*f2_N

    k = k_hmpc_to_h0(k_hmpc)
    metric = ScalarBackground(
        a=float(a),
        m2=p.m2_over_H02,
        f1=float(f1),
        f2=float(f2),
        H=float(H),
        H_omega=float(H_omega),
        c=float(c),
        xi=float(y),
        kappa=float(p.alpha**2),
        k2=float(k*k),
        G8pi=1.0,
    )
    derivatives = ScalarBackgroundDerivatives(
        H_prime=float(H_prime),
        H_omega_prime=float(H_omega_prime),
        c_prime=float(c_prime),
        xi_prime=float(xi_prime),
        f1_prime=float(f1_prime),
        f2_prime=float(f2_prime),
    )

    rho_g_m = 3.0*p.omega_g_m0*a**-3
    rho_g_r = 3.0*p.omega_g_r0*a**-4
    rho_f_m = 3.0*p.omega_f_m0*(p.y0/(a*y))**3

    return CandidateCBackgroundPoint(
        y=float(y),
        y_N=float(y_N),
        y_NN=float(y_NN),
        metric=metric,
        derivatives=derivatives,
        rho_g_m=float(rho_g_m),
        rho_g_r=float(rho_g_r),
        rho_f_m=float(rho_f_m),
    )
