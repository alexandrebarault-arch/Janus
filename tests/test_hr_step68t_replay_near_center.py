"""Step68t near-center signed interval certificate strict SHA and replay."""
import json
from pathlib import Path
import pytest
from numerics.hr_step68t_replay_near_center import prep,replay

def test_valid_range_and_all_1006_positive_signed_leaves():
    rows, sha, prov=prep('near')
    assert len(rows)==1006 and len(prov['original_shas'])==8
    assert len(sha)==64


def test_five_leaves_recomputed_exactly_with_resume(tmp_path):
    p=tmp_path/'state.json'
    a=replay('near',p,max_cells=3)
    assert a['completed']==3 and a['status']=='INCOMPLETE'
    b=replay('near',p,max_cells=2)
    assert b['completed']==5 and b['status']=='INCOMPLETE'
    assert not b['failures']


def test_tamper_1006_proof_bytes_rejected(tmp_path):
    original=Path(__file__).resolve().parents[1]/'research/reports/gate2b-step68s-inner-1over32-to-1over16-cover.json'
    wrong=tmp_path/'bad.json'
    wrong.write_bytes(original.read_bytes()+b' ')
    with pytest.raises(ValueError,match='SHA256'):prep('near',wrong)
