import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.comelli_descriptor import (
    LocalBarotropicFluid,
    STATE_ORDER,
    ROW_ORDER,
    polynomial_coefficients,
    polynomial_residual,
)


def _sample_background():
    bg = ScalarBackground(
        a=0.73,
        m2=2.4,
        f1=0.36,
        f2=0.58,
        H=1.35,
        H_omega=1.01,
        c=0.7481481481481481,
        xi=1.18,
        kappa=0.21,
        k2=4.7,
        G8pi=1.0,
    )
    bgp = ScalarBackgroundDerivatives(
        H_prime=-0.42,
        H_omega_prime=-0.31,
        c_prime=-0.08,
        xi_prime=0.05,
        f1_prime=0.02,
        f2_prime=-0.03,
    )
    return bg, bgp


def test_descriptor_polynomial_reconstructs_direct_residual():
    bg, bgp = _sample_background()
    g = LocalBarotropicFluid(rho=2.1, w=1.0/3.0)
    f = LocalBarotropicFluid(rho=1.7, w=0.0)
    x = np.array([
        0.031, 0.018, -0.012, 0.022, -0.017,
        0.014, -0.009, 0.027, 0.006, -0.019, 0.004,
    ])
    s = 0.37

    p0, p1, p2 = polynomial_coefficients(
        bg, bgp, g_fluid=g, f_fluid=f, a18_variant="derived_prime"
    )
    rebuilt = (p0 + s*p1 + s*s*p2) @ x
    direct = polynomial_residual(
        s, x, bg, bgp, g_fluid=g, f_fluid=f,
        a18_variant="derived_prime",
    )

    assert p0.shape == p1.shape == p2.shape == (13, 11)
    assert len(STATE_ORDER) == 11
    assert len(ROW_ORDER) == 13
    assert np.allclose(rebuilt, direct, rtol=2e-12, atol=2e-12)


def test_descriptor_keeps_a18_prime_and_printed_forms_distinct():
    bg, bgp = _sample_background()
    g = LocalBarotropicFluid(rho=2.1, w=1.0/3.0)
    f = LocalBarotropicFluid(rho=1.7, w=0.0)
    x = np.zeros(11)
    x[STATE_ORDER.index("E")] = 0.031
    s = 0.37

    r_prime = polynomial_residual(
        s, x, bg, bgp, g_fluid=g, f_fluid=f,
        a18_variant="derived_prime",
    )
    r_printed = polynomial_residual(
        s, x, bg, bgp, g_fluid=g, f_fluid=f,
        a18_variant="printed_unprime",
    )
    i = ROW_ORDER.index("A18")

    expected_difference = -(1.0-s)*x[0]*(bg.H+bg.H_omega)
    assert np.isclose(r_prime[i]-r_printed[i], expected_difference)
    assert not np.allclose(r_prime, r_printed)
