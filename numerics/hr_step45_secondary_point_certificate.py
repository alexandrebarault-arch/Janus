"""Rational interval proof that the FROZEN Step41 primary profile has C != 0.

Uses the analytically derived, no-radial-difference C=K00-(K01)' from
hr_step45_exact_physical_ward, original Step33g primary algebra and exact
terminating-decimal benchmark constants. Each frozen Step41 binary64 f_delta
coefficient is interpreted EXACTLY using Fraction.from_float. Square roots
are outward enclosed by integer arithmetic to 10^-70. The RESULT applies
only to this frozen approximate profile, not a theorem forbidding exact
secondary-constrained data, nor a generic physical cosmology no-go.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, isfinite
import json
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward

FDELTA=tuple(F.from_float(float(x)) for x in
    (-2.1921905214999423e-5,0.,.0015479757723131573,0.,
     -2.0933708880890434e-5,0.,-1.757101536020765e-7,0.,
     -2.9380881416697167e-9))

@dataclass(frozen=True)
class IV:
    lo:F
    hi:F
    def __post_init__(self):
        object.__setattr__(self,'lo',F(self.lo))
        object.__setattr__(self,'hi',F(self.hi))
        if self.lo>self.hi:raise ValueError('reversed interval')
    @classmethod
    def p(cls,v):return cls(F(v),F(v))
    @staticmethod
    def c(v):return v if isinstance(v,IV) else IV.p(v)
    def __add__(self,b):
        b=self.c(b);return IV(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,b):return self+-self.c(b)
    def __rsub__(self,b):return self.c(b)+-self
    def __mul__(self,b):
        b=self.c(b)
        p=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return IV(min(p),max(p))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('zero in interval')
        return IV(1/self.hi,1/self.lo)
    def __truediv__(self,b):return self*self.c(b).inv()
    def __rtruediv__(self,b):return self.c(b)*self.inv()
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('nonnegative integer power')
        if n==0:return IV.p(1)
        if n&1:return IV(self.lo**n,self.hi**n)
        if self.lo<=0<=self.hi:return IV(0,max(self.lo**n,self.hi**n))
        return IV(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
    def sqrt(self,digits=70):
        if self.lo<0:raise ValueError('negative radicand')
        d=10**digits
        def down(f):return F(isqrt((f.numerator*d*d)//f.denominator),d)
        return IV(down(self.lo),down(self.hi)+F(1,d))


def frozen_primary_at(r):
    """All 12 canonical q and required q' at a rational radial coordinate.

    Every operation uses exact rational arithmetic with outward-enclosed
    algebraic radicals. Includes two independently reconstructed dust
    momenta and both radial momentum primaries. No numerical derivatives.
    """
    r=F(r)
    if not 0<r<=F('.85'):raise ValueError('only positive interior/endpoint radius')
    a=F('.4');y=F('.5787707228025044');b=a*y
    mg=F(1);mf=F('.10879548725')**2;m2=F('23.3348939346')
    b0,b1,b2,b3,b4=map(F,('0','1','-4.2383993109','13.6801214252','-38.5117901844'))
    cg=F('.0015');cf=F('-.0012');zscale=F('.004')
    kg=F('.0012');kf=F('-.0016');s=r*r
    vg=b0+3*b1*y+3*b2*y*y+b3*y**3
    H=IV.p(F('.9')/(3*a**3)+m2*vg/3).sqrt()
    Pg=-2*a*a*H;Pf=-2*mf*b*a*H
    ug=1+cg*s;uf=1+cf*s
    Lg=a*ug**2;Lf=b*uf**2;Sg=r*Lg;Sf=r*Lf
    Lgr=4*a*cg*r*ug;Lfr=4*b*cf*r*uf
    Sgr=a*ug*(1+5*cg*s);Sfr=b*uf*(1+5*cf*s)
    plg=Pg*s*(1+F(5,2)*cg*s)
    plgr=2*r*(1+5*cg*s)*Pg
    Qf=Pf+sum(FDELTA[2*k]*s**k for k in range(5))
    plf=Pf*s*(1+F(5,2)*cf*s)+sum(FDELTA[2*k]*(s**(k+1)/F(k+1)+5*cf*s**(k+2)/F(k+2)) for k in range(5))
    plfr=2*r*(1+5*cf*s)*Qf
    tgr=kg*r*Lg;tfr=kf*r*Lf
    z=zscale*r;zr=zscale;root=IV.p(1-z*z).sqrt()
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    K=m2*mg*Lg*Lf*At;Dg=K*z/root
    Wg=m2*mg*(Lg*A0+Lf*At*root)
    Wf=m2*mg*(Lf*Af+Lg*At*root)
    Rg=-48*cg/(a*a*ug**5);Rf=-48*cf/(b*b*uf**5)
    def dust(L,S,Sr,pl,plr,mi,tr,D,W,R3):
        fac=pl/(2*mi*S*Sr)
        kin=L*pl*pl/(4*mi*S*S)
        curvature=-mi*L*S*S*R3/2
        numerator=kin-fac*(D+L*plr)+curvature+z*Dg/L+W
        beta=IV.p(1+(tr/L)**2).sqrt()+fac*tr
        if beta.lo<=0:raise ArithmeticError('nonpositive dust coefficient')
        p=-numerator/beta
        pS=(D+L*plr-p*tr)/Sr
        return p,pS
    pg,psg=dust(Lg,Sg,Sgr,plg,plgr,mg,tgr,Dg,Wg,Rg)
    pf,psf=dust(Lf,Sf,Sfr,plf,plfr,mf,tfr,-Dg,Wf,Rf)
    q={'Lg':Lg,'pLg':plg,'Sg':Sg,'pSg':psg,'tg':0,'pg':pg,
       'Lf':Lf,'pLf':plf,'Sf':Sf,'pSf':psf,'tf':0,'pf':pf,
       'Lgr':Lgr,'pLgr':plgr,'Sgr':Sgr,'tgr':tgr,
       'Lfr':Lfr,'pLfr':plfr,'Sfr':Sfr,'tfr':tfr,
       'z':z,'zr':zr,'zrr':0,
       'Mg2':mg,'Mf2':mf,'m2':m2,
       **dict(zip(('beta0','beta1','beta2','beta3','beta4'),(b0,b1,b2,b3,b4)))}
    return {k:IV.c(v) for k,v in q.items()}


def evaluate_expr(expr, values):
    """Recursive exact rational enclosure for a SymPy arithmetic expression."""
    if expr.is_Symbol:
        return values[str(expr)]
    if expr.is_Rational:return IV.p(F(int(expr.p),int(expr.q)))
    if expr.is_Add:
        out=IV.p(0)
        for term in expr.args:out+=evaluate_expr(term,values)
        return out
    if expr.is_Mul:
        out=IV.p(1)
        for term in expr.args:out*=evaluate_expr(term,values)
        return out
    if expr.is_Pow:
        base=evaluate_expr(expr.base,values)
        exponent=sp.Rational(expr.exp)
        if exponent.q==1:
            n=int(exponent)
            return base**n if n>=0 else (base**(-n)).inv()
        if exponent.q==2:
            n=int(exponent.p)
            return (base**n).sqrt() if n>=0 else (base**(-n)).sqrt().inv()
    raise TypeError(f'unsupported symbolic node: {type(expr)} / {str(expr)[:100]}')


def certify_frozen_C(r=F('.85')):
    r=F(r)
    th=exact_physical_ward()
    values=frozen_primary_at(r)
    interval=evaluate_expr(th['C_exact'],values)
    if interval.lo>0:verdict='STRICTLY_POSITIVE_CERTIFIED'
    elif interval.hi<0:verdict='STRICTLY_NEGATIVE_CERTIFIED'
    else:verdict='INCONCLUSIVE_CONTAINS_ZERO'
    return {'r_exact':str(r),'C_interval_lower_exact':str(interval.lo),
            'C_interval_upper_exact':str(interval.hi),
            'C_lower_float':float(interval.lo),'C_upper_float':float(interval.hi),
            'verdict':verdict,
            'model_scope':'frozen Step41 coefficient vector, model constants as terminating exact rationals and exact binary64 f_delta; on primary surface',
            'physical_inference':'proves frozen approximate-secondary profile does not satisfy C=0 at this radius if interval excludes 0; does not rule out another exact-secondary profile',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':print(json.dumps(certify_frozen_C(),indent=2))
