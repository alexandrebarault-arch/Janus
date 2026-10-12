import math

from numerics.ltb_regular_center import (
    required_c4,
    radial_metric_factor,
    regular_center_defect,
)


def test_constraint_46_requires_c4_minus_c3():
    assert required_c4(2.5) == -2.5


def test_regular_center_requires_unit_radial_normalization():
    assert math.isclose(regular_center_defect(1.0), 0.0)
    assert regular_center_defect(1.2) > 0.0


def test_regular_solution_has_flrw_constant_curvature_radial_factor():
    # C3=-k, so denominator 1+C3 chi^2 = 1-k chi^2.
    assert math.isclose(
        radial_metric_factor(chi=0.4, c3=-0.2, c1=1.0),
        1.0 / (1.0 - 0.2 * 0.4**2),
    )
