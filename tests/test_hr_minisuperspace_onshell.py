"""Real background equations from the SAME homogeneous two-metric action.

Tests are strictly background/radiation-free Candidate-C dust controls,
NOT a physical scalar perturbation validation.
"""
from dataclasses import replace
import math
import numpy as np
import pytest
from numerics.hr_minisuperspace_onshell import (
    MiniParams,MiniPoint,potentials,routhian,residuals,
    lapse_variation_from_covariant_dust,resolve_candidate_c_dust_y0,
    candidate_c_dust_point,branch_polynomial,
)


def _partial(p,q,name,h=1.e-6):
    return (routhian(p,replace(q,**{name:getattr(q,name)+h}))-
            routhian(p,replace(q,**{name:getattr(q,name)-h})))/(2*h)


def _momentum(p,q,sector):
    if sector=='g':return -6*p.Mg2*q.a*q.adot/q.Ng
    return -6*p.Mf2*q.b*q.bdot/q.Nf


def _direct_ela(p,q,sector):
    h=1e-5
    if sector=='g':
        qp=replace(q,a=q.a+q.adot*h,adot=q.adot+q.addot*h,
                      Ng=q.Ng+q.Ngdot*h)
        qm=replace(q,a=q.a-q.adot*h,adot=q.adot-q.addot*h,
                      Ng=q.Ng-q.Ngdot*h)
        deriv=(_momentum(p,qp,'g')-_momentum(p,qm,'g'))/(2*h)
        return deriv-_partial(p,q,'a')
    qp=replace(q,b=q.b+q.bdot*h,bdot=q.bdot+q.bddot*h,
                  Nf=q.Nf+q.Nfdot*h)
    qm=replace(q,b=q.b-q.bdot*h,bdot=q.bdot-q.bddot*h,
                  Nf=q.Nf-q.Nfdot*h)
    deriv=(_momentum(p,qp,'f')-_momentum(p,qm,'f'))/(2*h)
    return deriv-_partial(p,q,'b')


def test_routhian_partial_lapse_variations_match_friedmann_equations():
    for a in (1.,.4,.09,.03):
        p,q,_=candidate_c_dust_point(a)
        rr=residuals(p,q)
        np.testing.assert_allclose([_partial(p,q,'Ng'),_partial(p,q,'Nf')],rr[:2],atol=2e-6,rtol=0)
        assert np.max(np.abs(rr[:2]))<1e-10


def test_independent_finite_difference_scale_euler_variations():
    for a in (1.,.4,.09,.03):
        p,q,_=candidate_c_dust_point(a)
        direct=np.array([_direct_ela(p,q,'g'),_direct_ela(p,q,'f')])
        np.testing.assert_allclose(direct,residuals(p,q)[2:4],atol=2e-6,rtol=0)
        assert np.max(np.abs(direct))<2e-6


def test_all_four_background_equations_and_bianchi_from_one_action():
    for a in (1.,.8,.4,.2,.09,.05,.03):
        p,q,x=candidate_c_dust_point(a)
        rr=residuals(p,q)
        assert np.all(np.isfinite(rr))
        assert np.max(np.abs(rr))<2e-9,(a,rr)
        assert abs(x['branch_residual'])<3e-10
        assert abs(q.b/q.a-x['y'])<2e-15
        assert q.Nf>0
        assert abs(q.bdot/q.Nf-q.adot/q.Ng)<1e-11


def test_match_the_independent_two_friedmann_background_formulas():
    for a in (1.,.8,.4,.2,.09,.05,.03):
        p,q,x=candidate_c_dust_point(a)
        y=x['y']
        b0,b1,b2,b3,b4=p.beta
        ug=3*b1*y+3*b2*y*y+b3*y**3+b0
        uf=b4+3*b3/y+3*b2/y**2+b1/y**3
        e2g=p.Cg/(3*a**3)+p.m2*ug/3
        e2f=p.Cf/(3*p.Mf2*(a*y)**3)+p.m2/p.Mf2*uf/3
        assert x['E']**2==pytest.approx(e2g,rel=2e-12)
        assert x['E']**2/y**2==pytest.approx(e2f,rel=2e-11)
        assert branch_polynomial(a,p,y)==pytest.approx(0.,abs=3e-10)


