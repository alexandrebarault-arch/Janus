import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_zero_metric_potentials_reduce_to_existing_pullback_formula():
    from numerics.nonhomothetic_stueckelberg_weak_metric import pullback_weak_f_metric

    out = pullback_weak_f_metric(
        b=1.3, c_background=0.6, r=0.8,
        Phi_f=0.0, Psi_f=0.0,
        sigma_dot=0.03, sigma_prime=-0.04,
        mu=0.2, mu_dot=0.05, mu_prime=-0.02,
    )
    J = np.array([[0.63, -0.04], [0.04, 1.184]])
    expected = 1.3**2*(J.T @ np.diag([-1.0, 1.0]) @ J)
    assert np.allclose(out.radial_block, expected, rtol=0.0, atol=1.0e-14)


def test_zero_stueckelberg_fields_reproduce_weak_nonhomothetic_f_metric():
    from numerics.nonhomothetic_stueckelberg_weak_metric import pullback_weak_f_metric

    b, c, r = 1.7, 0.43, 2.3
    Phi_f, Psi_f = 0.07, -0.03
    out = pullback_weak_f_metric(
        b=b, c_background=c, r=r,
        Phi_f=Phi_f, Psi_f=Psi_f,
        sigma_dot=0.0, sigma_prime=0.0,
        mu=0.0, mu_dot=0.0, mu_prime=0.0,
    )
    expected = np.diag([
        -b*b*c*c*(1.0 + 2.0*Phi_f),
        b*b*(1.0 - 2.0*Psi_f),
    ])
    assert np.allclose(out.radial_block, expected, rtol=0.0, atol=1.0e-14)
    assert abs(out.angular_coefficient - b*b*r*r*(1.0 - 2.0*Psi_f)) < 1.0e-14


def test_weak_g_inverse_radial_is_exact_for_newtonian_gauge_ansatz():
    from numerics.nonhomothetic_stueckelberg_weak_metric import weak_g_inverse_radial

    a = 0.8
    Phi_g = 0.06
    Psi_g = -0.02
    got = weak_g_inverse_radial(a=a, Phi_g=Phi_g, Psi_g=Psi_g)
    expected = np.diag([
        -1.0/(a*a*(1.0 + 2.0*Phi_g)),
        1.0/(a*a*(1.0 - 2.0*Psi_g)),
    ])
    assert np.allclose(got, expected, rtol=0.0, atol=1.0e-15)
