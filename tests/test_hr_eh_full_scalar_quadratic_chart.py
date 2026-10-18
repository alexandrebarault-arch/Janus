"""The actual spacetime quadratic EH chart Hessian has boundary-null chart rows."""
import numpy as np
import pytest
from numerics.hr_eh_full_scalar_quadratic_chart import (
    full_scalar_eh_chart_quadratic,
    native_eh_metric_quadratic_in_deformed_chart,QUADRATIC_ORDER,
)
from numerics.hr_eh_full_scalar_chart_ward import full_scalar_chart_ward


def test_full_spacetime_eh_chart_rows_null_but_metric_block_nonzero():
    out=full_scalar_eh_chart_quadratic(quadrature_order=42)
    assert out.hessian.shape==(6,6)
    assert QUADRATIC_ORDER==('deltaT','deltaR','Phi_f','U_f','psi_f','E_f')
    np.testing.assert_allclose(out.hessian,out.hessian.T,rtol=0,atol=2e-14)
    np.testing.assert_allclose(out.hessian[:2,:],0.,atol=4e-10)
    assert np.linalg.norm(out.hessian[2:,2:])>1.
    assert abs(out.gradient[0])<1e-11 and abs(out.gradient[1])<1e-11


def test_negative_control_frozen_native_metric_sampling_breaks_chart_nullity():
    full=full_scalar_eh_chart_quadratic()
    frozen=full_scalar_eh_chart_quadratic(freeze_native_sampling=True)
    assert np.max(np.abs(full.hessian[:2,2:]))<1e-9
    assert np.min(np.abs(frozen.hessian[:2,2:]))>1e-6
    # Without transported field variations, the native metric Hessian at
    # the identity chart is unchanged, but its mixed chart block is WRONG.
    np.testing.assert_allclose(full.hessian[2:,2:],
                               frozen.hessian[2:,2:],atol=1e-10)
    assert np.linalg.norm(frozen.hessian[:2,2:])>1e-2


def test_metric_field_hessian_invariant_under_finite_chart_motion():
    baseline=native_eh_metric_quadratic_in_deformed_chart(
        eps_time=0.,eps_radial=0.)
    for epT,epR in ((.04,0),(-.035,0),(0,.035),(0,-.04),(.045,-.035)):
        shifted=native_eh_metric_quadratic_in_deformed_chart(
            eps_time=epT,eps_radial=epR)
        np.testing.assert_allclose(shifted,baseline,atol=7e-10,rtol=2e-9)


def test_complete_quadratic_matches_separate_metric_hessian_oracle():
    joined=full_scalar_eh_chart_quadratic()
    metric=native_eh_metric_quadratic_in_deformed_chart(
        eps_time=0.,eps_radial=0.,step=.004)
    np.testing.assert_allclose(joined.hessian[2:,2:],metric,atol=1e-10,rtol=1e-10)


def test_mixed_eh_chart_hessian_matches_independent_ward_table():
    combined=full_scalar_eh_chart_quadratic(
        quadrature_order=42,chart_step=.002,field_step=.002)
    ward=full_scalar_chart_ward(
        quadrature_order=42,eps=.002,field_step=.002)
    np.testing.assert_allclose(combined.hessian[:2,2:].T,ward.full_mixed,
                               rtol=0,atol=1e-10)
    frozen=full_scalar_eh_chart_quadratic(
        quadrature_order=42,chart_step=.002,field_step=.002,
        freeze_native_sampling=True)
    np.testing.assert_allclose(frozen.hessian[:2,2:].T,ward.frozen_mixed,
                               rtol=0,atol=1e-10)


def test_time_radial_chart_hessian_null_with_shifted_compact_support():
    for T,R in ((.3,.7),(.42,.55)):
        x=full_scalar_eh_chart_quadratic(
            time_radius=T,radial_radius=R,quadrature_order=44)
        np.testing.assert_allclose(x.hessian[:2,:],0.,atol=7e-10)
        assert np.linalg.norm(x.hessian[2:,2:])>.1


def test_finite_difference_step_refinement_and_nonlinear_zero_modes():
    a=full_scalar_eh_chart_quadratic(quadrature_order=42,
                                    chart_step=.004,field_step=.006)
    b=full_scalar_eh_chart_quadratic(quadrature_order=42,
                                    chart_step=.002,field_step=.003)
    np.testing.assert_allclose(a.hessian[2:,2:],b.hessian[2:,2:],atol=6e-3,rtol=7e-4)
    assert np.max(np.abs(a.hessian[:2,:]))<1e-9
    assert np.max(np.abs(b.hessian[:2,:]))<2e-9


def test_reject_invalid_chart_and_field_steps():
    for params in ({'chart_step':0.},{'field_step':-1.},
                   {'chart_step':float('inf')},{'quadrature_order':5},
                   {'time_radius':-1.}):
        with pytest.raises(ValueError):full_scalar_eh_chart_quadratic(**params)
    with pytest.raises(ValueError):native_eh_metric_quadratic_in_deformed_chart(
        eps_time=0,eps_radial=0,step=0)


def test_hr_mixed_interaction_has_nonzero_relative_chart_response():
    # Contrast the isolated f EH compact-coordinate null direction against
    # an algebraic HR beta1-3 potential. Different radial/trial profiles:
    # NONZERO here is only an interaction benchmark, not a physical mode.
    from numerics.hr_compact_radial_interaction import integrate_compact_hr_interaction
    pars=dict(N=1.,a=.92,n=1.13,alpha=.84,k=2.2,m2=.7,Mg2=1.2,
              betas=(0.,1.,-.4,.2,0.),mu=-.25,sigma_r=-.11,
              sigma_dot=.15,mu_dot=.14,n_dot=.09,alpha_dot=-.07,
              n_ddot=.025,alpha_ddot=-.02)
    hr=integrate_compact_hr_interaction(radius=.23,quadrature_order=32,**pars)
    chart=hr.hessian[8:12,8:12]
    assert np.linalg.norm(chart)>.01
    assert np.linalg.norm(hr.hessian[:8,8:12])>.01
    off=integrate_compact_hr_interaction(
        radius=.23,quadrature_order=16,**dict(pars,m2=0.))
    np.testing.assert_allclose(off.hessian,0.,rtol=0,atol=1e-15)
