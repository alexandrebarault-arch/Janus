"""Step37 restricted collocation gates, NOT full Dirac/ghost elimination."""
import numpy as np
import pytest
from numerics.hr_curved_moving_dust_primary import build_primary, BETA,M2,MG2,MF2
from numerics.hr_step37_curved_solver import kernel_fast, local_candidate, solve_even_center
from numerics.hr_step37_original_nonibp_oracle import original_pb


def curved(scale=.1,delta=()):
    return build_primary(curv_g=.015*scale,curv_f=-.012*scale,
        z_slope=.04*scale,theta_g=.012*scale,theta_f=-.016*scale,
        grav_g=0.,grav_f=0.,f_delta=tuple(delta))

@pytest.fixture(scope='module')
def solution():
    return solve_even_center(scale=.1,degree=4,iterations=5)


def test_historical_curved_full_kernel_regression():
    w=build_primary()
    k=kernel_fast(w,.43)
    np.testing.assert_allclose(k[0,0],.41113496513668346,atol=5e-12)
    np.testing.assert_allclose(k[0,1],-.008944371578075146,atol=5e-12)
    np.testing.assert_allclose(k[1,0],.11498513679744424,atol=5e-12)
    np.testing.assert_allclose(k[1,1],.026099594544177672,atol=5e-12)
    np.testing.assert_allclose(k[2,0],k[1,1],atol=1e-13)
    np.testing.assert_allclose(k[0,2],0.,atol=1e-13)
    assert local_candidate(w,.43,.005)[0]==pytest.approx(.47166555,abs=1e-6)


def test_mixed_derivative_ward_approaches_zero_quadratically():
    w=build_primary()
    _,a=local_candidate(w,.43,.008)
    _,b=local_candidate(w,.43,.004)
    assert abs(a)>abs(b)*3.7
    assert abs(a)<abs(b)*4.3


def test_flat_momentum_generator_is_not_pL_div_r2():
    a=.4;b=a*.5787707228025044
    J=BETA[1]+2*BETA[2]*b/a+BETA[3]*(b/a)**2
    A=.5*M2*MG2*a*a*J
    for n in (0,1,2,4):
        c=.0001
        dp=tuple([0.]*n+[c])
        w=curved(scale=0.,delta=dp)
        r=.43
        actual=local_candidate(w,r,.002)[0]
        # pLf/r² = 2/(n+2)* Qf_n*r^n: exact origin of the inverse factor.
        expected=-A*r*r*(n+3)*(2/(n+2))*c*r**n/(MF2*b)
        assert actual==pytest.approx(expected,rel=3e-9,abs=2e-12)


def test_even_parity_solver_has_no_free_odd_powers(solution):
    x=solution['history'][-1]['f_delta']
    assert len(x)==9
    assert np.all(np.array(x)[1::2]==0.)
    assert solution['verdict'].startswith('FINITE_RADIAL')


def test_constrained_positive_two_dust_primary_profile(solution):
    w=curved(delta=solution['history'][-1]['f_delta'])
    r=np.linspace(.04,.85,51)
    v=w.eval(r,('Hg','Hf','Ddiag','Fz','pg','pf','z','K','R3g','R3f'))
    assert np.max(np.abs(v[:4]))<8e-13
    assert min(v[4].min(),v[5].min())>0
    assert np.min(v[7])>0
    assert np.max(np.abs(v[6]))<.01
    assert np.min(np.abs(v[8]))>0 and np.min(np.abs(v[9]))>0


def test_explicit_iterated_secondary_residual_drops_five_orders(solution):
    rows=solution['history']
    assert len(rows)==6
    assert rows[0]['max_C']>.7
    assert rows[-1]['max_C']<2e-7
    assert rows[-1]['max_C']/rows[0]['max_C']<3e-7
    assert all(row['min_pf']>0 for row in rows)
    assert all(row['max_primary']<1e-11 for row in rows)


def test_validation_radii_are_not_fit_radii(solution):
    # Finite validation grid, not a proof that C(r) vanishes for ALL r.
    rr=np.array(solution['validation_radii'])
    fr=np.linspace(.05,.85,18)
    assert all(np.min(np.abs(fr-r))>1e-6 for r in rr)


def test_secondary_stencil_refinement_exposes_finite_precision_floor(solution):
    w=curved(delta=solution['history'][-1]['f_delta'])
    r=.7
    c1,_=local_candidate(w,r,h=.002)
    c2,_=local_candidate(w,r,h=.001)
    c3,_=local_candidate(w,r,h=.0005)
    assert abs(c2-c3)<abs(c1-c2)
    assert abs(c3)<1e-6


def test_original_nonibp_oracle_independent_resolution_convergence(solution):
    w0=curved()
    w=curved(delta=solution['history'][-1]['f_delta'])
    a=original_pb(w0,161)
    res=[original_pb(w,n) for n in (81,161,321,641)]
    assert a['bracket']>.009
    assert abs(res[-1]['bracket'])<5e-8
    assert abs(res[-1]['bracket'])<abs(res[0]['bracket'])/60
    assert all(row['max_abs_discrete_primary']<3e-7 for row in res)
    assert all(row['min_pf']>0 for row in res)
    assert all(len(row['pair_contributions'])==6 for row in res)


def test_reject_invalid_and_non_regular_sampling():
    w=curved()
    with pytest.raises(ValueError):kernel_fast(w,0.)
    with pytest.raises(ValueError):local_candidate(w,.03,.01)
    with pytest.raises(ValueError):solve_even_center(scale=-.1)
    with pytest.raises(ValueError):solve_even_center(degree=0)
