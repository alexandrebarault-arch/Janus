"""Homothetic Aoki oracle evaluated in the native relative (L,T) chart."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.nonhomothetic_hr_relative_native import relative_native_hr_density


@dataclass(frozen=True)
class NativeRelativeAokiCoefficients:
    kinetic_hessian_coefficient: float
    gradient_hessian_coefficient: float
    sound_speed_squared: float
    fit_residual: float


def _profile(eta,r,T,R):
    x=eta/T
    if abs(x)>=1.0 or r<=0.0 or r>=R:
        return 0.0,0.0,0.0
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr=2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    return A*F,At*F,A*Fr


def _background(eta,H0,w):
    if abs(1.0+3.0*w)<1e-12:
        raise ValueError('w=-1/3 requires separate chart')
    p=2.0/(1.0+3.0*w)
    u=1.0+H0*eta/p
    if u<=0.0:
        raise ValueError('compact support left positive FLRW chart')
    a=u**p
    Hc=H0/u
    Hcp=-(H0*H0/p)/(u*u)
    H=Hc/a
    add_over_a=-0.5*(1.0+3.0*w)*H*H
    return p,u,a,Hc,Hcp,H,add_over_a


def _relative_fields(eta,r,amp,*,H0,w,mu,T,R):
    p,u,a,Hc,Hcp,H,add=_background(eta,H0,w)
    _,pi_eta,pi_r=_profile(eta,r,T,R)
    pi_eta*=amp; pi_r*=amp
    q=1.0+mu
    deta=(-pi_eta + r*Hc*mu*pi_r/q)/(a*a)
    dr=(pi_r/q + r*Hc*mu*pi_eta/q)/(a*a)
    M=mu*(2.0+mu)
    sigma=-0.5*Hc*r*r*M
    sigma_eta=-0.5*Hcp*r*r*M
    sigma_r=-Hc*r*M
    eta_f=eta+sigma
    _,_,a_f,_,_,_,_=_background(eta_f,H0,w)
    Tcos=a_f*((1.0+sigma_eta)*deta+sigma_r*dr)
    Lr=q*dr
    return Tcos,Lr


def _relative_jet(eta,r,amp,*,H0,w,mu,T,R):
    T0,L0=_relative_fields(eta,r,amp,H0=H0,w=w,mu=mu,T=T,R=R)
    he=max(2e-7,2e-5*T)
    hr=max(2e-7,2e-5*R)
    Tep,Lep=_relative_fields(eta+he,r,amp,H0=H0,w=w,mu=mu,T=T,R=R)
    Tem,Lem=_relative_fields(eta-he,r,amp,H0=H0,w=w,mu=mu,T=T,R=R)
    Trp,Lrp=_relative_fields(eta,r+hr,amp,H0=H0,w=w,mu=mu,T=T,R=R)
    Trm,Lrm=_relative_fields(eta,r-hr,amp,H0=H0,w=w,mu=mu,T=T,R=R)
    _,_,a,_,_,_,_=_background(eta,H0,w)
    return T0,(Tep-Tem)/(2*he*a),(Trp-Trm)/(2*hr),L0,(Lep-Lem)/(2*he*a),(Lrp-Lrm)/(2*hr)


def _action(amp,*,betas,K,w,mu,H0,T,R,order):
    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    etas=T*xt; rs=.5*R*(xr+1.0)
    ew=T*wt; rw=.5*R*wr
    total=0.0
    M=mu*(2.0+mu)
    for i,eta in enumerate(etas):
        p,u,a,Hc,Hcp,H,add_over_a=_background(float(eta),H0,w)
        s=-a*Hc*M
        s_dot=-0.5*(1.0-3.0*w)*M*Hc*Hc
        for j,r in enumerate(rs):
            Tfield,Tdot,Tr,Lr,Ldotr,Lrr=_relative_jet(float(eta),float(r),amp,H0=H0,w=w,mu=mu,T=T,R=R)
            dens=relative_native_hr_density(
                betas=betas,m2=1.0,Mg2=1.0,
                a=a,n=K,alpha=K*a,r=float(r),
                n_dot_over_n=0.0,n_ddot_over_n=0.0,
                alpha_dot_over_alpha=H,alpha_ddot_over_alpha=add_over_a,
                mu=mu,mu_dot=0.0,s=s,s_dot=s_dot,
                T=Tfield,T_dot=Tdot,T_r=Tr,L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
            )
            # Convert the native cosmic radial density dt dr to d eta dr.
            total += ew[i]*rw[j]*a*dens
    return float(total)


def _amp_hessian(*,amplitude_step,**kw):
    h=float(amplitude_step)
    fp=_action(h,**kw); f0=_action(0.0,**kw); fm=_action(-h,**kw)
    return (fp-2*f0+fm)/(h*h)


def _profile_integrals(T,R,order):
    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    etas=T*xt; rs=.5*R*(xr+1.0); ew=T*wt; rw=.5*R*wr
    ik=0.0; ig=0.0
    for i,eta in enumerate(etas):
        for j,r in enumerate(rs):
            _,pe,pr=_profile(float(eta),float(r),T,R)
            ww=ew[i]*rw[j]*r*r
            ik += ww*pe*pe; ig += ww*pr*pr
    return float(ik),float(ig)


def recover_native_relative_aoki_coefficients(*,betas,K,w,mu,
        time_scales=(0.5,1.0,2.0),radius=1.0,hubble_step=0.007,
        amplitude_step=0.002,quadrature_order=18):
    vals=(K,w,mu,radius,hubble_step,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals) or K<=0 or mu<=-1 or radius<=0 or hubble_step<=0 or amplitude_step<=0:
        raise ValueError('invalid native Aoki oracle inputs')
    rows=[]; rhs=[]
    for T in time_scales:
        common=dict(betas=tuple(betas),K=float(K),w=float(w),mu=float(mu),T=float(T),R=float(radius),order=int(quadrature_order))
        hp=_amp_hessian(H0=+hubble_step,amplitude_step=amplitude_step,**common)
        hm=_amp_hessian(H0=-hubble_step,amplitude_step=amplitude_step,**common)
        h0=_amp_hessian(H0=0.0,amplitude_step=amplitude_step,**common)
        h2=(hp+hm-2*h0)/(2*hubble_step*hubble_step)
        ik,ig=_profile_integrals(float(T),float(radius),int(quadrature_order))
        rows.append((ik,ig)); rhs.append(h2)
    X=np.asarray(rows,float); y=np.asarray(rhs,float)
    coeff,_,rank,_=np.linalg.lstsq(X,y,rcond=None)
    if rank!=2 or abs(coeff[0])<1e-16:
        raise np.linalg.LinAlgError('native Aoki compact fit is rank deficient')
    residual=float(np.linalg.norm(X@coeff-y)/max(1.0,np.linalg.norm(y)))
    return NativeRelativeAokiCoefficients(float(coeff[0]),float(coeff[1]),float(-coeff[1]/coeff[0]),residual)
