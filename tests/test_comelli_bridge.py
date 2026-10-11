import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_bridge import (
    beta_to_comelli_a,
    comelli_f1_f2,
    janus_J_Gamma,
    comelli_branch_lhs,
    janus_branch_potential_lhs,
)


def test_beta_to_comelli_factorial_mapping():
    beta = (0.0, 1.2, -3.4, 5.6, -7.8)
    a = beta_to_comelli_a(beta)
    assert a == (0.0, 1.2, -1.7, 5.6 / 6.0, -7.8 / 24.0)


def test_f1_f2_match_janus_J_Gamma():
    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    y = 0.5922763712069927
    c = 0.8512702016825817
    a = beta_to_comelli_a(beta)
    f1, f2 = comelli_f1_f2(y, c, a)
    J, Gamma = janus_J_Gamma(y, c, beta)
    assert math.isclose(f2, y * J, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(f1, Gamma, rel_tol=0.0, abs_tol=1e-12)


def test_background_constraint_potential_parts_are_same_equation():
    beta = (0.0, 1.0, -4.2383993109, 13.6801214252, -38.5117901844)
    y = 0.9335321962075307
    kappa = 0.10879548725**2
    a = beta_to_comelli_a(beta)
    # Comelli Eq. (3.8) LHS is the negative of the standard
    # Hassan-Rosen potential difference divided by three.
    lhs_comelli = comelli_branch_lhs(y, kappa, a)
    lhs_janus = janus_branch_potential_lhs(y, kappa, beta)
    assert math.isclose(lhs_comelli, -lhs_janus, rel_tol=0.0, abs_tol=1e-12)
