"""Step49 exact indicial algebra and numeric, NOT rigorous center global proof."""
import math
import sympy as sp
import pytest
from numerics.hr_step49_regular_center_shoot import (
    exact_indicial_data, benchmark_u0, estimate_u1, initial_pLf,
    solve_cutoff, sample_dust, center_shooting_study, finite_radius_F1)


@pytest.fixture(scope='module')
def report():return center_shooting_study()


def test_exact_indicial_exponent_and_excluded_singular_solution():
    d=exact_indicial_data()
    assert d['indicial_exponent_s']==sp.Rational(-3,2)
    assert d['homogeneous_pLf(r)']!=0
    assert sp.simplify(d['first_even_coefficient_formula']-sp.Symbol('F1')/5)==0


def test_center_leading_condition_not_old_frozen_guess():
    assert -.005253<benchmark_u0()<-.005252
    assert initial_pLf(.01,0)==pytest.approx(benchmark_u0()*.01**2,abs=1e-20)


def test_numerical_first_even_correction_stable_to_halving():
    assert .0007897<estimate_u1()<.0007898
    assert abs(estimate_u1(.008)-estimate_u1(.004))<1e-10
    assert math.isfinite(finite_radius_F1(.008))


def test_first_frobenius_term_improves_endpoint_by_orders_of_magnitude(report):
    r=report['cutoff_results']
    assert r[0]['order0_abs_delta_from_reference']>2e-10
    assert r[0]['order1_abs_delta_from_reference']<2e-14
    assert r[1]['order1_abs_delta_from_reference']<1e-15


def test_missing_U1_cutoff_error_scales_as_eps_fifth_power(report):
    x=[r['order0_abs_delta_from_reference'] for r in report['cutoff_results']]
    assert all(30< x[i]/x[i+1]<34 for i in range(3))


def test_first_even_coefficient_gives_empirical_seventh_order(report):
    x=[r['order1_abs_delta_from_reference'] for r in report['cutoff_results']]
    assert x[0]>50*x[1]
    # At the finest cutoff, binary64 numerical roundoff dominates.
    assert x[-1]<1e-16


def test_center_outward_branch_rejoins_step47_interior_endpoint(report):
    assert abs(report['reference_order1_endpoint']-(-.0033864293564877215))<5e-13
    assert report['reference_eps']==.001


def test_two_dust_source_remain_positive_at_129_samples_not_a_continuum_proof(report):
    d=report['positive_dust_sample']
    assert d['sample_count']==129
    assert d['min_pg_over_r2_sample']>.885
    assert d['min_pf_over_r2_sample']>.111
    assert d['max_abs_analytic_C_substitution']<1e-12
    assert d['NOT_CONTINUOUS_CERTIFICATION'] is True


def test_error_guards():
    with pytest.raises(ValueError):initial_pLf(0)
    with pytest.raises(ValueError):initial_pLf(.01,2)
    with pytest.raises(ValueError):estimate_u1(1)
    with pytest.raises(ValueError):solve_cutoff(.1,stop=.05)
    with pytest.raises(ValueError):center_shooting_study(cutoffs=(.001,.0005))


def test_manifest_is_cautious_and_all_physical_reds_open(report):
    assert report['GATE_2B']=='OPEN' and report['JANUS_R']=='NOT_VALIDATED'
    assert 'analytic existence at center' in report['NOT_PROVED']
    assert 'continuous new-IVP dust positivity' in report['NOT_PROVED']
    assert 'Dirac time preservation' in report['NOT_PROVED']
