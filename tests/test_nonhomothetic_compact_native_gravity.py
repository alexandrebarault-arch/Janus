import numpy as np

BASE=dict(
    betas=(0.0,1.0,-4.2383993109,13.6801214252,-38.5117901844),
    a=1.0,n=1.0,alpha=1.0,
    a_dot_over_a=0.05,a_ddot_over_a=-0.00125,
    n_dot_over_n=0.0,n_ddot_over_n=0.0,
    alpha_dot_over_alpha=0.05,alpha_ddot_over_alpha=-0.00125,
    mu=-0.55,mu_dot=0.0,s=0.039875,s_dot=0.000996875,
    time_radius=0.3,radial_radius=0.7,
    interaction_mass2=0.02,planck_ratio=1.0,
    amplitude_step=5e-4,quadrature_order=16,
)


def test_total_native_compact_hessian_is_symmetric_and_metric_block_invertible():
    from numerics.nonhomothetic_compact_native_gravity import compact_native_gravity_hessian
    out=compact_native_gravity_hessian(**BASE)
    assert out.hessian.shape==(6,6)
    assert np.all(np.isfinite(out.hessian))
    assert np.allclose(out.hessian,out.hessian.T,rtol=0,atol=1e-10)
    assert out.metric_rank==4
    assert np.isfinite(out.metric_condition_number)
    assert out.metric_condition_number < 1e12


def test_metric_schur_leaves_two_stueckelberg_amplitudes():
    from numerics.nonhomothetic_compact_native_gravity import reduce_compact_native_metric_block
    out=reduce_compact_native_metric_block(**BASE)
    assert out.reduced_hessian.shape==(2,2)
    assert np.all(np.isfinite(out.reduced_hessian))
    assert np.allclose(out.reduced_hessian,out.reduced_hessian.T,rtol=0,atol=1e-10)


def test_zero_interaction_mass_removes_stueckelberg_dynamics_after_metric_schur():
    from numerics.nonhomothetic_compact_native_gravity import reduce_compact_native_metric_block
    kw=dict(BASE); kw['interaction_mass2']=0.0
    out=reduce_compact_native_metric_block(**kw)
    assert np.linalg.norm(out.reduced_hessian,ord=np.inf) < 1e-9
