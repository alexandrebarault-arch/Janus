"""Constraint reduction for the Comelli two-matter scalar system.

The seven scalar constraint/identity equations have rank six when the gauge
invariants are transcribed correctly. E' is therefore a genuine dynamical
input, not an algebraically determined quantity. At fixed E', the remaining
six quantities (Phi1', Phi2', B1, B2, F1, F2) are determined on the physical
constraint manifold.

This is still not the full JANUS-R transfer integrator: the trace/evolution
equations must determine E'' and propagate the dynamical state.
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
    """Solve the six nondynamical quantities after prescribing E'.

    The full 7x7 affine system has rank six. Removing the E' column leaves a
    7x6 full-column-rank system; the seventh equation is a consistency
    condition selecting the physical constraint manifold. Least squares is
    used only to exploit that redundant row, and a non-negligible residual is
    treated as an inconsistent state rather than silently projected away.
    """
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
