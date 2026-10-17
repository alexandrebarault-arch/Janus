"""Spherical radial profile projection for finite-mu HR interaction."""
import numpy as np
import pytest
from numerics.hr_stueckelberg_profile_pullback import (
    spherical_bessel_j0_with_radial_derivative,
    regular_profile_to_native_jet,
    project_hr_native_profile,
)
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet

def test_regular_bessel_profile_and_derivative():
    k=2.3
    assert spherical_bessel_j0_with_radial_derivative(k,0)==(1.,0.)
    for r in (.0002,.06,.7):
        v,d=spherical_bessel_j0_with_radial_derivative(k,r)
        h=1e-6
        vp=spherical_bessel_j0_with_radial_derivative(k,r+h)[0]
        vm=spherical_bessel_j0_with_radial_derivative(k,r-h)[0]
        assert abs((vp-vm)/(2*h)-d)<2e-8

def test_profile_map_is_derivative_compatible():
    r=.18;f,fp=spherical_bessel_j0_with_radial_derivative(2.3,r)
    P=regular_profile_to_native_jet(r=r,profile=f,profile_r=fp)
    assert P.shape==(14,12)
    x=np.zeros(12);x[8:12]=[.12,-.23,.34,.45]
    j=P@x
    assert j[8]==pytest.approx(f*.12)
    assert j[9]==pytest.approx(f*.34)
    assert j[10]==pytest.approx(fp*.12)
    assert j[11]==pytest.approx(r*f*.45)
    assert j[12]==pytest.approx((f+r*fp)*(-.23))
    assert j[13]==pytest.approx(f*(-.23))
    np.testing.assert_array_equal(P[:8,:8],np.eye(8))

def test_center_regular_dilation():
    P=regular_profile_to_native_jet(r=0,profile=1,profile_r=0)
    assert P[10,8]==0 and P[11,11]==0
    assert P[12,9]==1 and P[13,9]==1 and P[9,10]==1

def test_exact_quadratic_form_under_chart_profile_projection():
    p=dict(N=1.,a=.8,n=1.16,alpha=.9,k=2.3,m2=.7,Mg2=1.3,
           betas=(.2,1.,-.5,.24,.31),mu=-.42,r=.11,
           sigma_r=-.72,sigma_dot=.19,mu_dot=.13,
           n_dot=.34,alpha_dot=-.17,n_ddot=.25,alpha_ddot=-.08)
    source=native_hr_stueckelberg_jet(**p)
    out=project_hr_native_profile(source,r=p['r'],k=p['k'])
    assert out.hessian.shape==(12,12)
    np.testing.assert_allclose(out.hessian,out.hessian.T,atol=1e-13)
    z=np.array([.2,-.4,.03,.11,-.1,.2,.13,-.09,.05,-.02,.03,.04])
    x=out.jacobian@z
    lhs=.5*z@out.hessian@z+out.gradient@z
    rhs=.5*x@source.hessian@x+source.gradient@x
    assert lhs==pytest.approx(rhs,abs=4e-12)

def test_zero_wave_and_invalid_radius():
    assert spherical_bessel_j0_with_radial_derivative(0,1.2)==(1.,0.)
    with pytest.raises(ValueError):
        regular_profile_to_native_jet(r=-.3,profile=1.,profile_r=0.)
