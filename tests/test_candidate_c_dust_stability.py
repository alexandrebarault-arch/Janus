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


def test_candidate_high_k_adaptive_track_does_not_switch_scalar_pair():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_stability import track_candidate_c_dust_gravity

    trajectory = build_candidate_c_dust_trajectory(0.2, grid_size=61)
    result = track_candidate_c_dust_gravity(
        0.2,
        samples=81,
        trajectory=trajectory,
        min_overlap=0.90,
        max_refinements=8,
    )
    # The old fixed 81-point tracker could jump to another pair and create
    # alternating negative pockets.  The late gravity-connected branch itself
    # remains positive and the weak-overlap intervals are refined automatically.
    assert len(result.a) > 81
    assert result.cs2[0] > 1.0e-5
    assert np.min(result.cs2) > 1.0e-5
    assert result.zero_crossings_a == ()
    assert result.late_healthy_start_a is not None
    assert abs(result.late_healthy_start_a-result.a[0]) < 1e-12
    assert np.min(result.overlap_scores[:-1]) >= 0.90
