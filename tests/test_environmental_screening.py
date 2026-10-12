import math

from numerics.environmental_screening import (
    critical_relative_contrast,
    rv_over_r,
    weighted_relative_contrast,
)
from numerics.higuchi_scale_window import (
    mass_ratio_from_compton_mpc,
    matter_higuchi_crossing_redshift,
)


def test_100mpc_mode_is_unscreened_for_order_unity_relative_void_today():
    delta_crit = critical_relative_contrast(
        lambda_mpc=100.0,
        z=0.0,
        omega_m0=0.30,
        h0_km_s_mpc=70.0,
    )
    assert 18300.0 < delta_crit < 18400.0
    ratio = rv_over_r(
        lambda_mpc=100.0,
        z=0.0,
        delta_relative=1.0,
        omega_m0=0.30,
        h0_km_s_mpc=70.0,
    )
    assert 0.037 < ratio < 0.039


def test_higuchi_crossing_has_order_six_screening_threshold_in_matter_era():
    mass_ratio = mass_ratio_from_compton_mpc(100.0, h0_km_s_mpc=70.0)
    z_h = matter_higuchi_crossing_redshift(mass_ratio, omega_m0=0.30)
    delta_crit = critical_relative_contrast(
        lambda_mpc=100.0,
        z=z_h,
        omega_m0=0.30,
        h0_km_s_mpc=70.0,
    )
    assert math.isclose(delta_crit, 6.0, rel_tol=1e-10)


def test_weighted_relative_contrast_adds_for_visible_void_and_twin_overdensity():
    # Source structure is proportional to delta_g - weight_f * delta_f.
    value = weighted_relative_contrast(
        delta_g=-0.8,
        delta_f=1.2,
        weight_f=0.5,
    )
    assert math.isclose(value, -1.4)
