"""Time-dependent pre-BD change of variables to relative Stueckelberg coordinates."""
from __future__ import annotations

import math
import numpy as np


def _square_finite(x, name):
    a = np.asarray(x, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be a finite square matrix")
    return a


def transform_state_rate_hessian(H, R, Rdot):
    """Transform a quadratic Hessian under ``q_old = R q_new``.

    State/rate ordering is ``(q, qdot)`` on both sides and
    ``qdot_old = Rdot q_new + R qdot_new``.
    """
    H = _square_finite(H, "H")
    R = _square_finite(R, "R")
    Rdot = _square_finite(Rdot, "Rdot")
    n = R.shape[0]
    if Rdot.shape != R.shape or H.shape != (2*n, 2*n):
        raise ValueError("incompatible H, R and Rdot shapes")
    T = np.block([[R, np.zeros_like(R)], [Rdot, R]])
    out = T.T @ H @ T
    return 0.5 * (out + out.T)


def prebd_bridge_matrices(*, k: float, nHf: float, nHf_dot: float):
    """Return ``(R,Rdot)`` from ``(Y1,Y2,L,T,p_g,p_f)`` to pre-BD variables.

    Old state order is ``(Y1,Y2,Y3,Z,p_g,p_f)`` with

    ``Y3 = -2 L`` and ``Z = -nHf*T + k^2 L/3``.

    ``nHf`` is the inverse of De Felice's ``1/(n H_f)`` coefficient and dots
    are derivatives with respect to the same g-cosmic time used by the
    quadratic action.
    """
    vals = (k, nHf, nHf_dot)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("bridge inputs must be finite")
    if k < 0.0 or nHf <= 0.0:
        raise ValueError("require k>=0 and nHf>0")
    k2 = float(k) * float(k)
    B = float(nHf)
    Bd = float(nHf_dot)
    R = np.eye(6, dtype=float)
    R[2, :] = 0.0
    R[2, 2] = -2.0
    R[3, :] = 0.0
    R[3, 2] = k2 / 3.0
    R[3, 3] = -B
    Rdot = np.zeros((6, 6), dtype=float)
    Rdot[3, 3] = -Bd
    return R, Rdot
