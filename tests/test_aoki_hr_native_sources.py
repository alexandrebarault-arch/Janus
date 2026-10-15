import numpy as np


def test_native_hr_sources_reduce_to_direct_diagonal_tensor_for_identity_maps():
    from numerics.aoki_hr_native_sources import native_interaction_sources
    from numerics.nonhomothetic_hr_interaction_tensor import interaction_mixed_tensors
    betas=(0.2,1.0,-0.7,0.4,-0.3)
    t=0.73; x=1.31
    out=native_interaction_sources(
        g_radial_native=np.diag([-1.0,1.0]),
        f_radial_native=np.diag([-t*t,x*x]),
        g_angular_native=1.0,
        f_angular_native=x*x,
        jacobian_g=np.eye(2), jacobian_f=np.eye(2), betas=betas,
    )
    expected_g,expected_f=interaction_mixed_tensors(np.diag([t,x,x,x]),betas)
    assert np.allclose(out.g_native,expected_g,rtol=0,atol=3e-13)
    assert np.allclose(out.f_native,expected_f,rtol=0,atol=3e-13)


def test_native_sources_are_independent_of_common_radial_coordinate_chart():
    from numerics.aoki_hr_native_sources import native_interaction_sources
    betas=(0.0,1.1,-0.4,0.8,0.2)
    t=0.81; x=1.22
    g=np.diag([-1.0,1.0])
    f=np.diag([-t*t,x*x])
    identity=native_interaction_sources(
        g_radial_native=g, f_radial_native=f,
        g_angular_native=1.0, f_angular_native=x*x,
        jacobian_g=np.eye(2), jacobian_f=np.eye(2), betas=betas,
    )
    P=np.array([[1.03,0.17],[-0.08,0.94]])
    transformed=native_interaction_sources(
        g_radial_native=g, f_radial_native=f,
        g_angular_native=1.0, f_angular_native=x*x,
        jacobian_g=P, jacobian_f=P, betas=betas,
    )
    assert np.allclose(transformed.g_native,identity.g_native,rtol=3e-13,atol=3e-13)
    assert np.allclose(transformed.f_native,identity.f_native,rtol=3e-13,atol=3e-13)
