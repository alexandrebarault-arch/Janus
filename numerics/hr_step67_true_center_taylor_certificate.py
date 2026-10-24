"""Step67 genuine original Step45/46/55 six-pair G: *new* U3 center certificate.

The authentic four original modules (including Step55 global interval geometry)
are byte-verified against historical GitHub blobs before executing. A truncated
polynomial Taylor-jet ring with outward integer interval coefficients gives
a rigorous enclosure of the s^3 coefficient of REAL G(s,U(s)); its
coefficient divided by 9 is the third regular-center U_3 in the exact
normalized radial secondary ODE 2*s U_s=G-2U.

This verifies only center radial C=0 initial-data higher derivatives; it is
NOT original six-pair TEMPORAL Dirac, lapse fixing, or 4D dynamics.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from functools import lru_cache
import sympy as sp
from . import hr_step55_global_barrier as old

PINNED={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def verify_bytes(root=None):
    root=Path(root) if root is not None else Path(__file__).resolve().parent
    for name,wanted in PINNED.items():
        raw=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=wanted:raise ValueError('authentic historical module mismatch '+name+': '+actual)
    return PINNED.copy()


class J:
    """Order-three polynomial s-jet in rigorous Step55 integer outward intervals.

    Each coefficient is the actual Step55 I interval on 10**28 integer lattice,
    so the resulting enclosure contains every Taylor coefficient of the true
    rational/sqrt expression when its constant terms obey the input intervals.
    No floating point is used in any coefficient operation.
    """
    __slots__=('a',)
    def __init__(self,constant=0,coeffs=None):
        self.a=tuple(old.I.c(t) for t in (coeffs if coeffs is not None else [constant,0,0,0]))
        if len(self.a)!=4:raise ValueError('jet order exactly three')
    @staticmethod
    def c(x):return x if isinstance(x,J) else J(x)
    def __add__(self,o):
        b=J.c(o);return J(coeffs=[x+y for x,y in zip(self.a,b.a)])
    __radd__=__add__
    def __neg__(self):return J(coeffs=[-x for x in self.a])
    def __sub__(self,o):return self+-J.c(o)
    def __rsub__(self,o):return J.c(o)+-self
    def __mul__(self,o):
        b=J.c(o)
        return J(coeffs=[sum((self.a[k]*b.a[n-k] for k in range(n+1)),old.I.c(0)) for n in range(4)])
    __rmul__=__mul__
    def inv(self):
        y=[old.I.c(0)]*4
        y[0]=self.a[0].inv()
        for n in range(1,4):
            y[n]=-y[0]*sum((self.a[k]*y[n-k] for k in range(1,n+1)),old.I.c(0))
        return J(coeffs=y)
    def __truediv__(self,o):return self*J.c(o).inv()
    def __rtruediv__(self,o):return J.c(o)*self.inv()
    def __pow__(self,n):
        if n==sp.Rational(1,2) or n==.5:return self.sqrt()
        if n==sp.Rational(-1,2) or n==-.5:return self.sqrt().inv()
        if int(n)!=n:raise ValueError('only integral and square-root powers')
        n=int(n)
        if n<0:return (self.inv())**(-n)
        res=J(1);base=self
        while n:
            if n&1:res=res*base
            n//=2
            if n:base=base*base
        return res
    def sqrt(self):
        y=[old.I.c(0)]*4
        y[0]=self.a[0].sqrt()
        if y[0].lo<=0<=y[0].hi:
            raise ZeroDivisionError('Taylor root center coefficient includes zero')
        two=old.I.c(2)
        for n in range(1,4):
            lower=sum((y[k]*y[n-k] for k in range(1,n)),old.I.c(0))
            y[n]=(self.a[n]-lower)/(two*y[0])
        return J(coeffs=y)
    def __abs__(self):
        if self.a[0].lo>0:return self
        if self.a[0].hi<0:return -self
        raise ValueError('abs sign not certified at polynomial center')
    def __repr__(self):return 'J('+','.join(str(z.disp()) for z in self.a)+')'


def geometry_taylor(s):
    """Literal expression-level lift of historical old.geometry to J algebra.

    All original named benchmark constants come from the byte-pinned
    original Step55 module, not retyped decimal approximations.
    Cross-check zeroth coefficient of EVERY input against old.geometry(0).
    """
    C=lambda x:J.c(x)
    A,Y,B,MG,MF,M2=(C(getattr(old,k)) for k in ('A','Y','B','MG','MF','M2'))
    B0,B1,B2,B3,B4=(C(getattr(old,k)) for k in ('B0','B1','B2','B3','B4'))
    CG,CF,KG,KF,Z1=(C(getattr(old,k)) for k in ('CG','CF','KG','KF','Z1'))
    PG=C(old.PG)
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
    return dict(Lg0=Lg,Lf0=Lf,Sgr0=Sgr,Sfr0=Sfr,Gmom=Gmom,Psg0=Psg,Rhog=Rhog,Gprime=Gprime,tg0=KG*Lg,tf0=KF*Lf,z1=Z1,Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr0=4*A*CG*ug,Lfr0=4*B*CF*uf,
      Mg2=MG,Mf2=MF,m2=M2,beta0=B0,beta1=B1,beta2=B2,beta3=B3,beta4=B4)


def interval_encloses(a,b):return a.lo<=b.lo and a.hi>=b.hi


@lru_cache(1)
def true_center_U3():
    verify_bytes()
    source_syms,original_G=old.compiled()
    s=J(coeffs=(0,1,0,0))
    inputs=geometry_taylor(s)
    reference=old.geometry(old.I.c(0))
    # Independent authenticated source's original geometry(0).
    assert set(inputs)==set(reference)
    for name in inputs:
        assert interval_encloses(inputs[name].a[0],reference[name]),(name,inputs[name].a[0],reference[name])
    u=J(coeffs=(old.U0,old.U1,old.U2,0))
    d=dict(inputs,s=s,U=u)
    g=original_G(*[d[str(k)] for k in source_syms])
    assert isinstance(g,J)
    residuals=[g.a[0]-old.I.c(2)*old.U0,
               g.a[1]-old.I.c(4)*old.U1,
               g.a[2]-old.I.c(6)*old.U2]
    # Rounding from a 10^-28 lattice must include true equality at each n.
    assert all(x.lo<=0<=x.hi for x in residuals),[x.disp() for x in residuals]
    U3=g.a[3]/old.I.c(9)
    assert U3.lo<=U3.hi
    return dict(U0=old.U0,U1=old.U1,U2=old.U2,U3=U3,
                g_coeffs=g.a,residuals=residuals,
                original_geometry_center_reproduced=True,
                original_git_blobs=verify_bytes())


def manifest():
    c=true_center_U3()
    return dict(step=67,claimed_physical_scope='exact initial constrained spherical radial center only',
                source_git_blobs=c['original_git_blobs'],
                U3_strict_enclosure=[str(F(c['U3'].lo,old.S)),str(F(c['U3'].hi,old.S))],
                U3_readable=c['U3'].disp(),
                U0_U1_U2_residual_enclosures=[(str(F(x.lo,old.S)),str(F(x.hi,old.S))) for x in c['residuals']],
                original_256_cell_proof_rerun_separately=True,
                finite_taylor_order=3,
                rigorous_method='same Step55 outward 10^-28 integer coefficient lattice, exact truncated square-root/Taylor algebra with full original physical G',
                original_six_pair_time_dirac='NOT_EVALUATED',lapse_fixing='NOT_DETERMINED',
                GATE_2B='OPEN',JANUS_R='NOT_VALIDATED')


if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))
