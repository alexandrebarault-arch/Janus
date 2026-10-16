import math
import numpy as np


def test_candidate_stueckelberg_prebd_temporal_rate_is_kinetic_null():
    from numerics.candidate_c_linear_stueckelberg_action import (
        candidate_c_stueckelberg_physical_action,
    )
    out = candidate_c_stueckelberg_physical_action(
        0.5, k_hmpc=0.1, derivative_step_N=2e-3,
    )
    assert out.tdot_kinetic_residual < 1e-10
    assert out.pdot_residual < 1e-8
    assert math.isfinite(out.t_algebraic_coefficient)
    assert abs(out.t_algebraic_coefficient) > 0.0


def test_candidate_stueckelberg_local_speeds_match_de_felice_basis():
    from numerics.candidate_c_linear_stueckelberg_action import (
        candidate_c_stueckelberg_local_squared_speeds,
    )
    from numerics.de_felice_dust_local_modes import candidate_c_dust_local_squared_speeds

    kwargs = dict(
        a=0.5,
        k_hmpc=0.2,
        action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )
    st = candidate_c_stueckelberg_local_squared_speeds(**kwargs)
    df = candidate_c_dust_local_squared_speeds(**kwargs)
    assert st.shape == df.shape == (3,)
    # A time-dependent point transformation may change Hessian boundary terms,
    # but not the full Euler-Lagrange spectrum.
    assert np.allclose(st, df, rtol=3e-5, atol=5e-7)


def test_candidate_stueckelberg_gravity_branch_passes_independent_principal_oracle():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_linear_stueckelberg_action import (
        candidate_c_stueckelberg_local_squared_speeds,
    )
    from numerics.de_felice_action_principal import gravity_principal_action

    a = 0.5
    kh = 0.2
    point = candidate_c_dust_background_point(a, k_hmpc=kh)
    target = gravity_principal_action(
        point.metric, rho_f_plus_p_f=point.rho_f_m,
    ).cs2
    speeds = candidate_c_stueckelberg_local_squared_speeds(
        a, k_hmpc=kh,
        action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )
    assert max(abs(speeds[0]), abs(speeds[1])) < 4e-4
    assert math.isclose(speeds[2], target, rel_tol=2e-3, abs_tol=2e-5)
