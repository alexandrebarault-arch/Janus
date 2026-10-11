from numerics.full_linear_health import linear_health_point
from numerics.tophat_candidates import v2_late_mixing_control_candidate
from numerics.two_matter_tophat import v2_tophat_control_candidate


def test_late_mixing_candidate_is_gradient_stable_just_before_w_boundary():
    model = v2_late_mixing_control_candidate()
    p = linear_health_point(model, z=3.0)
    assert p.j > 0.0
    assert p.w > 0.0
    assert p.b_kinetic > 0.0
    assert 0.75 < p.vector_cs2 < 0.90
    assert 0.25 < p.scalar_cs2 < 0.35


def test_decoupled_control_can_have_positive_w_but_scalar_gradient_instability():
    model = v2_tophat_control_candidate()
    p = linear_health_point(model, z=10.0)
    assert p.w > 0.0
    assert p.b_kinetic > 0.0
    assert p.vector_cs2 > 0.0
    assert p.scalar_cs2 < 0.0


def test_both_controls_are_well_behaved_today():
    late = linear_health_point(v2_late_mixing_control_candidate(), z=0.0)
    decoupled = linear_health_point(v2_tophat_control_candidate(), z=0.0)
    for p in (late, decoupled):
        assert p.w > 0.0
        assert p.b_kinetic > 0.0
        assert p.vector_cs2 > 0.0
        assert p.scalar_cs2 > 0.0
