"""Compact HR Hessian before imposing the one-field Aoki Stueckelberg relation.

The first two amplitudes independently scale the published Aoki profile shapes
for delta_eta and delta_r. Setting them equal projects exactly onto the pi
oracle used by ``aoki_compact_metric_pi_action``.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class CompactHRSixFieldHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile_value(t,r,T,R):
    if abs(t) >= T or r <= 0.0 or r >= R:
        return 0.0
    x=t/T
    return (1.0-x*x)**3*(r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6)


def _profiles(t,r,T,R):
    x=t/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    Att=(-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F=r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6
    Fr=2*r-12*r**3/R**2+18*r**5/R**4-8*r**7/R**6
    Frr=2-36*r**2/R**2+90*r**4/R**4-56*r**6/R**6
    return A,At,Att,F,Fr,Frr


def _action(x, *, betas,K,w,mu,conformal_H,time_radius,radial_radius,quadrature_order):
    eta_amp,r_amp,pg,sg,pf,sf=[float(v) for v in x]
    p=2.0/(1.0+3.0*w)
    xt,wt=np.polynomial.legendre.leggauss(quadrature_order)
    xr,wr=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*xt; rs=0.5*radial_radius*(xr+1.0)
    tw=time_radius*wt; rw=0.5*radial_radius*wr
    b0,b1,b2,b3,b4=[float(v) for v in betas]
    C=mu/(1.0+mu); M=mu*(2.0+mu)
    total=0.0
    for i,t in enumerate(ts):
        u=1.0+conformal_H*t/p
        if u<=0: raise ValueError("compact support leaves FLRW chart")
        Hc=conformal_H/u
        Hcp=-(conformal_H*conformal_H/p)/(u*u)
        abase=u**p; inva2=abase**-2; inva2_t=-2*Hc*inva2
        for j,r in enumerate(rs):
            A,At,Att,F,Fr,Frr=_profiles(t,r,time_radius,radial_radius)
            P=At*F; Q=A*Fr; Pt=Att*F; Pr=At*Fr; Qt=Pr; Qr=A*Frr
            E=inva2*(-P+r*Hc*C*Q)
            Et=inva2_t*(-P+r*Hc*C*Q)+inva2*(-Pt+r*C*(Hcp*Q+Hc*Qt))
            Er=inva2*(-Pr+C*Hc*(Q+r*Qr))
            R=inva2*(Q/(1.0+mu)+r*Hc*C*P)
            Rt=inva2_t*(Q/(1.0+mu)+r*Hc*C*P)+inva2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt))
            Rr=inva2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))
            deta=eta_amp*E; deta_t=eta_amp*Et; deta_r=eta_amp*Er
            drad=r_amp*R; drad_t=r_amp*Rt; drad_r=r_amp*Rr

            eta_g=t+deta; rg=r+drad
            ug=1.0+conformal_H*eta_g/p
            if ug<=0 or rg<=0: raise ValueError("g chart left positive branch")
            ag=ug**p
            phig=pg*_profile_value(eta_g,rg,time_radius,radial_radius)
            psig=sg*_profile_value(eta_g,rg,time_radius,radial_radius)
            Jg=np.array([[1+deta_t,deta_r],[drad_t,1+drad_r]],float)
            gn=ag*ag*np.diag([-math.exp(2*phig),math.exp(2*psig)])
            gc=Jg.T@gn@Jg; gang=ag*ag*rg*rg

            eta_f=t-0.5*Hc*r*r*M
            eta_ft=1.0-0.5*Hcp*r*r*M
            eta_fr=-Hc*r*M; rf=(1.0+mu)*r
            uf=1.0+conformal_H*eta_f/p
            if uf<=0 or rf<=0: raise ValueError("f chart left positive branch")
            af=uf**p
            phif=pf*_profile_value(eta_f,rf,time_radius,radial_radius)
            psif=sf*_profile_value(eta_f,rf,time_radius,radial_radius)
            Jf=np.array([[eta_ft,eta_fr],[0.0,1.0+mu]],float)
            fn=(K*af)**2*np.diag([-math.exp(2*phif),math.exp(2*psif)])
            fc=Jf.T@fn@Jf; fang=(K*af)**2*rf*rf

            A2=np.linalg.solve(gc,fc)
            det=float(np.linalg.det(A2)); tr=float(np.trace(A2))
            if det<=0: raise ValueError("g^-1 f determinant nonpositive")
            sd=math.sqrt(det); den=tr+2*sd
            if den<=0: raise ValueError("principal square root nonreal")
            Sr=(A2+sd*np.eye(2))/math.sqrt(den)
            trS=float(np.trace(Sr)); detS=float(np.linalg.det(Sr)); ell=math.sqrt(fang/gang)
            e1=trS+2*ell
            e2=detS+2*ell*trS+ell*ell
            e3=2*ell*detS+ell*ell*trS
            e4=ell*ell*detS
            pot=b0+b1*e1+b2*e2+b3*e3+b4*e4
            sqrtg=math.sqrt(-float(np.linalg.det(gc)))*gang
            total += tw[i]*rw[j]*sqrtg*pot
    return float(total)


def compact_hr_six_field_hessian(*, betas,K,w,mu,conformal_H,time_radius,radial_radius,
                                  amplitude_step=7e-4,quadrature_order=16):
    if len(tuple(betas))!=5 or K<=0 or mu<=-1 or amplitude_step<=0:
        raise ValueError("invalid six-field compact HR inputs")
    h=float(amplitude_step); n=6
    kw=dict(betas=tuple(betas),K=K,w=w,mu=mu,conformal_H=conformal_H,
            time_radius=time_radius,radial_radius=radial_radius,quadrature_order=quadrature_order)
    z=np.zeros(n); f0=_action(z,**kw)
    g=np.zeros(n); H=np.zeros((n,n))
    for i in range(n):
        ei=np.zeros(n); ei[i]=h
        fp=_action(ei,**kw); fm=_action(-ei,**kw)
        g[i]=(fp-fm)/(2*h); H[i,i]=(fp-2*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=h
            hij=(_action(ei+ej,**kw)-_action(ei-ej,**kw)-_action(-ei+ej,**kw)+_action(-ei-ej,**kw))/(4*h*h)
            H[i,j]=H[j,i]=hij
    return CompactHRSixFieldHessian(gradient=g,hessian=H)
