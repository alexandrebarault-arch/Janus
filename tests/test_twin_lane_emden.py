import numpy as np

from numerics.twin_lane_emden import (
    BetaPotential,
    compact_core,
    compact_shell,
    solve_initial_data,
)


def test_biminkowski_vacuum_is_exact_control():
    beta = BetaPotential.from_b123(beta1=0.02, beta2=-0.005, beta3=0.002)
    sol = solve_initial_data(
        beta=beta,
        density_g=lambda r: np.zeros_like(r),
        density_f=lambda r: np.zeros_like(r),
        r_max=20.0,
    )
    assert sol.success
    assert np.max(np.abs(sol.psi_g - 1.0)) < 1e-8
    assert np.max(np.abs(sol.psi_f - 1.0)) < 1e-8


def test_visible_shell_plus_twin_core_has_regular_positive_initial_data():
    beta = BetaPotential.from_b123(beta1=0.02, beta2=-0.005, beta3=0.002)
    sol = solve_initial_data(
        beta=beta,
        density_g=lambda r: compact_shell(r, amplitude=2e-3, radius=5.0, width=1.2),
        density_f=lambda r: compact_core(r, amplitude=2e-3, width=1.8),
        r_max=20.0,
    )
    assert sol.success
    assert np.all(np.isfinite(sol.psi_g))
    assert np.all(np.isfinite(sol.psi_f))
    assert np.min(sol.psi_g) > 0.0
    assert np.min(sol.psi_f) > 0.0
    assert np.max(np.abs(sol.constraint_g)) < 2e-5
    assert np.max(np.abs(sol.constraint_f)) < 2e-5


def test_g_f_exchange_symmetry_of_initial_constraints():
    beta = BetaPotential.from_b123(beta1=0.018, beta2=-0.004, beta3=0.003)
    dg = lambda r: compact_shell(r, amplitude=1.5e-3, radius=4.5, width=1.0)
    df = lambda r: compact_core(r, amplitude=2.2e-3, width=1.6)

    original = solve_initial_data(
        beta=beta,
        density_g=dg,
        density_f=df,
        kappa_g=1.2,
        kappa_f=0.8,
        r_max=18.0,
    )
    swapped = solve_initial_data(
        beta=beta.exchanged(),
        density_g=df,
        density_f=dg,
        kappa_g=0.8,
        kappa_f=1.2,
        r_max=18.0,
    )
    assert original.success and swapped.success
    assert np.max(np.abs(original.psi_g - swapped.psi_f)) < 2e-5
    assert np.max(np.abs(original.psi_f - swapped.psi_g)) < 2e-5
