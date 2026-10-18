"""Off-shell diagonal Ward: null directional quadratic vs Hessian kernel."""
import numpy as np
import pytest
from numerics.hr_coupled_chart_hessian import (
    coupled_hr_independent_chart_action,
    coupled_hr_independent_chart_hessian,ORDER,
)
from numerics.hr_coupled_diagonal_ward import coupled_hr_spacetime_action


def test_independent_chart_diagonal_matches_and_relative_maps_differ():
    for et,er in ((.04,0.),(0.,-.035),(.037,-.02)):
        diag=coupled_hr_independent_chart_action(chart=(et,er,et,er))
        fonly=coupled_hr_independent_chart_action(chart=(0.,0.,et,er))
        assert diag==pytest.approx(coupled_hr_spacetime_action(
            mode='diagonal',eps_time=et,eps_radial=er,
            quadrature_order=38),abs=2e-13)
        # f-only common-chart displacement is NOT the same as a native
        # delta(T,R): the two are related by the nonhomothetic Jacobian J0.
        # Deliberately distinguish them to prevent mixing chart profiles.
        native_relative=coupled_hr_spacetime_action(
            mode='relative_f',eps_time=et,eps_radial=er,
            quadrature_order=38)
        assert abs(fonly-native_relative)>1e-10


def test_exact_diagonal_paths_have_zero_first_second_action_variations():
    origin=coupled_hr_independent_chart_action()
    for h in (.04,.02,-.06):
        for g in ((1.,0.,1.,0.),(0.,1.,0.,1.),(1.,-.7,1.,-.7)):
            v=h*np.array(g)
            assert coupled_hr_independent_chart_action(chart=v)==pytest.approx(origin,abs=3e-13)
            assert coupled_hr_independent_chart_action(chart=-v)==pytest.approx(origin,abs=3e-13)


def test_offshell_independent_chart_hessian_is_not_spurious_gauge_kernel():
    x=coupled_hr_independent_chart_hessian(step=.0015)
    assert ORDER==('g_time_chart','g_radial_chart','f_time_chart','f_radial_chart')
    np.testing.assert_allclose(x.hessian,x.hessian.T,atol=2e-14)
    ut=np.array([1.,0.,1.,0.])
    ur=np.array([0.,1.,0.,1.])
    # Direct directional identity holds exactly, while componentwise centered
    # Hessian incurs O(h²) finite differences for higher chart derivatives.
    assert abs(ut@x.hessian@ut)<2e-6
    assert abs(ur@x.hessian@ur)<2e-8
    assert abs(x.gradient@ut)<5e-9
    assert abs(x.gradient@ur)<5e-9
    # The OFF-SHELL mixed Hessian need NOT annihilate the diagonal vector:
    # Ward: S_,ij R^j = -S_,j R^j_,i. On-shell tadpoles are necessary
    # before declaring the true constrained gauge null eigendirections.
    assert np.linalg.norm(x.hessian@ut)>1e-4
    assert np.linalg.norm(x.hessian@ur)>1e-4


def test_diagonal_direction_finite_step_truncation_scales_quadratically():
    u=np.array([1.,0.,1.,0.])
    h1=coupled_hr_independent_chart_hessian(step=.006)
    h2=coupled_hr_independent_chart_hessian(step=.003)
    d1=abs(u@h1.hessian@u)
    d2=abs(u@h2.hessian@u)
    assert d1/5<d2<d1/3  # O(step²), not a physical small mass
    assert abs(h2.gradient@u)<abs(h1.gradient@u)/3


def test_beta0_beta4_no_relative_chart_dynamics_as_f_only_controls():
    for k in (0,4):
        betas=tuple(float(i==k) for i in range(5))
        base=coupled_hr_independent_chart_action(betas=betas)
        for h in ((0,0,.055,0),(0,0,0,-.048)):
            assert coupled_hr_independent_chart_action(betas=betas,chart=h)==pytest.approx(base,abs=2e-13)
    # With beta0 alone, the f chart has zero gradient and Hessian.
    beta0=coupled_hr_independent_chart_hessian(betas=(1,0,0,0,0),step=.002)
    assert np.max(abs(beta0.hessian[2:,:]))<1e-9
    assert np.max(abs(beta0.gradient[2:]))<1e-9
    # With beta4 alone, the g chart is decoupled instead.
    beta4=coupled_hr_independent_chart_hessian(betas=(0,0,0,0,1),step=.002)
    assert np.max(abs(beta4.hessian[:2,:]))<1e-9
    assert np.max(abs(beta4.gradient[:2]))<1e-9


def test_separate_metric_chart_gradient_contributions_cancel_at_first_order():
    h=.0015
    out=coupled_hr_independent_chart_hessian(step=h)
    np.testing.assert_allclose(out.gradient[:2],-out.gradient[2:],atol=2e-9,rtol=2e-6)
    assert np.linalg.norm(out.gradient[:2])>1e-4


def test_hessian_quadrature_stability_for_nonzero_relative_blocks():
    lo=coupled_hr_independent_chart_hessian(step=.003,quadrature_order=30)
    hi=coupled_hr_independent_chart_hessian(step=.003,quadrature_order=46)
    np.testing.assert_allclose(lo.hessian,hi.hessian,atol=4e-9,rtol=2e-7)
    np.testing.assert_allclose(lo.gradient,hi.gradient,atol=1e-10,rtol=2e-8)
    assert np.linalg.norm(hi.hessian[:2,2:])>.05


def test_invalid_chart_shape_and_step_rejected():
    with pytest.raises(ValueError):coupled_hr_independent_chart_action(chart=(0,0,0))
    with pytest.raises(ValueError):coupled_hr_independent_chart_action(chart=(0,0,float('inf'),0))
    with pytest.raises(ValueError):coupled_hr_independent_chart_action(chart=(10,0,0,0))
    with pytest.raises(ValueError):coupled_hr_independent_chart_hessian(step=0)
    with pytest.raises(ValueError):coupled_hr_independent_chart_hessian(step=float('nan'))
