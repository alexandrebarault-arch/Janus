import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.comelli_case_c import case_c_background_from_tau
from numerics.lagos_bridge import lagos_background_from_comelli


def _assert_bridge(point):
    lb = lagos_background_from_comelli(point.metric)
    bg = point.metric

    assert math.isclose(lb.a, bg.a, rel_tol=0.0, abs_tol=0.0)
    assert math.isclose(lb.r, bg.xi, rel_tol=2e-14)
    assert math.isclose(lb.b, bg.a * bg.xi, rel_tol=2e-14)
    assert math.isclose(lb.Nbar, bg.c * bg.xi, rel_tol=2e-14)

    # Lagos uses g-sector cosmic time t, while Comelli/JANUS stores
    # conformal Hubble rates calH=a H_cosmic and H_omega=b'/b.
    assert math.isclose(lb.H, bg.H / bg.a, rel_tol=2e-14)
    assert math.isclose(lb.Hb, bg.H_omega / bg.a, rel_tol=2e-14)

    # Massive-bigravity specialization of Lagos-Ferreira Eqs. (3.14)-(3.15).
    assert math.isclose(lb.Z, bg.m2 * bg.f2 / bg.xi, rel_tol=2e-14)
    assert math.isclose(lb.Ztilde, bg.m2 * bg.f1 / bg.xi, rel_tol=2e-14)

    # kappa=M_f^2/M_g^2, while Lagos nu^2=M_1^2/M_2^2.
    assert math.isclose(lb.nu2, 1.0 / bg.kappa, rel_tol=2e-14)


def test_lagos_bridge_matches_candidate_c_background():
    for a in (1.0, 0.5, 0.1):
        _assert_bridge(candidate_c_background_point(a, k_hmpc=0.2))


def test_lagos_bridge_matches_exact_case_c_background():
    point = case_c_background_from_tau(1e-2, k=25.0)
    _assert_bridge(point)


def test_healthy_branch_lapse_matches_db_da_on_candidate_c():
    point = candidate_c_background_point(0.5, k_hmpc=0.2)
    lb = lagos_background_from_comelli(point.metric)
    # b=a*xi and dxi/d ln a = y_N, hence db/da=xi+y_N=c*xi=Nbar.
    db_da = point.y + point.y_N
    assert math.isclose(lb.Nbar, db_da, rel_tol=2e-13)
