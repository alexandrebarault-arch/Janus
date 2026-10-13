import math
import numpy as np


def test_candidate_raw_couplings_satisfy_aoki_early_stability_sufficient_condition():
    from numerics.candidate_c_aoki_proxy import candidate_c_aoki_coupling_condition
    result = candidate_c_aoki_coupling_condition()
    assert result.beta2_raw < 0.0
    assert result.discriminant > 0.0
    assert result.sufficient_condition


def test_local_aoki_proxy_has_one_admissible_stable_dust_root_near_late_linear_start():
    from numerics.candidate_c_aoki_proxy import candidate_c_aoki_local_proxy
    point = candidate_c_aoki_local_proxy(0.057951440818742664, w=0.0)
    assert point.homothetic_proxy_only
    assert len(point.admissible_roots) == 1
    root = point.admissible_roots[0]
    assert math.isclose(root.mu, -0.73599, rel_tol=0.0, abs_tol=4e-4)
    assert root.kinetic > 0.0
    assert root.sound_speed_squared > 0.0
    assert math.isclose(root.kinetic, 0.0260, rel_tol=0.04, abs_tol=0.0)
    assert root.sound_speed_squared > 20.0


def test_local_aoki_admissible_root_varies_continuously_over_early_dust_interval():
    from numerics.candidate_c_aoki_proxy import candidate_c_aoki_proxy_track
    a = np.geomspace(0.02, 0.10, 33)
    track = candidate_c_aoki_proxy_track(a, w=0.0)
    mu = np.asarray([p.admissible_roots[0].mu for p in track])
    kinetic = np.asarray([p.admissible_roots[0].kinetic for p in track])
    cs2 = np.asarray([p.admissible_roots[0].sound_speed_squared for p in track])
    assert np.all(mu > -1.0)
    assert np.max(np.abs(np.diff(mu))) < 0.08
    assert np.all(kinetic > 0.0)
    assert np.all(cs2 > 0.0)


def test_proxy_explicitly_reports_nonhomothetic_mismatch():
    from numerics.candidate_c_aoki_proxy import candidate_c_aoki_local_proxy
    point = candidate_c_aoki_local_proxy(0.057951440818742664, w=0.0)
    # Aoki's derivation assumes f=K^2 g with constant K and hence c=1.
    # Candidate C is far from that at the planned late-linear start.
    assert abs(point.lapse_ctilde - 1.0) > 0.5
    assert point.homothetic_proxy_only
