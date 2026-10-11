from numerics.static_branch_selection import track_case_a_branch


def test_visible_dominated_case_keeps_homothetic_branch_deep_inside_rv():
    result = track_case_a_branch(q=1e-3, start_mu=0.0, u_max=100.0)
    assert result.failed_at_u is None


def test_twin_dominated_case_loses_homothetic_branch_before_rv():
    result = track_case_a_branch(q=10.0, start_mu=0.0, u_max=10.0)
    assert result.failed_at_u is not None
    assert result.failed_at_u < 1.0


def test_twin_dominated_case_has_regular_nonhomothetic_algebraic_branch():
    result = track_case_a_branch(q=10.0, start_mu=0.698872, u_max=100.0)
    assert result.failed_at_u is None


def test_case_a_environmental_branch_boundary_is_order_unity_in_q():
    low = track_case_a_branch(q=1.30, start_mu=0.698872, u_max=100.0)
    high = track_case_a_branch(q=1.40, start_mu=0.698872, u_max=100.0)
    assert low.failed_at_u is not None
    assert high.failed_at_u is None
