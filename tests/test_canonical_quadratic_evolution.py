import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_canonical_phase_matrix_matches_hamilton_equations_with_measure():
    from numerics.canonical_quadratic_evolution import canonical_phase_matrix
    A = np.diag([4.0, 9.0, 16.0])
    B = np.array([[0.2, -0.1, 0.0], [0.05, 0.3, -0.07], [0.0, 0.02, -0.4]])
    D = np.diag([1.0, 0.5, 2.0])
    Hh = np.block([[A, B], [B.T, D]])
    Hg = 0.7
    F = canonical_phase_matrix(hamiltonian_hessian=Hh, H_g=Hg)
    expected = np.block([[B.T, D], [-A, -B - 3.0*Hg*np.eye(3)]])
    assert np.allclose(F, expected, rtol=0, atol=1e-14)


def test_fundamental_rhs_N_matches_matrix_exponential_for_constant_coefficients():
    from scipy.linalg import expm
    from scipy.integrate import solve_ivp
    from numerics.canonical_quadratic_evolution import (
        fundamental_rhs_N,
        canonical_phase_matrix_N,
    )
    Hh = np.diag([4.0, 9.0, 16.0, 1.0, 1.0, 1.0])
    Hg = 2.0

    def provider(N):
        return Hh, Hg

    N0, N1 = -0.4, 0.25
    F0 = np.eye(6).reshape(-1)
    sol = solve_ivp(
        lambda N, y: fundamental_rhs_N(N, y, coefficients_provider=provider),
        (N0, N1), F0, rtol=2e-11, atol=2e-13,
    )
    measured = sol.y[:, -1].reshape(6, 6)
    expected = expm(
        canonical_phase_matrix_N(hamiltonian_hessian=Hh, H_g=Hg) * (N1-N0)
    )
    assert np.allclose(measured, expected, rtol=2e-9, atol=2e-10)
