"""Canonical evolution helpers for a time-dependent quadratic Hamiltonian."""
from __future__ import annotations

import math
import numpy as np


def canonical_phase_matrix(*, hamiltonian_hessian, H_g: float) -> np.ndarray:
    """Return cosmic-time generator for normalized phase state (Y,Pi).

    The reduced action has common measure a^3 and normalized Hamiltonian
    h=1/2 z^T H z. With Pi=P/a^3, Hamilton's equations are

        Ydot = d h / d Pi,
        Pidot = -d h / d Y - 3 H_g Pi.
    """
    H = np.asarray(hamiltonian_hessian, dtype=float)
    if H.shape != (6, 6) or not np.all(np.isfinite(H)):
        raise ValueError("hamiltonian_hessian must be finite 6x6")
    Hg = float(H_g)
    if not math.isfinite(Hg):
        raise ValueError("H_g must be finite")
    H = 0.5 * (H + H.T)
    Hyy = H[:3, :3]
    HyP = H[:3, 3:]
    HPy = H[3:, :3]
    HPP = H[3:, 3:]
    return np.block([
        [HPy, HPP],
        [-Hyy, -HyP - 3.0 * Hg * np.eye(3, dtype=float)],
    ])


def canonical_phase_matrix_N(*, hamiltonian_hessian, H_g: float) -> np.ndarray:
    """Return d/dN generator, N=ln(a), from the cosmic-time generator."""
    Hg = float(H_g)
    if not math.isfinite(Hg) or Hg <= 0.0:
        raise ValueError("H_g must be finite and positive for N evolution")
    return canonical_phase_matrix(
        hamiltonian_hessian=hamiltonian_hessian, H_g=Hg,
    ) / Hg


def canonical_rhs_N(N: float, state, *, coefficients_provider) -> np.ndarray:
    """Evaluate d(Y,Pi)/dN using ``provider(N)->(Hham,H_g)``."""
    z = np.asarray(state, dtype=float)
    if z.shape != (6,) or not np.all(np.isfinite(z)):
        raise ValueError("canonical state must be a finite length-6 vector")
    H, Hg = coefficients_provider(float(N))
    return canonical_phase_matrix_N(hamiltonian_hessian=H, H_g=Hg) @ z


def fundamental_rhs_N(N: float, flat_matrix, *, coefficients_provider) -> np.ndarray:
    """Evaluate dF/dN=A(N)F for a flattened 6x6 fundamental matrix."""
    flat = np.asarray(flat_matrix, dtype=float)
    if flat.shape != (36,) or not np.all(np.isfinite(flat)):
        raise ValueError("fundamental matrix must be a finite flattened 6x6 array")
    H, Hg = coefficients_provider(float(N))
    A = canonical_phase_matrix_N(hamiltonian_hessian=H, H_g=Hg)
    F = flat.reshape(6, 6)
    return (A @ F).reshape(-1)
