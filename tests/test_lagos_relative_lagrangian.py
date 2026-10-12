import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_relative_mode import (
    relative_common_kinetic_projection,
    relative_e_slice_coefficients,
)


def _bg():
    return ScalarBackground(
        a=1.0, m2=1.7, f1=1.0, f2=1.0,
        H=0.8, H_omega=0.8, c=1.0, xi=1.0,
        kappa=1.0, k2=9.0, G8pi=1.0,
    )


def test_relative_slice_kinetic_matches_hessian_projection():
    bg = _bg()
    p = relative_common_kinetic_projection(bg)
    c = relative_e_slice_coefficients(bg)

    assert c.kinetic > 0.0
    assert math.isclose(c.kinetic, p.e_relative, rel_tol=2e-11, abs_tol=2e-11)


def test_relative_slice_coefficients_are_finite_structural_controls():
    c = relative_e_slice_coefficients(_bg())
    assert math.isfinite(c.kinetic)
    assert math.isfinite(c.mixed)
    assert math.isfinite(c.static)
