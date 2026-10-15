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
