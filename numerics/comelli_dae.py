"""Constraint and acceleration reduction for the Comelli two-matter scalars.

The seven scalar constraint/identity equations have rank six when the gauge
invariants are transcribed correctly. E' is therefore a genuine dynamical
input, not an algebraically determined quantity. At fixed E', the remaining
six quantities (Phi1', Phi2', B1, B2, F1, F2) are determined on the physical
constraint manifold.

Differentiating the two momentum constraints and combining them with the two
spatial-trace Einstein equations gives a 4x4 system for
(E'', Phi1'', Phi2'', B1'). This supplies the metric acceleration layer needed
by a future full transfer integrator while keeping the published equations
independently auditable.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class ScalarBackground:
    a: float
    m2: float
    f1: float
    f2: float
    H: float
    H_omega: float
    c: float
    xi: float
    kappa: float
    k2: float
    G8pi: float = 1.0


@dataclass(frozen=True)
class ScalarBackgroundDerivatives:
    H_prime: float
    H_omega_prime: float
    c_prime: float
    xi_prime: float
    f1_prime: float
    f2_prime: float


@dataclass(frozen=True)
class MetricState:
    E: float
    Phi1: float
    Phi2: float


@dataclass(frozen=True)
class MatterSources:
    delta_rho_g: float
    momentum_g: float
    delta_rho_f: float
    momentum_f: float


@dataclass(frozen=True)
class MatterEvolutionSources:
    momentum_g_prime: float
    momentum_f_prime: float
    delta_p_g: float
    delta_p_f: float


@dataclass(frozen=True)
class ConstraintSolution:
    vector: np.ndarray
    condition_number: float
    reduced_rank: int
    consistency_residual: float

    @property
    def E_prime(self): return float(self.vector[0])
    @property
    def Phi1_prime(self): return float(self.vector[1])
    @property
    def Phi2_prime(self): return float(self.vector[2])
    @property
    def B1(self): return float(self.vector[3])
    @property
    def B2(self): return float(self.vector[4])
    @property
    def F1(self): return float(self.vector[5])
    @property
    def F2(self): return float(self.vector[6])


@dataclass(frozen=True)
class MetricAccelerationSolution:
    vector: np.ndarray
    condition_number: float
    rank: int

    @property
    def E_double_prime(self): return float(self.vector[0])
    @property
    def Phi1_double_prime(self): return float(self.vector[1])
    @property
    def Phi2_double_prime(self): return float(self.vector[2])
    @property
    def B1_prime(self): return float(self.vector[3])


def _psis(bg: ScalarBackground, s: MetricState) -> tuple[float, float]:
    psi1 = bg.a**2 * bg.m2 * bg.f1 * s.E - s.Phi1
    psi2 = -bg.a**2 * bg.m2 * bg.f1 * s.E / (
        bg.kappa * bg.c * bg.xi**2
    ) - s.Phi2
    return psi1, psi2


def constraint_residual_vector(q, bg: ScalarBackground, s: MetricState,
                               src: MatterSources) -> np.ndarray:
    q = np.asarray(q, dtype=float)
    E_p, P1_p, P2_p, B1, B2, F1, F2 = q
    psi1, psi2 = _psis(bg, s)
    c2 = bg.c**2
    xi2 = bg.xi**2

    g00 = (
        -2.0 * bg.k2 * s.Phi1
        + 6.0 * bg.H * (psi1 * bg.H - P1_p)
        + bg.a**2 * bg.m2 * bg.f2 * (3.0 * F1 + bg.k2 * s.E)
        + bg.G8pi * bg.a**2 * src.delta_rho_g
    )
    f00 = (
        -2.0 * c2 * bg.k2 * s.Phi2
        + 6.0 * bg.H_omega * (psi2 * bg.H_omega - P2_p)
        + bg.m2 * bg.a**2 * bg.f2 * c2 / (bg.kappa * xi2)
        * (-bg.k2 * s.E - 3.0 * F2)
        + bg.G8pi / bg.kappa * bg.a**2 * c2 * xi2 * src.delta_rho_f
    )
    g0i = (
        2.0 * psi1 * bg.H
        - 2.0 * P1_p
        + bg.a**2 * bg.m2 * B1 * bg.f2 / (1.0 + bg.c)
        + bg.G8pi * bg.a**2 * src.momentum_g
    )
    f0i = (
        2.0 * bg.c * (psi2 * bg.H_omega - P2_p)
        - bg.m2 * bg.a**2 * bg.f2 * B2
        / (bg.kappa * xi2 * (1.0 + bg.c))
        + bg.G8pi / bg.kappa * bg.c * bg.a**2 * xi2 * src.momentum_f
    )
    a1 = B2 - B1 + (1.0 - c2) * E_p
    a17 = (
        bg.H_omega * F2 - bg.H * F1
        - (bg.H - bg.H_omega) * (s.Phi1 - s.Phi2)
    )
    # Direct substitution of the gauge-invariant definitions gives B1-E'.
    # The searchable PDF text layer drops this prime in A.3/A.18.
    a18 = (
        c2 * (F2 + F1)
        - (B1 - E_p) * (bg.H + bg.H_omega)
        + 2.0 * c2 * (s.Phi1 - s.Phi2)
    )
    return np.array([g00, f00, g0i, f0i, a1, a17, a18], dtype=float)


def constraint_matrix(bg: ScalarBackground, s: MetricState,
                      src: MatterSources) -> tuple[np.ndarray, np.ndarray]:
    z = np.zeros(7, dtype=float)
    b = constraint_residual_vector(z, bg, s, src)
    A = np.empty((7, 7), dtype=float)
    for j in range(7):
        e = np.zeros(7, dtype=float)
        e[j] = 1.0
        A[:, j] = constraint_residual_vector(e, bg, s, src) - b
    return A, b


def solve_metric_constraints(
    bg: ScalarBackground,
    s: MetricState,
    src: MatterSources,
    *,
    E_prime: float,
    consistency_rtol: float = 1e-10,
) -> ConstraintSolution:
    """Solve the six nondynamical quantities after prescribing E'."""
    A, b = constraint_matrix(bg, s, src)
    reduced = A[:, 1:]
    rhs = -(b + A[:, 0] * float(E_prime))
    x, _, rank, _ = np.linalg.lstsq(reduced, rhs, rcond=None)
    rank = int(rank)
    if rank != 6:
        raise np.linalg.LinAlgError(
            f"Reduced scalar constraint matrix has rank {rank}, expected 6"
        )

    q = np.concatenate(([float(E_prime)], x))
    residual = float(np.linalg.norm(A @ q + b, ord=np.inf))
    scale = max(1.0, float(np.linalg.norm(rhs, ord=np.inf)))
    if residual > consistency_rtol * scale:
        raise ValueError(
            "State is off the scalar constraint manifold: "
            f"residual={residual:.6g}, scale={scale:.6g}"
        )

    return ConstraintSolution(
        vector=q,
        condition_number=float(np.linalg.cond(reduced)),
        reduced_rank=rank,
        consistency_residual=residual,
    )


