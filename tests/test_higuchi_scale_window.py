import math

from numerics.higuchi_scale_window import (
    eds_relative_growth,
    hubble_length_mpc,
    mass_ratio_from_compton_mpc,
    matter_higuchi_crossing_redshift,
)


def test_100_mpc_scale_implies_transition_around_z_13_for_h70():
    ratio = mass_ratio_from_compton_mpc(100.0, h0_km_s_mpc=70.0)
    assert 42.7 < ratio < 43.0
    z = matter_higuchi_crossing_redshift(ratio, omega_m0=0.30)
    assert 13.3 < z < 13.7


def test_maximal_relative_growth_from_transition_is_modest_for_tiny_seed():
    growth = eds_relative_growth(13.5)
    assert 23.0 < growth < 25.0
    assert 1e-5 * growth < 3e-4


def test_hubble_length_for_h70():
    assert math.isclose(hubble_length_mpc(70.0), 4282.7494, rel_tol=1e-6)
