"""Compact-support Einstein-Hilbert quadratic audit for Aoki scalar metric potentials."""
from __future__ import annotations

import math
import numpy as np

from numerics.aoki_compact_action_oracle import _profiles
from numerics.spherical_eh_reduced_action import reduced_eh_density


def _action(phi_amp, psi_amp, *, hubble, w, T, R, quadrature_order):
    if abs(1.0+3.0*w) < 1e-12:
        raise ValueError("w=-1/3 requires a separate background chart")
    p=2.0/(1.0+3.0*w)
    xt,wt=np.polynomial.legendre.leggauss(quadrature_order)
    xr,wr=np.polynomial.legendre.leggauss(quadrature_order)
    total=0.0
    for i,t in enumerate(T*xt):
        base=1.0+hubble*t/p
        if base <= 0.0:
            raise ValueError("compact domain crossed FLRW conformal-time singularity")
        a=base**p
        Hc=hubble/base
        Hcp=-0.5*(1.0+3.0*w)*Hc*Hc
        ap=a*Hc
        app=a*(Hcp+Hc*Hc)
        for j,r in enumerate(0.5*R*(xr+1.0)):
            A,At,Att,F,Fr,Frr=_profiles(t,r,T,R)
            phi=phi_amp*A*F
            phi_t=phi_amp*At*F
            phi_r=phi_amp*A*Fr
            phi_rr=phi_amp*A*Frr
            psi=psi_amp*A*F
            psi_t=psi_amp*At*F
            psi_tt=psi_amp*Att*F
            psi_r=psi_amp*A*Fr
            dens=reduced_eh_density(
                a=a,a_prime=ap,a_second=app,r=r,
                phi=phi,phi_t=phi_t,phi_r=phi_r,phi_rr=phi_rr,
                psi=psi,psi_t=psi_t,psi_tt=psi_tt,psi_r=psi_r,
            )
            total += (T*wt[i])*(0.5*R*wr[j])*dens
    return float(total)


def compact_eh_metric_hessian(
    *, hubble: float, w: float, T: float, R: float,
    amplitude_step: float=5e-4, quadrature_order: int=32,
) -> np.ndarray:
    vals=(hubble,w,T,R,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if T <= 0.0 or R <= 0.0 or amplitude_step <= 0.0:
        raise ValueError("T, R and amplitude_step must be positive")
    if quadrature_order < 12:
        raise ValueError("quadrature_order must be at least 12")
    h=float(amplitude_step)
    kw=dict(hubble=float(hubble),w=float(w),T=float(T),R=float(R),quadrature_order=int(quadrature_order))
    f00=_action(0.0,0.0,**kw)
    H=np.empty((2,2),dtype=float)
    H[0,0]=(_action(h,0.0,**kw)-2.0*f00+_action(-h,0.0,**kw))/(h*h)
    H[1,1]=(_action(0.0,h,**kw)-2.0*f00+_action(0.0,-h,**kw))/(h*h)
    H[0,1]=H[1,0]=(
        _action(h,h,**kw)-_action(h,-h,**kw)-_action(-h,h,**kw)+_action(-h,-h,**kw)
    )/(4.0*h*h)
    return H
