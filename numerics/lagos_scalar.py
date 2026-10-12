"""Independent Lagos-Ferreira scalar benchmark helpers for JANUS Gate 2B.

This module starts from the one-matter massive-bigravity notation of
Lagos & Ferreira (arXiv:1410.0207) and maps its interaction combinations
onto the JANUS/Comelli background variables. It is intentionally kept
separate from the Comelli reduction so it can act as an independent audit.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LagosInteractionCoefficients:
    """Dimensionless interaction combinations used in arXiv:1410.0207."""

    Z: float
    Z_tilde: float


@dataclass(frozen=True)
class LagosBeta1RadiationBackground:
    """Exact one-matter beta1-only healthy-branch radiation background."""

    N: float
    a: float
    rho_star: float
    H: float
    H_prime: float
    N_prime: float
    X: float
    X_prime: float
    h: float
    h_prime: float


def lagos_interaction_coefficients(
    beta,
    *,
    xi: float,
    c: float,
) -> LagosInteractionCoefficients:
    """Return the dimensionless Lagos ``Z`` and ``Z_tilde`` combinations.

    With ``N=xi`` and ``X=c`` in arXiv:1410.0207,

        Z       = beta1 + 2 beta2 xi + beta3 xi^2,
        Z_tilde = beta1 + beta2 xi (1+c) + beta3 xi^2 c.

    The scalar equations in that paper multiply these combinations by ``m^2``
    explicitly. Thus ``Z=J`` and ``xi*Z_tilde=Gamma`` in JANUS notation.
    """
    if len(beta) != 5:
        raise ValueError("beta must contain beta_0 through beta_4")
    if not (xi > 0.0 and math.isfinite(xi)):
        raise ValueError("xi must be finite and positive")
    if not math.isfinite(c):
        raise ValueError("c must be finite")

    b1 = float(beta[1])
    b2 = float(beta[2])
    b3 = float(beta[3])
    Z = b1 + 2.0 * b2 * xi + b3 * xi**2
    Z_tilde = b1 + b2 * xi * (1.0 + c) + b3 * xi**2 * c
    return LagosInteractionCoefficients(Z=float(Z), Z_tilde=float(Z_tilde))


def beta1_radiation_background(
    *,
    N: float,
    a: float,
    beta1: float = 1.0,
    m2: float = 1.0,
) -> LagosBeta1RadiationBackground:
    """Exact beta1-only one-matter radiation background in Lagos notation.

    For beta0=beta2=beta3=beta4=0 and w=1/3, Eq. (3.12) gives

        rho_star = m^2 beta1 (1/N - 3N),

    while Eq. (3.4) reduces to H^2=a^2 m^2 beta1/(3N). Conservation fixes
    N' and the healthy-branch identity h=XH then fixes X. Derivatives are
    analytic and are included so later scalar-equation tests need no finite
    differencing of the background.
    """
    if not (0.0 < N < 1.0 / math.sqrt(3.0)):
        raise ValueError("N must lie in the positive-density beta1 radiation branch")
    if not (a > 0.0 and beta1 > 0.0 and m2 > 0.0):
        raise ValueError("a, beta1 and m2 must be positive")

    rho_star = m2 * beta1 * (1.0 / N - 3.0 * N)
    H = a * math.sqrt(m2 * beta1 / (3.0 * N))
    rho_N = m2 * beta1 * (-1.0 / N**2 - 3.0)
    N_prime = -4.0 * H * rho_star / rho_N

    X = 1.0 + N_prime / (N * H)
    X_N = -48.0 * N / (1.0 + 3.0 * N**2) ** 2
    X_prime = X_N * N_prime

    H_prime = H * (H - 0.5 * N_prime / N)
    h = X * H
    h_prime = X_prime * H + X * H_prime

    return LagosBeta1RadiationBackground(
        N=float(N),
        a=float(a),
        rho_star=float(rho_star),
        H=float(H),
        H_prime=float(H_prime),
        N_prime=float(N_prime),
        X=float(X),
        X_prime=float(X_prime),
        h=float(h),
        h_prime=float(h_prime),
    )
