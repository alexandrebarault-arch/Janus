import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_exact_polynomial_reproduces_representative_real_roots():
    from numerics.candidate_c_aoki_full_proxy import real_roots_at_a

    roots = real_roots_at_a(0.02)
    assert np.min(abs(roots + 0.8842714061688633)) < 2.0e-10
    assert np.min(abs(roots)) < 1.0e-12


def test_early_stable_branch_stays_simple_and_does_not_join_linear_root():
    from numerics.candidate_c_aoki_full_proxy import track_early_stable_branch

    a = np.geomspace(0.01, 1.0, 500)
    track = track_early_stable_branch(a)
    assert np.max(np.abs(track.mu_imag)) < 1.0e-10
    assert np.min(track.nearest_root_separation) > 0.05

    j = int(np.argmin(abs(a - 0.10165)))
    assert track.mu[j] < -0.5
    assert abs(track.mu[-1]) > 0.4


def test_small_equal_adiabatic_source_probe_does_not_remove_branch_gap():
    from numerics.candidate_c_aoki_full_proxy import track_early_stable_branch

    a = np.geomspace(0.02, 0.12, 180)
    for fraction in (1.0e-4, 1.0e-3, 1.0e-2):
        track = track_early_stable_branch(a, equal_source_fraction=fraction)
        j = int(np.argmin(abs(a - 0.10165)))
        assert track.mu[j] < -0.5
        assert track.nearest_root_separation[j] > 0.15
