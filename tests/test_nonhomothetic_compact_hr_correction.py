import numpy as np

BASE=dict(
    betas=(0.0,1.0,-4.2383993109,13.6801214252,-38.5117901844),
    a=0.8,n=0.9,alpha=0.7,
    n_dot_over_n=-0.08,n_ddot_over_n=0.012,
    alpha_dot_over_alpha=0.04,alpha_ddot_over_alpha=-0.006,
    time_radius=0.12,radial_radius=0.5,quadrature_order=18,
    amplitude_step=5e-4,
)

def test_compact_relative_hr_correction_vanishes_identically_at_mu_zero():
    from numerics.nonhomothetic_compact_hr_correction import compact_relative_hr_correction_hessian
    out=compact_relative_hr_correction_hessian(mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,**BASE)
    assert np.linalg.norm(out.gradient,ord=np.inf) < 1e-12
    assert np.linalg.norm(out.hessian,ord=np.inf) < 1e-10


def test_compact_relative_hr_correction_is_finite_symmetric_and_nonzero_at_finite_mu():
    from numerics.nonhomothetic_compact_hr_correction import compact_relative_hr_correction_hessian
    out=compact_relative_hr_correction_hessian(mu=-0.55,mu_dot=0.03,s=-0.025,s_dot=0.004,**BASE)
    assert out.hessian.shape==(6,6)
    assert np.all(np.isfinite(out.hessian))
    assert np.allclose(out.hessian,out.hessian.T,rtol=0,atol=1e-11)
    assert np.linalg.norm(out.hessian,ord=np.inf) > 1e-5
    assert np.all(np.isfinite(out.gradient))


def test_small_mu_compact_hessian_has_regular_linear_limit():
    from numerics.nonhomothetic_compact_hr_correction import compact_relative_hr_correction_hessian
    norms=[]
    for mu in (-1e-2,-3e-3,-1e-3):
        out=compact_relative_hr_correction_hessian(mu=mu,mu_dot=0.0,s=0.0,s_dot=0.0,**BASE)
        norms.append(np.linalg.norm(out.hessian,ord=np.inf)/abs(mu))
    assert max(norms)/min(norms) < 1.01


def test_finite_mu_compact_hessian_is_stable_under_amplitude_step_refinement():
    from numerics.nonhomothetic_compact_hr_correction import compact_relative_hr_correction_hessian
    kw=dict(BASE); kw.pop('amplitude_step')
    a=compact_relative_hr_correction_hessian(mu=-0.55,mu_dot=0.03,s=-0.025,s_dot=0.004,amplitude_step=8e-4,**kw).hessian
    b=compact_relative_hr_correction_hessian(mu=-0.55,mu_dot=0.03,s=-0.025,s_dot=0.004,amplitude_step=4e-4,**kw).hessian
    assert np.linalg.norm(a-b,ord=np.inf) < 5e-7*max(1.0,np.linalg.norm(b,ord=np.inf))
