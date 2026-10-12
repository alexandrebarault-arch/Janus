import importlib.util
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_bridge import janus_J_Gamma


def test_lagos_interaction_bridge_matches_janus_J_gamma():
    spec = importlib.util.find_spec("numerics.lagos_scalar")
    assert spec is not None, "numerics.lagos_scalar is not implemented yet"

    from numerics.lagos_scalar import lagos_interaction_coefficients

    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    xi = 0.5922763712069927
    c = 0.8512702016825817
    m2 = 2.3

    coeff = lagos_interaction_coefficients(beta, xi=xi, c=c, m2=m2)
    J, Gamma = janus_J_Gamma(xi, c, beta)

    assert math.isclose(coeff.Z, m2 * J, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(xi * coeff.Z_tilde, m2 * Gamma, rel_tol=0.0, abs_tol=1e-12)


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
