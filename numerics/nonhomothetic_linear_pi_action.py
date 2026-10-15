"""Compact HR Hessian for the linear (mu=0) non-homothetic scalar pi map."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class CompactNonhomotheticLinearPiHessian:
    gradient: np.ndarray
    hessian: np.ndarray


def _profile(t,r,T,R):
    x=t/T
    A=(1-x*x)**3; At=(-6*x*(1-x*x)**2)/T; Att=(-6+36*x*x-30*x**4)/(T*T)
    F=r*r-3*r**4/R**2+3*r**6/R**4-r**8/R**6
    Fr=2*r-12*r**3/R**2+18*r**5/R**4-8*r**7/R**6
    Frr=2-36*r**2/R**2+90*r**4/R**4-56*r**6/R**6
    return A,At,Att,F,Fr,Frr


def _pv(t,r,T,R):
    if abs(t)>=T or r<=0 or r>=R: return 0.0
    A,_,_,F,_,_=_profile(t,r,T,R); return A*F


def _action(x,*,betas,jet,T,R,order):
    pi,pg,sg,pf,sf=[float(v) for v in x]
    xt,wt=np.polynomial.legendre.leggauss(order); xr,wr=np.polynomial.legendre.leggauss(order)
    ts=T*xt; rs=.5*R*(xr+1); tw=T*wt; rw=.5*R*wr
    b0,b1,b2,b3,b4=map(float,betas); total=0.0
    Tf=jet.c*T
    for i,t in enumerate(ts):
        a=jet.a+jet.a_p*t+.5*jet.a_pp*t*t; ap=jet.a_p+jet.a_pp*t
        c=jet.c+jet.c_p*t; H=ap/a; inv=1/(a*a); invp=-2*H*inv
        tau=jet.c*t+.5*jet.c_p*t*t
        fj=jet.f_native; b=fj.b+fj.b_f_p*tau+.5*fj.b_f_pp*tau*tau
        if min(a,c,b)<=0: raise ValueError('Taylor background left positive branch')
        for j,r in enumerate(rs):
            A,At,Att,F,Fr,Frr=_profile(float(t),float(r),T,R)
            P=At*F; Q=A*Fr; Pt=Att*F; Pr=At*Fr; Qt=Pr; Qr=A*Frr
            E=-inv*P; Et=-(invp*P+inv*Pt); Er=-inv*Pr
            D=inv*c*Q
            Dt=invp*c*Q+inv*jet.c_p*Q+inv*c*Qt
            Dr=inv*c*Qr
            de=pi*E; dr=pi*D
            etag=t+de; rg=r+dr
            ag=jet.a+jet.a_p*etag+.5*jet.a_pp*etag*etag
            if ag<=0 or rg<=0: raise ValueError('g chart left positive branch')
            Jg=np.array([[1+pi*Et,pi*Er],[pi*Dt,1+pi*Dr]],float)
            phig=pg*_pv(etag,rg,T,R); psig=sg*_pv(etag,rg,T,R)
            gn=ag*ag*np.diag([-math.exp(2*phig),math.exp(2*psig)])
            gc=Jg.T@gn@Jg; gang=ag*ag*rg*rg

            etaf=tau; rf=r
            phif=pf*_pv(etaf,rf,Tf,R); psif=sf*_pv(etaf,rf,Tf,R)
            Jf=np.array([[c,0.0],[0.0,1.0]],float)
            fn=b*b*np.diag([-math.exp(2*phif),math.exp(2*psif)])
            fc=Jf.T@fn@Jf; fang=b*b*r*r
            A2=np.linalg.solve(gc,fc); det=float(np.linalg.det(A2)); tr=float(np.trace(A2))
            if det<=0: raise ValueError('g^-1 f determinant nonpositive')
            sd=math.sqrt(det); den=tr+2*sd
            if den<=0: raise ValueError('principal square root nonreal')
            S=(A2+sd*np.eye(2))/math.sqrt(den); trS=float(np.trace(S)); detS=float(np.linalg.det(S)); ell=math.sqrt(fang/gang)
            e1=trS+2*ell; e2=detS+2*ell*trS+ell*ell; e3=2*ell*detS+ell*ell*trS; e4=ell*ell*detS
            pot=b0+b1*e1+b2*e2+b3*e3+b4*e4
            total += tw[i]*rw[j]*math.sqrt(-float(np.linalg.det(gc)))*gang*pot
    return float(total)


def compact_hr_linear_pi_five_field_hessian(*,betas,jet,time_radius,radial_radius,amplitude_step=3e-5,quadrature_order=14):
    if len(tuple(betas))!=5 or min(time_radius,radial_radius,amplitude_step)<=0: raise ValueError('invalid inputs')
    h=float(amplitude_step); n=5; kw=dict(betas=tuple(betas),jet=jet,T=float(time_radius),R=float(radial_radius),order=int(quadrature_order))
    z=np.zeros(n); f0=_action(z,**kw); g=np.zeros(n); H=np.zeros((n,n))
    for i in range(n):
        ei=np.zeros(n); ei[i]=h; fp=_action(ei,**kw); fm=_action(-ei,**kw)
        g[i]=(fp-fm)/(2*h); H[i,i]=(fp-2*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=h
            H[i,j]=H[j,i]=(_action(ei+ej,**kw)-_action(ei-ej,**kw)-_action(-ei+ej,**kw)+_action(-ei-ej,**kw))/(4*h*h)
    return CompactNonhomotheticLinearPiHessian(gradient=g,hessian=H)
