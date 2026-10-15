"""Compact exact HR pullback action for spherical oscillation audits.

The low-level integrator knows only the two spherical coordinate maps into the
native g/f FLRW charts. Homothetic Aoki kinematics are provided as one wrapper;
non-homothetic backgrounds can therefore be inserted before any reduction.
"""
from __future__ import annotations

import math
import numpy as np

from numerics.aoki_compact_action_oracle import _profiles


def _integrate_hr_pullback(
    *, weights, betas,
    a_g, r_g, Jg00, Jg01, Jg10, Jg11,
    b_f, r_f, Jf00, Jf01, Jf10, Jf11,
):
    b1,b2,b3=(float(betas[0]),float(betas[1]),float(betas[2]))
    g00=a_g*a_g*(-Jg00*Jg00+Jg10*Jg10)
    g01=a_g*a_g*(-Jg00*Jg01+Jg10*Jg11)
    g11=a_g*a_g*(-Jg01*Jg01+Jg11*Jg11)
    det_g2=g00*g11-g01*g01
    gi00=g11/det_g2; gi01=-g01/det_g2; gi11=g00/det_g2

    f00=b_f*b_f*(-Jf00*Jf00+Jf10*Jf10)
    f01=b_f*b_f*(-Jf00*Jf01+Jf10*Jf11)
    f11=b_f*b_f*(-Jf01*Jf01+Jf11*Jf11)

    A00=gi00*f00+gi01*f01
    A01=gi00*f01+gi01*f11
    A10=gi01*f00+gi11*f01
    A11=gi01*f01+gi11*f11
    det_A=A00*A11-A01*A10
    tr_A=A00+A11
    if np.any(det_A <= 0.0):
        raise ValueError("radial g^-1 f determinant left the positive branch")
    root_det=np.sqrt(det_A)
    den=tr_A+2.0*root_det
    if np.any(den <= 0.0):
        raise ValueError("principal HR square root left the real branch")
    tr_S=np.sqrt(den)
    ell=b_f*r_f/(a_g*r_g)
    e1=tr_S+2.0*ell
    e2=root_det+2.0*ell*tr_S+ell*ell
    e3=2.0*ell*root_det+ell*ell*tr_S
    potential=b1*e1+b2*e2+b3*e3

    det_Jg=Jg00*Jg11-Jg01*Jg10
    sqrt_minus_g=a_g**4*det_Jg*r_g*r_g
    return float(np.sum(weights*sqrt_minus_g*potential))


def homothetic_pi_compact_action(
    *, amp: float, hubble: float,
    beta1: float, beta2: float, beta3: float,
    K: float, w: float, mu: float,
    T: float, R: float, order: int,
) -> float:
    vals=(amp,hubble,beta1,beta2,beta3,K,w,mu,T,R)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if K <= 0.0 or mu <= -1.0 or T <= 0.0 or R <= 0.0:
        raise ValueError("require K,T,R>0 and mu>-1")
    if abs(1.0+3.0*w) < 1e-12:
        raise ValueError("w=-1/3 requires a separate chart")
    if order < 12:
        raise ValueError("quadrature order must be at least 12")

    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    t=T*xt[:,None]+np.zeros((1,order))
    r=0.5*R*(xr[None,:]+1.0)+np.zeros((order,1))
    weights=(T*wt[:,None])*(0.5*R*wr[None,:])

    A,At,Att,F,Fr,Frr=_profiles(t,r,T,R)
    C=mu/(1.0+mu)
    M=mu*(2.0+mu)
    p=2.0/(1.0+3.0*w)
    base=1.0+hubble*t/p
    if np.any(base <= 0.0):
        raise ValueError("compact domain crossed FLRW chart boundary")
    Hc=hubble/base
    Hcp=-0.5*(1.0+3.0*w)*Hc*Hc
    abase=base**p
    inv_a2=abase**-2

    P=amp*At*F; Q=amp*A*Fr
    Pt=amp*Att*F; Pr=amp*At*Fr; Qt=Pr; Qr=amp*A*Frr
    deta=inv_a2*(-P+r*Hc*C*Q)
    drad=inv_a2*(Q/(1.0+mu)+r*Hc*C*P)
    inv_a2_t=-2.0*Hc*inv_a2
    deta_t=(
        inv_a2_t*(-P+r*Hc*C*Q)
        +inv_a2*(-Pt+r*C*(Hcp*Q+Hc*Qt))
    )
    deta_r=inv_a2*(-Pr+C*Hc*(Q+r*Qr))
    drad_t=(
        inv_a2_t*(Q/(1.0+mu)+r*Hc*C*P)
        +inv_a2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt))
    )
    drad_r=inv_a2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))

    eta_g=t+deta
    r_g=r+drad
    base_g=1.0+hubble*eta_g/p
    if np.any(base_g <= 0.0):
        raise ValueError("g pullback left FLRW chart")
    a_g=base_g**p

    eta_f=t-0.5*Hc*r*r*M
    eta_f_t=1.0-0.5*Hcp*r*r*M
    eta_f_r=-Hc*r*M
    r_f=(1.0+mu)*r
    base_f=1.0+hubble*eta_f/p
    if np.any(base_f <= 0.0):
        raise ValueError("f pullback left FLRW chart")
    b_f=K*base_f**p

    ones=np.ones_like(t); zeros=np.zeros_like(t)
    return _integrate_hr_pullback(
        weights=weights,betas=(beta1,beta2,beta3),
        a_g=a_g,r_g=r_g,
        Jg00=1.0+deta_t,Jg01=deta_r,Jg10=drad_t,Jg11=1.0+drad_r,
        b_f=b_f,r_f=r_f,
        Jf00=eta_f_t,Jf01=eta_f_r,Jf10=zeros,Jf11=(1.0+mu)*ones,
    )


