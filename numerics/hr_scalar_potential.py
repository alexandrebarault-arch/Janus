"""Exact Hassan-Rosen scalar-mode interaction potential.

The function in this module evaluates the non-derivative bimetric potential
on one flat scalar Fourier mode written in De Felice variables.  Choosing the
wave-vector along x makes both metrics block diagonal: one 2x2 time/longitudinal
block plus two identical transverse entries.  The principal square root of the
2x2 block is therefore analytic and no background field equation is used.
"""

from __future__ import annotations

import math
import numpy as np


def _e4_from_uvll(u_plus_v: float, uv: float, ell: float) -> tuple[float, ...]:
    """Elementary symmetric polynomials of eigenvalues (u,v,ell,ell)."""
    e0 = 1.0
    e1 = u_plus_v + 2.0*ell
    e2 = uv + 2.0*ell*u_plus_v + ell*ell
    e3 = 2.0*ell*uv + ell*ell*u_plus_v
    e4 = ell*ell*uv
    return e0, e1, e2, e3, e4


def hr_scalar_potential_density_de_felice(
    *,
    N: float,
    a: float,
    n: float,
    alpha: float,
    m2: float,
    Mg2: float,
    betas,
    k: float,
    Phi_g: float,
    B_g: float,
    psi_g: float,
    E_g: float,
    Phi_f: float,
    B_f: float,
    psi_f: float,
    E_f: float,
) -> float:
    """Return ``m^2 Mg^2 sqrt(-g) sum beta_n e_n(sqrt(g^-1 f))``.

    The scalar metric convention is De Felice et al. Eq. (41),(67), with the
    Fourier wave-vector aligned with x.  ``k`` is the comoving wave number.
    """
    betas = tuple(float(x) for x in betas)
    if len(betas) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    vals = (
        N, a, n, alpha, m2, Mg2, k,
        Phi_g, B_g, psi_g, E_g,
        Phi_f, B_f, psi_f, E_f,
        *betas,
    )
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all potential inputs must be finite")
    if N <= 0.0 or a <= 0.0 or n <= 0.0 or alpha <= 0.0:
        raise ValueError("lapses and scale factors must be positive")
    if k < 0.0:
        raise ValueError("k must be non-negative")

    k2 = k*k

    # De Felice scalar spatial perturbation:
    # H_xx=2 psi-(2/3)k^2 E, H_yy=H_zz=2 psi+(1/3)k^2 E.
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

    g2 = np.array([[g00, g0x], [g0x, gx]], dtype=float)
    f2 = np.array([[f00, f0x], [f0x, fx]], dtype=float)
    det_g2 = float(np.linalg.det(g2))
    if det_g2 >= 0.0:
        raise ValueError("time-longitudinal g block must remain Lorentzian")

    A = np.linalg.solve(g2, f2)
    detA = float(np.linalg.det(A))
    trA = float(np.trace(A))
    if detA <= 0.0:
        raise ValueError("g^-1 f block must have positive determinant")
    root_det = math.sqrt(detA)
    denom2 = trA + 2.0*root_det
    if denom2 <= 0.0:
        raise ValueError("principal square-root denominator is non-positive")
    denom = math.sqrt(denom2)
    S2 = (A + root_det*np.eye(2)) / denom

    trS = float(np.trace(S2))
    detS = float(np.linalg.det(S2))
    ell = math.sqrt(fy/gy)
    es = _e4_from_uvll(trS, detS, ell)

    # sqrt(-g) for the block-diagonal mode: sqrt(-det(g2))*g_yy,
    # with y and z transverse entries equal.
    sqrt_minus_g = math.sqrt(-det_g2) * gy
    return float(m2 * Mg2 * sqrt_minus_g * sum(b*e for b, e in zip(betas, es)))
