import numpy as np


def _kwargs(betas):
    return dict(betas=betas,K=1.0,w=0.0,mu=-0.669234418875108,
                conformal_H=0.04,time_radius=0.7,radial_radius=0.8,
                amplitude_step=7e-4,quadrature_order=16)


def test_zero_interaction_has_zero_five_field_hessian():
    from numerics.aoki_compact_metric_pi_action import compact_hr_five_field_hessian
    out=compact_hr_five_field_hessian(**_kwargs((0,0,0,0,0)))
    assert np.linalg.norm(out.hessian) < 1e-12


def test_compact_hr_five_field_hessian_is_symmetric_and_finite():
    from numerics.aoki_compact_metric_pi_action import compact_hr_five_field_hessian
    out=compact_hr_five_field_hessian(**_kwargs((0,1,-4.2383993109,13.6801214252,0)))
    assert out.hessian.shape == (5,5)
    assert np.all(np.isfinite(out.hessian))
    assert np.allclose(out.hessian,out.hessian.T,rtol=0,atol=2e-8)
    assert abs(out.hessian[0,0]) > 1e-8


def test_pi_pi_entry_is_quadrature_stable():
    from numerics.aoki_compact_metric_pi_action import compact_hr_five_field_hessian
    a=compact_hr_five_field_hessian(**_kwargs((0,1,-4.2383993109,13.6801214252,0)))
    kw=_kwargs((0,1,-4.2383993109,13.6801214252,0)); kw['quadrature_order']=20
    b=compact_hr_five_field_hessian(**kw)
    scale=max(1.0,abs(b.hessian[0,0]))
    assert abs(a.hessian[0,0]-b.hessian[0,0])/scale < 2e-4
