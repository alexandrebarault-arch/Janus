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


def spherical_square_root_invariants(
    *, a: float, r: float, n: float, alpha: float,
    T_t: float, T_r: float, R: float, R_t: float, R_r: float,
) -> SphericalSquareRootInvariants:
    vals=(a,r,n,alpha,T_t,T_r,R,R_t,R_r)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all pullback inputs must be finite")
    if a <= 0 or r <= 0 or n <= 0 or alpha <= 0:
        raise ValueError("a,r,n,alpha must be positive")
    if R <= 0:
        raise ValueError("R must be positive")
    ftt = -n*n*T_t*T_t + alpha*alpha*R_t*R_t
    ftr = -n*n*T_t*T_r + alpha*alpha*R_t*R_r
    frr = -n*n*T_r*T_r + alpha*alpha*R_r*R_r
    A = np.array([[-ftt, -ftr], [ftr/(a*a), frr/(a*a)]], dtype=float)
    detA=float(np.linalg.det(A)); trA=float(np.trace(A))
    if detA <= 0:
        raise ValueError("spherical g^-1 f block must have positive determinant")
    root_det=math.sqrt(detA)
    rad=trA+2.0*root_det
    if rad <= 0:
        raise ValueError("principal square-root trace radicand must be positive")
    trS=math.sqrt(rad)
    detS=root_det
    ell=alpha*R/(a*r)
    e=np.array([
        1.0,
        trS+2.0*ell,
        detS+2.0*ell*trS+ell*ell,
        2.0*ell*detS+ell*ell*trS,
        ell*ell*detS,
    ],dtype=float)
    return SphericalSquareRootInvariants(
        tr_spherical_block=trS,
        det_spherical_block=detS,
        angular_eigenvalue=ell,
        e=e,
        det_ginv_f_block=detA,
        tr_ginv_f_block=trA,
    )


def spherical_interaction_density(*, betas, **kwargs) -> float:
    beta=tuple(float(x) for x in betas)
    if len(beta)!=5 or not all(math.isfinite(x) for x in beta):
        raise ValueError("betas must contain five finite coefficients")
    inv=spherical_square_root_invariants(**kwargs)
    return float(np.dot(np.asarray(beta,dtype=float),inv.e))


def temporal_interaction_branch_factor(*, beta1: float, beta2: float, beta3: float, xi: float, mu: float) -> float:
    vals=(beta1,beta2,beta3,xi,mu)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("branch-factor inputs must be finite")
    if xi <= 0.0 or mu <= -1.0:
        raise ValueError("xi must be positive and mu must exceed -1")
    q=1.0+mu
    return float(beta1 + 2.0*beta2*xi*q + beta3*xi*xi*q*q)


def temporal_shift_coefficient(*, a: float, H_g: float, c: float, mu: float, mu_dot: float) -> float:
    """Uniform-mode cosmic-time shift chi=(s/2)r^2 on the interaction branch."""
    vals=(a,H_g,c,mu,mu_dot)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("temporal-shift inputs must be finite")
    if a <= 0.0 or c <= 0.0 or mu <= -1.0:
        raise ValueError("a,c must be positive and mu must exceed -1")
    return float(-(a*a/c)*(mu_dot + H_g*mu*(c + 1.0 + mu)))


def homothetic_early_radial_polynomial_coefficients(
    *, beta1: float, beta2: float, beta3: float, K: float, w: float,
) -> np.ndarray:
    """Return normalized [mu^2,mu,1] coefficients of the early radial branch.

    Direct reduction of the exact spherical HR pullback on a homothetic FLRW
    background. These are algebraically the polynomial coefficients whose two
    roots are Aoki-Maeda-Namba Eq. (68), after excluding mu=-1.
    """
    vals=(beta1,beta2,beta3,K,w)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("homothetic radial inputs must be finite")
    if K <= 0.0:
        raise ValueError("K must be positive")
    D=beta1 + 2.0*K*beta2 + K*K*beta3
    if abs(D) <= 1e-14*max(1.0,abs(beta1),abs(2*K*beta2),abs(K*K*beta3)):
        raise np.linalg.LinAlgError("homothetic interaction normalization is singular")
    B2=(K*beta2 + K*K*beta3)/D
    B3=K*K*beta3/D
    return np.asarray([
        -2.0*B2 + (1.0+3.0*w)*B3,
        6.0*w*B2 - 2.0*B2 - 2.0,
        3.0*(w-1.0),
    ],dtype=float)
