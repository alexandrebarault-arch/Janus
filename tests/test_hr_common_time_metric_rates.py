"""Extra native ADM trace/shear time jets, all preconstraint only."""
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import Trajectory, sector_density,profile,M2,MG2,MF2
from numerics.hr_two_dust_common_time_canonical import (
    action as old_action,analytic_canonical_pair_integrals
)
from numerics.hr_common_time_metric_rates import (
    ORDER, RATE_INDICES,eh_rate_delta_density,action,
    extra_rate_hessian,analytic_background_rate_hessian
)

@pytest.fixture(scope='module')
def bg():return Trajectory.solve(width=.04)


def test_full_18_field_rate_jet_action_reduces_exactly_to_14_without_rates(bg):
    x14=np.array([.012,-.004,.006,-.002,.008,.013,-.009,
             -.008,.006,-.005,.002,-.006,.009,.005])
    actual=action(np.r_[x14,np.zeros(4)],trajectory=bg,quadrature_order=22)
    old=old_action(x14,trajectory=bg,quadrature_order=22)
    np.testing.assert_allclose(actual.contributions,old.contributions,atol=1e-17,rtol=1e-14)
    assert len(ORDER)==18 and RATE_INDICES==(14,15,16,17)


def test_exact_background_eh_metric_rate_kinetic_H_matches_closed_form(bg):
    # Use h~.03 rather than 1e-4: f shear coefficient is order 1e-11 and
    # otherwise buried by finite differencing a nonzero background action.
    numeric=extra_rate_hessian(step=.03,quadrature_order=22,trajectory=bg)
    analytic=analytic_background_rate_hessian(quadrature_order=22,trajectory=bg)
    np.testing.assert_allclose(numeric,analytic,rtol=1e-4,atol=3e-15)
    assert numeric[0,0]<0 and numeric[2,2]<0
    assert numeric[1,1]>0 and numeric[3,3]>0
    # Negative PRECONSTRAINT trace is NOT a physical BD ghost test.


def test_analytic_rate_block_diagonal_between_two_sectors_and_trace_shear(bg):
    H=analytic_background_rate_hessian(trajectory=bg)
    assert H.shape==(4,4)
    np.testing.assert_allclose(H,np.diag(np.diag(H)),atol=0,rtol=0)
    assert np.linalg.matrix_rank(H,tol=1e-13)==4


def test_added_metric_rate_jets_affect_only_each_sectors_EH_piece(bg):
    for i,target,min_effect in ((14,0,1e-9),(15,0,1e-13),(16,1,1e-10),(17,1,1e-15)):
        x=np.zeros(18);x[i]=.024
        base=action(trajectory=bg)
        varied=action(x,trajectory=bg)
        keep=[j for j in range(5) if j!=target]
        np.testing.assert_allclose(varied.contributions[keep],
             base.contributions[keep],rtol=0,atol=6e-17)
        assert abs(varied.contributions[target]-base.contributions[target])>min_effect


def test_metric_rate_delta_is_exact_for_finite_nonlinear_scalar_metric(bg):
    # Independently recompute the COMPLETE ADM Kt/Kr kinetic expression
    # both before and after inserting the independent time-rate jets.
    t=.004;r=.16;a,b,ad,bd,nf,rhog,rhof=bg.at(t)
    x=np.array([.018,-.012,.023,-.014])
    pr=.019;er=-.028;k=1.7
    _,_,metric,area,_=sector_density(scale=b,scale_rate=bd,lapse=nf,
       rho0=rhof,amp=np.r_[x,[0.,0.]],t=t,r=r,time_radius=.027,
       radial_radius=.32,planck=MF2)
    T,Tr,F,Fr,Frr=profile(t,r,.027,.32)
    ph,u,s,e=x
    U=u*T*r*F;Ur=u*T*(F+r*Fr)
    psi=s*T*F;psir=s*T*Fr
    E=e*T*r*r*F;Er=e*T*(2*r*F+r*r*Fr)
    qr=1+2*psi-2*k*k*E/3;qt=1+2*psi+k*k*E/3
    qrr=2*psir-2*k*k*Er/3;qtr=2*psir+k*k*Er/3
    Qrt0=2*s*Tr*F-2*k*k*e*Tr*r*r*F/3
    Qtt0=2*s*Tr*F+k*k*e*Tr*r*r*F/3
    deltaQr=2*pr*T*F-2*k*k*er*T*r*r*F/3
    deltaQt=2*pr*T*F+k*k*er*T*r*r*F/3
    g00,g01,g11=metric
    N=np.sqrt(-g00+g01*g01/g11)
    shift=g01/g11
    sr=nf/b*(Ur/qr-U*qrr/qr**2)
    Kr0=(bd/b+Qrt0/(2*qr)-sr-shift*qrr/(2*qr))/N
    Kt0=(bd/b+Qtt0/(2*qt)-shift*(1/r+qtr/(2*qt)))/N
    Kr1=(bd/b+(Qrt0+deltaQr)/(2*qr)-sr-shift*qrr/(2*qr))/N
    Kt1=(bd/b+(Qtt0+deltaQt)/(2*qt)-shift*(1/r+qtr/(2*qt)))/N
    independent=.5*MF2*N*np.sqrt(g11)*area*(
        (-4*Kr1*Kt1-2*Kt1**2)-(-4*Kr0*Kt0-2*Kt0**2))
    constructed=eh_rate_delta_density(scale=b,scale_rate=bd,
       background_lapse=nf,planck=MF2,original_metric_amp=x,
       psi_rate=pr,E_rate=er,t=t,r=r,time_radius=.027,radial_radius=.32)
    assert constructed==pytest.approx(independent,rel=2e-13,abs=1e-18)


