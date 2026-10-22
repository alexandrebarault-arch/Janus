"""Step48 exact center necessary condition + independent original-action oracle."""
import numpy as np
import sympy as sp
import pytest
from numerics.hr_step48_center_compatibility import center_relation,benchmark_center_gap
from numerics.hr_step48_original_ivp_oracle import (
    GIT_PINS,verify_actual_providers,clock,solve_ivp_initial_data,
    sample_actual_canonical,original_unintegrated_poisson,richardson,
    run_original_check)
from numerics.hr_step37_original_nonibp_oracle import hamiltonians

@pytest.fixture(scope='module')
def ode():return solve_ivp_initial_data()


def test_exact_leading_C_and_center_compatibility():
    s=center_relation()
    assert s['C_over_r2_leading']!=0
    assert s['C_over_r2_after_f_primary']!=0
    U=s['variables'][4]
    assert sp.simplify(s['C_over_r2_after_f_primary'].subs(U,s['necessary_Uf_0']))==0
    assert s['C_center_U_coefficient']!=0


def test_explicit_shift_center_momentum_correction():
    s=center_relation();mg,mf,m2,b0,b1,b2,b3,b4=s['parameters']
    r,a,b,Pg,U,V,G,k,Z=s['variables']
    assert sp.simplify(s['necessary_Uf_0']-mf*b*(Pg/(mg*a)-2*Z))==0
    assert sp.simplify(s['shift_correction_to_baseline_Pf']+2*mf*b*Z)==0


def test_center_frozen_coefficient_is_close_but_not_exactly_compatible():
    q=benchmark_center_gap()
    assert abs(q['old_minus_necessary'])<1e-12
    assert q['old_minus_necessary']!=0.0


def test_original_provider_source_pins_match_real_checkout():
    assert verify_actual_providers()==GIT_PINS


def test_clock_scalar_derivative_matches_background_phase_gradient():
    for r in (.06,.2,.43,.77):
        h=1e-5
        for k,scale,c in ((.0012,.4,.0015),(-.0016,.4*.5787707228025044,-.0012)):
            d=(clock(r+h,k,scale,c)-clock(r-h,k,scale,c))/(2*h)
            exact=k*r*scale*(1+c*r*r)**2
            assert abs(d-exact)<1e-11


def test_ivp_original_end_data_reproduced(ode):
    assert ode.success
    assert abs(ode.y[0,-1]-(-.0033864293564877215))<2e-12


def test_canonical_node_sampling_and_true_unintegrated_hamiltonians(ode):
    r=np.linspace(.05,.85,161)
    q,C=sample_actual_canonical(ode,r)
    assert q.shape==(12,161)
    assert np.min(q[5,1:-1])>0 and np.min(q[11,1:-1])>0
    assert C<1e-12
    H1,H2=hamiltonians(q,r)
    assert np.isfinite(H1).all() and np.isfinite(H2).all()
    assert max(np.max(abs(H1[12:-12])),np.max(abs(H2[12:-12])))<1e-6


def test_two_lapse_pair_original_poisson_converges_at_second_order(ode):
    for pair in ('A','B'):
        coarse=original_unintegrated_poisson(ode,161,pair)
        fine=original_unintegrated_poisson(ode,321,pair)
        assert coarse['bracket']<0 and fine['bracket']<0
        assert 3.8<coarse['bracket']/fine['bracket']<4.2
        assert coarse['max_discrete_primaries']>fine['max_discrete_primaries']>0
        assert len(coarse['six_contributions'])==6
        assert fine['min_pf_div_r2_sample']>.11


def test_richardson_is_assumption_not_exact_error_bound():
    m=richardson([-16.,-4.,-1.,-.25])
    assert m['R2']==[0.,0.,0.]
    assert m['R4']==[0.,0.]
    assert 'NOT a proven bound' in m['assumption']


def test_interrupted_run_manifest_keeps_Dirac_red():
    # Skip long grids in the test, but exercise machine-readable full checker.
    r=run_original_check((161,321,641),check_git=True)
    assert r['GATE_2B']=='OPEN' and r['JANUS_R']=='NOT_VALIDATED'
    assert 'secondary time preservation' in r['NOT_PROVED']
    assert r['two_lapse_pairs']['A']['richardson_exploratory']['R4']
    assert r['two_lapse_pairs']['B']['richardson_exploratory']['R4']
