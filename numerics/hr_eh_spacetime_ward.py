"""Compact f-sector FLRW Einstein-Hilbert coordinate-change Ward oracle.

Necessary subset of the native EH chart-variation test: a homogeneous
spatially flat native f metric with a native scalar lapse perturbation
q(T,R). Uses the exact ADM+GHY representative (no gauge constraint
elimination), not the full f scalar-tensor action or a physical mode.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class FlatEHWard:
    full_mixed: np.ndarray
    frozen_mixed: np.ndarray
    sampling_mixed: np.ndarray
    chart_min_determinant: float
    baseline_action: float


def _quadrature(Tmax,Rmax,order):
    if not all(math.isfinite(float(v)) and float(v)>0 for v in (Tmax,Rmax)):
        raise ValueError('finite positive time and radial compact domain required')
    if type(order) is not int or order<8:
        raise ValueError('quadrature order must be integer >=8')
    x,w=np.polynomial.legendre.leggauss(order)
    t=Tmax*x[:,None]
    r=Rmax*(x[None,:]+1)/2
    weights=2*np.pi*Tmax*Rmax*w[:,None]*w[None,:]
    return t,r,weights


def _chart(t,r):
    sigma=.08+.025*t
    mu=-.22+.05*t
    T=t+.5*sigma*r*r
    R=(1+mu)*r
    Tt=1+.5*.025*r*r
    Tr=sigma*r
    Rt=.05*r
    Rr=1+mu
    D=Tt*Rr-Tr*Rt
    return T,R,Tt,Tr,Rt,Rr,D


def _shapes(t,r,Tmax,Rmax):
    A=(1-(t/Tmax)**2)**4
    At=-8*t/Tmax**2*(1-(t/Tmax)**2)**3
    F=(1-(r/Rmax)**2)**4
    Fr=-8*r/Rmax**2*(1-(r/Rmax)**2)**3
    # mode: (dT,dR,dT_t,dT_r,dR_t,dR_r)
    temporal=(A*F,np.zeros_like(A*F),At*F,A*Fr,
              np.zeros_like(A*F),np.zeros_like(A*F))
    radial=(np.zeros_like(A*F),r*A*F,np.zeros_like(A*F),
            np.zeros_like(A*F),r*At*F,A*(F+r*Fr))
    return temporal,radial


def _native(T,R):
    # Positive time-drifting FLRW f background, no zero scale rate.
    a=1+.15*T+.035*T*T
    ad=.15+.07*T
    add=.07
    n=1+.08*T+.02*T*T
    nd=.08+.04*T
    q=1+.3*T+.2*R*R+.1*T*R*R
    qT=.3+.1*R*R
    qR=(.4+.2*T)*R
    # ADM EH with +Mf²/2, native U=0 and Phi=v*q(T,R):
    # L0=-3 Mf² a ad² R²/n;
    # L1=+3 Mf² a ad² R² q/n.
    strength=3*a*ad*ad/n
    strengthT=3*((ad*ad*ad+2*a*ad*add)/n-a*ad*ad*nd/(n*n))
    rho0=-strength*R*R
    rho1=strength*R*R*q
    dT1=strengthT*R*R*q+strength*R*R*qT
    dR1=strength*(2*R*q+R*R*qR)
    noT=strengthT*R*R*q
    noR=2*strength*R*q
    sampleT=strength*R*R*qT
    sampleR=strength*R*R*qR
    return rho0,rho1,dT1,dR1,noT,noR,sampleT,sampleR,strength,q


def eh_flat_native_spacetime_ward(*,time_radius=.4,radial_radius=.6,order=40):
    """Mixed coordinate/native lapse Ward derivative: complete = 0."""
    t,r,w=_quadrature(time_radius,radial_radius,order)
    T,R,Tt,Tr,Rt,Rr,D=_chart(t,r)
    if np.min(D)<=0:raise ValueError('baseline chart not regular')
    rho0,rho1,dT1,dR1,noT,noR,smT,smR,_,_=_native(T,R)
    complete=[];frozen=[];sampling=[]
    for dT,dR,dTt,dTr,dRt,dRr in _shapes(t,r,time_radius,radial_radius):
        dD=dTt*Rr+Tt*dRr-dTr*Rt-Tr*dRt
        complete.append(float(np.sum(w*(D*(dT1*dT+dR1*dR)+rho1*dD))))
        frozen.append(float(np.sum(w*(D*(noT*dT+noR*dR)+rho1*dD))))
        sampling.append(float(np.sum(w*D*(smT*dT+smR*dR))))
    return FlatEHWard(np.array(complete),np.array(frozen),np.array(sampling),
                      float(np.min(D)),float(np.sum(w*D*rho0)))


def eh_flat_native_spacetime_action(*,eps_time=0.,eps_radial=0.,lapse_amp=0.,
                  freeze_native_sampling=False,time_radius=.4,radial_radius=.6,order=40):
    """Exact finite chart-mapped FLRW ADM EH with one native lapse scalar.

    A coordinate reparameterization is a change of variables of the native
    scalar ADM density, not an assertion that common-chart ADM and native ADM
    integrands must equal each other pointwise (they differ by boundaries).
    """
    epT=float(eps_time);epR=float(eps_radial);v=float(lapse_amp)
    if not all(math.isfinite(x) for x in (epT,epR,v)):
        raise ValueError('finite perturbation amplitudes required')
    t,r,w=_quadrature(time_radius,radial_radius,order)
    T0,R0,Tt,Tr,Rt,Rr,_=_chart(t,r)
    temporal,radial=_shapes(t,r,time_radius,radial_radius)
    T=T0+epT*temporal[0]
    R=R0+epR*radial[1]
    Jt=Tt+epT*temporal[2]
    Jr=Tr+epT*temporal[3]
    Kt=Rt+epR*radial[4]
    Kr=Rr+epR*radial[5]
    D=Jt*Kr-Jr*Kt
    if np.min(D)<=0 or np.min(R)<=0:raise ValueError('non-regular perturbed native chart')
    _,_,_,_,_,_,_,_,strength,_=_native(T,R)
    qT,qR=(T0,R0) if freeze_native_sampling else (T,R)
    q=1+.3*qT+.2*qR*qR+.1*qT*qR*qR
    if np.min(1+2*v*q)<=0:raise ValueError('ADM lapse not real')
    density=-D*strength*R*R/np.sqrt(1+2*v*q)
    return float(np.sum(w*density))
