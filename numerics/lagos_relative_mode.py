"""Relative/common decomposition of the reduced Lagos metric action."""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import (
    reduced_pure_metric_lagrangian,
    reduced_velocity_hessian,
)


@dataclass(frozen=True)
class RelativeCommonKineticProjection:
    psi_common: float
    psi_relative: float
    e_common: float
    e_relative: float
    rank: int


@dataclass(frozen=True)
class RelativeESliceCoefficients:
    """Quadratic coefficients on the structural E- slice.

    L(E-,dot E-) = 1/2*K*dotE^2 + C*E*dotE + 1/2*P*E^2.
    These coefficients are a proportional-background structural control only;
    they are not Candidate-C observables before matter/background terms are
    included.
    """

    kinetic: float
    mixed: float
    static: float


def _relative_e_vector() -> np.ndarray:
    s = 1.0 / math.sqrt(2.0)
    return np.array([0.0, 0.0, s, -s], dtype=float)


def relative_common_kinetic_projection(
    bg: ScalarBackground,
) -> RelativeCommonKineticProjection:
    """Project the post-auxiliary kinetic Hessian onto common/relative modes."""
    K = np.asarray(reduced_velocity_hessian(bg), dtype=float)
    invsqrt2 = 1.0 / math.sqrt(2.0)
    basis = (
        np.array([invsqrt2, invsqrt2, 0.0, 0.0]),
        np.array([invsqrt2, -invsqrt2, 0.0, 0.0]),
        np.array([0.0, 0.0, invsqrt2, invsqrt2]),
        _relative_e_vector(),
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


def relative_e_slice_coefficients(bg: ScalarBackground) -> RelativeESliceCoefficients:
    """Return quadratic coefficients on E- after lapse/shift elimination."""
    r = _relative_e_vector()
    z = np.zeros(4, dtype=float)

    base = reduced_pure_metric_lagrangian(bg, z, z)
    lpv = reduced_pure_metric_lagrangian(bg, z, r)
    lmv = reduced_pure_metric_lagrangian(bg, z, -r)
    kinetic = lpv + lmv - 2.0*base

    lpq = reduced_pure_metric_lagrangian(bg, r, z)
    lmq = reduced_pure_metric_lagrangian(bg, -r, z)
    static = lpq + lmq - 2.0*base

    lpp = reduced_pure_metric_lagrangian(bg, r, r)
    lpm = reduced_pure_metric_lagrangian(bg, r, -r)
    lmp = reduced_pure_metric_lagrangian(bg, -r, r)
    lmm = reduced_pure_metric_lagrangian(bg, -r, -r)
    mixed = 0.25*(lpp-lpm-lmp+lmm)

    return RelativeESliceCoefficients(
        kinetic=float(kinetic),
        mixed=float(mixed),
        static=float(static),
    )
