import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.de_felice_action_principal import gravity_principal_action
from numerics.flrw_two_matter import candidate_c, diagnostics, solve_branch


def _historical_cs2(a):
    p = candidate_c()
    grid = np.geomspace(1.0, a, 1600)
    y = solve_branch(grid, p)[-1]
    return float(diagnostics(np.array([a]), np.array([y]), p)["scalar_cs2"][0])


def test_action_principal_speed_matches_independent_de_felice_diagnostic():
    for a in (1.0, 0.5, 0.2):
        point = candidate_c_background_point(a, k_hmpc=0.5)
        action = gravity_principal_action(
            point.metric,
            rho_f_plus_p_f=point.rho_f_m,
        )
        expected = _historical_cs2(a)
        assert math.isclose(action.cs2, expected, rel_tol=3e-8, abs_tol=3e-10)
        assert math.isclose(action.gradient_coefficient / action.kinetic_coefficient, action.cs2, rel_tol=1e-14)


def test_action_principal_is_healthy_at_candidate_c_z1():
    point = candidate_c_background_point(0.5, k_hmpc=0.5)
    action = gravity_principal_action(point.metric, rho_f_plus_p_f=point.rho_f_m)

    assert action.kinetic_coefficient > 0.0
    assert action.gradient_coefficient > 0.0
    assert math.isclose(math.sqrt(action.cs2), 0.83191345, rel_tol=2e-6)
