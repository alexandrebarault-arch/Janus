"""Regular local equations for the exact two-dust scalar phase action.

The canonical (Y,Pi) Hamiltonian is mathematically correct but can be badly
conditioned at large Fourier k because the time-dependent canonical momentum
contains high powers of k.  This module derives the equivalent regular
second-order/DAE tangent system directly from the same post-BD phase Hessian.
No physical degree of freedom is projected out.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.candidate_c_dust_background import candidate_c_dust_background_point
from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action


@dataclass(frozen=True)
class DustDAELocalSystem:
    generator_cosmic: np.ndarray
    generator_N: np.ndarray
    momentum_map: np.ndarray
    momentum_rate_map: np.ndarray
    acceleration_map: np.ndarray
    kkt_matrix: np.ndarray
    kkt_condition_number: float
    momentum_block_condition_number: float


def dust_dae_local_system(
    physical_phase_hessian,
    physical_phase_hessian_N,
    *,
    H_g: float,
) -> DustDAELocalSystem:
    """Return the regular six-dimensional (Y,Ydot) tangent system.

    The effective order is ``(Y1,Y2,Y3,p_g,p_f,Y1dot,Y2dot,Y3dot)``.
    Production ``DustCanonicalAction`` retains two additional structural
    ``p_gdot,p_fdot`` rows/columns, yielding a 10x10 Hessian; those rows must
    be numerically zero and are validated before reduction to the effective
    8x8 form.  The derivative argument is ``dH/dN`` along one on-shell
    background trajectory.  The two dust momenta are algebraic and are solved
    exactly at every point.  Differentiating their algebraic equations and
    combining them with the three Euler-Lagrange equations gives a 5x5 KKT
    solve for ``(Yddot,pdot)``.
    """
    H = np.asarray(physical_phase_hessian, dtype=float)
    HN = np.asarray(physical_phase_hessian_N, dtype=float)
    if H.shape != HN.shape or H.shape not in ((8, 8), (10, 10)):
        raise ValueError("dust physical phase Hessians must be matching 8x8 or 10x10")
    if not np.all(np.isfinite(H)) or not np.all(np.isfinite(HN)):
        raise ValueError("dust physical phase Hessians must be finite")
    if H.shape == (10, 10):
        pdot = (8, 9)
        for name, matrix in (("H", H), ("dH/dN", HN)):
            scale = max(1.0, float(np.linalg.norm(matrix, ord=np.inf)))
            residual = max(
                float(np.linalg.norm(matrix[list(pdot), :], ord=np.inf)),
                float(np.linalg.norm(matrix[:, list(pdot)], ord=np.inf)),
            ) / scale
            if residual > 1.0e-8:
                raise np.linalg.LinAlgError(
                    f"non-structural pdot dynamics in {name}: residual={residual:.6g}"
                )
        active = np.arange(8)
        H = H[np.ix_(active, active)]
        HN = HN[np.ix_(active, active)]
    Hg = float(H_g)
    if not math.isfinite(Hg) or Hg <= 0.0:
        raise ValueError("H_g must be finite and positive")
    H = 0.5 * (H + H.T)
    HN = 0.5 * (HN + HN.T)
    Hdot = Hg * HN

    M = H[:5, :5]
    C = H[:5, 5:8]
    K = H[5:8, 5:8]
    Mdot = Hdot[:5, :5]
    Cdot = Hdot[:5, 5:8]
    Kdot = Hdot[5:8, 5:8]

    Myy = M[:3, :3]
    Myp = M[:3, 3:5]
    Mpy = M[3:5, :3]
    Mpp = M[3:5, 3:5]
    Cy = C[:3, :]
    Cp = C[3:5, :]

    Mpyd = Mdot[3:5, :3]
    Mppd = Mdot[3:5, 3:5]
    Cyd = Cdot[:3, :]
    Cpd = Cdot[3:5, :]

    cond_pp = float(np.linalg.cond(Mpp))
    if np.linalg.matrix_rank(Mpp) != 2 or not math.isfinite(cond_pp):
        raise np.linalg.LinAlgError(
            f"dust momentum block invalid: rank={np.linalg.matrix_rank(Mpp)}, "
            f"cond={cond_pp}"
        )

    # Algebraic dust constraint: M_py Y + M_pp p + C_p Ydot = 0.
    momentum_map = np.linalg.solve(
        Mpp,
        -np.hstack([Mpy, Cp]),
    )

    mu = 3.0 * Hg
    Av = Kdot + mu * K + Cy.T - Cy
    By = Cyd.T + mu * Cy.T - Myy
    Bp = Cpd.T + mu * Cp.T - Myp

    top_rhs_map = -np.hstack([By, Av]) - Bp @ momentum_map
    bottom_rhs_map = (
        -np.hstack([Mpyd, Mpy + Cpd])
        - Mppd @ momentum_map
    )

    G = np.block([[K, Cp.T], [Cp, Mpp]])
    rank_g = int(np.linalg.matrix_rank(G))
    cond_g = float(np.linalg.cond(G))
    if rank_g != 5 or not math.isfinite(cond_g):
        raise np.linalg.LinAlgError(
            f"dust tangent KKT block invalid: rank={rank_g}, cond={cond_g}"
        )
    solved = np.linalg.solve(G, np.vstack([top_rhs_map, bottom_rhs_map]))
    acceleration_map = solved[:3, :]
    momentum_rate_map = solved[3:5, :]

    generator_cosmic = np.block([
        [np.zeros((3, 3), dtype=float), np.eye(3, dtype=float)],
        [acceleration_map[:, :3], acceleration_map[:, 3:6]],
    ])
    generator_N = generator_cosmic / Hg
    return DustDAELocalSystem(
        generator_cosmic=np.asarray(generator_cosmic, dtype=float),
        generator_N=np.asarray(generator_N, dtype=float),
        momentum_map=np.asarray(momentum_map, dtype=float),
        momentum_rate_map=np.asarray(momentum_rate_map, dtype=float),
        acceleration_map=np.asarray(acceleration_map, dtype=float),
        kkt_matrix=np.asarray(G, dtype=float),
        kkt_condition_number=cond_g,
        momentum_block_condition_number=cond_pp,
    )


def _candidate_phase_hessian(a: float, k_hmpc: float, action_step: float) -> tuple[np.ndarray, float]:
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    action = candidate_c_dust_canonical_action(
        a, k_hmpc=k_hmpc, derivative_step_N=action_step,
    )
    return action.physical_phase_hessian, point.metric.H / point.metric.a


def candidate_c_dust_local_system(
    a: float,
    *,
    k_hmpc: float,
    action_derivative_step_N: float = 2.0e-3,
    trajectory_derivative_step_N: float = 2.0e-3,
) -> DustDAELocalSystem:
    """Build the regular local DAE system on the strict Candidate-C dust path."""
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    h = float(trajectory_derivative_step_N)
    if not (h > 0.0 and h < 0.03 and math.isfinite(h)):
        raise ValueError("trajectory_derivative_step_N must lie in (0,0.03)")
    H0, Hg = _candidate_phase_hessian(a, k_hmpc, action_derivative_step_N)
    samples = {}
    for offset in (-3, -2, -1, 1, 2, 3):
        H, _ = _candidate_phase_hessian(
            a * math.exp(offset * h), k_hmpc, action_derivative_step_N,
        )
        samples[offset] = H
    HN = (
        -samples[-3] + 9.0 * samples[-2] - 45.0 * samples[-1]
        + 45.0 * samples[1] - 9.0 * samples[2] + samples[3]
    ) / (60.0 * h)
    return dust_dae_local_system(H0, HN, H_g=Hg)


def _pair_slow_roots(roots: np.ndarray) -> list[tuple[complex, complex]]:
    """Pair four slow roots into two dust branches without assuming ordering."""
    roots = list(roots)
    if len(roots) != 4:
        raise ValueError("exactly four slow roots are required")
    pairings = [
        ((0, 1), (2, 3)),
        ((0, 2), (1, 3)),
        ((0, 3), (1, 2)),
    ]
    best = None
    best_score = math.inf
    for p1, p2 in pairings:
        pairs = [(roots[p1[0]], roots[p1[1]]), (roots[p2[0]], roots[p2[1]])]
        # Dust growing/decaying partners have modest pair sums. Cross-pairing
        # a growing root from one sector with a decaying root from the other
        # produces much larger opposing sums.
        score = sum(abs(x + y) for x, y in pairs)
        if score < best_score:
            best_score = score
            best = pairs
    return best


def local_phase_squared_speeds(
    system: DustDAELocalSystem,
    *,
    a: float,
    k: float,
) -> np.ndarray:
    """Return two dust and one gravity principal squared-speed estimators.

    The gravity pair is the two roots with largest absolute frequency.  At
    high k the remaining four roots are the pressureless growing/decaying
    branches; their products vanish as k^-2 when converted to phase speed.
    """
    aa = float(a)
    kk = float(k)
    if not (aa > 0.0 and kk > 0.0 and math.isfinite(aa) and math.isfinite(kk)):
        raise ValueError("a and k must be finite and positive")
    roots = np.linalg.eigvals(system.generator_cosmic)
    if not np.all(np.isfinite(roots)):
        raise np.linalg.LinAlgError("non-finite local DAE eigenvalue")
    order = np.argsort(np.abs(roots))
    slow = roots[order[:4]]
    gravity = roots[order[4:6]]
    factor = (aa / kk) ** 2
    gravity_cs2 = float(np.real(gravity[0] * gravity[1]) * factor)
    dust_pairs = _pair_slow_roots(slow)
    dust = [float(np.real(x * y) * factor) for x, y in dust_pairs]
    dust.sort(key=abs)
    return np.asarray([dust[0], dust[1], gravity_cs2], dtype=float)


def candidate_c_dust_local_squared_speeds(
    a: float,
    *,
    k_hmpc: float,
    action_derivative_step_N: float = 2.0e-3,
    trajectory_derivative_step_N: float = 2.0e-3,
) -> np.ndarray:
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    system = candidate_c_dust_local_system(
        a,
        k_hmpc=k_hmpc,
        action_derivative_step_N=action_derivative_step_N,
        trajectory_derivative_step_N=trajectory_derivative_step_N,
    )
    return local_phase_squared_speeds(
        system, a=a, k=math.sqrt(point.metric.k2),
    )
