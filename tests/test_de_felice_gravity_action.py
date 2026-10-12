import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.lagos_scalar_action import einstein_hilbert_lagrangian


def _background(a=0.73, k=2.4, H_phys=0.91):
    return ScalarBackground(
        a=a, m2=1.0, f1=0.8, f2=0.9,
        H=H_phys * a, H_omega=H_phys * a * 0.87,
        c=0.87, xi=1.2, kappa=0.6, k2=k*k, G8pi=1.0,
    )


def _df_value(**overrides):
    kwargs = dict(
        lapse=1.0, scale_factor=0.68, H=0.83, Hdot_over_lapse=-0.21,
        k=2.7, Phi=0.0, B=0.0, psi=0.0, E=0.0,
        psi_dot=0.0, E_dot=0.0,
    )
    kwargs.update(overrides)
    return eh_scalar_quadratic_density_flat(**kwargs)


def _mixed(name1, name2):
    return (
        _df_value(**{name1:1.0,name2:1.0})
        - _df_value(**{name1:1.0})
        - _df_value(**{name2:1.0})
        + _df_value()
    )


def test_de_felice_eh_velocity_block_matches_lagos_after_variable_bridge():
    a = 0.73
    k = 2.4
    H_phys = 0.91
    bg = _background(a=a, k=k, H_phys=H_phys)

    psi_l_dot = 0.041
    e_l_dot = 0.016
    lagos = einstein_hilbert_lagrangian(
        bg,
        np.zeros(8),
        np.array([psi_l_dot, 0.0, e_l_dot, 0.0]),
    )

    psi_df_dot = -psi_l_dot - k*k*e_l_dot/3.0
    e_df_dot = 2.0*e_l_dot
    df_density = eh_scalar_quadratic_density_flat(
        lapse=1.0, scale_factor=a, H=H_phys, Hdot_over_lapse=0.0,
        k=k, Phi=0.0, B=0.0, psi=0.0, E=0.0,
        psi_dot=psi_df_dot, E_dot=e_df_dot,
    )
    assert math.isclose(lagos, 0.5*df_density, rel_tol=2e-13, abs_tol=2e-13)


def test_eq44_shift_Edot_contraction_has_negative_fourier_sign():
    a = 0.68
    k = 2.7
    expected = -(2.0/3.0)*k**4/a
    assert math.isclose(_mixed("B","E_dot"), expected, rel_tol=2e-13, abs_tol=2e-13)


def test_eq44_spatial_Phi_E_and_psi_E_contractions_have_positive_sign():
    a = 0.68
    k = 2.7
    expected = +(2.0/3.0)*k**4/a**2
    assert math.isclose(_mixed("Phi","E"), expected, rel_tol=2e-13, abs_tol=2e-13)
    assert math.isclose(_mixed("psi","E"), expected, rel_tol=2e-13, abs_tol=2e-13)


def test_eq44_lapse_trace_velocity_contraction_is_twelve_H_Phi_psidot():
    H = 0.83
    assert math.isclose(_mixed("Phi","psi_dot"), 12.0*H, rel_tol=2e-13, abs_tol=2e-13)


def test_de_felice_eh_scalar_density_is_quadratic():
    kwargs = dict(
        lapse=1.17, scale_factor=0.81, H=0.74, Hdot_over_lapse=-0.23,
        k=2.6, Phi=0.09, B=-0.04, psi=0.031, E=-0.012,
        psi_dot=0.027, E_dot=-0.008,
    )
    L1 = eh_scalar_quadratic_density_flat(**kwargs)
    doubled = dict(kwargs)
    for name in ("Phi", "B", "psi", "E", "psi_dot", "E_dot"):
        doubled[name] *= 2.0
    L2 = eh_scalar_quadratic_density_flat(**doubled)
    assert math.isclose(L2, 4.0*L1, rel_tol=2e-13, abs_tol=2e-13)
