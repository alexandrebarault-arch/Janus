"""Exact conditional Step55 second-jet enclosure from FIRST partial derivatives.

The physical partial G_s differentiates G(s,u)=E(s,u,gamma(s)) with
respect to s at fixed u, INCLUDING every prescribed geometry derivative.
This is not an original Step55/58 physical execution or an interval proof.
"""
from fractions import Fraction as Q
import sympy as sp


def total_s_derivative(expr, s, u, geometry):
    """Return physical G_s with geometry(s) composed, keeping u fixed.

    geometry maps each independent auxiliary symbol v to its exact v(s).
    Do not differentiate E(s,u,v) holding v fixed and call that G_s.
    """
    if s in geometry or u in geometry:
        raise ValueError('s and u must be independent')
    composed = expr.subs(geometry, simultaneous=True)
    return sp.diff(composed, s), composed


def exact_ode_jet(s, u, g, gs, gu):
    """Scalar rational ODE-consistent jets, s>0; no dense P derivatives."""
    s,u,g,gs,gu = map(Q, (s,u,g,gs,gu))
    if s <= 0:
        raise ValueError('s must be positive; centre requires separate chart')
    f=(g-2*u)/(2*s)
    uss=(gs+(gu-4)*f)/(2*s)
    radial=g+2*s*gs+gu*(g-2*u)
    assert radial == 2*u+10*s*f+4*s*s*uss
    return {'U_s':f, 'U_ss':uss, 'pLf_second':radial,
            'pLf':s*u, 'pLf_prime_over_r':g}


class RInterval:
    """Exact rational closed interval (simple dependency-safe enclosure)."""
    def __init__(self, lo, hi=None):
        self.lo=Q(lo); self.hi=Q(lo if hi is None else hi)
        if self.lo>self.hi: raise ValueError('reversed interval')
    @staticmethod
    def wrap(x): return x if isinstance(x,RInterval) else RInterval(x)
    def __add__(self, other):
        o=self.wrap(other); return RInterval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return RInterval(-self.hi,-self.lo)
    def __sub__(self, other): return self+-self.wrap(other)
    def __rsub__(self, other): return self.wrap(other)+-self
    def __mul__(self, other):
        o=self.wrap(other)
        p=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
        return RInterval(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self, other):
        o=self.wrap(other)
        if o.lo<=0<=o.hi: raise ZeroDivisionError('denominator crosses zero')
        return self*RInterval(1/o.hi,1/o.lo)
    def contains(self, x): return self.lo<=Q(x)<=self.hi
    def __repr__(self): return f'[{self.lo},{self.hi}]'


def enclose_second_jet(s, u_box, g_box, gs_box, gu_box):
    """Rigorous IF input boxes are physical outward enclosures at exact s.

    No G_sU, G_UU or Lipschitz constant is needed.  This is generally
    wider than a pointwise sensitivity enclosure; it cannot certify A/B/E
    without downstream original Step58 interval evaluation.
    """
    s=Q(s)
    if s<=0: raise ValueError('s must be positive')
    u,g,gs,gu=map(RInterval.wrap,(u_box,g_box,gs_box,gu_box))
    f=(g-2*u)/(2*s)
    uss=(gs+(gu-4)*f)/(2*s)
    radial=g+2*s*gs+gu*(g-2*u)
    return {'U_s':f,'U_ss':uss,'pLf_second':radial,
            'pLf':s*u,'pLf_prime_over_r':g}


def symbolic_residuals():
    s,u=sp.symbols('s u',positive=True)
    g=sp.Function('G')(s,u)
    f=(g-2*u)/(2*s)
    q=(sp.diff(g,s)+(sp.diff(g,u)-4)*f)/(2*s)
    radial=g+2*s*sp.diff(g,s)+sp.diff(g,u)*(g-2*u)
    return [sp.simplify(2*u+2*s*f-g),
            sp.simplify(2*u+10*s*f+4*s*s*q-radial)]
