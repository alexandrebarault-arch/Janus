"""Basis-sensitive scalar kinetic invariants used to audit Gate 2B.

The physical kinetic matrix is ordered as De Felice Eq. (72),
``(Y1, Y2, Y3)``.  Eq. (77) defines the third no-ghost invariant as

    NG3 = det(K) / (K11 K22 - K12^2).

This tiny helper is intentionally separate from the action reconstruction so
that the invariant itself cannot hide or repair an error in the reduction.
"""

from __future__ import annotations

import math
import numpy as np


def kinetic_ng3(kinetic_hessian: np.ndarray) -> float:
    """Return De Felice Eq. (77) ``NG3`` for a 3x3 physical kinetic matrix."""
    K = np.asarray(kinetic_hessian, dtype=float)
    if K.shape != (3, 3):
        raise ValueError("kinetic_hessian must be 3x3")
    if not np.all(np.isfinite(K)):
        raise ValueError("kinetic_hessian must be finite")
    K = 0.5 * (K + K.T)
    minor = float(K[0, 0] * K[1, 1] - K[0, 1] * K[0, 1])
    scale = max(1.0, float(np.linalg.norm(K, ord=np.inf)) ** 2)
    if abs(minor) <= 1e-15 * scale:
        raise np.linalg.LinAlgError("leading 2x2 kinetic minor is singular")
    value = float(np.linalg.det(K) / minor)
    if not math.isfinite(value):
        raise FloatingPointError("NG3 is not finite")
    return value
