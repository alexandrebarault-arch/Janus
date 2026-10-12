"""Hassan-Rosen scalar-mode interaction potential in De Felice variables.

``hr_scalar_potential_density_de_felice`` evaluates the standard-beta local
matrix density ``+m^2 M_g^2 sqrt(-g) sum beta_n e_n(S)`` and is retained as a
convention/audit helper.

``hr_scalar_quadratic_potential_density_de_felice`` is the historical helper
that evaluates the exact diagonal De-Felice-sign potential and adds the
Fourier shift block.  It is useful for finite-difference audits but still
contains background and linear pieces.

``hr_scalar_quadratic_action_density_de_felice`` implements directly the
O(delta^2) interaction written in De Felice et al. Eqs. (45)-(46).  It has no
background or linear term and is therefore the numerically stable helper to
use when assembling a quadratic Hessian.
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
    """Historical exact-diagonal De Felice helper plus analytic shift block.

    The diagonal/lapse/spatial piece is minus the exact standard-beta
    potential.  It therefore contains background and linear pieces and should
    be used for convention audits rather than high-k numerical Hessians.
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


def hr_scalar_quadratic_action_density_de_felice(
    *, N: float, a: float, n: float, alpha: float, m2: float, Mg2: float,
    betas, k: float, Phi_g: float, B_g: float, psi_g: float, E_g: float,
    Phi_f: float, B_f: float, psi_f: float, E_f: float,
) -> float:
    """Return only the O(delta^2) HR interaction of De Felice Eqs. (45)-(46).

    Unlike the exact-potential audit helper above, this expression contains
    neither the background nor linear perturbation pieces.  This avoids
    catastrophic subtraction when the quadratic action is differentiated to
    obtain the lapse/shift constraints at large k.
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

    beta0,beta1,beta2,beta3,beta4 = betas
    xi = alpha/a
    ctilde = n*a/(N*alpha)
    if xi <= 0.0 or ctilde <= 0.0 or ctilde + 1.0 == 0.0:
        raise ValueError("xi and ctilde must be positive")

    J = beta1 + 2.0*beta2*xi + beta3*xi*xi
    Gamma = xi*J + (ctilde-1.0)*xi*xi*(beta2 + beta3*xi)
    rhohat_g = beta0 + 3.0*beta1*xi + 3.0*beta2*xi*xi + beta3*xi**3
    rhohat_f = beta4 + 3.0*beta3/xi + 3.0*beta2/(xi*xi) + beta1/(xi**3)

    k2 = k*k
    k4 = k2*k2

    def scalar_invariants(psi: float, E: float) -> tuple[float,float]:
        tr = 6.0*psi
        h2 = 12.0*psi*psi + (2.0/3.0)*k4*E*E
        return tr,h2

    trg,h2g = scalar_invariants(psi_g,E_g)
    trf,h2f = scalar_invariants(psi_f,E_f)

    volume_g_2 = (
        -0.5*Phi_g*Phi_g
        + 0.5*k2*B_g*B_g
        + 0.125*(trg*trg - 2.0*h2g)
        + 0.5*Phi_g*trg
    )
    volume_f_2 = (
        -0.5*Phi_f*Phi_f
        + 0.5*k2*B_f*B_f
        + 0.125*(trf*trf - 2.0*h2f)
        + 0.5*Phi_f*trf
    )

    # Eq. (46): the last (ctilde-1) term is essential.  For scalar modes the
    # cross-contraction (H+h):(H-h) reduces to H:H-h:h.
    delta_spatial = (trg*trg - trf*trf) - 2.0*(h2g-h2f)
    Delta_2 = (
        (Phi_g-ctilde*Phi_f)*(trg-trf)
        + k2*(B_g-ctilde*B_f)**2/(ctilde+1.0)
        - 0.25*(ctilde-1.0)*delta_spatial
    )

    # Eq. (45) Gamma block.
    H_dot_h = 12.0*psi_g*psi_f + (2.0/3.0)*k4*E_g*E_f
    hdiff2 = h2g + h2f - 2.0*H_dot_h
    gamma_block = (trg-trf)**2 - hdiff2

    density = m2*Mg2*(
        -N*a**3*rhohat_g*volume_g_2
        -n*alpha**3*rhohat_f*volume_f_2
        +0.5*N*a**3*xi*J*Delta_2
        +0.125*N*a**3*Gamma*gamma_block
    )
    return float(density)
