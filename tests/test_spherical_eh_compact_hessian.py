import numpy as np


def test_minkowski_compact_eh_has_zero_linear_term_and_symmetric_hessian():
    from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives
    out=compact_eh_amplitude_derivatives(
        a0=1.0, conformal_H=0.0, w=0.0,
        time_radius=1.0, radial_radius=1.0,
        amplitude_step=2e-4, quadrature_order=28,
    )
    assert np.linalg.norm(out.gradient) < 3e-7
    assert np.all(np.isfinite(out.hessian))
    assert np.allclose(out.hessian,out.hessian.T,rtol=0,atol=3e-10)


def test_compact_eh_hessian_is_quadrature_stable():
    from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives
    a=compact_eh_amplitude_derivatives(a0=1.0,conformal_H=0.0,w=0.0,
        time_radius=1.0,radial_radius=1.0,amplitude_step=2e-4,quadrature_order=24)
    b=compact_eh_amplitude_derivatives(a0=1.0,conformal_H=0.0,w=0.0,
        time_radius=1.0,radial_radius=1.0,amplitude_step=2e-4,quadrature_order=32)
    scale=max(1.0,np.linalg.norm(b.hessian))
    assert np.linalg.norm(a.hessian-b.hessian)/scale < 3e-6


def test_taylor_background_compact_eh_matches_constant_w_on_small_support():
    from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives, compact_eh_amplitude_derivatives_taylor
    a0=1.0; H=0.04; w=0.0; p=2.0
    ap0=a0*H
    app0=a0*H*H*(1.0-1.0/p)
    exact=compact_eh_amplitude_derivatives(a0=a0,conformal_H=H,w=w,
        time_radius=.08,radial_radius=.5,amplitude_step=4e-4,quadrature_order=20)
    approx=compact_eh_amplitude_derivatives_taylor(a0=a0,ap0=ap0,app0=app0,
        time_radius=.08,radial_radius=.5,amplitude_step=4e-4,quadrature_order=20)
    scale=max(1.0,np.linalg.norm(exact.hessian))
    assert np.linalg.norm(approx.hessian-exact.hessian)/scale < 3e-5
