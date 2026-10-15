import numpy as np


def _kwargs(mg2, mf2):
    return dict(
        betas=(0.0, 1.0, -4.2383993109, 13.6801214252, 0.0),
        a_g=1.0,
        a_g_prime=0.05,
        a_f=1.0,
        a_f_prime=0.05,
        conformal_H=0.05,
        conformal_H_prime=-0.5*0.05**2,
        radius=1.0,
        mu=-0.669234418875108,
        omega=20.0,
        k=10.0,
        delta_eta=1.0 + 0.0j,
        delta_r=0.0 + 0.0j,
        mass_g2=mg2,
        mass_f2=mf2,
        source_step=2e-6,
    )


def test_zero_interaction_mass_gives_zero_weak_metric_potentials():
    from numerics.aoki_homothetic_weak_constraints import solve_weak_metric_constraints
    out = solve_weak_metric_constraints(**_kwargs(0.0, 0.0))
    assert np.linalg.norm(out.potentials) < 1e-14
    assert out.relative_residual < 1e-12


def test_weak_metric_potentials_scale_linearly_with_small_common_mass():
    from numerics.aoki_homothetic_weak_constraints import solve_weak_metric_constraints
    norms = []
    masses = (1e-4, 3e-4, 1e-3)
    for m in masses:
        out = solve_weak_metric_constraints(**_kwargs(m, m))
        norms.append(np.linalg.norm(out.potentials))
        assert out.relative_residual < 1e-10
        assert np.isfinite(out.condition_number)
    scaled = np.asarray(norms) / np.asarray(masses)
    assert np.max(scaled) / np.min(scaled) < 1.01


def test_solved_potentials_cancel_all_four_native_tt_tr_constraints():
    from numerics.aoki_homothetic_weak_constraints import solve_weak_metric_constraints
    out = solve_weak_metric_constraints(**_kwargs(2e-3, 7e-4))
    assert out.relative_residual < 1e-10
    assert np.linalg.norm(out.residual) < 1e-9 * max(1.0, np.linalg.norm(out.rhs))
    assert out.condition_number < 1e6
