"""Step32d: genuinely compact and time-INTEGRABLE four metric scalar velocities.

18-slot common-time action: old Step32a 14 slots, followed by four NEW
independent *parent field* amplitudes psi_g_extra,E_g_extra,psi_f_extra,
E_f_extra. Their prescribed parent profile is G(t)=t*T(t), with
G'(t)=T(t)+t*T'(t); unlike Step32b these are NOT disconnected rate jets.

Both g/f Einstein-Hilbert actions are recomputed exactly from complete
spherical ADM intrinsic curvature and extrinsic curvature, not patched with
kinetic terms alone. Full all-beta HR + two exact canonical dust sectors use
THE SAME perturbed metric components. Background remains physically
HOMOGENEOUS Candidate-C dust-only; no BD/ADM reduction or stability verdict.
The old two dust theta_rate jets are still independent local probes.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_full_onshell_tadpole import (
    Trajectory,profile,hr_density,BETAS,M2,MG2,MF2,CG,CF
)
from numerics.hr_two_dust_common_time_canonical import (
    adm_dust_geometry,phase_samples,dust_reduced_density,
    action as old_action,ORDER as OLD_ORDER
)

ORDER=OLD_ORDER+('psi_g_extra_tT','E_g_extra_tT',
                 'psi_f_extra_tT','E_f_extra_tT')
PARENT_INDICES=(14,15,16,17)


def temporal_profile(t,time_radius):
    """Exact compact parent G=t*T and derivative G'=T+tT'."""
    t=np.asarray(t,dtype=float)
    if not math.isfinite(float(time_radius)) or time_radius<=0:
        raise ValueError('positive time radius required')
    q=1-(t/time_radius)**2
    T=q**4
    Tp=-8*t/time_radius**2*q**3
    G=t*T
    Gp=T+t*Tp
    return T,Tp,G,Gp


def integrable_sector(*,scale,scale_rate,lapse,planck,amp,extra,t,r,
                      time_radius,radial_radius,k=1.7):
    """Nonlinear native/common ADM EH metric with actual compact velocities.

    amp=(Phi,U,psi,E) on T(t)F(r). extra=(psi,E) on G(t)F(r).
    Both old+extra perturbations modify spatial geometry, R3, HR, dust,
    shift and ADM Kr,Kt; no truncated kinetic-only variation.
    """
    x=np.asarray(amp,float);v=np.asarray(extra,float)
    if x.shape!=(4,) or v.shape!=(2,) or not np.all(np.isfinite(x)) or not np.all(np.isfinite(v)):
        raise ValueError('four old and two compact extra finite metric amplitudes required')
    if not math.isfinite(float(planck)) or planck<=0 or not math.isfinite(float(k)) or k<=0:
        raise ValueError('positive Planck coefficient and k required')
    t=np.asarray(t,float);r=np.asarray(r,float)
    if np.any(r<=0):raise ValueError('positive radial quadrature support required')
    T,Tp,F,Fr,Frr=profile(t,r,time_radius,radial_radius)
    _,_,G,Gp=temporal_profile(t,time_radius)
    p,u,s,e=x;sv,ev=v
    phi=p*T*F
    U=u*T*r*F;Ur=u*T*(F+r*Fr)
    psi=(s*T+sv*G)*F
    psir=(s*T+sv*G)*Fr
    psirr=(s*T+sv*G)*Frr
    psit=(s*Tp+sv*Gp)*F
    E=(e*T+ev*G)*r*r*F
    Er=(e*T+ev*G)*(2*r*F+r*r*Fr)
    Err=(e*T+ev*G)*(2*F+4*r*Fr+r*r*Frr)
    Et=(e*Tp+ev*Gp)*r*r*F
    qr=1+2*psi-2*k*k*E/3
    qt=1+2*psi+k*k*E/3
    qr_r=2*psir-2*k*k*Er/3
    qt_r=2*psir+k*k*Er/3
    qt_rr=2*psirr+k*k*Err/3
    qr_t=2*psit-2*k*k*Et/3
    qt_t=2*psit+k*k*Et/3
    lapse_sq=1+2*phi+U*U/qr
    if np.any(qr<=0) or np.any(qt<=0) or np.any(lapse_sq<=0):
        raise ValueError('non-Lorentzian metric trial')
    N=lapse*np.sqrt(lapse_sq)
    L=scale*np.sqrt(qr)
    S=scale*r*np.sqrt(qt)
    Z=1+r*qt_r/(2*qt)
    W=np.sqrt(qt/qr)*Z
    Wr=np.sqrt(qt/qr)*((qt_r/qt-qr_r/qr)*Z/2
                  +qt_r/(2*qt)+r*(qt_rr/qt-(qt_r/qt)**2)/2)
    R3=2/S**2*(1-W*W-2*(S/L)*Wr)
    shift=(lapse/scale)*U/qr
    shiftr=(lapse/scale)*(Ur/qr-U*qr_r/(qr*qr))
    Kr=(scale_rate/scale+qr_t/(2*qr)-shiftr-shift*qr_r/(2*qr))/N
    Kt=(scale_rate/scale+qt_t/(2*qt)-shift*(1/r+qt_r/(2*qt)))/N
    eh=.5*planck*N*L*S*S*(R3-4*Kr*Kt-2*Kt*Kt)
    metric=(-lapse**2*(1+2*phi),lapse*scale*U,scale**2*qr)
    area=scale**2*r*r*qt
    return eh,metric,area,R3


@dataclass(frozen=True)
class IntegrableFiveSectorAction:
    contributions:np.ndarray
    total:float
    names:tuple[str,...]=('EH_g','EH_f','HR','dust_g_can','dust_f_can')


def action(amplitudes=None,*,trajectory=None,time_radius=.027,
           radial_radius=.32,quadrature_order=24,betas=BETAS,m2=M2):
    """Same physical 5-sector action with compact parent metric-rate fields."""
    x=np.zeros(18) if amplitudes is None else np.asarray(amplitudes,float)
    if x.shape!=(18,) or not np.all(np.isfinite(x)):
        raise ValueError('18 finite compact-field / dust-rate amplitudes required')
    if type(quadrature_order) is not int or quadrature_order<10 or min(time_radius,radial_radius)<=0:
        raise ValueError('positive compact support and quadrature>=10 required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    if time_radius>bg.width:raise ValueError('time support exceeds on-shell trajectory')
    nodes,weights=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*nodes
    t=ts[:,None];r=radial_radius*(nodes[None,:]+1)/2
    measure=2*math.pi*time_radius*radial_radius*weights[:,None]*weights[None,:]
    bgs=np.asarray([bg.at(float(tt)) for tt in ts])
    a,b,ad,bd,nf=[bgs[:,i,None] for i in (0,1,2,3,4)]
    eg,gm,ga,_=integrable_sector(scale=a,scale_rate=ad,lapse=1.,planck=MG2,
            amp=x[:4],extra=x[14:16],t=t,r=r,time_radius=time_radius,
            radial_radius=radial_radius)
    ef,fm,fa,_=integrable_sector(scale=b,scale_rate=bd,lapse=nf,planck=MF2,
            amp=x[7:11],extra=x[16:18],t=t,r=r,time_radius=time_radius,
            radial_radius=radial_radius)
    N_g,sh_g,vol_g,grr_g=adm_dust_geometry(gm,ga)
    N_f,sh_f,vol_f,grr_f=adm_dust_geometry(fm,fa)
    th_g,thr_g,pg=phase_samples(base_lapse=1.,charge=CG,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[4],p_amp=x[5],rate_amp=x[6])
    th_f,thr_f,pf=phase_samples(base_lapse=nf,charge=CF,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[11],p_amp=x[12],rate_amp=x[13])
    dg=dust_reduced_density(N=N_g,shift=sh_g,r_rr=grr_g,
                            theta_t=th_g,theta_r=thr_g,p=pg)
    df=dust_reduced_density(N=N_f,shift=sh_f,r_rr=grr_f,
                            theta_t=th_f,theta_r=thr_f,p=pf)
    hr=hr_density(gm,fm,ga,fa,m2=m2,betas=betas)
    cs=np.array([float(np.sum(measure*z)) for z in (eg,ef,hr,dg,df)])
    return IntegrableFiveSectorAction(cs,float(cs.sum()))


def first_variations(*,step=2e-5,trajectory=None,quadrature_order=24,**kwargs):
    if not math.isfinite(step) or not 0<step<.001:
        raise ValueError('positive finite first difference step required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    grad=np.zeros(18)
    for i in range(18):
        p=np.zeros(18);p[i]=step
        grad[i]=(action(p,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total
                -action(-p,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total)/(2*step)
    return grad
