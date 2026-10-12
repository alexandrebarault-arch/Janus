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
