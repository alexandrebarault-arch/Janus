"""STEP42: rational interval centre regularity for the STORED Step41 profile.

Independent exact-interval evaluation of the reconstructed curved primary
Hamiltonian variables as functions of s=r**2, including the r=0 limit.
This is an initial-data/coordinate-regularity certificate, NOT proof of
C_local=0, full Einstein spacetime regularity, Dirac closure or lapse fixing.

Input comes from research/reports/gate2b-step41-report.json, with a pinned
SHA-256 for the published coefficient vector. No opaque floating tolerance
is used in the interval proof. Physical decimal constants are interpreted
as exact terminating rationals *conditionally*.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt, isfinite
from pathlib import Path
import hashlib
import json

A=F('.4'); Y=F('.5787707228025044'); B=A*Y
MG2=F(1); MF2=F('.10879548725')**2; M2=F('23.3348939346')
BETA=tuple(map(F,('0','1','-4.2383993109','13.6801214252','-38.5117901844')))
CG=F('.0015'); CF=F('-.0012'); Z=F('.004')
THETA_G=F('.0012'); THETA_F=F('-.0016'); DUST_G=F('.9')
RMAX=F('.85')
STEP41_COEFFICIENT_SHA256='bff542954a2ddba0505223d0d08075e3714dcebed23cd3c9012bd67c91d28b2d'


@dataclass(frozen=True)
class Interval:
    lo:F
    hi:F
    def __post_init__(self):
        object.__setattr__(self,'lo',F(self.lo))
        object.__setattr__(self,'hi',F(self.hi))
        if self.lo>self.hi:raise ValueError('reversed interval')
    @classmethod
    def point(cls,value):return cls(F(value),F(value))
    @staticmethod
    def cast(value):return value if isinstance(value,Interval) else Interval.point(value)
    def __add__(self,other):
        q=self.cast(other);return Interval(self.lo+q.lo,self.hi+q.hi)
    __radd__=__add__
    def __neg__(self):return Interval(-self.hi,-self.lo)
    def __sub__(self,other):return self+-self.cast(other)
    def __rsub__(self,other):return self.cast(other)+-self
    def __mul__(self,other):
        q=self.cast(other)
        vals=(self.lo*q.lo,self.lo*q.hi,self.hi*q.lo,self.hi*q.hi)
        return Interval(min(vals),max(vals))
    __rmul__=__mul__
    def reciprocal(self):
        if self.lo<=0<=self.hi:raise ValueError('division through zero')
        return Interval(1/self.hi,1/self.lo)
    def __truediv__(self,other):return self*self.cast(other).reciprocal()
    def __rtruediv__(self,other):return self.cast(other)*self.reciprocal()
    def __pow__(self,power):
        if not isinstance(power,int) or power<0:raise ValueError('natural integer powers only')
        if power==0:return Interval.point(1)
        if power%2:
            return Interval(self.lo**power,self.hi**power)
        return Interval(F(0) if self.lo<=0<=self.hi else min(self.lo**power,self.hi**power),
                        max(self.lo**power,self.hi**power))
    def sqrt(self,places=22):
        if self.lo<0:raise ValueError('negative square root')
        scale=10**places
        def lower(x):return F(isqrt((x.numerator*scale*scale)//x.denominator),scale)
        return Interval(lower(self.lo),lower(self.hi)+F(1,scale))


def actual_coefficients(report_path=None):
    path=Path(report_path) if report_path is not None else (
        Path(__file__).resolve().parents[1]/'research/reports/gate2b-step41-report.json')
    record=json.loads(path.read_text(encoding='utf-8'))
    if record.get('step')!='41' or record.get('status',{}).get('GATE_2B')!='OPEN':
        raise ValueError('not the correct previous scientific gate report')
    raw=record['actual_f_delta']
    if len(raw)!=9 or any(type(x) not in (int,float) for x in raw):
        raise ValueError('invalid coefficient data')
    # Step41's digest was computed AFTER converting each source coefficient
    # to float; the report may serialize exact zero as JSON integer 0.
    vals=[float(x) for x in raw]
    if not all(isfinite(x) for x in vals):
        raise ValueError('nonfinite correction coefficient')
    canonical=json.dumps(vals,separators=(',',':'))
    digest=hashlib.sha256(canonical.encode()).hexdigest()
    if digest!=STEP41_COEFFICIENT_SHA256 or record.get('coefficients_sha256')!=digest:
        raise ValueError('step41 coefficient digest mismatches authenticated snapshot')
    coeffs=tuple(F.from_float(v) for v in vals)
    if any(coeffs[i]!=0 for i in (1,3,5,7)):
        raise ValueError('odd momentum correction incompatible with center parity')
    if max(abs(coeffs[i]) for i in (0,2,4,6,8))>=F(1,200):
        raise ValueError('not inside strict Step40 momentum ball')
    return coeffs


def reference_h2():
    b0,b1,b2,b3,b4=BETA
    pot=b0+3*b1*Y+3*b2*Y*Y+b3*Y**3
    x=DUST_G/(3*A**3)+M2*pot/3
    if x<=0:raise ArithmeticError('no real reference H')
    return x


def canonical_regularized(s,coeffs):
    """RETURN exact enclosures: pg/r², pf/r², pLg/r², pLf/r²,
    pSg/r, pSf/r, Dg/r³, K/r², J(Sf/Sg), sqrt(1-z²).

    Define u_i=1+c_i*s; L_i=a_i*u_i²; S_i=r*L_i.  Then
    S'_i=a_i*u_i*(1+5c_i*s) and curvature R3_i=-48 c_i/(a_i²*u_i⁵).
    All expressions below have finite analytic s=0 extensions when their
    listed nonzero denominators and square roots are bounded positively.
    """
    s=Interval.cast(s)
    if s.lo<0 or s.hi>RMAX**2:raise ValueError('radial interval outside chart')
    if len(coeffs)!=9:raise ValueError('expected nine correction coefficients')
    if any(F(v)!=0 for v in (coeffs[1],coeffs[3],coeffs[5],coeffs[7])):
        raise ValueError('non-even momentum polynomial')
    H=Interval.point(reference_h2()).sqrt()
    Pg=-2*A*A*H
    Pf=-2*MF2*B*A*H
    ug=1+CG*s;uf=1+CF*s
    lg=A*ug**2;lf=B*uf**2
    e=Y*(uf/ug)**2
    b0,b1,b2,b3,b4=BETA
    j=b1+2*b2*e+b3*e**2
    a0=b0+2*b1*e+b2*e**2
    af=b2+2*b3*e+b4*e**2
    Aang=A*A*ug**4
    kbar=M2*MG2*lg*lf*Aang*j
    root=(1-Z**2*s).sqrt()
    dbar=kbar*Z/root
    wg=M2*MG2*Aang*(lg*a0+lf*j*root)
    wf=M2*MG2*Aang*(lf*af+lg*j*root)
    zg=Z*Z*s*kbar/(lg*root)
    zf=Z*Z*s*kbar/(lf*root)
    Qg=Pg
    pLbar_g=Pg*(1+F(5,2)*CG*s)
    Qf=Pf
    pLbar_f=Pf*(1+F(5,2)*CF*s)
    for k in range(5):
        d=F(coeffs[2*k])
        Qf+=d*s**k
        pLbar_f+=d*(s**k/F(k+1)+5*CF*s**(k+1)/F(k+2))

    def sector(ai,ui,ci,mi,ki,Q,ph,sgn,wbar,shift):
        d=1+5*ci*s
        Li=ai*ui**2
        Sprime=ai*ui*d
        ratio=ph/(2*mi*ai**2*ui**3*d) # [pLi/(2 mi Si Si')]/r
        kin=ph**2/(4*mi*ai*ui**2)
        cross=ph*Q/(mi*ai*ui)
        curvature=24*mi*ai*ci*ui
        constant=kin-cross-sgn*ratio*dbar*s+curvature+shift+wbar
        beta=(1+ki*ki*s).sqrt()+ratio*ki*Li*s
        if beta.lo<=0:raise ArithmeticError('nonpositive lapse dust coefficient')
        pbar=-constant/beta
        pSbar=(sgn*s*dbar+2*Li*d*Q-ki*Li*s*pbar)/Sprime
        return pbar,pSbar,beta,Sprime

    pg,pSg,bg,Sgprime=sector(A,ug,CG,MG2,THETA_G,Qg,pLbar_g,
                              F(1),wg,zg)
    pf,pSf,bf,Sfprime=sector(B,uf,CF,MF2,THETA_F,Qf,pLbar_f,
                              F(-1),wf,zf)
    return dict(pg_over_r2=pg,pf_over_r2=pf,pLg_over_r2=pLbar_g,
                pLf_over_r2=pLbar_f,pSg_over_r=pSg,pSf_over_r=pSf,
                Dg_over_r3=dbar,K_over_r2=kbar,J=j,
                shift_root=root,dust_beta_g=bg,dust_beta_f=bf,
                Sprime_g=Sgprime,Sprime_f=Sfprime)


def certify_center_and_dust(coeffs,ncells=256):
    """An exact finite COVER of every real s∈[0,R²].

    Finite intervals certify CONTINUUM analytic boundedness and positivity,
    not that the secondary Hamiltonian constraint vanishes or is preserved.
    """
    if not isinstance(ncells,int) or not 8<=ncells<=4096:
        raise ValueError('invalid rational cover cell count')
    smax=RMAX**2
    names=('pg_over_r2','pf_over_r2','K_over_r2','J',
           'shift_root','dust_beta_g','dust_beta_f','Sprime_g','Sprime_f')
    bounds={name:[] for name in names}
    bounded=('pLg_over_r2','pLf_over_r2','pSg_over_r','pSf_over_r','Dg_over_r3')
    finite={name:[] for name in bounded}
    for k in range(ncells):
        values=canonical_regularized(Interval(smax*k/ncells,smax*(k+1)/ncells),coeffs)
        for name in names:
            v=values[name]
            if v.lo<=0:raise ArithmeticError(f'not certified positive: {name}, interval {k}')
            bounds[name].append(v)
        for name in bounded:finite[name].append(values[name])
    return {'step':42,'domain_r':['0',str(RMAX)],'domain_s':['0',str(smax)],
            'cells':ncells,
            'strict_positive_lower_exact':{k:str(min(v.lo for v in cells)) for k,cells in bounds.items()},
            'strict_positive_lower_float':{k:float(min(v.lo for v in cells)) for k,cells in bounds.items()},
            'finite_signed_bounds_float':{k:[float(min(v.lo for v in cells)),float(max(v.hi for v in cells))] for k,cells in finite.items()},
            'centre_parity':{'metric_cartesian':'Lg and Lf are analytic in s=r², S_i=r L_i',
              'radial_shift':'z=Z*r, corresponding Cartesian vector z*x^i/r=Z*x^i',
              'dust_clocks':'theta_i prime=k_i*r*L_i, so theta_i analytic in s',
              'pL_i':'r² times finite analytic function of s',
              'pS_i':'r times finite analytic function of s',
              'dust_canonical_p_i':'r² times strictly positive analytic function of s',
              'Dg':'r³ times finite analytic function of s',
              'K':'r² times strictly positive analytic function of s'},
            'not_proved':['regularity of time-evolved 4D solution','full canonical tensor-density extension independent of symmetry reduction',
                          'pointwise exact C_local=0','full Dirac time preservation','lapse fixing'],
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def report(report_path=None,ncells=256):
    coeffs=actual_coefficients(report_path)
    result=certify_center_and_dust(coeffs,ncells)
    result['source_step41_coefficient_sha256']=STEP41_COEFFICIENT_SHA256
    return result

if __name__=='__main__':print(json.dumps(report(),indent=2))
