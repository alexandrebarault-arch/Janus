from numerics.static_void_transition import (
    critical_void_transition,
    void_vainshtein_ratio,
)


def test_equal_weight_anticorrelated_void_has_endpoint_near_2p7_rv():
    c = critical_void_transition(q=-1.0)
    assert abs(c.mu_critical - 0.11223734) < 2e-5
    assert abs(c.source_g_critical + 0.22971182) < 2e-5
    assert 2.68 < c.radius_over_rv < 2.71


def test_endpoint_radius_is_weakly_dependent_on_anticorrelated_ratio():
    for q in (-0.1, -0.3, -1.0, -3.0, -10.0):
        c = critical_void_transition(q=q)
        assert 2.65 < c.radius_over_rv < 2.74


def test_void_vainshtein_ratio_places_transition_near_void_scale_for_hubble_mass():
    rv_over_r = void_vainshtein_ratio(
        omega_m=0.3,
        delta_g=-0.8,
        q=-1.0,
        m_eff_over_h0=1.5,
    )
    transition = 2.7 * rv_over_r
    assert 1.05 < transition < 1.20
