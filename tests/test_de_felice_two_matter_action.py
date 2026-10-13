import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_case_c import case_c_background_from_a
from numerics.de_felice_action_principal import gravity_principal_action
from numerics.de_felice_invariants import kinetic_ng3
from numerics.de_felice_two_matter_action import (
    DFKessenceFluid,
    matter_log_phidot_rates,
    flat_gauge_quadratic_hessian,
    eliminate_flat_gauge_auxiliaries,
    bd_basis_transform,
    bd_state_coefficient_decomposition,
    eliminate_bd_mode,
    physical_squared_phase_speeds,
)


def _case_c(a, k):
    point = case_c_background_from_a(a, k=k)
    g = DFKessenceFluid(rho=point.rho1, pressure=point.rho1/3.0, cs2=1.0/3.0)
    f = DFKessenceFluid(rho=point.rho2, pressure=0.0, cs2=0.1)
    return point, g, f


def test_matter_rate_variables_include_background_phidot_drift():
    point, g, f = _case_c(0.2,20.0)
    rg, rf = matter_log_phidot_rates(point.metric, point.derivatives, g_fluid=g, f_fluid=f)
    bg = point.metric; bgp = point.derivatives
    Hg = bg.H/bg.a
    expected_g = -3.0*Hg*g.cs2
    n_dot_over_n = (bgp.xi_prime/bg.xi + bgp.c_prime/bg.c)/bg.a
    n = bg.xi*bg.c
    Hf = bg.H_omega/(bg.a*bg.xi*bg.c)
    expected_f = n_dot_over_n - 3.0*n*Hf*f.cs2
    assert math.isclose(rg, expected_g, rel_tol=2e-13, abs_tol=2e-13)
    assert math.isclose(rf, expected_f, rel_tol=2e-13, abs_tol=2e-13)


def test_two_matter_flat_gauge_hessian_is_symmetric():
    point, g, f = _case_c(0.1, 12.0)
    Q = flat_gauge_quadratic_hessian(
        point.metric, point.derivatives,
        betas=(0.0,1.0,0.0,0.0,0.0),
        g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
    )
    assert Q.shape == (12,12)
    assert np.all(np.isfinite(Q))
    assert np.allclose(Q,Q.T,rtol=2e-10,atol=2e-10)


def test_two_matter_case_c_has_exactly_three_kinetic_directions_after_auxiliary_elimination():
    for a,k in ((0.1,12.0),(0.2,20.0),(0.4,30.0)):
        point, g, f = _case_c(a,k)
        reduced = eliminate_flat_gauge_auxiliaries(
            point.metric, point.derivatives,
            betas=(0.0,1.0,0.0,0.0,0.0),
            g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
        )
        eig = np.linalg.eigvalsh(reduced.kinetic_hessian)
        scale = max(1.0,float(np.max(np.abs(eig))))
        tol = 2e-7*scale
        assert np.count_nonzero(np.abs(eig)>tol) == 3
        assert np.min(np.abs(eig)) < tol
        assert reduced.auxiliary_rank == 4


def test_eq72_bd_basis_has_no_Zdot_kinetic_direction():
    for a,k in ((0.1,12.0),(0.2,20.0),(0.4,30.0)):
        point, g, f = _case_c(a,k)
        reduced = eliminate_flat_gauge_auxiliaries(
            point.metric, point.derivatives,
            betas=(0.0,1.0,0.0,0.0,0.0),
            g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
        )
        M = bd_basis_transform(point.metric, point.derivatives)
        transformed = M.T @ reduced.reduced_hessian @ M
        K = transformed[4:8,4:8]
        scale = max(1.0,float(np.linalg.norm(K,ord=np.inf)))
        assert np.linalg.norm(K[3,:],ord=np.inf) < 3e-7*scale
        assert np.linalg.norm(K[:,3],ord=np.inf) < 3e-7*scale


