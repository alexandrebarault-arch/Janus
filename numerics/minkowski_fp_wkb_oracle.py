"""Phase-averaged WKB Fierz-Pauli scalar oracle in spherical coordinates.

This audit helper keeps two Fourier quadratures for each weak metric potential,
Schur-eliminates those eight metric amplitudes at fixed (omega,k), and checks
that the reduced helicity-0 action approaches the Minkowski light cone.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.spherical_eh_compact_action import eh_radial_density


@dataclass(frozen=True)
class FierzPauliLightConeScan:
    speeds: np.ndarray
    reduced_coefficients: np.ndarray
    metric_condition_numbers: np.ndarray
    minimum_speed: float
    minimum_value: float


def _wave_pair(a_cos: float, a_sin: float, theta: float, omega: float, k: float):
    c=math.cos(theta); s=math.sin(theta)
    value=a_cos*c+a_sin*s
    dt=omega*(a_cos*s-a_sin*c)
    dr=k*(-a_cos*s+a_sin*c)
    dtt=-omega*omega*value
    drr=-k*k*value
    return value,dt,dr,dtt,drr


def _phase_averaged_action(x, *, omega: float, k: float, r0: float,
                           interaction_mass2: float, nphase: int) -> float:
    p=float(x[0])
    pg=np.asarray(x[1:3],float); sg=np.asarray(x[3:5],float)
    pf=np.asarray(x[5:7],float); sf=np.asarray(x[7:9],float)
    betas=(-3.0,1.0,0.0,0.0,-1.0)
    total=0.0
    for q in range(nphase):
        theta=2.0*math.pi*(q+0.5)/nphase
        ct=math.cos(theta); st=math.sin(theta)
        # Normalize pi so that its second derivatives remain O(p) as k changes.
        pi=p*ct/(k*k)
        pi_t=p*omega*st/(k*k)
        pi_r=-p*st/k
        pi_tt=-p*omega*omega*ct/(k*k)
        pi_rr=-p*ct
        pi_tr=p*omega*ct/k
        del pi

        delta_eta=-pi_t
        delta_r=pi_r
        delta_eta_t=-pi_tt
        delta_eta_r=-pi_tr
        delta_r_t=pi_tr
        delta_r_r=pi_rr

        theta_g=theta+k*delta_r-omega*delta_eta
        phig,phig_t,phig_r,_,phig_rr=_wave_pair(pg[0],pg[1],theta_g,omega,k)
        psig,psig_t,psig_r,psig_tt,_=_wave_pair(sg[0],sg[1],theta_g,omega,k)
        Jg=np.array([[1.0+delta_eta_t,delta_eta_r],
                     [delta_r_t,1.0+delta_r_r]],dtype=float)
        g_native=np.diag([-math.exp(2.0*phig),math.exp(2.0*psig)])
        g_common=Jg.T@g_native@Jg
        rg=r0+delta_r
        if rg<=0.0:
            raise ValueError("g radial chart left positive branch")
        g_ang=rg*rg

        phif,phif_t,phif_r,_,phif_rr=_wave_pair(pf[0],pf[1],theta,omega,k)
        psif,psif_t,psif_r,psif_tt,_=_wave_pair(sf[0],sf[1],theta,omega,k)
        f_common=np.diag([-math.exp(2.0*phif),math.exp(2.0*psif)])
        f_ang=r0*r0

        A=np.linalg.solve(g_common,f_common)
        detA=float(np.linalg.det(A)); trA=float(np.trace(A))
        if detA<=0.0:
            raise ValueError("g^-1 f left principal real branch")
        sd=math.sqrt(detA); den=trA+2.0*sd
        if den<=0.0:
            raise ValueError("principal radial square root became non-real")
        S=(A+sd*np.eye(2))/math.sqrt(den)
        trS=float(np.trace(S)); detS=float(np.linalg.det(S))
        ell=math.sqrt(f_ang/g_ang)
        e=(1.0,
           trS+2.0*ell,
           detS+2.0*ell*trS+ell*ell,
           2.0*ell*detS+ell*ell*trS,
           ell*ell*detS)
        hr=math.sqrt(-float(np.linalg.det(g_common)))*g_ang*sum(b*en for b,en in zip(betas,e))

        eg=eh_radial_density(a=1.0,ap=0.0,app=0.0,r=r0,
            phi=phig,phi_t=phig_t,phi_r=phig_r,phi_rr=phig_rr,
            psi=psig,psi_t=psig_t,psi_tt=psig_tt,psi_r=psig_r)
        ef=eh_radial_density(a=1.0,ap=0.0,app=0.0,r=r0,
            phi=phif,phi_t=phif_t,phi_r=phif_r,phi_rr=phif_rr,
            psi=psif,psi_t=psif_t,psi_tt=psif_tt,psi_r=psif_r)
        total += -interaction_mass2*hr + 0.5*eg + 0.5*ef
    return float(total/nphase)


def _hessian(*, omega: float, k: float, r0: float, interaction_mass2: float,
             amplitude_step: float, nphase: int) -> np.ndarray:
    h=float(amplitude_step); n=9
    zero=np.zeros(n,float)
    kwargs=dict(omega=omega,k=k,r0=r0,interaction_mass2=interaction_mass2,nphase=nphase)
    f0=_phase_averaged_action(zero,**kwargs)
    H=np.zeros((n,n),float)
    for i in range(n):
        ei=np.zeros(n); ei[i]=h
        fp=_phase_averaged_action(ei,**kwargs); fm=_phase_averaged_action(-ei,**kwargs)
        H[i,i]=(fp-2.0*f0+fm)/(h*h)
        for j in range(i+1,n):
            ej=np.zeros(n); ej[j]=h
            H[i,j]=H[j,i]=(
                _phase_averaged_action(ei+ej,**kwargs)
                -_phase_averaged_action(ei-ej,**kwargs)
                -_phase_averaged_action(-ei+ej,**kwargs)
                +_phase_averaged_action(-ei-ej,**kwargs)
            )/(4.0*h*h)
    return H


def scan_fierz_pauli_light_cone(*, k: float, kr0: float, speeds,
                                 interaction_mass2: float=0.2,
                                 amplitude_step: float=2e-4,
                                 nphase: int=12) -> FierzPauliLightConeScan:
    vals=(k,kr0,interaction_mass2,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("inputs must be finite")
    if k<=0.0 or kr0<=0.0 or interaction_mass2<=0.0 or amplitude_step<=0.0:
        raise ValueError("k, kr0, mass squared and amplitude step must be positive")
    speeds=np.asarray(tuple(float(s) for s in speeds),float)
    if speeds.ndim!=1 or speeds.size<3 or not np.all(np.isfinite(speeds)) or np.any(speeds<=0.0):
        raise ValueError("speeds must contain at least three positive finite values")
    if nphase<8:
        raise ValueError("nphase must be at least eight")
    r0=kr0/k
    reduced=[]; cond=[]
    for speed in speeds:
        H=_hessian(omega=float(speed*k),k=float(k),r0=float(r0),
                   interaction_mass2=float(interaction_mass2),
                   amplitude_step=float(amplitude_step),nphase=int(nphase))
        Hmm=H[1:,1:]
        coupling=H[0,1:]
        if np.linalg.matrix_rank(Hmm)<8:
            raise np.linalg.LinAlgError("metric WKB block is rank deficient")
        reduced.append(float(H[0,0]-coupling@np.linalg.solve(Hmm,coupling)))
        cond.append(float(np.linalg.cond(Hmm)))
    reduced=np.asarray(reduced,float); cond=np.asarray(cond,float)
    coeff=np.polyfit(speeds,reduced,2)
    if coeff[0]<=0.0:
        raise np.linalg.LinAlgError("reduced WKB scan has no local convex light-cone minimum")
    minimum_speed=float(-coeff[1]/(2.0*coeff[0]))
    minimum_value=float(np.polyval(coeff,minimum_speed))
    return FierzPauliLightConeScan(
        speeds=speeds,reduced_coefficients=reduced,
        metric_condition_numbers=cond,
        minimum_speed=minimum_speed,minimum_value=minimum_value,
    )
