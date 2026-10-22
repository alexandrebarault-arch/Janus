"""Exact algebraic U1 under rationalized Step41 inputs, not a Dirac proof."""
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
from subprocess import run
import json
import os
import sys
import pytest
from numerics.hr_step52_exact_center_taylor import (
    exact_jets, verify_source_pins, SOURCE_PINS, H2, Q, J, P)
from numerics.hr_step51_highprecision_center_coefficient import richardson_u1_at_decade


@pytest.fixture(scope='module')
def cert():
    return exact_jets()


def test_authentic_github_historical_sources_byte_exact():
    assert verify_source_pins()==SOURCE_PINS


def test_source_drift_refused(monkeypatch):
    import numerics.hr_step52_exact_center_taylor as mod
    pins=dict(SOURCE_PINS)
    pins['numerics/hr_step46_exact_secondary_ode.py']='0'*40
    monkeypatch.setattr(mod,'SOURCE_PINS',pins)
    with pytest.raises(ValueError,match='original source SHA drift'):
        mod.verify_source_pins()


def test_quadratic_number_field_exact_arithmetic_and_sqrt_branch():
    H=Q(0,1)
    assert H*H==Q(H2)
    assert ((H+Q(2))/(H+Q(2)))==Q(1)
    assert (H**2-H2)==Q()
    assert H2>0


def test_exact_rhs_center_coefficient_identities(cert):
    assert cert['center_rhs_coefficients_checked'] is True
    assert cert['rhs_remainder_unknown_from_r_power']>3
    assert cert['exact_formula'].startswith('U1=A+B*sqrt(H2)')


def test_certified_rational_interval_contains_quadratic_result(cert):
    a=F(cert['U1_rational_A']);b=F(cert['U1_rational_B'])
    lo=F(cert['strict_lower_rational']);hi=F(cert['strict_upper_rational'])
    assert b>0 and lo<hi and hi-lo<F('1e-80')
    assert F('0.0007897451667202464909325108904961683602148118201690')<lo
    assert hi<F('0.0007897451667202464909325108904961683602148118201692')


def test_independent_highprecision_original_rhs_estimate_agrees(cert):
    from decimal import Decimal
    old=richardson_u1_at_decade(9,120)
    # Numerically extrapolated source contains nonrigorous O(r^4) bias.
    value=Decimal(cert['decimal_display'])
    estimate=Decimal(old['u1_extrapolated_unenclosed'])
    assert abs(value-estimate)<Decimal('1e-38')


def test_exact_quadratic_coefficients_stable_across_three_orders():
    repo=Path(__file__).resolve().parents[1]
    out=[]
    for order in (14,20,26):
        env=os.environ.copy()
        env['JANUS_JET_ORDER']=str(order)
        env['OPENBLAS_NUM_THREADS']='1'
        env['PYTHONPATH']=str(repo)
        p=run([sys.executable,'-m','numerics.hr_step52_exact_center_taylor'],
              capture_output=True,text=True,env=env,cwd=repo,check=True)
        out.append(json.loads(p.stdout))
    assert len({x['U1_rational_A'] for x in out})==1
    assert len({x['U1_rational_B'] for x in out})==1
    assert [x['rhs_remainder_unknown_from_r_power'] for x in out]==[9,15,21]


def test_no_extrapolation_or_global_time_preservation_claim(cert):
    assert cert['GATE_2B']=='OPEN'
    assert cert['JANUS_R']=='NOT_VALIDATED'
    assert cert['Dirac_time_preservation']=='NOT_COMPUTED'
    assert cert['global_continuum_radial_solution']=='NOT_PROVED'
