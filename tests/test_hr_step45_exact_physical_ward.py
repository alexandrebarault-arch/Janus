"""Exact symbolic Ward/shift identities, no nonzero-tolerance approximations."""
import sympy as sp
import pytest
from numerics.hr_step45_exact_physical_ward import exact_physical_ward, exact_certificate_summary

@pytest.fixture(scope='module')
def result():return exact_physical_ward()

def test_six_canonical_pairs_twelve_fields_three_smearing_jets(result):
    assert len(result['q'])==len(result['dq'])==len(result['ddq'])==12
    assert len(result['K'])==9
    assert all(len(jet)==12 for sector in ('eg','ef') for jet in result[sector])

def test_all_four_high_jets_vanish_exactly(result):
    for j in ('high_02','high_12','high_21','high_22'):
        assert result['residuals'][j]==0

def test_K20_explicit_formula_offshell(result):
    assert result['residuals']['K20_value']==0
    assert result['K20_expected']!=0

def test_K11_equals_K20_offshell(result):
    assert result['residuals']['K11_equal_K20']==0

def test_nontrivial_W_is_primary_Hg_exactly(result):
    assert result['residuals']['W_equals_zHg_over_Lf']==0
    q=dict(zip(result['Q'],result['q']));z=result['parameters'][-3]
    assert sp.cancel(result['W']-z*result['Hg']/q['Lf'])==0
    assert result['W']!=0  # not identically zero off shell

def test_shift_envelope_theorem_both_lapse_primaries(result):
    assert result['residuals']['shift_g_stationarity']==0
    assert result['residuals']['shift_f_stationarity']==0
    assert result['Fz']!=0

def test_exact_C_is_nonzero_offshell(result):
    assert result['C_exact']!=0

def test_exact_C_has_no_second_radial_canonical_jets(result):
    assert result['C_exact'].free_symbols.isdisjoint(result['ddq'])

def test_exact_C_has_no_z_radial_second_derivative(result):
    assert result['parameters'][-1] not in result['C_exact'].free_symbols

def test_total_derivative_includes_zprime_and_field_jets(result):
    z,zr,zrr=result['parameters'][-3:]
    assert result['total_derivative'](z)==zr
    assert result['total_derivative'](zr)==zrr
    assert result['total_derivative'](result['q'][0])==result['dq'][0]
    assert result['total_derivative'](result['dq'][0])==result['ddq'][0]

def test_negative_control_singular_Lf_region_not_certified(result):
    q=dict(zip(result['Q'],result['q']))
    assert q['Lf'] in result['W'].free_symbols
    assert result['W'].has(1/q['Lf']) or result['W'].has(q['Lf']**-1)

def test_manifest_keeps_dirac_red(result):
    v=exact_certificate_summary()
    assert v['exact_symbolic_residuals_all_zero']
    assert v['secondary_exact_zero']=='NOT_PROVED'
    assert v['secondary_time_preservation']=='NOT_COMPUTED'
    assert v['lapse_fixing']=='NOT_COMPUTED'
    assert v['GATE_2B']=='OPEN' and v['JANUS_R']=='NOT_VALIDATED'
