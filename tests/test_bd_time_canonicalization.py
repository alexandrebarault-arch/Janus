import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.bd_time_canonicalization import canonicalize_linear_zdot_time_dependent


def test_time_dependent_zdot_canonicalization_matches_integration_by_parts():
    H = np.zeros((8, 8), dtype=float)
    M = np.diag([1.0, 2.0, 3.0, 11.0])
    C = np.arange(16, dtype=float).reshape(4, 4) / 10.0
    K = np.diag([2.0, 3.0, 4.0, 0.0])
    H[:4, :4] = M
    H[:4, 4:] = C
    H[4:, :4] = C.T
    H[4:, 4:] = K

    dot_c = np.array([0.3, -0.2, 0.5, 0.7], dtype=float)
    mu_measure = 1.25
    out = canonicalize_linear_zdot_time_dependent(
        H, dot_c=dot_c, mu_measure=mu_measure,
    )

    c = C[:, 3].copy()
    correction = dot_c + mu_measure * c

    expected_M = M.copy()
    for i in range(3):
        expected_M[i, 3] -= correction[i]
        expected_M[3, i] -= correction[i]
    expected_M[3, 3] -= correction[3]

    expected_C = C.copy()
    for i in range(3):
        expected_C[3, i] -= c[i]
    expected_C[:, 3] = 0.0

    assert np.allclose(out[:4, :4], expected_M, rtol=0.0, atol=1.0e-14)
    assert np.allclose(out[:4, 4:], expected_C, rtol=0.0, atol=1.0e-14)
    assert np.allclose(out[4:, :4], expected_C.T, rtol=0.0, atol=1.0e-14)
    assert np.allclose(out[4:, 4:], K, rtol=0.0, atol=1.0e-14)
