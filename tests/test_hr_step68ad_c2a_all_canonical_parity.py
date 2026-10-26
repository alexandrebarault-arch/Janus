"""Exact SymPy cross-derivative oracle for 68ad-C2a (not physical interval tests)."""
from fractions import Fraction as F
from pathlib import Path
import pytest
import sympy as sp
from numerics.hr_step68ad_c2a_all_canonical_parity import (
    radial_jet,dust_clock_jet,all_canonical_jets,
    CANONICAL_PROFILE_POWERS,ALL_FIELDS,certified_scope,
    authenticate_temporal_sources,git_blob)

r=sp.symbols('r',real=True)
s=sp.symbols('s',real=True)
f=sp.Function('F')(s)

@pytest.mark.parametrize('power',[0,1,2])
def test_chain_rule_original_radial_power_symbolically(power):
    original=r**power*f.subs(s,r*r)
    fvals=[sp.diff(f,s,n).subs(s,r*r) for n in range(4)]
    actual=radial_jet(power,r,*fvals)
    for order in range(4):
        assert sp.simplify(sp.diff(original,r,order)-actual[order])==0

@pytest.mark.parametrize('power',[0,1,2])
def test_chain_rule_exact_rational_polynomial(power):
    poly=F(2,3)+F(5,7)*s-F(11,13)*s**2+F(17,19)*s**3
    rr=F(1,64)
    vals=[sp.diff(poly,s,n).subs(s,sp.Rational(rr.numerator,rr.denominator)**2)
          for n in range(4)]
    result=radial_jet(power,sp.Rational(rr.numerator,rr.denominator),*vals)
    expected=sp.Rational(rr.numerator,rr.denominator)**power*poly.subs(s,sp.Rational(rr.numerator,rr.denominator)**2)
    for n in range(4):
        assert result[n]==sp.diff(r**power*poly.subs(s,r*r),r,n).subs(r,sp.Rational(rr.numerator,rr.denominator))

def test_clock_derivatives_exact():
    k=sp.symbols('k')
    L=sp.Function('L')(s)
    Lr=L.subs(s,r*r)
    jet=dust_clock_jet(r,k,Lr,sp.diff(L,s).subs(s,r*r),sp.diff(L,s,2).subs(s,r*r))
    assert jet[0]==0
    assert sp.simplify(jet[1]-r*k*Lr)==0
    assert sp.simplify(jet[2]-sp.diff(r*k*Lr,r))==0
    assert sp.simplify(jet[3]-sp.diff(r*k*Lr,r,2))==0

def test_all_twelve_fields_order_and_parity():
    profiles={name:(F(1),F(2),F(3),F(4)) for name in CANONICAL_PROFILE_POWERS}
    jets=all_canonical_jets(F(0),profiles,F(5),F(7))
    assert tuple(jets)==ALL_FIELDS and len(jets)==12
    for name in ('Lg','Lf','pLg','pLf','pg','pf','tg','tf'):
        assert jets[name][3]==0
    for name in ('Sg','Sf','pSg','pSf'):
        assert jets[name][3]==12
    assert jets['tg'][2]==5 and jets['tf'][2]==7
    assert jets['pLf'][2]==2 and jets['pLf'][3]==0

def test_original_pLf_c1_identity_exact():
    u0,u1,u2,u3=sp.symbols('U Us Uss Usss')
    x=radial_jet(2,r,u0,u1,u2,u3)
    assert sp.simplify(x[3]/r-(24*u1+36*r*r*u2+8*r**4*u3))==0

def test_center_no_singular_division_and_clock_gauge():
    vals=[F(2),F(3),F(4),F(5)]
    for k in range(3):
        result=radial_jet(k,F(0),*vals)
        assert len(result)==4 and all(isinstance(x,F) for x in result)
    clock=dust_clock_jet(F(0),F(3),*vals[:3])
    assert clock==(0,F(0),F(6),F(0))

def test_invalid_profile_power_fails_closed():
    with pytest.raises(ValueError):radial_jet(3,F(0),1,2,3,4)

def test_missing_or_extra_profile_fails_closed():
    profiles={name:(1,2,3,4) for name in CANONICAL_PROFILE_POWERS}
    for altered in ({k:v for k,v in profiles.items() if k!='pSf'},
                    {**profiles,'ghost':(1,2,3,4)}):
        with pytest.raises(ValueError):all_canonical_jets(F(0),altered,1,1)

def test_missing_derivative_fails_closed():
    profiles={name:(1,2,3,4) for name in CANONICAL_PROFILE_POWERS}
    profiles['pf']=(1,2,3)
    with pytest.raises(ValueError):all_canonical_jets(F(0),profiles,1,1)

def test_pins_reject_tampering(tmp_path):
    for name in ('hr_step68o_temporal_interval_annulus.py','hr_step58_temporal_operator.py',
                 'hr_step60_full_constraint_prolongation.py'):
        (tmp_path/name).write_text('not original')
    with pytest.raises(ValueError,match='source changed'):
        authenticate_temporal_sources(tmp_path)

def test_explicit_scope_does_not_claim_temporal_result():
    m=certified_scope()
    assert len(m['all_twelve_canonical_fields'])==12
    assert m['physical_interval_profile_derivatives']=='REQUIRED_NOT_COMPUTED'
    assert m['temporal_Step58_AN_AM']=='NOT_EVALUATED'
    assert m['GATE_2B']=='OPEN' and m['JANUS_R']=='NOT_VALIDATED'
