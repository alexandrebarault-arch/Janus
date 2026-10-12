from numerics.nonlinear_source_continuation import connected_branch_until


def test_case_a_branch_survives_strong_anticorrelated_source():
    result = connected_branch_until(
        beta2=-3.0,
        beta3=3.0,
        h2=0.01,
        start_mu=0.6920784193,
        source_max=5.0,
        source_step=0.01,
    )
    assert result.failed_at is None
    assert result.last_source >= 5.0 - 1e-12


def test_case_b_linear_branch_terminates_near_known_source_endpoint():
    result = connected_branch_until(
        beta2=-1.0,
        beta3=0.5,
        h2=0.01,
        start_mu=0.0,
        source_max=0.7,
        source_step=0.0005,
    )
    assert result.failed_at is not None
    assert 0.47 < result.failed_at < 0.49
