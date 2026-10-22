"""Controls for numerical interior integration of the exact-form local ODE."""
import pytest
from numerics.hr_step47_interior_ivp import integrate_interior,local_diagnostics

@pytest.fixture(scope='module')
def run():return integrate_interior()

def test_ivp_reaches_full_requested_interior_radius(run):
    assert run['r_interval']==[.05,.85]
    assert run['nfev']>50 and len(run['samples'])==33

def test_both_canonical_dust_momenta_positive_at_all_samples(run):
    assert run['min_pf_over_r2']>.11
    assert run['min_pg_over_r2']>.885

def test_all_four_original_primaries_numerically_near_zero(run):
    m=run['max_residuals']
    for k in ('Hg_original','Hf_original','Ddiag_original','Fz_original'):
        assert m[k]<1e-12

def test_analytic_secondary_elimination_numerically_near_zero(run):
    assert run['max_residuals']['C_analytic_substitution']<1e-12

def test_distinct_from_frozen_approximate_profile(run):
    last=run['samples'][-1]
    assert abs(last['pLf']-last['original_frozen_pLf'])>1e-15

def test_local_ode_is_not_promoted_to_global_ghost_free(run):
    assert run['GATE_2B']=='OPEN' and run['JANUS_R']=='NOT_VALIDATED'
    assert 'center r=0 not reached' in run['limitations']

def test_guard_on_uncontrolled_chart():
    with pytest.raises(ValueError):integrate_interior(start=.01)
    with pytest.raises(ValueError):integrate_interior(stop=.95)
