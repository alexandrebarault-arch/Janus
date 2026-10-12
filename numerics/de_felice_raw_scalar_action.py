"""Raw De Felice scalar-action building blocks.

This module follows De Felice et al. arXiv:1404.0008 directly rather than the
background-reduced Lagos action. The scalar decomposition is

    V_i = D_i B
    H_ij = 2 psi delta_ij + (D_i D_j - delta_ij Delta/3) E

with flat-space Fourier convention ``Delta -> -k^2``. The functions below
return source-level quadratic densities before any background reduction.
"""

from __future__ import annotations

import math


def eh_scalar_quadratic_density_flat(
    *, lapse: float, scale_factor: float, H: float, Hdot_over_lapse: float,
    k: float, Phi: float, B: float, psi: float, E: float,
    psi_dot: float, E_dot: float,
) -> float:
    """Scalar specialization of De Felice Eq. (44) for ``K=0``.

    The result is the bracket ``L_EH^(2)`` before the overall factor
    ``(M^2/2) * lapse * scale_factor^3``. No background equation is used.
    """
    vals = (lapse, scale_factor, H, Hdot_over_lapse, k, Phi, B,
            psi, E, psi_dot, E_dot)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all EH scalar inputs must be finite")
    if lapse <= 0.0 or scale_factor <= 0.0 or k < 0.0:
        raise ValueError("lapse and scale_factor must be positive and k non-negative")
    N = lapse; a = scale_factor; k2 = k*k; k4 = k2*k2; k6 = k4*k2
    Hd = Hdot_over_lapse
    kinetic = (
        -6.0*psi_dot**2/N**2 + k4*E_dot**2/(6.0*N**2)
        + 12.0*H*Phi*psi_dot/N
        + B*(2.0*k4*E_dot/(3.0*N*a) - 4.0*k2*psi_dot/(N*a))
    )
    spatial = (
        4.0*H*k2*Phi*B/a + 4.0*k2*Phi*psi/a**2
        + 2.0*k2*psi**2/a**2 + 2.0*k4*Phi*E/(3.0*a**2)
        + 2.0*k4*psi*E/(3.0*a**2) + k6*E**2/(18.0*a**2)
    )
    background = (
        -9.0*H**2*Phi**2 + 18.0*H**2*Phi*psi
        + 3.0*H**2*k2*B**2 + (9.0*H**2 + 6.0*Hd)*psi**2
        + (-H**2 - (2.0/3.0)*Hd)*k4*E**2
    )
    return float(kinetic + spatial + background)


def hr_scalar_quadratic_density_g_flat(
    *, xi: float, ctilde: float, k: float,
    mu_g: float, mu_f: float, zeta: float, gamma_m: float,
    Phi: float, B: float, varphi: float, b: float, Sigma: float, S: float,
) -> float:
    """Raw Hassan-Rosen quadratic density from De Felice Eqs. (45)-(46).

    The result is normalized by ``M_g^2 N a^3`` and already includes ``m^2``.
    The source-transparent coefficient combinations are
    ``mu_g=m^2*rhohat_m,g``, ``mu_f=m^2*rhohat_m,f``,
    ``zeta=m^2*xi*J`` and ``gamma_m=m^2*Gamma``.

    The gauge is g-flat (``psi=E=0``). No background identity is applied
    internally.
    """
    vals = (xi, ctilde, k, mu_g, mu_f, zeta, gamma_m,
            Phi, B, varphi, b, Sigma, S)
    if not all(math.isfinite(v) for v in vals):
        raise ValueError("all HR scalar inputs must be finite")
    if xi <= 0.0 or ctilde <= 0.0 or k < 0.0:
        raise ValueError("xi and ctilde must be positive and k non-negative")
    k2 = k*k; k4 = k2*k2
    trh = 6.0*Sigma
    h2 = 12.0*Sigma**2 + (2.0/3.0)*k4*S**2
    qg = -0.5*Phi**2 + 0.5*k2*B**2
    qf = (
        -0.5*varphi**2 + 0.5*k2*b**2
        + 0.125*(trh**2 - 2.0*h2) + 0.5*varphi*trh
    )
    c2 = trh**2 - 2.0*h2
    delta2 = (
        -(Phi-ctilde*varphi)*trh
        + k2*(B-ctilde*b)**2/(ctilde+1.0)
        + 0.25*(ctilde-1.0)*c2
    )
    gamma_contraction = trh**2 - h2
    return float(
        -mu_g*qg - ctilde*xi**4*mu_f*qf
        + 0.5*zeta*delta2 + 0.125*gamma_m*gamma_contraction
    )
