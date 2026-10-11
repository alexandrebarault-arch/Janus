import math

from numerics.cosmological_nonlinear_trajectory import (
    TrajectorySpec,
    source_to_contrast_ratio,
    track_case,
)


def test_case_a_realistic_void_trajectory_remains_connected():
    spec = TrajectorySpec(
        beta2=-3.0,
        beta3=3.0,
        start_mu=0.3964,
        h2_today=0.01,
        delta_g0=-0.8,
        delta_f0=1.0,
    )
    result = track_case(spec)
    assert result.failed_at is None
    assert result.last_a == 1.0
    assert 0.60 < result.last_mu < 0.75


def test_case_b_previous_dimensional_threshold_is_not_physical_void_threshold():
    spec = TrajectorySpec(
        beta2=-1.0,
        beta3=0.5,
        start_mu=1.0954,
        h2_today=0.01,
        delta_g0=-0.8,
        delta_f0=1.0,
    )
    result = track_case(spec)
    assert result.failed_at is None
    assert result.last_mu > 1.0


def test_dimensionful_source_threshold_must_be_normalized_by_h2():
    assert math.isclose(source_to_contrast_ratio(0.476, 0.01, 1.0), 47.6)
    assert math.isclose(source_to_contrast_ratio(0.03, 0.01, 3.0), 1.0)
