"""Step62 exact original six-pair Step55 physical G_UU and full-interval sign.

Imports BYTE IDENTICAL original Step45/46/55 symbolic files.  The benchmark
radial metric inputs below are a literal rational transcription of Step55's
hr_step55_global_barrier.py; the latter file is NOT imported in this targeted
worktree, and its byte identity is NOT asserted here.

The result is a uniform exact-rational bound on G_UU, independent of U,
for the fixed benchmark radial family. It is NOT a certificate of G_s,
G_U,G_ss,G_sU, or the Step60 four lapse coefficients/Dirac rank.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import sympy as sp
from .hr_step55_normalized_secondary import normalized_symbolic,check_original_source_blobs

PINNED={
  'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
  'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
  'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862'
}


def check_sources():
    root=Path(__file__).resolve().parent
    for name,pinned in PINNED.items():
        data=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if actual != pinned:
            raise ValueError('historical source mismatch '+name+': '+actual)
    assert check_original_source_blobs()
    return dict(PINNED)


@lru_cache(1)
def curvature_identity():
    check_sources()
    G,s,U,v=normalized_symbolic()
    d={str(k):k for k in G.free_symbols}
    lf,lg,tf,mf,b1,b2,b3,z1=[d[k] for k in
         ('Lf0','Lg0','tf0','Mf2','beta1','beta2','beta3','z1')]
    root=sp.sqrt(1-s*z1*z1)
    A=lf**2*b3+2*lf*lg*b2+lg**2*b1
    T=(3*lf**2*b3+2*lf*lg*b2-lg**2*b1)*root+4*lf*lg*b2+4*lg**2*b1
    formula=-s*tf*T/(2*lf*mf*sp.sqrt(lf**2+s*tf**2)*root*A)
    guu=sp.factor(sp.diff(G,U,2))
    assert sp.cancel(sp.together(guu-formula))==0
    assert sp.Poly(G,U).degree()==2
    assert sp.diff(G,U,3)==0
    assert guu.subs(s,0)==0
    # For source symbols Sfr0/Lf0, exact center U-slope is -Sfr0/Lf0.
    assert sp.cancel(sp.together(sp.diff(G,U).subs(s,0)+d['Sfr0']/lf))==0
    return dict(G=G,s=s,U=U,guu=guu,At=A,T=T,root=root,
                physical_formula=formula,variables=d,
                polynomial_U_degree=2,source_check=PINNED.copy())


class Interval:
    """Exact Fraction-endpoint interval arithmetic (NO floats)."""
    def __init__(self,a,b=None):
        if isinstance(a,Interval) and b is None:
            self.lo,self.hi=a.lo,a.hi
        else:
            self.lo=F(a);self.hi=F(a if b is None else b)
        if self.lo>self.hi:raise ValueError('backward interval')
    def __add__(self,o):
        o=Interval(o);return Interval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,o):return self+-Interval(o)
    def __rsub__(self,o):return Interval(o)+-self
    def __mul__(self,o):
        o=Interval(o)
        v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return Interval(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=Interval(o)
        if o.lo<=0<=o.hi:raise ZeroDivisionError('interval crosses zero')
        return self*Interval(F(1,o.hi),F(1,o.lo))
    def __rtruediv__(self,o):return Interval(o)/self
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('positive integer power only')
        if n==0:return Interval(1)
        if n%2==0:
            vals=[self.lo**n,self.hi**n]
            return Interval(0 if self.lo<=0<=self.hi else min(vals),max(vals))
        return Interval(self.lo**n,self.hi**n)
    def bounds(self):return str(self.lo),str(self.hi)


@lru_cache(1)
def benchmark_rational_certificate():
    """Uniform G_UU interval for s in [0,289/400], U arbitrary.

    Uses positive denominator, certified simple rational elementary
    sqrt envelopes, all computations EXACT Fraction (no sampling).
    Square-root enclosures verified by squaring rational endpoints.
    """
    smax=F('0.7225')
    a=F('.4'); y=F('.5787707228025044');b=a*y
    cg=F('.0015');cf=F('-.0012')
    kf=F('-.0016');z1=F('.004')
    mf=F('.10879548725')**2
    beta1=F(1);beta2=F('-4.2383993109');beta3=F('13.6801214252')
    s=Interval(0,smax)
    lg=Interval(a,a*(1+cg*smax)**2)
    lf=Interval(b*(1+cf*smax)**2,b)
    # Root R1=sqrt(1-s*z1²): use exact loose rational enclosure
    rmin=F('0.99999')
    assert rmin*rmin < 1-smax*z1*z1
    r1=Interval(rmin,1)
    # Root R2=sqrt(1+s*kf²): both exact rational enclosures
    rmax=F('1.00001')
    assert rmax*rmax > 1+smax*kf*kf
    r2=Interval(1,rmax)
    At=lf**2*beta3+2*lf*lg*beta2+lg**2*beta1
    T=(3*lf**2*beta3+2*lf*lg*beta2-lg**2*beta1)*r1+4*lf*lg*beta2+4*lg**2*beta1
    if not At.lo>0:raise AssertionError('interaction At positive sign unproved')
    if not T.lo>0:raise AssertionError('quadratic curvature numerator sign unproved')
    # tf0=kf*Lf0; sqrt(Lf0²+s tf0²)=Lf0*sqrt(1+s kf²), Lf0>0.
    curvature=s*(-kf)*T/(2*lf*mf*r2*r1*At)
    if not (curvature.lo>=0 and curvature.hi<F(1)):
        raise AssertionError('needed uniform curvature range 0<=G_UU<1 not proved')
    return dict(s_interval=('0',str(smax)),Lg=lg.bounds(),Lf=lf.bounds(),
                sqrt1=r1.bounds(),sqrt2=r2.bounds(),At=At.bounds(),
                numerator=T.bounds(),curvature=curvature.bounds(),
                exact_conclusion='0 <= G_UU(s,U) < 1 on [0,289/400], independent of U; s>0 -> strictly positive',
                caveat='Certified benchmark only; not yet bounds on G_s,G_U,G_ss,G_sU or temporal Dirac rank')


def certified_tube_linearization():
    """Exact quadratic Taylor control ON true Step55 |U-Ustar|<=1/10000.

    G_UU is independent of U. On the Step55 physical benchmark and all
    s in [0,289/400], 0<=G_UU<337/500, hence exactly
       |G_U(s,U)-G_U(s,Ustar)| < 337/5000000,
       |G(s,U)-G(s,Ustar)-G_U(s,Ustar)*(U-Ustar)|
           < 337/100000000000.
    Bounds involve no floating point, and do not assert control of G_s.
    """
    b=benchmark_rational_certificate()
    upper=F(b['curvature'][1]);limit=F(337,500)
    assert upper<limit
    tube=F(1,10000)
    deriv_limit=limit*tube
    remainder_limit=limit*tube*tube/2
    assert deriv_limit==F(337,5_000_000)
    assert remainder_limit==F(337,100_000_000_000)
    return dict(U_delta=tube,curvature_upper_strict=limit,
                Gu_difference_strict=deriv_limit,
                Taylor_quadratic_remainder_strict=remainder_limit,
                scope='Step55 exact U tube around Ustar, same benchmark geometry; does NOT bound G_s')


def manifest():
    c=curvature_identity();b=benchmark_rational_certificate();t=certified_tube_linearization()
    return dict(step=62,original_source_git_blobs=PINNED,
                imported_actual_physical_G=True,polynomial_degree_U=2,
                G_UU_expression=str(c['guu']),G_UUU_exact_zero=True,
                benchmark_interval=b,certified_Taylor_tube={k:str(v) for k,v in t.items()},
                physical_temporal_rank='NOT_COMPUTED',
                GATE_2B='OPEN',JANUS_R='NOT_VALIDATED')

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))
