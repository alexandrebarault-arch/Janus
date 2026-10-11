"""Static anti-correlated void/twin-sector branch endpoint diagnostic.

This module specializes the Aoki-Maeda-Namba static equation (Appendix A,
Eq. A13 of arXiv:1506.04543) to an exterior spherical perturbation.

The quantity

    q = (K^2 G_f M_f)/(G_g M_g)

is a *perturbation-mass* ratio. A visible-sector mass deficit has M_g < 0,
while a twin-sector overdensity has M_f > 0, hence the Janus-like case has
q < 0. No fundamental negative matter mass is assumed.

The diagnostic finds the double-root endpoint of the asymptotically
homothetic (mu -> 0) algebraic branch. Loss of this algebraic branch is NOT a
proof that the full solution ceases to exist: it is precisely where radial
gradient terms neglected by the adiabatic/static algebraic approximation may
become essential.
"""

from __future__ import annotations

from dataclasses import dataclass

from scipy.optimize import root

from numerics.aoki_scalar_polynomial import Params, C_m2


@dataclass(frozen=True)
class CriticalVoidTransition:
    q: float
    mu_critical: float
    source_g_critical: float
    radius_over_rv: float


def static_outside_equation(
    mu: float,
    source_g: float,
    q: float,
    *,
    beta2: float = -3.0,
    beta3: float = 3.0,
    mg2: float = 0.5,
    mf2: float = 0.5,
    lambda_g: float = 0.0,
) -> float:
    """Return the exterior static scalar equation for a localized perturbation.

    Outside a spherical source,

        kappa_g^2 rho_tilde_g = source_g ~ M_g/R^3,

    while the f-sector mean density contains R_f = R(1+mu).  Writing the
    weighted perturbation-mass ratio as q makes the explicit (1+mu)^-3 factor
    cancel the corresponding factor in C_matter.
    """
    p = Params(beta2=beta2, beta3=beta3, mg2=mg2, mf2=mf2)
    matter = source_g * (
        (1.0 + mu) ** 2 * (1.0 - beta3 * mu**2)
        - q * (1.0 + 2.0 * mu + (2.0 * beta2 - beta3) * mu**2)
    )
    c_lambda = -lambda_g * mu * (1.0 + mu) ** 2 * (
        6.0
        + (2.0 + 8.0 * beta2) * mu
        + 2.0 * (beta2 + beta3) * mu**2
    )
    return float(C_m2(mu, p) + matter + c_lambda)


def _d_equation_dmu(
    mu: float,
    source_g: float,
    q: float,
    beta2: float,
    beta3: float,
    mg2: float,
    mf2: float,
    lambda_g: float,
) -> float:
    h = 1.0e-6
    return (
        static_outside_equation(
            mu + h,
            source_g,
            q,
            beta2=beta2,
            beta3=beta3,
            mg2=mg2,
            mf2=mf2,
            lambda_g=lambda_g,
        )
        - static_outside_equation(
            mu - h,
            source_g,
            q,
            beta2=beta2,
            beta3=beta3,
            mg2=mg2,
            mf2=mf2,
            lambda_g=lambda_g,
        )
    ) / (2.0 * h)


def critical_void_transition(
    q: float,
    *,
    beta2: float = -3.0,
    beta3: float = 3.0,
    mg2: float = 0.5,
    mf2: float = 0.5,
    lambda_g: float = 0.0,
) -> CriticalVoidTransition:
    """Locate the double-root endpoint connected to the homothetic branch.

    The radius normalization uses Lambda_g=0 and m_eff^2 = m_g^2 + m_f^2,
    which follows Eq. (5.7) of Aoki-Maeda-Namba for the variables used in
    their nonlinear scalar equation.
    """
    if q >= 0.0:
        raise ValueError("this void diagnostic requires anti-correlated q < 0")
    if lambda_g != 0.0:
        raise NotImplementedError("R/R_V normalization currently assumes Lambda_g=0")

    meff2 = mg2 + mf2
    guess_source = -0.46 / (1.0 - q)
    sol = root(
        lambda z: (
            static_outside_equation(
                z[0],
                z[1],
                q,
                beta2=beta2,
                beta3=beta3,
                mg2=mg2,
                mf2=mf2,
                lambda_g=lambda_g,
            ),
            _d_equation_dmu(
                z[0],
                z[1],
                q,
                beta2,
                beta3,
                mg2,
                mf2,
                lambda_g,
            ),
        ),
        (0.11, guess_source),
    )
    if not sol.success:
        raise RuntimeError(f"double-root solve failed: {sol.message}")

    mu_critical = float(sol.x[0])
    source_critical = float(sol.x[1])

    # source_g = 6 G_g M_g/R^3.  Eq. (A22) gives, for Lambda_g=0,
    # |source_g(R_V)| = 9 m_eff^2 / |1-q|.
    source_at_rv = 9.0 * meff2 / abs(1.0 - q)
    radius_over_rv = (source_at_rv / abs(source_critical)) ** (1.0 / 3.0)

    return CriticalVoidTransition(
        q=q,
        mu_critical=mu_critical,
        source_g_critical=source_critical,
        radius_over_rv=radius_over_rv,
    )


def void_vainshtein_ratio(
    *,
    omega_m: float,
    delta_g: float,
    q: float,
    m_eff_over_h0: float,
) -> float:
    """Return R_V/R_void for a spherical density contrast at z~0.

    Using rho_m = 3 H0^2 Omega_m/(8 pi G) and Eq. (A22) at Lambda_g=0,

      (R_V/R_void)^3 = Omega_m |delta_g| |1-q| /
                       [3 (m_eff/H0)^2].
    """
    if omega_m <= 0.0 or m_eff_over_h0 <= 0.0 or delta_g == 0.0:
        raise ValueError("require omega_m>0, m_eff_over_h0>0 and delta_g!=0")
    return (
        omega_m
        * abs(delta_g)
        * abs(1.0 - q)
        / (3.0 * m_eff_over_h0**2)
    ) ** (1.0 / 3.0)
