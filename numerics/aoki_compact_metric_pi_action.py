"""Compact-support HR interaction Hessian for (pi, phi_g, psi_g, phi_f, psi_f)."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class CompactHRFiveFieldHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile_value(t,r,T,R):
    if abs(t) >= T or r <= 0.0 or r >= R:
        return 0.0
    x=t/T
    A=(1.0-x*x)**3
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    return A*F


def _pi_profiles(t,r,T,R):
    x=t/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    Att=(-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr=2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    Frr=2.0-36.0*r**2/R**2+90.0*r**4/R**4-56.0*r**6/R**6
    return A,At,Att,F,Fr,Frr


def _action(x, *, betas,K,w,mu,conformal_H,time_radius,radial_radius,quadrature_order):
    pi_amp,pg,sg,pf,sf=[float(v) for v in x]
    p=2.0/(1.0+3.0*w)
    xt,wt=np.polynomial.legendre.leggauss(quadrature_order)
    xr,wr=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*xt
    rs=0.5*radial_radius*(xr+1.0)
    tw=time_radius*wt
    rw=0.5*radial_radius*wr
    b0,b1,b2,b3,b4=[float(v) for v in betas]
    total=0.0
    C=mu/(1.0+mu)
    M=mu*(2.0+mu)
    for i,t in enumerate(ts):
        u=1.0+conformal_H*t/p
        if u<=0:
            raise ValueError("compact support leaves FLRW chart")
        Hc=conformal_H/u
        Hcp=-(conformal_H*conformal_H/p)/(u*u)
        abase=u**p
        inva2=abase**-2
        for j,r in enumerate(rs):
            A,At,Att,F,Fr,Frr=_pi_profiles(t,r,time_radius,radial_radius)
            P=pi_amp*At*F
            Q=pi_amp*A*Fr
            Pt=pi_amp*Att*F
            Pr=pi_amp*At*Fr
            Qt=Pr
            Qr=pi_amp*A*Frr
            deta=inva2*(-P+r*Hc*C*Q)
            drad=inva2*(Q/(1.0+mu)+r*Hc*C*P)
            inva2_t=-2.0*Hc*inva2
            deta_t=(inva2_t*(-P+r*Hc*C*Q)
                    +inva2*(-Pt+r*C*(Hcp*Q+Hc*Qt)))
            deta_r=inva2*(-Pr+C*Hc*(Q+r*Qr))
            drad_t=(inva2_t*(Q/(1.0+mu)+r*Hc*C*P)
                    +inva2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt)))
            drad_r=inva2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))

            eta_g=t+deta; rg=r+drad
            ug=1.0+conformal_H*eta_g/p
            if ug<=0 or rg<=0:
                raise ValueError("g chart left positive branch")
            ag=ug**p
            phig=pg*_profile_value(eta_g,rg,time_radius,radial_radius)
            psig=sg*_profile_value(eta_g,rg,time_radius,radial_radius)
            Jg=np.array([[1.0+deta_t,deta_r],[drad_t,1.0+drad_r]],dtype=float)
            gn=ag*ag*np.diag([-math.exp(2*phig),math.exp(2*psig)])
            gc=Jg.T@gn@Jg
            gang=ag*ag*rg*rg

            eta_f=t-0.5*Hc*r*r*M
            eta_ft=1.0-0.5*Hcp*r*r*M
            eta_fr=-Hc*r*M
            rf=(1.0+mu)*r
            uf=1.0+conformal_H*eta_f/p
            if uf<=0 or rf<=0:
                raise ValueError("f chart left positive branch")
            af=uf**p
            phif=pf*_profile_value(eta_f,rf,time_radius,radial_radius)
            psif=sf*_profile_value(eta_f,rf,time_radius,radial_radius)
            Jf=np.array([[eta_ft,eta_fr],[0.0,1.0+mu]],dtype=float)
            fn=(K*af)**2*np.diag([-math.exp(2*phif),math.exp(2*psif)])
            fc=Jf.T@fn@Jf
            fang=(K*af)**2*rf*rf

            A2=np.linalg.solve(gc,fc)
            det=float(np.linalg.det(A2)); tr=float(np.trace(A2))
            if det<=0:
                raise ValueError("g^-1 f determinant nonpositive")
            sd=math.sqrt(det); den=tr+2*sd
            if den<=0:
                raise ValueError("principal square root nonreal")
            Sr=(A2+sd*np.eye(2))/math.sqrt(den)
            trS=float(np.trace(Sr)); detS=float(np.linalg.det(Sr))
            ell=math.sqrt(fang/gang)
            e1=trS+2*ell
            e2=detS+2*ell*trS+ell*ell
            e3=2*ell*detS+ell*ell*trS
            e4=ell*ell*detS
            pot=b0+b1*e1+b2*e2+b3*e3+b4*e4
            sqrtg=math.sqrt(-float(np.linalg.det(gc)))*gang
            total += tw[i]*rw[j]*sqrtg*pot
    return float(total)


def compact_hr_five_field_hessian(*, betas,K,w,mu,conformal_H,
                                  time_radius,radial_radius,
                                  amplitude_step=7e-4,quadrature_order=16):
    if len(tuple(betas))!=5:
        raise ValueError("betas must have length five")
    if K<=0 or mu<=-1 or time_radius<=0 or radial_radius<=0 or amplitude_step<=0:
        raise ValueError("invalid compact HR inputs")
    if abs(1+3*w)<1e-12:
        raise ValueError("w=-1/3 unsupported")
    h=float(amplitude_step); n=5
    kwargs=dict(betas=tuple(betas),K=K,w=w,mu=mu,conformal_H=conformal_H,
                time_radius=time_radius,radial_radius=radial_radius,
                quadrature_order=quadrature_order)
    zero=np.zeros(n)
    f0=_action(zero,**kwargs)
    H=np.zeros((n,n),dtype=float)
    g=np.zeros(n,dtype=float)
    for i in range(n):
        ei=np.zeros(n); ei[i]=h
        fp=_action(ei,**kwargs); fm=_action(-ei,**kwargs)
        g[i]=(fp-fm)/(2*h)
        H[i,i]=(fp-2*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=h
            fpp=_action(ei+ej,**kwargs)
            fpm=_action(ei-ej,**kwargs)
            fmp=_action(-ei+ej,**kwargs)
            fmm=_action(-ei-ej,**kwargs)
            hij=(fpp-fpm-fmp+fmm)/(4*h*h)
            H[i,j]=H[j,i]=hij
    return CompactHRFiveFieldHessian(gradient=g,hessian=H)
