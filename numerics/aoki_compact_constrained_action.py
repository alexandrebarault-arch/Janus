"""Single-profile compact Galerkin reduction of Aoki's homothetic scalar sector.

This is an audit bridge between the already validated compact HR Stückelberg
action and the full six-field calculation.  It adds compact Einstein-Hilbert
quadratic blocks for the four weak metric potentials and eliminates those
four amplitudes by a Schur complement.  The common-profile ansatz is not yet
a production finite-mass solver; its first acceptance test is the controlled
weak-interaction limit, where it must reduce to the HR-only compact oracle.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.aoki_compact_action_oracle import _profiles, _profile_integrals
from numerics.aoki_compact_eh_metric_action import compact_eh_metric_hessian


@dataclass(frozen=True)
class ConstrainedCompactCoefficients:
    kinetic_hessian_coefficient: float
    gradient_hessian_coefficient: float
    sound_speed_squared: float
    fit_residual: float
    max_metric_condition: float


def _profile_value(t, r, T, R):
    t=np.asarray(t,dtype=float); r=np.asarray(r,dtype=float)
    x=t/T
    A=(1.0-x*x)**3
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    mask=(np.abs(t) <= T) & (r >= 0.0) & (r <= R)
    return np.where(mask,A*F,0.0)


def _interaction_action(amps, *, hubble, beta1, beta2, beta3, K, w, mu, T, R, order):
    pi_amp, phig_amp, psig_amp, phif_amp, psif_amp=[float(v) for v in amps]
    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    t=T*xt[:,None]+np.zeros((1,order))
    r=0.5*R*(xr[None,:]+1.0)+np.zeros((order,1))
    weights=(T*wt[:,None])*(0.5*R*wr[None,:])

    A,At,Att,F,Fr,Frr=_profiles(t,r,T,R)
    C=mu/(1.0+mu); M=mu*(2.0+mu); p=2.0/(1.0+3.0*w)
    base=1.0+hubble*t/p
    if np.any(base <= 0.0):
        raise ValueError("compact domain crossed FLRW conformal-time singularity")
    Hc=hubble/base
    Hcp=-0.5*(1.0+3.0*w)*Hc*Hc
    abase=base**p
    inv_a2=abase**-2

    P=pi_amp*At*F; Q=pi_amp*A*Fr
    Pt=pi_amp*Att*F; Pr=pi_amp*At*Fr; Qt=Pr; Qr=pi_amp*A*Frr
    deta=inv_a2*(-P+r*Hc*C*Q)
    drad=inv_a2*(Q/(1.0+mu)+r*Hc*C*P)
    inv_a2_t=-2.0*Hc*inv_a2
    deta_t=inv_a2_t*(-P+r*Hc*C*Q)+inv_a2*(-Pt+r*C*(Hcp*Q+Hc*Qt))
    deta_r=inv_a2*(-Pr+C*Hc*(Q+r*Qr))
    drad_t=inv_a2_t*(Q/(1.0+mu)+r*Hc*C*P)+inv_a2*(Qt/(1.0+mu)+r*C*(Hcp*P+Hc*Pt))
    drad_r=inv_a2*(Qr/(1.0+mu)+C*Hc*(P+r*Pr))

    eta_g=t+deta; r_g=r+drad
    base_g=1.0+hubble*eta_g/p
    if np.any(base_g <= 0.0):
        raise ValueError("g pullback left the FLRW chart")
    a_g=base_g**p
    pg=_profile_value(eta_g,r_g,T,R)
    phi_g=phig_amp*pg; psi_g=psig_amp*pg
    eg0=np.exp(2.0*phi_g); eg1=np.exp(2.0*psi_g)
    j00=1.0+deta_t; j01=deta_r; j10=drad_t; j11=1.0+drad_r
    g00=a_g*a_g*(-eg0*j00*j00+eg1*j10*j10)
    g01=a_g*a_g*(-eg0*j00*j01+eg1*j10*j11)
    g11=a_g*a_g*(-eg0*j01*j01+eg1*j11*j11)
    det_g2=g00*g11-g01*g01
    gi00=g11/det_g2; gi01=-g01/det_g2; gi11=g00/det_g2

    eta_f=t-0.5*Hc*r*r*M
    eta_f_t=1.0-0.5*Hcp*r*r*M
    eta_f_r=-Hc*r*M
    r_f=(1.0+mu)*r
    base_f=1.0+hubble*eta_f/p
    if np.any(base_f <= 0.0):
        raise ValueError("f pullback left the FLRW chart")
    a_f=base_f**p
    pf=_profile_value(eta_f,r_f,T,R)
    phi_f=phif_amp*pf; psi_f=psif_amp*pf
    ef0=np.exp(2.0*phi_f); ef1=np.exp(2.0*psi_f)
    fk=(K*a_f)**2
    f00=fk*(-ef0*eta_f_t*eta_f_t)
    f01=fk*(-ef0*eta_f_t*eta_f_r)
    f11=fk*(-ef0*eta_f_r*eta_f_r+ef1*(1.0+mu)**2)

    A00=gi00*f00+gi01*f01; A01=gi00*f01+gi01*f11
    A10=gi01*f00+gi11*f01; A11=gi01*f01+gi11*f11
    det_A=A00*A11-A01*A10; tr_A=A00+A11
    if np.any(det_A <= 0.0):
        raise ValueError("radial square root left real branch")
    root_det=np.sqrt(det_A)
    den=tr_A+2.0*root_det
    if np.any(den <= 0.0):
        raise ValueError("principal radial square root left real branch")
    tr_S=np.sqrt(den)
    ell=K*a_f*r_f/(a_g*r_g)
    e1=tr_S+2.0*ell
    e2=root_det+2.0*ell*tr_S+ell*ell
    e3=2.0*ell*root_det+ell*ell*tr_S
    potential=beta1*e1+beta2*e2+beta3*e3
    det_J=j00*j11-j01*j10
    sqrt_minus_g=a_g**4*np.exp(phi_g+psi_g)*det_J*r_g*r_g
    return float(np.sum(weights*sqrt_minus_g*potential))


def _interaction_hessian(*, amplitude_step, **kwargs):
    h=float(amplitude_step)
    z=np.zeros(5,dtype=float)
    f0=_interaction_action(z,**kwargs)
    H=np.empty((5,5),dtype=float)
    for i in range(5):
        ep=np.zeros(5); ep[i]=h
        H[i,i]=(_interaction_action(ep,**kwargs)-2.0*f0+_interaction_action(-ep,**kwargs))/(h*h)
    for i in range(5):
        for j in range(i+1,5):
            epp=np.zeros(5); epp[i]=h; epp[j]=h
            epm=np.zeros(5); epm[i]=h; epm[j]=-h
            emp=-epm; emm=-epp
            H[i,j]=H[j,i]=(
                _interaction_action(epp,**kwargs)-_interaction_action(epm,**kwargs)
                -_interaction_action(emp,**kwargs)+_interaction_action(emm,**kwargs)
            )/(4.0*h*h)
    return H


def _effective_pi_hessian(*, interaction_strength, planck_ratio, amplitude_step, **kwargs):
    lam=float(interaction_strength)
    if lam <= 0.0:
        raise ValueError("interaction_strength must be positive")
    K=float(kwargs["K"])
    Hint=_interaction_hessian(amplitude_step=amplitude_step,**kwargs)
    Heh=compact_eh_metric_hessian(
        hubble=kwargs["hubble"],w=kwargs["w"],T=kwargs["T"],R=kwargs["R"],
        amplitude_step=amplitude_step,quadrature_order=kwargs["order"],
    )
    H=lam*Hint
    H[1:3,1:3] += 0.5*Heh
    H[3:5,3:5] += 0.5*float(planck_ratio)*K*K*Heh
    Hmm=H[1:,1:]
    cond=float(np.linalg.cond(Hmm))
    eff=float(H[0,0]-H[0,1:]@np.linalg.solve(Hmm,H[1:,0]))
    return eff/lam, cond


def recover_constrained_pi_coefficients(
    *, beta1, beta2, beta3, K, w, mu,
    interaction_strength: float, planck_ratio: float,
    time_scales=(0.5,1.0,2.0), radius=1.0,
    hubble_step=0.007, amplitude_step=8e-4, quadrature_order=22,
):
    vals=(beta1,beta2,beta3,K,w,mu,interaction_strength,planck_ratio,radius,hubble_step,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all inputs must be finite")
    if K <= 0.0 or mu <= -1.0 or interaction_strength <= 0.0 or planck_ratio <= 0.0:
        raise ValueError("K, interaction strength and planck ratio must be positive and mu>-1")
    rows=[]; rhs=[]; conds=[]
    for T in time_scales:
        common=dict(beta1=beta1,beta2=beta2,beta3=beta3,K=K,w=w,mu=mu,T=float(T),R=float(radius),order=int(quadrature_order))
        hp,cp=_effective_pi_hessian(hubble=hubble_step,interaction_strength=interaction_strength,planck_ratio=planck_ratio,amplitude_step=amplitude_step,**common)
        hm,cm=_effective_pi_hessian(hubble=-hubble_step,interaction_strength=interaction_strength,planck_ratio=planck_ratio,amplitude_step=amplitude_step,**common)
        h0,c0=_effective_pi_hessian(hubble=0.0,interaction_strength=interaction_strength,planck_ratio=planck_ratio,amplitude_step=amplitude_step,**common)
        h2=(hp+hm-2.0*h0)/(2.0*hubble_step*hubble_step)
        ik,ig=_profile_integrals(float(T),float(radius),int(quadrature_order))
        rows.append((ik,ig)); rhs.append(h2); conds.extend((cp,cm,c0))
    X=np.asarray(rows,dtype=float); y=np.asarray(rhs,dtype=float)
    coeff,_,rank,_=np.linalg.lstsq(X,y,rcond=None)
    if rank != 2 or abs(coeff[0]) < 1e-14:
        raise np.linalg.LinAlgError("compact constrained fit is rank deficient")
    residual=float(np.linalg.norm(X@coeff-y)/max(1.0,np.linalg.norm(y)))
    return ConstrainedCompactCoefficients(
        kinetic_hessian_coefficient=float(coeff[0]),
        gradient_hessian_coefficient=float(coeff[1]),
        sound_speed_squared=float(-coeff[1]/coeff[0]),
        fit_residual=residual,
        max_metric_condition=float(max(conds)),
    )
