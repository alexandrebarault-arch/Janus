from numerics.critical_susceptibility import susceptibility_health_point
from numerics.tophat_candidates import v2_late_mixing_control_candidate


def test_late_mixing_response_scales_like_inverse_w_near_boundary():
    model = v2_late_mixing_control_candidate()
    p25 = susceptibility_health_point(model, z=2.5, epsilon=1e-5)
    p30 = susceptibility_health_point(model, z=3.0, epsilon=1e-5)

    assert p25.w_over_h2 > 0.0
    assert p30.w_over_h2 > 0.0
    assert p30.w_over_h2 < p25.w_over_h2
    assert p30.twin_growth_slope > p25.twin_growth_slope

    # In this control trajectory the product stays O(5), indicating a
    # susceptibility approximately proportional to 1/W as W -> 0+.
    assert 4.0 < p25.slope_times_w_over_h2 < 6.5
    assert 4.0 < p30.slope_times_w_over_h2 < 6.5
    assert abs(p30.slope_times_w_over_h2 / p25.slope_times_w_over_h2 - 1.0) < 0.20
