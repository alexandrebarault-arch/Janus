"""Independent Lagos-Ferreira scalar benchmark helpers for JANUS Gate 2B.

This module starts from the one-matter massive-bigravity notation of
Lagos & Ferreira (arXiv:1410.0207) and maps its interaction combinations
onto the JANUS/Comelli background variables. It is intentionally kept
separate from the Comelli reduction so it can act as an independent audit.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


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


@dataclass(frozen=True)
class LagosScalarState:
    """Variables needed by the four Lagos auxiliary scalar equations."""

    E1: float
    E1_prime: float
    E2: float
    E2_prime: float
    psi2: float
    psi2_prime: float


@dataclass(frozen=True)
class LagosAuxiliarySolution:
    """Solution order is ``(B1, B2, phi1, phi2)``."""

    vector: np.ndarray
    rank: int
    condition_number: float
    residual: float

    @property
    def B1(self): return float(self.vector[0])

    @property
    def B2(self): return float(self.vector[1])

    @property
    def phi1(self): return float(self.vector[2])

    @property
    def phi2(self): return float(self.vector[3])


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
    """Exact beta1-only one-matter radiation background in Lagos notation."""
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


def lagos_auxiliary_residuals(
    auxiliary,
    bg: LagosBeta1RadiationBackground,
    state: LagosScalarState,
    *,
    k: float,
    w: float,
    beta,
    m2: float = 1.0,
    nu2: float = 1.0,
) -> np.ndarray:
    """Residuals of Lagos-Ferreira Eqs. (3.21),(3.22),(3.25),(3.26).

    Auxiliary-vector order is ``(B1,B2,phi1,phi2)``.  These four equations
    are algebraic in those variables after the gauge ``psi1=chi=0``.
    """
    x = np.asarray(auxiliary, dtype=float)
    if x.shape != (4,):
        raise ValueError("auxiliary vector must have length 4")
    if not (k >= 0.0 and math.isfinite(k)):
        raise ValueError("k must be finite and non-negative")

    B1, B2, phi1, phi2 = x
    coeff = lagos_interaction_coefficients(beta, xi=bg.N, c=bg.X)
    Z = coeff.Z
    k2 = k * k
    a2 = bg.a * bg.a
    combo_g = 3.0 * state.psi2 + k2 * state.E2
    combo_rel = 3.0 * state.psi2 + k2 * (state.E2 - state.E1)

    r21 = (
        2.0 * bg.H * (3.0 * state.psi2_prime + k2 * state.E2_prime)
        + ((1.0 + w) * bg.rho_star * combo_g + m2 * bg.N * Z * combo_rel) * a2
        + 2.0 * (state.psi2 * k2 + bg.H * (3.0 * phi2 * bg.H - k2 * B2))
    )
    r22 = (
        2.0 * (bg.X + 1.0) * state.psi2_prime
        + 2.0 * bg.H * (bg.X + 1.0) * phi2
        - m2 * Z * bg.N * (bg.X * B1 - B2)
        + (1.0 + w) * bg.rho_star * (1.0 + bg.X) * B2
    )
    r25 = (
        2.0 * bg.N * bg.h * k2 * state.E1_prime
        - a2 * nu2 * Z * combo_rel * bg.X**2
        - 2.0 * bg.N * bg.h * k2 * B1 * bg.X
        + 6.0 * phi1 * bg.h**2 * bg.N
    )
    r26 = (
        2.0 * bg.h * phi1 * bg.N * (bg.X + 1.0)
        + nu2 * bg.X * a2 * Z * (bg.X * B1 - B2)
    )
    return np.array([r21, r22, r25, r26], dtype=float)


def solve_lagos_auxiliaries(
    bg: LagosBeta1RadiationBackground,
    state: LagosScalarState,
    *,
    k: float,
    w: float,
    beta,
    m2: float = 1.0,
    nu2: float = 1.0,
) -> LagosAuxiliarySolution:
    """Solve the four algebraic scalar auxiliaries from Eqs. 3.21/22/25/26."""
    zero = np.zeros(4, dtype=float)
    base = lagos_auxiliary_residuals(
        zero, bg, state, k=k, w=w, beta=beta, m2=m2, nu2=nu2
    )
    matrix = np.empty((4, 4), dtype=float)
    for j in range(4):
        basis = np.zeros(4, dtype=float)
        basis[j] = 1.0
        matrix[:, j] = lagos_auxiliary_residuals(
            basis, bg, state, k=k, w=w, beta=beta, m2=m2, nu2=nu2
        ) - base

    rank = int(np.linalg.matrix_rank(matrix))
    if rank != 4:
        raise np.linalg.LinAlgError(
            f"Lagos auxiliary matrix has rank {rank}, expected 4"
        )
    vector = np.linalg.solve(matrix, -base)
    residuals = lagos_auxiliary_residuals(
        vector, bg, state, k=k, w=w, beta=beta, m2=m2, nu2=nu2
    )
    return LagosAuxiliarySolution(
        vector=vector,
        rank=rank,
        condition_number=float(np.linalg.cond(matrix)),
        residual=float(np.linalg.norm(residuals, ord=np.inf)),
    )
