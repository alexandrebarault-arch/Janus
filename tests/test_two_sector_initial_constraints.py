import numpy as np
from numerics.two_sector_initial_constraints import (
    Interaction,
    MatterProfile,
    solve_constraints,
)


def test_vacuum_minkowski_is_exact_solution():
    result = solve_constraints(
        interaction=Interaction.symmetric(beta1=1.0, beta2=0.0, beta3=1.0, mass2=0.02),
        g_profile=MatterProfile.zero(),
        f_profile=MatterProfile.zero(),
        r_max=15.0,
    )
    assert result.success
    assert np.max(np.abs(result.psi_g - 1.0)) < 2e-7
    assert np.max(np.abs(result.psi_f - 1.0)) < 2e-7


def test_segregated_core_shell_initial_data_is_regular():
    result = solve_constraints(
        interaction=Interaction.symmetric(beta1=1.0, beta2=0.0, beta3=1.0, mass2=0.02),
        g_profile=MatterProfile.gaussian_shell(amplitude=0.08, radius=5.0, width=0.8),
        f_profile=MatterProfile.gaussian_core(amplitude=0.08, width=1.5),
        r_max=20.0,
    )
    assert result.success
    assert result.psi_g.min() > 0.0
    assert result.psi_f.min() > 0.0
    assert abs(result.psi_g[-1] - 1.0) < 2e-6
    assert abs(result.psi_f[-1] - 1.0) < 2e-6
    assert result.max_constraint_residual < 2e-5


def test_symmetric_theory_swaps_when_matter_sectors_swap():
    interaction = Interaction.symmetric(beta1=1.0, beta2=0.0, beta3=1.0, mass2=0.02)
    shell = MatterProfile.gaussian_shell(amplitude=0.05, radius=4.0, width=0.7)
    core = MatterProfile.gaussian_core(amplitude=0.07, width=1.3)

    gf = solve_constraints(interaction=interaction, g_profile=shell, f_profile=core, r_max=18.0)
    fg = solve_constraints(interaction=interaction, g_profile=core, f_profile=shell, r_max=18.0)

    assert gf.success and fg.success
    assert np.max(np.abs(gf.psi_g - fg.psi_f)) < 2e-5
    assert np.max(np.abs(gf.psi_f - fg.psi_g)) < 2e-5
