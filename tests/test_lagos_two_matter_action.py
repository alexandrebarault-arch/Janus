import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import pure_metric_lagrangian_healthy
import numerics.lagos_two_matter_action as two


def _proportional_background():
    return ScalarBackground(
        a=1.0,
        m2=1.7,
        f1=1.0,
        f2=1.0,
        H=0.8,
        H_omega=0.8,
        c=1.0,
        xi=1.0,
        kappa=1.0,
        k2=9.0,
        G8pi=1.0,
    )


def test_zero_matter_reduces_exactly_to_pure_metric_action():
    bg = _proportional_background()
    state = np.array([
        0.13, -0.08, 0.021, -0.017,
        0.032, -0.026, 0.011, -0.014,
        0.0, 0.0,
    ])
    rates = np.array([0.041, -0.037, 0.016, -0.012, 0.0, 0.0])

    assert hasattr(two, "KessenceBackground"), (
        "two-matter action background is not implemented"
    )
    vacuum = two.KessenceBackground(rho=0.0, pressure=0.0, cs2=1.0 / 3.0)
    measured = two.two_matter_lagrangian_healthy(
        bg, vacuum, vacuum, state, rates
    )
    expected = pure_metric_lagrangian_healthy(bg, state[:8], rates[:4])
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_equal_matter_action_is_exchange_symmetric_on_proportional_background():
    bg = _proportional_background()
    matter = two.KessenceBackground(rho=3.2, pressure=0.7, cs2=0.4)
    state = np.array([
        0.13, -0.08, 0.021, -0.017,
        0.032, -0.026, 0.011, -0.014,
        0.19, -0.23,
    ])
    rates = np.array([0.041, -0.037, 0.016, -0.012, 0.17, -0.21])

    swapped_state = state.copy()
    for i, j in ((0, 1), (2, 3), (4, 5), (6, 7), (8, 9)):
        swapped_state[i], swapped_state[j] = state[j], state[i]
    swapped_rates = rates.copy()
    for i, j in ((0, 1), (2, 3), (4, 5)):
        swapped_rates[i], swapped_rates[j] = rates[j], rates[i]

    lhs = two.two_matter_lagrangian_healthy(bg, matter, matter, state, rates)
    rhs = two.two_matter_lagrangian_healthy(
        bg, matter, matter, swapped_state, swapped_rates
    )
    assert math.isclose(lhs, rhs, rel_tol=2e-12, abs_tol=2e-12)


def test_two_matter_lapses_and_shifts_are_algebraically_eliminated():
    bg = _proportional_background()
    matter_g = two.KessenceBackground(rho=3.2, pressure=0.7, cs2=0.4)
    matter_f = two.KessenceBackground(rho=2.7, pressure=0.5, cs2=0.3)
    dynamic = np.array([0.13, -0.08, 0.021, -0.017, 0.19, -0.23])
    rates = np.array([0.041, -0.037, 0.016, -0.012, 0.17, -0.21])

    assert hasattr(two, "eliminate_two_matter_auxiliaries"), (
        "combined auxiliary elimination is not implemented"
    )
    solution = two.eliminate_two_matter_auxiliaries(
        bg, matter_g, matter_f, dynamic, rates
    )
    assert solution.auxiliary_hessian_rank == 4
    assert solution.stationarity_residual < 2e-11
    assert np.all(np.isfinite(solution.auxiliaries))
    assert math.isfinite(solution.reduced_lagrangian)


def test_metric_only_matter_residual_is_only_the_background_lapse_correction():
    """Lagos S_T already contains the other metric-only matter terms.

    For a general P(X) fluid the residual lapse susceptibility is the canonical
    Lagos correction plus the c_s-dependent difference from De Felice Eq. (54),
    giving (rho+P)/(2 c_s^2) Phi^2 per sector in its own volume measure.
    """
    bg = _proportional_background()
    matter_g = two.KessenceBackground(rho=3.2, pressure=0.7, cs2=0.4)
    matter_f = two.KessenceBackground(rho=2.7, pressure=0.5, cs2=0.3)
    state = np.array([
        0.13, -0.08, 0.021, -0.017,
        0.032, -0.026, 0.011, -0.014,
        0.0, 0.0,
    ])
    rates = np.array([0.041, -0.037, 0.016, -0.012, 0.0, 0.0])

    measured = two.two_matter_lagrangian_healthy(
        bg, matter_g, matter_f, state, rates
    ) - pure_metric_lagrangian_healthy(bg, state[:8], rates[:4])
    expected = 0.5 * bg.G8pi * (
        (matter_g.rho + matter_g.pressure) / matter_g.cs2 * state[4] ** 2
        + (matter_f.rho + matter_f.pressure) / matter_f.cs2 * state[5] ** 2
    )
    assert math.isclose(measured, expected, rel_tol=2e-12, abs_tol=2e-12)


def test_reduced_two_matter_velocity_hessian_has_three_kinetic_directions():
    """Two fluid scalars plus one helicity-0 gravity scalar must propagate."""
    bg = _proportional_background()
    matter_g = two.KessenceBackground(rho=3.2, pressure=0.7, cs2=0.4)
    matter_f = two.KessenceBackground(rho=2.7, pressure=0.5, cs2=0.3)

    assert hasattr(two, "reduced_two_matter_velocity_hessian"), (
        "reduced two-matter velocity Hessian is not implemented"
    )
    kinetic = two.reduced_two_matter_velocity_hessian(
        bg, matter_g, matter_f
    )
    assert kinetic.shape == (6, 6)
    assert np.allclose(kinetic, kinetic.T, rtol=1e-12, atol=1e-12)
    assert np.linalg.matrix_rank(kinetic, tol=1e-9) == 3
