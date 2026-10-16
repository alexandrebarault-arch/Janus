import numpy as np


def _controls():
    return (
        dict(
            betas=(0.0, 1.0, -4.2383993109, 13.6801214252, 0.0),
            K=1.0, w=0.0, mu=-0.669234418875108,
            conformal_H=0.04, time_radius=0.7, radial_radius=0.8,
            amplitude_step=7e-4, quadrature_order=10,
        ),
        dict(
            betas=(0.0, 1.0, -1.7, 0.8, 0.0),
            K=0.63, w=0.0, mu=-0.31,
            conformal_H=0.025, time_radius=0.5, radial_radius=0.65,
            amplitude_step=7e-4, quadrature_order=10,
        ),
    )


def test_shared_native_hr_primitive_reproduces_historical_aoki_sixfield_hessian():
    from numerics.aoki_compact_sixfield_action import compact_hr_six_field_hessian
    from numerics.aoki_compact_sixfield_native import compact_native_hr_six_field_hessian

    for kwargs in _controls():
        old = compact_hr_six_field_hessian(**kwargs)
        new = compact_native_hr_six_field_hessian(**kwargs)
        assert np.allclose(new.gradient, old.gradient, rtol=0.0, atol=3e-10)
        assert np.allclose(new.hessian, old.hessian, rtol=0.0, atol=8e-8)
