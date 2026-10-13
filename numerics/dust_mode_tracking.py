"""Continuous tracking helpers for local scalar eigenmode pairs."""
from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
import math
import numpy as np


@dataclass(frozen=True)
class TrackedEigenpairBranch:
    eigenvalues: np.ndarray
    overlap_scores: np.ndarray
    pair_indices: np.ndarray


def is_real_dynamical_pair(values, *, rtol: float = 1e-7) -> bool:
    vals = np.asarray(values, dtype=complex)
    if vals.shape != (2,) or not np.all(np.isfinite(vals)):
        return False
    scale = max(1.0, float(np.max(np.abs(vals))))
    if np.max(np.abs(vals.imag)) <= rtol * scale:
        return True
    return abs(vals[1] - np.conj(vals[0])) <= rtol * scale or abs(vals[0] - np.conj(vals[1])) <= rtol * scale


def _anchor_pair(values: np.ndarray) -> tuple[int, int]:
    vals = np.asarray(values, dtype=complex)
    candidates = []
    for pair in combinations(range(len(vals)), 2):
        vp = vals[list(pair)]
        if is_real_dynamical_pair(vp):
            candidates.append((float(np.sum(np.abs(vp))), pair))
    if not candidates:
        raise np.linalg.LinAlgError("no valid real/conjugate eigenpair at anchor")
    return max(candidates, key=lambda item: item[0])[1]


def _eigensystem(matrix: np.ndarray, state_scale):
    G = np.asarray(matrix, dtype=float)
    if state_scale is not None:
        s = np.asarray(state_scale, dtype=float)
        if s.shape != (G.shape[0],) or not np.all(np.isfinite(s)) or np.any(s <= 0.0):
            raise ValueError("state_scale must be a finite positive vector matching state size")
        G = (s[:, None] * G) / s[None, :]
    values, vectors = np.linalg.eig(G)
    try:
        inverse = np.linalg.inv(vectors)
    except np.linalg.LinAlgError as exc:
        raise np.linalg.LinAlgError("local eigenvector matrix is singular") from exc
    return values, vectors, inverse


def _pair_projector(vectors: np.ndarray, inverse: np.ndarray, pair: tuple[int, int]) -> np.ndarray:
    return vectors[:, list(pair)] @ inverse[list(pair), :]


def _projector_overlap(Pa: np.ndarray, Pb: np.ndarray) -> float:
    """Return a bounded similarity-invariant continuation score."""
    A = np.asarray(Pa, dtype=complex)
    B = np.asarray(Pb, dtype=complex)
    if A.shape != B.shape or A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("spectral projectors must be matching square matrices")
    rank = max(1, int(round(float(np.trace(A).real))))
    eig = np.linalg.eigvals(A @ B)
    active = eig[np.argsort(np.abs(eig))[-rank:]]
    distance = float(np.max(np.abs(active - 1.0)))
    return 1.0 / (1.0 + distance)


def track_eigenpair_branch(
    generators,
    *,
    anchor_index: int = -1,
    anchor_pair: tuple[int, int] | None = None,
    state_scale=None,
) -> TrackedEigenpairBranch:
    """Track one spectral pair by biorthogonal-projector continuity."""
    G = np.asarray(generators, dtype=float)
    if G.ndim != 3 or G.shape[1] != G.shape[2] or G.shape[0] < 1:
        raise ValueError("generators must have shape (n_points,n,n)")
    if not np.all(np.isfinite(G)):
        raise ValueError("generators must be finite")
    npts, n, _ = G.shape
    ai = int(anchor_index)
    if ai < 0:
        ai += npts
    if ai < 0 or ai >= npts:
        raise IndexError("anchor_index is out of range")

    specs = [_eigensystem(matrix, state_scale) for matrix in G]
    vals0, V0, W0 = specs[ai]
    pair0 = _anchor_pair(vals0) if anchor_pair is None else tuple(map(int, anchor_pair))
    if len(pair0) != 2 or pair0[0] == pair0[1] or min(pair0) < 0 or max(pair0) >= n:
        raise ValueError("anchor_pair must contain two distinct valid eigenvalue indices")
    if not is_real_dynamical_pair(vals0[list(pair0)]):
        raise ValueError("anchor_pair must be a real or conjugate dynamical pair")

    out_vals = np.empty((npts, 2), dtype=complex)
    out_pairs = np.empty((npts, 2), dtype=int)
    scores = np.full(npts, np.nan, dtype=float)
    out_vals[ai] = vals0[list(pair0)]
    out_pairs[ai] = pair0
    scores[ai] = 1.0
    anchor_projector = _pair_projector(V0, W0, pair0)

    def walk(indices, initial_projector, initial_values):
        prev_projector = initial_projector
        prev_vals = np.asarray(initial_values, dtype=complex)
        for i in indices:
            values, vectors, inverse = specs[i]
            best = None
            best_key = None
            for pair in combinations(range(n), 2):
                vp = values[list(pair)]
                if not is_real_dynamical_pair(vp):
                    continue
                projector = _pair_projector(vectors, inverse, pair)
                overlap = _projector_overlap(prev_projector, projector)
                aa = np.sort_complex(vp)
                bb = np.sort_complex(prev_vals)
                scale = max(1.0, float(np.max(np.abs(bb))))
                continuity = float(np.sum(np.abs(aa-bb)) / scale)
                key = (overlap, -continuity)
                if best_key is None or key > best_key:
                    best_key = key
                    best = (pair, projector, vp, overlap)
            if best is None:
                raise np.linalg.LinAlgError(f"no valid spectral pair at point {i}")
            pair, prev_projector, vp, overlap = best
            out_pairs[i] = pair
            out_vals[i] = vp
            scores[i] = overlap
            prev_vals = vp

    walk(range(ai+1, npts), anchor_projector, out_vals[ai])
    walk(range(ai-1, -1, -1), anchor_projector, out_vals[ai])
    return TrackedEigenpairBranch(out_vals, scores, out_pairs)


