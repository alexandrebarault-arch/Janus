"""Time-dependent integration by parts for an algebraic scalar rate."""
from __future__ import annotations

import math
import numpy as np


def canonicalize_linear_rate_time_dependent(
    H: np.ndarray,
    *,
    dot_c,
    mu_measure: float,
    z_index: int,
) -> np.ndarray:
    """Integrate terms linear in one algebraic coordinate rate by parts.

    ``H`` is a symmetric state/rate Hessian of shape ``(2n,2n)`` in the
    order ``(x_0..x_{n-1}, xdot_0..xdot_{n-1})``. ``z_index`` identifies
    the algebraic coordinate whose rate is to be removed. The caller supplies
    the time derivative of ``C[:,z]`` and ``d ln(measure)/dt``.
    """
    H = np.asarray(H, dtype=float)
    if H.ndim != 2 or H.shape[0] != H.shape[1] or H.shape[0] % 2 != 0:
        raise ValueError("state/rate Hessian must be square with even dimension")
    if not np.all(np.isfinite(H)):
        raise ValueError("state/rate Hessian must be finite")
    n = H.shape[0] // 2
    z = int(z_index)
    if z < 0 or z >= n:
        raise ValueError("z_index is outside the state block")
    dc = np.asarray(dot_c, dtype=float)
    if dc.shape != (n,) or not np.all(np.isfinite(dc)):
        raise ValueError(f"dot_c must be a finite length-{n} vector")
    mu = float(mu_measure)
    if not math.isfinite(mu):
        raise ValueError("mu_measure must be finite")

    H = 0.5 * (H + H.T)
    M = H[:n, :n].copy()
    C = H[:n, n:].copy()
    K = H[n:, n:].copy()
    c = C[:, z].copy()
    correction = dc + mu * c

    for i in range(n):
        if i == z:
            continue
        M[i, z] -= correction[i]
        M[z, i] -= correction[i]
        C[z, i] -= c[i]
    M[z, z] -= correction[z]
    C[:, z] = 0.0
    K[z, :] = 0.0
    K[:, z] = 0.0

    out = np.block([[M, C], [C.T, K]])
    return 0.5 * (out + out.T)


def canonicalize_linear_zdot_time_dependent(
    H: np.ndarray,
    *,
    dot_c,
    mu_measure: float,
) -> np.ndarray:
    """Backward-compatible Eq. (72) four-state BD wrapper."""
    H = np.asarray(H, dtype=float)
    if H.shape != (8, 8):
        raise ValueError("BD-basis Hessian must be 8x8")
    dc = np.asarray(dot_c, dtype=float)
    if dc.shape != (4,) or not np.all(np.isfinite(dc)):
        raise ValueError("dot_c must be a finite length-4 vector")
    return canonicalize_linear_rate_time_dependent(
        H, dot_c=dc, mu_measure=mu_measure, z_index=3,
    )
