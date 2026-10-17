"""Exact O(delta^2) spherical Hassan--Rosen density with a finite radial map.

This is an *interaction-only*, instantaneous background-jet diagnostic. The
f-metric is pulled back from its native chart by

    T=t+sigma(t) r^2/2, R=(1+mu(t)) r,

with local Jacobian (1+sigma_dot*r^2/2, sigma*r; mu_dot*r,1+mu).
The native lapse/scale factor are expanded through a supplied second-order
background Taylor jet at T=t+sigma*r^2/2. With zero rate inputs they remain
frozen. This does not yet include perturbations of T or R, nor all of the
on-shell O(r^2) action.

Variable order: (Phi_g,B_g,psi_g,E_g, Phi_f,B_f,psi_f,E_f).
Neither EH nor matter action is included. No finite-mu propagation or fold
verdict can be extracted from this Hessian alone.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class NativeHRScalarJet:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    radial_jacobian: np.ndarray


class _Jet:
    """Second-order multivariate Taylor jet with exact product/chain rules."""
    __slots__=('v','d','h')
    n=8
    def __init__(self,v,d=None,h=None):
        self.v=float(v)
        self.d=np.zeros(self.n) if d is None else np.asarray(d,dtype=float)
        self.h=np.zeros((self.n,self.n)) if h is None else np.asarray(h,dtype=float)

    @classmethod
    def variable(cls,i):
        d=np.zeros(cls.n);d[i]=1.
        return cls(0.,d)

    @staticmethod
    def _make(x):
        return x if isinstance(x,_Jet) else _Jet(x)

    def __add__(self,y):
        y=self._make(y)
        return _Jet(self.v+y.v,self.d+y.d,self.h+y.h)
    __radd__=__add__
    def __neg__(self):
        return _Jet(-self.v,-self.d,-self.h)
    def __sub__(self,y):
        return self+-self._make(y)
    def __rsub__(self,y):
        return self._make(y)+-self
    def __mul__(self,y):
        y=self._make(y)
        return _Jet(self.v*y.v,self.v*y.d+y.v*self.d,
                    self.v*y.h+y.v*self.h+np.outer(self.d,y.d)+np.outer(y.d,self.d))
    __rmul__=__mul__
    def inv(self):
        if self.v==0.:
            raise ValueError('singular metric determinant or scalar denominator')
        u=self.v
        return _Jet(1/u,-self.d/(u*u),2*np.outer(self.d,self.d)/(u**3)-self.h/(u*u))
    def __truediv__(self,y):
        return self*self._make(y).inv()
    def __rtruediv__(self,y):
        return self._make(y)*self.inv()
    def sqrt(self):
        if self.v<=0.:
            raise ValueError('principal Hassan--Rosen square root left real positive branch')
        r=math.sqrt(self.v)
        return _Jet(r,self.d/(2*r),self.h/(2*r)-np.outer(self.d,self.d)/(4*r**3))


def native_hr_scalar_jet(*,N:float,a:float,n:float,alpha:float,k:float,
                         m2:float,Mg2:float,betas,mu:float=0.,r:float=0.,
                         sigma_r:float=0.,sigma_dot:float=0.,mu_dot:float=0.,
                         n_dot:float=0.,alpha_dot:float=0.,
                         n_ddot:float=0.,alpha_ddot:float=0.) -> NativeHRScalarJet:
    """Return exact potential, gradient and quadratic Hessian in native fields.

    Coordinates are local g-comoving cosmic time and radial position. The
    scalar Fourier longitudinal/transverse metric convention is the same as
    the direct De Felice Eq. (45)-(46) action (k is the same comoving k).
    Native f fields are pulled through the finite-mu spherical chart.
    """
    beta=tuple(float(v) for v in betas)
    values=(N,a,n,alpha,k,m2,Mg2,mu,r,sigma_r,sigma_dot,mu_dot,
            n_dot,alpha_dot,n_ddot,alpha_ddot,*beta)
    if len(beta)!=5 or not all(math.isfinite(float(v)) for v in values):
        raise ValueError('inputs must be finite and betas have length five')
    if min(N,a,n,alpha,Mg2)<=0 or k<0 or m2<0 or mu<=-1 or r<0:
        raise ValueError('invalid lapse, scale, mass, radial Jacobian or radius')
    time_offset=0.5*sigma_r*r*r
    n=n+n_dot*time_offset+0.5*n_ddot*time_offset*time_offset
    alpha=alpha+alpha_dot*time_offset+0.5*alpha_ddot*time_offset*time_offset
    if n<=0 or alpha<=0:
        raise ValueError("native background Taylor jet left positive lapse/scale branch")
    Tt=1+0.5*sigma_dot*r*r
    Tr=sigma_r*r
    Rt=mu_dot*r
    Rr=1+mu
    if Tt*Rr-Tr*Rt<=0:
        raise ValueError('non-positive time-radial pullback Jacobian')
    J=np.array([[Tt,Tr],[Rt,Rr]],dtype=float)
    Pg,Bg,sg,Eg,Pf,Bf,sf,Ef=[_Jet.variable(i) for i in range(8)]
    k2=k*k
    g00=-N*N*(1+2*Pg)
    g01=N*a*k*Bg
    g11=a*a*(1+2*sg-(2*k2/3)*Eg)
    gyy=a*a*(1+2*sg+(k2/3)*Eg)
    ft00=-n*n*(1+2*Pf)
    ft01=n*alpha*k*Bf
    ft11=alpha*alpha*(1+2*sf-(2*k2/3)*Ef)
    f00=ft00*(Tt*Tt)+ft01*(2*Tt*Rt)+ft11*(Rt*Rt)
    f01=ft00*Tt*Tr+ft01*(Tt*Rr+Rt*Tr)+ft11*Rt*Rr
    f11=ft00*(Tr*Tr)+ft01*(2*Tr*Rr)+ft11*(Rr*Rr)
    fyy=alpha*alpha*(Rr*Rr)*(1+2*sf+(k2/3)*Ef)
    dg=g00*g11-g01*g01
    df=f00*f11-f01*f01
    trA=(g11*f00+g00*f11-2*g01*f01)/dg
    detS=(df/dg).sqrt()
    trS=(trA+2*detS).sqrt()
    ell=(fyy/gyy).sqrt()
    e1=trS+2*ell
    e2=detS+2*ell*trS+ell*ell
    e3=2*ell*detS+ell*ell*trS
    e4=ell*ell*detS
    es=(1,e1,e2,e3,e4)
    sum_beta=sum((b*e for b,e in zip(beta,es)),_Jet(0.))
    density=-m2*Mg2*(-dg).sqrt()*gyy*sum_beta
    if not all(np.isfinite(v) for v in [density.v,*density.d,*density.h.flat]):
        raise ArithmeticError('nonfinite exact HR Hessian')
    return NativeHRScalarJet(
        value=density.v,
        gradient=density.d.copy(),
        hessian=(0.5*(density.h+density.h.T)).copy(),
        radial_jacobian=J,
    )
