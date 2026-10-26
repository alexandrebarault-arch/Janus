"""Independent symbolic examples, not seven-cell physical evaluations."""
import sympy as sp
import pytest
from numerics.hr_step68ad_c2d2b_shift_second_jet import certify

@pytest.mark.parametrize('d0,d1,k0,k1',[
 (sp.Rational(1,5),sp.Rational(1,10),sp.Rational(1,4),sp.Rational(1,20)),
 (-sp.Rational(2,7),sp.Rational(1,8),sp.Rational(3,5),sp.Rational(1,9)),
 (0,sp.Rational(1,6),sp.Rational(1,3),0),
 (sp.Rational(2,5),0,sp.Rational(2,3),0),
 (sp.Rational(1,8),-sp.Rational(1,9),sp.Rational(1,2),-sp.Rational(1,10)),
 (sp.Rational(1,17),sp.Rational(1,31),sp.Rational(3,11),sp.Rational(1,13)),
])
def test_independent_polynomial_center(d0,d1,k0,k1):
    r=sp.symbols('r',real=True)
    s=r*r
    d=d0+d1*s
    k=k0+k1*s
    z=r*d/sp.sqrt(k*k+s*d*d)
    Aprime=d1/k0-d0*k1/k0**2-d0**3/(2*k0**3)
    assert sp.simplify(sp.diff(z,r).subs(r,0)-d0/k0)==0
    assert sp.simplify(sp.diff(z,r,2).subs(r,0))==0
    assert sp.simplify(sp.diff(z,r,3).subs(r,0)-6*Aprime)==0

def test_symbolic_certification():
    report=certify()
    assert report['symbolic_identities']==10
    assert report['all_exact'] is True
    assert report['original_step58_seven_cells']=='NOT_EXECUTED'
    assert report['original_step60_quotient']=='NOT_EXECUTED'

def test_positive_K_stationarity_exact():
    D=sp.Rational(2,3);K=sp.Rational(4,5)
    z=D/sp.sqrt(D**2+K**2)
    assert sp.simplify(D-K*z/sp.sqrt(1-z*z))==0

def test_negative_K_branch_is_not_same_formula():
    D=sp.Rational(2,3);K=-sp.Rational(4,5)
    z=D/sp.sqrt(D**2+K**2)
    assert sp.simplify(D-K*z/sp.sqrt(1-z*z))!=0

def test_unfactored_center_requires_assumption():
    # D=O(r) rather than O(r^3) does not give z=O(r).
    r=sp.symbols('r',positive=True)
    D=r;K=r*r
    z=D/sp.sqrt(D*D+K*K)
    assert sp.limit(z,r,0,dir='+')==1
