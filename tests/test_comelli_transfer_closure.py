import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.candidate_c_transfer import candidate_c_background_point
from numerics.comelli_transfer import (
    FluidPerturbations,
    solve_metric_closure,
)


def _sample_state(point):
    # Keep the shear variable at its natural sub-horizon scale k^2 E~1e-5.
    E = 1.0e-5 / max(point.metric.k2, 1.0)
    E_prime = point.metric.H * E
    fluids = FluidPerturbations(
        delta_m=1.0e-5,
        u_m=0.0,
        delta_r=4.0e-5/3.0,
        u_r=0.0,
        delta_f=0.8e-5,
        u_f=0.0,
    )
    return E, E_prime, fluids


def test_candidate_c_closure_satisfies_unused_f00_bianchi_identity():
    point = candidate_c_background_point(1.0/11.0, k_hmpc=0.02)
    E, E_prime, fluids = _sample_state(point)
    solved = solve_metric_closure(point, E=E, E_prime=E_prime, fluids=fluids)

    assert solved.rank == 12
    assert solved.normalized_residual < 1e-11
    assert solved.f00_bianchi_relative < 1e-9
    assert math.isfinite(solved.condition_number)


def test_closure_bianchi_check_survives_candidate_c_scale_redshift_grid():
    for z in (0.0, 10.0, 100.0, 140.0):
        for k_hmpc in (0.01, 0.02, 0.05):
            point = candidate_c_background_point(
                1.0/(1.0+z), k_hmpc=k_hmpc
            )
            E, E_prime, fluids = _sample_state(point)
            solved = solve_metric_closure(
                point, E=E, E_prime=E_prime, fluids=fluids
            )
            assert solved.rank == 12
            assert solved.normalized_residual < 2e-10
            assert solved.f00_bianchi_relative < 2e-8


def test_metric_closure_is_linear_in_perturbation_amplitude():
    point = candidate_c_background_point(1.0/3.0, k_hmpc=0.02)
    E, E_prime, fluids = _sample_state(point)
    one = solve_metric_closure(point, E=E, E_prime=E_prime, fluids=fluids)
    two = solve_metric_closure(
        point,
        E=2.0*E,
        E_prime=2.0*E_prime,
        fluids=FluidPerturbations(*(
            2.0*np.array(fluids.as_tuple(), dtype=float)
        )),
    )
    assert np.allclose(two.vector, 2.0*one.vector, rtol=2e-10, atol=1e-12)
