import math
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from numerics.comelli_dae import ScalarBackground
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.lagos_scalar_action import einstein_hilbert_lagrangian


def test_de_felice_eh_velocity_block_matches_lagos_after_variable_bridge():
    a = 0.73
    k = 2.4
    H_phys = 0.91
    bg = ScalarBackground(
        a=a, m2=1.0, f1=0.8, f2=0.9,
        H=H_phys * a, H_omega=H_phys * a * 0.87,
        c=0.87, xi=1.2, kappa=0.6, k2=k*k, G8pi=1.0,
    )

    # Lagos rates for metric 1.
    psi_l_dot = 0.041
    e_l_dot = 0.016
    lagos = einstein_hilbert_lagrangian(
        bg,
        np.zeros(8),
        np.array([psi_l_dot, 0.0, e_l_dot, 0.0]),
    )

    # De Felice scalar variables: E_DF=2 E_L and
    # psi_DF=-Psi_L-k^2 E_L/3.  With all fields zero only rates remain.
    psi_df_dot = -psi_l_dot - k*k*e_l_dot/3.0
    e_df_dot = 2.0*e_l_dot
    df_density = eh_scalar_quadratic_density_flat(
        lapse=1.0,
        scale_factor=a,
        H=H_phys,
        Hdot_over_lapse=0.0,
        k=k,
        Phi=0.0,
        B=0.0,
        psi=0.0,
        E=0.0,
        psi_dot=psi_df_dot,
        E_dot=e_df_dot,
    )

    # IEH=(Mg^2/2) int N a^3 L_EH. Lagos helper returns the full
    # Mg^2 a^3-normalized sector, hence the comparison is N*L_EH/2.
    assert math.isclose(lagos, 0.5*df_density, rel_tol=2e-13, abs_tol=2e-13)


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