def test_background_rate_analytic_quadrature_convergence(bg):
    a=analytic_background_rate_hessian(quadrature_order=20,trajectory=bg)
    b=analytic_background_rate_hessian(quadrature_order=32,trajectory=bg)
    np.testing.assert_allclose(a,b,rtol=3e-13,atol=4e-16)
    assert np.min(np.abs(np.diag(b)))>1e-12


def test_added_rates_do_not_change_dust_phase_pair_canonical_rank(bg):
    h=.02; z=np.zeros(18)
    def diff(pi,ri):
        x=z.copy();y=z.copy();x[pi]=h;y[ri]=h
        return (action(x+y,trajectory=bg).total-action(x-y,trajectory=bg).total
              -action(-x+y,trajectory=bg).total+action(-x-y,trajectory=bg).total)/(4*h*h)
    H=np.array([[diff(5,6),diff(5,13)],[diff(12,6),diff(12,13)]])
    np.testing.assert_allclose(H,analytic_canonical_pair_integrals(),atol=2e-13,rtol=3e-9)
    assert np.linalg.matrix_rank(H,tol=1e-8)==2


def test_new_metric_rates_do_not_break_existing_hr_cross(bg):
    h=.004
    def cross(rate_amp):
        z=np.zeros(18);z[14]=rate_amp;u=z.copy();v=z.copy();u[0]+=h;v[9]+=h
        # isolate coefficients about selected background metric-rate jet
        return (action(u+v-z,trajectory=bg).total-action(u-v+z,trajectory=bg).total
                -action(-u+v+z,trajectory=bg).total+action(3*z-u-v,trajectory=bg).total)/(4*h*h)
    # At rate_amp=0, the old HR cross is unchanged.
    val=cross(0.)
    assert val< -1.7e-4 and val> -2e-4


def test_metric_rate_delta_exact_zero_when_independent_rates_zero(bg):
    t=.006;r=.18;a,b,ad,bd,nf,rhog,rhof=bg.at(t)
    for x in (np.zeros(4),np.array([.02,-.01,.014,-.005])):
        d=eh_rate_delta_density(scale=a,scale_rate=ad,background_lapse=1.,
         planck=MG2,original_metric_amp=x,psi_rate=0.,E_rate=0.,t=t,r=r,
         time_radius=.027,radial_radius=.32)
        assert d==0.


def test_metric_rate_jet_first_variations_are_not_legal_compact_field_tadpoles(bg):
    # Pure rate jets are independent local derivatives, not time-integrated
    # variations of psi or E. Nonzero linear rates DO NOT refute on-shell.
    for i in (14,16):
        x=np.zeros(18);x[i]=.005
        y=-x
        d=(action(x,trajectory=bg).total-action(y,trajectory=bg).total)/.01
        assert abs(d)>1e-7


def test_rate_geometry_and_domain_guards(bg):
    with pytest.raises(ValueError):action(np.zeros(14),trajectory=bg)
    with pytest.raises(ValueError):action(np.zeros(18),trajectory=bg,quadrature_order=8)
    with pytest.raises(ValueError):eh_rate_delta_density(scale=1.,scale_rate=.1,background_lapse=1.,
        planck=1.,original_metric_amp=np.zeros(4),psi_rate=0.,E_rate=0.,
        t=0.,r=0.,time_radius=.027,radial_radius=.32)
    with pytest.raises(ValueError):extra_rate_hessian(step=0,trajectory=bg)
