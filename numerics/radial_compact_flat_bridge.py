"""Boundary-safe radial compact bridge between native flat gauge and Fourier scalars."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density


@dataclass(frozen=True)
class RadialCompactProfileData:
    norm: float
    gradient_norm: float
    k2_eff: float


def _profile(r,R):
    F=r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6
    Fr=2*r-12*r**3/R**2+18*r**5/R**4-8*r**7/R**6
    Frr=2-36*r*r/R**2+90*r**4/R**4-56*r**6/R**6
    return F,Fr,Frr


def radial_compact_profile_data(*,R:float,order:int=80)->RadialCompactProfileData:
    R=float(R)
    if not math.isfinite(R) or R<=0:
        raise ValueError('R must be positive and finite')
    if order<12:
        raise ValueError('order must be at least 12')
    x,w=np.polynomial.legendre.leggauss(int(order)); r=.5*R*(x+1); rw=.5*R*w
    F,Fr,_=_profile(r,R)
    n=float(np.sum(rw*r*r*F*F)); g=float(np.sum(rw*r*r*Fr*Fr))
    if n<=0:
        raise RuntimeError('compact norm must be positive')
    return RadialCompactProfileData(n,g,g/n)


def _eh_action(phi_amp,B_amp,*,lapse,scale_factor,H,R,order):
    x,w=np.polynomial.legendre.leggauss(int(order)); r=.5*R*(x+1); rw=.5*R*w
    adot=float(H)*float(scale_factor)*float(lapse)
    total=0.0
    for rr,ww in zip(r,rw):
        F,Fr,Frr=_profile(float(rr),float(R))
        total += ww*0.5*flat_spherical_adm_eh_density(
            scale_factor=scale_factor,scale_rate=adot,background_lapse=lapse,r=float(rr),
            Phi=phi_amp*F,shift=B_amp*Fr,shift_r=B_amp*Frr)
    return float(total)


def radial_compact_eh_lapse_shift_hessian(*,lapse:float,scale_factor:float,H:float,R:float,
                                           order:int=80,amplitude_step:float=1e-3)->np.ndarray:
    vals=(lapse,scale_factor,H,R,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError('inputs must be finite')
    if lapse<=0 or scale_factor<=0 or R<=0 or amplitude_step<=0:
        raise ValueError('positive scales required')
    h=float(amplitude_step)
    kw=dict(lapse=float(lapse),scale_factor=float(scale_factor),H=float(H),R=float(R),order=int(order))
    f0=_eh_action(0,0,**kw); Hm=np.zeros((2,2))
    Hm[0,0]=(_eh_action(h,0,**kw)-2*f0+_eh_action(-h,0,**kw))/h**2
    Hm[1,1]=(_eh_action(0,h,**kw)-2*f0+_eh_action(0,-h,**kw))/h**2
    Hm[0,1]=Hm[1,0]=(_eh_action(h,h,**kw)-_eh_action(h,-h,**kw)-_eh_action(-h,h,**kw)+_eh_action(-h,-h,**kw))/(4*h**2)
    return Hm


def radial_compact_dust_phase_value(*,lapse:float,scale_factor:float,R:float,rho:float,
                                    Phi:float,B:float,q:float,q_rate:float,momentum:float,
                                    log_phidot_rate:float=0.0,order:int=80)->float:
    """Integrate one native dust phase mode with independent state/rate amplitudes."""
    from numerics.spherical_flat_dust_phase_action import flat_spherical_dust_phase_density
    vals=(lapse,scale_factor,R,rho,Phi,B,q,q_rate,momentum,log_phidot_rate)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError('dust bridge inputs must be finite')
    if lapse<=0 or scale_factor<=0 or R<=0 or rho<=0:
        raise ValueError('positive dust scales required')
    x,w=np.polynomial.legendre.leggauss(int(order)); r=.5*R*(x+1); rw=.5*R*w
    total=0.0
    for rr,ww in zip(r,rw):
        F,Fr,_=_profile(float(rr),float(R))
        total += ww*flat_spherical_dust_phase_density(
            scale_factor=scale_factor,lapse=lapse,r=float(rr),rho=rho,
            Phi=Phi*F,shift=B*Fr,q=q*F,q_t=q_rate*F,q_r=q*Fr,
            momentum=momentum*F,log_phidot_rate=log_phidot_rate)
    return float(total)
