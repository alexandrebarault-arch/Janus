"""Bounded, fail-closed rational replay of Step68p/68q numerical certificates."""
import json
from pathlib import Path
import pytest
from numerics.hr_step68r_cell_replay import prep,replay,PROOFS

@pytest.mark.parametrize('label',('outer','inner'))
def test_certified_exact_no_gap_provenance(label):
    rows,sha,provenance=prep(label)
    assert len(rows)==PROOFS[label][4]
    assert len(provenance['original_shas'])==8
    assert len(sha)==64

@pytest.mark.parametrize('label',('outer','inner'))
def test_actual_engine_exact_replay_of_first_three_rows(tmp_path,label):
    target=tmp_path/(label+'.json')
    x=replay(label,target,max_cells=3)
    assert x['completed']==3 and x['status']=='INCOMPLETE'
    y=replay(label,target,max_cells=2)
    assert y['completed']==5 and y['status']=='INCOMPLETE'
    assert not y['failures']


def test_tampered_proof_rejected_before_any_computation(tmp_path):
    original=Path(__file__).resolve().parents[1]/'research/reports'/PROOFS['inner'][0]
    target=tmp_path/'proof.json';target.write_bytes(original.read_bytes()+b' ')
    with pytest.raises(ValueError,match='SHA256'):prep('inner',target)


def test_mutated_resume_state_refused(tmp_path):
    target=tmp_path/'state.json';v=replay('outer',target,max_cells=1)
    v['source_provenance']['new_engine_sha']='corrupted';target.write_text(json.dumps(v))
    with pytest.raises(ValueError,match='drift'):replay('outer',target,max_cells=1)
