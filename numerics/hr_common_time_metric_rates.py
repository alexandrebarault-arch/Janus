"""Add four INDEPENDENT trace/shear time-rate jets to Step32 2-dust action.

Exact EH extrinsic-curvature correction at unchanged native/common spatial
metric, ADM lapse/shift and HR/dust fields. The 18 amplitudes are
14 Step32 phase-space fields plus (psi_rate_g,E_rate_g,psi_rate_f,E_rate_f).

A rate jet is NOT an independently compactly supported field variation:
its effect on the first variation must be combined with the time derivative
of its parent metric scalar before integrating by parts. This does NOT
eliminate lapse/shift/BD constraints nor yield physical mode velocities.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_full_onshell_tadpole import (
    Trajectory, sector_density, profile, MG2, MF2, BETAS, M2
)
from numerics.hr_two_dust_common_time_canonical import (
    ORDER as ORDER14, action as canonical_action, adm_dust_geometry
)

ORDER=ORDER14+('psi_rate_g','E_rate_g','psi_rate_f','E_rate_f')
RATE_INDICES=(14,15,16,17)


def eh_rate_delta_density(*,scale,scale_rate,background_lapse,planck,
             original_metric_amp,psi_rate,E_rate,t,r,
             time_radius,radial_radius,k=1.7):
    """Difference EH[K_r+deltaK_r,K_t+deltaK_t]-EH[K_r,K_t].

    Spatial R^(3) and metric/lapse/shift are unchanged by independently
    specified derivative jets. This formula is EXACT in the rate jets
    even at finite original spatial/lapse/shift perturbations.
    """
    x=np.asarray(original_metric_amp,float)
    if x.shape!=(4,) or not np.all(np.isfinite(x)):
        raise ValueError('four finite metric perturbation amplitudes required')
    if not all(math.isfinite(float(v)) for v in (psi_rate,E_rate,k,planck)) or min(k,planck)<=0:
        raise ValueError('invalid positive EH rate parameters')
    t=np.asarray(t,float);r=np.asarray(r,float)
    if np.any(r<=0):raise ValueError('positive radial quadrature support required')
    # Reuse the unchanged EXACT Step31 metric and its true ADM variables.
    amp=np.array([*x,0.,0.]);rho0=np.ones_like(np.asarray(scale,float))
    _,_,metric,area,_=sector_density(
        scale=scale,scale_rate=scale_rate,lapse=background_lapse,rho0=rho0,
        amp=amp,t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,
        planck=planck,k=k)
    N,shift,vol,grr=adm_dust_geometry(metric,area)
    T,Tr,F,Fr,Frr=profile(t,r,time_radius,radial_radius)
    p,u,s,e=x
    U=u*T*r*F
    Ur=u*T*(F+r*Fr)
    psi=s*T*F
    psir=s*T*Fr
    E=e*T*r*r*F
    Er=e*T*(2*r*F+r*r*Fr)
    Qr=1+2*psi-2*k*k*E/3
    Qt=1+2*psi+k*k*E/3
    Qrr=2*psir-2*k*k*Er/3
    Qtr=2*psir+k*k*Er/3
    Qrt0=2*s*Tr*F-2*k*k*e*Tr*r*r*F/3
    Qtt0=2*s*Tr*F+k*k*e*Tr*r*r*F/3
    shift_r=(background_lapse/scale)*(Ur/Qr-U*Qrr/(Qr*Qr))
    Kr0=(scale_rate/scale+Qrt0/(2*Qr)-shift_r-shift*Qrr/(2*Qr))/N
    Kt0=(scale_rate/scale+Qtt0/(2*Qt)-shift*(1/r+Qtr/(2*Qt)))/N
    deltaQr_t=2*psi_rate*T*F-(2*k*k/3)*E_rate*T*r*r*F
    deltaQt_t=2*psi_rate*T*F+(k*k/3)*E_rate*T*r*r*F
    deltaKr=deltaQr_t/(2*Qr*N)
    deltaKt=deltaQt_t/(2*Qt*N)
    return .5*planck*N*vol*(-4*(Kr0*deltaKt+deltaKr*Kt0+deltaKr*deltaKt)
                               -4*Kt0*deltaKt-2*deltaKt*deltaKt)


@dataclass(frozen=True)
class EighteenJetAction:
    contributions:np.ndarray
    total:float
    names:tuple[str,...]=('EH_g','EH_f','HR','dust_g','dust_f')


def action(amplitudes=None,*,trajectory=None,time_radius=.027,
          radial_radius=.32,quadrature_order=24,betas=BETAS,m2=M2):
    """Real five-sector common action with 14 old fields + 4 EH rates."""
    if amplitudes is None:amplitudes=np.zeros(18)
    x=np.asarray(amplitudes,float)
    if x.shape!=(18,) or not np.all(np.isfinite(x)):
        raise ValueError('18 independent finite field/rate jet amplitudes required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    old=canonical_action(x[:14],trajectory=bg,time_radius=time_radius,
                   radial_radius=radial_radius,quadrature_order=quadrature_order,
                   betas=betas,m2=m2)
    nodes,weights=np.polynomial.legendre.leggauss(quadrature_order)
    t=(time_radius*nodes)[:,None]
    r=(radial_radius*(nodes+1)/2)[None,:]
    measure=2*math.pi*time_radius*radial_radius*weights[:,None]*weights[None,:]
    bgs=np.asarray([bg.at(float(tt)) for tt in time_radius*nodes])
    a,b,ad,bd,nf=[bgs[:,i,None] for i in range(5)]
    dg=eh_rate_delta_density(scale=a,scale_rate=ad,background_lapse=1.,
         planck=MG2,original_metric_amp=x[:4],psi_rate=x[14],E_rate=x[15],
         t=t,r=r,time_radius=time_radius,radial_radius=radial_radius)
    df=eh_rate_delta_density(scale=b,scale_rate=bd,background_lapse=nf,
         planck=MF2,original_metric_amp=x[7:11],psi_rate=x[16],E_rate=x[17],
         t=t,r=r,time_radius=time_radius,radial_radius=radial_radius)
    pieces=old.contributions.copy()
    pieces[0]+=np.sum(measure*dg)
    pieces[1]+=np.sum(measure*df)
    return EighteenJetAction(pieces,float(pieces.sum()))


def extra_rate_hessian(*,step=.002,trajectory=None,**kwargs):
    """4x4 gravitational rate-rate block, NOT constrained physical kinetic."""
    if not math.isfinite(step) or step<=0:raise ValueError('positive difference step')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    def fun(v):return action(v,trajectory=bg,**kwargs).total
    zero=np.zeros(18);f0=fun(zero)
    H=np.zeros((4,4))
    for i in range(4):
        ei=np.zeros(18);ei[14+i]=step
        H[i,i]=(fun(ei)+fun(-ei)-2*f0)/(step*step)
        for j in range(i+1,4):
            ej=np.zeros(18);ej[14+j]=step
            H[i,j]=H[j,i]=(fun(ei+ej)-fun(ei-ej)-fun(-ei+ej)+fun(-ei-ej))/(4*step*step)
    return H


def analytic_background_rate_hessian(*,time_radius=.027,radial_radius=.32,
                                     quadrature_order=24,trajectory=None,k=1.7):
    """Independent flat isotropic EH trace/shear rate-rate quadratic oracle.

    For the two native EH pieces with M²/2 overall coefficient:
    H[psi_rate,psi_rate] = -6 M²∫4π dt dr a³r²(TF)²/n;
    H[E_rate,E_rate] = M²k⁴/6∫4π dt dr a³r²(T r² F)²/n;
    H[psi_rate,E_rate]=0.
    """
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    nodes,w=np.polynomial.legendre.leggauss(quadrature_order)
    t=(time_radius*nodes)[:,None];r=(radial_radius*(nodes+1)/2)[None,:]
    factor=2*math.pi*time_radius*radial_radius*w[:,None]*w[None,:]
    T,_,F,_,_=profile(t,r,time_radius,radial_radius)
    bgs=np.asarray([bg.at(float(v)) for v in time_radius*nodes])
    a,b,nf=[bgs[:,i,None] for i in (0,1,4)]
    H=np.zeros((4,4))
    for j,(scale,N,P) in enumerate(((a,1.,MG2),(b,nf,MF2))):
        weight=factor*P*scale**3*r*r/N
        H[2*j,2*j]=float(np.sum(weight*(-6)*(T*F)**2))
        H[2*j+1,2*j+1]=float(np.sum(weight*(k**4/6)*(T*r*r*F)**2))
    return H
