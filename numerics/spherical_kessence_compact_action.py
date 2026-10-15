"""Covariant compact-support P(X) scalar action in spherical areal gauge."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class CompactKessenceHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile(t,r,T,R):
    x=t/T
    A=(1-x*x)**3; At=(-6*x*(1-x*x)**2)/T
    F=r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6
    Fr=2*r-12*r**3/R**2+18*r**5/R**4-8*r**7/R**6
    return A,At,F,Fr


def _action(x,*,a0,ap0,app0,rho,pressure,cs2,T,R,order):
    qamp,phiamp,psiamp=map(float,x)
    enthalpy=rho+pressure
    if enthalpy<=0: raise ValueError('rho+pressure must be positive')
    # Choose X0=1/2, so the background scalar has phi0'=a and
    # P_X=rho+P, P_XX=(rho+P)(1/cs2-1).
    PX=enthalpy; PXX=enthalpy*(1.0/cs2-1.0); X0=.5; P0=pressure
    xt,wt=np.polynomial.legendre.leggauss(order); xr,wr=np.polynomial.legendre.leggauss(order)
    ts=T*xt; rs=.5*R*(xr+1); tw=T*wt; rw=.5*R*wr; total=0.0
    for i,t in enumerate(ts):
        a=a0+ap0*t+.5*app0*t*t
        if a<=0: raise ValueError('Taylor scale factor left positive branch')
        for j,r in enumerate(rs):
            A,At,F,Fr=_profile(float(t),float(r),T,R)
            q=qamp*A*F; qt=qamp*At*F; qr=qamp*A*Fr
            phi=phiamp*A*F; psi=psiamp*A*F
            X=.5*math.exp(-2*phi)*(a+qt)**2/(a*a)-.5*math.exp(-2*psi)*qr*qr/(a*a)
            dX=X-X0
            P=P0+PX*dX+.5*PXX*dX*dX
            dens=a**4*math.exp(phi+psi)*r*r*P
            total+=tw[i]*rw[j]*dens
    return float(total)


def compact_kessence_hessian(*,a0,ap0,app0,rho,pressure,cs2,time_radius,radial_radius,
                              amplitude_step=2e-4,quadrature_order=24):
    vals=(a0,ap0,app0,rho,pressure,cs2,time_radius,radial_radius,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals): raise ValueError('inputs must be finite')
    if min(a0,rho,cs2,time_radius,radial_radius,amplitude_step)<=0 or pressure<0: raise ValueError('invalid kessence inputs')
    h=float(amplitude_step);n=3;kw=dict(a0=float(a0),ap0=float(ap0),app0=float(app0),rho=float(rho),pressure=float(pressure),cs2=float(cs2),T=float(time_radius),R=float(radial_radius),order=int(quadrature_order))
    z=np.zeros(n);f0=_action(z,**kw);g=np.zeros(n);H=np.zeros((n,n))
    for i in range(n):
        ei=np.zeros(n);ei[i]=h;fp=_action(ei,**kw);fm=_action(-ei,**kw)
        g[i]=(fp-fm)/(2*h);H[i,i]=(fp-2*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n);ej[j]=h
            H[i,j]=H[j,i]=(_action(ei+ej,**kw)-_action(ei-ej,**kw)-_action(-ei+ej,**kw)+_action(-ei-ej,**kw))/(4*h*h)
    return CompactKessenceHessian(gradient=g,hessian=H)
