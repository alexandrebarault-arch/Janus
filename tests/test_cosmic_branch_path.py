import numpy as np
from numerics.cosmic_branch_path import track_matter_era_path


def test_case_a_connects_early_gr_to_late_nonlinear_branch():
    result = track_matter_era_path(
        beta2=-3,
        beta3=3,
        start_mu=0.396418,
        h2_early=1e6,
        h2_late=1e-3,
        delta_i=1e-5,
        growth_exponent=1.186,
        steps=1200,
    )
    assert result.failed_at_h2 is None
    assert abs(result.last_mu - 0.69817) < 5e-3


def test_case_b_loses_adiabatic_branch_near_transition():
    result = track_matter_era_path(
        beta2=-1,
        beta3=0.5,
        start_mu=1.095445,
        h2_early=1e6,
        h2_late=1e-3,
        delta_i=1e-5,
        growth_exponent=1.186,
        steps=1600,
    )
    assert result.failed_at_h2 is not None
    assert 0.005 < result.failed_at_h2 < 0.03
