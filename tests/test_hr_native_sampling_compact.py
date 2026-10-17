"""Independent inverse-coordinate-Jacobian and integration controls."""
import numpy as np
import pytest
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet
from numerics.hr_native_field_sampling import add_native_field_sampling
from numerics.hr_compact_radial_interaction import compact_native_profile_map
from numerics.hr_native_sampling_compact import (
    compact_metric_radial_profiles, sampled_compact_native_map,
    integrate_sampled_compact_hr_interaction,SAMPLED_COMPACT_ORDER,
)
P=dict(N=1.,a=.92,n=1.13,alpha=.84,k=2.2,m2=.7,Mg2=1.2,
       betas=(.31,1.,-.4,.2,.13),mu=-.25,sigma_r=-.11,
       sigma_dot=.15,mu_dot=.14,n_dot=.09,alpha_dot=-.07,
       n_ddot=.025,alpha_ddot=-.02)

def test_native_jacobian_chain_rule_exact():
    r=.17;R=.3
    Q=sampled_compact_native_map(r=r,R=R,k=P['k'],mu=P['mu'],
                                 mu_dot=P['mu_dot'],sigma_r=P['sigma_r'],sigma_dot=P['sigma_dot'])
    p,dp=compact_metric_radial_profiles(r=r,R=R,k=P['k'])
    x=np.zeros(16)
    x[4:8]=[.1,-.11,.12,.02]
    x[12:16]=[.03,.05,-.06,.09]
    n=Q@x
    Tt=1+.5*P['sigma_dot']*r*r
    Tr=P['sigma_r']*r
    Rt=P['mu_dot']*r
    Rr=1+P['mu']
    for j in range(4):
        qt=x[12+j]*p[j]
        qr=x[4+j]*dp[j]
        assert Tt*n[14+j]+Rt*n[18+j]==pytest.approx(qt,abs=5e-14)
        assert Tr*n[14+j]+Rr*n[18+j]==pytest.approx(qr,abs=5e-14)
    assert Q.shape==(22,16)
    assert len(SAMPLED_COMPACT_ORDER)==16

def test_metric_profile_spatial_derivatives_independent_center():
    R=.3;k=2.2
    p,d=compact_metric_radial_profiles(r=0.,R=R,k=k)
    assert p[1]==p[3]==0
    assert d[0]==d[2]==d[3]==0
    assert d[1]==pytest.approx(-8/(R*R*k))
    for r in (.025,.1,.22):
        p,d=compact_metric_radial_profiles(r=r,R=R,k=k)
        h=1e-6
        v1=compact_metric_radial_profiles(r=r+h,R=R,k=k)[0]
        v0=compact_metric_radial_profiles(r=r-h,R=R,k=k)[0]
        np.testing.assert_allclose((v1-v0)/(2*h),d,atol=2e-7,rtol=3e-8)

def test_native_transport_nonzero_when_profile_advects():
    r=.19;R=.3;k=2.2
    q=sampled_compact_native_map(r=r,R=R,k=k,mu=-.25,mu_dot=.42,
                                 sigma_r=0,sigma_dot=0)
    p,dp=compact_metric_radial_profiles(r=r,R=R,k=k)
    for j in range(4):
        assert q[14+j,4+j]==pytest.approx(-.42*r*dp[j]/.75)
        assert q[18+j,4+j]==pytest.approx(dp[j]/.75)
        assert q[18+j,12+j]==0
    assert np.max(abs(q[14:18,4:8]))>0

def test_direct_quadratic_sampling_chain_rule_at_fixed_radius():
    r=.16;R=.32
    native=native_hr_stueckelberg_jet(r=r,**P)
    ext=add_native_field_sampling(native,r=r)
    Q=sampled_compact_native_map(r=r,R=R,k=P['k'],mu=P['mu'],mu_dot=P['mu_dot'],
                                 sigma_r=P['sigma_r'],sigma_dot=P['sigma_dot'])
    x=np.array([.1,-.05,.02,.01,.13,-.09,.02,.05,
                .06,-.03,.08,.04,.03,-.02,.07,-.01])
    full=Q@x
    local=full[:14].copy()
    for j in range(4):
        local[4+j]+=(full[14+j]*full[8]+r*full[18+j]*full[13])
    rhs=native.gradient@local+.5*full[:14]@native.hessian@full[:14]
    lhs=ext.gradient@full+.5*full@ext.hessian@full
    assert lhs==pytest.approx(rhs,rel=1e-13,abs=1e-13)

def test_spatial_integral_convergence_and_f_rate_cross_terms():
    a=integrate_sampled_compact_hr_interaction(radius=.23,quadrature_order=16,**P)
    b=integrate_sampled_compact_hr_interaction(radius=.23,quadrature_order=28,**P)
    np.testing.assert_allclose(a.hessian,b.hessian,rtol=2e-10,atol=8e-12)
    np.testing.assert_allclose(a.gradient,b.gradient,rtol=2e-10,atol=8e-12)
    assert a.value==pytest.approx(b.value,rel=2e-11)
    assert a.hessian.shape==(16,16)
    np.testing.assert_allclose(a.hessian,a.hessian.T,rtol=0,atol=2e-13)
    assert np.linalg.norm(a.hessian[12:16,8:12])>1e-7

def test_beta0_decoupling_after_sampling_and_quadrature():
    obj=integrate_sampled_compact_hr_interaction(radius=.21,quadrature_order=12,
        **dict(P,betas=(1.,0.,0.,0.,0.)))
    for j in range(4,16):
        assert abs(obj.gradient[j])<1e-12
        assert np.max(np.abs(obj.hessian[j,:]))<1e-12

def test_frozen_moving_chart_reduces_to_direct_derivatives():
    r=.16;R=.32;k=2.2
    Q=sampled_compact_native_map(r=r,R=R,k=k,mu=0.,mu_dot=0.,
                                 sigma_r=0.,sigma_dot=0.)
    p,dp=compact_metric_radial_profiles(r=r,R=R,k=k)
    for j in range(4):
        assert Q[14+j,12+j]==pytest.approx(p[j])
        assert Q[18+j,4+j]==pytest.approx(dp[j])
        assert Q[14+j,4+j]==0
        assert Q[18+j,12+j]==0
    np.testing.assert_array_equal(Q[:14,:12],compact_native_profile_map(r=r,R=R,k=k))

def test_bad_chart_and_domains_rejected():
    kw=dict(r=.2,R=.3,k=2.2,mu=-.25,mu_dot=.14,sigma_r=-.11,sigma_dot=.15)
    with pytest.raises(ValueError):sampled_compact_native_map(**dict(kw,mu=-1.))
    with pytest.raises(ValueError):sampled_compact_native_map(**dict(kw,k=0))
    with pytest.raises(ValueError):sampled_compact_native_map(**dict(kw,sigma_r=40.,mu_dot=40.))
    with pytest.raises(ValueError):integrate_sampled_compact_hr_interaction(radius=0,**P)
    with pytest.raises(ValueError):integrate_sampled_compact_hr_interaction(radius=.3,quadrature_order=7,**P)
