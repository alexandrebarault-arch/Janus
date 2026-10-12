import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import (
    ScalarBackground,
    MetricState,
    MatterSources,
    constraint_residual_vector,
    constraint_matrix,
    solve_metric_constraints,
)


def _synthetic_case():
    bg = ScalarBackground(
        a=0.73, m2=2.4, f1=0.36, f2=0.58,
        H=1.35, H_omega=1.01, c=0.7481481481481481,
        xi=1.18, kappa=0.21, k2=4.7, G8pi=1.0,
    )
    state = MetricState(E=0.031, Phi1=0.018, Phi2=-0.012)
    E_prime = 0.009
    Phi1_prime = -0.006
    Phi2_prime = 0.004
    B1 = 0.022
    B2 = B1 - (1.0 - bg.c**2) * E_prime
    dphi = state.Phi1 - state.Phi2
    fsum = ((B1-E_prime)*(bg.H+bg.H_omega) - 2*bg.c**2*dphi) / bg.c**2
    d = (bg.H-bg.H_omega)*dphi
    F1 = (bg.H_omega*fsum - d)/(bg.H+bg.H_omega)
    F2 = fsum - F1
    q_true = np.array([E_prime, Phi1_prime, Phi2_prime, B1, B2, F1, F2])

    psi1 = bg.a**2*bg.m2*bg.f1*state.E - state.Phi1
    psi2 = -bg.a**2*bg.m2*bg.f1*state.E/(bg.kappa*bg.c*bg.xi**2) - state.Phi2
    base_g00 = (-2*bg.k2*state.Phi1
                +6*bg.H*(psi1*bg.H-Phi1_prime)
                +bg.a**2*bg.m2*bg.f2*(3*F1+bg.k2*state.E))
    drho_g = -base_g00/(bg.G8pi*bg.a**2)
    base_g0i = (2*psi1*bg.H - 2*Phi1_prime
                + bg.a**2*bg.m2*B1*bg.f2/(bg.c+1))
    mom_g = -base_g0i/(bg.G8pi*bg.a**2)

    c2=bg.c**2; xi2=bg.xi**2
    base_f00 = (-2*c2*bg.k2*state.Phi2
                +6*bg.H_omega*(psi2*bg.H_omega-Phi2_prime)
                +bg.m2*bg.a**2*bg.f2*c2/(bg.kappa*xi2)
                  *(-bg.k2*state.E-3*F2))
    drho_f = -base_f00*bg.kappa/(bg.G8pi*bg.a**2*c2*xi2)
    base_f0i = (2*bg.c*(psi2*bg.H_omega-Phi2_prime)
                -bg.m2*bg.a**2*bg.f2*B2/(bg.kappa*xi2*(1+bg.c)))
    mom_f = -base_f0i*bg.kappa/(bg.G8pi*bg.c*bg.a**2*xi2)

    src = MatterSources(delta_rho_g=drho_g, momentum_g=mom_g,
                        delta_rho_f=drho_f, momentum_f=mom_f)
    return bg, state, src, q_true


def test_full_constraint_matrix_has_one_dynamic_null_direction():
    bg, state, src, _ = _synthetic_case()
    A, _ = constraint_matrix(bg, state, src)
    assert np.linalg.matrix_rank(A, tol=1e-12) == 6


def test_constraint_solver_recovers_known_solution_when_E_prime_is_supplied():
    bg, state, src, q_true = _synthetic_case()
    solved = solve_metric_constraints(
        bg, state, src, E_prime=q_true[0]
    )
    assert np.allclose(solved.vector, q_true, rtol=0.0, atol=2e-12)
    assert solved.condition_number < 1e6
    assert solved.reduced_rank == 6
    assert np.linalg.norm(
        constraint_residual_vector(solved.vector, bg, state, src), ord=np.inf
    ) < 1e-11


def test_reduced_constraint_matrix_has_full_column_rank_at_c_equal_one():
    bg = ScalarBackground(a=1.0, m2=1.0, f1=0.4, f2=0.4,
                          H=1.0, H_omega=1.0, c=1.0,
                          xi=1.0, kappa=1.0, k2=10.0, G8pi=1.0)
    state = MetricState(E=0.0, Phi1=1e-5, Phi2=1e-5)
    src = MatterSources(delta_rho_g=0.0, momentum_g=0.0,
                        delta_rho_f=0.0, momentum_f=0.0)
    A, _ = constraint_matrix(bg, state, src)
    reduced = A[:, 1:]
    assert np.linalg.matrix_rank(reduced, tol=1e-12) == 6
    assert np.isfinite(np.linalg.cond(reduced))
