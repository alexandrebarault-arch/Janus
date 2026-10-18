"""Step29: falsify naive insertion of on-shell FLRW into a relative chart.

These are *necessary* local g-lapse field-equation tests. They are not
full on-shell solutions of the coupled inhomogeneous bimetric equations.
"""
import math
import numpy as np
import pytest
from numerics.hr_nonhomothetic_center_obstruction import (
    center_g_lapse_source, snapshot_on_homogeneous_g_constraint,
    independent_g_lapse_hr_derivative, independent_total_g_lapse_residual,
    compact_g_lapse_first_variation, radial_bump_norm,
    central_linearized_chart_sensitivity, Jg, Vg,
)

# Previously verified Step28 radiation-free dust Candidate-C y and Nf values.
SNAPSHOTS=((1.0,.5568825591873054,.551545778648),
           (.4,.578770722803,.518526433828),
           (.05,1.360739478178,.417132659305),
           (.03,1.979545244855,.461831564933))


def background(a=.4):
    _,y,nf=next(row for row in SNAPSHOTS if row[0]==a)
    return snapshot_on_homogeneous_g_constraint(a=a,y=y,Nf=nf)


def test_original_candidate_c_g_friedmann_residual_vanishes():
    for a,y,nf in SNAPSHOTS:
        q=snapshot_on_homogeneous_g_constraint(a=a,y=y,Nf=nf)
        c=center_g_lapse_source(q)
        assert abs(c.g_lapse_original)<1e-11
        assert abs(c.g_lapse_mapped)<1e-11
        assert c.obstruction==0.


def test_naive_fixed_f_native_scale_insertion_is_offshell():
    q=background(.4)
    c=center_g_lapse_source(q,radial_scale=.78)
    assert c.spatial_ratio_after==pytest.approx(.78*c.spatial_ratio_before)
    assert c.g_lapse_mapped==pytest.approx(0.160780603696934,abs=3e-12)
    assert c.obstruction==pytest.approx(c.g_lapse_mapped-c.g_lapse_original)
    assert abs(c.g_lapse_original)<1e-12


@pytest.mark.parametrize('a,lambda_r',[(1.,.78),(.4,.78),(.05,.78),(.03,.231117),(.4,.5)])
def test_direct_full_hr_square_root_g_lapse_derivative_matches_central_formula(a,lambda_r):
    q=background(a)
    exact=center_g_lapse_source(q,radial_scale=lambda_r)
    direct=independent_total_g_lapse_residual(q,radius=1e-4,
            radial_scale=lambda_r,step=5e-6)
    assert direct==pytest.approx(exact.g_lapse_mapped,abs=2e-8)
    if lambda_r!=1:
        assert abs(exact.obstruction)>1e-3


def test_direct_HR_source_approaches_center_as_radius_decreases():
    q=background(.4)
    c=center_g_lapse_source(q,radial_scale=.78)
    a=independent_total_g_lapse_residual(q,radius=.06,radial_scale=.78,
           radial_scale_rate=.05,sigma=.08,sigma_rate=.025,b_rate=.17,
           fn_rate=.04,step=5e-6)
    b=independent_total_g_lapse_residual(q,radius=.03,radial_scale=.78,
           radial_scale_rate=.05,sigma=.08,sigma_rate=.025,b_rate=.17,
           fn_rate=.04,step=5e-6)
    assert abs(b-c.g_lapse_mapped)<abs(a-c.g_lapse_mapped)*.27
    assert abs(b-c.g_lapse_mapped)>1e-9


def test_even_lambda_one_has_offshell_radial_lapse_source_if_tilted():
    q=background(.4)
    assert abs(center_g_lapse_source(q,radial_scale=1.).g_lapse_mapped)<1e-12
    r=.20
    z=independent_total_g_lapse_residual(q,radius=r,radial_scale=1.,
        radial_scale_rate=.04,sigma=.08,sigma_rate=.025,b_rate=.17,
        fn_rate=.04,step=5e-6)
    assert abs(z)>5e-4
    z0=independent_total_g_lapse_residual(q,radius=r,radial_scale=1.,
          step=5e-6)
    assert abs(z0)<2e-9


