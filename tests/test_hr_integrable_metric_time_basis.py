"""Step32d: full compact metric parent fields, not disconnected rate jets."""
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import (
    Trajectory,sector_density,profile,hr_density,MG2,MF2
)
from numerics.hr_common_time_metric_rates import eh_rate_delta_density,action as old_rates
from numerics.hr_two_dust_common_time_canonical import (
    action as old_action,analytic_canonical_pair_integrals
)
from numerics.hr_integrable_metric_time_basis import (
    ORDER,temporal_profile,integrable_sector,action,first_variations
)

@pytest.fixture(scope='module')
def bg():return Trajectory.solve(width=.04)


def test_compact_new_parent_time_profile_and_exact_derivative():
    R=.027
    for t in (-R,-.014,-.005,0.,.006,.019,R):
        T,Tp,G,Gp=temporal_profile(t,R)
        if abs(t)==R:
            assert G==0. and Gp==0.
        if abs(t)<.026:
            h=1e-6
            derivative=(temporal_profile(t+h,R)[2]-temporal_profile(t-h,R)[2])/(2*h)
            assert Gp==pytest.approx(derivative,abs=1e-7)
    assert temporal_profile(0.,R)[2]==0.
    assert temporal_profile(0.,R)[3]==1.
    assert len(ORDER)==18


def test_same_full_action_exactly_old_phase_space_action_when_extras_zero(bg):
    for x in (np.zeros(14),
              np.array([.012,-.004,.006,-.002,.008,.013,-.009,
                        -.008,.006,-.005,.002,-.006,.009,.005])):
        new=action(np.r_[x,np.zeros(4)],trajectory=bg,quadrature_order=20)
        old=old_action(x,trajectory=bg,quadrature_order=20)
        np.testing.assert_allclose(new.contributions,old.contributions,atol=0,rtol=0)


def test_eh_integrable_kinetics_against_independent_step32b_exact_finite_rate_patch(bg):
    # For one time node, s_eff=s+v*t and e_eff=e+w*t describe the
    # instantaneous spatial metric. Its true rate differs from the
    # old isolated parent rate by +v*T and +w*T; that exact contribution
    # was independently derived in Step32b's ADM extrinsic-curvature jet.
    for t,r,which in ((.007,.14,'g'),(-.011,.18,'f')):
        a,b,ad,bd,nf,rhog,rhof=bg.at(t)
        scale,srate,N,planck,rho=(a,ad,1.,MG2,rhog) if which=='g' else (b,bd,nf,MF2,rhof)
        x=np.array([.018,-.012,.021,-.013]);extra=np.array([.026,-.032])
        target,metric,area,R3=integrable_sector(scale=scale,scale_rate=srate,
                lapse=N,planck=planck,amp=x,extra=extra,t=t,r=r,
                time_radius=.027,radial_radius=.32)
        effective=np.array([x[0],x[1],x[2]+t*extra[0],x[3]+t*extra[1],0.,0.])
        old,_,old_metric,old_area,old_R3=sector_density(scale=scale,
                scale_rate=srate,lapse=N,rho0=rho,amp=effective,t=t,r=r,
                time_radius=.027,radial_radius=.32,planck=planck)
        correction=eh_rate_delta_density(scale=scale,scale_rate=srate,
                background_lapse=N,planck=planck,original_metric_amp=effective[:4],
                psi_rate=extra[0],E_rate=extra[1],t=t,r=r,
                time_radius=.027,radial_radius=.32)
        assert float(target)==pytest.approx(float(old+correction),rel=5e-12,abs=2e-15)
        np.testing.assert_allclose(metric,old_metric,atol=2e-15,rtol=3e-14)
        assert area==pytest.approx(old_area,rel=3e-14)
        assert R3==pytest.approx(old_R3,rel=3e-14,abs=1e-14)


def test_all_sixteen_legal_compact_field_tadpoles_vanish_on_shell(bg):
    gradient=first_variations(trajectory=bg,quadrature_order=20,step=2e-5)
    legal=[i for i in range(18) if i not in (6,13)]
    assert np.max(np.abs(gradient[legal]))<6e-10
    np.testing.assert_allclose(gradient[14:18],0.,atol=6e-10,rtol=0)
    # Two OLD theta_rate local jets are not independent compact theta
    # fields, hence their raw first derivative is (legitimately) nonzero.
    assert abs(gradient[6])>1e-4 and abs(gradient[13])>1e-5


