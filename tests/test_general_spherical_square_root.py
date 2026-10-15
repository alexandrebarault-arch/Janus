import numpy as np


def test_general_block_helper_reproduces_existing_diagonal_g_path():
    from numerics.nonhomothetic_hr_spherical import (
        square_root_invariants,
        square_root_invariants_from_blocks,
    )
    a = 1.3
    b = 0.9
    r = 0.4
    old = square_root_invariants(
        a=a, b=b, c_background=0.8, r=r,
        sigma_dot=0.03, sigma_prime=-0.02,
        mu=-0.1, mu_dot=0.04, mu_prime=0.01,
    )
    J = np.array([[0.83, -0.02], [r*0.04, 1.0-0.1+r*0.01]])
    f = b*b*(J.T @ np.diag([-1.0, 1.0]) @ J)
    g = np.diag([-a*a, a*a])
    new = square_root_invariants_from_blocks(
        g_radial=g,
        g_angular=a*a*r*r,
        f_radial=f,
        f_angular=(b*(1.0-0.1)*r)**2,
    )
    assert np.allclose(new.radial_square_root, old.radial_square_root, rtol=0, atol=1e-13)
    assert np.allclose(new.elementary_symmetric, old.elementary_symmetric, rtol=0, atol=1e-13)


def test_common_pullback_of_homothetic_pair_preserves_K_eigenvalues():
    from numerics.nonhomothetic_hr_spherical import square_root_invariants_from_blocks
    K = 0.73
    J = np.array([[1.07, 0.13], [-0.09, 0.88]])
    native = np.diag([-1.0, 1.0])
    g = J.T @ native @ J
    f = K*K*g
    R = 1.21
    gth = R*R
    fth = K*K*gth
    inv = square_root_invariants_from_blocks(
        g_radial=g, g_angular=gth,
        f_radial=f, f_angular=fth,
    )
    assert np.allclose(inv.radial_square_root, K*np.eye(2), rtol=0, atol=1e-13)
    assert abs(inv.angular_eigenvalue-K) < 1e-13
    expected = np.array([1.0, 4.0*K, 6.0*K*K, 4.0*K**3, K**4])
    assert np.allclose(inv.elementary_symmetric, expected, rtol=0, atol=1e-13)
