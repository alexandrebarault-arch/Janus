import numpy as np

from numerics.sector_dual_control_input import (
    reference_g_only_control_rows,
    reference_f_only_dual_control_rows,
)


def test_reference_g_only_and_f_only_dual_rows_exchange_metric_sectors():
    g = reference_g_only_control_rows(n=160, delta_r=0.08, solve_points=500, tol=5e-7)
    f = reference_f_only_dual_control_rows(n=160, delta_r=0.08, solve_points=500, tol=5e-7)
    assert g["solution"].success
    assert f["solution"].success

    rg = g["rows"]
    rf = f["rows"]
    np.testing.assert_allclose(rg[:, 0], rf[:, 0], rtol=0, atol=0)
    # gA/gB <-> fA/fB under exact sector duality.
    np.testing.assert_allclose(rg[:, 1], rf[:, 8], rtol=2e-6, atol=2e-8)
    np.testing.assert_allclose(rg[:, 2], rf[:, 9], rtol=2e-6, atol=2e-8)
    np.testing.assert_allclose(rg[:, 8], rf[:, 1], rtol=2e-6, atol=2e-8)
    np.testing.assert_allclose(rg[:, 9], rf[:, 2], rtol=2e-6, atol=2e-8)

    # Conserved matter moves to the other sector with no leakage.
    np.testing.assert_allclose(rg[:, 20], rf[:, 23], rtol=2e-6, atol=2e-10)
    np.testing.assert_allclose(rg[:, 23], 0.0, rtol=0, atol=0)
    np.testing.assert_allclose(rf[:, 20], 0.0, rtol=0, atol=0)


def test_sector_dual_runtime_coefficients_are_reversed():
    g = reference_g_only_control_rows(n=80, delta_r=0.1, solve_points=300, tol=1e-6)
    f = reference_f_only_dual_control_rows(n=80, delta_r=0.1, solve_points=300, tol=1e-6)
    assert tuple(reversed(g["runtime_b"])) == f["runtime_b"]
