"""Reduced scalar metric closure for JANUS-R Gate 2B.

The physical perturbation state is taken to be

    (E, E', delta_m, u_m, delta_r, u_r, delta_f, u_f)

where visible dust and radiation couple to g and twin dust couples to f.
The metric potentials are not evolved as independent degrees of freedom.
Instead, at every background point they are reconstructed from a 12x12
linear system made only from published scalar equations:

- the seven Comelli scalar constraints/gauge identities;
- derivatives of the g and f momentum constraints;
- the g and f spatial-trace Einstein equations;
- the derivative of the g 00 Einstein constraint.

The derivative of the f 00 constraint is deliberately NOT used in the solve.
It is returned as an independent Bianchi/consistency diagnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.candidate_c_transfer import CandidateCBackgroundPoint
from numerics.comelli_dae import (
    ConstraintSolution,
    MatterEvolutionSources,
    MatterSources,
    MetricAccelerationSolution,
    MetricState,
    acceleration_residual_vector,
    constraint_residual_vector,
)


@dataclass(frozen=True)
class FluidPerturbations:
    delta_m: float
    u_m: float
    delta_r: float
    u_r: float
    delta_f: float
    u_f: float

    def as_tuple(self) -> tuple[float, ...]:
        return (
            self.delta_m,
            self.u_m,
            self.delta_r,
            self.u_r,
            self.delta_f,
            self.u_f,
        )


@dataclass(frozen=True)
class MetricClosureSolution:
    """Algebraic metric reconstruction at one time and Fourier scale.

    Vector order:
      Phi1, Phi2, Phi1', Phi2', B1, B2, F1, F2,
      E'', Phi1'', Phi2'', B1'.
    """

    vector: np.ndarray
    condition_number: float
    rank: int
    residual: float
    normalized_residual: float
    f00_bianchi_residual: float
    f00_bianchi_relative: float
    fluid_rates: np.ndarray

    @property
    def Phi1(self): return float(self.vector[0])
    @property
    def Phi2(self): return float(self.vector[1])
    @property
    def Phi1_prime(self): return float(self.vector[2])
    @property
    def Phi2_prime(self): return float(self.vector[3])
    @property
    def B1(self): return float(self.vector[4])
    @property
    def B2(self): return float(self.vector[5])
    @property
    def F1(self): return float(self.vector[6])
    @property
    def F2(self): return float(self.vector[7])
    @property
    def E_double_prime(self): return float(self.vector[8])
    @property
    def Phi1_double_prime(self): return float(self.vector[9])
    @property
    def Phi2_double_prime(self): return float(self.vector[10])
    @property
    def B1_prime(self): return float(self.vector[11])


def _matter_sources(
    point: CandidateCBackgroundPoint,
    fluids: FluidPerturbations,
) -> MatterSources:
    return MatterSources(
        delta_rho_g=(
            point.rho_g_m * fluids.delta_m
            + point.rho_g_r * fluids.delta_r
        ),
        momentum_g=(
            point.rho_g_m * fluids.u_m
            + (4.0 / 3.0) * point.rho_g_r * fluids.u_r
        ),
        delta_rho_f=point.rho_f_m * fluids.delta_f,
        momentum_f=point.rho_f_m * fluids.u_f,
    )


def _psis(point, E: float, Phi1: float, Phi2: float) -> tuple[float, float]:
    bg = point.metric
    psi1 = bg.a**2 * bg.m2 * bg.f1 * E - Phi1
    psi2 = -bg.a**2 * bg.m2 * bg.f1 * E / (
        bg.kappa * bg.c * bg.xi**2
    ) - Phi2
    return psi1, psi2


def _constraint_solution_from_vector(
    vector: np.ndarray,
    E_prime: float,
) -> ConstraintSolution:
    q = np.array(
        [
            E_prime,
            vector[2],
            vector[3],
            vector[4],
            vector[5],
            vector[6],
            vector[7],
        ],
        dtype=float,
    )
    return ConstraintSolution(
        vector=q,
        condition_number=float("nan"),
        reduced_rank=6,
        consistency_residual=float("nan"),
    )


def _fluid_rates_and_evolution(
    point: CandidateCBackgroundPoint,
    *,
    E: float,
    Phi1: float,
    Phi2: float,
    con: ConstraintSolution,
    fluids: FluidPerturbations,
) -> tuple[np.ndarray, MatterEvolutionSources, float, float]:
    """Return conformal-time fluid rates and aggregate source derivatives."""
    bg = point.metric
    bd = point.derivatives
    psi1, psi2 = _psis(point, E, Phi1, Phi2)

    dm_p = bg.k2 * fluids.u_m - 3.0 * con.Phi1_prime
    um_p = -bg.H * fluids.u_m - psi1

    dr_p = (4.0 / 3.0) * (
        bg.k2 * fluids.u_r - 3.0 * con.Phi1_prime
    )
    ur_p = -0.25 * fluids.delta_r - psi1

    df_p = bg.k2 * fluids.u_f - 3.0 * con.Phi2_prime
    uf_p = (
        (-bg.H_omega + bd.c_prime / bg.c) * fluids.u_f
        - bg.c**2 * psi2
    )

    rates = np.array([dm_p, um_p, dr_p, ur_p, df_p, uf_p], dtype=float)

    rho_m_p = -3.0 * bg.H * point.rho_g_m
    rho_r_p = -4.0 * bg.H * point.rho_g_r
    rho_f_p = -3.0 * bg.H_omega * point.rho_f_m

    momentum_g_prime = (
        rho_m_p * fluids.u_m
        + point.rho_g_m * um_p
        + (4.0 / 3.0)
        * (rho_r_p * fluids.u_r + point.rho_g_r * ur_p)
    )
    momentum_f_prime = (
        rho_f_p * fluids.u_f + point.rho_f_m * uf_p
    )

    delta_p_g = point.rho_g_r * fluids.delta_r / 3.0
    delta_p_f = 0.0
    evo = MatterEvolutionSources(
        momentum_g_prime=float(momentum_g_prime),
        momentum_f_prime=float(momentum_f_prime),
        delta_p_g=float(delta_p_g),
        delta_p_f=float(delta_p_f),
    )

    delta_rho_g_prime = (
        rho_m_p * fluids.delta_m
        + point.rho_g_m * dm_p
        + rho_r_p * fluids.delta_r
        + point.rho_g_r * dr_p
    )
    delta_rho_f_prime = (
        rho_f_p * fluids.delta_f + point.rho_f_m * df_p
    )
    return rates, evo, float(delta_rho_g_prime), float(delta_rho_f_prime)


def _psi_primes(
    point: CandidateCBackgroundPoint,
    *,
    E: float,
    con: ConstraintSolution,
) -> tuple[float, float]:
    bg = point.metric
    bd = point.derivatives

    K1 = bg.a**2 * bg.m2 * bg.f1
    K1_p = bg.a**2 * bg.m2 * (bd.f1_prime + 2.0 * bg.H * bg.f1)
    psi1_p = K1_p * E + K1 * con.E_prime - con.Phi1_prime

    pref = bg.a**2 * bg.m2 / (bg.kappa * bg.c * bg.xi**2)
    K2 = pref * bg.f1
    K2_p = pref * (
        bd.f1_prime
        + bg.f1
        * (
            2.0 * bg.H
            - bd.c_prime / bg.c
            - 2.0 * bd.xi_prime / bg.xi
        )
    )
    psi2_p = -K2_p * E - K2 * con.E_prime - con.Phi2_prime
    return float(psi1_p), float(psi2_p)


def _F_primes(
    point: CandidateCBackgroundPoint,
    *,
    Phi1: float,
    Phi2: float,
    con: ConstraintSolution,
    acc: MetricAccelerationSolution,
) -> tuple[float, float]:
    """Differentiate the A.17/A.18 gauge identities."""
    bg = point.metric
    bd = point.derivatives
    dphi = Phi1 - Phi2
    dphi_p = con.Phi1_prime - con.Phi2_prime

    rhs_difference = (
        (bd.H_prime - bd.H_omega_prime) * dphi
        + (bg.H - bg.H_omega) * dphi_p
        - bd.H_omega_prime * con.F2
        + bd.H_prime * con.F1
    )

    rhs_sum = (
        (acc.B1_prime - acc.E_double_prime) * (bg.H + bg.H_omega)
        + (con.B1 - con.E_prime) * (bd.H_prime + bd.H_omega_prime)
        - 4.0 * bg.c * bd.c_prime * dphi
        - 2.0 * bg.c**2 * dphi_p
        - 2.0 * bg.c * bd.c_prime * (con.F1 + con.F2)
    )
    sum_prime = rhs_sum / bg.c**2

    F1_prime = (
        bg.H_omega * sum_prime - rhs_difference
    ) / (bg.H + bg.H_omega)
    F2_prime = sum_prime - F1_prime
    return float(F1_prime), float(F2_prime)


def _00_derivative_diagnostics(
    point: CandidateCBackgroundPoint,
    *,
    E: float,
    Phi1: float,
    Phi2: float,
    con: ConstraintSolution,
    acc: MetricAccelerationSolution,
    src: MatterSources,
    delta_rho_g_prime: float,
    delta_rho_f_prime: float,
) -> tuple[float, float, float]:
    """Return d(g00), d(f00), and absolute-term scale of d(f00)."""
    bg = point.metric
    bd = point.derivatives
    psi1, psi2 = _psis(point, E, Phi1, Phi2)
    psi1_p, psi2_p = _psi_primes(point, E=E, con=con)
    F1_p, F2_p = _F_primes(
        point, Phi1=Phi1, Phi2=Phi2, con=con, acc=acc
    )

    Mg = bg.a**2 * bg.m2 * bg.f2
    Mg_p = bg.a**2 * bg.m2 * (bd.f2_prime + 2.0 * bg.H * bg.f2)
    g_terms = np.array(
        [
            -2.0 * bg.k2 * con.Phi1_prime,
            6.0 * bd.H_prime * (psi1 * bg.H - con.Phi1_prime),
            6.0
            * bg.H
            * (
                psi1_p * bg.H
                + psi1 * bd.H_prime
                - acc.Phi1_double_prime
            ),
            Mg_p * (3.0 * con.F1 + bg.k2 * E),
            Mg * (3.0 * F1_p + bg.k2 * con.E_prime),
            bg.a**2
            * (2.0 * bg.H * src.delta_rho_g + delta_rho_g_prime),
        ],
        dtype=float,
    )
    g_residual = float(np.sum(g_terms))

    xi2 = bg.xi**2
    Q_pref = bg.m2 * bg.a**2 * bg.c**2 / (bg.kappa * xi2)
    Q = Q_pref * bg.f2
    Q_p = Q_pref * (
        bd.f2_prime
        + bg.f2
        * (
            2.0 * bg.H
            + 2.0 * bd.c_prime / bg.c
            - 2.0 * bd.xi_prime / bg.xi
        )
    )
    D = bg.a**2 * bg.c**2 * xi2 / bg.kappa
    D_p = D * (
        2.0 * bg.H
        + 2.0 * bd.c_prime / bg.c
        + 2.0 * bd.xi_prime / bg.xi
    )
    f_terms = np.array(
        [
            -4.0 * bg.c * bd.c_prime * bg.k2 * Phi2,
            -2.0 * bg.c**2 * bg.k2 * con.Phi2_prime,
            6.0
            * bd.H_omega_prime
            * (psi2 * bg.H_omega - con.Phi2_prime),
            6.0
            * bg.H_omega
            * (
                psi2_p * bg.H_omega
                + psi2 * bd.H_omega_prime
                - acc.Phi2_double_prime
            ),
            Q_p * (-bg.k2 * E - 3.0 * con.F2),
            Q * (-bg.k2 * con.E_prime - 3.0 * F2_p),
            D_p * src.delta_rho_f,
            D * delta_rho_f_prime,
        ],
        dtype=float,
    )
    f_residual = float(np.sum(f_terms))
    f_scale = max(float(np.sum(np.abs(f_terms))), np.finfo(float).tiny)
    return g_residual, f_residual, f_scale


def closure_residual_vector(
    vector,
    point: CandidateCBackgroundPoint,
    *,
    E: float,
    E_prime: float,
    fluids: FluidPerturbations,
) -> tuple[np.ndarray, float, float, np.ndarray]:
    """Return 12 solve residuals plus unused f00 Bianchi diagnostic."""
    x = np.asarray(vector, dtype=float)
    if x.shape != (12,):
        raise ValueError("metric closure vector must have length 12")

    Phi1, Phi2 = float(x[0]), float(x[1])
    con = _constraint_solution_from_vector(x, E_prime)
    state = MetricState(E=float(E), Phi1=Phi1, Phi2=Phi2)
    src = _matter_sources(point, fluids)
    constraint_residuals = constraint_residual_vector(
        con.vector, point.metric, state, src
    )

    rates, evo, drho_g_p, drho_f_p = _fluid_rates_and_evolution(
        point,
        E=E,
        Phi1=Phi1,
        Phi2=Phi2,
        con=con,
        fluids=fluids,
    )
    acc = MetricAccelerationSolution(
        vector=np.asarray(x[8:12], dtype=float),
        condition_number=float("nan"),
        rank=4,
    )
    acceleration_residuals = acceleration_residual_vector(
        acc.vector,
        point.metric,
        point.derivatives,
        state,
        con,
        src,
        evo,
    )
    g00_p, f00_p, f00_scale = _00_derivative_diagnostics(
        point,
        E=E,
        Phi1=Phi1,
        Phi2=Phi2,
        con=con,
        acc=acc,
        src=src,
        delta_rho_g_prime=drho_g_p,
        delta_rho_f_prime=drho_f_p,
    )
    residuals = np.concatenate(
        [constraint_residuals, acceleration_residuals, [g00_p]]
    )
    return residuals, f00_p, f00_scale, rates


def solve_metric_closure(
    point: CandidateCBackgroundPoint,
    *,
    E: float,
    E_prime: float,
    fluids: FluidPerturbations,
) -> MetricClosureSolution:
    """Reconstruct all nondynamical metric variables for the 8D state."""
    zero = np.zeros(12, dtype=float)
    base, _, _, _ = closure_residual_vector(
        zero, point, E=E, E_prime=E_prime, fluids=fluids
    )
    A = np.empty((12, 12), dtype=float)
    for j in range(12):
        basis = np.zeros(12, dtype=float)
        basis[j] = 1.0
        r, _, _, _ = closure_residual_vector(
            basis, point, E=E, E_prime=E_prime, fluids=fluids
        )
        A[:, j] = r - base

    rank = int(np.linalg.matrix_rank(A))
    if rank != 12:
        raise np.linalg.LinAlgError(
            f"Reduced metric closure has rank {rank}, expected 12"
        )
    vector = np.linalg.solve(A, -base)
    residuals, f00_p, f00_scale, rates = closure_residual_vector(
        vector, point, E=E, E_prime=E_prime, fluids=fluids
    )
    residual = float(np.linalg.norm(residuals, ord=np.inf))
    normalization = max(
        1.0,
        float(np.linalg.norm(base, ord=np.inf)),
        float(np.linalg.norm(A, ord=np.inf) * np.linalg.norm(vector, ord=np.inf)),
    )
    normalized = residual / normalization

    return MetricClosureSolution(
        vector=vector,
        condition_number=float(np.linalg.cond(A)),
        rank=rank,
        residual=residual,
        normalized_residual=float(normalized),
        f00_bianchi_residual=float(f00_p),
        f00_bianchi_relative=float(abs(f00_p) / f00_scale),
        fluid_rates=np.asarray(rates, dtype=float),
    )
