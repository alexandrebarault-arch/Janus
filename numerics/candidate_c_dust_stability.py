"""Continuous exact-dust gravity-branch stability diagnostics."""
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
    """Track a gravity eigensubspace from today backward on a fixed grid."""
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


def track_candidate_c_dust_gravity(
    k_hmpc: float,
    *,
    samples: int = 81,
    trajectory=None,
    state_scale=None,
    min_overlap: float = 0.90,
    max_refinements: int = 8,
) -> GravityStabilityTrack:
    """Adaptively track the exact-dust Candidate-C-like gravity branch.

    The physical branch is anchored at today and followed backward.  Intervals
    are bisected whenever the bounded spectral-projector continuation score is
    too small, preventing a coarse public sampling choice from silently
    switching to another scalar pair near a quasi-degeneracy.
    """
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory

    kh = float(k_hmpc)
    if not (math.isfinite(kh) and kh > 0.0):
        raise ValueError("k_hmpc must be finite and positive")
    if int(samples) < 11:
        raise ValueError("samples must be at least 11")
    traj = trajectory or build_candidate_c_dust_trajectory(
        kh, grid_size=max(21, int(samples)),
    )
    N0 = float(traj.N_grid[0])
    initial_N = np.linspace(N0, 0.0, int(samples))

    def generator_cosmic(N: float) -> np.ndarray:
        a = math.exp(float(N))
        point = candidate_c_dust_background_point(a, k_hmpc=kh)
        Hg = point.metric.H / point.metric.a
        return Hg * traj.generator_N(float(N))

    N, branch = track_eigenpair_branch_adaptive(
        generator_cosmic,
        initial_N,
        anchor_index=-1,
        state_scale=state_scale,
        min_score=float(min_overlap),
        max_refinements=int(max_refinements),
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
