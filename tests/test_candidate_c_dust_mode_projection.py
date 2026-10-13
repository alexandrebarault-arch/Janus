import math
import numpy as np


def test_balanced_gr_matching_satisfies_physical_constraints_at_arbitrary_surface():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_mode_projection import gr_matched_state_at

    trajectory = build_candidate_c_dust_trajectory(0.1, grid_size=61)
    N = math.log(0.12)
    lift = gr_matched_state_at(trajectory, N)
    A = trajectory.generator_N(N)
    common = trajectory.common_map(N)
    relative = trajectory.relative_map(N)
    common_N = trajectory.common_map_N(N) + common @ A
    relative_N = trajectory.relative_map_N(N) + relative @ A
    assert math.isclose(float(common @ lift.state), 1.0, rel_tol=0.0, abs_tol=2e-8)
    assert abs(float(relative @ lift.state)) < 2e-8
    assert math.isclose(float(common_N @ lift.state), 1.0, rel_tol=0.0, abs_tol=3e-5)
    assert abs(float(relative_N @ lift.state)) < 3e-5
    assert abs(float(lift.state[2])) < 3e-12
    assert abs(float(lift.state[5])) < 3e-12
    assert lift.scaled_condition_number < lift.raw_condition_number
    assert lift.constraint_residual < 1e-7


def test_candidate_healthy_surface_still_excites_fast_relative_rich_mode():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_mode_projection import fastest_mode_projection

    trajectory = build_candidate_c_dust_trajectory(0.1, grid_size=61)
    result = fastest_mode_projection(trajectory, math.log(0.12))
    assert result.eigenvalue.real > 5.0
    assert abs(result.eigenvalue.imag) < 1e-8
    assert abs(result.mode_relative_to_common) > 1.0
    # The GR-matched state is an instantaneous cancellation of local modes;
    # the fast relative-rich direction is not projected away.
    assert abs(result.initial_common_contribution) > 0.1
    assert abs(result.initial_relative_contribution) > 0.1
    assert np.isfinite(result.lift.raw_condition_number)
