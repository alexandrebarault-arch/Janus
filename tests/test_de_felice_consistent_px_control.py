import math
import numpy as np

from numerics.de_felice_consistent_px_control import (
    consistent_px_background,
    consistent_px_mode_speeds,
    consistent_px_gravity_target,
)


def test_consistent_px_nonhomothetic_control_matches_principal_gravity_speed():
    a=0.30
    bg=consistent_px_background(a, cs2_g=0.4, cs2_f=0.3)
    target=consistent_px_gravity_target(bg)
    speeds=consistent_px_mode_speeds(a, 1800.0, cs2_g=0.4, cs2_f=0.3)
    expected_matter=np.array(sorted((bg.ctilde*math.sqrt(0.3), math.sqrt(0.4))))
    assert abs(speeds[0]-target)<8e-4
    assert np.allclose(np.array(sorted(speeds[1:])), expected_matter, rtol=0.0, atol=8e-4)


def test_consistent_px_control_remains_healthy_away_from_proportional_limit():
    for a in (0.5,0.4,0.35,0.30):
        bg=consistent_px_background(a, cs2_g=0.4, cs2_f=0.3)
        assert bg.ctilde>0.0
        assert consistent_px_gravity_target(bg)>0.0
