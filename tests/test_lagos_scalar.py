import importlib.util
import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_bridge import janus_J_Gamma


def test_lagos_interaction_bridge_matches_janus_J_gamma():
    spec = importlib.util.find_spec("numerics.lagos_scalar")
    assert spec is not None, "numerics.lagos_scalar is not implemented yet"

    from numerics.lagos_scalar import lagos_interaction_coefficients

    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    xi = 0.5922763712069927
    c = 0.8512702016825817

    coeff = lagos_interaction_coefficients(beta, xi=xi, c=c)
    J, Gamma = janus_J_Gamma(xi, c, beta)

    assert math.isclose(coeff.Z, J, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(xi * coeff.Z_tilde, Gamma, rel_tol=0.0, abs_tol=1e-12)

    with pytest.raises(TypeError):
        lagos_interaction_coefficients(beta, xi=xi, c=c, m2=2.3)


def test_beta1_radiation_background_satisfies_branch_friedmann_and_conservation():
    from numerics.lagos_scalar import beta1_radiation_background

    N = 0.1
    a = 1.0
    bg = beta1_radiation_background(N=N, a=a, beta1=1.0, m2=1.0)

    expected_rho = 1.0 / N - 3.0 * N
    assert math.isclose(bg.rho_star, expected_rho, rel_tol=0.0, abs_tol=1e-13)
    assert math.isclose(bg.H**2, a**2 / (3.0 * N), rel_tol=0.0, abs_tol=1e-13)
    assert math.isclose(bg.h, bg.X * bg.H, rel_tol=0.0, abs_tol=1e-13)

    rho_N = -1.0 / N**2 - 3.0
    assert math.isclose(rho_N * bg.N_prime, -4.0 * bg.H * bg.rho_star,
                        rel_tol=2e-13, abs_tol=1e-13)
    assert math.isclose(bg.h, bg.H + bg.N_prime / N,
                        rel_tol=2e-13, abs_tol=1e-13)


def test_lagos_auxiliary_equations_have_rank_four_and_reconstruct_constraints():
    from numerics.lagos_scalar import (
        LagosScalarState,
        beta1_radiation_background,
        lagos_auxiliary_residuals,
        solve_lagos_auxiliaries,
    )

    bg = beta1_radiation_background(N=0.1, a=1.0, beta1=1.0, m2=1.0)
    state = LagosScalarState(
        E1=0.021,
        E1_prime=-0.014,
        E2=0.032,
        E2_prime=0.017,
        psi2=0.011,
        psi2_prime=-0.006,
    )

    solution = solve_lagos_auxiliaries(
        bg, state, k=5.0, w=1.0 / 3.0, beta=(0.0, 1.0, 0.0, 0.0, 0.0),
        m2=1.0, nu2=1.0,
    )
    residuals = lagos_auxiliary_residuals(
        solution.vector, bg, state, k=5.0, w=1.0 / 3.0,
        beta=(0.0, 1.0, 0.0, 0.0, 0.0), m2=1.0, nu2=1.0,
    )

    assert solution.rank == 4
    assert max(abs(x) for x in residuals) < 2e-11


def test_lagos_eq323_loses_all_psi2_time_derivatives_after_auxiliary_elimination():
    from numerics.lagos_scalar import (
        LagosScalarState,
        beta1_radiation_background,
        lagos_eq323_reduced_residual,
    )

    bg = beta1_radiation_background(N=0.1, a=1.0, beta1=1.0, m2=1.0)
    beta = (0.0, 1.0, 0.0, 0.0, 0.0)
    common = dict(E1=0.021, E1_prime=-0.014, E2=0.032,
                  E2_prime=0.017, psi2=0.011)

    values = []
    for psi2_prime, psi2_double_prime in ((-0.006, 0.0), (0.2, -0.3), (-0.5, 0.7)):
        state = LagosScalarState(**common, psi2_prime=psi2_prime)
        values.append(lagos_eq323_reduced_residual(
            bg, state,
            E1_double_prime=0.03,
            E2_double_prime=-0.04,
            psi2_double_prime=psi2_double_prime,
            k=5.0, w=1.0 / 3.0, beta=beta, m2=1.0, nu2=1.0,
            derivative_step=1e-6,
        ))

    scale = max(1.0, max(abs(v) for v in values))
    assert max(abs(v - values[0]) for v in values) < 5e-8 * scale
