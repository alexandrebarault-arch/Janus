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
    assert abs(result.initial_common_contribution) > 0.1
    assert abs(result.initial_relative_contribution) > 0.1
    assert np.isfinite(result.lift.raw_condition_number)


def test_four_physical_matching_conditions_leave_two_helicity_directions_free():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_mode_projection import gr_matching_family_at

    trajectory = build_candidate_c_dust_trajectory(0.1, grid_size=61)
    N = math.log(0.12)
    family = gr_matching_family_at(trajectory, N)
    assert family.free_basis.shape == (6, 2)
    assert np.allclose(family.free_basis[[2,5], :], np.eye(2), rtol=0.0, atol=2e-10)

    A = trajectory.generator_N(N)
    common = trajectory.common_map(N)
    relative = trajectory.relative_map(N)
    common_N = trajectory.common_map_N(N) + common @ A
    relative_N = trajectory.relative_map_N(N) + relative @ A
    physical = np.vstack([common, relative, relative_N, common_N])
    assert np.linalg.norm(physical @ family.free_basis, ord=np.inf) < 3e-7


def test_free_helicity_matching_data_materially_change_today_observables():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_mode_projection import propagate_matching_sensitivity

    trajectory = build_candidate_c_dust_trajectory(0.1, grid_size=61)
    out = propagate_matching_sensitivity(trajectory, math.log(0.12), rtol=3e-9, atol=3e-12)
    assert out.final_output_jacobian.shape == (2, 2)
    assert np.all(np.isfinite(out.final_output_jacobian))
    # The old Y3=Y3dot=0 convention is not dynamically innocuous: changing
    # the two free helicity matching data changes both final observables.
    assert np.linalg.norm(out.final_output_jacobian[0], ord=np.inf) > 1e2
    assert np.linalg.norm(out.final_output_jacobian[1], ord=np.inf) > 1e3
