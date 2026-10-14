import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_background_square_root_has_expected_nonhomothetic_eigenvalues():
    from numerics.nonhomothetic_hr_spherical import square_root_invariants

    a = 0.8
    b = 1.12
    c = 0.47
    inv = square_root_invariants(
        a=a, b=b, c_background=c, r=1.3,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    x = b/a
    eigenvalues = [x*c, x, x, x]
    expected = [
        1.0,
        sum(eigenvalues),
        sum(eigenvalues[i]*eigenvalues[j]
            for i in range(4) for j in range(i + 1, 4)),
        sum(eigenvalues[i]*eigenvalues[j]*eigenvalues[k]
            for i in range(4) for j in range(i + 1, 4)
            for k in range(j + 1, 4)),
        np.prod(eigenvalues),
    ]
    assert np.allclose(inv.elementary_symmetric, expected, rtol=0.0, atol=1.0e-13)


def test_homothetic_limit_reduces_to_binomial_elementary_symmetric_polynomials():
    from numerics.nonhomothetic_hr_spherical import square_root_invariants

    K = 1.37
    a = 0.62
    inv = square_root_invariants(
        a=a, b=K*a, c_background=1.0, r=0.9,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    expected = np.array([1.0, 4.0*K, 6.0*K*K, 4.0*K**3, K**4])
    assert np.allclose(inv.elementary_symmetric, expected, rtol=0.0, atol=2.0e-13)


def test_radial_square_root_squares_back_to_g_inverse_f_for_generic_map():
    from numerics.nonhomothetic_hr_spherical import square_root_invariants

    inv = square_root_invariants(
        a=0.9, b=1.1, c_background=0.6, r=0.7,
        sigma_dot=0.03, sigma_prime=-0.04,
        mu=0.2, mu_dot=0.05, mu_prime=-0.02,
    )
    assert np.allclose(
        inv.radial_square_root @ inv.radial_square_root,
        inv.radial_g_inverse_f,
        rtol=2.0e-13, atol=2.0e-13,
    )
