"""Independent exact algebra tests for Step68ad-B1 polarization."""
from fractions import Fraction as F
import sys
from pathlib import Path
import pytest
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from numerics.hr_step68ad_b_directional_polarization import (
    reconstruct,source_R2,source_R3)

s,u,t=sp.symbols('s u t')

def series(expr,ds,du,ss=F(1,7),uu=F(-2,9)):
    poly=sp.expand(expr.subs({s:sp.Rational(ss.numerator,ss.denominator)+ds*t,
                              u:sp.Rational(uu.numerator,uu.denominator)+du*t}))
    return [F(poly.coeff(t,k)) for k in range(4)]

def polar(expr):
    return reconstruct(*(series(expr,*d) for d in [(1,0),(0,1),(1,1),(1,-1)]))

@pytest.mark.parametrize('a,b',[(0,0),(1,0),(0,1),(2,0),(1,1),(0,2),
                                (3,0),(2,1),(1,2),(0,3)])
def test_monomials_all_ten_mixed_derivatives(a,b):
    expr=s**a*u**b
    out=polar(expr)
    orders={'G':(0,0),'G_s':(1,0),'G_U':(0,1),
        'G_ss':(2,0),'G_sU':(1,1),'G_UU':(0,2),
        'G_sss':(3,0),'G_ssU':(2,1),'G_sUU':(1,2),'G_UUU':(0,3)}
    for key,(i,j) in orders.items():
        truth=sp.diff(expr,s,i,u,j).subs({s:sp.Rational(1,7),u:sp.Rational(-2,9)})
        assert out[key]==F(truth),(a,b,key,out[key],truth)


def test_general_cubic_with_cross_terms():
    expr=F(5,7)*s**3*u**3-3*s**2*u+2*s*u**2+11*s-17*u+13
    # only total degree <=3 in t matters; no approximation involved.
    out=polar(expr)
    for key,di,dj in [('G_ssU',2,1),('G_sUU',1,2),('G_UUU',0,3)]:
        truth=sp.diff(expr,s,di,u,dj).subs({s:sp.Rational(1,7),u:sp.Rational(-2,9)})
        assert out[key]==F(truth)


def test_r2_r3_independent_sympy_chain_rule():
    expr=7*s**3+2*s**2*u+3*s*u**2+5*u**3-11*s*u
    p=polar(expr)
    us=F(3,11);uss=F(-7,13)
    r2=source_R2(p,us);r3=source_R3(p,us,uss)
    U=sp.Function('U')(s)
    G=expr.subs(u,U)
    gu=sp.diff(expr,u).subs(u,U)
    for n,result in [(2,r2),(3,r3)]:
        R=sp.diff(G,s,n)-gu*sp.diff(U,s,n)
        expected=R.subs({s:sp.Rational(1,7),U:sp.Rational(-2,9),
            sp.diff(U,s):sp.Rational(3,11),sp.diff(U,s,2):sp.Rational(-7,13)})
        assert F(expected)==result


def test_reject_missing_direction_coefficients():
    with pytest.raises(ValueError,match='degree-three'):
        reconstruct([0,1,2],[0]*4,[0]*4,[0]*4)


def test_sign_of_minus_direction_required():
    expr=s**2*u+s*u**2
    exact=polar(expr)
    assert exact['G_ssU']==2
    assert exact['G_sUU']==2


def test_nonlinear_original_G_not_assumed_affine_in_U():
    p=polar(s**2*u**3+u**3)
    assert p['G_UU']!=0 and p['G_UUU']!=0


def test_no_finite_differences_in_source():
    text=(ROOT/'numerics'/'hr_step68ad_b_directional_polarization.py').read_text()
    assert 'finite differences' in text
    assert 'j.jet_G(sj,uj)' in text


def test_physical_certificate_rejects_invalid_cell_counts_before_import():
    from numerics.hr_step68ad_b_directional_polarization import physical_R2_global
    with pytest.raises(ValueError,match='cell count'):
        physical_R2_global('/nonexistent',cells=0)
    with pytest.raises(ValueError,match='cell count'):
        physical_R2_global('/nonexistent',cells=2049)


class ExactBox:
    """Independent Fraction interval oracle, not the production Step55 I."""
    def __init__(self,lo,hi=None):
        self.lo=F(lo);self.hi=F(lo if hi is None else hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        if not isinstance(o,ExactBox):o=ExactBox(o)
        return ExactBox(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return ExactBox(-self.hi,-self.lo)
    def __sub__(self,o):return self+-o
    def __rsub__(self,o):return ExactBox(o)+-self
    def __mul__(self,o):
        if not isinstance(o,ExactBox):o=ExactBox(o)
        p=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return ExactBox(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,ExactBox):o=ExactBox(o)
        assert o.lo>0
        return self*ExactBox(1/o.hi,1/o.lo)
    def __pow__(self,n):
        assert n>=0
        if n==0:return ExactBox(1)
        out=ExactBox(1)
        for _ in range(n):out=out*self
        return out


def test_outward_interval_polarization_encloses_exact_mixed_derivatives():
    expr=2*s**3*u**2-7*s**2*u+3*s*u**3+u**3
    exact=polar(expr)
    eps=F(1,10**9)
    dirs=[(1,0),(0,1),(1,1),(1,-1)]
    coefficients=[[ExactBox(c-eps,c+eps) for c in series(expr,*d)] for d in dirs]
    boxes=reconstruct(*coefficients)
    for key,val in exact.items():
        assert boxes[key].lo<=val<=boxes[key].hi,key
    us=ExactBox(F(3,11)-eps,F(3,11)+eps)
    uss=ExactBox(F(-7,13)-eps,F(-7,13)+eps)
    p=polar(expr)
    assert source_R2(boxes,us).lo<=source_R2(p,F(3,11))<=source_R2(boxes,us).hi
    assert source_R3(boxes,us,uss).lo<=source_R3(p,F(3,11),F(-7,13))<=source_R3(boxes,us,uss).hi
