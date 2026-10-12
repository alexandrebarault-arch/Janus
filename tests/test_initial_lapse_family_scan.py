from numerics.initial_lapse_family_scan import evaluate_wall


def test_reference_wall_is_admissible():
    q = evaluate_wall(points=260, tol=8.0e-7)
    assert q["bvp_success"]
    assert q["admissible"]
    assert q["W_min"] > 0.75


def test_large_reference_amplitudes_remain_on_positive_lapse_branch():
    q = evaluate_wall(f_amp=0.32, g_amp=0.20, points=260, tol=8.0e-7)
    assert q["bvp_success"]
    assert q["admissible"]
    assert q["W_min"] > 0.70


def test_known_beta_wall_crosses_forbidden_lapse_branch():
    q = evaluate_wall(beta2=-0.35, beta3=0.0, points=420, tol=2.0e-7)
    assert q["bvp_success"]
    assert not q["admissible"]
    assert q["W_min"] < 0.0
    assert len(q["Wg_zero_brackets"]) >= 1
