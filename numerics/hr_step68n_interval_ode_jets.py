"""Experimental, outward-integer *pointwise* Taylor enclosure for genuine Step55 ODE.

Use original pinned compiled G and geometry; propagate U_s,U_ss,U_sss from a
certified full-branch Ustar+-1e-6 enclosure at one fixed positive radius.
Not yet an interval enclosure of temporal A_N,A_M or a continuum sign proof.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha1
import json
from . import hr_step55_global_barrier as old
from .hr_step68l_refined_global_barrier import authentic_originals
I=old.I
K=3
BLOB68L='2a1ffc026a30abf41208b44a707dc869daf0929d'


class Jet:
    """Factorial-normalized 1D Taylor jet, each coefficient outward interval."""
    __slots__=('a',)
    def __init__(self, coefficients):
        if isinstance(coefficients,Jet):
            self.a=coefficients.a[:]
        elif isinstance(coefficients,(tuple,list)):
            if len(coefficients)>K+1:raise ValueError('order too high')
            self.a=([I.c(x) for x in coefficients]+[I.c(0)]*(K+1-len(coefficients)))
        else:
            self.a=[I.c(coefficients)]+[I.c(0)]*K
    @staticmethod
    def coerce(x):return x if isinstance(x,Jet) else Jet(x)
    def __add__(self,o):
        o=self.coerce(o)
        return Jet([x+y for x,y in zip(self.a,o.a)])
    __radd__=__add__
    def __neg__(self):return Jet([-x for x in self.a])
    def __sub__(self,o):return self+-self.coerce(o)
    def __rsub__(self,o):return self.coerce(o)+-self
    def __mul__(self,o):
        o=self.coerce(o)
        return Jet([sum((self.a[i]*o.a[n-i] for i in range(n+1)),I.c(0)) for n in range(K+1)])
    __rmul__=__mul__
    def inv(self):
        if self.a[0].lo<=0<=self.a[0].hi:raise ZeroDivisionError('jet denominator crosses zero')
        b=[self.a[0].inv()]
        for n in range(1,K+1):
            b.append(-(sum((self.a[j]*b[n-j] for j in range(1,n+1)),I.c(0))*b[0]))
        return Jet(b)
    def __truediv__(self,o):return self*self.coerce(o).inv()
    def __rtruediv__(self,o):return self.coerce(o)*self.inv()
    def sqrt(self):
        b=[self.a[0].sqrt()]
        if b[0].lo<=0:raise ValueError('sqrt jet not strictly positive')
        for n in range(1,K+1):
            b.append((self.a[n]-sum((b[j]*b[n-j] for j in range(1,n)),I.c(0)))/(2*b[0]))
        return Jet(b)
    def __pow__(self,n):
        if n==F(1,2):return self.sqrt()
        if n==F(-1,2):return self.sqrt().inv()
        if not int(n)==n:raise ValueError('unsupported jet power')
        n=int(n)
        if n<0:return self.inv()**-n
        out=Jet(1);base=self
        while n:
            if n&1:out=out*base
            n>>=1
            if n:base=base*base
        return out
    def __repr__(self):return f'Jet({self.a!r})'


def certify_sources():
    res=authentic_originals()
    src=Path(__file__).with_name('hr_step68l_refined_global_barrier.py').read_bytes()
    sha=sha1(b'blob '+str(len(src)).encode()+b'\0'+src).hexdigest()
    if sha!=BLOB68L:raise ValueError('Step68l source changed')
    return res


def jet_geometry(s):
    """Same Step55 physical geometry as byte-original geometry(), but Jet type."""
    A,B,MG,MF,M2,B0,B1,B2,B3,B4,CG,CF,KG,KF,Z1,PG = [Jet(getattr(old,k)) for k in
      ('A','B','MG','MF','M2','B0','B1','B2','B3','B4','CG','CF','KG','KF','Z1','PG')]
    ug=1+CG*s;uf=1+CF*s
    Lg=A*ug**2;Lf=B*uf**2
    Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
    T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
    T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
    Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
    root=(1-Z1**2*s).sqrt()
    Dbar=M2*MG*Lg*Lf*T*Z1/root
    Wgbar=M2*MG*(Lg*T0+Lf*T*root)
    Wfbar=M2*MG*(Lf*Tf+Lg*T*root)
    Rg=-48*CG/(A**2*ug**5)
    Rf=-48*CF/(B**2*uf**5)
    Gmom=PG*(1+F(5,2)*CG*s)
    Gprime=2*PG*(1+5*CG*s)
    fac=Gmom/(2*MG*Lg*Sgr)
    betag=(1+KG**2*s).sqrt()+s*fac*KG*Lg
    Rhog=-(Gmom**2/(4*MG*Lg)-fac*(s*Dbar+Lg*Gprime)-MG*Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag
    Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr
    return dict(Lg0=Lg,Lf0=Lf,Sgr0=Sgr,Sfr0=Sfr,Gmom=Gmom,Psg0=Psg,Rhog=Rhog,Gprime=Gprime,
        tg0=KG*Lg,tf0=KF*Lf,z1=Z1,Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr0=4*A*CG*ug,Lfr0=4*B*CF*uf,
        Mg2=MG,Mf2=MF,m2=M2,beta0=B0,beta1=B1,beta2=B2,beta3=B3,beta4=B4)


def jet_G(s,u):
    vals=jet_geometry(s)
    vals['s']=s;vals['U']=u
    symbols,fn=old.compiled()
    result=fn(*[vals[str(sym)] for sym in symbols])
    return Jet.coerce(result)


def coefficient_interval(x):return [str(F(x.lo,old.S)),str(F(x.hi,old.S))]


def fixed_s_ode_jet(s0=F(4,25), delta=F(1,1000000)):
    certify_sources()
    if s0<=0 or s0>F(289,400) or delta!=F(1,1000000):
        raise ValueError('Requires original Step68l certified chart and s>0')
    si=I.c(s0)
    star,_,_=old.stars(si)
    du=I.c(delta)
    ui=I(star.lo-du.hi,star.hi+du.hi)
    sj=Jet([si,I.c(1)])
    uj=Jet(ui)
    for n in range(1,K+1):
        fj=(jet_G(sj,uj)-2*uj)/(2*sj)
        uj.a[n]=fj.a[n-1]/n
    # NOTE: the normalized jet U(s0+t)=sum U^(n)(s0)/n! *t^n
    return {'s0':s0,'U_star':star,'U_tube':ui,'U_coefficients':uj.a,
        'G0':jet_G(sj,uj).a[0], 'G_original':old.G(si,ui)}


def manifest():
    c=fixed_s_ode_jet()
    for order in (0,1,2,3):
        x=c['U_coefficients'][order]
        if x.lo>x.hi:raise AssertionError('invalid outgoing interval')
    return {'step':'68n','kind':'RIGOROUS FIXED_S_ODE_TAYLOR_COEFFICIENT_ENCLOSURES',
       's0':'4/25','r0':'2/5','input_certified_global_U_bound':'Ustar+-1e-6 from Step68l',
       'source_sha':certify_sources(),'U_coefficients':[coefficient_interval(x) for x in c['U_coefficients']],
       'G0_interval':coefficient_interval(c['G0']),
       'G_original_interval':coefficient_interval(c['G_original']),
       'temporal_A_N_A_M_interval_bounds':'NOT_CALCULATED',
       'continuous_spatial_s_range_covered_by_this_jet':'single s0 only (global U bound used at s0)',
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(manifest(),indent=2))
