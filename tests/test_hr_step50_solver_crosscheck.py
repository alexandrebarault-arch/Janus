"""Step50 integrator diversity checks (purely numerical evidence)."""
import math
import pytest
from numerics.hr_step50_solver_crosscheck import crosscheck, METHODS

@pytest.fixture(scope='module')
def run():return crosscheck()

def test_all_three_qualitatively_distinct_integrators_reach_endpoint(run):
    assert set(run['integrators'])==set(METHODS)
    assert all(v['success'] for v in run['integrators'].values())
    assert all(v['nfev']>100 for v in run['integrators'].values())

def test_outward_shooting_endpoints_agree_approximately(run):
    ends=[v['endpoint_pLf'] for v in run['integrators'].values()]
    assert max(ends)-min(ends)<3e-13
    assert all(abs(p+.003386429356487895)<3e-13 for p in ends)

def test_entire_sampled_momentum_traces_agree_without_claiming_exactness(run):
    assert run['n_validation_sites']==2049
    assert max(run['max_abs_pLf_against_first_method'].values())<3e-13

def test_2049_radii_have_positive_two_dust_densities_for_each_solver(run):
    for r in run['integrators'].values():
        assert r['min_sampled_pg_div_r2']>.8855
        assert r['min_sampled_pf_div_r2']>.1118

def test_analytic_substitution_small_by_construction(run):
    assert all(r['max_sampled_C_by_construction']<1e-12 for r in run['integrators'].values())
    assert 'not rigorous error enclosure' in run['main_scope']

def test_max_step_input_guard():
    with pytest.raises(ValueError):crosscheck(max_step=.2)

def test_refuses_duplicate_or_unknown_integrator():
    with pytest.raises(ValueError):crosscheck(methods=('RK45','RK45'))
    with pytest.raises(ValueError):crosscheck(methods=('INVALID',))

def test_refuses_to_infer_continuum_positivity_from_samples(run):
    assert 'continuous dust positivity between sampling sites' in run['not_proved']
    assert run['GATE_2B']=='OPEN' and run['JANUS_R']=='NOT_VALIDATED'
