import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.comelli_case_c import case_c_background_from_a
from numerics.lagos_action_bridge import lagos_bigravity_parameters


def test_lagos_map_matches_janus_f1_f2_on_candidate_c():
    point = candidate_c_background_point(0.5, k_hmpc=0.5)
    p = lagos_bigravity_parameters(point.metric)

    assert math.isclose(p.r, point.metric.xi, rel_tol=0.0, abs_tol=0.0)
    assert math.isclose(p.Nbar, point.metric.xi * point.metric.c, rel_tol=1e-14)
    assert math.isclose(p.Z, point.metric.m2 * point.metric.f2 / point.metric.xi, rel_tol=1e-14)
    assert math.isclose(p.Z_tilde, point.metric.m2 * point.metric.f1 / point.metric.xi, rel_tol=1e-14)
    assert math.isclose(p.r * p.Z, point.metric.m2 * point.metric.f2, rel_tol=1e-14)
    assert math.isclose(p.r * p.Z_tilde, point.metric.m2 * point.metric.f1, rel_tol=1e-14)


def test_lagos_map_reduces_to_a1_only_case_c_interaction():
    point = case_c_background_from_a(1e-3, k=10.0)
    p = lagos_bigravity_parameters(point.metric)

    # For a1-only Case C, J=1 and f1=f2=xi, so Z=Z_tilde=m^2=1.
    assert math.isclose(p.Z, 1.0, rel_tol=2e-12)
    assert math.isclose(p.Z_tilde, 1.0, rel_tol=2e-12)
    assert math.isclose(p.Nbar / p.r, point.metric.c, rel_tol=1e-14)
