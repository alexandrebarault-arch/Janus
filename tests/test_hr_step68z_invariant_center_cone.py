"""Step68z: proof checks, strict signs and fail-closed negative tests."""
from fractions import Fraction as F
from pathlib import Path
import copy
import pytest
from numerics.hr_step68z_invariant_center_cone import tightened_bounds, original_reports, report

ROOT=Path(__file__).resolve().parents[1]/'research'/'reports'
FLO=F(-104671973400629476166791119,800000000000000000000000000000000)
FHI=F(-473550521560821294562534863,5000000000000000000000000000000000)
GLO=F(-80486828173226613100871119,80000000000000000000000000)
GHI=F(-496930963235322352562534863,500000000000000000000000000)

def fixture_reports():
    return {'68u': {'U3_lower_from_published_Step67b':'-31325163121998456229/2500000000000000000000000000',
                    'U3_upper_from_published_Step67b':'-62650326243996887233/5000000000000000000000000000'},
            '68v': {'G_U_center_interval':list(map(str,(GLO,GHI)))},
            '68y': {'F0_over_s_cubed_intersection':list(map(str,(FLO,FHI))),
                    'kappa':'1/10000000','U_minus_Ustar_over_s_cubed':['-1/10000000','0'],
                    'U_s_minus_Ustar_s_over_s_squared':['-1/1000000','1/1000000'],
                    'G_minus_Vstar_over_s_cubed':['-1/1000000','1/1000000']}}

def test_exact_barrier_and_sharp_signs():
    a=tightened_bounds(fixture_reports())
    assert a['h']==(FLO/(8-GHI),FHI/(8-GLO))
    assert a['ds'][1]<0 and a['v'][1]<0 and a['aux'][0]>0
    assert -F(2,100000000)<a['h'][1]<0
    assert all(x.denominator>0 for bounds in a.values() for x in bounds)

def test_barrier_residual_signs_at_extrema():
    a=tightened_bounds(fixture_reports())
    lower,upper=a['h']
    # Exact uniform test over rectangle (f,g) corners; not floating-point.
    for f in a['f']:
        for g in a['g']:
            assert f+(g-8)*lower >= 0
            assert f+(g-8)*upper <= 0

def test_sharper_than_prior_envelopes():
    a=tightened_bounds(fixture_reports())
    assert a['h'][0]>-F(1,10000000)
    assert a['ds'][0]>FLO/2
    assert a['ds'][1]<0
    assert a['v'][1]<0 and a['aux'][0]>0

def test_reject_changed_u3():
    d=fixture_reports();d['68u']['U3_upper_from_published_Step67b']='0'
    with pytest.raises(ArithmeticError,match='Taylor'):tightened_bounds(d)

def test_reject_wrong_sign_g():
    d=fixture_reports();d['68v']['G_U_center_interval']=['-2','1']
    with pytest.raises(ValueError,match='Signed'):tightened_bounds(d)

def test_reject_broadened_f():
    d=fixture_reports();d['68y']['F0_over_s_cubed_intersection']=['-1/1000000','1/1000000']
    with pytest.raises(ValueError,match='Signed'):tightened_bounds(d)

def test_reject_uncontained_improvement():
    d=fixture_reports();d['68y']['G_minus_Vstar_over_s_cubed']=['0','0']
    with pytest.raises(ArithmeticError,match='source certificate'):tightened_bounds(d)

def test_authenticated_full_run_when_originals_available():
    if not ROOT.exists() or not (ROOT/'gate2b-step68u-center-cubic-barrier.json').exists():
        pytest.skip('Authenticated upstream reports unavailable in local scratch')
    o=report(ROOT)
    assert o['signs_for_every_s_gt_zero']['G_minus_Vstar']=='NEGATIVE'
    assert o['signs_for_every_s_gt_zero']['G_U_minus_G_Ustar']=='POSITIVE'
    assert o['GATE_2B']=='OPEN' and o['JANUS_R']=='NOT_VALIDATED'
