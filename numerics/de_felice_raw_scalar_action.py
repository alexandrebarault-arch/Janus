"""Raw De Felice scalar-action building blocks.

Direct source route from De Felice et al. arXiv:1404.0008: Eq. (44), the
f-metric analogue, Eqs. (45)-(46), and two copies of Eq. (54). No background
identity is applied inside these helpers.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from numerics.de_felice_matter_action import kessence_scalar_quadratic_density


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


def raw_two_matter_scalar_density_g_flat(
    bg: RawBimetricBackground, *, k, Phi, B, varphi, b, Sigma, S,
    Sigma_dot, S_dot, rho_g, pressure_g, cs2_g, u_g, u_g_dot,
    rho_f, pressure_f, cs2_f, u_f, u_f_dot,
) -> float:
    """Full raw quadratic density divided by ``M_g^2 N a^3``.

    This is the independent A2.4d oracle: EH(g)+EH(f)+HR+matter(g)+matter(f).
    The g-flat gauge is ``psi_g=E_g=0``. Background equations must be used by
    the caller only when constructing the coefficient combinations in ``bg``.
    """
    if bg.Mgsq<=0 or bg.kappa<=0: raise ValueError("Mgsq and kappa must be positive")
    if bg.N<=0 or bg.a<=0 or bg.xi<=0 or bg.ctilde<=0: raise ValueError("background lapse/scale ratios must be positive")
    eh_g=eh_scalar_quadratic_density_flat(lapse=bg.N,scale_factor=bg.a,H=bg.H,Hdot_over_lapse=bg.Hdot_over_N,k=k,Phi=Phi,B=B,psi=0.0,E=0.0,psi_dot=0.0,E_dot=0.0)
    eh_f=eh_scalar_quadratic_density_flat(lapse=bg.n,scale_factor=bg.alpha,H=bg.Hf,Hdot_over_lapse=bg.Hfdot_over_n,k=k,Phi=varphi,B=b,psi=Sigma,E=S,psi_dot=Sigma_dot,E_dot=S_dot)
    gravity=.5*eh_g+.5*bg.kappa*bg.ctilde*bg.xi**4*eh_f+hr_scalar_quadratic_density_g_flat(xi=bg.xi,ctilde=bg.ctilde,k=k,mu_g=bg.mu_g,mu_f=bg.mu_f,zeta=bg.zeta,gamma_m=bg.gamma_m,Phi=Phi,B=B,varphi=varphi,b=b,Sigma=Sigma,S=S)
    matter_g=kessence_scalar_quadratic_density(rho=rho_g,pressure=pressure_g,cs2=cs2_g,lapse=bg.N,scale_factor=bg.a,k=k,Phi=Phi,B=B,psi=0.0,E=0.0,field_ratio=u_g,field_velocity_ratio=u_g_dot)
    matter_f=kessence_scalar_quadratic_density(rho=rho_f,pressure=pressure_f,cs2=cs2_f,lapse=bg.n,scale_factor=bg.alpha,k=k,Phi=varphi,B=b,psi=Sigma,E=S,field_ratio=u_f,field_velocity_ratio=u_f_dot)
    return float(gravity+matter_g/bg.Mgsq+bg.ctilde*bg.xi**4*matter_f/bg.Mgsq)
