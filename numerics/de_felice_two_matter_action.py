"""Full local scalar quadratic action for ghost-free bigravity with two fluids.

This module combines, in De Felice conventions and without Lagos one-matter
background simplifications:

1. the scalar specialization of De Felice et al. Eq. (44) for each EH sector;
2. the Hassan-Rosen interaction in the De Felice sign convention, with the
   Fourier relative-shift square inserted from Eqs. (45)-(46);
3. one Eq. (54) P(X) matter action for each metric.

The first reduction is performed in g-flat gauge (psi_g=E_g=0). Lapses and
shifts are algebraic auxiliaries and are eliminated by a Schur complement.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.de_felice_gravity_action import eh_scalar_quadratic_density_flat
from numerics.de_felice_matter_action import kessence_scalar_quadratic_density
from numerics.hr_scalar_potential import hr_scalar_quadratic_potential_density_de_felice


FLAT_DYNAMIC_ORDER = ("psi_f", "E_f", "q_g", "q_f")
FLAT_RATE_ORDER = ("psi_f_dot", "E_f_dot", "q_g_dot", "q_f_dot")
AUXILIARY_ORDER = ("Phi_g", "Phi_f", "B_g", "B_f")


@dataclass(frozen=True)
class DFKessenceFluid:
    rho: float
    pressure: float
    cs2: float

    def __post_init__(self):
        vals=(self.rho,self.pressure,self.cs2)
        if not all(math.isfinite(v) for v in vals):
            raise ValueError("fluid parameters must be finite")
        if self.cs2<=0.0:
            raise ValueError("cs2 must be positive before the reduced dust limit")


@dataclass(frozen=True)
class FlatGaugeReducedAction:
    reduced_hessian: np.ndarray
    kinetic_hessian: np.ndarray
    auxiliary_hessian: np.ndarray
    auxiliary_rank: int
    auxiliary_condition_number: float


def _as4(values,name: str)->np.ndarray:
    arr=np.asarray(values,dtype=float)
    if arr.shape!=(4,):
        raise ValueError(f"{name} must have length 4")
    return arr


def _cosmic_background(bg: ScalarBackground,bgp: ScalarBackgroundDerivatives)->dict[str,float]:
    if bg.a<=0.0 or bg.xi<=0.0 or bg.c<=0.0:
        raise ValueError("a, xi and c must be positive")
    a=bg.a; xi=bg.xi; c=bg.c
    alpha=a*xi; N=1.0; n=xi*c
    Hg=bg.H/a
    Hf=bg.H_omega/(a*xi*c)
    Hg_dot_over_N=(bgp.H_prime-bg.H*bg.H)/(a*a)
    log_den_prime=bg.H+bgp.xi_prime/xi+bgp.c_prime/c
    numerator=bgp.H_omega_prime-bg.H_omega*log_den_prime
    Hf_dot_over_n=numerator/(a*a*xi*xi*c*c)
    n_dot_over_n=(bgp.xi_prime/xi+bgp.c_prime/c)/a
    return dict(N=N,a=a,n=n,alpha=alpha,Hg=Hg,Hf=Hf,
                Hg_dot_over_N=Hg_dot_over_N,Hf_dot_over_n=Hf_dot_over_n,
                n_dot_over_n=n_dot_over_n)


def matter_log_phidot_rates(
    bg: ScalarBackground,bgp: ScalarBackgroundDerivatives,*,
    g_fluid: DFKessenceFluid,f_fluid: DFKessenceFluid,
)->tuple[float,float]:
    """Return d ln(phi_dot_0)/dt for the two P(X) backgrounds.

    De Felice Eqs. (17)-(18) give, for u=phi_dot/lapse,
    ``d ln u/dt = -3 lapse H cs2``.  The g-cosmic-time choice has N=1,
    while the f lapse is ``n=xi*c``.
    """
    p=_cosmic_background(bg,bgp)
    rg=-3.0*p["Hg"]*g_fluid.cs2
    rf=p["n_dot_over_n"]-3.0*p["n"]*p["Hf"]*f_fluid.cs2
    return float(rg),float(rf)


def flat_gauge_action_value(
    bg: ScalarBackground,bgp: ScalarBackgroundDerivatives,*,betas,
    g_fluid: DFKessenceFluid,f_fluid: DFKessenceFluid,
    dynamic,rates,auxiliaries,
)->float:
    """Common-normalized quadratic action value in g-flat gauge.

    ``q_g`` and ``q_f`` denote ``delta phi / phi_dot_0``.  Their supplied
    rates are the true time derivatives of q.  Eq. (54), however, contains
    ``delta phi_dot / phi_dot_0``; therefore the background drift of
    ``phi_dot_0`` is added explicitly below.
    """
    q=_as4(dynamic,"dynamic"); v=_as4(rates,"rates"); aux=_as4(auxiliaries,"auxiliaries")
    p=_cosmic_background(bg,bgp)
    psi_f,E_f,q_g,q_f=q
    psi_f_dot,E_f_dot,q_g_dot,q_f_dot=v
    Phi_g,Phi_f,B_g,B_f=aux
    psi_g=E_g=psi_g_dot=E_g_dot=0.0
    k=math.sqrt(bg.k2); a=p["a"]; alpha=p["alpha"]; xi=bg.xi; n=p["n"]
    rg,rf=matter_log_phidot_rates(bg,bgp,g_fluid=g_fluid,f_fluid=f_fluid)
    delta_phidot_ratio_g=q_g_dot+rg*q_g
    delta_phidot_ratio_f=q_f_dot+rf*q_f

    L_eh_g=0.5*eh_scalar_quadratic_density_flat(
        lapse=1.0,scale_factor=a,H=p["Hg"],Hdot_over_lapse=p["Hg_dot_over_N"],k=k,
        Phi=Phi_g,B=B_g,psi=psi_g,E=E_g,psi_dot=psi_g_dot,E_dot=E_g_dot)
    L_eh_f=0.5*bg.kappa*n*xi**3*eh_scalar_quadratic_density_flat(
        lapse=n,scale_factor=alpha,H=p["Hf"],Hdot_over_lapse=p["Hf_dot_over_n"],k=k,
        Phi=Phi_f,B=B_f,psi=psi_f,E=E_f,psi_dot=psi_f_dot,E_dot=E_f_dot)

    L_m_g=kessence_scalar_quadratic_density(
        rho=g_fluid.rho,pressure=g_fluid.pressure,cs2=g_fluid.cs2,
        lapse=1.0,scale_factor=a,k=k,Phi=Phi_g,B=B_g,psi=psi_g,E=E_g,
        delta_phi_over_phidot=q_g,delta_phidot_over_phidot=delta_phidot_ratio_g)
    L_m_f=n*xi**3*kessence_scalar_quadratic_density(
        rho=f_fluid.rho,pressure=f_fluid.pressure,cs2=f_fluid.cs2,
        lapse=n,scale_factor=alpha,k=k,Phi=Phi_f,B=B_f,psi=psi_f,E=E_f,
        delta_phi_over_phidot=q_f,delta_phidot_over_phidot=delta_phidot_ratio_f)

    potential=hr_scalar_quadratic_potential_density_de_felice(
        N=1.0,a=a,n=n,alpha=alpha,m2=bg.m2,Mg2=1.0,betas=betas,k=k,
        Phi_g=Phi_g,B_g=B_g,psi_g=psi_g,E_g=E_g,
        Phi_f=Phi_f,B_f=B_f,psi_f=psi_f,E_f=E_f)/a**3
    return float(L_eh_g+L_eh_f+L_m_g+L_m_f+potential)


def flat_gauge_quadratic_hessian(
    bg: ScalarBackground,bgp: ScalarBackgroundDerivatives,*,betas,
    g_fluid: DFKessenceFluid,f_fluid: DFKessenceFluid,
    finite_difference_step: float=5.0e-5,
)->np.ndarray:
    h=float(finite_difference_step)
    if not (h>0.0 and math.isfinite(h)):
        raise ValueError("finite_difference_step must be finite and positive")
    n=12; zero=np.zeros(n,dtype=float); eye=np.eye(n,dtype=float)*h
    def L(x):
        x=np.asarray(x,dtype=float)
        return flat_gauge_action_value(bg,bgp,betas=betas,g_fluid=g_fluid,f_fluid=f_fluid,
                                      dynamic=x[:4],rates=x[4:8],auxiliaries=x[8:12])
    base=L(zero); H=np.empty((n,n),dtype=float); hh=h*h
    for i in range(n):
        H[i,i]=(L(eye[i])-2.0*base+L(-eye[i]))/hh
        for j in range(i+1,n):
            H[i,j]=H[j,i]=(L(eye[i]+eye[j])-L(eye[i]-eye[j])-L(-eye[i]+eye[j])+L(-eye[i]-eye[j]))/(4.0*hh)
    return H


def eliminate_flat_gauge_auxiliaries(
    bg: ScalarBackground,bgp: ScalarBackgroundDerivatives,*,betas,
    g_fluid: DFKessenceFluid,f_fluid: DFKessenceFluid,
    finite_difference_step: float=5.0e-5,
)->FlatGaugeReducedAction:
    Q=flat_gauge_quadratic_hessian(bg,bgp,betas=betas,g_fluid=g_fluid,f_fluid=f_fluid,
                                  finite_difference_step=finite_difference_step)
    Qzz=Q[:8,:8]; Qza=Q[:8,8:12]; Qaa=Q[8:12,8:12]
    rank=int(np.linalg.matrix_rank(Qaa))
    if rank!=4:
        raise np.linalg.LinAlgError(f"auxiliary Hessian rank {rank}, expected 4")
    reduced=Qzz-Qza@np.linalg.solve(Qaa,Qza.T)
    reduced=0.5*(reduced+reduced.T)
    kinetic=0.5*(reduced[4:8,4:8]+reduced[4:8,4:8].T)
    return FlatGaugeReducedAction(
        reduced_hessian=np.asarray(reduced,dtype=float),
        kinetic_hessian=np.asarray(kinetic,dtype=float),
        auxiliary_hessian=np.asarray(Qaa,dtype=float),
        auxiliary_rank=rank,
        auxiliary_condition_number=float(np.linalg.cond(Qaa)),
    )
