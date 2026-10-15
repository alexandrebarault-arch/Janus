import numpy as np


def _jet():
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    return from_log_derivatives(a=1.0,Hc=0.06,Hc_N=-0.03,
        xi=1.2,xi_N=-0.015,xi_NN=0.002,c=0.83,c_N=0.01)


def test_zero_interaction_mass_removes_stueckelberg_block_after_metric_schur():
    from numerics.nonhomothetic_compact_metric_schur import reduce_nonhomothetic_compact_metric_block
    out=reduce_nonhomothetic_compact_metric_block(
        betas=(0,1,-0.7,0.35,0),jet=_jet(),mu=-0.3,mu_p=0.01,mu_pp=-0.001,
        time_radius=.03,radial_radius=.35,interaction_mass2=0.0,planck_ratio=.2,
        amplitude_step=8e-4,quadrature_order=14)
    assert np.linalg.norm(out.reduced_stueckelberg_hessian) < 1e-14
    assert np.linalg.norm(out.reduced_stueckelberg_gradient) < 1e-14
    assert out.metric_rank == 4


def test_nonhomothetic_metric_schur_is_symmetric_and_finite():
    from numerics.nonhomothetic_compact_metric_schur import reduce_nonhomothetic_compact_metric_block
    out=reduce_nonhomothetic_compact_metric_block(
        betas=(0,1,-0.7,0.35,0),jet=_jet(),mu=-0.3,mu_p=0.01,mu_pp=-0.001,
        time_radius=.03,radial_radius=.35,interaction_mass2=3e-3,planck_ratio=.2,
        amplitude_step=8e-4,quadrature_order=14)
    assert np.all(np.isfinite(out.reduced_stueckelberg_hessian))
    assert np.allclose(out.reduced_stueckelberg_hessian,out.reduced_stueckelberg_hessian.T,atol=1e-12,rtol=0)
    assert out.metric_rank == 4
    assert np.isfinite(out.metric_condition_number)


def test_metric_rank_does_not_depend_on_absolute_compact_action_scale():
    from numerics.nonhomothetic_compact_metric_schur import reduce_nonhomothetic_compact_metric_block
    from numerics.nonhomothetic_background_jet import from_log_derivatives
    jet=from_log_derivatives(a=.5,Hc=0.9011914176813176,Hc_N=-0.16696497542872346,
        xi=0.5682425082862556,xi_N=-0.03575119249023922,xi_NN=0.08843149708626062,
        c=0.937084621497149,c_N=0.15166446723375743)
    out=reduce_nonhomothetic_compact_metric_block(
        betas=(0,1,-4.2383993109,13.6801214252,-38.5117901844),
        jet=jet,mu=0.0,mu_p=0.0,mu_pp=0.0,
        time_radius=.03,radial_radius=.10,interaction_mass2=23.3348939346,
        planck_ratio=0.011836458045964914,amplitude_step=0.0015,quadrature_order=14)
    assert out.metric_rank == 4
    assert out.metric_condition_number < 1e5
