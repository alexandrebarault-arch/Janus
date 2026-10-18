"""Exact nonlinear spherical Hassan--Rosen interaction: diagonal vs relative chart Ward.

The metric pair shares one common spherical spacetime. The f metric is a
native Lorentzian FLRW scalar field pulled back through a finite nonhomothetic
(T,R)(t,r) chart. A compact *diagonal* diffeomorphism of both g and f must
leave the interaction action invariant. By contrast a displacement of ONLY
f's native chart is a relative-field variation and generally changes
beta1/2/3 interaction. beta0 and beta4 decouple in the relative test.

This is an OFF-SHELL action/coordinate-invariance audit, not a derivation of
the canonical physical scalar modes, EH+matter equations or fold crossing.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

BETAS=(.21,.78,-.35,.16,.11)

@dataclass(frozen=True)
class CoupledChartWard:
    baseline: float
    diagonal_variations: np.ndarray
    relative_variations: np.ndarray
    chart_orientation_min: float


def _quad(time_radius, radial_radius, order):
    if not all(math.isfinite(float(q)) and q>0 for q in (time_radius,radial_radius)):
        raise ValueError('positive finite compact domains required')
    if type(order) is not int or order<10:
        raise ValueError('Gauss Legendre order must be int >=10')
    z,w=np.polynomial.legendre.leggauss(order)
    t=time_radius*z[:,None]
    r=radial_radius*(z[None,:]+1)/2
    wt=2*math.pi*time_radius*radial_radius*w[:,None]*w[None,:]
    return t,r,wt


def _bump(t,r,Tmax,Rmax):
    A=(1-(t/Tmax)**2)**4
    At=-8*t/Tmax**2*(1-(t/Tmax)**2)**3
    F=(1-(r/Rmax)**2)**4
    Fr=-8*r/Rmax**2*(1-(r/Rmax)**2)**3
    return A*F,At*F,A*Fr,r*A*F,r*At*F,A*(F+r*Fr)


def _native_chart(u,v):
    sigma=.08+.025*u
    mu=-.22+.05*u
    T=u+.5*sigma*v*v
    R=(1+mu)*v
    return (T,R,1+.5*.025*v*v,sigma*v,.05*v,1+mu)


def _native_metric(time,radius,sector,amplitudes):
    """Spherical scalar metric: (g00,g01,g11, g_angular_per_sin2)."""
    x=np.asarray(amplitudes,float)
    if x.shape!=(4,) or not np.all(np.isfinite(x)):
        raise ValueError('four finite scalar native metric amplitudes required')
    T,R=np.broadcast_arrays(time,radius)
    if sector=='g':
        n=1.04+.035*T+.01*T*T
        a=.95+.06*T+.012*T*T
    elif sector=='f':
        n=1.13+.045*T+.012*T*T
        a=.87+.09*T+.025*T*T
    else:raise ValueError('sector must be g or f')
    k=1.6
    q=1+.17*T+(.07+.02*T)*R*R
    phi=x[0]*q
    shift=x[1]*R*(1+.11*T+.07*R*R)
    psi=x[2]*(1+.13*T+.04*R*R)
    E=x[3]*R*R*(1+.08*T+.03*R*R)
    qr=1+2*psi-2*k*k*E/3
    qt=1+2*psi+k*k*E/3
    return (-n*n*(1+2*phi),n*a*shift,a*a*qr,a*a*R*R*qt)


def _pull(native,j00,j01,j10,j11):
    x,y,z,area=native
    p00=x*j00*j00+2*y*j00*j10+z*j10*j10
    p01=x*j00*j01+y*(j00*j11+j10*j01)+z*j10*j11
    p11=x*j01*j01+2*y*j01*j11+z*j11*j11
    return (p00,p01,p11,area)


def _interaction_density(g,f,betas):
    g00,g01,g11,ggy=g
    f00,f01,f11,fyy=f
    dg=g00*g11-g01*g01
    df=f00*f11-f01*f01
    if np.any(dg>=0) or np.any(df>=0) or np.any(ggy<=0) or np.any(fyy<=0):
        raise ValueError('metric left Lorentzian spherical branch')
    dets=np.sqrt(df/dg)
    tra=(g11*f00+g00*f11-2*g01*f01)/dg
    if np.any(tra+2*dets<=0):
        raise ValueError('real principal radial square-root branch lost')
    trs=np.sqrt(tra+2*dets)
    ell=np.sqrt(fyy/ggy)
    es=(np.ones_like(trs),trs+2*ell,dets+2*ell*trs+ell*ell,
        2*ell*dets+ell*ell*trs,ell*ell*dets)
    poly=sum(float(b)*e for b,e in zip(betas,es))
    return -np.sqrt(-dg)*ggy*poly


def coupled_hr_spacetime_action(*,betas=BETAS,mode='diagonal',eps_time=0.,
        eps_radial=0.,g_fields=(.012,-.014,.016,.009),
        f_fields=(-.017,.013,-.011,.008),time_radius=.4,
        radial_radius=.6,quadrature_order=40):
    """Integrate 4pi dt dr interaction with both metrics pulled correctly.

    diagonal: same compact common-chart displacement pulls back BOTH metrics;
    relative_f: only the f-native chart (T,R) is displaced, g fixed.
    """
    bs=tuple(float(z) for z in betas)
    if len(bs)!=5 or not all(math.isfinite(z) for z in bs):
        raise ValueError('five finite HR betas required')
    if mode not in ('diagonal','relative_f'):raise ValueError('invalid chart mode')
    eT=float(eps_time);eR=float(eps_radial)
    if not all(math.isfinite(x) for x in (eT,eR)):
        raise ValueError('nonfinite chart amplitudes')
    t,r,w=_quad(time_radius,radial_radius,quadrature_order)
    b,bt,br,c,ct,cr=_bump(t,r,time_radius,radial_radius)
    if mode=='diagonal':
        u=t+eT*b;v=r+eR*c
        jt0=1+eT*bt; jr0=eT*br
        jt1=eR*ct; jr1=1+eR*cr
        if np.min(jt0*jr1-jr0*jt1)<=0 or np.min(v)<=0:
            raise ValueError('g common chart has nonpositive orientation or radius')
        gu=_pull(_native_metric(u,v,'g',g_fields),jt0,jr0,jt1,jr1)
        T,R,Tt,Tr,Rt,Rr=_native_chart(u,v)
        fJ00=Tt*jt0+Tr*jt1
        fJ01=Tt*jr0+Tr*jr1
        fJ10=Rt*jt0+Rr*jt1
        fJ11=Rt*jr0+Rr*jr1
    else:
        gu=_native_metric(t,r,'g',g_fields)
        T,R,Tt,Tr,Rt,Rr=_native_chart(t,r)
        T=T+eT*b
        R=R+eR*c
        fJ00=Tt+eT*bt
        fJ01=Tr+eT*br
        fJ10=Rt+eR*ct
        fJ11=Rr+eR*cr
    dj=fJ00*fJ11-fJ01*fJ10
    if np.min(dj)<=0 or np.any(R<=0):raise ValueError('f-native radial chart not regular')
    fu=_pull(_native_metric(T,R,'f',f_fields),fJ00,fJ01,fJ10,fJ11)
    value=float(np.sum(w*_interaction_density(gu,fu,bs)))
    return value


def diagonal_and_relative_ward(*,betas=BETAS,order=40):
    """Finite-difference coordinate response: 2 chart displacements each."""
    baseline=coupled_hr_spacetime_action(betas=betas,quadrature_order=order)
    diag=[];rel=[]
    for mode,out in (('diagonal',diag),('relative_f',rel)):
        for et,er in ((.04,0.),(0.,-.04),(.035,-.023)):
            out.append(coupled_hr_spacetime_action(betas=betas,mode=mode,
                eps_time=et,eps_radial=er,quadrature_order=order)-baseline)
    t,r,_=_quad(.4,.6,order)
    _,_,Tt,Tr,Rt,Rr=_native_chart(t,r)
    det_min=float(np.min(Tt*Rr-Tr*Rt))
    return CoupledChartWard(baseline,np.array(diag),np.array(rel),det_min)
