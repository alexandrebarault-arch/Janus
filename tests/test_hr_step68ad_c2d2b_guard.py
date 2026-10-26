"""Guard/certificate integrity tests; original Step58/Step60 NOT executed."""
from fractions import Fraction as F
from types import SimpleNamespace
import copy
import pytest
from numerics.hr_step68ad_c2d2b_guard import assert_guard_binding, summarize_temporal_signs, SCALE


def fixture_box():
    lo, hi = F(1, 64), F(1, 56)
    rlo = lo.numerator*SCALE//lo.denominator
    rhi = -((-hi.numerator*SCALE)//hi.denominator)
    cell = SimpleNamespace(lo=rlo*rlo//SCALE, hi=-((-rhi*rhi)//SCALE))
    box = {"s": [str(F(cell.lo, SCALE)), str(F(cell.hi, SCALE))],
           "outward_s_lattice_guard": True,
           "U": ["-1/4", "-1/5"], "U_s": ["1/1000", "2/1000"],
           "U_ss": ["-1/100", "-1/200"], "U_sss": ["-1/1000", "-1/2000"]}
    return box, cell


def rows(N="POSITIVE_CERTIFIED", M="NEGATIVE_CERTIFIED"):
    pairs = {"POSITIVE_CERTIFIED": ["1/10", "1/5"],
             "NEGATIVE_CERTIFIED": ["-1/5", "-1/10"],
             "INCOMPLETE": ["-1/10", "1/10"]}
    return [{"r": [str(F(1,64)+F(i,448)),str(F(1,64)+F(i+1,448))],
             "temporal": {"N": {"sign": N, "enclosure": pairs.get(N)},
                          "M": {"sign": M, "enclosure": pairs.get(M)}}} for i in range(7)]


def test_matching_guard_passes():
    b,cell=fixture_box();assert assert_guard_binding(b,cell)

def test_guard_missing_fails_closed():
    b,cell=fixture_box();del b['outward_s_lattice_guard']
    with pytest.raises(ValueError,match='Missing outward'):assert_guard_binding(b,cell)

def test_stale_cell_rejected_even_when_jet_bounds_present():
    b,cell=fixture_box();cell.hi+=1
    with pytest.raises(ValueError,match='does not match'):assert_guard_binding(b,cell)

def test_missing_s_rejected():
    b,cell=fixture_box();del b['s']
    with pytest.raises(ValueError,match='Missing or malformed'):assert_guard_binding(b,cell)

def test_reversed_derivative_rejected():
    b,cell=fixture_box();b['U_ss']=['-1/200','-1/100']
    with pytest.raises(ValueError,match='Reversed derivative'):assert_guard_binding(b,cell)

def test_bad_derivative_fraction_rejected():
    b,cell=fixture_box();b['U']=['NaN','1']
    with pytest.raises(ValueError,match='Non-rational derivative'):assert_guard_binding(b,cell)

def test_historical_pattern_reported_separately():
    o=summarize_temporal_signs(rows());assert o['all_nonzero_signs_certified']
    assert o['all_expected_A_N_positive_A_M_negative'];assert o['incomplete_coefficients']==[]
    assert o['exact_rational_enclosures_checked']==14

def test_opposite_nonzero_signs_are_not_misreported_as_historical_pattern():
    o=summarize_temporal_signs(rows('NEGATIVE_CERTIFIED','POSITIVE_CERTIFIED'))
    assert o['all_nonzero_signs_certified'] and not o['all_expected_N_positive_M_negative']
    assert len(o['opposite_to_historical_pattern'])==14

def test_zero_crossing_keeps_incomplete():
    o=summarize_temporal_signs(rows('INCOMPLETE','NEGATIVE_CERTIFIED'))
    assert not o['all_nonzero_signs_certified'];assert len(o['incomplete_coefficients'])==7

def test_missing_operator_label_rejected():
    a=rows();del a[0]['temporal']['M']
    with pytest.raises(ValueError,match='Incomplete temporal'):summarize_temporal_signs(a)

def test_incorrect_cell_count_rejected():
    with pytest.raises(ValueError,match='seven'):summarize_temporal_signs(rows()[:6])

def test_unrecognized_sign_rejected():
    a=rows();a[0]['temporal']['N']['sign']='POSSIBLE'
    with pytest.raises(ValueError,match='Invalid temporal sign'):summarize_temporal_signs(a)

def test_positive_label_with_zero_crossing_rejected():
    a=rows();a[0]['temporal']['N']['enclosure']=['-1','1']
    with pytest.raises(ValueError,match='Sign/enclosure mismatch'):summarize_temporal_signs(a)

def test_negative_label_with_positive_enclosure_rejected():
    a=rows();a[0]['temporal']['M']['enclosure']=['1','2']
    with pytest.raises(ValueError,match='Sign/enclosure mismatch'):summarize_temporal_signs(a)

def test_incomplete_label_with_strict_sign_rejected():
    a=rows();a[0]['temporal']['N']['sign']='INCOMPLETE'
    with pytest.raises(ValueError,match='Sign/enclosure mismatch'):summarize_temporal_signs(a)

def test_missing_enclosure_rejected():
    a=rows();del a[0]['temporal']['N']['enclosure']
    with pytest.raises(ValueError,match='Missing or malformed'):summarize_temporal_signs(a)

def test_nonrational_enclosure_rejected():
    a=rows();a[0]['temporal']['N']['enclosure']=['nan','2']
    with pytest.raises(ValueError,match='Non-rational'):summarize_temporal_signs(a)

def test_reversed_enclosure_rejected():
    a=rows();a[0]['temporal']['N']['enclosure']=['2','1']
    with pytest.raises(ValueError,match='Reversed interval'):summarize_temporal_signs(a)

def test_duplicate_cell_rejected():
    a=rows();a[1]['r']=a[0]['r']
    with pytest.raises(ValueError,match='gap/overlap'):summarize_temporal_signs(a)

def test_gap_rejected():
    a=rows();a[1]['r']=['1/50',a[1]['r'][1]]
    with pytest.raises(ValueError,match='gap/overlap'):summarize_temporal_signs(a)

def test_last_cell_does_not_reach_end_rejected():
    a=rows();a[-1]['r'][1]='1/33'
    with pytest.raises(ValueError,match='does not reach'):summarize_temporal_signs(a)

def test_nonrational_radius_rejected():
    a=rows();a[0]['r'][0]='nan'
    with pytest.raises(ValueError,match='Non-rational'):summarize_temporal_signs(a)

def test_no_inference_about_lapse_values():
    o=summarize_temporal_signs(rows())
    assert o['labels_are_lapse_coefficients_not_lapse_values'] is True
