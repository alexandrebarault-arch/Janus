import numpy as np


def _integrals(T,R,n=80):
    xt,wt=np.polynomial.legendre.leggauss(n); xr,wr=np.polynomial.legendre.leggauss(n)
    t=T*xt; r=.5*R*(xr+1); W=(T*wt)[:,None]*(.5*R*wr)[None,:]
    x=t[:,None]/T; A=(1-x*x)**3; At=(-6*x*(1-x*x)**2)/T
    rr=r[None,:]; F=rr**2-3*rr**4/R**2+3*rr**6/R**4-rr**8/R**6
    Fr=2*rr-12*rr**3/R**2+18*rr**5/R**4-8*rr**7/R**6
    return float(np.sum(W*rr**2*(At*F)**2)),float(np.sum(W*rr**2*(A*Fr)**2))


def test_fixed_minkowski_kessence_q_hessian_has_requested_sound_speed():
    from numerics.spherical_kessence_compact_action import compact_kessence_hessian
    rho=1.7; pressure=.2; cs2=.3; T=.4; R=.7
    out=compact_kessence_hessian(a0=1.0,ap0=0.0,app0=0.0,
        rho=rho,pressure=pressure,cs2=cs2,time_radius=T,radial_radius=R,
        amplitude_step=2e-4,quadrature_order=24)
    ik,ig=_integrals(T,R)
    A=rho+pressure
    expected=(A/cs2)*ik-A*ig
    assert np.isclose(out.hessian[0,0],expected,rtol=2e-5,atol=1e-12)
