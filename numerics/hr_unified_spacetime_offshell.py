"""Same-field-space full spacetime EH_g+EH_f+HR+two irrotational dust actions.

This is an OFF-SHELL, explicitly specified native scalar trial model. All
five action densities are evaluated on exactly the same g and f spherical
metrics, native polynomial backgrounds and compact spacetime integration.
The two dust sectors use the covariant irrotational-pressureless-fluid
Lagrange-multiplier formulation, not yet the time-dependent canonical
phase-space reduction used in the earlier *separate* dust audit.

NOT an on-shell Candidate-C solution; not the physical BD-constrained
scalar theory. EH is the native ADM+GHY representative with a positive
Planck coefficient and chart-invariant spacetime boundary prescription.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_coupled_diagonal_ward import (
    BETAS, _quad, _bump, _native_chart, _native_metric,
    _interaction_density, _pull,
)

CONTRIBUTIONS=('EH_g','EH_f','HR','dust_g','dust_f')
FIELD_ORDER=('Phi_g','U_g','psi_g','E_g','theta_g','rho_g',
             'Phi_f','U_f','psi_f','E_f','theta_f','rho_f')

@dataclass(frozen=True)
class UnifiedAction:
    value: float
    components: np.ndarray
    minimum_g_jacobian: float
    minimum_f_jacobian: float
    components_order: tuple[str,...] = CONTRIBUTIONS


def _background(T,sector):
    if sector=='g':
        n=1.04+.035*T+.01*T*T
        a=.95+.06*T+.012*T*T
        ad=.06+.024*T
        nd=.035+.02*T
        rho_const=.7
    elif sector=='f':
        n=1.13+.045*T+.012*T*T
        a=.87+.09*T+.025*T*T
        ad=.09+.05*T
        nd=.045+.024*T
        rho_const=.43
    else:raise ValueError('unknown metric sector')
    return n,a,ad,nd,rho_const


def native_geometry_and_densities(T,R,sector,fields, *, k=1.6, planck=1.):
    """Exact ADM+GHY, covariant irrotational-dust densities per dT dR dOmega.

    fields=(Phi,U,psi,E,theta_amplitude,rho_amplitude).
    Dust: L=-rho/2 sqrt(-metric) [(metric^-1)^{AB}theta_A theta_B+1].
    A native background theta_0'(T)=n(T) obeys the dust norm constraint,
    rho_0(T)=rho_const/a(T)^3 enforces native homogeneous dust continuity.
    Metric perturbations and matter ansatz are polynomial trial functions.
    """
    x=np.asarray(fields,dtype=float)
    if x.shape!=(6,) or not np.all(np.isfinite(x)):
        raise ValueError('six finite native metric/dust amplitudes required')
    T,R=np.broadcast_arrays(np.asarray(T,float),np.asarray(R,float))
    if np.any(R<=0) or not np.all(np.isfinite(T)) or not np.all(np.isfinite(R)):
        raise ValueError('native radius positive and coordinates finite required')
    if not math.isfinite(k) or k<=0 or not math.isfinite(planck) or planck<=0:
        raise ValueError('positive native k and Planck coefficient required')
    n,a,ad,nd,rhoc=_background(T,sector)
    phi=x[0]*(1+.17*T+(.07+.02*T)*R*R)
    U=x[1]*R*(1+.11*T+.07*R*R)
    Ur=x[1]*(1+.11*T+.21*R*R)
    psi=x[2]*(1+.13*T+.04*R*R)
    psir=x[2]*.08*R
    psirr=x[2]*.08*np.ones_like(R)
    psit=x[2]*.13*np.ones_like(R)
    E=x[3]*R*R*(1+.08*T+.03*R*R)
    Er=x[3]*(2*R*(1+.08*T)+.12*R**3)
    Err=x[3]*(2*(1+.08*T)+.36*R*R)
    Et=x[3]*.08*R*R
    qr=1+2*psi-2*k*k*E/3
    qt=1+2*psi+k*k*E/3
    qr_r=2*psir-2*k*k*Er/3
    qt_r=2*psir+k*k*Er/3
    qt_rr=2*psirr+k*k*Err/3
    qr_t=2*psit-2*k*k*Et/3
    qt_t=2*psit+k*k*Et/3
    lapse_sq=1+2*phi+U*U/qr
    if (np.any(a<=0) or np.any(n<=0) or np.any(qr<=0)
       or np.any(qt<=0) or np.any(lapse_sq<=0)):
        raise ValueError('invalid positive native ADM/lapse branch')
    lapse=n*np.sqrt(lapse_sq)
    L=a*np.sqrt(qr)
    S=a*R*np.sqrt(qt)
    z=1+R*qt_r/(2*qt)
    w=np.sqrt(qt/qr)*z
    w_r=np.sqrt(qt/qr)*(
        (qt_r/qt-qr_r/qr)*z/2 + qt_r/(2*qt)
        +R*(qt_rr/qt-(qt_r/qt)**2)/2)
    R3=2/S**2*(1-w*w-2*(S/L)*w_r)
    nr=(n/a)*U/qr
    nr_r=(n/a)*(Ur/qr-U*qr_r/(qr*qr))
    Kr=(ad/a+qr_t/(2*qr)-nr_r-nr*qr_r/(2*qr))/lapse
    Kt=(ad/a+qt_t/(2*qt)-nr*(1/R+qt_r/(2*qt)))/lapse
    eh=.5*planck*lapse*L*S*S*(R3-4*Kr*Kt-2*Kt*Kt)
    metric=_native_metric(T,R,sector,x[:4])
    det=metric[0]*metric[2]-metric[1]*metric[1]
    if np.any(det>=0) or np.any(metric[3]<=0):
        raise ValueError('native metric left Lorentzian branch')
    # Dust phase theta=integral n(T)dT + y*(1+.16T)(1+.10R^2).
    bump= (1+.16*T)*(1+.10*R*R)
    thetat=n+x[4]*.16*(1+.10*R*R)
    thetar=x[4]*(1+.16*T)*.20*R
    rho=(rhoc/(a*a*a))*(1+x[5]*(1+.12*T+.08*R*R))
    if np.any(rho<=0):raise ValueError('dust density left positive branch')
    norm=(metric[2]*thetat*thetat-2*metric[1]*thetat*thetar
         +metric[0]*thetar*thetar)/det
    dust=-.5*np.sqrt(-det)*metric[3]*rho*(norm+1)
    if not np.all(np.isfinite(eh)) or not np.all(np.isfinite(dust)):
        raise ArithmeticError('nonfinite native action')
    return eh,dust,metric


def unified_spacetime_action(*,betas=BETAS,
        fields_g=(.012,-.014,.016,.009,.025,-.017),
        fields_f=(-.017,.013,-.011,.008,-.022,.015),
        mode='diagonal', eps_time=0.,eps_radial=0.,
        time_radius=.4,radial_radius=.6,quadrature_order=40,
        planck_g=1.,planck_f=1.35,hr_mass2=.7):
    """Five coupled action sectors with a single source for both native metrics.

    diagonal: pull both g and f under the SAME compact common-chart map.
    relative_f: change only the f-native (T,R) map; g stays fixed.
    Components are individually measurable (EH_g, EH_f, HR, dust_g,
    dust_f). Both dust contributions remain separately covariant.
    """
    bs=tuple(float(z) for z in betas)
    if len(bs)!=5 or not all(math.isfinite(z) for z in bs):
        raise ValueError('five finite HR coefficients required')
    if mode not in ('diagonal','relative_f'):
        raise ValueError('mode must be diagonal or relative_f')
    if not all(math.isfinite(float(z)) and float(z)>0 for z in (planck_g,planck_f)):
        raise ValueError('both Planck coefficients must be finite positive')
    if not math.isfinite(float(hr_mass2)) or hr_mass2<0:
        raise ValueError('interaction coefficient must be nonnegative')
    eT=float(eps_time);eR=float(eps_radial)
    if not all(math.isfinite(z) for z in (eT,eR)):
        raise ValueError('finite chart amplitude required')
    gfields=np.asarray(fields_g,dtype=float)
    ffields=np.asarray(fields_f,dtype=float)
    if gfields.shape!=(6,) or ffields.shape!=(6,):
        raise ValueError('two six-amplitude native metric+dust sectors required')
    t,r,weights=_quad(time_radius,radial_radius,quadrature_order)
    b,bt,br,c,ct,cr=_bump(t,r,time_radius,radial_radius)
    if mode=='diagonal':
        u=t+eT*b;v=r+eR*c
        jg00=1+eT*bt;jg01=eT*br;jg10=eR*ct;jg11=1+eR*cr
        T,R,Tt,Tr,Rt,Rr=_native_chart(u,v)
        jf00=Tt*jg00+Tr*jg10
        jf01=Tt*jg01+Tr*jg11
        jf10=Rt*jg00+Rr*jg10
        jf11=Rt*jg01+Rr*jg11
    else:
        u=t;v=r
        jg00=np.ones_like(t+0*r);jg01=np.zeros_like(t+0*r)
        jg10=np.zeros_like(t+0*r);jg11=np.ones_like(t+0*r)
        T,R,Tt,Tr,Rt,Rr=_native_chart(t,r)
        T=T+eT*b;R=R+eR*c
        jf00=Tt+eT*bt;jf01=Tr+eT*br
        jf10=Rt+eR*ct;jf11=Rr+eR*cr
    Dg=jg00*jg11-jg01*jg10
    Df=jf00*jf11-jf01*jf10
    if np.min(Dg)<=0 or np.min(Df)<=0 or np.min(v)<=0 or np.min(R)<=0:
        raise ValueError('nonpositive coordinate Jacobian or radial orientation')
    ehg,dg,gm=native_geometry_and_densities(u,v,'g',gfields,planck=planck_g)
    ehf,df,fm=native_geometry_and_densities(T,R,'f',ffields,planck=planck_f)
    gp=_pull(gm,jg00,jg01,jg10,jg11)
    fp=_pull(fm,jf00,jf01,jf10,jf11)
    hr=hr_mass2*_interaction_density(gp,fp,bs)
    components=np.array([
        np.sum(weights*Dg*ehg),np.sum(weights*Df*ehf),
        np.sum(weights*hr),np.sum(weights*Dg*dg),
        np.sum(weights*Df*df)
    ],float)
    return UnifiedAction(float(np.sum(components)),components,
                         float(np.min(Dg)),float(np.min(Df)))
