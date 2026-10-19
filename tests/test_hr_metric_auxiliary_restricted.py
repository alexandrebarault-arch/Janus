"""Step 32c: restricted Galerkin Schur, never physical BD or ghost inference."""
import numpy as np
import pytest
from numerics.hr_full_onshell_tadpole import Trajectory,profile
from numerics.hr_metric_auxiliary_restricted import (
    AUXILIARY_INDICES,RETAINED_INDICES,restricted_auxiliary_schur,
    restricted_quadratic_residuals,hessian_and_gradient,
)
from numerics.hr_common_time_metric_rates import (
    analytic_background_rate_hessian,analytic_background_rate_hessian as oracle,
    action,
)
from numerics.hr_two_dust_common_time_canonical import analytic_canonical_pair_integrals

@pytest.fixture(scope='module')
def bg():return Trajectory.solve(width=.04)

@pytest.fixture(scope='module')
def result(bg):return restricted_auxiliary_schur(trajectory=bg,quadrature_order=20)


def test_full_common_action_symmetric_18x18_and_positive_auxiliary_rank(result):
    H=result.hessian
    assert H.shape==(18,18)
    np.testing.assert_allclose(H,H.T,rtol=0,atol=0)
    assert tuple(AUXILIARY_INDICES)==(0,1,7,8)
    assert len(RETAINED_INDICES)==14
    assert result.auxiliary_rank==4
    assert 400<result.condition<800
    vals=np.linalg.eigvalsh(result.auxiliary)
    assert np.count_nonzero(vals<0)==2
    assert np.count_nonzero(vals>0)==2
    # No physical positivity interpretation of the AUXILIARY signature.


def test_auxiliary_gradient_tadpoles_use_accurate_separate_finite_step(result):
    # The background solves its equations: the four legal first variations
    # must vanish with a small first-difference step, not the Hessian step.
    assert np.max(np.abs(result.gradient[list(AUXILIARY_INDICES)]))<3e-10
    # Independent metric RATE jets aren't legal compact fields; at least
    # one of their raw gradients can be nonzero without an Euler tadpole.
    assert np.max(np.abs(result.gradient[14:18]))>1e-8


def test_restricted_schur_is_exact_quadratic_stationary_elimination(result):
    rng=np.random.default_rng(20261019)
    for y in (rng.normal(size=14)*.001,
              np.r_[np.zeros(10), [.002,-.001,-.003,.004]],
              np.linspace(-.0003,.0004,14)):
        whole,q18,q14,source=restricted_quadratic_residuals(result,y)
        assert abs(q18-q14)<1e-17
        np.testing.assert_allclose(source,0.,atol=1e-17)
        np.testing.assert_allclose(result.auxiliary@whole[list(AUXILIARY_INDICES)]
                                   +result.mixed@whole[list(RETAINED_INDICES)],
                                   0.,atol=1e-17)


def test_restricted_schur_agrees_with_independent_block_inverse(result):
    H=result.hessian
    a=np.array(AUXILIARY_INDICES);p=np.array(RETAINED_INDICES)
    A=H[np.ix_(a,a)]; B=H[np.ix_(a,p)]; C=H[np.ix_(p,p)]
    independent=C-B.T@np.linalg.inv(A)@B
    np.testing.assert_allclose(result.schur,independent,atol=3e-13,rtol=2e-11)
    np.testing.assert_allclose(result.schur,result.schur.T,atol=1e-15)


def test_two_dust_canonical_pairs_preserved_after_restricted_schur(result):
    expected=analytic_canonical_pair_integrals()
    np.testing.assert_allclose(result.symplectic,expected,rtol=5e-7,atol=2e-12)
    assert np.linalg.matrix_rank(result.symplectic,tol=1e-8)==2
    # The original fully coupled Hessian has no auxiliary--phase RATE cross:
    # Schur cannot eliminate the two canonical p-theta_dot pairs.
    np.testing.assert_allclose(result.hessian[np.ix_(AUXILIARY_INDICES,[6,13])],0.,atol=5e-14)
    # Distinct scalar momentum/rate channels survive intact.
    idx={v:i for i,v in enumerate(RETAINED_INDICES)}
    for mom,rate in ((5,6),(12,13)):
        assert result.schur[idx[mom],idx[rate]]>1e-6


