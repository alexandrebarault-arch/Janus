"""Independent high-k scalar principal action from De Felice et al.

This module implements the gravitational scalar principal coefficients from
arXiv:1404.0008, Eqs. (80), (82), and (86), directly in JANUS background
variables.  It deliberately does not call ``flrw_two_matter.diagnostics`` or
any Comelli perturbation equation.

Conventions: flat FLRW by default, M_g^2 = 1, and ``ScalarBackground.H`` is
the conformal Hubble rate calH, so the physical Hubble rate is calH/a.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

from numerics.comelli_dae import ScalarBackground


@dataclass(frozen=True)
class GravityPrincipalAction:
    J: float
    Gamma: float
    W: float
    B: float
    kinetic_coefficient: float
    gradient_coefficient: float
    cs2: float


def gravity_principal_action(
    bg: ScalarBackground,
    *,
    rho_f_plus_p_f: float,
    curvature_K: float = 0.0,
    M_g2: float = 1.0,
) -> GravityPrincipalAction:
    """Return the helicity-0 high-frequency principal action coefficients.

    ``rho_f_plus_p_f`` is the f-sector enthalpy density in the same units as
    ``M_g2 * H^2``.  The returned kinetic coefficient is the k->infinity
    De-Felice NG3 coefficient (flat-space expression when K=0); the gradient
    coefficient is defined as ``kinetic * cs2``.
    """
    values = (
        bg.a, bg.m2, bg.f1, bg.f2, bg.H, bg.c, bg.xi,
        bg.kappa, rho_f_plus_p_f, curvature_K, M_g2,
    )
    if not all(math.isfinite(v) for v in values):
        raise ValueError("all inputs must be finite")
    if bg.a <= 0.0 or bg.xi == 0.0 or bg.kappa == 0.0 or M_g2 <= 0.0:
        raise ValueError("a and M_g2 must be positive; xi and kappa non-zero")

    xi = bg.xi
    kappa = bg.kappa
    J = bg.f2 / xi
    Gamma = bg.f1
    if J == 0.0:
        raise ValueError("J must be non-zero for the scalar principal action")

    H2_phys = (bg.H / bg.a) ** 2
    curvature_term = curvature_K / (bg.a * bg.a)
    W = (
        bg.m2 * (1.0 + kappa * xi * xi) * J / (2.0 * kappa * xi)
        - (H2_phys + curvature_term)
    )
    B = 2.0 * W + xi * xi * rho_f_plus_p_f / (kappa * M_g2)
    if B == 0.0:
        raise ValueError("De Felice B is zero; principal scalar kinetic term is singular")

    cs2 = (
        bg.m2
        / (3.0 * B)
        * (1.0 + 1.0 / (kappa * xi * xi))
        * (4.0 * Gamma - xi * J * (bg.c + 1.0))
        + (
            bg.c
            - 4.0 * (H2_phys + curvature_term) * Gamma / (xi * J * B)
        )
        / 3.0
    )

    # Eq. (80): NG3 -> (3/8) m^2 a^4 xi J B for K=0.
    # Since xi*J=f2, this is also (3/8) m^2 a^4 f2 B.
    kinetic = 3.0 / 8.0 * bg.m2 * bg.a**4 * xi * J * B
    gradient = kinetic * cs2
    return GravityPrincipalAction(
        J=float(J),
        Gamma=float(Gamma),
        W=float(W),
        B=float(B),
        kinetic_coefficient=float(kinetic),
        gradient_coefficient=float(gradient),
        cs2=float(cs2),
    )