def track_eigenpair_branch_adaptive(
    generator,
    parameters,
    *,
    anchor_index: int = -1,
    anchor_pair: tuple[int, int] | None = None,
    state_scale=None,
    min_score: float = 0.90,
    max_refinements: int = 8,
    allow_unresolved_cluster: bool = False,
) -> tuple[np.ndarray, TrackedEigenpairBranch]:
    """Track a pair while bisecting intervals with weak subspace continuity.

    A genuine exceptional/quasi-degenerate cluster can keep every individual
    two-dimensional spectral projector ill-conditioned no matter how much the
    interval is refined.  With ``allow_unresolved_cluster=True`` the best
    refined branch is returned and its low overlap score is deliberately kept
    as a mode-mixing diagnostic instead of being mislabeled as numerical
    failure.
    """
    grid = np.asarray(parameters, dtype=float)
    if grid.ndim != 1 or len(grid) < 2 or not np.all(np.isfinite(grid)):
        raise ValueError("parameters must be a finite one-dimensional grid")
    if not np.all(np.diff(grid) > 0.0):
        raise ValueError("parameters must be strictly increasing")
    score_min = float(min_score)
    if not (0.0 < score_min < 1.0):
        raise ValueError("min_score must lie in (0,1)")
    ai0 = int(anchor_index)
    if ai0 in (-1, len(grid)-1):
        endpoint = -1
    elif ai0 == 0:
        endpoint = 0
    else:
        raise ValueError("adaptive tracking requires a first- or last-point anchor")
    refinements = int(max_refinements)
    if refinements < 0:
        raise ValueError("max_refinements must be non-negative")

    cache: dict[float, np.ndarray] = {}
    def matrix(x: float) -> np.ndarray:
        key = float(x)
        if key not in cache:
            value = np.asarray(generator(key), dtype=float)
            if value.ndim != 2 or value.shape[0] != value.shape[1] or not np.all(np.isfinite(value)):
                raise ValueError("generator must return a finite square matrix")
            cache[key] = value
        return cache[key]

    branch = None
    for level in range(refinements + 1):
        matrices = np.asarray([matrix(x) for x in grid])
        branch = track_eigenpair_branch(
            matrices,
            anchor_index=(-1 if endpoint == -1 else 0),
            anchor_pair=anchor_pair,
            state_scale=state_scale,
        )
        anchor = len(grid)-1 if endpoint == -1 else 0
        bad: list[tuple[int, int]] = []
        for i, score in enumerate(branch.overlap_scores):
            if i == anchor:
                continue
            if float(score) < score_min:
                bad.append((i, i+1) if endpoint == -1 else (i-1, i))
        if not bad:
            return grid, branch
        if level == refinements:
            break
        midpoints = np.asarray([0.5*(grid[i] + grid[j]) for i, j in bad], dtype=float)
        grid = np.unique(np.concatenate([grid, midpoints]))

    if allow_unresolved_cluster:
        return grid, branch
    raise np.linalg.LinAlgError(
        "adaptive eigenpair tracking reached a persistent quasi-degenerate cluster"
    )


def pair_phase_speed_squared(eigenvalue_pair, *, a: float, k: float) -> float:
    vals = np.asarray(eigenvalue_pair, dtype=complex)
    aa = float(a); kk = float(k)
    if vals.shape != (2,) or not np.all(np.isfinite(vals)):
        raise ValueError("eigenvalue_pair must contain two finite values")
    if not (math.isfinite(aa) and aa > 0.0 and math.isfinite(kk) and kk > 0.0):
        raise ValueError("a and k must be finite and positive")
    value = vals[0] * vals[1] * (aa / kk)**2
    if abs(value.imag) > 1e-7 * max(1.0, abs(value.real)):
        raise ValueError("tracked pair product is not approximately real")
    return float(value.real)