def test_bd_state_coefficient_decomposition_reconstructs_transformed_hzz():
    point, g, f = _case_c(0.05, 400.0)
    pieces = bd_state_coefficient_decomposition(
        point.metric, point.derivatives,
        betas=(0.0,1.0,0.0,0.0,0.0),
        g_fluid=g, f_fluid=f, finite_difference_step=2e-6,
    )
    explicit = (
        pieces["Sigma2"] + pieces["2A_Sigma_qf"] + pieces["A2_qf2"]
        + pieces["2Adot_Sigma_qfdot"] + pieces["2AAdot_qf_qfdot"]
        + pieces["Adot2_qfdot2"]
    )
    assert math.isclose(explicit, pieces["raw_hZZ"], rel_tol=2e-10, abs_tol=2e-8)
    assert math.isclose(pieces["raw_hZZ"], pieces["transformed_hZZ"], rel_tol=2e-10, abs_tol=2e-8)
    assert math.isclose(pieces["C_ZZ"], pieces["transformed_C_ZZ"], rel_tol=2e-10, abs_tol=2e-8)


def test_bd_elimination_leaves_positive_three_by_three_case_c_kinetic_matrix():
    for a,k in ((0.1,12.0),(0.2,20.0),(0.4,30.0)):
        point, g, f = _case_c(a,k)
        physical = eliminate_bd_mode(
            point.metric, point.derivatives,
            betas=(0.0,1.0,0.0,0.0,0.0),
            g_fluid=g, f_fluid=f, finite_difference_step=5e-5,
        )
        assert physical.physical_hessian.shape == (6,6)
        assert physical.kinetic_hessian.shape == (3,3)
        assert np.all(np.isfinite(physical.physical_hessian))
        eig = np.linalg.eigvalsh(physical.kinetic_hessian)
        assert np.all(eig > 0.0)
        assert abs(physical.bd_algebraic_coefficient) > 1e-10
        assert physical.zdot_kinetic_residual < 3e-7


def test_physical_speed_extractor_recovers_decoupled_known_branches():
    a=0.5
    k=20.0
    expected=np.array([-2.0/3.0,1.0/3.0,0.4])
    K=np.diag([2.0,3.0,5.0])
    M=-K@np.diag(expected*(k/a)**2)
    H=np.block([[M,np.zeros((3,3))],[np.zeros((3,3)),K]])
    measured=np.sort(physical_squared_phase_speeds(H,a=a,k=k))
    assert np.allclose(measured,np.sort(expected),rtol=1e-12,atol=1e-12)


def test_case_c_finite_k_ng3_matches_de_felice_eq78():
    point, g, f = _case_c(0.05, 400.0)
    physical = eliminate_bd_mode(
        point.metric, point.derivatives,
        betas=(0.0,1.0,0.0,0.0,0.0),
        g_fluid=g, f_fluid=f, finite_difference_step=2e-6,
    )
    measured = kinetic_ng3(physical.kinetic_hessian)
    expected = 0.0185421788  # De Felice Eq. (78)-(81), same exact Case-C point.
    assert math.isclose(measured, expected, rel_tol=0.03, abs_tol=5e-4), (measured, expected)


def test_case_c_high_k_physical_action_recovers_three_scalar_speed_branches():
    point, g, f = _case_c(0.05, 400.0)
    physical = eliminate_bd_mode(
        point.metric, point.derivatives,
        betas=(0.0,1.0,0.0,0.0,0.0),
        g_fluid=g, f_fluid=f,
        finite_difference_step=2e-6,
    )
    measured = np.sort(physical_squared_phase_speeds(
        physical.physical_hessian,
        a=point.metric.a,
        k=math.sqrt(point.metric.k2),
    ))
    grav = gravity_principal_action(
        point.metric,
        rho_f_plus_p_f=point.rho2,
    )
    expected = np.sort(np.array([
        grav.cs2,
        g.cs2,
        point.metric.c**2 * f.cs2,
    ]))
    assert math.isclose(grav.cs2, -0.6665833419871022, rel_tol=2e-10, abs_tol=2e-10)
    assert measured.shape == (3,)
    assert np.allclose(measured, expected, rtol=0.08, atol=0.03), (measured, expected)
