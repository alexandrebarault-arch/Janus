"""Regression tests for authentic Step58 execution and Step60 symbolic replay.

Pointwise signs are NOT continuum signs. A zero-containing interval is INCOMPLETE.
"""
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch
import pytest
from numerics import hr_step68o_temporal_interval_annulus as annulus
from numerics.hr_step68ad_c2d2b_executed_temporal_probe import (
    ORIGINAL_COMPILED, denominator_identity, factored_compiled, run,
)
from numerics.hr_step68ad_c2d2a_temporal_replay import (
    box_for_rounded_s, inject_s_jet, verify_original_files,
)
from numerics.hr_step68ad_c2b_center_boxes import load_pinned, Q, validate_reports
from numerics.hr_step68n_interval_ode_jets import Jet, I

ROOT = Path(__file__).resolve().parent.parent

@lru_cache(1)
def report():
    return run(ROOT)


def test_original_pins_verified():
    assert len(verify_original_files(ROOT/'numerics')) == 6
    assert len(load_pinned(ROOT/'research'/'reports')) == 3


@pytest.mark.parametrize('label', ['N','M'])
def test_exact_original_cse_denominator_identity(label):
    op,_ = ORIGINAL_COMPILED()
    syms, safe, repl, red, index, alternative = denominator_identity(op,label)
    assert str(repl[index][0]) == 'x'+str(index)
    assert alternative.has(*[x for x in syms if str(x)=='Sg'])


def test_original_interval_backend_rejects_first_cell_due_to_dependency():
    reports=load_pinned(ROOT/'research'/'reports')
    lo,hi=F(1,64),F(1,56)
    si=I.hull(lo,hi)**2
    box=box_for_rounded_s(reports,si,{'r':[str(lo),str(hi)]},Q,validate_reports)
    with inject_s_jet(annulus,box,Jet,I,si):
        with pytest.raises(ZeroDivisionError,match='crossing zero'):
            annulus.evaluate_cell(lo,hi)


def test_factored_first_cell_evaluates_but_contains_zero():
    reports=load_pinned(ROOT/'research'/'reports')
    lo,hi=F(1,64),F(1,56)
    si=I.hull(lo,hi)**2
    box=box_for_rounded_s(reports,si,{'r':[str(lo),str(hi)]},Q,validate_reports)
    with patch.object(annulus,'_compiled',factored_compiled):
        with inject_s_jet(annulus,box,Jet,I,si):
            vals=annulus.evaluate_cell(lo,hi)
    assert set(vals)=={'N','M'}
    assert all(v.lo<0<v.hi for v in vals.values())


def test_seven_cell_execution_is_incomplete_not_certified():
    r=report()
    assert len(r['seven_cell_continuum'])==7
    assert len(r['continuum_sign_audit']['incomplete_coefficients'])==14
    assert not r['continuum_sign_audit']['all_nonzero_signs_certified']
    assert all(v['sign']=='INCOMPLETE' for cell in r['seven_cell_continuum']
               for v in cell['temporal'].values())


def test_eight_pointwise_edge_signs_not_confused_with_continuum():
    r=report()
    assert len(r['pointwise_eight_edges'])==8
    assert [F(x['r']) for x in r['pointwise_eight_edges']][0]==F(1,64)
    assert [F(x['r']) for x in r['pointwise_eight_edges']][-1]==F(1,32)
    for point in r['pointwise_eight_edges']:
        assert point['temporal']['N']['sign']=='POSITIVE_CERTIFIED'
        assert point['temporal']['M']['sign']=='NEGATIVE_CERTIFIED'
        for key in ('N','M'):
            lo,hi=map(F,point['temporal'][key]['enclosure'])
            assert lo<=hi
            assert lo>0 if key=='N' else hi<0


def test_original_step60_symbolic_executed_but_seven_cell_quotient_not_done():
    r=report()
    m=r['Step60_original_symbolic_manifest']
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'
    assert m['full_lower_jet_constraint_quotient']=='NOT COMPLETED'
    assert r['Step60_seven_cell_lower_jet_quotient']=='NOT_EVALUATED'
    assert all(v=='0' for entries in m['checked_qrrr_derivative_residuals'].values()
               for v in entries.values())


def test_unmodified_original_compiled_after_scoped_patch():
    assert annulus._compiled is ORIGINAL_COMPILED
    assert factored_compiled is not ORIGINAL_COMPILED
