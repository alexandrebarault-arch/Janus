import math
import sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numerics.flrw_two_matter as flrw
from numerics.candidate_c_transfer import candidate_c_background_point


def _branch_value(a, p, reference_y=None):
    if reference_y is None:
        if math.isclose(a, 1.0):
            return float(flrw.positive_real_roots(1.0, p)[-1])
        grid = np.geomspace(1.0, a, 1800)
        return float(flrw.solve_branch(grid, p)[-1])
    roots = flrw.positive_real_roots(float(a), p)
    return float(min(roots, key=lambda r: abs(np.log(r/reference_y))))


def test_generic_branch_log_derivatives_match_candidate_c():
    p = flrw.candidate_c()
    eps = 5.0e-4
    for z in (0.0, 10.0, 100.0):
        a = 1.0/(1.0+z)
        y = _branch_value(a, p)
        y_N, y_NN = flrw.branch_log_derivatives(a, y, p)

        yp = _branch_value(a*math.exp(eps), p, y)
        ym = _branch_value(a*math.exp(-eps), p, y)
        y_N_fd = (yp-ym)/(2.0*eps)
        y_NN_fd = (yp - 2.0*y + ym)/(eps*eps)

        assert math.isclose(y_N, y_N_fd, rel_tol=2e-5, abs_tol=2e-8)
        assert math.isclose(y_NN, y_NN_fd, rel_tol=2e-5, abs_tol=2e-7)

        point = candidate_c_background_point(a, k_hmpc=0.02)
        assert math.isclose(y_N, point.y_N, rel_tol=2e-12, abs_tol=2e-12)
        assert math.isclose(y_NN, point.y_NN, rel_tol=2e-12, abs_tol=2e-12)


def test_candidate_c_dust_params_resolve_present_branch_on_shell():
    import numerics.candidate_c_dust_background as dust
    p_full = flrw.candidate_c()
    p = dust.candidate_c_dust_params()
    assert p.omega_g_r0 == 0.0
    assert p.beta1 == p_full.beta1
    assert p.beta2 == p_full.beta2
    assert p.beta3 == p_full.beta3
    assert p.beta4 == p_full.beta4
    assert p.alpha == p_full.alpha
    assert p.omega_g_m0 == p_full.omega_g_m0
    assert p.omega_f_m0 == p_full.omega_f_m0
    assert p.m2_over_H02 == p_full.m2_over_H02
    assert abs(flrw.branch_constraint(1.0, p.y0, p)) < 1.0e-11
    assert abs(p.y0 - p_full.y0) < 1.0e-6
    assert not math.isclose(p.y0, p_full.y0, rel_tol=0.0, abs_tol=1.0e-10)


def test_candidate_c_dust_background_is_on_shell_and_derivatives_are_consistent():
    import numerics.candidate_c_dust_background as dust
    p = dust.candidate_c_dust_params()
    for a in (1.0, 0.5, 0.1, 1.0/17.0):
        point = dust.candidate_c_dust_background_point(a, k_hmpc=0.05)
        assert abs(flrw.branch_constraint(a, point.y, p)) < 1.0e-11
        assert math.isclose(point.rho_g_m, 3.0*p.omega_g_m0*a**-3, rel_tol=1e-12)
        expected_f = 3.0*p.omega_f_m0*(p.y0/(a*point.y))**3
        assert math.isclose(point.rho_f_m, expected_f, rel_tol=1e-12)

    a = 1.0/11.0
    eps = 2.0e-5
    point = dust.candidate_c_dust_background_point(a, k_hmpc=0.02)
    plus = dust.candidate_c_dust_background_point(a*math.exp(eps), k_hmpc=0.02)
    minus = dust.candidate_c_dust_background_point(a*math.exp(-eps), k_hmpc=0.02)
    c_N_fd = (plus.metric.c-minus.metric.c)/(2.0*eps)
    c_N = point.derivatives.c_prime/point.metric.H
    assert math.isclose(c_N, c_N_fd, rel_tol=3e-5, abs_tol=3e-7)


def test_candidate_c_dust_linear_start_is_unique_meff_over_H_crossing():
    import numerics.candidate_c_dust_background as dust
    a_cross = dust.candidate_c_dust_linear_start()
    assert 1.0/18.0 < a_cross < 1.0/16.0
    assert math.isclose(dust.candidate_c_dust_meff_over_H(a_cross), 1.0,
                        rel_tol=0.0, abs_tol=2e-8)
    lo = dust.candidate_c_dust_meff_over_H(a_cross*0.999)
    hi = dust.candidate_c_dust_meff_over_H(a_cross*1.001)
    assert lo < 1.0 < hi


def test_candidate_c_dust_principal_speed_shift_matches_control_value():
    import numerics.candidate_c_dust_background as dust
    a = 0.5
    p_dust = dust.candidate_c_dust_params()
    pt = dust.candidate_c_dust_background_point(a, k_hmpc=0.1)
    d_dust = flrw.diagnostics(np.array([a]), np.array([pt.y]), p_dust)
    cs2_dust = float(d_dust['scalar_cs2'][0])

    p_full = flrw.candidate_c()
    y_full = _branch_value(a, p_full)
    d_full = flrw.diagnostics(np.array([a]), np.array([y_full]), p_full)
    cs2_full = float(d_full['scalar_cs2'][0])

    assert math.isclose(cs2_dust, 0.69207144458, rel_tol=2e-10, abs_tol=2e-10)
    rel_shift = cs2_dust/cs2_full - 1.0
    assert math.isclose(rel_shift, -1.23513e-5, rel_tol=3e-4, abs_tol=2e-9)