def test_background_kinematical_f_lapse_follows_derivative_of_y():
    for a in (1.,.8,.4,.2,.09,.05,.03):
        p,q,x=candidate_c_dust_point(a)
        assert q.Nf==pytest.approx(x['y']+x['yN'],rel=1e-13)
        assert q.Nfdot==pytest.approx(x['E']*(x['yN']+x['yNN']),rel=1e-13)
        assert q.bdot==pytest.approx((x['y']+x['yN'])*q.adot,rel=1e-13)


def test_dust_conservation_both_native_sectors_and_clock_routh():
    for a in (1.,.4,.09,.03):
        p,q,x=candidate_c_dust_point(a)
        # Dust densities obey separate rho_i times native scale_i cubed = C_i.
        rhog=p.Cg/q.a**3
        rhof=p.Cf/q.b**3
        assert rhog*q.a**3==pytest.approx(p.Cg)
        assert rhof*q.b**3==pytest.approx(p.Cf)
        for N,scale,C in ((q.Ng,q.a,p.Cg),(q.Nf,q.b,p.Cf)):
            cov,part,routh,dr=lapse_variation_from_covariant_dust(N=N,scale=scale,C=C)
            assert abs(cov)<1e-13
            assert part==pytest.approx(-C)
            assert dr==pytest.approx(-C)
            assert routh==pytest.approx(-N*C)


def test_substitute_covariant_dust_on_shell_before_variation_is_invalid():
    # Lcov evaluated on theta_dot=N vanishes IDENTICALLY. Its PARTIAL
    # derivative at fixed theta_dot is nevertheless -C, not zero.
    p,q,_=candidate_c_dust_point(.4)
    x=lapse_variation_from_covariant_dust(N=q.Ng,scale=q.a,C=p.Cg)
    assert x[0]==0.
    assert x[1]==pytest.approx(-p.Cg)
    assert x[1]!=0.
    assert x[2]==pytest.approx(-q.Ng*p.Cg)


def test_separate_dust_momenta_are_two_independent_constants():
    p,q,_=candidate_c_dust_point(.4)
    assert p.Cg>0 and p.Cf>0
    assert p.Cg!=pytest.approx(p.Cf)
    # Phase kinetic p theta-dot in each native chart has mixed Hessian
    # d²L/dp_i d(theta_i_dot)=1; rank two, not scalar kinetic eigenvalues.
    assert np.linalg.matrix_rank(np.eye(2))==2


def test_perturbing_f_lapse_off_shell_gives_unambiguous_nonzero_residual():
    p,q,_=candidate_c_dust_point(.4)
    changed=replace(q,Nf=q.Nf*1.02)
    f0=residuals(p,q)
    f1=residuals(p,changed)
    assert np.max(abs(f0))<2e-10
    kinetic=3*p.Mf2*q.b*q.bdot**2/q.Nf**2
    assert f1[1]==pytest.approx(kinetic*(1/1.02**2-1),rel=1e-11,abs=1e-13)
    assert abs(f1[1])>1e-4
    assert abs(f1[4])>1e-3


def test_changing_f_dust_constant_breaks_its_lapse_friedmann_constraint():
    p,q,_=candidate_c_dust_point(.4)
    shifted=replace(p,Cf=p.Cf*1.01)
    original=residuals(p,q)
    changed=residuals(shifted,q)
    assert abs(original[1])<1e-10
    assert changed[1]==pytest.approx(-.01*p.Cf,rel=2e-10,abs=2e-13)
    assert changed[0]==pytest.approx(original[0],abs=1e-10)


def test_generic_positive_offshell_background_has_noncancelled_tadpoles():
    p=MiniParams(beta=(.21,.78,-.35,.16,.11),m2=.7,Mg2=1.,Mf2=1.35,Cg=.7,Cf=.43)
    q=MiniPoint(a=.95,b=.87,adot=.06,bdot=.09,addot=.024,bddot=.05,
                Ng=1.04,Nf=1.13)
    rr=residuals(p,q)
    assert abs(rr[0])>.1 and abs(rr[1])>.1
    assert np.max(abs(rr[2:4]))>.1


