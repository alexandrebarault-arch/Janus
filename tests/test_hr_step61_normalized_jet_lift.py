"""Standalone algebraic checks of ACTUAL Step55 normalized ODE jet structure."""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics.hr_step61_normalized_jet_lift import (
    ode_jet_formulas,center_frobenius_recurrence,center_coefficients_from_G_jets,
    certified_position_momentum_enclosures,shift_second_jet_consistency,manifest)


def test_ODE_first_second_third_radial_jet_chain():
    x=ode_jet_formulas()
    assert 'G' in str(x['Psecond']) and x['Pthird'].has(x['r'])
    assert sp.simplify(x['Psecond']-x['H'])==0


def test_true_G_partial_chain_uses_both_spatial_and_field_derivatives():
    x=ode_jet_formulas();s,U=x['s'],x['U']
    g=s*U**2+U**3+2
    h=sp.factor(x['Psecond'].subs(x['G'],g).doit())
    assert sp.simplify(h-(g+2*s*sp.diff(g,s)+(g-2*U)*sp.diff(g,U)))==0


def test_exact_radial_jet_identity_on_analytic_manufactured_ODE_solution():
    s,r,u0,a=sp.symbols('s r u0 a',real=True)
    u=u0+a*s
    # G defined precisely by the ODE along its solution; it has required
    # G(0,U)=3u0-U as a function for ALL U.
    G=3*u0-sp.Symbol('U')+5*a*s
    x=ode_jet_formulas();ss,uu=x['s'],x['U']
    values={ss:s,uu:u}
    g=G.subs('U',uu)
    # G(s,u0+a*s)=2u0+4a*s, matching r^-1 d/dr(r²u).
    assert sp.expand(g.subs(values)-(2*u0+4*a*s))==0
    direct=sp.expand(r*r*u.subs(s,r*r))
    for order,key in [(1,'Pprime'),(2,'Psecond'),(3,'Pthird')]:
        expr=x[key].subs(x['G'],g,simultaneous=True)
        # For a symbolic undefined function substitute derivatives too:
        expr=expr.doit().subs(values).subs(s,r*r)
        assert sp.simplify(expr-sp.diff(direct,r,order))==0


def test_frobenius_nonresonance_first_ten_terms():
    r=center_frobenius_recurrence(degree=10)
    assert r['resonance_denominators']==list(range(5,24,2))
    assert len(r['coefficients'])==10


def test_frobenius_first_two_coefficients_from_physical_center_condition():
    c=center_coefficients_from_G_jets()
    gs,gss,gsu,u0=sp.symbols('G_s G_ss G_sU U0')
    assert c['U1']==gs/5
    assert sp.simplify(c['U2']-((gss/2)+(gs*gsu/5))/7)==0
    assert c['P_third_over_r_center']==24*gs/5


def test_frobenius_manufactured_A_matches_first_two_coefficients():
    s,U,u0,a,b,c=sp.symbols('s U u0 a b c')
    G=3*u0-U+s*(a+b*(U-u0)+c*s)
    coeff=center_coefficients_from_G_jets()
    U1=a/5;U2=(b*U1+c)/7
    Ucurve=u0+U1*s+U2*s**2
    residual=sp.expand(2*s*sp.diff(Ucurve,s)-(G.subs(U,Ucurve)-2*Ucurve))
    assert residual.coeff(s,1)==0 and residual.coeff(s,2)==0
    assert sp.simplify(sp.factor(residual/s**3)+b*U2)==0


def test_center_pprime_psecond_pthird_parity():
    r,U0,U1,U2=sp.symbols('r U0 U1 U2')
    P=r**2*(U0+U1*r**2+U2*r**4)
    assert sp.diff(P,r).subs(r,0)==0
    assert sp.diff(P,r,2).subs(r,0)==2*U0
    assert sp.diff(P,r,3).subs(r,0)==0
    assert sp.factor(sp.diff(P,r,3)/r-(24*U1+120*U2*r**2))==0


def test_interval_certified_Step55_tube_to_P_and_Pprime():
    t=certified_position_momentum_enclosures()
    assert t['bound_P_minus_Pstar']==F(289,4_000_000)
    assert t['bound_Pprime_minus_Pstar_prime']==F(697,400_000)
    assert t['bound_Psecond'].startswith('NOT FROM')


def test_lack_of_high_jets_from_only_first_derivative_tube():
    # Pure mathematical counterexample, NOT an extra solution of physical G.
    # At a FIXED interior s0, choose amplitude~1/n, frequency n:
    # perturbation and its first derivative remain bounded, second grows n.
    s,s0,eps,n=sp.symbols('s s0 eps n',positive=True)
    w=eps/n*(sp.cos(n*(s-s0))-sp.cos(n*s0))
    assert sp.simplify(w.subs(s,0))==0
    assert sp.simplify(sp.diff(w,s).subs(s,s0))==0
    assert sp.simplify(sp.diff(w,s,2).subs(s,s0)+eps*n)==0
    # Derivative of P=r²U(r²) has 4 s² U_ss term.
    assert sp.simplify(4*s0*s0*sp.diff(w,s,2).subs(s,s0)+4*s0*s0*eps*n)==0


def test_step60_shift_second_jet_defect_exact_expression():
    x=shift_second_jet_consistency()
    assert sp.simplify(x['defect_Z2_unsubstituted']-x['defect_explicit'])==0
    assert sp.factor(x['defect_explicit'].subs(x['zr'],x['Z1']))==0


def test_negative_control_zr_zero_wrong_when_z1_nonzero():
    x=shift_second_jet_consistency()
    subs={x['z']:sp.Rational(1,5),x['K']:2,
          sp.Symbol('D1',real=True):3,sp.Symbol('K1',real=True):4}
    assert x['defect_explicit'].subs(subs).subs(x['zr'],0)!=0


def test_correct_stationary_shift_jet_not_treated_as_independent():
    x=shift_second_jet_consistency()
    z,zr=x['z'],x['zr']
    assert sp.diff(x['defect_explicit'],zr)!=0
    assert x['Z1']!=0


def test_frobenius_invalid_degree_rejected():
    with pytest.raises(ValueError):center_frobenius_recurrence(degree=0)
    with pytest.raises(ValueError):center_frobenius_recurrence(degree=101)


def test_ODE_second_jet_requires_G_derivatives_even_at_nonzero_s():
    x=ode_jet_formulas()
    assert x['Psecond'].has(sp.Derivative(x['G'],x['s']))
    assert x['Psecond'].has(sp.Derivative(x['G'],x['U']))


def test_status_remains_open_and_does_not_claim_historical_provider_run():
    x=manifest()
    assert not x['original_imported_in_this_standalone_run']
    assert not x['full_physical_step60_operator_evaluated_on_exact_step55_profile']
    assert x['GATE_2B']=='OPEN' and x['JANUS_R']=='NOT_VALIDATED'
