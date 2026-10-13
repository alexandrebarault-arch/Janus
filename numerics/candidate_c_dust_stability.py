"""Continuous exact-dust gravity-branch stability diagnostics."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.dust_mode_tracking import track_eigenpair_branch, pair_phase_speed_squared


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
    """Track a gravity eigensubspace from today backward and map its sign.

    ``a_grid`` must increase toward today. The tracked pair is anchored at the
    final point; when ``anchor_pair`` is omitted the generic tracker uses the
    largest-|lambda| late pair.
    """
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
) -> GravityStabilityTrack:
    """Track the exact-dust Candidate-C-like gravity branch to today.

    The production trajectory supplies the conditioned local generator. The
    branch is anchored at today and followed backward by eigensubspace overlap.
    """
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory

    kh = float(k_hmpc)
    if not (math.isfinite(kh) and kh > 0.0):
        raise ValueError("k_hmpc must be finite and positive")
    if int(samples) < 11:
        raise ValueError("samples must be at least 11")
    traj = trajectory or build_candidate_c_dust_trajectory(kh, grid_size=max(21, int(samples)))
    N = np.linspace(float(traj.N_grid[0]), 0.0, int(samples))
    a = np.exp(N)
    generators = np.empty((len(N), 6, 6), dtype=float)
    k_h0 = None
    for i, (Ni, ai) in enumerate(zip(N, a)):
        point = candidate_c_dust_background_point(float(ai), k_hmpc=kh)
        Hg = point.metric.H / point.metric.a
        generators[i] = Hg * traj.generator_N(float(Ni))
        if k_h0 is None:
            k_h0 = math.sqrt(point.metric.k2)
    return track_gravity_stability(
        a,
        generators,
        k=float(k_h0),
        state_scale=state_scale,
    )