def _frozen_displacement_action(
    u_amp: float, v_amp: float, *, beta1: float, beta2: float, beta3: float,
    xi: float, c: float, mu: float, T: float, R: float, order: int,
) -> float:
    vals=(u_amp,v_amp,beta1,beta2,beta3,xi,c,mu,T,R)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all frozen-displacement inputs must be finite")
    if xi <= 0.0 or c <= 0.0 or mu <= -1.0 or T <= 0.0 or R <= 0.0:
        raise ValueError("require xi,c,T,R>0 and mu>-1")
    if order < 12:
        raise ValueError("quadrature order must be at least 12")

    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    t=T*xt[:,None]+np.zeros((1,order))
    r=0.5*R*(xr[None,:]+1.0)+np.zeros((order,1))
    weights=(T*wt[:,None])*(0.5*R*wr[None,:])
    A,At,Att,F,Fr,Frr=_profiles(t,r,T,R)

    u=u_amp*At*F
    v=v_amp*A*Fr
    ut=u_amp*Att*F
    ur=u_amp*At*Fr
    vt=v_amp*At*Fr
    vr=v_amp*A*Frr
    ones=np.ones_like(t); zeros=np.zeros_like(t)
    return _integrate_hr_pullback(
        weights=weights,betas=(beta1,beta2,beta3),
        a_g=ones,r_g=r+v,
        Jg00=1.0+ut,Jg01=ur,Jg10=vt,Jg11=1.0+vr,
        b_f=xi*ones,r_f=(1.0+mu)*r,
        Jf00=c*ones,Jf01=zeros,Jf10=zeros,Jf11=(1.0+mu)*ones,
    )


def frozen_displacement_hessian(
    *, beta1: float, beta2: float, beta3: float,
    xi: float, c: float, mu: float, T: float=1.0, R: float=1.0,
    order: int=36, amplitude_step: float=2.0e-4,
) -> np.ndarray:
    h=float(amplitude_step)
    if not math.isfinite(h) or h <= 0.0:
        raise ValueError("amplitude_step must be positive and finite")
    kw=dict(beta1=beta1,beta2=beta2,beta3=beta3,xi=xi,c=c,mu=mu,T=T,R=R,order=order)
    f0=_frozen_displacement_action(0.0,0.0,**kw)
    H=np.empty((2,2),dtype=float)
    H[0,0]=(_frozen_displacement_action(h,0.0,**kw)-2.0*f0+_frozen_displacement_action(-h,0.0,**kw))/(h*h)
    H[1,1]=(_frozen_displacement_action(0.0,h,**kw)-2.0*f0+_frozen_displacement_action(0.0,-h,**kw))/(h*h)
    H[0,1]=H[1,0]=(
        _frozen_displacement_action(h,h,**kw)-_frozen_displacement_action(h,-h,**kw)
        -_frozen_displacement_action(-h,h,**kw)+_frozen_displacement_action(-h,-h,**kw)
    )/(4.0*h*h)
    return H


def frozen_displacement_null_ratio(**kwargs) -> tuple[float,float]:
    """Return ``v_amp/u_amp`` for the smallest-eigenvalue direction.

    ``nullness`` is |lambda_min|/max(|lambda_max|, tiny). The direction is
    defined continuously up to an irrelevant overall sign.
    """
    H=frozen_displacement_hessian(**kwargs)
    vals,vecs=np.linalg.eigh(H)
    i=int(np.argmin(np.abs(vals)))
    v=vecs[:,i]
    if abs(v[0]) < 1e-14:
        raise np.linalg.LinAlgError("frozen null direction has vanishing temporal component")
    scale=max(1e-30,float(np.max(np.abs(vals))))
    return float(v[1]/v[0]), float(abs(vals[i])/scale)
