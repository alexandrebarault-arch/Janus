"""Reproducible exact 25-derivative identity proof in small groups.

Run pytest -k canonical_and_gradients, then -k metrics_a, metrics_b,
couplings_and_z separately; a single all-test run can exceed tool timeout.
"""
import pytest
from numerics.hr_step68j_BN_exact_secondary_identity import (
    GROUPS,original_remainder,group_certificate,rational_reference)

@pytest.mark.parametrize('name',sorted(GROUPS))
def test_exact_jet_derivative_group(name):
    assert set(group_certificate(name))==set(GROUPS[name])

def test_reference_and_nonzero_secondary():
    r=rational_reference()
    assert r['remainder_exact_zero']=='0'
    assert r['C_on_Fz_nonzero']!='0'
    assert r['wrong_sign_not_an_identity']

def test_all_25_symbols_are_covered():
    a=original_remainder()
    assert len(a['names'])==25
    assert set(a['names'])=={x for group in GROUPS.values() for x in group}

def test_unchanged_physical_authenticity():
    a=original_remainder()
    assert len(a['original_sha'])==5
