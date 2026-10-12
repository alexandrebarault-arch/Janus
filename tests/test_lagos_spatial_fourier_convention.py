import numpy as np
import pytest

from numerics.comelli_dae import ScalarBackground
from numerics.lagos_scalar_action import (
    einstein_hilbert_lagrangian,
    interaction_lagrangian_healthy,
)


def _vacuum_bg(*, a=2.0, xi=3.0, c=1.25, k2=9.0):
    return ScalarBackground(
        a=a,
        m2=0.0,
        f1=0.0,
        f2=0.0,
        H=0.0,
        H_omega=0.0,
        c=c,
        xi=xi,
        kappa=1.0,
        k2=k2,
    )


def test_g_sector_spatial_laplacian_uses_comoving_k_over_a():
    bg = _vacuum_bg(a=2.0, k2=9.0)
    state = np.zeros(8)
    state[0] = 1.0  # Psi1
    got = einstein_hilbert_lagrangian(bg, state, np.zeros(4))
    assert got == pytest.approx(bg.k2 / bg.a**2)


def test_g_sector_a2_laplacian_cancels_scale_factor_for_Edot():
    bg = _vacuum_bg(a=2.0, k2=9.0)
    state = np.zeros(8)
    mixed = einstein_hilbert_lagrangian(bg, state, [1.0, 0.0, 1.0, 0.0])
    psi_only = einstein_hilbert_lagrangian(bg, state, [1.0, 0.0, 0.0, 0.0])
    e_only = einstein_hilbert_lagrangian(bg, state, [0.0, 0.0, 1.0, 0.0])
    assert mixed - psi_only - e_only == pytest.approx(-2.0 * bg.k2)


def test_f_sector_spatial_laplacian_uses_comoving_k_over_b():
    bg = _vacuum_bg(a=2.0, xi=3.0, c=1.25, k2=9.0)
    state = np.zeros(8)
    state[1] = 1.0  # Psi2
    got = einstein_hilbert_lagrangian(bg, state, np.zeros(4))
    b = bg.a * bg.xi
    nbar = bg.xi * bg.c
    expected = nbar * bg.xi**3 * bg.kappa * bg.k2 / b**2
    assert got == pytest.approx(expected)


def test_g_interaction_shift_gradient_uses_comoving_k_over_a():
    # Choose Z=1 and Z_tilde=0.
    bg = ScalarBackground(
        a=2.0,
        m2=1.0,
        f1=0.0,
        f2=3.0,
        H=0.0,
        H_omega=0.0,
        c=1.25,
        xi=3.0,
        kappa=1.0,
        k2=9.0,
    )
    state = np.zeros(8)
    state[6] = 1.0  # B1
    got = interaction_lagrangian_healthy(bg, state)
    r = bg.xi
    nbar = r * bg.c
    expected = r*r/(2.0*(nbar+r)) * bg.k2/bg.a**2
    assert got == pytest.approx(expected)


def test_interaction_a2_laplacian_cancels_for_E1():
    # Choose Z=0 and Z_tilde=1.
    bg = ScalarBackground(
        a=2.0,
        m2=1.0,
        f1=3.0,
        f2=0.0,
        H=0.0,
        H_omega=0.0,
        c=1.25,
        xi=3.0,
        kappa=1.0,
        k2=9.0,
    )
    base = np.zeros(8)
    base[0] = 1.0  # Psi1
    with_e = base.copy()
    with_e[2] = 1.0  # E1
    delta = interaction_lagrangian_healthy(bg, with_e) - interaction_lagrangian_healthy(bg, base)
    expected = 2.0 * bg.xi * bg.k2
    assert delta == pytest.approx(expected)
