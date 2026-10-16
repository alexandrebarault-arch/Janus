import numpy as np


def test_direct_flat_map_equals_eq72_then_prebd_bridge():
    from numerics.prebd_stueckelberg_transform import (
        direct_flat_reduced_transform,
        prebd_bridge_matrices,
    )

    k = 9.0
    B = 1.7
    Bdot = -0.31
    A = 1.0 / B
    A_dot = -Bdot / (B*B)
    C = k*k / 6.0

    T = np.zeros((4, 4), dtype=float)
    T[0, 3] = 1.0
    T[1, 2] = 1.0
    T[2, 0] = 1.0
    T[3, 1] = 1.0
    T[3, 2] = A*C
    T[3, 3] = A
    Tdot = np.zeros((4, 4), dtype=float)
    Tdot[3, 2] = A_dot*C
    Tdot[3, 3] = A_dot

    eq72 = np.zeros((8, 8), dtype=float)
    eq72[:4, :4] = T
    eq72[4:, :4] = Tdot
    eq72[4:, 4:] = T
    extended = np.zeros((10, 12), dtype=float)
    cols = [0, 1, 2, 3, 6, 7, 8, 9]
    extended[np.ix_(range(8), cols)] = eq72
    extended[8, 4] = 1.0
    extended[9, 5] = 1.0

    R, Rdot = prebd_bridge_matrices(k=k, nHf=B, nHf_dot=Bdot)
    zero = np.zeros_like(R)
    bridge = np.block([[R, zero], [Rdot, R]])
    composed = extended @ bridge

    direct = direct_flat_reduced_transform(k=k, nHf=B, nHf_dot=Bdot)
    assert np.allclose(direct, composed, rtol=0.0, atol=2e-14)