def test_four_independent_eh_metric_rates_match_external_closed_form(result,bg):
    target=analytic_background_rate_hessian(quadrature_order=20,trajectory=bg)
    np.testing.assert_allclose(result.hessian[14:18,14:18],target,atol=1e-14,rtol=1e-4)
    assert target[0,0]<0 and target[2,2]<0
    assert target[1,1]>0 and target[3,3]>0
    # These are preconstraint configuration-velocity jets, NOT physical ghosts.


def test_auxiliary_quadrature_refinement_robust(bg,result):
    low=restricted_auxiliary_schur(trajectory=bg,quadrature_order=12)
    np.testing.assert_allclose(result.auxiliary,low.auxiliary,atol=3e-12,rtol=1e-6)
    assert abs(result.condition-low.condition)<.004
    np.testing.assert_allclose(result.symplectic,low.symplectic,atol=2e-12)


def test_auxiliary_hessian_finite_difference_step_robust(bg,result):
    lower=restricted_auxiliary_schur(trajectory=bg,quadrature_order=20,step=.008)
    np.testing.assert_allclose(result.auxiliary,lower.auxiliary,atol=6e-8,rtol=3e-4)
    assert abs(result.condition-lower.condition)<.06
    np.testing.assert_allclose(result.symplectic,lower.symplectic,atol=3e-12)


def test_restricting_trial_basis_prevents_claim_of_full_adm_constraints(bg,result):
    # The step32b rate jets are independent local probes with time profile
    # T(t)F(r), while the actual derivative of parent perturbation T(t)F(r)
    # is T'(t)F(r). At t=0, T'=0 but T is positive, so no jet closure.
    T,Tr,F,Fr,Frr=profile(0.,.12,.027,.32)
    assert Tr==0.
    assert T*F>.1
    assert abs(Tr*F)<1e-15
    # An on-shell Ward/gauge analysis must close the temporal derivatives
    # before interpreting the Schur matrix as reduced physical kinetic.


def test_invalid_auxiliary_quadratic_coordinates_and_guard(bg,result):
    with pytest.raises(ValueError):restricted_quadratic_residuals(result,np.zeros(13))
    with pytest.raises(ValueError):restricted_quadratic_residuals(result,np.full(14,np.nan))
    with pytest.raises(ValueError):restricted_auxiliary_schur(trajectory=bg,step=0.)
    with pytest.raises(ValueError):restricted_auxiliary_schur(trajectory=bg,gradient_step=0.)
    with pytest.raises(ValueError):restricted_auxiliary_schur(trajectory=bg,quadrature_order=5)
    with pytest.raises(ValueError):restricted_auxiliary_schur(trajectory=bg,max_condition=1.)
    with pytest.raises(np.linalg.LinAlgError):restricted_auxiliary_schur(trajectory=bg,max_condition=2.)


def test_schur_directional_curvature_against_nonlin_action_second_difference(bg,result):
    # Independent nonlinear full-action evaluation along a constrained
    # *TRIAL* direction.  A finite-difference Schur H is NOT an exact
    # physical canonical constraint or on-shell reduced scalar operator.
    y=np.zeros(14);y[2]=1.  # theta_g is a legal compact phase field
    z,_,q_schur,src=restricted_quadratic_residuals(result,y)
    h=.0005
    f0=action(trajectory=bg,quadrature_order=20).total
    fp=action(h*z,trajectory=bg,quadrature_order=20).total
    fm=action(-h*z,trajectory=bg,quadrature_order=20).total
    actual=(fp+fm-2*f0)/h**2
    assert actual<0
    assert actual==pytest.approx(2*q_schur,rel=.007,abs=2e-7)
