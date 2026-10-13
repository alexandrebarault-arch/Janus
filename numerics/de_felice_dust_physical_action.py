"""BD reduction and six-dimensional canonical Hamiltonian for two dust sectors."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.bd_time_canonicalization import canonicalize_linear_rate_time_dependent
from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_params,
)
from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_two_dust_action import eliminate_flat_gauge_two_dust
from numerics.de_felice_two_matter_action import bd_basis_transform


@dataclass(frozen=True)
class DustCanonicalAction:
    transformed_hessian: np.ndarray
    canonical_hessian: np.ndarray
    physical_phase_hessian: np.ndarray
    hamiltonian_hessian: np.ndarray
    kkt_matrix: np.ndarray
    velocity_momentum_map: np.ndarray
    matter_momentum_map: np.ndarray
    bd_state_map: np.ndarray
    bd_algebraic_coefficient: float
    zdot_kinetic_residual: float
    pdot_residual: float
    kkt_condition_number: float
    dot_c: np.ndarray
    zdot_column: np.ndarray


def _extended_bd_transform(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
) -> np.ndarray:
    """Map 6 state/rate variables to reduced old variables.

    Old reduced order is ``(Sigma,S,q_g,q_f, their rates, p_g,p_f)``.
    New state order is ``(Y1,Y2,Y3,Z,p_g,p_f)`` followed by their six rates.
    The two phase momenta are states; their rates do not enter before the BD
    integration by parts.
    """
    base = bd_basis_transform(bg, bgp)
    transform = np.zeros((10, 12), dtype=float)
    cols = [0, 1, 2, 3, 6, 7, 8, 9]
    transform[np.ix_(range(8), cols)] = base
    transform[8, 4] = 1.0
    transform[9, 5] = 1.0
    return transform


def _transformed_dust_hessian(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    rho_g: float,
    rho_f: float,
) -> np.ndarray:
    reduced = eliminate_flat_gauge_two_dust(
        bg, bgp, betas=betas, rho_g=rho_g, rho_f=rho_f,
    )
    transform = _extended_bd_transform(bg, bgp)
    H = transform.T @ reduced.reduced_hessian @ transform
    return 0.5 * (H + H.T)


def _hamiltonian_from_physical_phase_hessian(
    H: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Legendre-KKT reduce the first-order dust action to (Y,Pi).

    ``H`` has state order ``(Y1,Y2,Y3,p_g,p_f)`` and rate order
    ``(Y1dot,Y2dot,Y3dot,p_gdot,p_fdot)``. The last two rates vanish
    structurally. The definitions of the three canonical momenta and the two
    algebraic equations dL/dp=0 form a 5x5 linear KKT system for
    ``(Ydot1,Ydot2,Ydot3,p_g,p_f)``.
    """
    H = np.asarray(H, dtype=float)
    if H.shape != (10, 10):
        raise ValueError("physical dust phase Hessian must be 10x10")
    M = H[:5, :5]
    C = H[:5, 5:8]
    K = H[5:8, 5:8]
    C_y = C[:3, :]
    C_p = C[3:5, :]
    M_py = M[3:5, :3]
    M_pp = M[3:5, 3:5]

    G = np.block([[K, C_p.T], [C_p, M_pp]])
    rank = int(np.linalg.matrix_rank(G))
    cond = float(np.linalg.cond(G))
    if rank != 5 or not math.isfinite(cond):
        raise np.linalg.LinAlgError(
            f"dust Legendre-KKT block invalid: rank={rank}, cond={cond}"
        )

    rhs_map = np.block([
        [-C_y.T, np.eye(3, dtype=float)],
        [-M_py, np.zeros((2, 3), dtype=float)],
    ])
    solution_map = np.linalg.solve(G, rhs_map)
    velocity_map = solution_map[:3, :]
    p_map = solution_map[3:5, :]

    x_map = np.zeros((5, 6), dtype=float)
    x_map[:3, :3] = np.eye(3, dtype=float)
    x_map[3:5, :] = p_map
    pi_selector = np.zeros((3, 6), dtype=float)
    pi_selector[:, 3:6] = np.eye(3, dtype=float)

    lagrangian_hessian = (
        x_map.T @ M @ x_map
        + x_map.T @ C @ velocity_map
        + velocity_map.T @ C.T @ x_map
        + velocity_map.T @ K @ velocity_map
    )
    canonical_term_hessian = (
        pi_selector.T @ velocity_map + velocity_map.T @ pi_selector
    )
    hamiltonian = canonical_term_hessian - lagrangian_hessian
    hamiltonian = 0.5 * (hamiltonian + hamiltonian.T)
    return hamiltonian, G, solution_map, cond


