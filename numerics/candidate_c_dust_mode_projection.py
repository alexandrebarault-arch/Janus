"""Local mode content and matching freedom of exact-dust initial data."""
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
class GRMatchingFamily:
    N: float
    base_state: np.ndarray
    free_basis: np.ndarray
    raw_condition_number: float
    scaled_condition_number: float


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


@dataclass(frozen=True)
class MatchingSensitivity:
    N: float
    a: float
    base_final_outputs: np.ndarray
    final_output_jacobian: np.ndarray
    fundamental_matrix: np.ndarray
    family: GRMatchingFamily


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


def _matching_matrix(trajectory, N: float) -> np.ndarray:
    x = float(N)
    generator = np.asarray(trajectory.generator_N(x), dtype=float)
    common = np.asarray(trajectory.common_map(x), dtype=float)
    relative = np.asarray(trajectory.relative_map(x), dtype=float)
    common_N = np.asarray(trajectory.common_map_N(x), dtype=float) + common @ generator
    relative_N = np.asarray(trajectory.relative_map_N(x), dtype=float) + relative @ generator
    y3 = np.array([0.0, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=float)
    y3dot = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0], dtype=float)
    return np.vstack([common, relative, relative_N, common_N, y3, y3dot])


def _validate_N(trajectory, N: float) -> float:
    x = float(N)
    if not math.isfinite(x):
        raise ValueError("N must be finite")
    lo = float(trajectory.N_grid[0])
    hi = float(trajectory.N_grid[-1])
    if x < lo or x > hi:
        raise ValueError("N lies outside the trajectory domain")
    return x


def gr_matched_state_at(trajectory, N: float) -> GRMatchedLift:
    """Return the historical Y3=Y3dot=0 member of the matching family."""
    x = _validate_N(trajectory, N)
    constraints = _matching_matrix(trajectory, x)
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


def gr_matching_family_at(trajectory, N: float) -> GRMatchingFamily:
    """Return the two-parameter family left by the four physical constraints.

    The free coordinates are chosen to be initial ``(Y3,Y3dot)``.  The base
    member sets both to zero only as a coordinate origin; no physics is
    attached to that choice.  Each column of ``free_basis`` changes one of
    these coordinates by one while leaving common/relative values and their
    N-derivatives unchanged.
    """
    x = _validate_N(trajectory, N)
    constraints = _matching_matrix(trajectory, x)
    raw_condition = float(np.linalg.cond(constraints))
    base_target = np.array([1.0, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=float)
    base, scaled_condition, _ = _balanced_linear_solve(constraints, base_target)
    columns = []
    for free_index in (4, 5):
        target = np.zeros(6, dtype=float)
        target[free_index] = 1.0
        direction, _, residual = _balanced_linear_solve(constraints, target)
        if residual > 1.0e-7:
            raise np.linalg.LinAlgError(
                f"matching free-direction residual too large: {residual:.6g}"
            )
        columns.append(direction)
    return GRMatchingFamily(
        N=x,
        base_state=np.asarray(base, dtype=float),
        free_basis=np.column_stack(columns),
        raw_condition_number=raw_condition,
        scaled_condition_number=scaled_condition,
    )


def fastest_mode_projection(trajectory, N: float) -> FastModeProjection:
    """Project the historical base lift onto the largest local growth mode."""
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
    ratio = complex(np.inf) if abs(common_mode) <= 1.0e-14*scale else complex(relative_mode/common_mode)
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


def propagate_matching_sensitivity(
    trajectory,
    N: float,
    *,
    rtol: float = 1.0e-9,
    atol: float = 1.0e-12,
) -> MatchingSensitivity:
    """Map the two unfixed helicity matching data to today's densities."""
    from scipy.integrate import solve_ivp

    family = gr_matching_family_at(trajectory, N)
    x = family.N
    initial = np.eye(6, dtype=float).reshape(-1)

    def rhs(n, flat):
        F = np.asarray(flat, dtype=float).reshape(6, 6)
        return (np.asarray(trajectory.generator_N(float(n)), dtype=float) @ F).reshape(-1)

    sol = solve_ivp(
        rhs,
        (x, 0.0),
        initial,
        t_eval=[0.0],
        method="DOP853",
        rtol=float(rtol),
        atol=float(atol),
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    F = np.asarray(sol.y[:, -1], dtype=float).reshape(6, 6)
    common_today = np.asarray(trajectory.common_map(0.0), dtype=float)
    relative_today = np.asarray(trajectory.relative_map(0.0), dtype=float)
    outputs = np.vstack([common_today, relative_today])
    base_final = outputs @ F @ family.base_state
    jacobian = outputs @ F @ family.free_basis
    return MatchingSensitivity(
        N=x,
        a=float(math.exp(x)),
        base_final_outputs=np.asarray(base_final, dtype=float),
        final_output_jacobian=np.asarray(jacobian, dtype=float),
        fundamental_matrix=F,
        family=family,
    )
