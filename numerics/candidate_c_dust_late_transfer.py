"""Late exact-dust transfer on the strictly on-shell Candidate-C benchmark.

The canonical (Y,Pi) action remains the reference representation, but direct
integration in that frame is poorly scaled at large k. We therefore evolve
the equivalent regular tangent variables w=(Y,Ydot). The post-BD physical
phase Hessian is sampled on the on-shell dust trajectory, interpolated with a
cubic spline, and its spline derivative supplies dH/dN to the exact DAE
reduction in :mod:`de_felice_dust_local_modes`.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np
from scipy.interpolate import CubicSpline

from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_linear_start,
)
from numerics.de_felice_dust_local_modes import dust_dae_local_system
from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
from numerics.canonical_quadratic_evolution import canonical_phase_matrix_N
from numerics.dust_observables import dust_density_maps


@dataclass
class CandidateCDustTrajectory:
    k_hmpc: float
    N_grid: np.ndarray
    hessian_grid: np.ndarray
    common_map_grid: np.ndarray
    relative_map_grid: np.ndarray
    kkt_condition_grid: np.ndarray
    momentum_condition_grid: np.ndarray
    _hessian_spline: CubicSpline
    _common_spline: CubicSpline
    _relative_spline: CubicSpline
    _generator_spline: CubicSpline

    def physical_hessian(self, N: float) -> np.ndarray:
        return np.asarray(self._hessian_spline(float(N)), dtype=float)

    def physical_hessian_N(self, N: float) -> np.ndarray:
        return np.asarray(self._hessian_spline(float(N), 1), dtype=float)

    def local_system(self, N: float):
        a = math.exp(float(N))
        point = candidate_c_dust_background_point(a, k_hmpc=self.k_hmpc)
        Hg = point.metric.H / point.metric.a
        return dust_dae_local_system(
            self.physical_hessian(N), self.physical_hessian_N(N), H_g=Hg,
        )

    def generator_N(self, N: float) -> np.ndarray:
        return np.asarray(self._generator_spline(float(N)), dtype=float)

    def common_map(self, N: float) -> np.ndarray:
        return np.asarray(self._common_spline(float(N)), dtype=float)

    def common_map_N(self, N: float) -> np.ndarray:
        return np.asarray(self._common_spline(float(N), 1), dtype=float)

    def relative_map(self, N: float) -> np.ndarray:
        return np.asarray(self._relative_spline(float(N)), dtype=float)

    def relative_map_N(self, N: float) -> np.ndarray:
        return np.asarray(self._relative_spline(float(N), 1), dtype=float)


def _regular_density_maps(action, point, system) -> tuple[np.ndarray, np.ndarray]:
    """Return common/relative density maps on regular state w=(Y,Ydot)."""
    H = np.asarray(action.physical_phase_hessian, dtype=float)
    active = np.arange(8)
    H8 = H[np.ix_(active, active)]
    M = H8[:5, :5]
    C = H8[:5, 5:8]
    K = H8[5:8, 5:8]
    pmap = np.asarray(system.momentum_map, dtype=float)

    xmap = np.zeros((5, 6), dtype=float)
    xmap[:3, :3] = np.eye(3, dtype=float)
    xmap[3:5, :] = pmap
    vmap = np.zeros((3, 6), dtype=float)
    vmap[:, 3:6] = np.eye(3, dtype=float)
    pi_map = C.T @ xmap + K @ vmap
    canonical_map = np.zeros((6, 6), dtype=float)
    canonical_map[:3, :3] = np.eye(3, dtype=float)
    canonical_map[3:6, :] = pi_map
    zmap = np.asarray(action.bd_state_map, dtype=float) @ canonical_map

    rho_g = point.rho_g_m
    rho_f = point.rho_f_m
    n = point.metric.xi * point.metric.c
    pref_f = n * point.metric.xi**3
    dg = pmap[0] / rho_g
    df = pmap[1] / (pref_f * rho_f) - 3.0 * zmap
    relative = dg - df
    wg = rho_g
    wf = pref_f * rho_f
    common = (wg * dg + wf * df) / (wg + wf)
    return np.asarray(common, dtype=float), np.asarray(relative, dtype=float)


def build_candidate_c_dust_trajectory(
    k_hmpc: float,
    *,
    grid_size: int = 321,
    action_derivative_step_N: float = 2.0e-3,
) -> CandidateCDustTrajectory:
    """Precompute the on-shell post-BD dust action and observable maps."""
    kh = float(k_hmpc)
    if not (math.isfinite(kh) and kh > 0.0):
        raise ValueError("k_hmpc must be finite and positive")
    if int(grid_size) < 21:
        raise ValueError("grid_size must be at least 21")
    N0 = math.log(candidate_c_dust_linear_start())
    N_grid = np.linspace(N0, 0.0, int(grid_size))
    # The physical Hessian derivative is cancellation-sensitive at the start
    # of the late interval. Padding by the coarse public-grid spacing is not
    # enough: even apparently converged transfer ratios can share the same
    # biased boundary derivative. Insert a small conditioned stencil around
    # both boundaries while leaving the public output grid unchanged.
    h_boundary = min(float(action_derivative_step_N), 2.0e-3)
    boundary_offsets = h_boundary * np.arange(-4, 5, dtype=float)
    refined = np.concatenate([
        N_grid,
        N_grid[0] + boundary_offsets,
        N_grid[-1] + boundary_offsets,
    ])
    sample_N = np.unique(np.asarray(refined, dtype=float))
    actions = []
    hessians = []
    for N in sample_N:
        a = math.exp(float(N))
        action = candidate_c_dust_canonical_action(
            a, k_hmpc=kh, derivative_step_N=action_derivative_step_N,
        )
        actions.append(action)
        hessians.append(action.physical_phase_hessian)
    sample_hessians = np.asarray(hessians, dtype=float)
    hs = CubicSpline(sample_N, sample_hessians, axis=0)

    common_maps = []
    relative_maps = []
    sample_kkt = []
    sample_pp = []
    sample_generators = []
    for N, action in zip(sample_N, actions):
        a = math.exp(float(N))
        point = candidate_c_dust_background_point(a, k_hmpc=kh)
        Hg = point.metric.H / point.metric.a
        system = dust_dae_local_system(
            action.physical_phase_hessian,
            np.asarray(hs(float(N), 1), dtype=float),
            H_g=Hg,
        )
        common, relative = _regular_density_maps(action, point, system)
        common_maps.append(common)
        relative_maps.append(relative)
        sample_kkt.append(system.kkt_condition_number)
        sample_pp.append(system.momentum_block_condition_number)
        sample_generators.append(system.generator_N)
    sample_common = np.asarray(common_maps, dtype=float)
    sample_relative = np.asarray(relative_maps, dtype=float)
    common_spline = CubicSpline(sample_N, sample_common, axis=0)
    relative_spline = CubicSpline(sample_N, sample_relative, axis=0)
    generator_spline = CubicSpline(
        sample_N, np.asarray(sample_generators, dtype=float), axis=0,
    )
    public = np.searchsorted(sample_N, N_grid)
    if not np.allclose(sample_N[public], N_grid, rtol=0.0, atol=2.0e-14):
        raise RuntimeError("public N grid was not preserved in refined trajectory")
    return CandidateCDustTrajectory(
        k_hmpc=kh,
        N_grid=N_grid,
        hessian_grid=sample_hessians[public],
        common_map_grid=sample_common[public],
        relative_map_grid=sample_relative[public],
        kkt_condition_grid=np.asarray(sample_kkt, dtype=float)[public],
        momentum_condition_grid=np.asarray(sample_pp, dtype=float)[public],
        _hessian_spline=hs,
        _common_spline=common_spline,
        _relative_spline=relative_spline,
        _generator_spline=generator_spline,
    )


def _canonical_density_maps(N: float, k_hmpc: float):
    a = math.exp(float(N))
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    action = candidate_c_dust_canonical_action(
        a, k_hmpc=k_hmpc, derivative_step_N=2.0e-3,
    )
    maps = dust_density_maps(
        action, point.metric, rho_g=point.rho_g_m, rho_f=point.rho_f_m,
    )
    pref_f = (point.metric.xi * point.metric.c) * point.metric.xi**3
    wg = point.rho_g_m
    wf = pref_f * point.rho_f_m
    common = (wg * maps.delta_g_map + wf * maps.delta_f_map) / (wg + wf)
    return action, point, np.asarray(common, dtype=float), np.asarray(maps.delta_relative_map, dtype=float)


def select_gr_connected_adiabatic_mode(*, trajectory: CandidateCDustTrajectory) -> np.ndarray:
    """Return the regular w=(Y,Ydot) GR-matched adiabatic initial state.

    The matching conditions are imposed directly in physical variables and do
    not assume any real/complex classification of instantaneous eigenmodes:

      common=1, relative=0, relative_N=0, common_N=1,
      Y3=0, Y3dot=0.

    In the Eq. (72) g-flat basis ``Y3`` is the relative scalar spatial metric
    mode. Setting its displacement and velocity to zero is the regular GR
    continuation with no independent helicity-0 excitation at the matching
    surface. The six linear conditions determine the six regular DAE phase
    variables uniquely.
    """
    N0 = float(trajectory.N_grid[0])
    A = trajectory.generator_N(N0)
    common = trajectory.common_map(N0)
    relative = trajectory.relative_map(N0)
    common_N = trajectory.common_map_N(N0) + common @ A
    relative_N = trajectory.relative_map_N(N0) + relative @ A
    y3 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=float)
    y3dot = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0], dtype=float)
    constraints = np.vstack([
        common,
        relative,
        relative_N,
        common_N,
        y3,
        y3dot,
    ])
    cond = float(np.linalg.cond(constraints))
    if np.linalg.matrix_rank(constraints) != 6 or not math.isfinite(cond):
        raise np.linalg.LinAlgError(
            f"GR-matched dust initial lift is singular: cond={cond}"
        )
    target = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=float)
    regular_state = np.linalg.solve(constraints, target)
    if not np.all(np.isfinite(regular_state)):
        raise np.linalg.LinAlgError("non-finite GR-matched initial state")
    return np.asarray(regular_state, dtype=float)


@dataclass(frozen=True)
class LateDustTransferResult:
    a: np.ndarray
    phase_state: np.ndarray
    delta_g: np.ndarray
    delta_f: np.ndarray
    delta_common: np.ndarray
    delta_relative: np.ndarray
    R: np.ndarray
    kkt_condition: np.ndarray
    momentum_condition: np.ndarray


def _sector_densities_from_common_relative(
    N: float,
    *,
    trajectory: CandidateCDustTrajectory,
    common_value: float,
    relative_value: float,
) -> tuple[float, float]:
    point = candidate_c_dust_background_point(math.exp(float(N)), k_hmpc=trajectory.k_hmpc)
    pref_f = (point.metric.xi * point.metric.c) * point.metric.xi**3
    wg = point.rho_g_m
    wf = pref_f * point.rho_f_m
    denom = wg + wf
    dg = common_value + wf / denom * relative_value
    df = common_value - wg / denom * relative_value
    return float(dg), float(df)


def solve_candidate_c_dust_late(
    k_hmpc: float,
    *,
    trajectory: CandidateCDustTrajectory | None = None,
    samples: int = 600,
    rtol: float = 1.0e-9,
    atol: float = 1.0e-12,
    grid_size: int = 401,
) -> LateDustTransferResult:
    """Integrate the GR-connected adiabatic exact-dust mode to today."""
    from scipy.integrate import solve_ivp

    traj = trajectory or build_candidate_c_dust_trajectory(
        k_hmpc, grid_size=grid_size,
    )
    if abs(float(k_hmpc) - traj.k_hmpc) > 1e-14 * max(1.0, abs(traj.k_hmpc)):
        raise ValueError("trajectory k_hmpc does not match requested scale")
    if int(samples) < 2:
        raise ValueError("samples must be at least 2")
    initial = select_gr_connected_adiabatic_mode(trajectory=traj)
    N_eval = np.linspace(float(traj.N_grid[0]), 0.0, int(samples))
    sol = solve_ivp(
        lambda N, w: traj.generator_N(N) @ w,
        (float(N_eval[0]), 0.0),
        initial,
        t_eval=N_eval,
        method="DOP853",
        rtol=float(rtol),
        atol=float(atol),
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    states = np.asarray(sol.y.T, dtype=float)
    common = np.empty(len(N_eval), dtype=float)
    relative = np.empty(len(N_eval), dtype=float)
    dg = np.empty(len(N_eval), dtype=float)
    df = np.empty(len(N_eval), dtype=float)
    kkt = np.empty(len(N_eval), dtype=float)
    pp = np.empty(len(N_eval), dtype=float)
    for i, (N, w) in enumerate(zip(N_eval, states)):
        common[i] = float(traj.common_map(float(N)) @ w)
        relative[i] = float(traj.relative_map(float(N)) @ w)
        dg[i], df[i] = _sector_densities_from_common_relative(
            float(N), trajectory=traj,
            common_value=common[i], relative_value=relative[i],
        )
        local = traj.local_system(float(N))
        kkt[i] = local.kkt_condition_number
        pp[i] = local.momentum_block_condition_number
    tiny = np.finfo(float).tiny
    if np.any(np.abs(common) <= tiny):
        raise np.linalg.LinAlgError("common density crossed numerical zero")
    return LateDustTransferResult(
        a=np.exp(N_eval),
        phase_state=states,
        delta_g=dg,
        delta_f=df,
        delta_common=common,
        delta_relative=relative,
        R=relative/common,
        kkt_condition=kkt,
        momentum_condition=pp,
    )


def fundamental_matrix_candidate_c_dust(
    k_hmpc: float,
    *,
    trajectory: CandidateCDustTrajectory | None = None,
    samples: int = 600,
    rtol: float = 1.0e-9,
    atol: float = 1.0e-12,
    grid_size: int = 401,
) -> np.ndarray:
    """Return sampled 6x6 fundamental matrices for the regular dust system."""
    from scipy.integrate import solve_ivp

    traj = trajectory or build_candidate_c_dust_trajectory(
        k_hmpc, grid_size=grid_size,
    )
    if abs(float(k_hmpc) - traj.k_hmpc) > 1e-14 * max(1.0, abs(traj.k_hmpc)):
        raise ValueError("trajectory k_hmpc does not match requested scale")
    N_eval = np.linspace(float(traj.N_grid[0]), 0.0, int(samples))
    initial = np.eye(6, dtype=float).reshape(-1)

    def rhs(N, flat):
        F = np.asarray(flat, dtype=float).reshape(6, 6)
        return (traj.generator_N(N) @ F).reshape(-1)

    sol = solve_ivp(
        rhs,
        (float(N_eval[0]), 0.0),
        initial,
        t_eval=N_eval,
        method="DOP853",
        rtol=float(rtol),
        atol=float(atol),
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return np.asarray(sol.y.T, dtype=float).reshape(len(N_eval), 6, 6)
