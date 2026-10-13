"""Local mode content of GR-matched exact-dust initial data."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class GRMatchedLift:
    N: float
    state: np.ndarray
    raw_condition_number: float
    scaled_condition_number: float
    constraint_residual: float


@dataclass(frozen=True)
class FastModeProjection:
    N: float
    a: float
    eigenvalue: complex
    mode_relative_to_common: complex
    initial_common_contribution: complex
    initial_relative_contribution: complex
    mode_component: np.ndarray
    lift: GRMatchedLift


def _balanced_linear_solve(A: np.ndarray, b: np.ndarray) -> tuple[np.ndarray, float, float]:
    """Equilibrate one square linear system without changing its solution."""
    matrix = np.asarray(A, dtype=float)
    rhs = np.asarray(b, dtype=float)
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("constraint matrix must be square")
    if rhs.shape != (matrix.shape[0],):
        raise ValueError("constraint target has incompatible shape")
    if not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(rhs)):
        raise ValueError("constraint system must be finite")

    row_norm = np.linalg.norm(matrix, axis=1)
    if np.any(row_norm == 0.0):
        raise np.linalg.LinAlgError("constraint matrix has a zero row")
    row_scaled = matrix / row_norm[:, None]
    rhs_scaled = rhs / row_norm
    col_norm = np.linalg.norm(row_scaled, axis=0)
    if np.any(col_norm == 0.0):
        raise np.linalg.LinAlgError("constraint matrix has a zero column")
    equilibrated = row_scaled / col_norm[None, :]
    rank = int(np.linalg.matrix_rank(equilibrated))
    if rank != matrix.shape[0]:
        raise np.linalg.LinAlgError(
            f"equilibrated GR matching matrix has rank {rank}, expected {matrix.shape[0]}"
        )
    u = np.linalg.solve(equilibrated, rhs_scaled)
    state = u / col_norm
    return np.asarray(state, dtype=float), float(np.linalg.cond(equilibrated)), float(
        np.linalg.norm(matrix @ state - rhs, ord=np.inf)
    )


def gr_matched_state_at(trajectory, N: float) -> GRMatchedLift:
    """Construct the same GR/common lift as the production solver at any N."""
    x = float(N)
    if not math.isfinite(x):
        raise ValueError("N must be finite")
    lo = float(trajectory.N_grid[0])
    hi = float(trajectory.N_grid[-1])
    if x < lo or x > hi:
        raise ValueError("N lies outside the trajectory domain")

    generator = np.asarray(trajectory.generator_N(x), dtype=float)
    common = np.asarray(trajectory.common_map(x), dtype=float)
    relative = np.asarray(trajectory.relative_map(x), dtype=float)
    common_N = np.asarray(trajectory.common_map_N(x), dtype=float) + common @ generator
    relative_N = np.asarray(trajectory.relative_map_N(x), dtype=float) + relative @ generator
    y3 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=float)
    y3dot = np.array([0.0, 0.0, 0.0, 0.0, 1.0], dtype=float)
    constraints = np.vstack([common, relative, relative_N, common_N, y3, y3dot])
    target = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=float)
    raw_condition = float(np.linalg.cond(constraints))
    state, scaled_condition, residual = _balanced_linear_solve(constraints, target)
    return GRMatchedLift(
        N=x,
        state=state,
        raw_condition_number=raw_condition,
        scaled_condition_number=scaled_condition,
        constraint_residual=residual,
    )


def fastest_mode_projection(trajectory, N: float) -> FastModeProjection:
    """Project the GR-matched state onto the largest local growth eigenmode.

    The spectral projector uses the left/right biorthogonal eigensystem, so
    the reported component is invariant under eigenvector normalization.  It
    intentionally measures local modal content; it is not a claim that the
    eigenvector remains an isolated mode through later avoided crossings.
    """
    lift = gr_matched_state_at(trajectory, N)
    x = float(N)
    generator = np.asarray(trajectory.generator_N(x), dtype=float)
    values, vectors = np.linalg.eig(generator)
    try:
        inverse = np.linalg.inv(vectors)
    except np.linalg.LinAlgError as exc:
        raise np.linalg.LinAlgError("local eigenvector matrix is singular") from exc
    index = int(np.argmax(values.real))
    projector = np.outer(vectors[:, index], inverse[index, :])
    component = projector @ lift.state

    common = np.asarray(trajectory.common_map(x), dtype=float)
    relative = np.asarray(trajectory.relative_map(x), dtype=float)
    common_mode = common @ vectors[:, index]
    relative_mode = relative @ vectors[:, index]
    scale = max(1.0, abs(common_mode), abs(relative_mode))
    if abs(common_mode) <= 1.0e-14 * scale:
        ratio = complex(np.inf)
    else:
        ratio = complex(relative_mode / common_mode)
    return FastModeProjection(
        N=x,
        a=float(math.exp(x)),
        eigenvalue=complex(values[index]),
        mode_relative_to_common=ratio,
        initial_common_contribution=complex(common @ component),
        initial_relative_contribution=complex(relative @ component),
        mode_component=np.asarray(component, dtype=complex),
        lift=lift,
    )
