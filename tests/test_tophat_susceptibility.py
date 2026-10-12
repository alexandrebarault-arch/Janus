import pytest

from numerics.tophat_candidates import v2_late_mixing_control_candidate
from numerics.two_matter_tophat import v2_tophat_control_candidate
from numerics.tophat_susceptibility import initial_twin_growth_slope


def test_late_mixing_susceptibility_grows_toward_higuchi_boundary():
    model = v2_late_mixing_control_candidate()
    s25 = initial_twin_growth_slope(model, z=2.5, epsilon=1e-5)
    s30 = initial_twin_growth_slope(model, z=3.0, epsilon=1e-5)
    assert 7.0 < s25 < 12.0
    assert s30 > 40.0
    assert s30 > 4.0 * s25


def test_decoupled_control_does_not_show_large_positive_susceptibility_at_z3():
    model = v2_tophat_control_candidate()
    slope = initial_twin_growth_slope(model, z=3.0, epsilon=1e-5)
    assert slope < 1.0


def test_susceptibility_is_linear_in_seed_in_small_amplitude_limit():
    model = v2_late_mixing_control_candidate()
    small = initial_twin_growth_slope(model, z=2.5, epsilon=1e-6)
    larger = initial_twin_growth_slope(model, z=2.5, epsilon=1e-5)
    assert small == pytest.approx(larger, rel=0.03)
