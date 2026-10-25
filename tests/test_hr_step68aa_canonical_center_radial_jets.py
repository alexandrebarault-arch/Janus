"""Audits Step68aa by original-source hash, symbolic oracle and negative controls."""
import json
from fractions import Fraction as F
from pathlib import Path
import shutil
import pytest
from numerics.hr_step68aa_canonical_center_radial_jets import (
    BLOB68Z_SOURCE,BLOB68Z_REPORT,LIMIT_MULTIPLIERS,authenticated_inputs,
    formal_radial_jet_audit,center_limits,report,git_blob,nonzero_radius_ode_identities)

ROOT=Path(__file__).resolve().parents[1]/'research'/'reports'

def test_original_hashes_original_rational_center():
    a,b=authenticated_inputs(ROOT)
    assert a<=b<0
    assert b-a<F(1,10**20)

def test_independent_analytic_radial_jet_oracle():
    assert formal_radial_jet_audit()==LIMIT_MULTIPLIERS

def test_strict_negative_canonical_third_radial_jet():
    a,b=authenticated_inputs(ROOT)
    d=center_limits(a,b)
    for name,(lo,hi) in d.items():
        assert F(lo)<=F(hi)<0,name
    assert F(d['pLf_tripleprime_over_r_minus_24U1_120U2s_over_s2'][0])==336*a
    assert F(d['pLf_doubleprime_minus_2U0_12U1s_30U2s2_over_s3'][1])==56*b

def test_exact_central_eighth_r_derivative():
    a,b=authenticated_inputs(ROOT)
    d=center_limits(a,b)
    assert list(map(F,d['pLf_8th_r_derivative_at_center']))==[40320*a,40320*b]

def test_radial_ode_hierarchy_unfrozen_G():
    v=nonzero_radius_ode_identities()
    assert 'G_U' in v['second_identity']
    assert 'G_UU' in v['third_identity'] and 'G_sU' in v['third_identity']
    assert '2*n+2-G_U' in v['center_denominator_proof']

def test_machine_report_scope_and_certified_originals():
    out=report(ROOT)
    assert out['step']=='68aa'
    assert out['temporal_Step58_AN_AM_near_center']=='NOT_COMPUTED'
    assert out['annulus_r_1over64_1over32']=='NOT_CERTIFIED'
    assert out['GATE_2B']=='OPEN' and out['JANUS_R']=='NOT_VALIDATED'
    assert out['input_authentic_Git_blobs']['68z_source']==BLOB68Z_SOURCE
    assert out['input_authentic_Git_blobs']['68z_report']==BLOB68Z_REPORT

def test_tampered_68z_report_rejected(tmp_path):
    for p in ROOT.glob('gate2b-step68*.json'): shutil.copy(p,tmp_path/p.name)
    p=tmp_path/'gate2b-step68z-invariant-center-cone.json'
    p.write_bytes(p.read_bytes().replace(b'"step": "68z"',b'"step": "68q"'))
    with pytest.raises(ValueError,match='SHA drift'):authenticated_inputs(tmp_path)

def test_center_u3_crosscheck_step68z_signs():
    a,b=authenticated_inputs(ROOT)
    out=report(ROOT)['exact_center_limit_intervals']
    assert list(map(F,out['pLf_prime_over_r_minus_Vstar_over_s3']))==[8*a,8*b]
    assert list(map(F,out['U_s_minus_Ustar_s_over_s2']))==[3*a,3*b]

def test_refuse_uncertified_positive_u3():
    with pytest.raises(ValueError,match='strictly negative'):
        center_limits(F(-1,10),F(1,10))
