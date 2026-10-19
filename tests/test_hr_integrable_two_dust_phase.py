"""Step32e: both dust clocks now admit real compact parent time derivatives."""
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import Trajectory,profile,CG,CF
from numerics.hr_integrable_metric_time_basis import (
    action as step32d_action,temporal_profile
)
from numerics.hr_two_dust_common_time_canonical import (
    analytic_canonical_pair_integrals,dust_reduced_density
)
from numerics.hr_integrable_two_dust_phase import (
    ORDER,phase_samples_integrable,action,first_variations,
    analytic_integrable_pair_block,finite_canonical_pair_block,
    phase_integration_by_parts
)

@pytest.fixture(scope='module')
def bg():return Trajectory.solve(width=.04)


def test_both_dust_parents_and_velocities_are_actual_derivatives():
    time_radius=.027;radius=.32
    for t in (-.025,-.012,0.,.014,.024):
        for r in (.11,.24):
            theta=.08;extra=-.12
            T,Tp,F,Fr,_=profile(t,r,time_radius,radius)
            _,_,G,Gp=temporal_profile(t,time_radius)
            calc_t,calc_r,p=phase_samples_integrable(base_lapse=1.,charge=CG,
                r=r,t=t,time_radius=time_radius,radial_radius=radius,
                theta_amp=theta,p_amp=.04,theta_extra=extra)
            h=1e-6
            def field(t_,r_):
                tt=temporal_profile(t_,time_radius)[0]
                GG=temporal_profile(t_,time_radius)[2]
                FF=profile(t_,r_,time_radius,radius)[2]
                return (theta*tt+extra*GG)*FF
            d_t=(field(t+h,r)-field(t-h,r))/(2*h)
            d_r=(field(t,r+h)-field(t,r-h))/(2*h)
            assert calc_t-1==pytest.approx(d_t,abs=8e-8)
            assert calc_r==pytest.approx(d_r,abs=8e-8)
            assert p>0
    assert ORDER[6]=='theta_g_extra_tT' and ORDER[13]=='theta_f_extra_tT'


def test_new_action_exactly_step32d_when_phase_extra_is_zero(bg):
    for x in (np.zeros(18),
              np.array([.011,-.003,.008,-.005,.016,.019,0.,
                        -.012,.004,-.007,.006,.015,.023,0.,
                        .01,-.012,.018,-.009])):
        new=action(x,trajectory=bg,quadrature_order=20)
        old=step32d_action(x,trajectory=bg,quadrature_order=20)
        np.testing.assert_array_equal(new.contributions,old.contributions)
        assert new.total==old.total


def test_all_eighteen_compact_field_tadpoles_cancel_on_shell(bg):
    g=first_variations(trajectory=bg,quadrature_order=20,step=2e-5)
    assert g.shape==(18,)
    assert max(abs(g))<5e-10
    np.testing.assert_allclose(g[[6,13]],0,atol=5e-11,rtol=0)
    np.testing.assert_allclose(g[14:18],0,atol=5e-10,rtol=0)


def test_old_disconnected_phase_velocity_tadpoles_are_removed(bg):
    h=2e-5
    for idx,min_old in ((6,1e-4),(13,1e-5)):
        v=np.zeros(18);v[idx]=h
        old=(step32d_action(v,trajectory=bg,quadrature_order=20).total-
             step32d_action(-v,trajectory=bg,quadrature_order=20).total)/(2*h)
        new=(action(v,trajectory=bg,quadrature_order=20).total-
             action(-v,trajectory=bg,quadrature_order=20).total)/(2*h)
        assert abs(old)>min_old
        assert abs(new)<1e-10


def test_exact_temporal_integration_by_parts_for_both_canonical_pairs():
    for charge in (CG,CF):
        for th,extra,pa in ((.12,-.07,.14),(-.08,.15,-.11),(.03,.22,.27)):
            lhs,rhs=phase_integration_by_parts(charge=charge,theta_amp=th,
                   theta_extra=extra,p_amp=pa,quadrature_order=32)
            assert lhs==pytest.approx(rhs,abs=2e-14,rel=2e-12)


def test_two_integrable_symplectic_projected_coefficients_are_half_previous():
    for q in (16,24,32):
        new=analytic_integrable_pair_block(quadrature_order=q)
        old=analytic_canonical_pair_integrals(quadrature_order=q)
        np.testing.assert_allclose(new,.5*old,rtol=0,atol=0)
        assert np.linalg.matrix_rank(new,tol=1e-8)==2
        np.testing.assert_allclose(new-np.diag(np.diag(new)),0.,atol=0)


def test_projected_dual_pair_block_matches_independent_action_second_variation(bg):
    calc=finite_canonical_pair_block(step=.009,trajectory=bg,quadrature_order=20)
    exact=analytic_integrable_pair_block(quadrature_order=20)
    np.testing.assert_allclose(calc,exact,atol=2e-12,rtol=2e-6)
    assert np.linalg.matrix_rank(calc,tol=1e-8)==2


def test_parent_phase_uses_both_time_profiles_and_is_not_local_velocity_only(bg):
    x=np.zeros(18);x[6]=.21;x[13]=-.13
    v=action(x,trajectory=bg,quadrature_order=20)
    zero=action(trajectory=bg,quadrature_order=20)
    assert v.contributions[0]==zero.contributions[0]
    assert v.contributions[1]==zero.contributions[1]
    assert v.contributions[2]==zero.contributions[2]
    assert abs(v.contributions[3]-zero.contributions[3])>1e-10
    assert abs(v.contributions[4]-zero.contributions[4])>1e-11


def test_matter_independence_and_cross_phase_coupling_zero(bg):
    x=np.zeros(18);x[6]=.14
    base=action(trajectory=bg,quadrature_order=20)
    gonly=action(x,trajectory=bg,quadrature_order=20)
    assert gonly.contributions[4]==base.contributions[4]
    x=np.zeros(18);x[13]=-.14
    fonly=action(x,trajectory=bg,quadrature_order=20)
    assert fonly.contributions[3]==base.contributions[3]


def test_full_action_tadpoles_converge_with_quadrature_and_support(bg):
    for q in (14,22,28):
        g=first_variations(trajectory=bg,quadrature_order=q,step=2e-5)
        assert np.max(abs(g))<5e-10
    for width in (.019,.027,.034):
        g=first_variations(trajectory=bg,time_radius=width,
                           quadrature_order=20,step=2e-5)
        assert np.max(abs(g))<9e-10


def test_canonical_momentum_positive_domain_guards(bg):
    x=np.zeros(18);x[5]=-4.
    with pytest.raises(ValueError):action(x,trajectory=bg,quadrature_order=18)
    x=np.zeros(18);x[12]=-4.
    with pytest.raises(ValueError):action(x,trajectory=bg,quadrature_order=18)
    with pytest.raises(ValueError):phase_samples_integrable(base_lapse=1.,charge=1.,
      r=.1,t=0.,time_radius=.027,radial_radius=.32,
      theta_amp=float('inf'),p_amp=0.,theta_extra=0.)


def test_reject_bad_inputs_and_difference_step(bg):
    with pytest.raises(ValueError):action(np.zeros(17),trajectory=bg)
    with pytest.raises(ValueError):action(np.full(18,np.nan),trajectory=bg)
    with pytest.raises(ValueError):action(trajectory=bg,quadrature_order=7)
    with pytest.raises(ValueError):action(trajectory=bg,time_radius=.06)
    with pytest.raises(ValueError):first_variations(step=0,trajectory=bg)
    with pytest.raises(ValueError):finite_canonical_pair_block(step=0,trajectory=bg)
