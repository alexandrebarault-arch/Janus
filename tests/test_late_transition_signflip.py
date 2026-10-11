import math

from numerics.asymmetric_twofluid import (
    critical_unscreened_strength_for_twin_sign_flip,
    critical_visible_fraction_for_twin_sign_flip,
)


def test_100_mpc_like_transition_requires_about_80_percent_visible_background():
    fcrit = critical_visible_fraction_for_twin_sign_flip(
        z_start=13.5132505, x=1.0
    )
    assert math.isclose(fcrit, 0.79934, rel_tol=3e-4)


def test_later_transition_requires_more_visible_dominance():
    fcrit = critical_visible_fraction_for_twin_sign_flip(
        z_start=8.142775, x=1.0
    )
    assert 0.893 < fcrit < 0.895


def test_partial_unscreening_must_be_strong_for_sign_flip():
    xcrit = critical_unscreened_strength_for_twin_sign_flip(
        f_g=0.90, z_start=13.5132505
    )
    assert 0.89 < xcrit < 0.90