def test_compact_lapse_action_variation_agrees_center_formula():
    q=background(.4)
    radius=.035
    act=compact_g_lapse_first_variation(q,support_radius=radius,
                                       radial_scale=.78,quadrature_order=32)
    analytic=center_g_lapse_source(q,radial_scale=.78).obstruction*radial_bump_norm(radius)
    assert act==pytest.approx(analytic,rel=2e-6,abs=5e-12)
    assert abs(act)>1e-7


def test_on_shell_positive_control_exact_zero_compact_tadpole():
    q=background(.4)
    variation=compact_g_lapse_first_variation(q,support_radius=.24,
                                             radial_scale=1.,quadrature_order=32)
    assert abs(variation)<1e-11


def test_tilted_chart_offshell_compact_tadpole_nonzero_at_lambda_one():
    q=background(.4)
    plain=compact_g_lapse_first_variation(q,support_radius=.29,
                                         radial_scale=1.,quadrature_order=30)
    tilted=compact_g_lapse_first_variation(q,support_radius=.29,
        radial_scale=1.,radial_scale_rate=.04,sigma=.08,sigma_rate=.025,
        b_rate=.17,fn_rate=.04,quadrature_order=30)
    # Finite-difference of the integrated action has O(eps²)+roundoff.
    assert abs(plain)<1e-10
    assert abs(tilted)>1e-6


def test_linearized_obstruction_slope_equals_nontrivial_HR_J_polynomial():
    for a in (1.,.4,.05):
        q=background(a)
        h=2e-4
        fp=center_g_lapse_source(q,radial_scale=1+h).g_lapse_mapped
        fm=center_g_lapse_source(q,radial_scale=1-h).g_lapse_mapped
        derivative=(fp-fm)/(2*h)
        expected=central_linearized_chart_sensitivity(q)
        assert derivative==pytest.approx(expected,rel=3e-7,abs=1e-8)
        assert abs(expected)>1e-2


def test_f_scale_coordinate_compensation_cancels_central_source():
    q=background(.4)
    lam=.78
    # Positive counterexample to an overbroad "nonhomothetic impossible" claim:
    # if one consistently rescales the native f scale to b/lambda, then
    # lambda*b_native/a=y. Other f matter/EH equations still need checking.
    from dataclasses import replace
    compensated=replace(q,b=q.b/lam)
    c=center_g_lapse_source(compensated,radial_scale=lam)
    assert abs(c.g_lapse_mapped)<1e-12
    assert abs(c.g_lapse_original)>1e-3


def test_beta4_has_no_visible_g_lapse_effect():
    from dataclasses import replace
    q=background(.4)
    m=replace(q,beta=tuple(q.beta[:4])+(-9999.,))
    for lam in (1.,.78,.23):
        assert center_g_lapse_source(q,radial_scale=lam).obstruction==pytest.approx(
               center_g_lapse_source(m,radial_scale=lam).obstruction,abs=1e-13)
        x=independent_g_lapse_hr_derivative(q,radius=.002,radial_scale=lam)
        y=independent_g_lapse_hr_derivative(m,radius=.002,radial_scale=lam)
        assert x==pytest.approx(y,abs=1e-6)


def test_zero_HR_mass_removes_relative_chart_source():
    from dataclasses import replace
    q=replace(background(.4),m2=0.)
    r0=center_g_lapse_source(q,radial_scale=1.)
    r1=center_g_lapse_source(q,radial_scale=.3)
    assert r0.obstruction==r1.obstruction==0.
    assert r0.g_lapse_mapped==r1.g_lapse_mapped
    assert independent_g_lapse_hr_derivative(q,radius=.2,radial_scale=.5)==pytest.approx(0.,abs=1e-12)


def test_quadrature_and_amplitude_step_refinement():
    q=background(.4)
    kw=dict(support_radius=.25,radial_scale=.78,radial_scale_rate=.05,
            sigma=.08,sigma_rate=.025,b_rate=.17,fn_rate=.04)
    a=compact_g_lapse_first_variation(q,quadrature_order=18,amplitude_step=4e-6,**kw)
    b=compact_g_lapse_first_variation(q,quadrature_order=34,amplitude_step=2e-6,**kw)
    assert a==pytest.approx(b,rel=1e-7,abs=1e-10)
    assert abs(a)>1e-5


