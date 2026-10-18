"""Independent compact full-scalar EH pullback & analytic-Hessian controls.

These test kinematic native ADM density covariance, NOT the full physical
nonhomothetic constrained Einstein–Hassan–Rosen two-dust action.
"""
import numpy as np
import pytest
from numerics.hr_eh_full_scalar_chart_ward import (
    FIELD_NAMES,native_fields,native_adm_from_field_samples,
    native_full_scalar_adm_density,full_scalar_chart_ward,
    full_scalar_spacetime_action,
)
from numerics.hr_full_scalar_eh_homothetic import _profiles, scalar_native_adm_jet
from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density


def _num_hessian(f,n,h=3.e-5):
    H=np.zeros((n,n));z=np.zeros(n);zero=f(z)
    for i in range(n):
        ei=np.zeros(n);ei[i]=h
        H[i,i]=(f(ei)+f(-ei)-2*zero)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n);ej[j]=h
            H[i,j]=H[j,i]=(f(ei+ej)-f(ei-ej)-f(-ei+ej)+f(-ei-ej))/(4*h*h)
    return H


def test_full_spherical_adm_density_vs_independent_old_eh_six_jet():
    # New nonlinear scalar ADM and old AD-Hessian use TWO distinct derivations.
    T=.13; R=.26; Rmax=.75; k=1.7
    F,Fr,Frr,E,Er,Err,*_=_profiles(R,Rmax,k)
    def f(x):
        samples=(x[0]*F,x[1]*Fr,x[1]*Frr,x[2]*F,x[2]*Fr,
                 x[2]*Frr,x[4]*F,x[3]*E,x[3]*Er,x[3]*Err,x[5]*E)
        return float(native_adm_from_field_samples(T,R,samples,k=k))
    a=1+.15*T+.035*T*T
    ad=.15+.07*T
    n=1+.08*T+.02*T*T
    old=scalar_native_adm_jet(scale=a,scale_rate=ad,lapse=n,
                             r=R,profile_radius=Rmax,k=k)
    np.testing.assert_allclose(_num_hessian(f,6),.5*old.hessian,
                               rtol=2e-4,atol=3e-5)
    assert f(np.zeros(6))==pytest.approx(.5*old.value,rel=4e-15)


def test_full_scalar_ward_for_each_field_and_both_chart_modes():
    result=full_scalar_chart_ward(quadrature_order=42)
    assert result.full_mixed.shape==(4,2)
    assert result.chart_min_determinant>0
    np.testing.assert_allclose(result.full_mixed,0.,atol=8e-11)
    assert np.all(np.abs(result.frozen_mixed)>1.e-6),result.frozen_mixed
    assert len(FIELD_NAMES)==4


def test_exact_finite_scalar_adm_action_chart_invariance_all_fields():
    for j in range(4):
        x=np.zeros(4);x[j]=.06
        ref=full_scalar_spacetime_action(amplitudes=x,quadrature_order=44)
        for et,er in ((.04,0),(-.04,0),(0,.035),(0,-.04),(.045,-.035)):
            changed=full_scalar_spacetime_action(
                amplitudes=x,eps_time=et,eps_radial=er,quadrature_order=44)
            assert changed==pytest.approx(ref,abs=2e-12)


def test_combined_four_native_scalars_and_radial_support():
    x=(.025,-.022,.032,-.012)
    for T,R in ((.4,.6),(.32,.72)):
        original=full_scalar_spacetime_action(amplitudes=x,time_radius=T,
                                              radial_radius=R,quadrature_order=46)
        shifted=full_scalar_spacetime_action(amplitudes=x,eps_time=.04,
                 eps_radial=-.03,time_radius=T,radial_radius=R,quadrature_order=46)
        assert original==pytest.approx(shifted,abs=3e-12)
        result=full_scalar_chart_ward(time_radius=T,radial_radius=R,
                                      quadrature_order=44)
        np.testing.assert_allclose(result.full_mixed,0.,atol=1e-10)
        assert np.min(np.abs(result.frozen_mixed))>2e-7


def test_frozen_sampling_fails_where_correct_native_sampling_passes():
    result=full_scalar_chart_ward(quadrature_order=46)
    # Both independent coordinate displacements and four scalar channels.
    assert np.all(np.abs(result.frozen_mixed)>1e-6)
    assert np.max(np.abs(result.full_mixed))<2e-10
    assert np.min(np.abs(result.frozen_mixed))>1e4*np.max(np.abs(result.full_mixed))


def test_flat_native_lapse_and_radial_shift_exact_adm_reference():
    T=.14;R=.28
    x=(.037,-.025,0.,0.)
    a=1+.15*T+.035*T*T
    ad=.15+.07*T
    n=1+.08*T+.02*T*T
    phi,U,Ur,*_=native_fields(T,R,x)
    new=native_full_scalar_adm_density(T,R,x)
    reference=.5*flat_spherical_adm_eh_density(scale_factor=a,
        scale_rate=ad,background_lapse=n,r=R,Phi=float(phi),
        shift=float(U),shift_r=float(Ur))
    assert float(new)==pytest.approx(reference,abs=2e-15)


def test_correct_compact_field_sampling_has_radial_regular_center():
    for R in (1e-8,1e-5,.2):
        _,U,_,psi,_,_,_,E,_,_,_=native_fields(.2,R,[.02,.03,.04,.05])
        assert np.isfinite(U) and np.isfinite(E)
        assert abs(U/R)<.1
        assert abs(E/R**2)<.1
        # Spherical regularity: Qr-Qt=-k²E vanishes as R².
        assert abs(1.7**2*E)<(.2*R*R)


def test_positive_chart_and_metric_domain_guards():
    with pytest.raises(ValueError):native_fields(.1,.2,[.1,.2,.3])
    with pytest.raises(ValueError):native_fields(.1,0.,[.1,.2,.3,.4])
    with pytest.raises(ValueError):native_full_scalar_adm_density(.1,.2,(-9,0,0,0))
    with pytest.raises(ValueError):native_full_scalar_adm_density(.1,.2,(0,0,0,0),k=0)
    with pytest.raises(ValueError):full_scalar_spacetime_action(eps_time=10)
    with pytest.raises(ValueError):full_scalar_spacetime_action(eps_radial=10)
    with pytest.raises(ValueError):full_scalar_chart_ward(quadrature_order=6)
    with pytest.raises(ValueError):full_scalar_chart_ward(eps=0)
