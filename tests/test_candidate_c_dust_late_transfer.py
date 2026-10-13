import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_gr_connected_initial_mode_satisfies_adiabatic_growing_constraints():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory,
        select_gr_connected_adiabatic_mode,
    )
    traj = build_candidate_c_dust_trajectory(0.1, grid_size=161)
    mode = select_gr_connected_adiabatic_mode(trajectory=traj)
    N0 = traj.N_grid[0]
    A = traj.generator_N(N0)
    common = traj.common_map(N0)
    relative = traj.relative_map(N0)
    common_N = traj.common_map_N(N0) + common @ A
    relative_N = traj.relative_map_N(N0) + relative @ A
    assert math.isclose(float(common @ mode), 1.0, rel_tol=0, abs_tol=2e-9)
    assert abs(float(relative @ mode)) < 2e-9
    assert math.isclose(float(common_N @ mode), 1.0, rel_tol=0, abs_tol=2e-5)
    assert abs(float(relative_N @ mode)) < 2e-5
    assert abs(float(mode[2])) < 3e-12
    assert abs(float(mode[5])) < 3e-12


def test_initial_adiabatic_mode_is_continuous_under_small_k_change():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory,
        select_gr_connected_adiabatic_mode,
    )
    modes = []
    for kh in (0.0999, 0.1, 0.1001):
        traj = build_candidate_c_dust_trajectory(kh, grid_size=61)
        v = select_gr_connected_adiabatic_mode(trajectory=traj)
        v = v / np.linalg.norm(v)
        modes.append(v)
    assert abs(float(modes[0] @ modes[1])) > 0.995
    assert abs(float(modes[1] @ modes[2])) > 0.995


def test_late_transfer_fundamental_matrix_reproduces_direct_adiabatic_propagation():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory,
        select_gr_connected_adiabatic_mode,
        solve_candidate_c_dust_late,
        fundamental_matrix_candidate_c_dust,
    )
    traj = build_candidate_c_dust_trajectory(0.05, grid_size=81)
    initial = select_gr_connected_adiabatic_mode(trajectory=traj)
    direct = solve_candidate_c_dust_late(
        0.05, trajectory=traj, samples=60, rtol=1e-9, atol=1e-12,
    )
    F = fundamental_matrix_candidate_c_dust(
        0.05, trajectory=traj, samples=60, rtol=1e-9, atol=1e-12,
    )
    propagated = F[-1] @ initial
    scale = max(1.0, np.linalg.norm(direct.phase_state[-1], ord=np.inf))
    assert np.linalg.norm(propagated-direct.phase_state[-1], ord=np.inf) < 3e-7*scale
    assert abs(direct.R[0]) < 3e-8
    assert np.all(np.isfinite(direct.R))
    assert np.all(np.isfinite(direct.delta_g))
    assert np.all(np.isfinite(direct.delta_f))


def test_late_transfer_ode_and_spline_grid_converge_before_scientific_use():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory,
        solve_candidate_c_dust_late,
    )
    tr = build_candidate_c_dust_trajectory(0.1, grid_size=161)
    loose = solve_candidate_c_dust_late(
        0.1, trajectory=tr, samples=60, rtol=1e-7, atol=1e-10,
    )
    tight = solve_candidate_c_dust_late(
        0.1, trajectory=tr, samples=60, rtol=3e-9, atol=3e-12,
    )
    assert math.isclose(loose.R[-1], tight.R[-1], rel_tol=2e-5, abs_tol=2e-5)

    tr321 = build_candidate_c_dust_trajectory(0.2, grid_size=321)
    tr401 = build_candidate_c_dust_trajectory(0.2, grid_size=401)
    r321 = solve_candidate_c_dust_late(
        0.2, trajectory=tr321, samples=60, rtol=1e-8, atol=1e-11,
    )
    r401 = solve_candidate_c_dust_late(
        0.2, trajectory=tr401, samples=60, rtol=1e-8, atol=1e-11,
    )
    assert math.isclose(r321.R[-1], r401.R[-1], rel_tol=1e-3, abs_tol=2e-3)


def test_required_late_scales_remain_finite_and_start_adiabatic():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory,
        solve_candidate_c_dust_late,
    )
    for kh in (0.01, 0.05, 0.1, 0.2):
        grid = 321 if kh == 0.2 else 61
        tr = build_candidate_c_dust_trajectory(kh, grid_size=grid)
        result = solve_candidate_c_dust_late(
            kh, trajectory=tr, samples=20, rtol=1e-6, atol=1e-9,
        )
        assert abs(result.R[0]) < 2e-8
        assert np.all(np.isfinite(result.phase_state))
        assert np.all(np.isfinite(result.R))
        assert np.all(result.kkt_condition > 0.0)
        assert np.all(result.momentum_condition > 0.0)


def test_trajectory_boundary_generator_matches_conditioned_local_stencil():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.de_felice_dust_local_modes import candidate_c_dust_local_system
    tr=build_candidate_c_dust_trajectory(0.1,grid_size=61)
    N0=float(tr.N_grid[0]); a=math.exp(N0)
    direct=candidate_c_dust_local_system(
        a,k_hmpc=0.1,action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    ).generator_N
    measured=tr.generator_N(N0)
    scale=max(1.0,float(np.linalg.norm(direct,ord=np.inf)))
    rel=float(np.linalg.norm(measured-direct,ord=np.inf)/scale)
    assert rel < 7e-4


def test_gr_matched_initial_mode_exists_at_low_k_and_has_no_relative_metric_scalar():
    from numerics.candidate_c_dust_late_transfer import (
        build_candidate_c_dust_trajectory, select_gr_connected_adiabatic_mode,
    )
    tr=build_candidate_c_dust_trajectory(0.01,grid_size=81)
    mode=select_gr_connected_adiabatic_mode(trajectory=tr)
    N0=float(tr.N_grid[0]); A=tr.generator_N(N0)
    common=tr.common_map(N0); relative=tr.relative_map(N0)
    common_N=tr.common_map_N(N0)+common@A
    relative_N=tr.relative_map_N(N0)+relative@A
    assert math.isclose(float(common@mode),1.0,rel_tol=0,abs_tol=3e-8)
    assert abs(float(relative@mode)) < 3e-8
    assert math.isclose(float(common_N@mode),1.0,rel_tol=0,abs_tol=3e-5)
    assert abs(float(relative_N@mode)) < 3e-5
    assert abs(float(mode[2])) < 3e-12
    assert abs(float(mode[5])) < 3e-12


def test_high_k_internal_coefficient_grid_is_independent_of_public_output_grid():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.de_felice_dust_local_modes import candidate_c_dust_local_system
    tr=build_candidate_c_dust_trajectory(0.2,grid_size=61)
    N=float(tr.N_grid[0]*0.75)
    a=math.exp(N)
    direct=candidate_c_dust_local_system(
        a,k_hmpc=0.2,action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    ).generator_N
    measured=tr.generator_N(N)
    scale=max(1.0,float(np.linalg.norm(direct,ord=np.inf)))
    rel=float(np.linalg.norm(measured-direct,ord=np.inf)/scale)
    # Intentional RED: current spline-Hessian production path is not yet
    # conditioned enough at k=0.2 h/Mpc. Keep this failing until the generator
    # derivative is made independent of the public output grid.
    assert rel < 2e-3
