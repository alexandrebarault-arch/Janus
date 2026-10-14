import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_zero_stueckelberg_fields_reproduce_nonhomothetic_flrw_f_metric():
    from numerics.nonhomothetic_stueckelberg_spherical import pullback_f_metric

    out = pullback_f_metric(
        b=1.7, c_background=0.43, r=2.3,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    assert np.allclose(
        out.radial_block,
        np.diag([-(1.7*0.43)**2, 1.7**2]),
        atol=1.0e-14, rtol=0.0,
    )
    assert abs(out.angular_coefficient - (1.7*2.3)**2) < 1.0e-14


def test_homothetic_limit_reproduces_aoki_offdiagonal_kinematics():
    from numerics.nonhomothetic_stueckelberg_spherical import pullback_f_metric

    b = 1.4
    r = 0.7
    sigma_dot = 0.08
    sigma_prime = -0.13
    mu = 0.31
    mu_dot = 0.04
    mu_prime = -0.06
    out = pullback_f_metric(
        b=b, c_background=1.0, r=r,
        sigma_dot=sigma_dot, sigma_prime=sigma_prime,
        mu=mu, mu_dot=mu_dot, mu_prime=mu_prime,
    )
    expected = b*b*(
        -(1.0 + sigma_dot)*sigma_prime
        + (r*mu_dot)*(1.0 + mu + r*mu_prime)
    )
    assert abs(out.radial_block[0, 1] - expected) < 1.0e-14


def test_orientation_jacobian_matches_coordinate_map():
    from numerics.nonhomothetic_stueckelberg_spherical import stueckelberg_jacobian

    J = stueckelberg_jacobian(
        c_background=0.6, r=0.8,
        sigma_dot=0.02, sigma_prime=0.04,
        mu=0.2, mu_dot=-0.03, mu_prime=0.05,
    )
    expected = np.array([[0.62, 0.04], [-0.024, 1.24]])
    assert np.allclose(J, expected, atol=1.0e-14, rtol=0.0)