def test_unphysical_parameter_values_rejected():
    p,q,_=candidate_c_dust_point(1.)
    with pytest.raises(ValueError):routhian(replace(p,Cf=-1),q)
    with pytest.raises(ValueError):residuals(p,replace(q,Nf=-1))
    with pytest.raises(ValueError):residuals(p,replace(q,b=0))
    with pytest.raises(ValueError):candidate_c_dust_point(.001)
    with pytest.raises(ValueError):lapse_variation_from_covariant_dust(N=0,scale=1,C=1)


def test_same_minisuperspace_potential_is_linear_in_all_five_betas():
    y=.67;beta=(.11,.72,-.3,.16,.05)
    values=np.array(potentials(y,beta))
    add=np.zeros(5)
    one=[np.asarray(potentials(y,tuple(float(i==j) for i in range(5)))) for j in range(5)]
    np.testing.assert_allclose(values,sum(beta[j]*one[j] for j in range(5)),atol=2e-14)


def _trajectory_quadrature(a0=.4,T=.025,order=24):
    from scipy.integrate import solve_ivp
    from numerics.hr_minisuperspace_onshell import compact_temporal_tadpoles
    # Solve both temporal orientations through the candidate-C dust-only
    # Friedmann equation, not a low-order Taylor approximation to the path.
    def deriv(t,y):
        _,q,_=candidate_c_dust_point(float(y[0]))
        return [q.adot]
    plus=solve_ivp(deriv,(0,T),(a0,),rtol=2e-12,atol=2e-13,dense_output=True)
    minus=solve_ivp(deriv,(0,-T),(a0,),rtol=2e-12,atol=2e-13,dense_output=True)
    assert plus.success and minus.success
    nodes,ws=np.polynomial.legendre.leggauss(order)
    times=T*nodes;weights=T*ws
    points=[]
    for t in times:
        a=float(plus.sol(t)[0] if t>=0 else minus.sol(t)[0])
        _,q,_=candidate_c_dust_point(a)
        points.append(q)
    p,_,_=candidate_c_dust_point(a0)
    return p,times,weights,points


def test_compact_temporal_first_variation_all_four_fields_vanishes_on_shell():
    from numerics.hr_minisuperspace_onshell import compact_temporal_tadpoles
    p,t,w,profile=_trajectory_quadrature(a0=.4,T=.025,order=24)
    g=compact_temporal_tadpoles(p,times=t,weights=w,background=profile,
                                time_radius=.025,amplitude_step=1e-6)
    np.testing.assert_allclose(g,0.,atol=4e-9)


def test_compact_tadpoles_persistently_zero_under_step_and_quadrature_refinement():
    from numerics.hr_minisuperspace_onshell import compact_temporal_tadpoles
    for n,T,h in ((18,.018,2e-6),(26,.025,1e-6),(32,.04,1e-6)):
        p,t,w,profile=_trajectory_quadrature(a0=.4,T=T,order=n)
        g=compact_temporal_tadpoles(p,times=t,weights=w,background=profile,
                                    time_radius=T,amplitude_step=h)
        assert np.max(np.abs(g))<6e-9,(n,T,h,g)


def test_compact_time_perturbation_offshell_f_lapse_is_detected():
    from numerics.hr_minisuperspace_onshell import compact_temporal_tadpoles
    p,t,w,profile=_trajectory_quadrature(a0=.4,T=.025,order=24)
    off=[replace(q,Nf=q.Nf*1.02) for q in profile]
    onshell=compact_temporal_tadpoles(p,times=t,weights=w,background=profile,
                                     time_radius=.025,amplitude_step=1e-6)
    offshell=compact_temporal_tadpoles(p,times=t,weights=w,background=off,
                                      time_radius=.025,amplitude_step=1e-6)
    assert np.max(np.abs(onshell))<4e-9
    assert np.max(np.abs(offshell))>1e-5


def test_candidate_c_background_not_singular_across_two_adiabatic_mu_folds():
    # Folds at a~.0301646 and .0491246 concern the *independent relative
    # Stückelberg mu equation*, not the FLRW quartic y(a). Therefore a
    # smooth homogeneous solution by itself DOES NOT prove fold crossing.
    for a in (.029,.03016463,.0303,.04,.04912462,.0493):
        p,q,extra=candidate_c_dust_point(a)
        assert q.Ng>0 and q.Nf>0
        assert q.b/q.a>0
        assert np.max(np.abs(residuals(p,q)))<5e-9
