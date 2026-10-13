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


def _scaled_pair_basis(vectors: np.ndarray, pair: tuple[int, int], state_scale) -> np.ndarray:
    V = np.asarray(vectors[:, list(pair)], dtype=complex)
    if state_scale is not None:
        s = np.asarray(state_scale, dtype=float)
        if s.shape != (V.shape[0],) or not np.all(np.isfinite(s)) or np.any(s <= 0.0):
            raise ValueError("state_scale must be a finite positive vector matching state size")
        V = s[:, None] * V
    Q, R = np.linalg.qr(V)
    if np.min(np.abs(np.diag(R))) <= 1e-12 * max(1.0, float(np.linalg.norm(R, ord=np.inf))):
        raise np.linalg.LinAlgError("candidate eigenpair subspace is numerically rank deficient")
    return Q[:, :2]


def _subspace_overlap(Qa: np.ndarray, Qb: np.ndarray) -> float:
    value = float(np.linalg.norm(Qa.conj().T @ Qb, ord="fro")**2 / 2.0)
    return min(1.0, max(0.0, value))


def _anchor_pair(values: np.ndarray) -> tuple[int, int]:
    idx = np.argsort(np.abs(values))[-2:]
    return int(idx[0]), int(idx[1])


def track_eigenpair_branch(
    generators,
    *,
    anchor_index: int = -1,
    anchor_pair: tuple[int, int] | None = None,
    state_scale=None,
) -> TrackedEigenpairBranch:
    """Track one two-dimensional eigensubspace by maximum adjacent overlap.

    The anchor defaults to the pair with largest ``|lambda|``. Subsequent
    points are selected from all eigenvector pairs by principal-subspace
    overlap, so branch identity is not redefined by instantaneous frequency.
    """
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

    eigvals: list[np.ndarray] = []
    eigvecs: list[np.ndarray] = []
    for matrix in G:
        vals, vecs = np.linalg.eig(matrix)
        eigvals.append(vals)
        eigvecs.append(vecs)

    pair0 = _anchor_pair(eigvals[ai]) if anchor_pair is None else tuple(map(int, anchor_pair))
    if len(pair0) != 2 or pair0[0] == pair0[1] or min(pair0) < 0 or max(pair0) >= n:
        raise ValueError("anchor_pair must contain two distinct valid eigenvalue indices")

    out_vals = np.empty((npts, 2), dtype=complex)
    out_pairs = np.empty((npts, 2), dtype=int)
    scores = np.full(npts, np.nan, dtype=float)
    out_vals[ai] = eigvals[ai][list(pair0)]
    out_pairs[ai] = pair0
    scores[ai] = 1.0
    anchor_basis = _scaled_pair_basis(eigvecs[ai], pair0, state_scale)

    def walk(indices, initial_basis):
        prev_basis = initial_basis
        prev_vals = None
        for i in indices:
            best = None
            best_key = None
            for pair in combinations(range(n), 2):
                try:
                    basis = _scaled_pair_basis(eigvecs[i], pair, state_scale)
                except np.linalg.LinAlgError:
                    continue
                overlap = _subspace_overlap(prev_basis, basis)
                vals = eigvals[i][list(pair)]
                if prev_vals is None:
                    continuity = 0.0
                else:
                    aa = np.sort_complex(vals)
                    bb = np.sort_complex(prev_vals)
                    scale = max(1.0, float(np.max(np.abs(bb))))
                    continuity = float(np.sum(np.abs(aa-bb)) / scale)
                key = (overlap, -continuity)
                if best_key is None or key > best_key:
                    best_key = key
                    best = (pair, basis, vals, overlap)
            if best is None:
                raise np.linalg.LinAlgError(f"no rank-2 eigenpair subspace at point {i}")
            pair, prev_basis, vals, overlap = best
            out_pairs[i] = pair
            out_vals[i] = vals
            scores[i] = overlap
            prev_vals = vals

    walk(range(ai+1, npts), anchor_basis)
    walk(range(ai-1, -1, -1), anchor_basis)
    return TrackedEigenpairBranch(
        eigenvalues=out_vals,
        overlap_scores=scores,
        pair_indices=out_pairs,
    )


def pair_phase_speed_squared(eigenvalue_pair, *, a: float, k: float) -> float:
    vals = np.asarray(eigenvalue_pair, dtype=complex)
    aa = float(a)
    kk = float(k)
    if vals.shape != (2,) or not np.all(np.isfinite(vals)):
        raise ValueError("eigenvalue_pair must contain two finite values")
    if not (math.isfinite(aa) and aa > 0.0 and math.isfinite(kk) and kk > 0.0):
        raise ValueError("a and k must be finite and positive")
    value = vals[0] * vals[1] * (aa / kk)**2
    if abs(value.imag) > 1e-7 * max(1.0, abs(value.real)):
        raise ValueError("tracked pair product is not approximately real")
    return float(value.real)
