from numerics.self_consistent_transition import (
    common_band,
    integrate_transition,
    sign_flip_band,
)


def test_100mpc_lambda_flips_twin_sign_for_visible_weight_90_percent():
    out = integrate_transition(
        f_g=0.90, structure_mpc=100.0, lambda_mpc=100.0
    )
    assert out.delta_g > 0.0
    assert out.delta_f < 0.0
    assert 13.3 < out.z_transition < 13.7


def test_same_point_does_not_flip_for_visible_weight_80_percent():
    out = integrate_transition(
        f_g=0.80, structure_mpc=100.0, lambda_mpc=100.0
    )
    assert out.delta_f > 0.0


def test_goldilocks_band_for_100mpc_structure_and_90_percent_visible_weight():
    lo, hi = sign_flip_band(f_g=0.90, structure_mpc=100.0)
    assert 24.0 < lo < 26.0
    assert 200.0 < hi < 204.0


def test_common_band_across_50_to_200mpc_for_90_percent_visible_weight():
    lo, hi = common_band(
        f_g=0.90,
        structures_mpc=[50.0, 100.0, 150.0, 200.0],
    )
    assert 61.0 < lo < 63.0
    assert 180.0 < hi < 183.0
