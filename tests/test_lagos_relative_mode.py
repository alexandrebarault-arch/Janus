import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_relative_mode import relative_common_kinetic_projection


def _bg(k=3.0):
    return ScalarBackground(
        a=1.0, m2=1.7, f1=1.0, f2=1.0,
        H=0.8, H_omega=0.8, c=1.0, xi=1.0,
        kappa=1.0, k2=k*k, G8pi=1.0,
    )


def test_only_relative_E_carries_reduced_metric_kinetic_term():
    p = relative_common_kinetic_projection(_bg())

    assert abs(p.psi_common) < 1e-9
    assert abs(p.psi_relative) < 1e-9
    assert abs(p.e_common) < 1e-9
    assert p.e_relative > 1e-6
    assert p.rank == 1


def test_relative_E_kinetic_coefficient_is_stable_across_H_and_k():
    for H in (0.2, 0.8, 1.5):
        for k in (1.0, 3.0, 10.0):
            bg = _bg(k)
            bg = ScalarBackground(**{**bg.__dict__, "H": H, "H_omega": H})
            p = relative_common_kinetic_projection(bg)
            assert p.rank == 1
            assert p.e_relative > 0.0
            assert math.isclose(p.e_common, 0.0, abs_tol=2e-9*max(1.0, p.e_relative))
