import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import (
    eliminate_auxiliaries,
    reduced_velocity_hessian,
)


def _proportional_background():
    return ScalarBackground(
        a=1.0, m2=1.7, f1=1.0, f2=1.0,
        H=0.8, H_omega=0.8, c=1.0, xi=1.0,
        kappa=1.0, k2=9.0, G8pi=1.0,
    )


def test_auxiliary_solution_is_stationary():
    bg = _proportional_background()
    q = np.array([0.13, -0.08, 0.021, -0.017])
    v = np.array([0.041, -0.037, 0.016, -0.012])
    sol = eliminate_auxiliaries(bg, q, v)

    assert sol.auxiliaries.shape == (4,)
    assert sol.auxiliary_hessian_rank == 4
    assert sol.stationarity_residual < 2e-10


def test_reduced_metric_velocity_hessian_has_one_kinetic_direction():
    bg = _proportional_background()
    K = reduced_velocity_hessian(bg)
    eig = np.linalg.eigvalsh(K)

    assert K.shape == (4, 4)
    assert np.allclose(K, K.T, rtol=1e-12, atol=1e-12)
    assert np.linalg.matrix_rank(K, tol=1e-9) == 1
    assert np.count_nonzero(np.abs(eig) > 1e-9) == 1
