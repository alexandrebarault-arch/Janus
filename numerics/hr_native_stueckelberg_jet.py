"""Exact quadratic native HR interaction including a finite-mu chart-variation jet.

Interaction-only *local geometric* audit, not a full cosmological action.
Variables (14): Phi_g,B_g,psi_g,E_g,Phi_f,B_f,psi_f,E_f,
               deltaT,deltaT_t,deltaT_r,deltaR_t,deltaR_r,deltaR_over_r.

The time/radius jets of deltaT and deltaR are algebraically independent here.
They must be constrained by actual field profiles before deriving a physical
mode, and the EH/dust terms require their own native pullbacks. The f-fluid
native metric perturbations are sampled at the shifted background time but
*their own spatial/temporal perturbation rates are not represented*.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


JET_ORDER = (
    'Phi_g','B_g','psi_g','E_g',
    'Phi_f','B_f','psi_f','E_f',
    'deltaT','deltaT_t','deltaT_r','deltaR_t','deltaR_r','deltaR_over_r',
)


@dataclass(frozen=True)
class NativeHRStueckelbergJet:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray
    radial_jacobian: np.ndarray
    variable_order: tuple[str, ...] = JET_ORDER


class _Jet:
    n=14
    __slots__=('v','d','h')
    def __init__(self,v,d=None,h=None):
        self.v=float(v)
        self.d=np.zeros(self.n) if d is None else np.asarray(d,dtype=float)
        self.h=np.zeros((self.n,self.n)) if h is None else np.asarray(h,dtype=float)
    @classmethod
    def var(cls,i):
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
            raise ValueError('singular radial determinant or scalar denominator')
        u=self.v
        return _Jet(1/u,-self.d/(u*u),
                    2*np.outer(self.d,self.d)/(u**3)-self.h/(u*u))
    def __truediv__(self,y):
        return self*self._make(y).inv()
    def __rtruediv__(self,y):
        return self._make(y)*self.inv()
    def sqrt(self):
        if self.v<=0.:
            raise ValueError('principal HR radial/angular square root is not real')
        root=math.sqrt(self.v)
        return _Jet(root,self.d/(2*root),
                    self.h/(2*root)-np.outer(self.d,self.d)/(4*root**3))


def native_hr_stueckelberg_jet(
    *,N:float,a:float,n:float,alpha:float,k:float,m2:float,Mg2:float,
    betas,mu:float=0.,r:float=0.,sigma_r:float=0.,sigma_dot:float=0.,
    mu_dot:float=0.,n_dot:float=0.,alpha_dot:float=0.,
    n_ddot:float=0.,alpha_ddot:float=0.,
) -> NativeHRStueckelbergJet:
    """Return interaction density gradient/14x14 Hessian for native charts.

    f-native background lapse/scale are Taylor-evaluated at the shifted time
    u=sigma*r^2/2+deltaT; their rate jets are supplied independently.
    The Jacobian variation contains the five independent first-derivative
    and radial-angular perturbations indicated by JET_ORDER.
    """
    beta=tuple(float(v) for v in betas)
    scalars=(N,a,n,alpha,k,m2,Mg2,mu,r,sigma_r,sigma_dot,mu_dot,
             n_dot,alpha_dot,n_ddot,alpha_ddot,*beta)
    if len(beta)!=5 or not all(math.isfinite(float(v)) for v in scalars):
        raise ValueError('all inputs must be finite and betas length 5')
    if min(N,a,n,alpha,Mg2)<=0 or k<0 or m2<0 or r<0 or mu<=-1:
        raise ValueError('invalid lapse/scale/mass/radius or nonregular mu')
    t0=1+.5*sigma_dot*r*r
    t1=sigma_r*r
    rr0=mu_dot*r
    rr1=1+mu
    J0=np.array([[t0,t1],[rr0,rr1]],dtype=float)
    if np.linalg.det(J0)<=0:
        raise ValueError('non-positive native radial chart Jacobian')

    (Pg,Bg,sg,Eg,Pf,Bf,sf,Ef,dT,dTt,dTr,dRt,dRr,dRoverr)=[
        _Jet.var(i) for i in range(14)
    ]
    u=.5*sigma_r*r*r+dT
    nT=n+n_dot*u+.5*n_ddot*u*u
    alT=alpha+alpha_dot*u+.5*alpha_ddot*u*u
    if nT.v<=0 or alT.v<=0:
        raise ValueError('native background time jet left positive metric branch')
    J00=t0+dTt;J01=t1+dTr;J10=rr0+dRt;J11=rr1+dRr
    k2=k*k
    g00=-N*N*(1+2*Pg)
    g01=N*a*k*Bg
    g11=a*a*(1+2*sg-2*k2*Eg/3)
    gyy=a*a*(1+2*sg+k2*Eg/3)
    fn00=-nT*nT*(1+2*Pf)
    fn01=nT*alT*k*Bf
    fn11=alT*alT*(1+2*sf-2*k2*Ef/3)
    f00=fn00*J00*J00+2*fn01*J00*J10+fn11*J10*J10
    f01=fn00*J00*J01+fn01*(J00*J11+J10*J01)+fn11*J10*J11
    f11=fn00*J01*J01+2*fn01*J01*J11+fn11*J11*J11
    fyy=alT*alT*(rr1+dRoverr)*(rr1+dRoverr)*(1+2*sf+k2*Ef/3)
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
    density=-m2*Mg2*(-dg).sqrt()*gyy*sum(
        (b*e for b,e in zip(beta,(1,e1,e2,e3,e4))),_Jet(0.)
    )
    if not np.isfinite(density.v) or not np.all(np.isfinite(density.d)) or not np.all(np.isfinite(density.h)):
        raise ArithmeticError('nonfinite native Stueckelberg Hessian')
    return NativeHRStueckelbergJet(
        value=density.v,gradient=density.d.copy(),
        hessian=.5*(density.h+density.h.T),radial_jacobian=J0,
    )
