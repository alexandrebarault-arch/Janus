"""Targeted Step53 formal Laurent / physical spherical secondary tests."""
from fractions import Fraction as F
from decimal import Decimal
import os,sys,subprocess,json
from pathlib import Path
import pytest
from numerics.hr_step53_exact_center_u2 import (
    Q,J,H2,background,exact_u2,rational_interval,exact_certificate)
from numerics.hr_step53_outward_compare import compare

U1_A=F('6208001291053702394129476735256316334533396863490262227811494820469332490792832990397189264359888632547935265740403706964896568431135042477171/8063117590497060413339167053752066292665863037109375000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
U1_B=F('137170281832716484398889218959696760026478530363669648507605220557178319557911/16513264825337979726518614126084231767379687500000000000000000000000000000000000000')

@pytest.fixture(scope='module')
def certificate():return exact_certificate()

@pytest.fixture(scope='module')
def shooting():return compare()

def test_center_U1_matches_previous_exact_github_certificate_bit_for_bit():
    x=exact_u2()
    assert x['U1'].a==U1_A
    assert x['U1'].b==U1_B
    assert x['first_cutoff']>5

def test_center_U2_has_exact_rational_quadratic_coordinates():
    x=exact_u2();q=x['U2']
    assert isinstance(q.a,F) and isinstance(q.b,F)
    assert q.a<0 and q.b<0
    assert x['second_cutoff']>5
    assert x['central_r1_correct'] and x['central_r3_correct']

def test_sign_of_U2_certified_not_only_highprecision_decimal():
    x=exact_u2();lo,hi=rational_interval(x['U2'],100)
    assert lo<hi<0
    assert hi-lo<F(1,10**100)
    assert F('-0.00001007385348674382817573689095286393593388364194376377344')<lo
    assert hi<F('-0.00001007385348674382817573689095286393593388364194376377342')

def test_exact_formal_reciprocal_and_square_root_independent_negative_controls():
    from numerics import hr_step53_exact_center_u2 as e
    e.background()
    r=J({1:Q(1)})
    geometric=(J.c(1)-r*r).inv()
    for k in (0,2,4,6,8):assert geometric.d[k]==Q(1)
    root=(J.c(1)-r*r).sqrt()
    square=root*root
    assert square.d.get(0,Q())==Q(1) and square.d.get(2,Q())==Q(-1)
    for k in (1,3,4,5,6):assert square.d.get(k,Q())==Q()
    with pytest.raises(ValueError):(r*r*r).sqrt()

def test_independent_four_orders_same_physical_U2_exact_fraction_pairs():
    repo=Path(__file__).resolve().parents[1];out=[]
    for order in (12,14,18,22):
        env=os.environ.copy();env.update(JANUS_JET_ORDER=str(order),PYTHONPATH=str(repo),OPENBLAS_NUM_THREADS='1')
        raw=subprocess.run([sys.executable,'-m','numerics.hr_step53_exact_center_u2'],cwd=repo,env=env,capture_output=True,text=True,check=True)
        out.append(json.loads(raw.stdout))
    assert len({(x['U2_A'],x['U2_B']) for x in out})==1
    assert len({(x['U1_A'],x['U1_B']) for x in out})==1
    assert [x['first_unknown_power'] for x in out]==[7,9,13,17]
    assert [x['second_unknown_power'] for x in out]==[7,9,13,17]

def test_Briot_Bouquet_center_coefficient_denominator_seven():
    import sympy as sp
    s,U0,U1,U2,g2,g11,g02=sp.symbols('s U0 U1 U2 g2 g11 g02')
    u=U0+U1*s+U2*s*s
    # physical G(0,U)=3U0-U; g10=5U1; all other coefficients symbolic
    G=3*U0-u+5*U1*s+g2*s*s+g11*s*(u-U0)+g02*(u-U0)**2
    delta=sp.expand(G-2*u-2*s*sp.diff(u,s))
    assert sp.expand(delta).coeff(s,2)==g2+g11*U1+g02*U1**2-7*U2

def test_two_and_three_term_numeric_shoot_improves_frozen_cutoff(shooting):
    row=shooting['rows'][0]
    assert row['eps']==.05
    assert row['degree1_abs_error_from_reference']>8e-15
    assert row['degree2_abs_error_from_reference']<1e-17
    assert row['degree2_abs_error_from_reference']<row['degree1_abs_error_from_reference']/1000

def test_cutoff_convergence_and_status_conservatism(shooting):
    assert abs(shooting['reference_endpoint']+.003386429356487895)<2e-13
    assert shooting['GATE_2B']=='OPEN' and shooting['JANUS_R']=='NOT_VALIDATED'
    assert shooting['Dirac_time_preservation']=='NOT_COMPUTED'
    assert shooting['both_dust_continuum_signs']=='NOT_CERTIFIED'

def test_result_preserves_exact_numeric_distinction(certificate):
    assert certificate['U2_enclosure_width_less_than_1e_minus_80']
    assert certificate['global_radial_solution']=='NOT_CERTIFIED'
    assert certificate['full_Dirac_time_preservation']=='NOT_COMPUTED'
