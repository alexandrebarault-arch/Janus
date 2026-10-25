"""Exact signed-band insufficiency and analytic Step68ab oracle regression."""
from fractions import Fraction as F
from pathlib import Path
import json
import copy
import pytest
from numerics.hr_step68ab_derivative_data_obstruction import (
    EPS,S_MAX,certified_underdetermination,symbolic_oracle,
    original_G_center_U4_recurrence,report)
ROOT=Path(__file__).resolve().parents[1]/'research'/'reports'

def test_actual_original_certificates_authenticated():
    out=certified_underdetermination(ROOT)
    assert out['verified_original_step68aa_and_68z']
    assert out['G_U']=='-1'

def test_all_five_original_bands_strictly_contain_analytic_family():
    a=certified_underdetermination(ROOT)['bands']
    assert set(a)=={'h','f','ds','v','aux'}
    for row in a.values():
        x,y=map(F,row['whole_family_enclosure'])
        lo,hi=map(F,row['original_band'])
        assert lo < x < y < hi

def test_exact_constructed_ode_residual_zero():
    x=symbolic_oracle()
    assert x['ode_identity']=='EXACT_ZERO'
    assert x['slope_G_U']=='-1'

def test_third_derivative_not_uniformly_bounded():
    from sympy import sympify, symbols, limit, oo
    e,k=symbols('eps k',positive=True)
    expr=e*S_MAX*(18-4*sympify('pi')**2*k*k)
    assert limit(expr.subs(e,EPS),k,oo)==-oo

def test_G_is_not_frozen_when_deriving_U4():
    d=original_G_center_U4_recurrence()
    assert 'g01' in d['denominator']
    assert d['actual_U4_interval']=='NOT_CERTIFIED'

def test_full_report_fail_closed_on_temporal_claim():
    d=report(ROOT)
    assert d['step']=='68ab'
    assert d['physical_Step55_G_higher_partials']=='NOT_YET_INTERVAL_CERTIFIED'
    assert d['temporal_Step58_AN_AM']=='NOT_COMPUTED'
    assert d['GATE_2B']=='OPEN' and d['JANUS_R']=='NOT_VALIDATED'

def test_negative_source_drift_rejected(tmp_path):
    import shutil
    for p in ROOT.glob('gate2b-step68*.json'): shutil.copy(p,tmp_path/p.name)
    p=tmp_path/'gate2b-step68z-invariant-center-cone.json'
    p.write_bytes(p.read_bytes().replace(b'"step": "68z"',b'"step": "68y"'))
    with pytest.raises(ValueError,match='SHA drift'):
        certified_underdetermination(tmp_path)

def test_frequency_bound_requires_n_ge_1():
    # The interval bounds in the proof use epsilon/n <= epsilon.
    assert EPS/F(1) == EPS and EPS/F(2) < EPS

from numerics.hr_step68ab_derivative_data_obstruction import (
    three_curve_barrier_oracle,symbolic_three_curve_oracle,enhanced_report)

def test_original_Fzero_Fplus_Fminus_third_derivatives_all_maintained():
    d=three_curve_barrier_oracle(ROOT)
    f0=F(d['Fzero_third_over_6']);fp=F(d['Fplus_third_over_6']);fm=F(d['Fminus_third_over_6'])
    assert F(d['original_step68u_upper'][0])<fp<F(d['original_step68u_upper'][1])
    assert F(d['original_step68u_lower'][0])<fm<F(d['original_step68u_lower'][1])
    assert F(d['original_step68v_Fzero'][0])<f0<F(d['original_step68v_Fzero'][1])

def test_all_original_GU_bands_hold_for_other_G_family():
    d=three_curve_barrier_oracle(ROOT)
    lo,hi=map(F,d['G_U_correction_max'])
    assert F(-1,1000)<lo<0<hi<F(1,1000)

def test_independent_symbolic_cubic_interpolator_keeps_three_reference_curves():
    d=symbolic_three_curve_oracle()
    assert d['on_shell_residual']=='EXACT_ZERO'
    assert d['Fplus']=='9*c-9*kappa'
    assert d['Fminus']=='9*c+9*kappa'

def test_stronger_report_does_not_claim_original_G_bounded_jet():
    d=enhanced_report(ROOT)
    assert d['all_original_third_derivative_boundary_certificate_countermodel']['all_frequencies_n_greater_equal_1']
    assert d['physical_Step55_G_higher_partials']=='NOT_YET_INTERVAL_CERTIFIED'
    assert d['temporal_Step58_AN_AM']=='NOT_COMPUTED'
