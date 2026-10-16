import numpy as np


def _eliminate_null(canonical, z):
    n = canonical.shape[0] // 2
    keep_rate = [n+i for i in range(n) if i != z]
    keep11 = list(range(n)) + keep_rate
    H11 = canonical[np.ix_(keep11, keep11)]
    hzz = float(H11[z, z])
    assert abs(hzz) > 1e-8
    keep = [i for i in range(H11.shape[0]) if i != z]
    hpz = H11[np.ix_(keep, [z])]
    out = H11[np.ix_(keep, keep)] - hpz @ hpz.T / hzz
    return 0.5 * (out + out.T)


def _el_matrices(H0, Hp, Hm, h, measure_rate):
    n = H0.shape[0] // 2
    Q = H0[:n, :n]
    C = H0[:n, n:]
    K = H0[n:, n:]
    Cdot = (Hp[:n, n:] - Hm[:n, n:]) / (2*h)
    Kdot = (Hp[n:, n:] - Hm[n:, n:]) / (2*h)
    D = Kdot + measure_rate*K + C - C.T
    E = Cdot + measure_rate*C - Q
    return K, D, E


def test_prebd_stueckelberg_change_preserves_full_euler_lagrange_equations():
    from numerics.bd_time_canonicalization import canonicalize_linear_rate_time_dependent
    from numerics.prebd_stueckelberg_transform import (
        prebd_bridge_matrices,
        transform_state_rate_hessian,
    )

    rng = np.random.default_rng(2026)
    n = 6
    z = 3
    measure_rate = 0.37
    k = 5.2

    M0 = rng.normal(size=(n, n)); M0 = 0.5*(M0 + M0.T); M0[z, z] += 8.0
    M1 = rng.normal(scale=.1, size=(n, n)); M1 = 0.5*(M1 + M1.T)
    M2 = rng.normal(scale=.02, size=(n, n)); M2 = 0.5*(M2 + M2.T)
    C0 = rng.normal(scale=.3, size=(n, n))
    C1 = rng.normal(scale=.07, size=(n, n))
    C2 = rng.normal(scale=.01, size=(n, n))
    K0 = rng.normal(scale=.2, size=(n, n)); K0 = 0.5*(K0 + K0.T)
    K1 = rng.normal(scale=.03, size=(n, n)); K1 = 0.5*(K1 + K1.T)
    K2 = rng.normal(scale=.01, size=(n, n)); K2 = 0.5*(K2 + K2.T)
    for K in (K0, K1, K2):
        K[z, :] = 0.0
        K[:, z] = 0.0

    def old_hessian(t):
        M = M0 + t*M1 + 0.5*t*t*M2
        C = C0 + t*C1 + 0.5*t*t*C2
        K = K0 + t*K1 + 0.5*t*t*K2
        return np.block([[M, C], [C.T, K]])

    def nHf(t):
        return 1.1 + .23*t + .04*t*t

    def nHf_dot(t):
        return .23 + .08*t

    def new_hessian(t):
        R, Rdot = prebd_bridge_matrices(k=k, nHf=nHf(t), nHf_dot=nHf_dot(t))
        return transform_state_rate_hessian(old_hessian(t), R, Rdot)

    diff = 1e-5

    def canonical_family(raw, t):
        H = raw(t)
        Cplus = raw(t + diff)[:n, n:]
        Cminus = raw(t - diff)[:n, n:]
        dot_c = (Cplus[:, z] - Cminus[:, z]) / (2*diff)
        return canonicalize_linear_rate_time_dependent(
            H, dot_c=dot_c, mu_measure=measure_rate, z_index=z,
        )

    def physical_old(t):
        return _eliminate_null(canonical_family(old_hessian, t), z)

    def physical_new(t):
        return _eliminate_null(canonical_family(new_hessian, t), z)

    h = 2e-5
    old_EL = _el_matrices(
        physical_old(0.0), physical_old(h), physical_old(-h), h, measure_rate,
    )
    new_EL = _el_matrices(
        physical_new(0.0), physical_new(h), physical_new(-h), h, measure_rate,
    )

    # After the null coordinate is removed, the only remaining coordinate
    # change is the time-independent Y3=-2L map.
    S = np.diag([1.0, 1.0, -2.0, 1.0, 1.0])
    for new, old in zip(new_EL, old_EL):
        target = S.T @ old @ S
        scale = max(1.0, float(np.linalg.norm(target, ord=np.inf)))
        assert np.linalg.norm(new - target, ord=np.inf) / scale < 3e-5
