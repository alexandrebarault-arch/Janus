"""Exact spherical Stückelberg pullback invariants for two FLRW metrics."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

@dataclass(frozen=True)
class SphericalSquareRootInvariants:
    tr_spherical_block: float
    det_spherical_block: float
    angular_eigenvalue: float
    e: np.ndarray
    det_ginv_f_block: float
    tr_ginv_f_block: float


def spherical_square_root_invariants(*, a: float, r: float, n: float, alpha: float,
                                     T_t: float, T_r: float, R: float, R_t: float, R_r: float) -> SphericalSquareRootInvariants:
    vals=(a,r,n,alpha,T_t,T_r,R,R_t,R_r)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all pullback inputs must be finite")
    if a <= 0 or r <= 0 or n <= 0 or alpha <= 0 or R <= 0:
        raise ValueError("a,r,n,alpha,R must be positive")
    ftt=-n*n*T_t*T_t+alpha*alpha*R_t*R_t
    ftr=-n*n*T_t*T_r+alpha*alpha*R_t*R_r
    frr=-n*n*T_r*T_r+alpha*alpha*R_r*R_r
    A=np.array([[-ftt,-ftr],[ftr/(a*a),frr/(a*a)]],dtype=float)
    detA=float(np.linalg.det(A)); trA=float(np.trace(A))
    if detA <= 0:
        raise ValueError("spherical g^-1 f block must have positive determinant")
    root_det=math.sqrt(detA); rad=trA+2.0*root_det
    if rad <= 0:
        raise ValueError("principal square-root trace radicand must be positive")
    trS=math.sqrt(rad); detS=root_det; ell=alpha*R/(a*r)
    e=np.array([1.0,trS+2*ell,detS+2*ell*trS+ell*ell,
                2*ell*detS+ell*ell*trS,ell*ell*detS],dtype=float)
    return SphericalSquareRootInvariants(trS,detS,ell,e,detA,trA)


def spherical_interaction_density(*, betas, **kwargs) -> float:
    beta=tuple(float(x) for x in betas)
    if len(beta)!=5 or not all(math.isfinite(x) for x in beta):
        raise ValueError("betas must contain five finite coefficients")
    return float(np.dot(np.asarray(beta,dtype=float),spherical_square_root_invariants(**kwargs).e))


def temporal_interaction_branch_factor(*, beta1: float, beta2: float, beta3: float, xi: float, mu: float) -> float:
    vals=(beta1,beta2,beta3,xi,mu)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("branch-factor inputs must be finite")
    if xi <= 0.0 or mu <= -1.0:
        raise ValueError("xi must be positive and mu must exceed -1")
    q=1.0+mu
    return float(beta1+2.0*beta2*xi*q+beta3*xi*xi*q*q)


def temporal_shift_coefficient(*, a: float, H_g: float, c: float, mu: float, mu_dot: float) -> float:
    """Uniform-mode cosmic-time shift chi=(s/2)r^2 on the interaction branch."""
    vals=(a,H_g,c,mu,mu_dot)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("temporal-shift inputs must be finite")
    if a <= 0.0 or c <= 0.0 or mu <= -1.0:
        raise ValueError("a,c must be positive and mu must exceed -1")
    return float(-(a*a/c)*(mu_dot+H_g*mu*(c+1.0+mu)))


def homothetic_early_radial_polynomial_coefficients(*, beta1: float, beta2: float, beta3: float, K: float, w: float) -> np.ndarray:
    """Normalized [mu^2,mu,1] coefficients whose roots are Aoki Eq. (68)."""
    vals=(beta1,beta2,beta3,K,w)
    if not all(math.isfinite(float(v)) for v in vals) or K <= 0.0:
        raise ValueError("homothetic radial inputs must be finite and K positive")
    D=beta1+2.0*K*beta2+K*K*beta3
    if abs(D)<=1e-14*max(1.0,abs(beta1),abs(2*K*beta2),abs(K*K*beta3)):
        raise np.linalg.LinAlgError("homothetic interaction normalization is singular")
    B2=(K*beta2+K*K*beta3)/D; B3=K*K*beta3/D
    return np.asarray([-2.0*B2+(1.0+3.0*w)*B3,
                       6.0*w*B2-2.0*B2-2.0,
                       3.0*(w-1.0)],dtype=float)


def nonhomothetic_adiabatic_radial_polynomial_coefficients(*, beta1: float, beta2: float, beta3: float,
                                                            xi: float, c: float, Hdot_over_H2: float) -> np.ndarray:
    """Raw [mu^2,mu,1] coefficients for non-homothetic adiabatic branches.

    The full leading radial equation has a separate factor ``mu`` for the
    linear branch.  These coefficients describe the two nonlinear branches
    after the temporal Stückelberg constraint is imposed.
    """
    vals=(beta1,beta2,beta3,xi,c,Hdot_over_H2)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("nonhomothetic radial inputs must be finite")
    if xi <= 0.0 or c <= 0.0:
        raise ValueError("xi and c must be positive")
    e=Hdot_over_H2
    A2=xi*(beta2+beta3*xi*(c+e+1.0))
    A1=beta1+beta2*xi*(c+2.0*e+5.0)+beta3*xi*xi*(3.0*c+2.0*e+2.0)
    A0=beta1*(e+3.0)+2.0*beta2*xi*(c+e+2.0)+beta3*xi*xi*(2.0*c+e+1.0)
    return np.asarray([A2,A1,A0],dtype=float)


def _diagonal_interaction_components(*, betas, temporal: float, spatial: float) -> np.ndarray:
    """Mixed-index g/f interaction components for diagonal ``S=(t,x,x,x)``.

    Returned order is ``(Vg_time,Vg_space,Vf_time,Vf_space)``.  The formulas
    are the diagonal Hassan-Rosen ``Y_(n)`` tensors; beta0/beta4 cancel from
    background-subtracted source polynomials below.
    """
    beta=tuple(float(v) for v in betas)
    if len(beta)!=5 or not all(math.isfinite(v) for v in beta):
        raise ValueError("betas must contain five finite coefficients")
    t=float(temporal); x=float(spatial)
    if not (math.isfinite(t) and math.isfinite(x) and t>0.0 and x>0.0):
        raise ValueError("diagonal square-root eigenvalues must be positive and finite")
    b0,b1,b2,b3,b4=beta
    vg_t=b0+3.0*b1*x+3.0*b2*x*x+b3*x**3
    vg_s=b0+b1*(t+2.0*x)+b2*(2.0*t*x+x*x)+b3*t*x*x
    ti=1.0/t; xi=1.0/x
    vf_t=b4+3.0*b3*xi+3.0*b2*xi*xi+b1*xi**3
    vf_s=b4+b3*(ti+2.0*xi)+b2*(2.0*ti*xi+xi*xi)+b1*ti*xi*xi
    return np.asarray([vg_t,vg_s,vf_t,vf_s],dtype=float)


def homothetic_weak_metric_source_polynomials(*, beta1: float, beta2: float, beta3: float,
                                               K: float, mu: float) -> np.ndarray:
    """Signed interaction polynomials in Aoki Eqs. (98)-(101).

    The result multiplies ``(m_g^2,m_g^2,m_f^2,m_f^2)`` respectively and is
    derived from the diagonal Hassan-Rosen interaction tensors rather than by
    hard-coding the published polynomials.
    """
    vals=(beta1,beta2,beta3,K,mu)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("weak-metric source inputs must be finite")
    if K<=0.0 or mu<=-1.0:
        raise ValueError("K must be positive and mu must exceed -1")
    b1=float(beta1); b2=float(beta2); b3=float(beta3); k=float(K); u=float(mu)
    D=b1*k+2.0*b2*k*k+b3*k**3
    scale=max(1.0,abs(b1*k),abs(2.0*b2*k*k),abs(b3*k**3))
    if abs(D)<=1e-14*scale:
        raise np.linalg.LinAlgError("homothetic interaction normalization is singular")
    background=_diagonal_interaction_components(
        betas=(0.0,b1,b2,b3,0.0), temporal=k, spatial=k,
    )
    perturbed=_diagonal_interaction_components(
        betas=(0.0,b1,b2,b3,0.0), temporal=k, spatial=k*(1.0+u),
    )
    dgt,dgs,dft,dfs=perturbed-background
    return np.asarray([
        dgt/(3.0*D),
        dgt/(3.0*D)-dgs/D,
        dft*k**4/(3.0*D),
        (dft/3.0-dfs)*k**4/D,
    ],dtype=float)
