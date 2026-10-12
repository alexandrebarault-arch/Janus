import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import (
    INTERACTION_STATE_ORDER,
    RATE_ORDER,
    pure_metric_lagrangian_healthy,
    velocity_hessian,
)


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


def _swap_metrics(x):
    x = np.asarray(x, dtype=float)
    out = x.copy()
    pairs = (("Psi1", "Psi2"), ("E1", "E2"), ("Phi1", "Phi2"), ("B1", "B2"))
    for a, b in pairs:
        ia = INTERACTION_STATE_ORDER.index(a)
        ib = INTERACTION_STATE_ORDER.index(b)
        out[ia], out[ib] = x[ib], x[ia]
    return out


def _swap_rates(v):
    v = np.asarray(v, dtype=float)
    out = v.copy()
    for a, b in (("Psi1_dot", "Psi2_dot"), ("E1_dot", "E2_dot")):
        ia = RATE_ORDER.index(a)
        ib = RATE_ORDER.index(b)
        out[ia], out[ib] = v[ib], v[ia]
    return out


def test_pure_metric_action_is_exchange_symmetric_on_proportional_background():
    bg = _proportional_background()
    state = np.array([0.13, -0.08, 0.021, -0.017, 0.032, -0.026, 0.011, -0.014])
    rates = np.array([0.041, -0.037, 0.016, -0.012])

    lhs = pure_metric_lagrangian_healthy(bg, state, rates)
    rhs = pure_metric_lagrangian_healthy(bg, _swap_metrics(state), _swap_rates(rates))
    assert math.isclose(lhs, rhs, rel_tol=2e-12, abs_tol=2e-12)


def test_auxiliary_lapses_and_shifts_have_no_velocity_slots():
    bg = _proportional_background()
    H = velocity_hessian(bg)

    # Only Psi1,Psi2,E1,E2 have rate slots. Lapses/shifts are algebraic by construction.
    assert RATE_ORDER == ("Psi1_dot", "Psi2_dot", "E1_dot", "E2_dot")
    assert H.shape == (4, 4)
    assert np.all(np.isfinite(H))
    assert np.allclose(H, H.T, rtol=1e-13, atol=1e-13)


def test_pure_metric_action_is_quadratic():
    bg = _proportional_background()
    state = np.array([0.09, -0.05, 0.018, 0.006, -0.021, 0.027, 0.012, -0.008])
    rates = np.array([0.031, -0.024, 0.014, -0.009])
    l1 = pure_metric_lagrangian_healthy(bg, state, rates)
    l2 = pure_metric_lagrangian_healthy(bg, 2.0*state, 2.0*rates)
    assert math.isclose(l2, 4.0*l1, rel_tol=2e-12, abs_tol=2e-12)