def test_parameter_and_chart_guards():
    q=background(.4)
    for scale in (0.,-1.,float('nan')):
        with pytest.raises(ValueError):center_g_lapse_source(q,radial_scale=scale)
    for kw in ({'radius':0.}, {'radius':.1,'step':0.},
               {'radius':.1,'radial_scale':.1,'radial_scale_rate':500.,'sigma':500.}):
        with pytest.raises(ValueError):independent_g_lapse_hr_derivative(q,**kw)
    for kw in ({'support_radius':0.},{'quadrature_order':3},
               {'amplitude_step':-1.}):
        with pytest.raises(ValueError):compact_g_lapse_first_variation(q,**kw)
    with pytest.raises(ValueError):radial_bump_norm(0.)


def test_candidate_snapshots_reproduce_independent_dust_only_quartic_and_f_lapse():
    # Independent quartic in the pre-existing Step28 parameters; checks that
    # the archived (a,y,Nf) inputs are indeed from that on-shell background,
    # not freely chosen labels to force the visible Friedmann constraint.
    alpha2=.10879548725**2; m2=23.3348939346
    Cg=.9; Cf=3*.23958426762*.5568825591873054**3
    b1,b2,b3,b4=(1.,-4.2383993109,13.6801214252,-38.5117901844)
    for a,y_ref,nf_ref in SNAPSHOTS:
        c=np.array([alpha2*m2*b3/3,alpha2*m2*b2-m2*b4/3,
                    alpha2*m2*b1-m2*b3,alpha2*Cg/(3*a**3)-m2*b2,
                    -Cf/(3*a**3)-m2*b1/3])
        roots=np.roots(c)
        y=min((v.real for v in roots if abs(v.imag)<1e-9 and v.real>0),
              key=lambda v:abs(v-y_ref))
        assert y==pytest.approx(y_ref,abs=2e-11)
        py=np.polyval(np.polyder(c),y)
        pn=(-alpha2*Cg/a**3)*y+Cf/a**3
        n_f=y-pn/py
        assert n_f==pytest.approx(nf_ref,abs=2e-10)
        assert abs(np.polyval(c,y))<1e-9


def test_compensating_center_f_scale_does_not_fix_tilted_finite_radius_lapse():
    from dataclasses import replace
    from numerics.hr_nonhomothetic_center_obstruction import f_common_slice_spatial_anisotropy
    q=background(.4);lam=.78
    compensated=replace(q,b=q.b/lam)
    assert abs(center_g_lapse_source(compensated,radial_scale=lam).g_lapse_mapped)<1e-12
    r=.2
    with_tilt=independent_total_g_lapse_residual(
        compensated,radius=r,radial_scale=lam,
        radial_scale_rate=.04,sigma=.08,sigma_rate=.025,
        b_rate=.17/lam,fn_rate=.04,step=5e-6)
    without_tilt=independent_total_g_lapse_residual(
        compensated,radius=r,radial_scale=lam,
        radial_scale_rate=.04,sigma=0.,sigma_rate=.025,
        b_rate=.17/lam,fn_rate=.04,step=5e-6)
    assert abs(with_tilt)>1e-3
    assert abs(without_tilt)<5e-6
    assert f_common_slice_spatial_anisotropy(
        f_native_lapse=q.Nf,radial_coordinate=r,sigma=.08,
        f_native_lapse_rate=.04)<0


def test_tilted_slice_anisotropy_is_exact_kinematic_slicing_witness():
    from numerics.hr_nonhomothetic_center_obstruction import f_common_slice_spatial_anisotropy
    q=background(.4)
    for r in (.04,.1,.3):
        s=.12
        n=q.Nf+.05*(.5*s*r*r)
        expected=-(n*s*r)**2
        actual=f_common_slice_spatial_anisotropy(
            f_native_lapse=q.Nf,radial_coordinate=r,
            sigma=s,f_native_lapse_rate=.05)
        assert actual==pytest.approx(expected,rel=5e-15)
        assert f_common_slice_spatial_anisotropy(
            f_native_lapse=q.Nf,radial_coordinate=r,sigma=0.)==0.
    with pytest.raises(ValueError):f_common_slice_spatial_anisotropy(
        f_native_lapse=-1.,radial_coordinate=.1,sigma=.1)
