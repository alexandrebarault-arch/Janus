import numpy as np

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    gaussian_profile,
    shell_profile,
    solve_initial_data,
)


def test_flat_beta_tuning():
    assert np.allclose(
        flat_beta_from123(1.0, 0.0, 0.0),
        (-3.0, 1.0, 0.0, 0.0, -1.0),
    )


def test_vacuum_returns_biminkowski():
    p = Params(beta=flat_beta_from123(1.0, 0.0, 0.0), interaction=0.1)
    z = lambda r: np.zeros_like(r)
    sol = solve_initial_data(p, z, z, r_max=20.0)
    assert sol.success
    assert np.max(np.abs(sol.psi_g - 1.0)) < 1.0e-7
    assert np.max(np.abs(sol.psi_f - 1.0)) < 1.0e-7


def test_janus_like_center_and_wall_have_regular_positive_initial_data():
    p = Params(beta=flat_beta_from123(1.0, 0.0, 0.0), interaction=0.05)
    dg = lambda r: shell_profile(r, amplitude=0.03, radius=6.0, width=1.5)
    df = lambda r: gaussian_profile(r, amplitude=0.03, width=2.0)
    sol = solve_initial_data(p, dg, df, r_max=25.0)

    assert sol.success
    assert sol.min_psi_g > 0.0
    assert sol.min_psi_f > 0.0
    assert sol.max_constraint_residual < 5.0e-5
    assert df(np.array([0.0]))[0] > dg(np.array([0.0]))[0]
    assert dg(np.array([6.0]))[0] > df(np.array([6.0]))[0]
