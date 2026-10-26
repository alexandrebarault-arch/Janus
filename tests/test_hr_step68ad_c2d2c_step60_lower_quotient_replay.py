"""Fail-closed tests of authentic Step60 lower-jet seven-cell replay."""
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
import pytest
import sympy as sp
from numerics.hr_step68ad_c2d2c_step60_lower_quotient_replay import (
    run, evaluate_lower_quotient, compiled_lower_quotient,
    shell_denominator_cse, canonical_symbol_values,
)
from numerics.hr_step68ad_c2b_center_boxes import load_pinned
from numerics.hr_step68ad_c2d2a_temporal_replay import verify_original_files
from numerics.hr_step60_full_constraint_prolongation import verified_original_sources
from numerics import hr_step68o_temporal_interval_annulus as annulus
from numerics.hr_step68ad_c2d2b_executed_temporal_probe import ORIGINAL_COMPILED

ROOT=Path(__file__).resolve().parent.parent
@lru_cache(1)
def report():return run(ROOT)


def test_original_source_and_physical_report_pins():
    assert len(verify_original_files(ROOT/'numerics'))==6
    assert len(verified_original_sources())==4
    assert len(load_pinned(ROOT/'research'/'reports'))==3


def test_original_step60_compiled_third_free_representatives():
    pair=compiled_lower_quotient()
    assert set(pair)=={'BN','AM'}
    assert len(pair['BN'][0])==29 and len(pair['AM'][0])==38


def test_cse_denominator_mismatch_rejected():
    a,b=sp.symbols('a b')
    with pytest.raises((AssertionError,StopIteration)):
        shell_denominator_cse([a+b],(a,b),0)


def test_seven_cells_cover_exact_domain():
    rows=report()['seven_cell_lower_quotient']
    assert len(rows)==7
    assert F(rows[0]['r'][0])==F(1,64)
    assert F(rows[-1]['r'][1])==F(1,32)
    for left,right in zip(rows,rows[1:]):
        assert F(left['r'][1])==F(right['r'][0])


def test_fourteen_continuum_quotients_are_incomplete():
    result=report()
    assert result['continuous_signs_certified']==0
    for row in result['seven_cell_lower_quotient']:
        for label in ('BN','AM'):
            lower,upper=map(F,row['lower_quotient'][label]['enclosure'])
            assert lower<0<upper
            assert row['lower_quotient'][label]['sign']=='INCOMPLETE'


def test_eight_pointwise_am_negative_bn_incomplete():
    rows=report()['eight_pointwise_edges']
    assert len(rows)==8
    for row in rows:
        q=row['lower_quotient']
        assert q['AM']['sign']=='NEGATIVE_CERTIFIED'
        assert F(q['AM']['enclosure'][1])<0
        assert q['BN']['sign']=='INCOMPLETE'
        assert F(q['BN']['enclosure'][0])<=0<=F(q['BN']['enclosure'][1])
        assert row['AM_overlaps_original_Step58'] is True


def test_reject_zero_or_out_of_domain():
    reports=load_pinned(ROOT/'research'/'reports')
    for lo,hi in [(F(0),F(1,64)),(F(1,32),F(1,16)),(F(1,32),F(1,64))]:
        with pytest.raises(ValueError):evaluate_lower_quotient(lo,hi,reports)


def test_replay_does_not_patch_original_step58_persistently():
    report()
    assert annulus._compiled is ORIGINAL_COMPILED


def test_report_carries_explicit_open_status_and_limitations():
    result=report()
    assert result['GATE_2B']=='OPEN'
    assert result['JANUS_R']=='NOT_VALIDATED'
    assert 'NOT a rank' in result['limitations']
