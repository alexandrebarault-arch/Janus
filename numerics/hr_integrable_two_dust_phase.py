"""Step32e: integrate both canonical dust clock velocities as compact parent fields.

The original Step32d 18-vector carried two NON-integrable local theta_rate
jets at indices 6 and 13. Here their amplitudes multiply G(t)=t*T(t)
IN THE PHASE ITSELF, so their velocity has the exact derivative G'(t).
The four new metric parent fields of Step32d, all positive EH_g/f, full HR
and BOTH canonical matter Hamiltonians remain otherwise unchanged.

This is a time-integrable *compact Galerkin action* on physically HOMOGENEOUS,
radiation-free on-shell Candidate-C. It is NOT a canonical BD or gauge
constraint reduction and NOT a new nonhomothetic physical solution.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_full_onshell_tadpole import (
    Trajectory, profile, hr_density, BETAS, M2, MG2, MF2, CG, CF
)
from numerics.hr_integrable_metric_time_basis import (
    integrable_sector, temporal_profile, action as old_action, ORDER as OLD_ORDER
)
from numerics.hr_two_dust_common_time_canonical import (
    adm_dust_geometry, dust_reduced_density, analytic_canonical_pair_integrals
)

ORDER = tuple('theta_g_extra_tT' if i==6 else 'theta_f_extra_tT' if i==13
              else x for i,x in enumerate(OLD_ORDER))
PAIR_INDICES = ((5,6),(12,13))


def phase_samples_integrable(*,base_lapse,charge,r,t,time_radius,radial_radius,
                             theta_amp,p_amp,theta_extra):
    """(theta_t,theta_r,p) from ONE compact theta parent in each sector.

    delta theta=[theta_amp*T(t)+theta_extra*G(t)] F(r), G=t*T.
    rho already eliminated in exact positive-momentum dust Hamiltonian.
    """
    if not np.all(np.isfinite([theta_amp,p_amp,theta_extra])):
        raise ValueError('finite dust phase and momentum amplitudes required')
    T,Tp,F,Fr,_=profile(t,r,time_radius,radial_radius)
    _,_,G,Gp=temporal_profile(t,time_radius)
    parent_t=theta_amp*Tp+theta_extra*Gp
    parent=theta_amp*T+theta_extra*G
    return (base_lapse+parent_t*F,
            parent*Fr,
            charge*r*r*(1+p_amp*T*F))


@dataclass(frozen=True)
class FullyIntegrableTrialAction:
    contributions: np.ndarray
    total: float
    names: tuple[str,...]=('EH_g','EH_f','HR','dust_g_can','dust_f_can')


def action(amplitudes=None,*,trajectory=None,time_radius=.027,
           radial_radius=.32,quadrature_order=24,betas=BETAS,m2=M2):
    """One five-sector 18-field common-time action, all jets integrable.

    The phase shapes and their actual derivatives are used consistently
    in BOTH dust Hamiltonians. No constrained physical scalar inference.
    """
    x=np.zeros(18) if amplitudes is None else np.asarray(amplitudes,float)
    if x.shape!=(18,) or not np.all(np.isfinite(x)):
        raise ValueError('exactly 18 finite compact field amplitudes required')
    if (type(quadrature_order) is not int or quadrature_order<10 or
        not all(math.isfinite(z) and z>0 for z in (time_radius,radial_radius))):
        raise ValueError('positive supports and quadrature order >=10 required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    if time_radius>bg.width: raise ValueError('time support exceeds background IVP')
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
    Ng,shg,_,grrg=adm_dust_geometry(gm,ga)
    Nf,shf,_,grrf=adm_dust_geometry(fm,fa)
    thg,thrg,pg=phase_samples_integrable(base_lapse=1.,charge=CG,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[4],p_amp=x[5],theta_extra=x[6])
    thf,thrf,pf=phase_samples_integrable(base_lapse=nf,charge=CF,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[11],p_amp=x[12],theta_extra=x[13])
    dg=dust_reduced_density(N=Ng,shift=shg,r_rr=grrg,
                            theta_t=thg,theta_r=thrg,p=pg)
    df=dust_reduced_density(N=Nf,shift=shf,r_rr=grrf,
                            theta_t=thf,theta_r=thrf,p=pf)
    hr=hr_density(gm,fm,ga,fa,m2=m2,betas=betas)
    pieces=np.asarray([float(np.sum(measure*z)) for z in (eg,ef,hr,dg,df)])
    return FullyIntegrableTrialAction(pieces,float(pieces.sum()))


def first_variations(*,step=2e-5,trajectory=None,quadrature_order=24,**kwargs):
    if not math.isfinite(step) or not 0<step<.001:
        raise ValueError('small positive finite first-variation step required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    out=np.zeros(18)
    for i in range(18):
        e=np.zeros(18);e[i]=step
        out[i]=(action(e,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total
                -action(-e,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total)/(2*step)
    return out


def analytic_integrable_pair_block(*,time_radius=.027,radial_radius=.32,
                                    quadrature_order=24):
    """Off-shell symplectic *projection* onto p_amp*T F, theta_extra*G F.

    Integration by parts, [T G']_{time} = 1/2 [T²]_{time} for G=t*T.
    Therefore each diagonal p--theta_extra coefficient is EXACTLY HALF
    the disconnected theta_rate coefficient in the Step32a profile.
    """
    return .5*analytic_canonical_pair_integrals(time_radius=time_radius,
        radial_radius=radial_radius,quadrature_order=quadrature_order)


def finite_canonical_pair_block(*,step=.01,trajectory=None,quadrature_order=24,**kwargs):
    if not math.isfinite(step) or not 0<step<.1:
        raise ValueError('positive finite pair-difference step required')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    out=np.empty((2,2))
    for i,(p_idx,_) in enumerate(PAIR_INDICES):
        for j,(_,phase_idx) in enumerate(PAIR_INDICES):
            p=np.zeros(18);th=np.zeros(18)
            p[p_idx]=step;th[phase_idx]=step
            out[i,j]=(action(p+th,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total
                     -action(p-th,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total
                     -action(-p+th,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total
                     +action(-p-th,trajectory=bg,quadrature_order=quadrature_order,**kwargs).total)/(4*step*step)
    return out


def phase_integration_by_parts(*,charge,theta_amp,p_amp,theta_extra,
                               time_radius=.027,radial_radius=.32,
                               quadrature_order=28):
    """Two independently computed time-integrated p*theta_dot + theta*p_dot.

    Both use the exact compact parent field and full native time derivative.
    The sum must vanish because theta perturbations vanish on t boundaries.
    """
    nodes,w=np.polynomial.legendre.leggauss(quadrature_order)
    t=time_radius*nodes[:,None]
    r=radial_radius*(nodes[None,:]+1)/2
    T,Tp,F,_,_=profile(t,r,time_radius,radial_radius)
    _,_,G,Gp=temporal_profile(t,time_radius)
    theta=(theta_amp*T+theta_extra*G)*F
    theta_t=(theta_amp*Tp+theta_extra*Gp)*F
    p=charge*r*r*(1+p_amp*T*F)
    pt=charge*r*r*p_amp*Tp*F
    measure=2*math.pi*time_radius*radial_radius*w[:,None]*w[None,:]
    lhs=float(np.sum(measure*p*theta_t))
    rhs=float(-np.sum(measure*theta*pt))
    return lhs,rhs
