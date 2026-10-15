import math
import numpy as np


def test_linear_branch_coefficients_match_aoki_eqs_453_454():
    from numerics.aoki_oscillation_oracle import linear_branch_coefficients
    K, cs2 = linear_branch_coefficients(w=0.0)
    assert K == 0.75
    assert cs2 == -1.0
    K2, cs22 = linear_branch_coefficients(w=-0.2)
    assert math.isclose(K2, 0.75*(1.0-0.6), rel_tol=0, abs_tol=1e-15)
    assert math.isclose(cs22, (-1.2)/(0.4), rel_tol=0, abs_tol=1e-15)


def test_nonlinear_branch_coefficients_obey_aoki_product_identity():
    from numerics.aoki_oscillation_oracle import nonlinear_branch_coefficients
    controls = [
        (0.0, 0.4, 0.7, -0.6),
        (0.0, 3.0, 2.0/3.0, -0.75),
        (-0.2, -0.4, 0.9, -0.3),
    ]
    for w, beta2, beta3, mu in controls:
        K, cs2 = nonlinear_branch_coefficients(w=w, beta2=beta2, beta3=beta3, mu=mu)
        target = 0.5*(3.0*(1.0-w) + (1.0-(3.0*w-1.0)*beta2)*mu)
        assert math.isclose(K*cs2, target, rel_tol=1e-13, abs_tol=1e-13)


def test_pi_map_matches_aoki_eqs_450_451():
    from numerics.aoki_oscillation_oracle import pi_to_stueckelberg
    out = pi_to_stueckelberg(a=2.0, H=3.0, r=0.1, mu=-0.25, pi_eta=5.0, pi_r=-7.0)
    q = (2.0*0.1*3.0*(-0.25))/(1.0-0.25)
    expected_eta = -5.0/4.0 + q*(-7.0)/4.0
    expected_r = (-7.0)/(4.0*0.75) + q*5.0/4.0
    assert np.allclose(out, [expected_eta, expected_r], rtol=0, atol=1e-15)


def test_dust_double_root_counterexample_is_not_kinetic_zero():
    from numerics.aoki_oscillation_oracle import nonlinear_branch_coefficients
    K, cs2 = nonlinear_branch_coefficients(w=0.0, beta2=3.0, beta3=2.0/3.0, mu=-0.75)
    assert math.isclose(K, 375.0/128.0, rel_tol=0, abs_tol=1e-15)
    assert K > 0.0
    assert math.isfinite(cs2)
