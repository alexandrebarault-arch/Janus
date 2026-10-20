"""Exact rational interval certificate for TWO positive moving dust sources.

Scope: original Step37 curved/noncomoving TWO-dust primary profile with
f_delta=(), grav_g=grav_f=0 and algebraically reconstructed pg,pf.
Certifies p_i/r²>0 for all 0<=r<=0.85 on the isolated primary surface,
not the momentum-corrected approximate SECONDARY from Step39.

Proof uses outward exact Fraction interval arithmetic and rational enclosures
of square roots (integer isqrt), so passing a finite interval subdivision
certifies a continuum result, unlike sampling a finite grid.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import json
from .hr_step40_curvature_box import M2,MG2,B1,B2,B3,A0,Y0,R

MF2=F('.10879548725')**2
CG=F('.0015');CF=F('-.0012')
ZG=F('.004');KG=F('.0012');KF=F('-.0016')
B0=F(0);B4=F('-38.5117901844')
DUST_CG=F('.9')

@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        object.__setattr__(self,'lo',F(self.lo))
        object.__setattr__(self,'hi',F(self.hi))
        if self.lo>self.hi:raise ValueError('reversed interval')
    @classmethod
    def point(cls, x):return cls(F(x),F(x))
    @staticmethod
    def as_i(x):return x if isinstance(x,I) else I.point(x)
    def __add__(self,o):
        q=self.as_i(o);return I(self.lo+q.lo,self.hi+q.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-self.as_i(o)
    def __rsub__(self,o):return self.as_i(o)+-self
    def __mul__(self,o):
        q=self.as_i(o)
        v=(self.lo*q.lo,self.lo*q.hi,self.hi*q.lo,self.hi*q.hi)
        return I(min(v),max(v))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ValueError('interval reciprocal includes zero')
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,o):return self*self.as_i(o).inv()
    def __rtruediv__(self,o):return self.as_i(o)*self.inv()
    def __pow__(self,n):
        if not isinstance(n,int) or n<0:raise ValueError('nonnegative integer power')
        if n==0:return I.point(1)
        if n%2==0:
            if self.lo<=0<=self.hi:return I(F(0),max(self.lo**n,self.hi**n))
            return I(min(self.lo**n,self.hi**n),max(self.lo**n,self.hi**n))
        return I(self.lo**n,self.hi**n)
    def sqrt(self,decimals=22):
        if self.lo<0:raise ValueError('negative interval square root')
        scale=10**decimals
        def lower(f):return F(isqrt(f.numerator*scale*scale//f.denominator),scale)
        l=lower(self.lo);h=lower(self.hi)
        # Increment exact grid quantum for a rigorous rational upper bound.
        return I(l,h+F(1,scale))
    def is_positive(self):return self.lo>0


def h2_rational():
    y=Y0
    V=B0+3*B1*y+3*B2*y*y+B3*y**3
    h2=DUST_CG/(3*A0**3)+M2*V/3
    assert h2>0
    return h2


def density_coeff_intervals(s:I, f_delta_per_coefficient_bound=F(0)):
    """Pointwise divided-by-r² original curved primary dust reconstruction.

    Derive from Step33g build_primary():
      u_i=1+c_i*r², L_i=a_i*u_i²,S_i=a_i*r*u_i²,
      pL_i=r² Pi*(1+(5/2)*ci*r²), pL_i'=2rPi*(1+5ci*r²),
      S_i'=a_i*u_i*(1+5ci*r²), theta_i'=ki*r*L_i,
      R3=-48*ci/(a_i²*u_i^5).
    All expressions below are analytic in s=r² INCLUDING s=0.
    """
    s=I.as_i(s)
    bound=F(f_delta_per_coefficient_bound)
    if bound<0:raise ValueError('f correction coefficient bound must be nonnegative')
    a=A0;b=A0*Y0
    H=I.point(h2_rational()).sqrt()
    pgenerator=-2*a*a*H
    fgenerator=-2*MF2*b*a*H
    ug=1+CG*s;uf=1+CF*s
    lg=a*ug**2;lf=b*uf**2
    e=Y0*(uf/ug)**2
    j=B1+2*B2*e+B3*e**2
    a0=B0+2*B1*e+B2*e**2
    af=B2+2*B3*e+B4*e**2
    Aang=a*a*ug**4
    kbar=M2*MG2*lg*lf*Aang*j
    root=(1-(ZG**2)*s).sqrt()
    dbar=kbar*ZG/root                  # Dg / r³, Df /r³ = -dbar
    term_shift_g=(ZG**2)*s*kbar/(lg*root) # z*Dg/(Lg r²)
    term_shift_f=(ZG**2)*s*kbar/(lf*root) # z*Dg/(Lf r²)
    wg=M2*MG2*Aang*(lg*a0+lf*j*root)
    wf=M2*MG2*Aang*(lf*af+lg*j*root)

    def one_dust(ai,ui,ci,Pi,Mi2,ki,d_sign,w,shift,q=None,ph=None):
        h=1+F(5,2)*ci*s
        d=1+5*ci*s
        q=Pi if q is None else q
        ph=Pi*h if ph is None else ph
        ratio_factor=ph/(2*Mi2*ai*ai*ui**3*d)  # (pL/(2Mi² S S'))/r
        kinetic=ph**2/(4*Mi2*ai*ui**2)
        subtract_L_plp=ph*q/(Mi2*ai*ui)
        curvature=24*Mi2*ai*ci*ui
        const=kinetic-subtract_L_plp-ratio_factor*d_sign*dbar*s+curvature+shift+w
        coeff=(1+ki*ki*s).sqrt()+ratio_factor*ki*ai*ui**2*s
        if coeff.lo<=0:raise ArithmeticError('dust coefficient not positive')
        return -const/coeff
    # Symmetric independent bounded EVEN coefficients delta_(2k), k=0..4:
    # Qf=(pLf)'/(2r[uf+2r uf']) = Pf + sum delta_(2k) r^(2k).
    # pLf/r² = Pf*(1+5cf*s/2) + sum delta_(2k) [s^k/(k+1)+5cf*s^(k+1)/(k+2)].
    # This matches exactly the Step37/39 polynomial f_delta generator.
    qf=I.point(0)+fgenerator
    phf=fgenerator*(1+F(5,2)*CF*s)
    if bound:
        for k in range(5):
            delta=I(-bound,bound)
            qf=qf+delta*s**k
            phf=phf+delta*(s**k/F(k+1)+5*CF*s**(k+1)/F(k+2))
    return one_dust(a,ug,CG,pgenerator,MG2,KG,F(1),wg,term_shift_g),one_dust(
               b,uf,CF,fgenerator,MF2,KF,F(-1),wf,term_shift_f,q=qf,ph=phf)


def interval_two_dust_certificate(ncells=256,f_delta_per_coefficient_bound=F(0)):
    if not isinstance(ncells,int) or not 4<=ncells<=4096:
        raise ValueError('required number of certified cells between 4 and 4096')
    f_delta_per_coefficient_bound=F(f_delta_per_coefficient_bound)
    rmax2=R*R
    g_lower=[];f_lower=[]
    for idx in range(ncells):
        s=I(rmax2*idx/ncells,rmax2*(idx+1)/ncells)
        g,f=density_coeff_intervals(s, f_delta_per_coefficient_bound)
        if g.lo<=0 or f.lo<=0:
            raise ArithmeticError(f'not certified at s cell {idx}: g.lo={float(g.lo)} f.lo={float(f.lo)}')
        g_lower.append(g.lo);f_lower.append(f.lo)
    return {'ncells':ncells,'f_delta_per_coefficient_bound':str(f_delta_per_coefficient_bound),'s_interval':['0',str(rmax2)],
            'r_interval':['0',str(R)],
            'strict_pg_over_r2_lower':str(min(g_lower)),
            'strict_pf_over_r2_lower':str(min(f_lower)),
            'strict_pg_over_r2_lower_float':float(min(g_lower)),
            'strict_pf_over_r2_lower_float':float(min(f_lower)),
            'physical_scope':'original curved primary with any EVEN polynomial f_delta coefficients (k=0..4) bounded separately as stated; Step39 corrected profile only certified IF it passes coefficient bound',
            'method':'outward exact rational interval arithmetic including sqrt integer enclosures',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(interval_two_dust_certificate(),indent=2))
