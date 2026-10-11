from numerics.two_matter_tophat import (
    v2_tophat_control_candidate,
    evolve_homogeneous_patch,
)


def test_zero_perturbation_reproduces_background():
    model = v2_tophat_control_candidate()
    result = evolve_homogeneous_patch(
        model,
        a_initial=1.0 / 11.0,
        delta_g_initial=0.0,
        delta_f_initial=0.0,
        visible_growth_slope=1.0,
    )
    assert abs(result.curvature_k) < 1e-8
    assert abs(result.delta_g_final) < 2e-6
    assert abs(result.delta_f_final) < 2e-6


def test_equal_anticorrelated_seed_is_not_preserved_in_control_candidate():
    model = v2_tophat_control_candidate()
    result = evolve_homogeneous_patch(
        model,
        a_initial=1.0 / 11.0,
        delta_g_initial=-1e-5,
        delta_f_initial=+1e-5,
        visible_growth_slope=1.0,
    )
    assert result.delta_g_final < -5e-5
    # The initially positive twin contrast is driven through zero in this
    # homogeneous separate-universe control.
    assert result.delta_f_final < 0.0


def test_large_primordial_twin_seed_can_preserve_anticorrelation():
    model = v2_tophat_control_candidate()
    result = evolve_homogeneous_patch(
        model,
        a_initial=1.0 / 11.0,
        delta_g_initial=-1e-5,
        delta_f_initial=+1e-4,
        visible_growth_slope=1.0,
    )
    assert result.delta_g_final < 0.0
    assert result.delta_f_final > 0.0
