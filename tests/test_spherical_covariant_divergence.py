import numpy as np


def test_constant_identity_mixed_tensor_has_zero_divergence_for_generic_spherical_metric():
    from numerics.spherical_covariant_divergence import mixed_tensor_divergence
    g=np.array([[-2.0,0.3],[0.3,1.4]])
    dg=np.array([
        [[0.2,-0.1],[-0.1,0.05]],
        [[-0.03,0.07],[0.07,0.11]],
    ])
    q=3.2; dq=np.array([0.4,-0.2])
    c=1.7
    V=c*np.eye(2); dV=np.zeros((2,2,2))
    out=mixed_tensor_divergence(
        g_radial=g,dg_radial=dg,g_angular=q,dg_angular=dq,
        V_radial=V,dV_radial=dV,V_angular=c,
    )
    assert np.allclose(out,0.0,rtol=0,atol=2e-14)


def test_flrw_perfect_fluid_divergence_reduces_to_continuity_equation():
    from numerics.spherical_covariant_divergence import mixed_tensor_divergence
    a=1.3; Hc=0.27; r=0.8
    g=a*a*np.diag([-1.0,1.0])
    dg=np.zeros((2,2,2)); dg[0]=2*Hc*g
    q=a*a*r*r
    dq=np.array([2*Hc*q,2*a*a*r])
    rho=2.4; p=0.35
    rhop=-3*Hc*(rho+p)
    V=np.diag([-rho,p])
    dV=np.zeros((2,2,2)); dV[0,0,0]=-rhop
    out=mixed_tensor_divergence(
        g_radial=g,dg_radial=dg,g_angular=q,dg_angular=dq,
        V_radial=V,dV_radial=dV,V_angular=p,
    )
    assert abs(out[0])<2e-13
    assert abs(out[1])<2e-13
