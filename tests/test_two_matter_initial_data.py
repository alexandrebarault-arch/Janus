import numpy as np

from numerics.two_matter_initial_data import (
    Interaction,
    Profiles,
    residual_max,
    solve_initial_data,
)


def test_asymptotic_flat_beta_completion():
    p = Interaction.from_internal(
        beta1=1.0,
        beta2=-0.2,
        beta3=0.0,
        m2=0.02,
        kappa_g=1.0,
        kappa_f=1.0,
    )
    assert abs(p.beta0 + 3 * p.beta1 + 3 * p.beta2 + p.beta3) < 1e-14
    assert abs(p.beta1 + 3 * p.beta2 + 3 * p.beta3 + p.beta4) < 1e-14


def test_vacuum_is_exact_biminkowski():
    p = Interaction.from_internal(
        beta1=1.0,
        beta2=-0.2,
        beta3=0.0,
        m2=0.02,
        kappa_g=1.0,
        kappa_f=1.0,
    )
    sol = solve_initial_data(p, Profiles.zero(), r_max=20.0, n=250)
    assert sol.success
    assert np.max(np.abs(sol.psi_g - 1.0)) < 1e-7
    assert np.max(np.abs(sol.psi_f - 1.0)) < 1e-7
    assert residual_max(sol, p, Profiles.zero()) < 1e-6


def test_central_f_plus_g_shell_has_regular_positive_solution():
    p = Interaction.from_internal(
        beta1=1.0,
        beta2=-0.2,
        beta3=0.0,
        m2=0.02,
        kappa_g=1.0,
        kappa_f=1.0,
    )
    prof = Profiles.central_f_and_g_shell(
        f_amp=0.04,
        f_sigma=2.0,
        g_amp=0.025,
        g_radius=5.0,
        g_sigma=1.0,
    )
    sol = solve_initial_data(p, prof, r_max=25.0, n=400)
    assert sol.success, sol.message
    assert sol.psi_g.min() > 0.5
    assert sol.psi_f.min() > 0.5
    assert abs(sol.dpsi_g[0]) < 1e-7
    assert abs(sol.dpsi_f[0]) < 1e-7
    assert abs(sol.psi_g[-1] - 1.0) < 1e-7
    assert abs(sol.psi_f[-1] - 1.0) < 1e-7
    assert residual_max(sol, p, prof) < 5e-5