def _psi_primes(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    s: MetricState,
    con: ConstraintSolution,
) -> tuple[float, float]:
    if bg.c == 0.0 or bg.xi == 0.0 or bg.kappa == 0.0:
        raise ValueError("c, xi and kappa must be non-zero")
    K1 = bg.a**2 * bg.m2 * bg.f1
    K1_p = bg.a**2 * bg.m2 * (
        bgp.f1_prime + 2.0 * bg.H * bg.f1
    )
    psi1_p = K1_p * s.E + K1 * con.E_prime - con.Phi1_prime

    K2_pref = bg.a**2 * bg.m2 / (bg.kappa * bg.c * bg.xi**2)
    K2 = K2_pref * bg.f1
    K2_p = K2_pref * (
        bgp.f1_prime
        + bg.f1 * (
            2.0 * bg.H
            - bgp.c_prime / bg.c
            - 2.0 * bgp.xi_prime / bg.xi
        )
    )
    psi2_p = -K2_p * s.E - K2 * con.E_prime - con.Phi2_prime
    return psi1_p, psi2_p


def acceleration_residual_vector(
    acceleration,
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    s: MetricState,
    con: ConstraintSolution,
    src: MatterSources,
    evo: MatterEvolutionSources,
) -> np.ndarray:
    """Residuals of d(0i)_g, d(0i)_f, trace_g and trace_f."""
    E_pp, P1_pp, P2_pp, B1_p = np.asarray(acceleration, dtype=float)
    if bg.c == 0.0 or bg.xi == 0.0 or bg.kappa == 0.0:
        raise ValueError("c, xi and kappa must be non-zero")

    psi1, psi2 = _psis(bg, s)
    psi1_p, psi2_p = _psi_primes(bg, bgp, s, con)
    c2 = bg.c**2
    xi2 = bg.xi**2

    Cg_pref = bg.a**2 * bg.m2 / (1.0 + bg.c)
    Cg = Cg_pref * bg.f2
    Cg_p = Cg_pref * (
        bgp.f2_prime
        + bg.f2 * (2.0 * bg.H - bgp.c_prime / (1.0 + bg.c))
    )
    dg0i = (
        2.0 * bgp.H_prime * psi1
        + 2.0 * bg.H * psi1_p
        - 2.0 * P1_pp
        + Cg_p * con.B1
        + Cg * B1_p
        + bg.G8pi * bg.a**2
        * (2.0 * bg.H * src.momentum_g + evo.momentum_g_prime)
    )

    Cf_pref = bg.m2 * bg.a**2 / (
        bg.kappa * xi2 * (1.0 + bg.c)
    )
    Cf = Cf_pref * bg.f2
    Cf_p = Cf_pref * (
        bgp.f2_prime
        + bg.f2 * (
            2.0 * bg.H
            - 2.0 * bgp.xi_prime / bg.xi
            - bgp.c_prime / (1.0 + bg.c)
        )
    )
    Df = bg.G8pi / bg.kappa * bg.c * bg.a**2 * xi2
    Df_p = Df * (
        bgp.c_prime / bg.c
        + 2.0 * bg.H
        + 2.0 * bgp.xi_prime / bg.xi
    )
    B2_p = (
        B1_p
        + 2.0 * bg.c * bgp.c_prime * con.E_prime
        - (1.0 - c2) * E_pp
    )
    df0i = (
        2.0 * bgp.c_prime * (psi2 * bg.H_omega - con.Phi2_prime)
        + 2.0 * bg.c * (
            psi2_p * bg.H_omega
            + psi2 * bgp.H_omega_prime
            - P2_pp
        )
        - Cf_p * con.B2
        - Cf * B2_p
        + Df_p * src.momentum_f
        + Df * evo.momentum_f_prime
    )

    a_diff = (
        (con.B1 - con.E_prime)
        * (bg.c * (bg.H - bg.H_omega) - bgp.c_prime)
        / c2
    )
    a_sum = (
        2.0 * bg.c**3 * (psi2 - psi1)
        + con.B1 * (
            bg.c * (bg.H_omega + bg.H) - 3.0 * bgp.c_prime
        )
        + 3.0 * bgp.c_prime * con.E_prime
        + bg.c * (
            2.0 * B1_p
            - 2.0 * E_pp
            - con.E_prime * (bg.H_omega + bg.H)
        )
    ) / c2
    A1 = 0.5 * (a_sum - a_diff)
    A2 = 0.5 * (a_sum + a_diff)

    gtrace = (
        bg.m2 * bg.a**2 * (2.0 * bg.f1 * con.F1 + bg.f2 * A1)
        + 2.0 * psi1 * (bg.H**2 + 2.0 * bgp.H_prime)
        - 2.0 * P1_pp
        - 2.0 * bg.H * (2.0 * con.Phi1_prime - psi1_p)
        - bg.G8pi * bg.a**2 * evo.delta_p_g
    )
    ftrace = (
        bg.m2 * bg.a**2 / (bg.kappa * xi2)
        * (2.0 * bg.c * bg.f1 * con.F2 + bg.f2 * A2)
        + 2.0 * (
            bg.H_omega**2
            + 2.0 * bgp.H_omega_prime
            - 2.0 * (bgp.c_prime / bg.c) * bg.H_omega
        ) * psi2
        - 2.0 * P2_pp
        + 2.0 * (
            bgp.c_prime / bg.c - 2.0 * bg.H_omega
        ) * con.Phi2_prime
        + 2.0 * bg.H_omega * psi2_p
        - bg.G8pi / bg.kappa * bg.a**2 * c2 * xi2 * evo.delta_p_f
    )
    return np.array([dg0i, df0i, gtrace, ftrace], dtype=float)


def acceleration_matrix(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    s: MetricState,
    con: ConstraintSolution,
    src: MatterSources,
    evo: MatterEvolutionSources,
) -> tuple[np.ndarray, np.ndarray]:
    z = np.zeros(4, dtype=float)
    b = acceleration_residual_vector(z, bg, bgp, s, con, src, evo)
    A = np.empty((4, 4), dtype=float)
    for j in range(4):
        e = np.zeros(4, dtype=float)
        e[j] = 1.0
        A[:, j] = (
            acceleration_residual_vector(e, bg, bgp, s, con, src, evo) - b
        )
    return A, b


def solve_metric_accelerations(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    s: MetricState,
    con: ConstraintSolution,
    src: MatterSources,
    evo: MatterEvolutionSources,
) -> MetricAccelerationSolution:
    A, b = acceleration_matrix(bg, bgp, s, con, src, evo)
    rank = int(np.linalg.matrix_rank(A))
    if rank != 4:
        raise np.linalg.LinAlgError(
            f"Metric acceleration matrix has rank {rank}, expected 4"
        )
    vector = np.linalg.solve(A, -b)
    return MetricAccelerationSolution(
        vector=vector,
        condition_number=float(np.linalg.cond(A)),
        rank=rank,
    )
