import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.bigravity_scalar_action import (
    RAW_FIELD_ORDER,
    raw_kinetic_hessian,
    shift_interaction_lagrangian,
)
from numerics.lagos_bridge import LagosBackground


def _bg():
    return LagosBackground(
        a=0.7,
        b=0.91,
        Nbar=1.17,
        r=1.3,
        H=1.4,
        Hb=1.05,
        M1sq=1.0,
        M2sq=0.25,
        nu2=4.0,
        Z=0.62,
        Ztilde=0.81,
    )


def test_lagos_shift_terms_form_one_relative_shift_square():
    bg = _bg()
    k = 2.3
    B1, B2 = 0.17, -0.09
    measured = shift_interaction_lagrangian(bg, k=k, B1=B1, B2=B2)
    expected = (
        bg.a**3 * bg.M1sq * bg.Z * k**2
        / (2.0 * (bg.Nbar + bg.r))
        * (bg.r * B1 - bg.Nbar * B2) ** 2
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_raw_lagos_action_has_no_lapse_or_shift_velocities():
    bg = _bg()
    K = raw_kinetic_hessian(bg, k=2.3)
    assert K.shape == (8, 8)
    assert np.allclose(K, K.T)

    for name in ("Phi1", "B1", "Phi2", "B2"):
        i = RAW_FIELD_ORDER.index(name)
        assert np.allclose(K[i, :], 0.0)
        assert np.allclose(K[:, i], 0.0)

    # Both Einstein-Hilbert sectors retain metric kinetic structure before
    # the auxiliary and gauge reductions.
    for name in ("Psi1", "E1", "Psi2", "E2"):
        i = RAW_FIELD_ORDER.index(name)
        assert np.linalg.norm(K[i, :]) > 0.0
