import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_candidate_dust_bd_reduction_builds_regular_six_dimensional_hamiltonian():
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    out = candidate_c_dust_canonical_action(0.5, k_hmpc=0.1, derivative_step_N=2e-4)
    assert out.transformed_hessian.shape == (12, 12)
    assert out.canonical_hessian.shape == (12, 12)
    assert out.physical_phase_hessian.shape == (10, 10)
    assert out.hamiltonian_hessian.shape == (6, 6)
    assert out.kkt_matrix.shape == (5, 5)
    assert out.velocity_momentum_map.shape == (5, 6)
    assert np.all(np.isfinite(out.hamiltonian_hessian))
    assert np.allclose(out.hamiltonian_hessian, out.hamiltonian_hessian.T,
                       rtol=0, atol=2e-9)
    assert out.bd_algebraic_coefficient != 0.0
    assert out.zdot_kinetic_residual < 1e-8
    assert out.pdot_residual < 1e-8
    assert np.linalg.matrix_rank(out.kkt_matrix) == 5
    assert math.isfinite(out.kkt_condition_number)
    assert out.kkt_condition_number < 1e7


def test_legendre_kkt_map_satisfies_momentum_and_dust_algebraic_equations():
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    out = candidate_c_dust_canonical_action(0.5, k_hmpc=0.05, derivative_step_N=2e-4)
    H = out.physical_phase_hessian
    M = H[:5, :5]
    C = H[:5, 5:8]
    K = H[5:8, 5:8]
    z = np.array([0.03, -0.021, 0.014, 0.42, -0.31, 0.17])
    sol = out.velocity_momentum_map @ z
    v = sol[:3]
    p = sol[3:]
    x = np.r_[z[:3], p]
    Pi = K @ v + C.T @ x
    dust_eq = M[3:5, :] @ x + C[3:5, :] @ v
    assert np.allclose(Pi, z[3:], rtol=2e-10, atol=2e-9)
    assert np.allclose(dust_eq, 0.0, rtol=0, atol=2e-8)


def test_candidate_dust_dot_c_five_point_derivative_converges_on_dominant_components():
    from numerics.de_felice_dust_physical_action import candidate_c_dust_canonical_action
    coarse = candidate_c_dust_canonical_action(0.5, k_hmpc=0.1, derivative_step_N=2e-4)
    fine = candidate_c_dust_canonical_action(0.5, k_hmpc=0.1, derivative_step_N=1e-4)
    for i in (2, 3):
        assert math.isclose(coarse.dot_c[i], fine.dot_c[i], rel_tol=2e-6, abs_tol=2e-4)
    assert max(abs(coarse.zdot_column[4]), abs(coarse.zdot_column[5])) < 1e-10
