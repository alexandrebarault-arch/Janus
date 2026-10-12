import numpy as np

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    shell_profile,
    solve_initial_data,
)


def test_g_only_and_dual_f_only_constraint_solutions_exchange_metrics():
    beta = flat_beta_from123(1.0, -0.2, 0.0)
    dual_beta = tuple(reversed(beta))
    p_g = Params(beta=beta, interaction=0.02, kappa_g=1.0, kappa_f=1.0)
    p_f = Params(beta=dual_beta, interaction=0.02, kappa_g=1.0, kappa_f=1.0)

    source = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    zero = lambda r: np.zeros_like(np.asarray(r, dtype=float))

    g_only = solve_initial_data(
        p_g, source, zero,
        r_max=25.0, points=500, tol=1.0e-7,
    )
    f_only = solve_initial_data(
        p_f, zero, source,
        r_max=25.0, points=500, tol=1.0e-7,
    )
    assert g_only.success
    assert f_only.success

    # Adaptive solve_bvp meshes can differ, so compare after interpolation.
    f_psi_g_on_g = np.interp(g_only.r, f_only.r, f_only.psi_g)
    f_psi_f_on_g = np.interp(g_only.r, f_only.r, f_only.psi_f)
    np.testing.assert_allclose(g_only.psi_g, f_psi_f_on_g, rtol=2e-7, atol=2e-9)
    np.testing.assert_allclose(g_only.psi_f, f_psi_g_on_g, rtol=2e-7, atol=2e-9)
