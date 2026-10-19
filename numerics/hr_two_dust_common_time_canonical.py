"""Exact common-time two-dust canonical bridge to Step31 on-shell EH+HR.

THIS IS A PRECONSTRAINT PHASE-SPACE TRIAL JET, NOT a reduced BD / ghost
result.  The original irrotational dust multiplier is Legendre-transformed
before applying proper-time normalization; two positive canonical momenta
stay independent. Full EH and HR metrics are reused without changing any
spatial scalar profile or radial/time integration.

14 amplitude order, per sector (Phi, U, psi, E, theta, p, theta_rate).
The extra theta_rate is a local *independent jet*; for a globally compact
field variation theta_rate must equal the prescribed time derivative of
its theta profile. It must not be treated as a new dynamical field.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_full_onshell_tadpole import (
    Trajectory, sector_density, hr_density, profile, BETAS, M2, MG2, MF2, CG, CF
)

ORDER=('Phi_g','U_g','psi_g','E_g','theta_g','p_g','theta_rate_g',
       'Phi_f','U_f','psi_f','E_f','theta_f','p_f','theta_rate_f')
PAIR_INDICES=((5,6),(12,13))  # canonical H[p_i, theta_rate_j]


def adm_dust_geometry(metric, area):
    """Spherical common-time ADM variables per unit angular solid angle."""
    g00,g01,g11=metric
    if np.any(g11<=0) or np.any(area<=0):
        raise ValueError('positive spatial metric required')
    N2=-g00+g01*g01/g11
    if np.any(N2<=0):raise ValueError('Lorentzian lapse required')
    N=np.sqrt(N2)
    shift=g01/g11
    rootgamma=np.sqrt(g11)*area
    return N,shift,rootgamma,g11


def dust_legendre_density(*,N,shift,rootgamma,g_rr,rho,theta_t,theta_r,p):
    """Exact first-order dust phase density at arbitrary positive rho.

    L_cov = (sqrtgamma*rho)/(2N) [(theta_t-N^r theta_r)^2
                  - N^2(1+theta_r^2/g_rr)].
    P = sqrtgamma rho (theta_t-N^r theta_r)/N.
    H(rho) = N[P^2/(2sqrtgamma rho)+sqrtgamma rho(1+theta_r²/g_rr)/2]
                + N^r P theta_r.
    Returns (covariant, canonical, Legendre momentum, rho-stationary value).
    """
    if np.any(N<=0) or np.any(rootgamma<=0) or np.any(rho<=0) or np.any(g_rr<=0):
        raise ValueError('positive lapse, volume, rho and radial metric required')
    speed=theta_t-shift*theta_r
    q=1+theta_r**2/g_rr
    calculated=rootgamma*rho*speed/N
    cov=.5*rootgamma*rho*(speed*speed/N-N*q)
    ham=N*(p*p/(2*rootgamma*rho)+.5*rootgamma*rho*q)+shift*p*theta_r
    canonical=p*theta_t-ham
    stationary=p/(rootgamma*np.sqrt(q))
    return cov,canonical,calculated,stationary


def dust_reduced_density(*,N,shift,r_rr,theta_t,theta_r,p):
    """After stationary multiplier elimination; p must remain positive."""
    if np.any(N<=0) or np.any(r_rr<=0) or np.any(p<=0):
        raise ValueError('positive lapse, radial metric and dust momentum required')
    return p*(theta_t-N*np.sqrt(1+theta_r*theta_r/r_rr)-shift*theta_r)


def phase_samples(*,base_lapse,charge,r,t,time_radius,radial_radius,
                  theta_amp,p_amp,rate_amp):
    T,Tr,F,Fr,_=profile(t,r,time_radius,radial_radius)
    shape=T*F
    return (base_lapse+theta_amp*Tr*F+rate_amp*shape,
            theta_amp*T*Fr,
            charge*r*r*(1+p_amp*shape))


@dataclass(frozen=True)
class CanonicalAction:
    contributions: np.ndarray
    total: float
    names: tuple[str,...]=('EH_g','EH_f','HR','dust_g_can','dust_f_can')


def action(amplitudes=None, *, trajectory=None,time_radius=.027,
           radial_radius=.32,quadrature_order=24,betas=BETAS,m2=M2):
    """Real full EH+HR unchanged, two dusts in positive-p Hamiltonian form.

    Momenta p_g,p_f are common-time scalar DENSITIES per angular volume;
    their background values CG*r² and CF*r² do not include an extra 4pi.
    Both metric lapse/shift sources and spatial curvature from Step31
    are identical; phase velocities vary independently as local jets.
    """
    if amplitudes is None:amplitudes=np.zeros(14)
    x=np.asarray(amplitudes,dtype=float)
    if x.shape!=(14,) or not np.all(np.isfinite(x)):
        raise ValueError('14 finite canonical trial amplitudes required')
    if type(quadrature_order)!=int or quadrature_order<10 or not math.isfinite(time_radius) or not math.isfinite(radial_radius) or min(time_radius,radial_radius)<=0:
        raise ValueError('positive support, quadrature>=10')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    if time_radius>bg.width:raise ValueError('time support exceeds on-shell background')
    nodes,weights=np.polynomial.legendre.leggauss(quadrature_order)
    ts=time_radius*nodes
    t=ts[:,None];r=radial_radius*(nodes[None,:]+1)/2
    measure=2*math.pi*time_radius*radial_radius*weights[:,None]*weights[None,:]
    bgs=np.asarray([bg.at(float(tt)) for tt in ts])
    a,b,ad,bd,nf,rhog,rhof=[bgs[:,i,None] for i in range(7)]
    g6=np.array([*x[:5],0.]); f6=np.array([*x[7:12],0.])
    eg,_,gm,ga,_=sector_density(scale=a,scale_rate=ad,lapse=1.,rho0=rhog,
        amp=g6,t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MG2)
    ef,_,fm,fa,_=sector_density(scale=b,scale_rate=bd,lapse=nf,rho0=rhof,
        amp=f6,t=t,r=r,time_radius=time_radius,radial_radius=radial_radius,planck=MF2)
    N_g,shift_g,vol_g,grr_g=adm_dust_geometry(gm,ga)
    N_f,shift_f,vol_f,grr_f=adm_dust_geometry(fm,fa)
    thtg,thrg,pg=phase_samples(base_lapse=1.,charge=CG,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[4],p_amp=x[5],rate_amp=x[6])
    thtf,thrf,pf=phase_samples(base_lapse=nf,charge=CF,r=r,t=t,
        time_radius=time_radius,radial_radius=radial_radius,
        theta_amp=x[11],p_amp=x[12],rate_amp=x[13])
    dg=dust_reduced_density(N=N_g,shift=shift_g,r_rr=grr_g,
                            theta_t=thtg,theta_r=thrg,p=pg)
    df=dust_reduced_density(N=N_f,shift=shift_f,r_rr=grr_f,
                            theta_t=thtf,theta_r=thrf,p=pf)
    hr=hr_density(gm,fm,ga,fa,m2=m2,betas=betas)
    pieces=np.array([np.sum(measure*z) for z in (eg,ef,hr,dg,df)])
    return CanonicalAction(pieces,float(np.sum(pieces)))


def derivative(i,*,step=1e-5,**kwargs):
    if type(i)!=int or i not in range(14) or not math.isfinite(step) or step<=0:
        raise ValueError('bad canonical amplitude/step')
    v=np.zeros(14);v[i]=step
    return (action(v,**kwargs).total-action(-v,**kwargs).total)/(2*step)


def kinetic_pair_block(*,step=2e-4,**kwargs):
    """2x2 p--theta_rate Hessian, ONLY symplectic preconstraint interface.

    This is deliberately NOT the physical kinetic matrix of propagating
    scalar modes. Metric auxiliaries and BD mode are not eliminated.
    """
    if not math.isfinite(step) or step<=0:raise ValueError('positive step')
    H=np.zeros((2,2))
    for i,(pi,_) in enumerate(PAIR_INDICES):
        for j,(_,ri) in enumerate(PAIR_INDICES):
            ep=np.zeros(14);er=np.zeros(14)
            ep[pi]=step;er[ri]=step
            H[i,j]=(action(ep+er,**kwargs).total-action(ep-er,**kwargs).total
                    -action(-ep+er,**kwargs).total+action(-ep-er,**kwargs).total)/(4*step*step)
    return H


def analytic_canonical_pair_integrals(*,time_radius=.027,radial_radius=.32,quadrature_order=24):
    """Known kinematical p--phase-rate coefficient 4pi C int dt dr r²(TF)²."""
    nodes,w=np.polynomial.legendre.leggauss(quadrature_order)
    t=time_radius*nodes[:,None]
    r=radial_radius*(nodes[None,:]+1)/2
    q,_,F,_,_=profile(t,r,time_radius,radial_radius)
    measure=2*math.pi*time_radius*radial_radius*w[:,None]*w[None,:]
    shared=float(np.sum(measure*r*r*(q*F)**2))
    return np.diag([CG*shared,CF*shared])


def full_preconstraint_hessian(*,step=.004,trajectory=None,**kwargs):
    """Complete 14x14 compact space-time quadratic H BEFORE constraints.

    Only 12 scalar/phase/momentum perturbations are legal compact fields;
    two independent rate jets are included solely to expose the two
    Hamiltonian p theta_dot coefficients. It is NOT a physical speed,
    gauge rank, or BD ghost matrix, nor the full metric-velocity operator.
    """
    if not math.isfinite(step) or step<=0:
        raise ValueError('positive Hessian difference step')
    bg=trajectory if trajectory is not None else Trajectory.solve(width=.04)
    def fun(v):return action(v,trajectory=bg,**kwargs).total
    z=np.zeros(14);f0=fun(z)
    H=np.zeros((14,14))
    for i in range(14):
        e=np.zeros(14);e[i]=step
        H[i,i]=(fun(e)-2*f0+fun(-e))/(step*step)
        for j in range(i+1,14):
            d=np.zeros(14);d[j]=step
            H[i,j]=H[j,i]=(fun(e+d)-fun(e-d)-fun(-e+d)+fun(-e-d))/(4*step*step)
    return H
