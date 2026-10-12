"""Relative/common kinetic decomposition of the reduced Lagos metric action."""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import reduced_velocity_hessian


@dataclass(frozen=True)
class RelativeCommonKineticProjection:
    psi_common: float
    psi_relative: float
    e_common: float
    e_relative: float
    rank: int


def relative_common_kinetic_projection(
    bg: ScalarBackground,
) -> RelativeCommonKineticProjection:
    """Project the post-auxiliary kinetic Hessian onto common/relative modes.

    The basis is orthonormal in `(Psi1,Psi2,E1,E2)`.  This function is a
    structural diagnostic for proportional-background controls; it does not by
    itself define Candidate-C physical variables in the presence of matter.
    """
    K = np.asarray(reduced_velocity_hessian(bg), dtype=float)
    invsqrt2 = 1.0 / math.sqrt(2.0)
    basis = (
        np.array([invsqrt2, invsqrt2, 0.0, 0.0]),
        np.array([invsqrt2, -invsqrt2, 0.0, 0.0]),
        np.array([0.0, 0.0, invsqrt2, invsqrt2]),
        np.array([0.0, 0.0, invsqrt2, -invsqrt2]),
    )
    coeffs = [float(v @ K @ v) for v in basis]
    scale = max(1.0, float(np.linalg.norm(K, ord=2)))
    rank = int(np.linalg.matrix_rank(K, tol=1e-10*scale))
    return RelativeCommonKineticProjection(
        psi_common=coeffs[0],
        psi_relative=coeffs[1],
        e_common=coeffs[2],
        e_relative=coeffs[3],
        rank=rank,
    )
