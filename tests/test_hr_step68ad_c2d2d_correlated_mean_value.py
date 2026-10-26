"""Independent checks of Step60 AM first-order continuum certificate."""
from fractions import Fraction as F
from pathlib import Path
import json
import pytest
from numerics.hr_step55_global_barrier import I,S
from numerics.hr_step68ad_c2d2d_correlated_mean_value import Dual,mean_value_cell,compact_certificate
from numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay import evaluate_lower_quotient
from numerics.hr_step68ad_c2b_center_boxes import load_pinned,certify_cells
from numerics.hr_step68ad_c2d2a_temporal_replay import verify_original_files
from numerics.hr_step60_full_constraint_prolongation import verified_original_sources

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'research/reports/gate2b-step68ad-C2d2d-Step60-AM-mean-value-compact.json'

def encloses(iv,x):
    return F(iv.lo,S)<=F(x)<=F(iv.hi,S)

def test_dual_polynomial_exact_point():
    x=Dual(F(3,2),1)
    y=x**3-2*x+1
    assert encloses(y.v,F(11,8))
    assert encloses(y.d,F(19,4))

def test_dual_inverse_sqrt_point():
    x=Dual(4,1)
    assert encloses(x.sqrt().v,2)
    assert encloses(x.sqrt().d,F(1,4))
    assert encloses(x.inv().v,F(1,4))
    assert encloses(x.inv().d,F(-1,16))

def test_dual_fail_closed_on_bad_domains():
    with pytest.raises(ZeroDivisionError): Dual(I.hull(-1,1),1).inv()
    with pytest.raises(ValueError): abs(Dual(I.hull(-1,1),1))
    with pytest.raises(ValueError): Dual(-1,1).sqrt()

def test_mean_value_theorem_independent_polynomial():
    x=Dual(I.hull(0,1),1)
    der=(x*x).d
    center=Dual(F(1,2),1)**2
    hull=center.v+I.hull(F(-1,2),F(1,2))*der
    assert encloses(hull,0) and encloses(hull,1)

def test_endpoint_signs_not_continuum_proof():
    def f(x):return F(1,8)-(x-F(1,2))**2
    assert f(0)<0 and f(1)<0 and f(F(1,2))>0

def test_authentic_sources_and_original_report_pins():
    source=verify_original_files(ROOT/'numerics')
    source.update(verified_original_sources())
    r=json.loads(REPORT.read_text())
    assert r['original_source_git_blobs'].items()<=source.items()
    assert r['original_report_git_blobs']==certify_cells(load_pinned(ROOT/'research/reports'))['pinned_original_report_git_blobs']

def test_certificate_exact_rational_full_cover_and_strict_sign():
    cert=json.loads(REPORT.read_text())
    assert cert['GATE_2B']=='OPEN' and cert['JANUS_R']=='NOT_VALIDATED'
    assert cert['Step60_BN_continuum']=='INCOMPLETE'
    assert cert['Step58_continuum']=='INCOMPLETE'
    assert cert['continuous_AM_negative_original_cells']==7 and cert['total_subcells']==224
    original=certify_cells(load_pinned(ROOT/'research/reports'))
    upper=[];lower=[]
    for i,row in enumerate(cert['original_cells']):
        a,b=map(F,row['r'])
        assert [str(a),str(b)]==original['cells'][i]['r']
        assert len(row['leaves'])==32
        assert F(row['leaves'][0]['r'][0])==a and F(row['leaves'][-1]['r'][1])==b
        for j,leaf in enumerate(row['leaves']):
            if j: assert F(row['leaves'][j-1]['r'][1])==F(leaf['r'][0])
            lo,hi=map(F,leaf['AM'])
            assert lo<=hi<0
            upper.append(hi);lower.append(lo)
    assert max(upper)==F(cert['max_AM_upper'])
    assert min(lower)==F(cert['min_AM_lower'])
    assert cert['original_cells'][0]['r'][0]=='1/64' and cert['original_cells'][-1]['r'][1]=='1/32'

def test_original_step60_midpoint_is_enclosed_by_mean_value():
    cert=json.loads(REPORT.read_text())
    leaf=cert['original_cells'][0]['leaves'][0]
    a,b=map(F,leaf['r']);mid=(a+b)/2
    original=evaluate_lower_quotient(mid,mid,load_pinned(ROOT/'research/reports'))['AM']['enclosure']
    orig_lo,orig_hi=map(F,original)
    bound_lo,bound_hi=map(F,leaf['AM'])
    assert bound_lo<=orig_lo<=orig_hi<=bound_hi

def test_recomputed_first_leaf_matches_published_witness():
    cert=json.loads(REPORT.read_text())
    leaf=cert['original_cells'][0]['leaves'][0]
    a,b=map(F,leaf['r'])
    value=mean_value_cell(a,b,load_pinned(ROOT/'research/reports'))['AM']['mean_value']
    assert [str(F(value.lo,S)),str(F(value.hi,S))]==leaf['AM']
