import numpy as np

from numerics.dust_mode_tracking import track_eigenpair_branch, pair_phase_speed_squared


def _osc(w):
    return np.array([[0.0, -w], [w, 0.0]])


def _generator(t):
    # The branch we want starts as the fastest pair but becomes slower than
    # another pair. A magnitude sort therefore switches identity near t=0.5.
    wg = 5.0 - 4.0*t
    wd = 2.0 + 1.9*t
    wo = 0.4
    D = np.block([
        [_osc(wg), np.zeros((2,2)), np.zeros((2,2))],
        [np.zeros((2,2)), _osc(wd), np.zeros((2,2))],
        [np.zeros((2,2)), np.zeros((2,2)), _osc(wo)],
    ])
    th = 0.55*t
    c, s = np.cos(th), np.sin(th)
    Q = np.block([
        [c*np.eye(2), -s*np.eye(2), np.zeros((2,2))],
        [s*np.eye(2),  c*np.eye(2), np.zeros((2,2))],
        [np.zeros((2,2)), np.zeros((2,2)), np.eye(2)],
    ])
    return Q @ D @ Q.T


def test_overlap_tracking_survives_frequency_crossing():
    t = np.linspace(0.0, 1.0, 41)
    generators = np.asarray([_generator(x) for x in t])
    branch = track_eigenpair_branch(generators, anchor_index=0)
    measured = np.sort(np.abs(branch.eigenvalues.imag), axis=1)[:, -1]
    expected = 5.0 - 4.0*t
    assert np.max(np.abs(measured-expected)) < 2e-10
    assert np.min(branch.overlap_scores[1:]) > 0.95

    naive = []
    for G in generators:
        vals = np.linalg.eigvals(G)
        pair = vals[np.argsort(np.abs(vals))[-2:]]
        naive.append(np.max(np.abs(pair.imag)))
    assert abs(naive[-1]-expected[-1]) > 2.5


def test_tracking_is_invariant_under_fixed_state_rescaling():
    t = np.linspace(0.0, 1.0, 31)
    generators = np.asarray([_generator(x) for x in t])
    scale = np.array([1e-6, 2e3, 7e-3, 5e2, 4.0, 0.2])
    S = np.diag(scale)
    Sinv = np.diag(1.0/scale)
    rescaled = np.asarray([S @ G @ Sinv for G in generators])
    branch = track_eigenpair_branch(rescaled, anchor_index=0, state_scale=1.0/scale)
    measured = np.sort(np.abs(branch.eigenvalues.imag), axis=1)[:, -1]
    expected = 5.0 - 4.0*t
    assert np.max(np.abs(measured-expected)) < 2e-9


def test_pair_phase_speed_uses_pair_product_sign():
    stable = np.array([-0.2+4.0j, -0.2-4.0j])
    unstable = np.array([3.0, -2.0])
    assert pair_phase_speed_squared(stable, a=0.5, k=2.0) > 0.0
    assert pair_phase_speed_squared(unstable, a=0.5, k=2.0) < 0.0


def test_tracker_only_returns_real_or_conjugate_dynamical_pairs():
    from numerics.dust_mode_tracking import is_real_dynamical_pair
    assert is_real_dynamical_pair(np.array([1.2, -0.7]))
    assert is_real_dynamical_pair(np.array([-0.3+2.0j, -0.3-2.0j]))
    assert not is_real_dynamical_pair(np.array([-0.3+2.0j, 0.4+1.5j]))


def test_default_anchor_is_itself_a_valid_dynamical_pair():
    G = np.block([
        [np.diag([-10.0, 1.0]), np.zeros((2,2)), np.zeros((2,2))],
        [np.zeros((2,2)), _osc(5.0), np.zeros((2,2))],
        [np.zeros((2,2)), np.zeros((2,2)), _osc(0.2)],
    ])
    branch = track_eigenpair_branch(np.asarray([G]))
    from numerics.dust_mode_tracking import is_real_dynamical_pair
    assert is_real_dynamical_pair(branch.eigenvalues[0])


def test_biorthogonal_tracking_resists_nonnormal_right_eigenvector_alignment():
    eps = 1e-6
    D = np.block([
        [_osc(5.0), np.zeros((2,2)), np.zeros((2,2))],
        [np.zeros((2,2)), _osc(2.0), np.zeros((2,2))],
        [np.zeros((2,2)), np.zeros((2,2)), _osc(0.2)],
    ])
    def similarity(x):
        S = np.eye(6)
        S[:,0] = [1,0,x*eps,0,0,0]
        S[:,1] = [0,1,0,x*eps,0,0]
        S[:,2] = [1,0,eps,0,0,0]
        S[:,3] = [0,1,0,eps,0,0]
        return S
    S0, S1 = similarity(0.0), similarity(2.0)
    G0 = S0 @ D @ np.linalg.inv(S0)
    G1 = S1 @ D @ np.linalg.inv(S1)
    vals0 = np.linalg.eigvals(G0)
    anchor = tuple(np.argsort(np.abs(np.abs(vals0)-5.0))[:2])
    branch = track_eigenpair_branch(np.asarray([G0,G1]), anchor_index=0, anchor_pair=anchor)
    assert np.allclose(np.sort(np.abs(branch.eigenvalues[1].imag)), [5.0,5.0], atol=1e-9)