def test_old_disconnected_metric_rate_jets_fail_the_same_tadpole_condition(bg):
    h=2e-5
    for i in (14,16):
        v=np.zeros(18);v[i]=h
        old=(old_rates(v,trajectory=bg,quadrature_order=20).total
            -old_rates(-v,trajectory=bg,quadrature_order=20).total)/(2*h)
        new=(action(v,trajectory=bg,quadrature_order=20).total
            -action(-v,trajectory=bg,quadrature_order=20).total)/(2*h)
        assert abs(old)>1e-7
        assert abs(new)<1e-9
    # Avoid interpreting the resulting two trial Hessians as physical modes.


def test_independent_parent_f_trace_changes_both_f_3geometry_and_hr(bg):
    x=np.zeros(18);x[16]=.021
    base=action(trajectory=bg,quadrature_order=20)
    changed=action(x,trajectory=bg,quadrature_order=20)
    assert abs(changed.contributions[1]-base.contributions[1])>1e-12
    assert abs(changed.contributions[2]-base.contributions[2])>1e-13
    assert changed.contributions[0]==base.contributions[0]
    assert changed.contributions[3]==base.contributions[3]
    # IMPORTANT: at fixed canonical momentum and comoving phase theta_r=0,
    # H_dust=N*p is independent of the spatial metric. f dust stays fixed.
    assert changed.contributions[4]==base.contributions[4]


def test_both_dust_canonical_p_dot_theta_time_rate_pairs_survive(bg):
    h=.008
    def cross(i,j):
        x=np.zeros(18);y=np.zeros(18);x[i]=h;y[j]=h
        return (action(x+y,trajectory=bg,quadrature_order=20).total
               -action(x-y,trajectory=bg,quadrature_order=20).total
               -action(-x+y,trajectory=bg,quadrature_order=20).total
               +action(-x-y,trajectory=bg,quadrature_order=20).total)/(4*h*h)
    H=np.array([[cross(i,j) for j in (6,13)] for i in (5,12)])
    np.testing.assert_allclose(H,analytic_canonical_pair_integrals(quadrature_order=20),
                               atol=2e-12,rtol=2e-6)
    assert np.linalg.matrix_rank(H,tol=1e-8)==2


def test_linear_field_variations_converge_under_quadrature(bg):
    for order in (14,22,30):
        g=first_variations(trajectory=bg,quadrature_order=order,step=3e-5)
        assert np.max(np.abs(g[[i for i in range(18) if i not in (6,13)]]))<5e-10


def test_integrable_parent_variations_are_not_extra_velocity_only(bg):
    # A parent compact field changes the SPATIAL metric at generic t!=0;
    # in contrast the old step32b rate jet changed EH kinetic ONLY.
    t=.008;r=.17;a,b,ad,bd,nf,rhog,rhof=bg.at(t)
    zero,metric0,area0,R30=integrable_sector(scale=b,scale_rate=bd,
        lapse=nf,planck=MF2,amp=np.zeros(4),extra=np.zeros(2),
        t=t,r=r,time_radius=.027,radial_radius=.32)
    v,metric1,area1,R31=integrable_sector(scale=b,scale_rate=bd,
        lapse=nf,planck=MF2,amp=np.zeros(4),extra=np.array([.04,.03]),
        t=t,r=r,time_radius=.027,radial_radius=.32)
    assert abs(area1-area0)>1e-8
    assert abs(R31-R30)>1e-6
    assert abs(v-zero)>1e-8


def test_integrable_domain_and_support_guards(bg):
    with pytest.raises(ValueError):action(np.zeros(17),trajectory=bg)
    with pytest.raises(ValueError):action(np.full(18,np.nan),trajectory=bg)
    with pytest.raises(ValueError):action(trajectory=bg,quadrature_order=8)
    with pytest.raises(ValueError):action(trajectory=bg,time_radius=.05)
    with pytest.raises(ValueError):integrable_sector(scale=1.,scale_rate=.1,lapse=1.,
      planck=1.,amp=np.zeros(4),extra=np.zeros(2),t=0.,r=0.,
      time_radius=.027,radial_radius=.32)
    with pytest.raises(ValueError):temporal_profile(0.,-1.)
    with pytest.raises(ValueError):first_variations(step=0,trajectory=bg)
