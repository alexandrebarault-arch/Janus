"""Exact spherically symmetric Einstein-Hilbert density for compact audits."""
from __future__ import annotations
import math


def spherical_ricci_scalar(*, a, ap, app, r,
                            phi, phi_t, phi_r, phi_rr,
                            psi, psi_t, psi_tt, psi_r):
    vals=(a,ap,app,r,phi,phi_t,phi_r,phi_rr,psi,psi_t,psi_tt,psi_r)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if a <= 0 or r <= 0:
        raise ValueError("a and r must be positive")
    Hc=ap/a
    Hcp=app/a-Hc*Hc
    At=Hc+phi_t
    Bt=Hc+psi_t
    Ar=phi_r
    Br=psi_r
    Btt=Hcp+psi_tt
    Arr=phi_rr
    em2A=math.exp(-2.0*phi)/(a*a)
    em2B=math.exp(-2.0*psi)/(a*a)
    R2=(2.0*em2A*(Btt+Bt*Bt-At*Bt)
        -2.0*em2B*(Arr+Ar*Ar-Ar*Br))
    areal=a*r
    Rt=ap*r
    Rr=a
    gradR2=-em2A*Rt*Rt+em2B*Rr*Rr
    boxR=(-em2A*(app*r+(-At+Bt)*ap*r)
          +em2B*((Ar-Br)*a))
    return R2+2.0/(areal*areal)*(1.0-gradR2-2.0*areal*boxR)


def eh_radial_density(**kwargs):
    a=float(kwargs['a']); r=float(kwargs['r'])
    phi=float(kwargs['phi']); psi=float(kwargs['psi'])
    return a**4*math.exp(phi+psi)*r*r*spherical_ricci_scalar(**kwargs)

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class CompactEHAmplitudeDerivatives:
    gradient: np.ndarray
    hessian: np.ndarray


def _compact_profile(t, r, T, R):
    x=t/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    Att=(-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr=2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    Frr=2.0-36.0*r**2/R**2+90.0*r**4/R**4-56.0*r**6/R**6
    return A,At,Att,F,Fr,Frr


def _compact_eh_action(phi_amp, psi_amp, *, a0, conformal_H, w,
                       time_radius, radial_radius, quadrature_order):
    if abs(1.0+3.0*w) < 1e-12:
        raise ValueError("w=-1/3 requires a separate conformal chart")
    p=2.0/(1.0+3.0*w)
    xt,wt=np.polynomial.legendre.leggauss(quadrature_order)
    xr,wr=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*xt
    rs=0.5*radial_radius*(xr+1.0)
    tw=time_radius*wt
    rw=0.5*radial_radius*wr
    total=0.0
    for i,t in enumerate(ts):
        u=1.0+conformal_H*t/p
        if u <= 0.0:
            raise ValueError("compact time support leaves the FLRW chart")
        a=a0*u**p
        Hc=conformal_H/u
        Hcp=-(conformal_H*conformal_H/p)/(u*u)
        ap=a*Hc
        app=a*(Hc*Hc+Hcp)
        for j,r in enumerate(rs):
            A,At,Att,F,Fr,Frr=_compact_profile(t,r,time_radius,radial_radius)
            phi=phi_amp*A*F
            psi=psi_amp*A*F
            dens=eh_radial_density(
                a=a,ap=ap,app=app,r=r,
                phi=phi,phi_t=phi_amp*At*F,
                phi_r=phi_amp*A*Fr,phi_rr=phi_amp*A*Frr,
                psi=psi,psi_t=psi_amp*At*F,
                psi_tt=psi_amp*Att*F,psi_r=psi_amp*A*Fr,
            )
            total += tw[i]*rw[j]*dens
    return float(total)


def compact_eh_amplitude_derivatives(*, a0, conformal_H, w,
                                     time_radius, radial_radius,
                                     amplitude_step=2e-4, quadrature_order=28):
    vals=(a0,conformal_H,w,time_radius,radial_radius,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all compact-EH inputs must be finite")
    if a0<=0 or time_radius<=0 or radial_radius<=0 or amplitude_step<=0:
        raise ValueError("positive scales and step required")
    if quadrature_order < 12:
        raise ValueError("quadrature_order must be at least 12")
    h=float(amplitude_step)
    f00=_compact_eh_action(0.0,0.0,a0=a0,conformal_H=conformal_H,w=w,
                           time_radius=time_radius,radial_radius=radial_radius,
                           quadrature_order=quadrature_order)
    fp0=_compact_eh_action(h,0.0,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    fm0=_compact_eh_action(-h,0.0,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    f0p=_compact_eh_action(0.0,h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    f0m=_compact_eh_action(0.0,-h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    fpp=_compact_eh_action(h,h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    fpm=_compact_eh_action(h,-h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    fmp=_compact_eh_action(-h,h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    fmm=_compact_eh_action(-h,-h,a0=a0,conformal_H=conformal_H,w=w,time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    grad=np.array([(fp0-fm0)/(2*h),(f0p-f0m)/(2*h)],dtype=float)
    H=np.array([
        [(fp0-2*f00+fm0)/(h*h),(fpp-fpm-fmp+fmm)/(4*h*h)],
        [(fpp-fpm-fmp+fmm)/(4*h*h),(f0p-2*f00+f0m)/(h*h)],
    ],dtype=float)
    return CompactEHAmplitudeDerivatives(gradient=grad,hessian=H)
