import numpy as np

from numerics.candidate_c_dust_stability import (
    track_gravity_stability,
    principal_gravity_stability,
)


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


def test_principal_character_is_distinct_from_continuous_pair_identity():
    # A pair whose frequency decreases can exchange ordering with a dust-like
    # pair without changing its continuously transported identity.  The local
    # principal diagnostic intentionally follows the finite-speed character.
    a = np.linspace(0.2, 1.0, 121)
    generators = []
    for aa in a:
        principal = _gravity_block(aa-0.5) * 8.0
        transported = _osc(2.0 + 4.0*aa)
        slow = _osc(0.15)
        generators.append(np.block([
            [principal, np.zeros((2,2)), np.zeros((2,2))],
            [np.zeros((2,2)), transported, np.zeros((2,2))],
            [np.zeros((2,2)), np.zeros((2,2)), slow],
        ]))
    out = principal_gravity_stability(a, np.asarray(generators), k=1.0)
    assert len(out.zero_crossings_a) == 1
    assert abs(out.zero_crossings_a[0]-0.5) < 1e-3
    assert out.cs2[0] < 0.0
    assert out.cs2[-1] > 0.0


def test_candidate_high_k_principal_branch_crosses_near_a_point_10165():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_stability import candidate_c_dust_principal_stability

    trajectory = build_candidate_c_dust_trajectory(0.2, grid_size=61)
    result = candidate_c_dust_principal_stability(
        0.2, samples=241, trajectory=trajectory,
    )
    assert result.cs2[0] < -5.0e-3
    assert result.cs2[-1] > 0.5
    assert len(result.zero_crossings_a) == 1
    assert abs(result.zero_crossings_a[0] - 0.10165) < 8.0e-4
    assert result.late_healthy_start_a is not None
    assert abs(result.late_healthy_start_a - result.zero_crossings_a[0]) < 8.0e-4


def test_candidate_transport_reports_quasi_degenerate_mode_mixing():
    from numerics.candidate_c_dust_late_transfer import build_candidate_c_dust_trajectory
    from numerics.candidate_c_dust_stability import track_candidate_c_dust_gravity

    trajectory = build_candidate_c_dust_trajectory(0.2, grid_size=61)
    result = track_candidate_c_dust_gravity(
        0.2, samples=81, trajectory=trajectory,
        min_overlap=0.90, max_refinements=8,
    )
    assert len(result.a) > 81
    assert np.all(np.isfinite(result.cs2))
    # Persistent low overlap is a physical/mathematical mixing diagnostic,
    # not permission to relabel the transported pair as the principal mode.
    assert np.min(result.overlap_scores[:-1]) < 0.75