def dust_canonical_action(
    bg: ScalarBackground,
    bgp: ScalarBackgroundDerivatives,
    *,
    betas,
    rho_g: float,
    rho_f: float,
    dot_c,
    mu_measure: float,
) -> DustCanonicalAction:
    """Perform time-dependent BD reduction and exact dust Legendre reduction."""
    transformed = _transformed_dust_hessian(
        bg, bgp, betas=betas, rho_g=rho_g, rho_f=rho_f,
    )
    n = 6
    z = 3
    dc = np.asarray(dot_c, dtype=float)
    if dc.shape != (n,) or not np.all(np.isfinite(dc)):
        raise ValueError("dot_c must be a finite length-6 vector")
    c = transformed[:n, n + z].copy()

    Kraw = transformed[n:, n:]
    scale = max(1.0, float(np.linalg.norm(Kraw, ord=np.inf)))
    zdot_residual = float(max(
        np.linalg.norm(Kraw[z, :], ord=np.inf),
        np.linalg.norm(Kraw[:, z], ord=np.inf),
    ) / scale)

    canonical = canonicalize_linear_rate_time_dependent(
        transformed, dot_c=dc, mu_measure=mu_measure, z_index=z,
    )

    keep11 = [i for i in range(12) if i != n + z]
    H11 = canonical[np.ix_(keep11, keep11)]
    hzz = float(H11[z, z])
    hscale = max(1.0, float(np.linalg.norm(H11, ord=np.inf)))
    if abs(hzz) <= 1e-14 * hscale:
        raise np.linalg.LinAlgError("BD dust scalar is not algebraically invertible")
    phys = [i for i in range(11) if i != z]
    hpz = H11[np.ix_(phys, [z])]
    physical = H11[np.ix_(phys, phys)] - hpz @ hpz.T / hzz
    physical = 0.5 * (physical + physical.T)

    p_rate = [8, 9]
    pscale = max(1.0, float(np.linalg.norm(physical, ord=np.inf)))
    pdot_residual = float(max(
        np.linalg.norm(physical[p_rate, :], ord=np.inf),
        np.linalg.norm(physical[:, p_rate], ord=np.inf),
    ) / pscale)
    if pdot_residual > 1e-8:
        raise np.linalg.LinAlgError(
            f"unexpected dust-momentum rate residual {pdot_residual:.6g}"
        )

    hamiltonian, kkt, solution_map, kkt_cond = _hamiltonian_from_physical_phase_hessian(
        physical,
    )

    physical_map = np.zeros((10, 6), dtype=float)
    physical_map[:3, :3] = np.eye(3, dtype=float)
    physical_map[3:5, :] = solution_map[3:5, :]
    physical_map[5:8, :] = solution_map[:3, :]
    bd_row_physical = -H11[z, phys] / hzz
    bd_state_map = bd_row_physical @ physical_map
    matter_momentum_map = solution_map[3:5, :].copy()

    return DustCanonicalAction(
        transformed_hessian=np.asarray(transformed, dtype=float),
        canonical_hessian=np.asarray(canonical, dtype=float),
        physical_phase_hessian=np.asarray(physical, dtype=float),
        hamiltonian_hessian=np.asarray(hamiltonian, dtype=float),
        kkt_matrix=np.asarray(kkt, dtype=float),
        velocity_momentum_map=np.asarray(solution_map, dtype=float),
        matter_momentum_map=np.asarray(matter_momentum_map, dtype=float),
        bd_state_map=np.asarray(bd_state_map, dtype=float),
        bd_algebraic_coefficient=hzz,
        zdot_kinetic_residual=zdot_residual,
        pdot_residual=pdot_residual,
        kkt_condition_number=kkt_cond,
        dot_c=np.asarray(dc, dtype=float),
        zdot_column=np.asarray(c, dtype=float),
    )


def _candidate_transformed(a: float, k_hmpc: float) -> tuple[np.ndarray, object]:
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    betas = (0.0, p.beta1, p.beta2, p.beta3, p.beta4)
    H = _transformed_dust_hessian(
        point.metric, point.derivatives, betas=betas,
        rho_g=point.rho_g_m, rho_f=point.rho_f_m,
    )
    return H, point


def candidate_c_dust_canonical_action(
    a: float,
    *,
    k_hmpc: float,
    derivative_step_N: float = 1.0e-4,
) -> DustCanonicalAction:
    """Build the strict on-shell Candidate-C dust canonical action."""
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    h = float(derivative_step_N)
    if not (h > 0.0 and h < 0.05 and math.isfinite(h)):
        raise ValueError("derivative_step_N must lie in (0,0.05)")

    _, point = _candidate_transformed(a, k_hmpc)
    samples = []
    for offset in (-2.0, -1.0, 1.0, 2.0):
        H, _ = _candidate_transformed(a * math.exp(offset * h), k_hmpc)
        samples.append(H[:6, 6 + 3])
    dm2, dm1, dp1, dp2 = samples
    dc_dN = (dm2 - 8.0 * dm1 + 8.0 * dp1 - dp2) / (12.0 * h)
    H_g = point.metric.H / point.metric.a
    dot_c = H_g * dc_dN
    mu_measure = 3.0 * H_g

    p = candidate_c_dust_params()
    betas = (0.0, p.beta1, p.beta2, p.beta3, p.beta4)
    return dust_canonical_action(
        point.metric, point.derivatives, betas=betas,
        rho_g=point.rho_g_m, rho_f=point.rho_f_m,
        dot_c=dot_c, mu_measure=mu_measure,
    )
