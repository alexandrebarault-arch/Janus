"""Rigorous fixed-point interval dust/J/K positivity around exact local Taylor profile.

This proves continuous positivity for an explicitly specified C1-neighbourhood
of the TRUNCATED center Taylor polynomial, not that the exact radial ODE
solution belongs to that neighbourhood. Inputs are rational printed benchmark
values plus rational outward enclosures of the previously certified U1/U2.
All interval operations round outward on an integer lattice (no floats).
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
from hashlib import sha1
from pathlib import Path
import json

S=10**30


def floor_div(a,b):
    if b<=0:raise ValueError('denominator positive required')
    return a//b

def ceil_div(a,b):return -floor_div(-a,b)

@dataclass(frozen=True)
class I:
    lo:int
    hi:int
    def __post_init__(self):
        if self.lo>self.hi:raise ValueError('invalid interval')
    @staticmethod
    def c(x):
        if isinstance(x,I):return x
        f=F(x)
        return I(floor_div(f.numerator*S,f.denominator),ceil_div(f.numerator*S,f.denominator))
    @staticmethod
    def hull(lo,hi):
        lo=F(lo);hi=F(hi)
        return I(floor_div(lo.numerator*S,lo.denominator),ceil_div(hi.numerator*S,hi.denominator))
    def __add__(self,o):
        o=I.c(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-I.c(o)
    def __rsub__(self,o):return I.c(o)+-self
    def __mul__(self,o):
        o=I.c(o)
        v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return I(floor_div(min(v),S),ceil_div(max(v),S))
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi:raise ZeroDivisionError('interval contains zero')
        # 1/x decreasing on both positive and negative sides
        return I(floor_div(S*S,self.hi),ceil_div(S*S,self.lo)) if self.lo>0 else I(
                 floor_div(-S*S,-self.hi),ceil_div(-S*S,-self.lo))
    def __truediv__(self,o):return self*I.c(o).inv()
    def __rtruediv__(self,o):return I.c(o)*self.inv()
    def __pow__(self,n):
        if not isinstance(n,int):raise TypeError
        if n<0:return (self.inv())**(-n)
        if n==0:return I.c(1)
        if n%2==0:
            # improve bounds for s^2, exact min zero on crossing zero
            x=self**(n//2)
            if x.lo<0<x.hi:return I(0,ceil_div(max(x.lo*x.lo,x.hi*x.hi),S))
            return I(floor_div(min(x.lo*x.lo,x.hi*x.hi),S),ceil_div(max(x.lo*x.lo,x.hi*x.hi),S))
        res=I.c(1);x=self
        while n:
            if n&1:res=res*x
            n//=2
            if n:x=x*x
        return res
    def sqrt(self):
        if self.lo<0:raise ValueError('sqrt of possibly negative interval')
        lower=isqrt(self.lo*S);upper=isqrt(self.hi*S)
        if upper*upper<self.hi*S:upper+=1
        return I(lower,upper)
    def lower_str(self):return str(F(self.lo,S))
    def upper_str(self):return str(F(self.hi,S))
    def lower_float(self):return float(F(self.lo,S))
    def upper_float(self):return float(F(self.hi,S))

PINS={'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
      'numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804'}

def authentic_sources(root=None):
    root=Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for p,want in PINS.items():
        raw=(root/p).read_bytes()
        got=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if got!=want:raise AssertionError(f'Step54 requires AUTHENTIC provider {p}, got {got}, not {want}')
    return PINS.copy()

A=I.c(F('.4'));Y=I.c(F('.5787707228025044'));B=A*Y
MG=I.c(1);MF=I.c(F('.10879548725')**2);M2=I.c(F('23.3348939346'))
B0,B1,B2,B3,B4=[I.c(F(x)) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
CG=I.c(F('.0015'));CF=I.c(F('-.0012'));KG=I.c(F('.0012'));KF=I.c(F('-.0016'));Z1=I.c(F('.004'))
H2=I.c(F('.9'))/(I.c(3)*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
PG=-2*A**2*H2.sqrt()
U0=MF*B*(PG/(MG*A)-2*Z1)
# Certified EXACT algebraic U1 and U2 bounds from Step52 and Step53,
# loaded as exact rational intervals rather than approximate numerical values.
U1=I.hull('0.0007897451667202464909325108904961683602148118201690',
          '0.0007897451667202464909325108904961683602148118201692')
U2=I.hull('-0.00001007385348674382817573689095286393593388364194376377344',
          '-0.00001007385348674382817573689095286393593388364194376377342')


def profiles(s,delta=I.c(0)):
    """Compute enclosures of both normalized dusts and physical chart factors.

    delta bounds |U-U_star| <= delta and |V-V_star| <= delta uniformly
    at the same radius, V=P'/r. No assumption that actual ODE meets tube!
    """
    s=I.c(s);delta=I.c(delta)
    if s.lo<0:raise ValueError('s must be nonnegative')
    if delta.lo<0:raise ValueError('delta nonnegative')
    ug=1+CG*s;uf=1+CF*s
    Lg=A*ug**2;Lf=B*uf**2
    Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
    T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
    T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
    Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
    Rg=-48*CG/(A**2*ug**5)
    Rf=-48*CF/(B**2*uf**5)
    root=(1-Z1**2*s).sqrt()
    Dhat=M2*MG*Lg*Lf*T*Z1/root
    Wghat=M2*MG*(Lg*T0+Lf*T*root)
    Wfhat=M2*MG*(Lf*Tf+Lg*T*root)
    # All phase gradients are k_i*r*L_i; no sqrt(r) terms survive.
    Gmom=PG*(1+F(5,2)*CG*s)
    Gpr=2*PG*(1+5*CG*s)
    Fg=Gmom/(2*MG*Lg*Sgr)
    betag=(1+KG**2*s).sqrt()+s*Fg*KG*Lg
    rho_g=-(Gmom**2/(4*MG*Lg)-Fg*(s*Dhat+Lg*Gpr)
           -MG*Lg**3*Rg/2+s*Z1*Dhat/Lg+Wghat)/betag
    Ustar=U0+U1*s+U2*s**2
    Vstar=2*U0+4*U1*s+6*U2*s**2
    U=I(Ustar.lo-delta.hi,Ustar.hi+delta.hi)
    V=I(Vstar.lo-delta.hi,Vstar.hi+delta.hi)
    Ff=U/(2*MF*Lf*Sfr)
    betaf=(1+KF**2*s).sqrt()+s*Ff*KF*Lf
    rho_f=-(U**2/(4*MF*Lf)-Ff*(-s*Dhat+Lf*V)
           -MF*Lf**3*Rf/2+s*Z1*Dhat/Lf+Wfhat)/betaf
    J=T/(Lg**2)
    Khat=M2*MG*Lg*Lf*T
    return {'rho_g':rho_g,'rho_f':rho_f,'J':J,'K_over_r2':Khat,
            'dust_denom_g':betag,'dust_denom_f':betaf,
            'Sfr':Sfr,'root':root,'U':U,'V':V}


def certify(cells=256,delta='0.0001',radius='0.85'):
    if not isinstance(cells,int) or not 16<=cells<=8192:raise ValueError('cells must be 16..8192')
    radius=F(radius);delta=F(delta)
    if not F(0)<radius<=F('.85') or not F(0)<=delta<=F('.01'):
        raise ValueError('uncertified radius/delta')
    sources=authentic_sources()
    d=I.c(delta)
    end=radius**2
    names=('rho_g','rho_f','J','K_over_r2','dust_denom_g','dust_denom_f','Sfr','root')
    minimum={k:10**100 for k in names}
    maximum={k:-10**100 for k in names}
    for i in range(cells):
        slab=I.hull(end*i/cells,end*(i+1)/cells)
        out=profiles(slab,d)
        for k in names:
            minimum[k]=min(minimum[k],out[k].lo)
            maximum[k]=max(maximum[k],out[k].hi)
    # Strictly positive proofs only if exact INTEGER lattice lower >0.
    if not all(minimum[k]>0 for k in names):
        raise ArithmeticError('wide interval chart: '+str({k:minimum[k]/S for k in names}))
    return {'step':54,'continuum_radius':[0,str(radius)],'cells':cells,
            'tube_max_abs_U_minus_Ustar_and_V_minus_Vstar':str(delta),
            'normalized_Ustar':'U0+U1*s+U2*s², s=r², exact U0 quadratic, U1/U2 rigorous rational bounds',
            'minima_lower_fixed_grid_exact':{k:str(F(minimum[k],S)) for k in names},
            'maxima_upper_fixed_grid_exact':{k:str(F(maximum[k],S)) for k in names},
            'minima_display':{k:minimum[k]/S for k in names},
            'source_git_blobs':sources,'outward_rounding_lattice':'integer rational 1e-30',
            'logical_scope':'FOR EVERY r in [0,rmax], IF |U(r²)-Ustar(r²)|<=delta AND |P_prime(r)/r-Vstar(r²)|<=delta, THEN the original TWO DUST densities and J/K chart factors are strictly positive. Not a proof the exact radial ODE solution lies in this tube.',
            'GLOBAL_CENTRE_TO_ENDPOINT_ODE_ERROR_TUBE_VERIFIED':False,
            'full_six_pair_Dirac_time_preservation':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(certify(),indent=2))
