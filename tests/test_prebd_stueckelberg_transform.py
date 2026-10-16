import numpy as np


def test_time_dependent_state_map_preserves_quadratic_action():
    from numerics.prebd_stueckelberg_transform import transform_state_rate_hessian
    rng = np.random.default_rng(123)
    n = 4
    H = rng.normal(size=(2*n, 2*n))
    H = 0.5 * (H + H.T)
    R = rng.normal(size=(n, n)) + 2.0*np.eye(n)
    Rdot = rng.normal(scale=0.2, size=(n, n))
    Hnew = transform_state_rate_hessian(H, R, Rdot)
    for _ in range(10):
        x = rng.normal(size=n)
        v = rng.normal(size=n)
        old = np.concatenate([R@x, Rdot@x + R@v])
        new = np.concatenate([x, v])
        assert np.isclose(
            0.5*old@H@old, 0.5*new@Hnew@new,
            rtol=2e-13, atol=2e-13,
        )


def test_prebd_bridge_maps_L_T_to_Y3_Z_and_rates():
    from numerics.prebd_stueckelberg_transform import prebd_bridge_matrices
    k = 7.0
    B = 1.3
    Bdot = -0.27
    R, Rdot = prebd_bridge_matrices(k=k, nHf=B, nHf_dot=Bdot)
    x = np.array([0.2, -0.1, 0.4, 0.3, 0.05, -0.02])
    v = np.array([-0.03, 0.07, 0.11, -0.08, 0.02, 0.01])
    old = R @ x
    olddot = Rdot @ x + R @ v
    assert np.isclose(old[2], -2.0*x[2])
    assert np.isclose(old[3], -B*x[3] + k*k*x[2]/3.0)
    assert np.isclose(olddot[2], -2.0*v[2])
    assert np.isclose(olddot[3], -B*v[3] - Bdot*x[3] + k*k*v[2]/3.0)
    assert np.allclose(old[[0, 1, 4, 5]], x[[0, 1, 4, 5]])


def test_Zdot_kinetic_null_becomes_Tdot_kinetic_null():
    from numerics.prebd_stueckelberg_transform import (
        prebd_bridge_matrices,
        transform_state_rate_hessian,
    )
    rng = np.random.default_rng(8)
    n = 6
    z = 3
    t = 3
    M = rng.normal(size=(n, n)); M = 0.5*(M + M.T)
    C = rng.normal(size=(n, n))
    K = rng.normal(size=(n, n)); K = 0.5*(K + K.T)
    K[z, :] = 0.0
    K[:, z] = 0.0
    H = np.block([[M, C], [C.T, K]])
    R, Rdot = prebd_bridge_matrices(k=12.0, nHf=0.9, nHf_dot=0.13)
    Hnew = transform_state_rate_hessian(H, R, Rdot)
    Knew = Hnew[n:, n:]
    assert np.linalg.norm(Knew[t, :], ord=np.inf) < 2e-13
    assert np.linalg.norm(Knew[:, t], ord=np.inf) < 2e-13
