import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.de_felice_bd_audit import case_c_time_dependent_physical_action
from numerics.de_felice_invariants import kinetic_ng3


def test_case_c_time_dependent_bd_ng3_matches_de_felice_eq78_at_four_k():
    targets = {
        100.0: 0.015890,
        200.0: 0.017943,
        400.0: 0.0185421788,
        800.0: 0.018698,
    }
    for k, expected in targets.items():
        physical = case_c_time_dependent_physical_action(
            a=0.05,
            k=k,
            f_cs2=0.1,
            background_step_fraction=1.0e-3,
            finite_difference_step=2.0e-6,
        )
        measured = kinetic_ng3(physical.kinetic_hessian)
        assert math.isclose(
            measured, expected,
            rel_tol=0.03, abs_tol=5.0e-4,
        ), (k, measured, expected)
