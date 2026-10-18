"""Full EH_g+EH_f+HR+two irrotational dust terms share identical metrics."""
import numpy as np
import pytest
from numerics.hr_unified_spacetime_offshell import (
    unified_spacetime_action,native_geometry_and_densities,
    _background,CONTRIBUTIONS,
)
from numerics.hr_coupled_diagonal_ward import (
    coupled_hr_spacetime_action,_native_metric,
)
from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density


def test_five_components_are_nonzero_and_add_to_total():
    x=unified_spacetime_action(quadrature_order=36)
    assert x.components.shape==(5,)
    assert CONTRIBUTIONS==('EH_g','EH_f','HR','dust_g','dust_f')
    assert np.min(np.abs(x.components))>1e-5
    assert x.value==pytest.approx(sum(x.components),abs=1e-14)
    assert x.minimum_g_jacobian>0 and x.minimum_f_jacobian>0


def test_all_five_densities_share_same_metric_with_old_hr():
    for sector in ('g','f'):
        for T,R in ((.15,.28),(-.21,.47)):
            v=(.015,-.019,.011,-.012,.021,-.023)
            _,_,g=native_geometry_and_densities(T,R,sector,v)
            old=_native_metric(T,R,sector,v[:4])
            np.testing.assert_allclose(g,old,atol=4e-15,rtol=1e-14)


def test_our_hr_sector_agrees_with_previous_independent_full_action():
    cases=[('diagonal',0.,0.),('diagonal',.06,-.04),
           ('relative_f',.035,-.023),('relative_f',-.05,.03)]
    for mode,et,er in cases:
        r=unified_spacetime_action(mode=mode,eps_time=et,
                           eps_radial=er,quadrature_order=40)
        old=coupled_hr_spacetime_action(mode=mode,eps_time=et,
                      eps_radial=er,quadrature_order=40)
        assert r.components[2]==pytest.approx(.7*old,abs=5e-14)


def test_native_eh_both_sectors_match_existing_flat_adm_exactly():
    for sector in ('g','f'):
        for T,R in ((.07,.23),(-.1,.4)):
            p=(.043,-.026,0.,0.,.027,.01)
            eh,_,_=native_geometry_and_densities(T,R,sector,p,planck=1.7)
            n,a,ad,_,_=_background(T,sector)
            phi=p[0]*(1+.17*T+(.07+.02*T)*R*R)
            U=p[1]*R*(1+.11*T+.07*R*R)
            Ur=p[1]*(1+.11*T+.21*R*R)
            expected=.5*1.7*flat_spherical_adm_eh_density(
                scale_factor=a,scale_rate=ad,background_lapse=n,
                r=R,Phi=phi,shift=U,shift_r=Ur)
            assert eh==pytest.approx(expected,rel=2e-13,abs=2e-14)


def test_full_five_sector_diagonal_chart_ward():
    reference=unified_spacetime_action(quadrature_order=44)
    for et,er in ((.05,0.),(-.04,0.),(0.,.048),(0.,-.045),(.06,-.04)):
        p=unified_spacetime_action(mode='diagonal',eps_time=et,
                                  eps_radial=er,quadrature_order=44)
        np.testing.assert_allclose(p.components,reference.components,
                                   rtol=0,atol=3e-13)
        assert p.value==pytest.approx(reference.value,abs=3e-13)


def test_relative_f_chart_changes_only_beta123_interaction():
    ref=unified_spacetime_action(quadrature_order=44)
    for et,er in ((.05,0.),(0.,-.045),(.035,-.023)):
        moved=unified_spacetime_action(mode='relative_f',eps_time=et,
                       eps_radial=er,quadrature_order=44)
        np.testing.assert_allclose(moved.components[[0,1,3,4]],
                    ref.components[[0,1,3,4]],atol=4e-13,rtol=0)
        assert abs(moved.components[2]-ref.components[2])>1e-7
        assert moved.value-ref.value==pytest.approx(
                     moved.components[2]-ref.components[2],abs=2e-13)


def test_beta0_beta4_f_relative_chart_is_individually_invariant():
    for i in (0,4):
        b=tuple(float(k==i) for k in range(5))
        original=unified_spacetime_action(betas=b)
        moved=unified_spacetime_action(betas=b,mode='relative_f',
                              eps_time=.05,eps_radial=-.04)
        np.testing.assert_allclose(moved.components,original.components,atol=3e-13,rtol=0)


def test_two_covariant_dust_backgrounds_conserved_native_and_norm_one():
    for s in ('g','f'):
        T=np.array([-.31,.02,.22]); R=np.array([.11,.24,.39])
        n,a,ad,_,const=_background(T,s)
        metric=_native_metric(T,R,s,np.zeros(4))
        rho=const/a**3
        assert rho*a**3==pytest.approx(np.full_like(T,const),abs=1e-14)
        inverse_norm=(metric[2]*n*n)/(metric[0]*metric[2]-metric[1]**2)
        np.testing.assert_allclose(inverse_norm,-1,rtol=0,atol=3e-15)
        eh,dust,mm=native_geometry_and_densities(T,R,s,np.zeros(6))
        np.testing.assert_allclose(dust,0.,rtol=0,atol=3e-15)


def test_nontrivial_dust_phase_and_density_affect_action():
    base=unified_spacetime_action()
    # An independent phase/multiplier pair is varied in EACH native sector.
    g=unified_spacetime_action(fields_g=(.012,-.014,.016,.009,.04,.08))
    f=unified_spacetime_action(fields_f=(-.017,.013,-.011,.008,.05,-.06))
    assert np.linalg.norm(g.components[[0,1,2,4]]-base.components[[0,1,2,4]])<1e-12
    assert np.linalg.norm(f.components[[0,1,2,3]]-base.components[[0,1,2,3]])<1e-12
    assert abs(g.components[3]-base.components[3])>1e-5
    assert abs(f.components[4]-base.components[4])>1e-5


def test_hr_mass_zero_retains_both_eh_and_two_dust():
    z=unified_spacetime_action(hr_mass2=0.)
    assert z.components[2]==0.
    assert np.linalg.norm(z.components[[0,1,3,4]])>0.1
    assert np.min(np.abs(z.components[[0,1,3,4]]))>1e-5


def test_native_quadrature_refinement_five_components():
    lo=unified_spacetime_action(quadrature_order=28)
    hi=unified_spacetime_action(quadrature_order=48)
    np.testing.assert_allclose(lo.components,hi.components,rtol=2e-10,atol=3e-13)


def test_full_action_offshell_gravitational_tadpoles_not_zero():
    h=1e-4
    def f(e):
        return unified_spacetime_action(fields_g=(.012+e,-.014,.016,.009,.025,-.017),quadrature_order=36).value
    deriv=(f(h)-f(-h))/(2*h)
    assert abs(deriv)>1e-4 # no on-shell physical constraint is claimed


def test_unified_positivity_and_domain_guards():
    kw=[{'betas':(1,2,3)}, {'mode':'invalid'},
        {'planck_f':-.1}, {'planck_g':0}, {'hr_mass2':-1},
        {'eps_time':float('nan')}, {'fields_g':(0,)*5},
        {'fields_f':(0,)*5}, {'quadrature_order':4},
        {'eps_radial':10.}, {'fields_f':(-10,0,0,0,0,0)},
        {'fields_g':(0,0,0,0,0,-100)}]
    for x in kw:
        with pytest.raises(ValueError):unified_spacetime_action(**x)
