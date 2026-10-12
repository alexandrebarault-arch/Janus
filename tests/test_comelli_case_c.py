import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_case_c import (
    case_c_xi_of_a,
    case_c_tau_of_a,
    case_c_a_of_tau,
    case_c_background_from_a,
    case_c_background_from_tau,
    scaled_derivative_coefficients,
)


def test_case_c_exact_branch_relation_and_early_limit():
    for a in (1e-4, 1e-3, 1e-2, 0.1):
        xi = case_c_xi_of_a(a)
        residual = a**4 * xi**2 + xi - a - a**4 / 3.0
        assert abs(residual) < 5e-14
    assert math.isclose(case_c_xi_of_a(1e-5) / 1e-5, 1.0, rel_tol=2e-10)


def test_case_c_background_is_dynamically_on_shell():
    bg = case_c_background_from_a(1e-3, k=10.0)
    assert bg.metric.c > 1.99 and bg.metric.c < 2.01
    assert math.isclose(bg.metric.H * 1e-3, 1.0, rel_tol=2e-6)
    assert math.isclose(bg.metric.H_omega / bg.metric.H, bg.metric.c, rel_tol=1e-13)
    assert math.isclose(bg.metric.f1, bg.metric.xi, rel_tol=1e-13)
    assert math.isclose(bg.metric.f2, bg.metric.xi, rel_tol=1e-13)
    assert math.isclose(bg.metric.k2, 100.0, rel_tol=0.0, abs_tol=0.0)


def test_case_c_tau_map_matches_series_and_inverts():
    a = 1.0e-2
    tau = case_c_tau_of_a(a)
    expected = a - a**6/12.0 - a**9/54.0
    assert math.isclose(tau, expected, rel_tol=0.0, abs_tol=2e-15)
    recovered = case_c_a_of_tau(tau)
    assert math.isclose(recovered, a, rel_tol=0.0, abs_tol=2e-13)

    by_tau = case_c_background_from_tau(tau, k=10.0)
    by_a = case_c_background_from_a(a, k=10.0)
    assert math.isclose(by_tau.metric.a, by_a.metric.a, rel_tol=0.0, abs_tol=2e-13)
    assert math.isclose(by_tau.metric.xi, by_a.metric.xi, rel_tol=2e-12)


def test_scaled_derivative_coefficients_preserve_x_operator():
    # D_tau[tau^p f(k tau)] = tau^(p-1) [p f + x f_x]
    # D_tau^2 gives (p-1+x d_x)(p+x d_x).
    p = 2.0
    x = 3.0
    f = x**4
    fx = 4.0*x**3
    fxx = 12.0*x**2
    first, second = scaled_derivative_coefficients(p, x, f, fx, fxx)
    assert math.isclose(first, p*f + x*fx)
    expected_second = p*(p-1.0)*f + 2.0*p*x*fx + x*x*fxx
    assert math.isclose(second, expected_second)
