import numpy as np

from numerics.candidate_c_dust_stability import track_gravity_stability


def _gravity_block(c):
    return np.array([[0.0, 1.0], [-c, 0.0]])


def _osc(w):
    return np.array([[0.0, -w], [w, 0.0]])


def test_tracked_stability_boundary_survives_mode_frequency_reordering():
    a = np.linspace(0.2, 1.0, 81)
    generators = []
    for aa in a:
        cgrav = aa - 0.43
        G = np.block([
            [_gravity_block(cgrav), np.zeros((2,2)), np.zeros((2,2))],
            [np.zeros((2,2)), _osc(0.9 + 0.6*aa), np.zeros((2,2))],
            [np.zeros((2,2)), np.zeros((2,2)), _osc(0.2)],
        ])
        generators.append(G)
    generators = np.asarray(generators)
    vals = np.linalg.eigvals(generators[-1])
    order = np.argsort(np.abs(np.abs(vals) - np.sqrt(0.57)))[:2]
    result = track_gravity_stability(
        a,
        generators,
        k=1.0,
        anchor_pair=(int(order[0]), int(order[1])),
    )
    assert len(result.zero_crossings_a) == 1
    assert abs(result.zero_crossings_a[0] - 0.43) < 3e-4
    assert result.cs2[0] < 0.0
    assert result.cs2[-1] > 0.0
    assert result.late_healthy_start_a is not None
    assert abs(result.late_healthy_start_a - 0.43) < 3e-4
    assert np.min(result.overlap_scores[:-1]) > 0.99
