"""Physical-parity but still interaction-only compact radial Hessian controls."""
import math
import numpy as np
import pytest
from numerics.hr_compact_radial_interaction import (
    AMPLITUDES, compact_scalar_profile,compact_native_profile_map,
    integrate_compact_hr_interaction,
)
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet

P=dict(N=1.,a=.92,n=1.13,alpha=.84,k=2.2,m2=.7,Mg2=1.2,
       betas=(.31,1.,-.4,.2,.13),mu=-.25,
       sigma_r=-.11,sigma_dot=.15,mu_dot=.14,
       n_dot=.09,alpha_dot=-.07,n_ddot=.025,alpha_ddot=-.02)


def test_compact_scalar_profile_derivatives_and_center():
    R=.41
    assert compact_scalar_profile(0,R)==(1.,0.,-8/R**2,0.)
    assert compact_scalar_profile(R,R)==(0.,0.,0.,0.)
    assert compact_scalar_profile(2*R,R)==(0.,0.,0.,0.)
    for r in (.05,.19,.35):
        F,dF,d2F,tf=compact_scalar_profile(r,R)
        h=3e-6
        fd=(compact_scalar_profile(r+h,R)[0]-compact_scalar_profile(r-h,R)[0])/(2*h)
        fdd=(compact_scalar_profile(r+h,R)[1]-compact_scalar_profile(r-h,R)[1])/(2*h)
        assert dF==pytest.approx(fd,abs=2e-9)
        assert d2F==pytest.approx(fdd,abs=3e-8)
        assert tf==pytest.approx(d2F-dF/r,abs=3e-14)


def test_metric_parity_and_regular_center():
    R=.3;k=2.2
    P0=compact_native_profile_map(r=0,R=R,k=k)
    assert P0.shape==(14,12)
    for i in (1,3,5,7):
        assert P0[i,i]==0 # radial shift and traceless scalar shear
    assert P0[8,8]==1 and P0[9,10]==1
    assert P0[10,8]==0 and P0[11,11]==0
    assert P0[12,9]==P0[13,9]==1
    for r in (.012,.071,.16):
        F,Fp,Fpp,tf=compact_scalar_profile(r,R)
        B=compact_native_profile_map(r=r,R=R,k=k)
        assert B[1,1]==pytest.approx(Fp/k)
        assert B[3,3]==pytest.approx(-2*tf/k**2)
        assert B[11,11]==pytest.approx(r*F)
        assert B[12,9]==pytest.approx(F+r*Fp)


def test_compact_integral_order_convergence_and_symmetry():
    a=integrate_compact_hr_interaction(radius=.24,quadrature_order=16,**P)
    b=integrate_compact_hr_interaction(radius=.24,quadrature_order=26,**P)
    assert a.hessian.shape==(12,12) and len(AMPLITUDES)==12
    assert a.integration_volume==pytest.approx(4*math.pi*.24**3/3)
    np.testing.assert_allclose(a.hessian,a.hessian.T,rtol=0,atol=5e-14)
    np.testing.assert_allclose(a.hessian,b.hessian,rtol=2e-10,atol=2e-11)
    np.testing.assert_allclose(a.gradient,b.gradient,rtol=2e-10,atol=2e-11)
    assert a.value==pytest.approx(b.value,rel=2e-11)


def test_integral_is_sum_of_native_quadratic_forms():
    R=.23
    out=integrate_compact_hr_interaction(radius=R,quadrature_order=8,**P)
    x=np.array([.2,-.4,.03,.1,-.11,.19,.08,-.03,.02,-.04,.06,-.07])
    lhs=out.gradient@x+.5*x@out.hessian@x
    t,w=np.polynomial.legendre.leggauss(8)
    rhs=0.
    for i in range(8):
        r=.5*R*(t[i]+1)
        Pmap=compact_native_profile_map(r=r,R=R,k=P['k'])
        jet=native_hr_stueckelberg_jet(r=r,**P)
        y=Pmap@x
        rhs+=2*math.pi*R*w[i]*r*r*(jet.gradient@y+.5*y@jet.hessian@y)
    assert lhs==pytest.approx(rhs,rel=1e-12,abs=1e-12)


def test_beta0_and_beta4_sector_separation_after_integration():
    p0=dict(P,betas=(1.,0.,0.,0.,0.))
    p4=dict(P,betas=(0.,0.,0.,0.,1.))
    b0=integrate_compact_hr_interaction(radius=.23,quadrature_order=14,**p0)
    b4=integrate_compact_hr_interaction(radius=.23,quadrature_order=14,**p4)
    for j in list(range(4,8))+list(range(8,12)):
        assert np.max(np.abs(b0.hessian[j,:]))<1e-12
        assert abs(b0.gradient[j])<1e-12
    for j in range(4):
        assert np.max(np.abs(b4.hessian[j,:]))<1e-12
        assert abs(b4.gradient[j])<1e-12


def test_compact_input_guards():
    with pytest.raises(ValueError):compact_scalar_profile(-1,1)
    with pytest.raises(ValueError):compact_scalar_profile(0,0)
    with pytest.raises(ValueError):compact_native_profile_map(r=0,R=1,k=0)
    with pytest.raises(ValueError):integrate_compact_hr_interaction(radius=0,**P)
    with pytest.raises(ValueError):integrate_compact_hr_interaction(radius=1,quadrature_order=7,**P)
    with pytest.raises(ValueError):integrate_compact_hr_interaction(radius=1,**dict(P,r=.3))
