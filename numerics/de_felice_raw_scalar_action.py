"""Raw De Felice scalar-action building blocks.

This module follows De Felice et al. arXiv:1404.0008 directly rather than the
background-reduced Lagos action. The scalar decomposition is

    V_i = D_i B
    H_ij = 2 psi delta_ij + (D_i D_j - delta_ij Delta/3) E

with flat-space Fourier convention ``Delta -> -k^2``. The functions below
return source-level quadratic densities before any background reduction.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


def eh_scalar_quadratic_density_flat(*, lapse, scale_factor, H, Hdot_over_lapse, k, Phi, B, psi, E, psi_dot, E_dot):
    vals=(lapse,scale_factor,H,Hdot_over_lapse,k,Phi,B,psi,E,psi_dot,E_dot)
    if not all(math.isfinite(v) for v in vals): raise ValueError("all EH scalar inputs must be finite")
    if lapse<=0 or scale_factor<=0 or k<0: raise ValueError("lapse and scale_factor must be positive and k non-negative")
    N=lapse; a=scale_factor; k2=k*k; k4=k2*k2; k6=k4*k2; Hd=Hdot_over_lapse
    return float(
        -6*psi_dot**2/N**2+k4*E_dot**2/(6*N**2)+12*H*Phi*psi_dot/N
        +B*(2*k4*E_dot/(3*N*a)-4*k2*psi_dot/(N*a))
        +4*H*k2*Phi*B/a+4*k2*Phi*psi/a**2+2*k2*psi**2/a**2
        +2*k4*Phi*E/(3*a**2)+2*k4*psi*E/(3*a**2)+k6*E**2/(18*a**2)
        -9*H**2*Phi**2+18*H**2*Phi*psi+3*H**2*k2*B**2
        +(9*H**2+6*Hd)*psi**2+(-H**2-(2/3)*Hd)*k4*E**2
    )


def hr_scalar_quadratic_density_g_flat(*, xi, ctilde, k, mu_g, mu_f, zeta, gamma_m, Phi, B, varphi, b, Sigma, S):
    vals=(xi,ctilde,k,mu_g,mu_f,zeta,gamma_m,Phi,B,varphi,b,Sigma,S)
    if not all(math.isfinite(v) for v in vals): raise ValueError("all HR scalar inputs must be finite")
    if xi<=0 or ctilde<=0 or k<0: raise ValueError("xi and ctilde must be positive and k non-negative")
    k2=k*k; k4=k2*k2; trh=6*Sigma; h2=12*Sigma**2+(2/3)*k4*S**2
    qg=-.5*Phi**2+.5*k2*B**2
    qf=-.5*varphi**2+.5*k2*b**2+.125*(trh**2-2*h2)+.5*varphi*trh
    c2=trh**2-2*h2
    delta2=-(Phi-ctilde*varphi)*trh+k2*(B-ctilde*b)**2/(ctilde+1)+.25*(ctilde-1)*c2
    return float(-mu_g*qg-ctilde*xi**4*mu_f*qf+.5*zeta*delta2+.125*gamma_m*(trh**2-h2))


@dataclass(frozen=True)
class RawBimetricBackground:
    N: float; a: float; xi: float; ctilde: float; kappa: float
    H: float; Hf: float; Hdot_over_N: float; Hfdot_over_n: float
    mu_g: float; mu_f: float; zeta: float; gamma_m: float
    Mgsq: float = 1.0
    @property
    def n(self): return self.N*self.ctilde*self.xi
    @property
    def alpha(self): return self.a*self.xi


def raw_two_matter_scalar_density_g_flat(bg: RawBimetricBackground, **kwargs) -> float:
    """TDD RED stub for the full Eq.44+45+46+54 two-matter assembly."""
    return 0.0
