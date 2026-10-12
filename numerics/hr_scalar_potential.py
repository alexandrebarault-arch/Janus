"""Hassan-Rosen scalar-mode interaction potential in De Felice variables.

``hr_scalar_potential_density_de_felice`` evaluates the standard-beta local
matrix density ``+m^2 M_g^2 sqrt(-g) sum beta_n e_n(S)`` and is retained as a
convention/audit helper.

De Felice et al. instead write the interaction as ``+m^2 M_g^2 sum alpha_i
L_i(K)`` with ``K=I-S``.  Under their published alpha/beta correspondence this
is the *negative* standard-beta potential.  The perturbative helper
``hr_scalar_quadratic_potential_density_de_felice`` therefore uses the
negative shift-free standard-beta density and adds the scalar Fourier shift
block of Eqs. (45)-(46) analytically.
"""

from __future__ import annotations

import math
import numpy as np


def _e4_from_uvll(u_plus_v: float, uv: float, ell: float) -> tuple[float, ...]:
    e0 = 1.0
    e1 = u_plus_v + 2.0*ell
    e2 = uv + 2.0*ell*u_plus_v + ell*ell
    e3 = 2.0*ell*uv + ell*ell*u_plus_v
    e4 = ell*ell*uv
    return e0, e1, e2, e3, e4


def hr_scalar_potential_density_de_felice(
    *, N: float, a: float, n: float, alpha: float, m2: float, Mg2: float,
    betas, k: float, Phi_g: float, B_g: float, psi_g: float, E_g: float,
    Phi_f: float, B_f: float, psi_f: float, E_f: float,
) -> float:
    """Return the exact local *standard-beta* HR potential density.

    This raw helper uses ``+sum beta_n e_n(S)``.  It is not by itself the
    De-Felice interaction convention, and nonzero Fourier shifts should not be
    used to construct a quadratic action because their gradient phases are
    lost in a local real matrix representation.
    """
    betas = tuple(float(x) for x in betas)
    if len(betas) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    vals = (N,a,n,alpha,m2,Mg2,k,Phi_g,B_g,psi_g,E_g,Phi_f,B_f,psi_f,E_f,*betas)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all potential inputs must be finite")
    if N <= 0.0 or a <= 0.0 or n <= 0.0 or alpha <= 0.0:
        raise ValueError("lapses and scale factors must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")

    k2 = k*k
    gx = a*a*(1.0 + 2.0*psi_g - (2.0/3.0)*k2*E_g)
    gy = a*a*(1.0 + 2.0*psi_g + (1.0/3.0)*k2*E_g)
    fx = alpha*alpha*(1.0 + 2.0*psi_f - (2.0/3.0)*k2*E_f)
    fy = alpha*alpha*(1.0 + 2.0*psi_f + (1.0/3.0)*k2*E_f)
    g00 = -N*N*(1.0 + 2.0*Phi_g)
    f00 = -n*n*(1.0 + 2.0*Phi_f)
    g0x = N*a*k*B_g
    f0x = n*alpha*k*B_f
    if gy <= 0.0 or fy <= 0.0:
        raise ValueError("transverse spatial metric factors must stay positive")

    g2 = np.array([[g00,g0x],[g0x,gx]], dtype=float)
    f2 = np.array([[f00,f0x],[f0x,fx]], dtype=float)
    det_g2 = float(np.linalg.det(g2))
    if det_g2 >= 0.0:
        raise ValueError("time-longitudinal g block must remain Lorentzian")
    A = np.linalg.solve(g2,f2)
    detA = float(np.linalg.det(A)); trA = float(np.trace(A))
    if detA <= 0.0:
        raise ValueError("g^-1 f block must have positive determinant")
    root_det = math.sqrt(detA)
    denom2 = trA + 2.0*root_det
    if denom2 <= 0.0:
        raise ValueError("principal square-root denominator is non-positive")
    S2 = (A + root_det*np.eye(2))/math.sqrt(denom2)
    trS = float(np.trace(S2)); detS = float(np.linalg.det(S2))
    ell = math.sqrt(fy/gy)
    es = _e4_from_uvll(trS,detS,ell)
    sqrt_minus_g = math.sqrt(-det_g2)*gy
    return float(m2*Mg2*sqrt_minus_g*sum(b*e for b,e in zip(betas,es)))


def hr_scalar_quadratic_potential_density_de_felice(
    *, N: float, a: float, n: float, alpha: float, m2: float, Mg2: float,
    betas, k: float, Phi_g: float, B_g: float, psi_g: float, E_g: float,
    Phi_f: float, B_f: float, psi_f: float, E_f: float,
) -> float:
    """Quadratic-action-safe De Felice interaction for a scalar Fourier mode.

    The diagonal/lapse/spatial piece is minus the standard-beta potential,
    according to the alpha_i L_i(I-S) / beta_n e_n(S) correspondence quoted by
    De Felice et al.  The shift term is inserted directly from Eqs. (45)-(46):

      +(m^2 M_g^2/2) N a^3 xi J/(ctilde+1)
        k^2 (B_g-ctilde B_f)^2.
    """
    betas = tuple(float(x) for x in betas)
    if len(betas) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    if min(N,a,n,alpha) <= 0.0:
        raise ValueError("lapses and scale factors must be positive")

    standard_diagonal = hr_scalar_potential_density_de_felice(
        N=N,a=a,n=n,alpha=alpha,m2=m2,Mg2=Mg2,betas=betas,k=k,
        Phi_g=Phi_g,B_g=0.0,psi_g=psi_g,E_g=E_g,
        Phi_f=Phi_f,B_f=0.0,psi_f=psi_f,E_f=E_f,
    )
    diagonal = -standard_diagonal

    xi = alpha/a
    ctilde = n*a/(N*alpha)
    _,beta1,beta2,beta3,_ = betas
    J = beta1 + 2.0*beta2*xi + beta3*xi*xi
    if ctilde + 1.0 == 0.0:
        raise ValueError("ctilde+1 must be non-zero")
    shift = 0.5*m2*Mg2*N*a**3*xi*J/(ctilde+1.0)*k*k*(B_g-ctilde*B_f)**2
    return float(diagonal + shift)
