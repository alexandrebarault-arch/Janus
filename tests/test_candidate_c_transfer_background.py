import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.flrw_two_matter import candidate_c, diagnostics, solve_branch
from numerics.candidate_c_transfer import candidate_c_background_point


def test_transfer_background_matches_flrw_candidate_c_diagnostics():
    p = candidate_c()
    for z in (0.0, 10.0, 100.0):
        a = 1.0/(1.0+z)
        grid = np.geomspace(1.0, a, 1200) if a < 1.0 else np.array([1.0, 0.999999])
        y_grid = solve_branch(grid, p)
        y = y_grid[-1] if a < 1.0 else p.y0
        d = diagnostics(np.array([a]), np.array([y]), p)
        point = candidate_c_background_point(a, k_hmpc=0.02)
        assert math.isclose(point.y, y, rel_tol=0.0, abs_tol=2e-9)
        assert math.isclose(point.metric.c, float(d['ctilde'][0]), rel_tol=0.0, abs_tol=2e-8)
        assert math.isclose(point.metric.f1, float(d['Gamma'][0]), rel_tol=0.0, abs_tol=2e-8)
        assert math.isclose(point.metric.f2, y*float(d['J'][0]), rel_tol=0.0, abs_tol=2e-8)
        assert math.isclose(point.metric.H, a*float(d['E'][0]), rel_tol=0.0, abs_tol=2e-8)
        assert math.isclose(point.metric.H_omega, point.metric.c*point.metric.H,
                            rel_tol=0.0, abs_tol=2e-10)


def test_analytic_c_log_derivative_matches_centered_branch_difference():
    a = 1.0/11.0
    point = candidate_c_background_point(a, k_hmpc=0.02)
    eps = 2e-5
    plus = candidate_c_background_point(a*math.exp(eps), k_hmpc=0.02)
    minus = candidate_c_background_point(a*math.exp(-eps), k_hmpc=0.02)
    c_N_fd = (plus.metric.c-minus.metric.c)/(2*eps)
    c_N = point.derivatives.c_prime/point.metric.H
    assert math.isclose(c_N, c_N_fd, rel_tol=2e-5, abs_tol=2e-7)


def test_background_matter_densities_follow_expected_scalings():
    p = candidate_c()
    point = candidate_c_background_point(1.0/21.0, k_hmpc=0.05)
    a = point.metric.a
    assert math.isclose(point.rho_g_m, 3*p.omega_g_m0*a**-3,
                        rel_tol=1e-12, abs_tol=0.0)
    assert math.isclose(point.rho_g_r, 3*p.omega_g_r0*a**-4,
                        rel_tol=1e-12, abs_tol=0.0)
    expected_f = 3*p.omega_f_m0*(p.y0/(a*point.y))**3
    assert math.isclose(point.rho_f_m, expected_f, rel_tol=1e-12, abs_tol=0.0)
