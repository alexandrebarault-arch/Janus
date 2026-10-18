"""Exact coupled HR diagonal Ward and relative-chart controls."""
import numpy as np
import pytest
from numerics.hr_coupled_diagonal_ward import (
    BETAS, _native_chart, _native_metric, _pull, _interaction_density,
    coupled_hr_spacetime_action, diagonal_and_relative_ward,
)
from numerics.hr_native_stueckelberg_jet import native_hr_stueckelberg_jet


def test_full_nonhomothetic_coupled_hr_diagonal_invariance_with_metric_fields():
    out=diagonal_and_relative_ward(order=44)
    assert np.max(np.abs(out.diagonal_variations))<3e-12
    assert np.min(np.abs(out.relative_variations))>5e-7


def test_all_five_single_beta_diagonal_ward():
    for k in range(5):
        betas=tuple(float(j==k) for j in range(5))
        out=diagonal_and_relative_ward(betas=betas,order=40)
        np.testing.assert_allclose(out.diagonal_variations,0.,atol=3e-12)
        if k in (0,4):
            np.testing.assert_allclose(out.relative_variations,0.,atol=3e-12)
        else:
            assert np.min(np.abs(out.relative_variations))>1e-6


def test_beta0_and_beta4_independent_relative_coordinate_volume_witness():
    for betas in ((1.,0.,0.,0.,0.),(0.,0.,0.,0.,1.)):
        value=coupled_hr_spacetime_action(betas=betas)
        for epsT,epsR in ((.06,0.),(-.05,0.),(0.,.055),(0.,-.05),(.065,-.04)):
            displaced=coupled_hr_spacetime_action(betas=betas,mode='relative_f',
                    eps_time=epsT,eps_radial=epsR)
            assert displaced==pytest.approx(value,abs=2e-12)


def test_exact_diagonal_invariance_with_stronger_fields_and_chart():
    params=dict(g_fields=(.045,-.033,.037,.021),
                f_fields=(-.031,.029,-.027,.019),quadrature_order=46)
    base=coupled_hr_spacetime_action(**params)
    for eT,eR in ((.06,0.),(-.065,0.),(0.,.058),(0.,-.06),(.07,-.06)):
        diag=coupled_hr_spacetime_action(eps_time=eT,eps_radial=eR,**params)
        assert diag==pytest.approx(base,abs=3e-12)


def test_interaction_linear_in_five_betas_under_diagonal_and_relative_charts():
    betas=(.14,.61,-.23,.16,.19)
    for mode,et,er in (('diagonal',.03,-.025),('relative_f',.025,-.03)):
        together=coupled_hr_spacetime_action(betas=betas,mode=mode,
                     eps_time=et,eps_radial=er,quadrature_order=36)
        parts=sum(betas[i]*coupled_hr_spacetime_action(
                    betas=tuple(float(j==i) for j in range(5)),mode=mode,
                    eps_time=et,eps_radial=er,quadrature_order=36)
                  for i in range(5))
        assert together==pytest.approx(parts,abs=3e-13)


def test_native_hr_exact_density_matches_previous_exact_stueckelberg_jet():
    # Old local HR oracle uses the algebraic 2x2 principal square root,
    # independent from our new explicit two-metric/determinant computation.
    for r in (.12,.23,.39):
        t=0.
        T,R,Tt,Tr,Rt,Rr=_native_chart(t,r)
        g=_native_metric(t,r,'g',(0.,0.,0.,0.))
        f=_pull(_native_metric(T,R,'f',(0.,0.,0.,0.)),Tt,Tr,Rt,Rr)
        direct=float(_interaction_density(g,f,BETAS))
        jet=native_hr_stueckelberg_jet(
            N=1.04,a=.95,n=1.13,alpha=.87,k=1.6,m2=1.,Mg2=1.,
            betas=BETAS,mu=-.22,r=r,sigma_r=.08,sigma_dot=.025,
            mu_dot=.05,n_dot=.045,alpha_dot=.09,
            n_ddot=.024,alpha_ddot=.05)
        assert direct==pytest.approx(r*r*jet.value,rel=3e-14,abs=3e-15)


def test_quadrature_refinement_stabilizes_diagonal_and_relative_actions():
    a=diagonal_and_relative_ward(order=30)
    b=diagonal_and_relative_ward(order=48)
    assert a.baseline==pytest.approx(b.baseline,abs=4e-12)
    np.testing.assert_allclose(a.relative_variations,b.relative_variations,atol=8e-12)
    np.testing.assert_allclose(b.diagonal_variations,0.,atol=4e-12)


def test_zero_interaction_and_input_guards():
    assert coupled_hr_spacetime_action(betas=(0,0,0,0,0))==pytest.approx(0,abs=1e-15)
    with pytest.raises(ValueError):coupled_hr_spacetime_action(betas=(1,2,3,4))
    with pytest.raises(ValueError):coupled_hr_spacetime_action(mode='invalid')
    with pytest.raises(ValueError):coupled_hr_spacetime_action(eps_time=float('nan'))
    with pytest.raises(ValueError):coupled_hr_spacetime_action(eps_radial=10.)
    with pytest.raises(ValueError):coupled_hr_spacetime_action(time_radius=-.1)
    with pytest.raises(ValueError):coupled_hr_spacetime_action(quadrature_order=5)
    with pytest.raises(ValueError):coupled_hr_spacetime_action(g_fields=(.01,.01))
    with pytest.raises(ValueError):coupled_hr_spacetime_action(f_fields=(-8,0,0,0))
