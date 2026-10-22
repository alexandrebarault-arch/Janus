"""Historical Step48 actual five GitHub provider pins and original Poisson.

NOTE: legacy imports hr_curved_moving_dust_primary and mixed_kernel are
local constants/Q adapters here, not byte-identical originals. The five
source files checked by Step48 ARE original Git blobs; no full-repository
historical dependency claim is made.
"""
import pytest
from numerics.hr_step48_original_ivp_oracle import (
    verify_actual_providers,GIT_PINS,run_original_check,
    git_blob,original_unintegrated_poisson,solve_ivp_initial_data)
from pathlib import Path

@pytest.fixture(scope='module')
def check():return run_original_check((161,321,641),check_git=True)

def test_five_historical_source_git_blob_ids_match_actual_files():
    assert verify_actual_providers()==GIT_PINS
    assert len(GIT_PINS)==5

def test_sixth_step48_runner_is_byte_original():
    root=Path(__file__).resolve().parents[1]
    assert git_blob((root/'numerics/hr_step48_original_ivp_oracle.py').read_bytes())=='dc5101d4b0d1d5b8d0834aacff4a3ad3715a28db'

def test_true_original_nonibp_two_smears_and_primaries(check):
    assert check['original_provider_pins']==GIT_PINS
    for label in ('A','B'):
        x=check['two_lapse_pairs'][label]['grid_results']
        assert [r['n'] for r in x]==[161,321,641]
        assert all(r['bracket']<0 for r in x)
        assert all(3.8<x[i]['bracket']/x[i+1]['bracket']<4.2 for i in (0,1))
        assert all(r['min_pf_div_r2_sample']>.111 for r in x)
        assert len(x[0]['six_contributions'])==6

def test_original_action_still_has_finite_grid_primary_error(check):
    for x in check['two_lapse_pairs'].values():
        row=x['grid_results']
        assert row[0]['max_discrete_primaries']>row[-1]['max_discrete_primaries']>1e-9

def test_pin_failure_on_any_modified_historical_file(monkeypatch):
    import numerics.hr_step48_original_ivp_oracle as original
    p=dict(GIT_PINS)
    first=next(iter(p));p[first]='f'*40
    monkeypatch.setattr(original,'GIT_PINS',p)
    with pytest.raises(ValueError,match='historical GitHub provider changed'):
        original.verify_actual_providers()

def test_secondary_dirac_time_uncomputed_during_original_run(check):
    assert 'secondary time preservation' in check['NOT_PROVED']
    assert check['GATE_2B']=='OPEN' and check['JANUS_R']=='NOT_VALIDATED'
