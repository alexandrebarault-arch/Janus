"""Exact algebraic regression checks for 68ad-C2d1 (not temporal sign tests)."""
import pytest
import sympy as sp
from numerics.hr_step68ad_c2d1_shift_variation_center import (
    physical_variations, center_certificate, theorem, SOURCE_PINS, authenticate_originals)


@pytest.fixture(scope='module')
def op():
    return physical_variations()


@pytest.fixture(scope='module')
def center():
    return center_certificate()


@pytest.mark.parametrize('sector',('N','M'))
@pytest.mark.parametrize('order',(2,3))
@pytest.mark.parametrize('quantity',('D','K'))
def test_exact_higher_lapse_coefficients(op,sector,order,quantity):
    assert sp.factor(op['delta'][sector][quantity][order])==0


def test_center_N_leading_identity(center):
    A,B,G,P,Z=(center['symbols'][k] for k in ('A','B','G','P','Z'))
    assert sp.factor(center['center_coefficients']['N']['D0_over_r']-Z*(P-2*G))==0


def test_center_M_leading_identity(center):
    A,B,G,P,Z=(center['symbols'][k] for k in ('A','B','G','P','Z'))
    assert sp.factor(center['center_coefficients']['M']['D0_over_r']-3*A*Z*(P-2*G)/B)==0


@pytest.mark.parametrize('sector',('N','M'))
def test_center_stationary_leading_cancels(center,sector):
    assert center['on_stationary_shift'][sector]==0


@pytest.mark.parametrize('sector',('N','M'))
def test_first_lapse_D_order_two(center,sector):
    assert not center['center_coefficients'][sector]['D1_over_r2'].has(sp.oo,sp.zoo,sp.nan)


@pytest.mark.parametrize('sector',('N','M'))
def test_first_lapse_K_order_three(center,sector):
    assert not center['center_coefficients'][sector]['K1_over_r3'].has(sp.oo,sp.zoo,sp.nan)


@pytest.mark.parametrize('sector',('N','M'))
def test_zero_lapse_K_order_two(center,sector):
    assert not center['center_coefficients'][sector]['K0_over_r2'].has(sp.oo,sp.zoo,sp.nan)


@pytest.mark.parametrize('sector',('N','M'))
def test_stationary_D_order_three(center,sector):
    assert not center['center_coefficients'][sector]['D0_on_shell_over_r3'].has(sp.oo,sp.zoo,sp.nan)


def test_theorem_scope():
    t=theorem()
    assert t['Step58_Cdot_7_cell_signs']=='NOT_EVALUATED'
    assert t['Step60_quotient']=='NOT_EVALUATED'
    assert t['GATE_2B']=='OPEN' and t['JANUS_R']=='NOT_VALIDATED'


def test_provenance_fail_closed(tmp_path):
    for f in SOURCE_PINS: (tmp_path/f).write_text('not original')
    with pytest.raises(ValueError,match='Physical source drift'):
        authenticate_originals(tmp_path)
