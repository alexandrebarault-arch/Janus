"""Time-dependent canonicalization of the algebraic BD scalar.

This helper contains only the integration-by-parts identity.  It deliberately
knows nothing about Case C, matter equations of state, or how coefficient time
derivatives are obtained.  Callers must provide ``dot_c`` and the logarithmic
derivative of the common action measure explicitly.
"""

from __future__ import annotations

import math
import numpy as np


def canonicalize_linear_zdot_time_dependent(
    H: np.ndarray,
    *,
    dot_c,
    mu_measure: float,
) -> np.ndarray:
    """Integrate all terms linear in ``Zdot`` by parts.

    ``H`` is the symmetric Hessian in the order
    ``(Y1,Y2,Y3,Z,Y1dot,Y2dot,Y3dot,Zdot)`` and is partitioned as
    ``[[M,C],[C.T,K]]``.  With ``c_i=C[i,Z]`` and common measure ``mu(t)``,
    the integration by parts uses

        d ln(mu)/dt = mu_measure.

    The caller supplies ``dot_c`` because its computation is background-model
    dependent.  The returned Hessian has no ``Zdot`` column or kinetic row.
    """
    H = np.asarray(H, dtype=float)
    if H.shape != (8, 8):
        raise ValueError("BD-basis Hessian must be 8x8")
    if not np.all(np.isfinite(H)):
        raise ValueError("BD-basis Hessian must be finite")

    dc = np.asarray(dot_c, dtype=float)
    if dc.shape != (4,) or not np.all(np.isfinite(dc)):
        raise ValueError("dot_c must be a finite length-4 vector")

    measure = float(mu_measure)
    if not math.isfinite(measure):
        raise ValueError("mu_measure must be finite")

    H = 0.5 * (H + H.T)
    M = H[:4, :4].copy()
    C = H[:4, 4:8].copy()
    K = H[4:8, 4:8].copy()

    z = 3
    c = C[:, z].copy()
    correction = dc + measure * c

    for i in range(3):
        # State correction from -(dot(c_i)+mu_measure*c_i) Y_i Z.
        M[i, z] -= correction[i]
        M[z, i] -= correction[i]
        # Antisymmetric rate coupling from -c_i Ydot_i Z.
        C[z, i] -= c[i]

    # c_Z Z Zdot = (c_Z/2) d(Z^2)/dt.
    M[z, z] -= correction[z]

    C[:, z] = 0.0
    K[z, :] = 0.0
    K[:, z] = 0.0

    out = np.block([[M, C], [C.T, K]])
    return 0.5 * (out + out.T)
