"""Exact-dust scalar stability and mode-character diagnostics."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.dust_mode_tracking import (
    track_eigenpair_branch,
    track_eigenpair_branch_adaptive,
    pair_phase_speed_squared,
)


@dataclass(frozen=True)
class GravityStabilityTrack:
    a: np.ndarray
    eigenvalues: np.ndarray
    cs2: np.ndarray
    overlap_scores: np.ndarray
    zero_crossings_a: tuple[float, ...]
    late_healthy_start_a: float | None


@dataclass(frozen=True)
class PrincipalGravityStability:
    a: np.ndarray
    cs2: np.ndarray
    eigenvalue_pairs: np.ndarray
    zero_crossings_a: tuple[float, ...]
    late_healthy_start_a: float | None


def _zero_crossings(a: np.ndarray, values: np.ndarray) -> tuple[float, ...]:
    out: list[float] = []
    for i in range(len(values)-1):
        u = float(values[i]); v = float(values[i+1])
        if not (math.isfinite(u) and math.isfinite(v)):
            continue
        if u == 0.0:
            out.append(float(a[i]))
            continue
        if u*v < 0.0:
            frac = -u/(v-u)
            out.append(float(a[i] + frac*(a[i+1]-a[i])))
    if values[-1] == 0.0:
        out.append(float(a[-1]))
    return tuple(out)


def _late_healthy_start(a: np.ndarray, values: np.ndarray, crossings: tuple[float, ...]) -> float | None:
    if float(values[-1]) < 0.0:
        return None
    if np.all(values >= 0.0):
        return float(a[0])
    for i in range(len(values)-2, -1, -1):
        if values[i] < 0.0 and values[i+1] >= 0.0:
            u = float(values[i]); v = float(values[i+1])
            frac = -u/(v-u) if v != u else 0.0
            return float(a[i] + frac*(a[i+1]-a[i]))
    return float(crossings[-1]) if crossings else float(a[0])


def track_gravity_stability(
    a_grid,
    generators_cosmic,
    *,
    k: float,
    anchor_pair: tuple[int, int] | None = None,
    state_scale=None,
) -> GravityStabilityTrack:
    """Transport one spectral pair continuously from a chosen late anchor."""
    a = np.asarray(a_grid, dtype=float)
    G = np.asarray(generators_cosmic, dtype=float)
    kk = float(k)
    if a.ndim != 1 or len(a) < 2 or not np.all(np.isfinite(a)) or np.any(a <= 0.0):
        raise ValueError("a_grid must be a finite positive one-dimensional grid")
    if not np.all(np.diff(a) > 0.0):
        raise ValueError("a_grid must increase toward today")
    if G.shape != (len(a), 6, 6):
        raise ValueError("generators_cosmic must have shape (len(a_grid),6,6)")
    if not (math.isfinite(kk) and kk > 0.0):
        raise ValueError("k must be finite and positive")

    branch = track_eigenpair_branch(
        G,
        anchor_index=-1,
        anchor_pair=anchor_pair,
        state_scale=state_scale,
    )
    cs2 = np.asarray([
        pair_phase_speed_squared(branch.eigenvalues[i], a=float(a[i]), k=kk)
        for i in range(len(a))
    ], dtype=float)
    crossings = _zero_crossings(a, cs2)
    return GravityStabilityTrack(
        a=a.copy(),
        eigenvalues=np.asarray(branch.eigenvalues, dtype=complex),
        cs2=cs2,
        overlap_scores=np.asarray(branch.overlap_scores, dtype=float),
        zero_crossings_a=crossings,
        late_healthy_start_a=_late_healthy_start(a, cs2, crossings),
    )


def principal_gravity_stability(
    a_grid,
    generators_cosmic,
    *,
    k: float,
) -> PrincipalGravityStability:
    """Identify the finite-speed principal scalar pair locally at each point.

    In the exact pressureless system the two dust pairs have phase products
    that vanish as k^-2, while the helicity-0 principal pair retains an O(1)
    squared phase speed.  At the production high-k scales it is the pair with
    the largest local |lambda|.  This diagnostic deliberately tracks *mode
    character*, not eigenpair identity through an avoided crossing.
    """
    a = np.asarray(a_grid, dtype=float)
    G = np.asarray(generators_cosmic, dtype=float)
    kk = float(k)
    if a.ndim != 1 or len(a) < 2 or not np.all(np.isfinite(a)) or np.any(a <= 0.0):
        raise ValueError("a_grid must be a finite positive one-dimensional grid")
    if not np.all(np.diff(a) > 0.0):
        raise ValueError("a_grid must increase toward today")
    if G.shape != (len(a), 6, 6) or not np.all(np.isfinite(G)):
        raise ValueError("generators_cosmic must be finite with shape (len(a_grid),6,6)")
    if not (math.isfinite(kk) and kk > 0.0):
        raise ValueError("k must be finite and positive")

    pairs = np.empty((len(a), 2), dtype=complex)
    cs2 = np.empty(len(a), dtype=float)
    for i, matrix in enumerate(G):
        values = np.linalg.eigvals(matrix)
        if not np.all(np.isfinite(values)):
            raise np.linalg.LinAlgError(f"non-finite scalar spectrum at index {i}")
        pair = values[np.argsort(np.abs(values))[-2:]]
        pairs[i] = pair
        cs2[i] = float(np.real(pair[0]*pair[1]) * (a[i]/kk)**2)
    crossings = _zero_crossings(a, cs2)
    return PrincipalGravityStability(
        a=a.copy(),
        cs2=cs2,
        eigenvalue_pairs=pairs,
        zero_crossings_a=crossings,
        late_healthy_start_a=_late_healthy_start(a, cs2, crossings),
    )


def _candidate_generator_cosmic(trajectory, kh: float, N: float):
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    a = math.exp(float(N))
    point = candidate_c_dust_background_point(a, k_hmpc=kh)
    Hg = point.metric.H / point.metric.a
    return Hg * trajectory.generator_N(float(N)), point


def track_candidate_c_dust_gravity(
    k_hmpc: float,
    *,
    samples: int = 81,
    trajectory=None,
    state_scale=None,
    min_overlap: float = 0.90,
    max_refinements: int = 8,
) -> GravityStabilityTrack:
    """Transport today's gravity-connected pair backward through mode mixing.

    Low overlap that persists after refinement is returned rather than hidden:
    it marks a genuine quasi-degenerate/mixed cluster.  This transported-pair
    diagnostic must not be substituted for the principal stability test.
    """
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory

    kh = float(k_hmpc)
    if not (math.isfinite(kh) and kh > 0.0):
        raise ValueError("k_hmpc must be finite and positive")
    if int(samples) < 11:
        raise ValueError("samples must be at least 11")
    traj = trajectory or build_candidate_c_dust_trajectory(kh, grid_size=max(21, int(samples)))
    N0 = float(traj.N_grid[0])
    initial_N = np.linspace(N0, 0.0, int(samples))

    def generator(N: float) -> np.ndarray:
        return _candidate_generator_cosmic(traj, kh, N)[0]

    N, branch = track_eigenpair_branch_adaptive(
        generator,
        initial_N,
        anchor_index=-1,
        state_scale=state_scale,
        min_score=float(min_overlap),
        max_refinements=int(max_refinements),
        allow_unresolved_cluster=True,
    )
    a = np.exp(N)
    point0 = candidate_c_dust_background_point(float(a[0]), k_hmpc=kh)
    k_h0 = math.sqrt(point0.metric.k2)
    cs2 = np.asarray([
        pair_phase_speed_squared(branch.eigenvalues[i], a=float(a[i]), k=k_h0)
        for i in range(len(a))
    ], dtype=float)
    crossings = _zero_crossings(a, cs2)
    return GravityStabilityTrack(
        a=np.asarray(a, dtype=float),
        eigenvalues=np.asarray(branch.eigenvalues, dtype=complex),
        cs2=cs2,
        overlap_scores=np.asarray(branch.overlap_scores, dtype=float),
        zero_crossings_a=crossings,
        late_healthy_start_a=_late_healthy_start(a, cs2, crossings),
    )


def candidate_c_dust_principal_stability(
    k_hmpc: float,
    *,
    samples: int = 241,
    trajectory=None,
) -> PrincipalGravityStability:
    """Map the exact-dust finite-speed principal stability to today."""
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory

    kh = float(k_hmpc)
    if not (math.isfinite(kh) and kh > 0.0):
        raise ValueError("k_hmpc must be finite and positive")
    if int(samples) < 41:
        raise ValueError("samples must be at least 41")
    traj = trajectory or build_candidate_c_dust_trajectory(kh, grid_size=max(41, int(samples)))
    N = np.linspace(float(traj.N_grid[0]), 0.0, int(samples))
    a = np.exp(N)
    generators = np.empty((len(N), 6, 6), dtype=float)
    for i, Ni in enumerate(N):
        generators[i] = _candidate_generator_cosmic(traj, kh, float(Ni))[0]
    point0 = candidate_c_dust_background_point(float(a[0]), k_hmpc=kh)
    return principal_gravity_stability(
        a,
        generators,
        k=math.sqrt(point0.metric.k2),
    )
