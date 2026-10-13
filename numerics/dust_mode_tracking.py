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
    # Spectral projectors are the right object for non-normal generators.
    # trace(Pa Pb)/rank is invariant under a fixed similarity transform and
    # stays discriminating when right eigenspaces are almost parallel.
    return float(abs(np.trace(Pa @ Pb)) / 2.0)


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
            scores[i] = min(1.0, overlap)
            prev_vals = vp

    walk(range(ai+1, npts), anchor_projector, out_vals[ai])
    walk(range(ai-1, -1, -1), anchor_projector, out_vals[ai])
    return TrackedEigenpairBranch(out_vals, scores, out_pairs)


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
