import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.comelli_case_c import case_c_background_from_a
from numerics.lagos_scalar_action import pure_metric_lagrangian_healthy
from numerics.two_matter_scalar_action import (
    KessenceFluid,
    combined_scalar_lagrangian,
    eliminate_combined_auxiliaries,
    reduced_flat_gauge_velocity_hessian,
)


def _proportional_background():
    return ScalarBackground(
        a=1.0, m2=1.7, f1=1.0, f2=1.0,
        H=0.8, H_omega=0.8, c=1.0, xi=1.0,
        kappa=1.0, k2=9.0, G8pi=1.0,
    )


def test_combined_action_reduces_to_pure_metric_when_matter_is_zero():
    bg = _proportional_background()
    dynamic = np.array([0.11, -0.07, 0.021, -0.016, 0.0, 0.0])
    rates = np.array([0.043, -0.032, 0.014, -0.011, 0.0, 0.0])
    aux = np.array([0.025, -0.018, 0.019, -0.013])
    zero = KessenceFluid(rho=0.0, pressure=0.0, cs2=0.4)

    measured = combined_scalar_lagrangian(
        bg, dynamic, rates, aux, g_fluid=zero, f_fluid=zero, M_g2=1.0
    )
    state = np.array([
        dynamic[0], dynamic[1], dynamic[2], dynamic[3],
        aux[0], aux[1], aux[2], aux[3],
    ])
    expected = pure_metric_lagrangian_healthy(bg, state, rates[:4])
    assert np.isclose(measured, expected, rtol=2e-13, atol=2e-13)


def test_combined_auxiliary_solution_is_stationary():
    bg = _proportional_background()
    g = KessenceFluid(rho=2.8, pressure=0.7, cs2=0.42)
    f = KessenceFluid(rho=3.6, pressure=0.4, cs2=0.31)
    dynamic = np.array([0.09, -0.06, 0.018, -0.014, 0.031, -0.027])
    rates = np.array([0.037, -0.029, 0.012, -0.010, -0.024, 0.021])

    sol = eliminate_combined_auxiliaries(
        bg, dynamic, rates, g_fluid=g, f_fluid=f, M_g2=1.0
    )
    assert sol.auxiliaries.shape == (4,)
    assert sol.auxiliary_hessian_rank == 4
    assert sol.stationarity_residual < 2e-9


def test_flat_gauge_case_c_velocity_hessian_has_one_nondynamical_bd_direction():
    point = case_c_background_from_a(0.1, k=12.0)
    bg = point.metric
    g = KessenceFluid(rho=point.rho1, pressure=point.rho1 / 3.0, cs2=1.0 / 3.0)
    # The exact Case-C f-background is dust. Keep a positive P(X) sound-speed
    # regulator until after the constrained action is reduced.
    f = KessenceFluid(rho=point.rho2, pressure=0.0, cs2=0.1)

    K = reduced_flat_gauge_velocity_hessian(
        bg, g_fluid=g, f_fluid=f, M_g2=1.0
    )
    eig = np.linalg.eigvalsh(K)
    assert K.shape == (4, 4)
    assert np.allclose(K, K.T, rtol=2e-11, atol=2e-11)

    scale = max(1.0, float(np.max(np.abs(eig))))
    tol = 2e-8 * scale
    assert np.count_nonzero(np.abs(eig) > tol) == 3
    assert np.min(np.abs(eig)) < tol
