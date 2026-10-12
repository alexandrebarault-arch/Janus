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


def test_lagos_shift_terms_form_source_normalized_relative_shift_square():
    bg = _bg()
    k = 2.3
    B1, B2 = 0.17, -0.09
    measured = shift_interaction_lagrangian(bg, k=k, B1=B1, B2=B2)
    # Lagos raises spatial indices with the background metric of each sector.
    # Combining the B1^2, B2^2 and B1 B2 terms of Eqs. (3.6)-(3.8) therefore
    # gives this comoving-k normalization.
    expected = (
        bg.a * bg.M1sq * bg.Z * k**2
        / (2.0 * (bg.Nbar + bg.r))
        * (bg.r * B1 - (bg.Nbar / bg.r) * B2) ** 2
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_raw_lagos_action_has_no_lapse_or_shift_velocities():
    bg = _bg()
    k = 2.3
    K = raw_kinetic_hessian(bg, k=k)
    assert K.shape == (8, 8)
    assert np.allclose(K, K.T)

    for name in ("Phi1", "B1", "Phi2", "B2"):
        i = RAW_FIELD_ORDER.index(name)
        assert np.allclose(K[i, :], 0.0)
        assert np.allclose(K[:, i], 0.0)

    for name in ("Psi1", "E1", "Psi2", "E2"):
        i = RAW_FIELD_ORDER.index(name)
        assert np.linalg.norm(K[i, :]) > 0.0

    # Eqs. (3.6)-(3.7) contain 2 a^2 partial^2 Edot_1 Psidot_1 and
    # 2 b^2/Nbar^2 partial^2 Edot_2 Psidot_2.  Since partial^2_A gives
    # -k^2/a_A^2 on a comoving Fourier mode, the scale factors cancel.
    p1 = RAW_FIELD_ORDER.index("Psi1")
    e1 = RAW_FIELD_ORDER.index("E1")
    p2 = RAW_FIELD_ORDER.index("Psi2")
    e2 = RAW_FIELD_ORDER.index("E2")
    assert math.isclose(K[p1, e1], -2.0 * k**2 * bg.a**3 * bg.M1sq)
    assert math.isclose(
        K[p2, e2],
        -2.0 * k**2 / bg.Nbar**2 * (bg.Nbar * bg.b**3 * bg.M2sq),
    )
