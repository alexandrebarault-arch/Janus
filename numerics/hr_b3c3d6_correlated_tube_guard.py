"""Exact rational Bernstein guard for P(s)-Ustar(s), not separate hulls.

Ustar(s)=U0+U1*s+U2*s**2, with outward rational intervals for Uj.
P is the exact rational DOP853 dense polynomial in x=(s-t0)/h.
A PASS proves |P(s)-Ustar(s)|<=delta on the entire requested cell,
for every coefficient choice inside the supplied intervals. No ODE error
or true-solution tube is proved by this helper alone.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb


@dataclass(frozen=True)
class RI:
    lo: Q
    hi: Q

    def __post_init__(self):
        object.__setattr__(self, 'lo', Q(self.lo))
        object.__setattr__(self, 'hi', Q(self.hi))
        if self.lo > self.hi:
            raise ValueError('reversed interval')

    @staticmethod
    def coerce(v):
        if isinstance(v, RI):
            return v
        if isinstance(v, (tuple, list)) and len(v) == 2:
            return RI(Q(v[0]), Q(v[1]))
        return RI(Q(v), Q(v))

    def __add__(self, v):
        v = RI.coerce(v)
        return RI(self.lo + v.lo, self.hi + v.hi)

    __radd__ = __add__

    def __neg__(self):
        return RI(-self.hi, -self.lo)

    def __sub__(self, v):
        return self + -RI.coerce(v)

    def times(self, q):
        q = Q(q)
        return RI(self.lo*q, self.hi*q) if q >= 0 else RI(self.hi*q, self.lo*q)


def bernstein_interval(coefficients, a, b):
    """Enclose interval-coefficient polynomial on x in [a,b]."""
    a, b = Q(a), Q(b)
    if b < a:
        raise ValueError('reversed cell')
    p = [RI(0, 0)]
    for c in reversed(coefficients):
        old = p
        p = [RI(0, 0) for _ in range(len(old)+1)]
        for j, v in enumerate(old):
            p[j] = p[j] + v.times(a)
            p[j+1] = p[j+1] + v.times(b-a)
        p[0] = p[0] + RI.coerce(c)
    while len(p) > 1 and p[-1] == RI(0, 0):
        p.pop()
    n = len(p)-1
    bs = [sum((p[j].times(Q(comb(k,j),comb(n,j))) for j in range(k+1)), RI(0,0))
          for k in range(n+1)]
    return RI(min(v.lo for v in bs), max(v.hi for v in bs))


def difference_enclosure(p, t0, h, a, b, center_coefficients):
    """Return exact enclosure for P(x)-[U0+U1*(t0+h*x)+U2*(t0+h*x)^2]."""
    t0, h = Q(t0), Q(h)
    if h <= 0:
        raise ValueError('positive h required')
    if len(center_coefficients) != 3:
        raise ValueError('center quadratic coefficients required')
    u0, u1, u2 = map(RI.coerce, center_coefficients)
    star = [u0 + u1.times(t0) + u2.times(t0*t0),
            u1.times(h) + u2.times(2*t0*h), u2.times(h*h)]
    n = max(len(p), 3)
    coeff = [RI.coerce(Q(p[j]) if j < len(p) else 0) -
             (star[j] if j < 3 else RI(0,0)) for j in range(n)]
    return bernstein_interval(coeff, a, b)


def certify_correlated_tube(p, t0, h, a, b, center_coefficients, delta):
    """Fail closed if exact Bernstein interval does not fit the center tube."""
    delta = Q(delta)
    if delta < 0:
        raise ValueError('negative tube width')
    result = difference_enclosure(p,t0,h,a,b,center_coefficients)
    if result.lo < -delta or result.hi > delta:
        raise ArithmeticError(f'correlated center tube not proved: {result}')
    return result


def physical_center_intervals(u0, u1, u2, scale):
    """Convert Step55 outward-integer I endpoints to exact rational intervals."""
    scale = Q(scale)
    if scale <= 0:
        raise ValueError('positive outward-integer scale required')
    return tuple(RI(Q(v.lo)/scale, Q(v.hi)/scale) for v in (u0,u1,u2))


def certify_dense_cells(p, t0, h, xmax, center_coefficients, delta, subcells=256):
    """Certify the correlated tube on EVERY exact dense subcell, or raise."""
    xmax = Q(xmax)
    if not (xmax > 0 and isinstance(subcells,int) and subcells >= 1):
        raise ValueError('positive domain and subcell count required')
    return [certify_correlated_tube(p,t0,h,xmax*Q(i,subcells),
                                  xmax*Q(i+1,subcells),center_coefficients,delta)
            for i in range(subcells)]


def physical_step55_dense_defect_correlated(dense, subcells=256):
    """Physical adapter: correlated tube first, then outward Step55 defect.

    Requires the authentic Step45/46/55 modules and their SHA checks.
    Still conditional on true center initial error and G_U tube certificate.
    """
    from .hr_b3c3d6_dop853_dense_rational_defect import (
        dop853_dense_coefficients,dense_exact_domain,interval_step_defect)
    from .hr_step55_global_barrier import G,I,S,U0,U1,U2
    from .hr_step55_normalized_secondary import check_original_source_blobs
    check_original_source_blobs()
    t0,_,h,xmax=dense_exact_domain(dense)
    p=dop853_dense_coefficients(dense)
    center=physical_center_intervals(U0,U1,U2,S)
    certified=certify_dense_cells(p,t0,h,xmax,center,Q(1,10000),subcells)
    cells=interval_step_defect(dense,G,I,subcells,tube_guard=None)
    bound=Q(max(max(abs(c.lo),abs(c.hi)) for c in cells),S)
    return {'bound':bound,'subcells':subcells,
            'correlated_center_tube':'PASS_ALL_'+str(len(certified))+'_CELLS',
            'scope':'EXACT_DENSE_INTERPOLANT_CORRELATED_TUBE_AND_CONTINUOUS_DEFECT',
            'center_initial_error':'NOT_CERTIFIED',
            'G_U_shared_tube':'SEPARATE_STEP63_CERTIFICATE_REQUIRED',
            'Step58_six_coefficients':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
