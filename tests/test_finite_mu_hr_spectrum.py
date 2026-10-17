import numpy as np
from numerics.finite_mu_hr_spectrum import spectral_potential


def test_spherical_elementary_polynomial_agrees_with_four_eigenvalues():
    for t,r,l in [(0.71,1.34,1.34),(2.1,.23,.54),(1.,1.,1.)]:
        b=np.array([.2,1.3,-.7,.8,-.11])
        U,_,_=spectral_potential(t,r,l,b)
        eig=np.array([t,r,l,l])
        e=np.array([1,sum(eig),
          sum(eig[i]*eig[j] for i in range(4) for j in range(i+1,4)),
          sum(eig[i]*eig[j]*eig[k] for i in range(4) for j in range(i+1,4) for k in range(j+1,4)),
          np.prod(eig)])
        assert np.isclose(U,b@e,rtol=2e-15,atol=1e-14)


def test_finite_mu_derivatives_agree_with_independent_differences():
    b=[.3,1.,-4.2383993109,13.6801214252,-38.5117901844]
    x=np.array([.41,.51,.67]); _,g,H=spectral_potential(*x,b)
    h=2e-5
    for j in range(3):
        shift=np.eye(3)[j]*h
        up,gp,_=spectral_potential(*(x+shift),b)
        um,gm,_=spectral_potential(*(x-shift),b)
        assert np.isclose(g[j],(up-um)/(2*h),rtol=1e-8,atol=1e-8)
        assert np.allclose(H[:,j],(gp-gm)/(2*h),rtol=2e-9,atol=3e-9)
    assert np.array_equal(H,H.T)


def test_spherical_limit_at_zero_and_finite_mu():
    b=[0,1,-4.2,13.68,-38.5]
    xi=.56;c=.94
    for mu in [0,-.77,-.95]:
        ell=xi*(1+mu)
        U,g,H=spectral_potential(xi*c,ell,ell,b)
        assert np.isfinite(U) and np.isfinite(g).all() and np.isfinite(H).all()
        assert np.isclose(g[1],g[2]/2)
