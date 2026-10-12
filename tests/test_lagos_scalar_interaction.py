import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.lagos_scalar_action import (
    INTERACTION_STATE_ORDER,
    interaction_lagrangian_healthy,
    interaction_lagrangian_raw,
)


def test_raw_and_healthy_branch_interaction_actions_agree():
    point = candidate_c_background_point(0.5, k_hmpc=0.2)
    x = np.array([0.13, -0.07, 0.021, -0.018, 0.031, -0.027, 0.009, -0.011])

    raw = interaction_lagrangian_raw(point.metric, x)
    reduced = interaction_lagrangian_healthy(point.metric, x)
    assert math.isclose(raw, reduced, rel_tol=2e-12, abs_tol=2e-12)


def test_interaction_action_is_quadratic_and_has_no_alpha_l_k4_term():
    point = candidate_c_background_point(0.5, k_hmpc=0.2)
    x = np.array([0.09, -0.04, 0.015, 0.008, -0.02, 0.03, 0.01, -0.006])

    l1 = interaction_lagrangian_healthy(point.metric, x)
    l2 = interaction_lagrangian_healthy(point.metric, 2.0*x)
    assert math.isclose(l2, 4.0*l1, rel_tol=2e-13, abs_tol=2e-13)
    assert len(INTERACTION_STATE_ORDER) == 8

    # HR massive bigravity has alpha_L=0 in Lagos-Ferreira.  With all lapse,
    # shift and curvature perturbations zero, a pure E1/E2 configuration has
    # no direct interaction E^2 term; its gradient appears only after the
    # auxiliary constraints mix E with the Einstein-Hilbert sector.
    e_only = np.zeros(8)
    e_only[INTERACTION_STATE_ORDER.index("E1")] = 0.2
    e_only[INTERACTION_STATE_ORDER.index("E2")] = -0.1
    assert interaction_lagrangian_healthy(point.metric, e_only) == 0.0
