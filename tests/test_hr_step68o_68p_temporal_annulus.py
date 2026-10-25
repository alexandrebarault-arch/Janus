"""Regression for certified OUTER annulus original Step58 signs, never 4D rank."""
from fractions import Fraction as F
import json
from pathlib import Path
import pytest
from numerics.hr_step68o_temporal_interval_annulus import evaluate_cell,canonical_jets_cell
from numerics.hr_step68p_adaptive_temporal_sign import cover,gi
from numerics.hr_step68f_physical_pointwise import verified_sources,evaluate_report
from numerics.hr_step68n_interval_ode_jets import certify_sources

CERT=Path(__file__).resolve().parents[1]/'research/reports/gate2b-step68p-adaptive-outer-cover.json'


def load():return json.loads(CERT.read_text())


def test_original_eight_physical_sha_exact():
    assert len(verified_sources())==8
    assert len(certify_sources())==4


def test_single_point_exact_signs():
    q=evaluate_cell(F(2,5),F(2,5))
    assert q['N'].lo>0 and q['M'].hi<0


def test_closed_mid_annulus_cell_signs():
    q=evaluate_cell(F(39,100),F(39,100)+F(1,50)/32)
    assert q['N'].lo>0 and q['M'].hi<0


def test_coarse_interval_is_not_falsely_certified():
    q=evaluate_cell(F(39,100),F(41,100))
    assert not(q['N'].lo>0 and q['M'].hi<0)


def test_no_radius_outside_certified_tube():
    with pytest.raises(ValueError):canonical_jets_cell(F(0),F(1,100))
    with pytest.raises(ValueError):canonical_jets_cell(F(4,5),F(9,10))
    with pytest.raises(ValueError):canonical_jets_cell(F(1,2),F(1,4))


def test_independent_rational_coverage_and_strict_signs():
    x=load(); assert x['status']=='CERTIFIED'
    assert x['coverage']==['1/8','17/20']
    assert x['processed']==529 and len(x['certified'])==265
    assert not x['queue'] and not x['failures']
    y=sorted(x['certified'],key=lambda row:F(row['lo']))
    assert F(y[0]['lo'])==F(1,8) and F(y[-1]['hi'])==F(17,20)
    assert all(F(l['hi'])==F(r['lo']) for l,r in zip(y,y[1:]))
    assert all(F(t['N'][0])>0 and F(t['M'][1])<0 and F(t['lo'])<F(t['hi']) for t in y)


def test_saved_certificate_fails_closed_on_source_drift(tmp_path):
    x=load(); x['provenance']['new_engine_sha']='deadbeef'
    p=tmp_path/'tampered.json';p.write_text(json.dumps(x))
    with pytest.raises(ValueError,match='drift'):
        cover(p,F(1,8),F(17,20),max_cells=1)


def test_saved_certificate_exact_sha_matches_reexecuted_modules():
    x=load(); root=Path(__file__).resolve().parents[1]/'numerics'
    assert x['provenance']['new_engine_sha']==gi(root/'hr_step68o_temporal_interval_annulus.py')
    assert x['provenance']['interval_jet_sha']==gi(root/'hr_step68n_interval_ode_jets.py')
    assert x['provenance']['original_shas']==verified_sources()


def test_rational_enclosure_contains_independent_float_original_step58():
    # Independent pointwise mpmath jets evaluated by the ORIGINAL Step58.
    sample=evaluate_report('0.4','0')
    q=evaluate_cell(F(2,5),F(2,5))
    assert F(q['N'].lo,10**28)<=F(str(sample['raw_temporal_coefficients']['N']['0']))<=F(q['N'].hi,10**28)
    assert F(q['M'].lo,10**28)<=F(str(sample['raw_temporal_coefficients']['M']['0']))<=F(q['M'].hi,10**28)


def test_global_ratio_positive_and_conservative_enclosure():
    x=load()['certified']
    rlo=min(-F(t['N'][0])/F(t['M'][0]) for t in x)
    rhi=max(-F(t['N'][1])/F(t['M'][1]) for t in x)
    assert F(0)<rlo<rhi
    # No false narrow precise global ratio claim: these are conservative.
    assert rlo<F(1,10000) and rhi>F(1)
