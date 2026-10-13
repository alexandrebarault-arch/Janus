import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.de_felice_bd_audit import case_c_bd_effective_coefficient


def test_case_c_bd_time_correction_converges_and_reproduces_large_cancellation():
    coarse = case_c_bd_effective_coefficient(
        a=0.05, k=400.0, f_cs2=0.1,
        background_step_fraction=2.0e-4,
        finite_difference_step=2.0e-6,
    )
    fine = case_c_bd_effective_coefficient(
        a=0.05, k=400.0, f_cs2=0.1,
        background_step_fraction=1.0e-4,
        finite_difference_step=2.0e-6,
    )

    assert coarse["raw_hZZ"] > 1.0e6
    assert fine["time_correction"] > 1.0e6
    assert fine["effective_hZZ"] < 0.0
    assert abs(fine["effective_hZZ"]) < 1.0e4
    assert math.isclose(
        coarse["effective_hZZ"], fine["effective_hZZ"],
        rel_tol=8e-3, abs_tol=10.0,
    )


def test_case_c_bd_cosmic_time_conversion_uses_conformal_H_as_adot():
    out = case_c_bd_effective_coefficient(
        a=0.05, k=400.0, f_cs2=0.1,
        background_step_fraction=1.0e-4,
        finite_difference_step=2.0e-6,
    )
    # ScalarBackground.H is conformal H = a H_cosmic, so for N=1:
    # da/dt = a H_cosmic = conformal H.
    assert math.isclose(out["a_dot"], out["conformal_H"], rel_tol=0.0, abs_tol=0.0)
