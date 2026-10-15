"""Compact HR six-field Hessian on a local non-homothetic FLRW Taylor jet."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class CompactNonhomotheticHRSixFieldHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile_value(t,r,T,R):
    if abs(t)>=T or r<=0.0 or r>=R:
        return 0.0
    x=t/T
    return (1.0-x*x)**3*(r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6)


def _profiles(t,r,T,R):
    x=t/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    Att=(-6.0+36.0*x*x-30.0*x**4)/(T*T)
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr=2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    Frr=2.0-36.0*r**2/R**2+90.0*r**4/R**4-56.0*r**6/R**6
    return A,At,Att,F,Fr,Frr


def _bg_at(t,jet,mu0,mu_p0,mu_pp0):
    a=jet.a+jet.a_p*t+0.5*jet.a_pp*t*t
    ap=jet.a_p+jet.a_pp*t
    xi=jet.xi+jet.xi_p*t+0.5*jet.xi_pp*t*t
    c=jet.c+jet.c_p*t
    mu=mu0+mu_p0*t+0.5*mu_pp0*t*t
    mup=mu_p0+mu_pp0*t
    if a<=0 or xi<=0 or c<=0 or mu<=-1:
        raise ValueError("local Taylor background left regular branch")
    Hc=ap/a
    Hcp=jet.a_pp/a-Hc*Hc
    Cp=mup/((1.0+mu)**2)
    C=mu/(1.0+mu)
    L=1.0/(1.0+mu)
    Lp=-Cp
    S=c+1.0+mu
    q=mup+Hc*mu*S
    qp=(mu_pp0+Hcp*mu*S+Hc*mup*S+Hc*mu*(jet.c_p+mup))
    tau=jet.c*t+0.5*jet.c_p*t*t
    return a,ap,xi,c,mu,mup,Hc,Hcp,C,Cp,L,Lp,q,qp,tau


def _a_of_eta(eta,jet):
    return jet.a+jet.a_p*eta+0.5*jet.a_pp*eta*eta


def _b_of_etaf(etaf,jet):
    fj=jet.f_native
    return fj.b+fj.b_f_p*etaf+0.5*fj.b_f_pp*etaf*etaf


def _action(x,*,betas,jet,mu,mu_p,mu_pp,time_radius,radial_radius,quadrature_order):
    eta_amp,r_amp,pg,sg,pf,sf=[float(v) for v in x]
    xt,wt=np.polynomial.legendre.leggauss(quadrature_order)
    xr,wr=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*xt; rs=0.5*radial_radius*(xr+1.0)
    tw=time_radius*wt; rw=0.5*radial_radius*wr
    b0,b1,b2,b3,b4=[float(v) for v in betas]
    total=0.0
    for i,t in enumerate(ts):
        a,ap,xi,c,mut,mutp,Hc,Hcp,C,Cp,L,Lp,q,qp,tau=_bg_at(float(t),jet,mu,mu_p,mu_pp)
        inva2=1.0/(a*a); inva2_t=-2.0*Hc*inva2
        for j,r in enumerate(rs):
            r=float(r)
            A,At,Att,F,Fr,Frr=_profiles(float(t),r,time_radius,radial_radius)
            P=At*F; Q=A*Fr; Pt=Att*F; Pr=At*Fr; Qt=Pr; Qr=A*Frr
            E=inva2*(-P+r*Hc*C*Q)
            Et=(inva2_t*(-P+r*Hc*C*Q)
                +inva2*(-Pt+r*((Hcp*C+Hc*Cp)*Q+Hc*C*Qt)))
            Er=inva2*(-Pr+Hc*C*(Q+r*Qr))
            R=inva2*(L*Q+r*Hc*C*P)
            Rt=(inva2_t*(L*Q+r*Hc*C*P)
                +inva2*(Lp*Q+L*Qt+r*((Hcp*C+Hc*Cp)*P+Hc*C*Pt)))
            Rr=inva2*(L*Qr+Hc*C*(P+r*Pr))
            deta=eta_amp*E; drad=r_amp*R
            eta_g=float(t)+deta; rg=r+drad
            ag=_a_of_eta(eta_g,jet)
            if ag<=0 or rg<=0: raise ValueError("g chart left positive branch")
            phig=pg*_profile_value(eta_g,rg,time_radius,radial_radius)
            psig=sg*_profile_value(eta_g,rg,time_radius,radial_radius)
            Jg=np.array([[1.0+eta_amp*Et,eta_amp*Er],[r_amp*Rt,1.0+r_amp*Rr]],float)
            gn=ag*ag*np.diag([-math.exp(2.0*phig),math.exp(2.0*psig)])
            gc=Jg.T@gn@Jg; gang=ag*ag*rg*rg

            eta_f=tau-0.5*q*r*r
            eta_ft=c-0.5*qp*r*r
            eta_fr=-q*r
            rf=(1.0+mut)*r
            rf_t=mutp*r
            rf_r=1.0+mut
            bf=_b_of_etaf(eta_f,jet)
            if bf<=0 or rf<=0: raise ValueError("f chart left positive branch")
            phif=pf*_profile_value(eta_f,rf,time_radius,radial_radius)
            psif=sf*_profile_value(eta_f,rf,time_radius,radial_radius)
            Jf=np.array([[eta_ft,eta_fr],[rf_t,rf_r]],float)
            fn=bf*bf*np.diag([-math.exp(2.0*phif),math.exp(2.0*psif)])
            fc=Jf.T@fn@Jf; fang=bf*bf*rf*rf

            A2=np.linalg.solve(gc,fc)
            det=float(np.linalg.det(A2)); tr=float(np.trace(A2))
            if det<=0: raise ValueError("g^-1 f determinant nonpositive")
            sd=math.sqrt(det); den=tr+2.0*sd
            if den<=0: raise ValueError("principal square root nonreal")
            Sr=(A2+sd*np.eye(2))/math.sqrt(den)
            trS=float(np.trace(Sr)); detS=float(np.linalg.det(Sr)); ell=math.sqrt(fang/gang)
            e1=trS+2.0*ell
            e2=detS+2.0*ell*trS+ell*ell
            e3=2.0*ell*detS+ell*ell*trS
            e4=ell*ell*detS
            pot=b0+b1*e1+b2*e2+b3*e3+b4*e4
            sqrtg=math.sqrt(-float(np.linalg.det(gc)))*gang
            total += tw[i]*rw[j]*sqrtg*pot
    return float(total)


def compact_hr_six_field_hessian_nonhomothetic(*,betas,jet,mu,mu_p=0.0,mu_pp=0.0,
                                                time_radius,radial_radius,
                                                amplitude_step=7e-4,quadrature_order=16):
    if len(tuple(betas))!=5 or mu<=-1 or amplitude_step<=0 or time_radius<=0 or radial_radius<=0:
        raise ValueError("invalid nonhomothetic compact HR inputs")
    vals=(mu,mu_p,mu_pp,amplitude_step,time_radius,radial_radius)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("nonhomothetic compact HR inputs must be finite")
    h=float(amplitude_step); n=6
    kw=dict(betas=tuple(betas),jet=jet,mu=float(mu),mu_p=float(mu_p),mu_pp=float(mu_pp),
            time_radius=float(time_radius),radial_radius=float(radial_radius),quadrature_order=int(quadrature_order))
    z=np.zeros(n); f0=_action(z,**kw); g=np.zeros(n); H=np.zeros((n,n))
    for i in range(n):
        ei=np.zeros(n); ei[i]=h
        fp=_action(ei,**kw); fm=_action(-ei,**kw)
        g[i]=(fp-fm)/(2.0*h); H[i,i]=(fp-2.0*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=h
            hij=(_action(ei+ej,**kw)-_action(ei-ej,**kw)-_action(-ei+ej,**kw)+_action(-ei-ej,**kw))/(4.0*h*h)
            H[i,j]=H[j,i]=hij
    return CompactNonhomotheticHRSixFieldHessian(gradient=g,hessian=H)
