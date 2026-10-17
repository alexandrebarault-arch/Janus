"""Independent full-spacetime beta4 HR volume Ward identity control.

The beta4 term sqrt(-g) e4(sqrt(g^-1 f)) is exactly sqrt(-f).
For a positive-orientation spherical native chart (T,R)(t,r),
S_beta4 = 4*pi int dt dr J n(T) alpha(T)^3 R^2 [1+v q(T,R)].
An interior smooth chart displacement MUST NOT change this integral,
including its mixed variation with an f-native metric perturbation q.

This is a necessary geometrical/off-shell interaction check, NOT a
sufficient test of full diffeomorphism identities, EH/dust dynamics, or
physical scalar stability. The simple time-dependent functions are
polynomial controls, NOT the Candidate-C background solution.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class WardControl:
    mixed_exact: np.ndarray
    mixed_without_field_sampling: np.ndarray
    mixed_field_sampling: np.ndarray
    native_volume: float
    jacobian_min: float


def _bump(x, limit):
    """Compact smooth even bump, its first derivative, and a domain check."""
    x=np.asarray(x,dtype=float)
    u=(x/limit)**2
    inside=u<1
    q=np.where(inside,1-u,0.)
    return q**4,-8*x/limit**2*q**3


def _background(t, r):
    """Independent regular polynomial native background trajectory."""
    sigma=.08+.025*t
    sigdot=.025
    mu=-.22+.05*t
    mudot=.05
    T=t+.5*sigma*r*r
    R=(1+mu)*r
    Tt=1+.5*sigdot*r*r
    Tr=sigma*r
    Rt=mudot*r
    Rr=1+mu
    D=Tt*Rr-Tr*Rt
    return T,R,Tt,Tr,Rt,Rr,D


def _native_density(T,R):
    """Return rho0, rho1 and derivatives of rho1 in native (T,R)."""
    n=1+.05*T+.03*T*T
    alpha=1+.02*T+.015*T*T
    ndot=.05+.06*T
    adot=.02+.03*T
    u=n*alpha**3
    udot=ndot*alpha**3+3*n*alpha**2*adot
    q=1+.45*T+.30*R**2+.20*T*R**2
    qt=.45+.20*R**2
    qr=(.60+.40*T)*R
    rho0=u*R**2
    rho1=rho0*q
    dT_rho1=udot*R**2*q +rho0*qt
    dR_rho1=2*u*R*q+rho0*qr
    dT_no=udot*R**2*q
    dR_no=2*u*R*q
    sampleT=rho0*qt
    sampleR=rho0*qr
    return rho0,rho1,dT_rho1,dR_rho1,dT_no,dR_no,sampleT,sampleR


def _mesh(time_radius,radial_radius,order):
    if not all(math.isfinite(float(x)) and float(x)>0 for x in (time_radius,radial_radius)):
        raise ValueError('positive finite compact domains required')
    if type(order) is not int or order<8:
        raise ValueError('quadrature order must be integer >= 8')
    x,w=np.polynomial.legendre.leggauss(order)
    t=time_radius*x[:,None]
    r=.5*radial_radius*(x[None,:]+1.)
    weights=2*math.pi*radial_radius*time_radius*w[:,None]*w[None,:]
    return t,r,weights


def _shift_fields(t,r,H,B,kind):
    A,At=_bump(t,H)
    F,Fr=_bump(r,B)
    if kind=='time':
        return A*F,np.zeros_like(A*F),At*F,A*Fr,np.zeros_like(A*F),np.zeros_like(A*F)
    if kind=='radial':
        return np.zeros_like(A*F),r*A*F,np.zeros_like(A*F),np.zeros_like(A*F),r*At*F,A*(F+r*Fr)
    raise ValueError('kind must be time or radial')


def beta4_ward_control(*,time_radius=.4,radial_radius=.6,order=40)->WardControl:
    """Analytic mixed chart/native-f variation and omitted-sampling control.

    In mixed eps * v derivative, the full result is an integrated total
    divergence, and must be zero for both compact interior displacements.
    """
    t,r,w=_mesh(time_radius,radial_radius,order)
    T,R,Tt,Tr,Rt,Rr,D=_background(t,r)
    if np.min(D)<=0:raise ValueError('background chart orientation lost')
    rho0,rho1,dt,dr,dt_no,dr_no,st,sr=_native_density(T,R)
    full=[];truncated=[];sampling=[]
    for kind in ('time','radial'):
        dT,dR,dTt,dTr,dRt,dRr=_shift_fields(t,r,time_radius,radial_radius,kind)
        dD=dTt*Rr+Tt*dRr-dTr*Rt-Tr*dRt
        true=D*(dt*dT+dr*dR)+rho1*dD
        omitted=D*(dt_no*dT+dr_no*dR)+rho1*dD
        added=D*(st*dT+sr*dR)
        full.append(float(np.sum(w*true)))
        truncated.append(float(np.sum(w*omitted)))
        sampling.append(float(np.sum(w*added)))
    return WardControl(np.array(full),np.array(truncated),np.array(sampling),
                       float(np.sum(w*D*rho0)),float(np.min(D)))


def beta4_spacetime_volume(*,eps_time=0.,eps_radial=0.,native_f_amp=0.,
                            time_radius=.4,radial_radius=.6,order=40,
                            freeze_native_sampling=False):
    """Exact finite map volume. Frozen q is intentionally an incorrect control.

    An arbitrary native lapse perturbation 1+v q(T,R) tests the mixed
    chart/native-metric Ward variation. The chart perturbations vanish
    at time and radial boundaries. No extra common-chart r^2 measure:
    the angular radius R^2 is already in sqrt(-f).
    """
    t,r,w=_mesh(time_radius,radial_radius,order)
    T0,R0,Tt,Tr,Rt,Rr,D0=_background(t,r)
    if np.min(D0)<=0:raise ValueError('invalid baseline chart')
    dT,dR,dTt,dTr,dRt,dRr=_shift_fields(t,r,time_radius,radial_radius,'time')
    eT=float(eps_time);eR=float(eps_radial);v=float(native_f_amp)
    if not all(math.isfinite(x) for x in (eT,eR,v)):
        raise ValueError('finite displacement amplitudes required')
    T=T0+eT*dT
    Tt=Tt+eT*dTt
    Tr=Tr+eT*dTr
    dT,dR,dTt,dTr,dRt,dRr=_shift_fields(t,r,time_radius,radial_radius,'radial')
    R=R0+eR*dR
    Rt=Rt+eR*dRt
    Rr=Rr+eR*dRr
    D=Tt*Rr-Tr*Rt
    if np.min(D)<=0 or np.min(R)<=0:raise ValueError('nonregular perturbed chart')
    n=1+.05*T+.03*T*T
    alpha=1+.02*T+.015*T*T
    Tq,Rq=(T0,R0) if freeze_native_sampling else (T,R)
    q=1+.45*Tq+.30*Rq**2+.20*Tq*Rq**2
    rho=n*alpha**3*R**2*(1+v*q)
    return float(np.sum(w*D*rho))
