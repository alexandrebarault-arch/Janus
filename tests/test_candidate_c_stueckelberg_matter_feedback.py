import math
import numpy as np


def test_candidate_gravity_mode_requires_dynamic_dust_feedback():
    from numerics.candidate_c_dust_background import candidate_c_dust_background_point
    from numerics.candidate_c_linear_stueckelberg_action import (
        candidate_c_stueckelberg_local_squared_speeds,
        candidate_c_stueckelberg_local_system,
    )

    a = 0.5
    kh = 0.2
    system = candidate_c_stueckelberg_local_system(
        a, k_hmpc=kh,
        action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )
    full = candidate_c_stueckelberg_local_squared_speeds(
        a, k_hmpc=kh,
        action_derivative_step_N=2e-3,
        trajectory_derivative_step_N=2e-3,
    )[2]

    # State order is (Y1,Y2,L,Y1dot,Y2dot,Ldot).  This deliberately clamps
    # both matter coordinates/rates to zero and keeps only the L subsystem.
    # It is not a physical reduction; it is an audit proving that matter
    # feedback is O(1) and therefore cannot be removed as a static auxiliary.
    G = system.generator_cosmic
    Lblock = G[np.ix_([2, 5], [2, 5])]
    roots = np.linalg.eigvals(Lblock)
    point = candidate_c_dust_background_point(a, k_hmpc=kh)
    k = math.sqrt(point.metric.k2)
    clamped = float(np.real(roots[0]*roots[1]) * (a/k)**2)

    assert 0.45 < clamped < 0.55
    assert 0.65 < full < 0.75
    assert abs(full - clamped) > 0.15
