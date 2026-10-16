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


def direct_flat_reduced_transform(*, k: float, nHf: float, nHf_dot: float):
    """Map Stückelberg phase variables directly to reduced flat-gauge dust variables.

    Old reduced order is
    ``(psi_f,E_f,q_g,q_f,psi_f_dot,E_f_dot,q_g_dot,q_f_dot,p_g,p_f)``.
    New order is six states ``(Y1,Y2,L,T,p_g,p_f)`` followed by their six
    rates.  The ``p_g_dot,p_f_dot`` columns are structural zeros.

    The exact identities are

    ``psi_f = k^2 L/3 - nHf T``, ``E_f=-2L``,
    ``q_g=Y1`` and ``q_f=Y2-T``.
    """
    vals = (k, nHf, nHf_dot)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("bridge inputs must be finite")
    if k < 0.0 or nHf <= 0.0:
        raise ValueError("require k>=0 and nHf>0")
    k2 = float(k) * float(k)
    B = float(nHf)
    Bd = float(nHf_dot)
    M = np.zeros((10, 12), dtype=float)

    M[0, 2] = k2 / 3.0
    M[0, 3] = -B
    M[1, 2] = -2.0
    M[2, 0] = 1.0
    M[3, 1] = 1.0
    M[3, 3] = -1.0

    M[4, 3] = -Bd
    M[4, 8] = k2 / 3.0
    M[4, 9] = -B
    M[5, 8] = -2.0
    M[6, 6] = 1.0
    M[7, 7] = 1.0
    M[7, 9] = -1.0

    M[8, 4] = 1.0
    M[9, 5] = 1.0
    return M


def direct_flat_augmented_transform(*, k: float, nHf: float, nHf_dot: float):
    """Map Stückelberg states/rates plus four common metric auxiliaries to the old 14-vector."""
    reduced = direct_flat_reduced_transform(k=k, nHf=nHf, nHf_dot=nHf_dot)
    P = np.zeros((14, 16), dtype=float)
    P[:8, :12] = reduced[:8, :]
    P[8:12, 12:16] = np.eye(4, dtype=float)
    P[12:14, :12] = reduced[8:10, :]
    return P


def direct_native_augmented_transform(
    *,
    k: float,
    nHf: float,
    nHf_dot: float,
    n_dot_over_n: float,
    n_over_alpha: float,
    alpha_over_n: float,
):
    """Map native Stückelberg variables/auxiliaries to old common flat variables.

    The new state/rate order is the same six phase variables as above, but the
    final four auxiliary columns are interpreted as **native**
    ``(Phi_g,Phi_f,B_g,B_f)``.  For the f sector the common De Felice
    auxiliaries are produced by the linear pullback with coordinate shifts
    ``xi^0=-T`` and ``xi=-L``:

    ``Phi_f_common = Phi_f_native - Tdot - (ndot/n) T``;

    ``B_f_common = B_f_native + (n/alpha) T - (alpha/n) Ldot``.

    In this representation the native matter perturbation is ``q_f_native=Y2``;
    its common-chart De Felice value remains ``q_f_common=Y2-T``.  This is the
    natural variable set for a finite-mu nonlinear HR pullback because the EH
    and matter sectors stay in their own native FLRW charts.
    """
    vals = (k, nHf, nHf_dot, n_dot_over_n, n_over_alpha, alpha_over_n)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("native bridge inputs must be finite")
    if k < 0.0 or nHf <= 0.0 or n_over_alpha <= 0.0 or alpha_over_n <= 0.0:
        raise ValueError("invalid native bridge scales")

    P = direct_flat_augmented_transform(k=k, nHf=nHf, nHf_dot=nHf_dot)
    # Replace the common f lapse/shift identity rows by their native pullback.
    P[9, :] = 0.0
    P[9, 13] = 1.0
    P[9, 3] = -float(n_dot_over_n)
    P[9, 9] = -1.0

    P[11, :] = 0.0
    P[11, 15] = 1.0
    P[11, 3] = float(n_over_alpha)
    P[11, 8] = -float(alpha_over_n)
    return P
