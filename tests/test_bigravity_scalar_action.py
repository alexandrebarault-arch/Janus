import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.bigravity_scalar_action import (
    RAW_FIELD_ORDER,
    raw_kinetic_hessian,
    sector1_eh_velocity_lagrangian,
    sector2_eh_velocity_lagrangian,
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

    p1 = RAW_FIELD_ORDER.index("Psi1")
    e1 = RAW_FIELD_ORDER.index("E1")
    p2 = RAW_FIELD_ORDER.index("Psi2")
    e2 = RAW_FIELD_ORDER.index("E2")
    assert math.isclose(K[p1, e1], -2.0 * k**2 * bg.a**3 * bg.M1sq)
    assert math.isclose(
        K[p2, e2],
        -2.0 * k**2 / bg.Nbar**2 * (bg.Nbar * bg.b**3 * bg.M2sq),
    )


def test_sector1_eh_velocity_block_matches_lagos_eq_3_6():
    bg = _bg()
    k = 2.3
    Phi1 = 0.08
    B1 = -0.13
    Psi1_dot = 0.21
    E1_dot = -0.17
    measured = sector1_eh_velocity_lagrangian(
        bg, k=k, Phi1=Phi1, B1=B1,
        Psi1_dot=Psi1_dot, E1_dot=E1_dot,
    )
    expected = bg.a**3 * bg.M1sq * (
        -3.0 * Psi1_dot**2
        - 6.0 * bg.H * Psi1_dot * Phi1
        - 2.0 * k**2 * E1_dot * (Psi1_dot + bg.H * Phi1)
        + 2.0 * k**2 / bg.a**2 * Psi1_dot * B1
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_sector2_eh_velocity_block_matches_lagos_eq_3_7():
    bg = _bg()
    k = 2.3
    Phi2 = -0.06
    B2 = 0.11
    Psi2_dot = -0.19
    E2_dot = 0.14

    measured = sector2_eh_velocity_lagrangian(
        bg,
        k=k,
        Phi2=Phi2,
        B2=B2,
        Psi2_dot=Psi2_dot,
        E2_dot=E2_dot,
    )

    # Lagos Eq. (3.7), using partial_2^2 -> -k^2/b^2.
    expected = bg.Nbar * bg.b**3 * bg.M2sq * (
        -3.0 * Psi2_dot**2 / bg.Nbar**2
        - 6.0 * bg.Hb * Psi2_dot * Phi2 / bg.Nbar**2
        - 2.0 * k**2 * E2_dot * (Psi2_dot + bg.Hb * Phi2) / bg.Nbar**2
        + 2.0 * k**2 * Psi2_dot * B2 / (bg.Nbar * bg.b**2)
    )
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)
