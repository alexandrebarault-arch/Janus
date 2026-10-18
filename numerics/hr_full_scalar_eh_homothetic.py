"""Exact spherical ADM scalar EH Hessian on an untilted constant-radial chart.

A well-defined intermediate GREEN gate, NOT a full finite-mu dynamical theory.
Native spatial metrics are LINEAR in psi,E (consistent with existing HR jet):
 h_rr=a^2(1+2psi-2k^2E/3), h_ang=a^2 r^2(1+2psi+k^2E/3).
The lapse and radial shift are g00=-n^2(1+2Phi), g0r=n*a*U.
Field profiles are compact with F=(1-r^2/R^2)^4, U=B F_r and
E=-2 E_amp (F_rr-F_r/r)/k^2. The latter is a prescribed trial basis,
not a physical Fourier eigenmode. Full on-shell EH chart variations and
the two physical transfer oracles are not included.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class ScalarEHJet:
    value: float
    gradient: np.ndarray
    hessian: np.ndarray

class Jet:
    __slots__=('v','d','h')
    def __init__(self, v, d=None, h=None):
        self.v=float(v)
        self.d=np.zeros(6) if d is None else np.asarray(d,dtype=float)
        self.h=np.zeros((6,6)) if h is None else np.asarray(h,dtype=float)
    @staticmethod
    def var(i):
        d=np.zeros(6); d[i]=1.
        return Jet(0.,d)
    @staticmethod
    def cv(y):return y if isinstance(y,Jet) else Jet(y)
    def __add__(self,y):
        y=self.cv(y)
        return Jet(self.v+y.v,self.d+y.d,self.h+y.h)
    __radd__=__add__
    def __neg__(self):return Jet(-self.v,-self.d,-self.h)
    def __sub__(self,y):return self+-self.cv(y)
    def __rsub__(self,y):return self.cv(y)+-self
    def __mul__(self,y):
        y=self.cv(y)
        return Jet(self.v*y.v,self.v*y.d+y.v*self.d,
            self.v*y.h+y.v*self.h+np.outer(self.d,y.d)+np.outer(y.d,self.d))
    __rmul__=__mul__
    def inv(self):
        if self.v==0:raise ValueError('singular scalar radial metric factor')
        return Jet(1/self.v,-self.d/self.v**2,
            2*np.outer(self.d,self.d)/self.v**3-self.h/self.v**2)
    def __truediv__(self,y):return self*self.cv(y).inv()
    def __rtruediv__(self,y):return self.cv(y)*self.inv()
    def sqrt(self):
        if self.v<=0:raise ValueError('nonpositive scalar spatial/lapse metric')
        s=math.sqrt(self.v)
        return Jet(s,self.d/(2*s),self.h/(2*s)-np.outer(self.d,self.d)/(4*s**3))

def _profiles(r,R,k):
    if r<0 or R<=0 or k<=0 or not all(math.isfinite(x) for x in (r,R,k)):
        raise ValueError('finite nonnegative radial coordinate and positive radius/k required')
    if r>=R:return np.zeros(8)
    x=r/R; q=1-x*x
    F=q**4
    Fr=-8*r/R**2*q**3
    Frr=-8/R**2*q**3+48*r*r/R**4*q*q
    tf=48*r*r/R**4*q*q
    tfr=96*r/R**4*q*(1-3*x*x)
    tfrr=96/R**4*(1-12*x*x+15*x**4)
    return np.array([F,Fr,Frr,-2*tf/k**2,-2*tfr/k**2,-2*tfrr/k**2,tf,tfr])

def scalar_native_adm_jet(*,scale,scale_rate,lapse,r,profile_radius,k):
    """Six-variable exact quadratic Taylor jet: Phi,B,psi,E,psi_dot,E_dot.

    Includes both intrinsic 3-curvature and ADM extrinsic curvature.
    Computes the EH density per unit dOmega (no M^2/2, no integral).
    """
    vals=(scale,scale_rate,lapse,r,profile_radius,k)
    if not all(math.isfinite(float(v)) for v in vals) or min(scale,lapse,profile_radius,k)<=0 or r<=0:
        raise ValueError('invalid native EH chart')
    a=float(scale);ad=float(scale_rate);n=float(lapse);rr=float(r)
    F,Fr,Frr,Pe,Per,Perr,_,_=_profiles(rr,profile_radius,k)
    P,B,S,E,Sd,Ed=[Jet.var(i) for i in range(6)]
    sf=S*F;ef=E*Pe
    Qr=1+2*sf-(2*k*k/3)*ef
    Qt=1+2*sf+(k*k/3)*ef
    Qrr=2*S*Fr-(2*k*k/3)*E*Per
    Qtr=2*S*Fr+(k*k/3)*E*Per
    Qtrr=2*S*Frr+(k*k/3)*E*Perr
    Qrt=2*Sd*F-(2*k*k/3)*Ed*Pe
    Qtt=2*Sd*F+(k*k/3)*Ed*Pe
    U=B*Fr;Ur=B*Frr
    N=n*(1+2*P*F+U*U/Qr).sqrt()
    # 3-curvature of dl²=a² Qr dr²+a² Qt r² dOmega²:
    z=1+rr*Qtr/(2*Qt)
    zr=Qtr/(2*Qt)+rr/2*(Qtrr/Qt-(Qtr/Qt)*(Qtr/Qt))
    ratio=Qt/Qr
    r3=2/(a*a*rr*rr*Qt)*(
        1-ratio*z*z-2*rr*ratio*((Qtr/Qt-Qrr/Qr)*z/2+zr))
    h=ad/a; b=n/a
    kr=(h+Qrt/(2*Qr)-b*(Ur/Qr-U*Qrr/(2*Qr*Qr)))/N
    kt=(h+Qtt/(2*Qt)-b*(U/Qr)*(1/rr+Qtr/(2*Qt)))/N
    action=N*(a**3)*rr*rr*Qr.sqrt()*Qt*(r3-4*kr*kt-2*kt*kt)
    if not np.isfinite(action.v) or not np.all(np.isfinite(action.d)) or not np.all(np.isfinite(action.h)):
        raise ArithmeticError('nonfinite scalar EH jet')
    return ScalarEHJet(action.v,action.d.copy(),.5*(action.h+action.h.T))

@dataclass(frozen=True)
class HomotheticScalarEH:
    hessian: np.ndarray
    gradient: np.ndarray
    radius: float
    quadrature_order: int
    f_radial_scale: float


def integrate_untilted_native_scalar_eh(*,radius,k,N,a,a_rate,n,alpha,alpha_rate,
                                         mu=0.,planck_ratio=1.,quadrature_order=24):
    """Exact full scalar native EH density for sigma=mu_dot=0, mu=const.

    Returns 24x24 Hessian on HR/two-dust 22 slots + psi_gdot,E_gdot.
    No chart perturbation variation has been made; temporal support is
    still frozen. f native radius=(1+mu)r, k_native=k/(1+mu).
    f B amplitude rescales by (1+mu) to preserve common physical U_f=BF_r.
    """
    scalars=(radius,k,N,a,a_rate,n,alpha,alpha_rate,mu,planck_ratio)
    if not all(math.isfinite(float(v)) for v in scalars) or min(radius,k,N,a,n,alpha,planck_ratio)<=0 or mu<=-1:
        raise ValueError('invalid homothetic native EH inputs')
    if type(quadrature_order) is not int or quadrature_order<8:
        raise ValueError('quadrature order must be integer >= 8')
    m=1+mu
    nodes,weights=np.polynomial.legendre.leggauss(quadrature_order)
    H=np.zeros((24,24));g=np.zeros(24)
    Mg=np.zeros((6,24));Mf=np.zeros((6,24))
    for j,idx in enumerate((0,1,2,3,22,23)):Mg[j,idx]=1
    for j,idx in enumerate((4,5,6,7,14,15)):Mf[j,idx]=1
    Mf[1,5]=m
    for x,w in zip(nodes,weights):
        r=.5*radius*(x+1)
        G=scalar_native_adm_jet(scale=a,scale_rate=a_rate,lapse=N,
                               r=r,profile_radius=radius,k=k)
        F=scalar_native_adm_jet(scale=alpha,scale_rate=alpha_rate,lapse=n,
                               r=m*r,profile_radius=m*radius,k=k/m)
        vol=2*math.pi*radius*w
        H+=vol*(.5*(Mg.T@G.hessian@Mg)+.5*planck_ratio*m*(Mf.T@F.hessian@Mf))
        g+=vol*(.5*(Mg.T@G.gradient)+.5*planck_ratio*m*(Mf.T@F.gradient))
    return HomotheticScalarEH(.5*(H+H.T),g,float(radius),quadrature_order,m)
