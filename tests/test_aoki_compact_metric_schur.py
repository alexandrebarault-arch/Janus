import numpy as np


def _kwargs(mass2):
    return dict(
        betas=(0,1,-4.2383993109,13.6801214252,0), K=1.0, w=0.0,
        mu=-0.669234418875108, conformal_H=0.08,
        time_radius=0.55, radial_radius=0.7,
        interaction_mass2=mass2, planck_ratio=1.0,
        amplitude_step=7e-4, quadrature_order=16,
    )


def test_zero_interaction_mass_removes_pi_from_total_action():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(0.0))
    assert abs(out.total_hessian[0,0]) < 1e-12
    assert np.linalg.norm(out.total_hessian[0,1:]) < 1e-12
    assert abs(out.reduced_pi_hessian) < 1e-12


def test_small_mass_schur_tends_to_hr_only_pi_entry():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(2e-5))
    leading=-2e-5*out.hr_hessian[0,0]
    assert abs(leading) > 1e-10
    assert abs(out.reduced_pi_hessian-leading)/abs(leading) < 2e-3
    assert np.isfinite(out.metric_condition_number)


def test_total_metric_block_is_symmetric():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block
    out=reduce_compact_metric_block(**_kwargs(3e-3))
    assert np.allclose(out.total_hessian,out.total_hessian.T,rtol=0,atol=2e-8)
    assert out.metric_rank == 4
