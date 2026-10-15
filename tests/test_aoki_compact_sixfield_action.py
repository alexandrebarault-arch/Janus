import numpy as np


def _kwargs():
    return dict(betas=(0,1,-4.2383993109,13.6801214252,0),K=1.0,w=0.0,
                mu=-0.669234418875108,conformal_H=0.04,time_radius=.7,radial_radius=.8,
                amplitude_step=7e-4,quadrature_order=14)


def test_sixfield_hr_projection_recovers_pi_fivefield_action():
    from numerics.aoki_compact_metric_pi_action import compact_hr_five_field_hessian
    from numerics.aoki_compact_sixfield_action import compact_hr_six_field_hessian
    five=compact_hr_five_field_hessian(**_kwargs())
    six=compact_hr_six_field_hessian(**_kwargs())
    v=np.array([1.,1.,0.,0.,0.,0.])
    assert np.isclose(v@six.hessian@v,five.hessian[0,0],rtol=0,atol=2e-7)
    assert np.isclose(v@six.gradient,five.gradient[0],rtol=0,atol=2e-9)
    assert np.allclose(six.hessian[2:,2:],five.hessian[1:,1:],rtol=0,atol=2e-7)


def test_sixfield_metric_schur_projection_recovers_pi_schur():
    from numerics.aoki_compact_metric_schur import reduce_compact_metric_block, reduce_compact_six_field_metric_block
    kw=_kwargs(); kw.update(interaction_mass2=2e-4,planck_ratio=1.0)
    five=reduce_compact_metric_block(**kw)
    six=reduce_compact_six_field_metric_block(**kw)
    v=np.array([1.,1.])
    assert np.isclose(v@six.reduced_stueckelberg_hessian@v,five.reduced_pi_hessian,rtol=0,atol=3e-7)
    assert np.isclose(v@six.reduced_stueckelberg_gradient,five.reduced_pi_gradient,rtol=0,atol=3e-9)
