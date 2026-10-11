"""Environmental Vainshtein scaling diagnostics for JANUS-R V2.

This module turns the static Aoki-Maeda-Namba Vainshtein-radius scaling into
simple dimensionless checks for a spherical relative perturbation.

For Lambda_g negligible and a matter-era top-hat relative source,

    (R_V / R)^3 ~= Omega_m(z) H(z)^2 |delta_rel| / (3 m_eff^2).

Using rho_m(z) = 3 H0^2 Omega_m0 (1+z)^3 /(8 pi G), the critical weighted
relative contrast at which R_V ~= R becomes

    |delta_rel|_crit = 3 (m_eff/H0)^2 / [Omega_m0 (1+z)^3].

This is a static scaling diagnostic. It is not a replacement for the full
cosmological nonlinear equations or a proof that the corresponding branch is
stable.
"""
from __future__ import annotations

from numerics.higuchi_scale_window import mass_ratio_from_compton_mpc


def weighted_relative_contrast(
    *, delta_g: float, delta_f: float, weight_f: float = 1.0
) -> float:
    """Return the relative source combination delta_g - weight_f*delta_f.

    `weight_f` packages the background/coupling factors multiplying the twin
    density in the relative scalar source. For a visible void and twin
    overdensity the two contributions add in magnitude.
    """
    if weight_f < 0.0:
        raise ValueError("weight_f must be non-negative")
    return float(delta_g - weight_f * delta_f)


def critical_relative_contrast(
    *,
    lambda_mpc: float,
    z: float,
    omega_m0: float = 0.30,
    h0_km_s_mpc: float = 70.0,
) -> float:
    """Contrast magnitude required for R_V/R=1 in the matter-source scaling."""
    if z < 0.0:
        raise ValueError("z must be non-negative")
    if omega_m0 <= 0.0:
        raise ValueError("omega_m0 must be positive")
    mass_ratio = mass_ratio_from_compton_mpc(
        lambda_mpc, h0_km_s_mpc=h0_km_s_mpc
    )
    return 3.0 * mass_ratio**2 / (omega_m0 * (1.0 + z) ** 3)


def rv_over_r(
    *,
    lambda_mpc: float,
    z: float,
    delta_relative: float,
    omega_m0: float = 0.30,
    h0_km_s_mpc: float = 70.0,
) -> float:
    """Return the static top-hat Vainshtein radius ratio R_V/R."""
    delta_crit = critical_relative_contrast(
        lambda_mpc=lambda_mpc,
        z=z,
        omega_m0=omega_m0,
        h0_km_s_mpc=h0_km_s_mpc,
    )
    return (abs(delta_relative) / delta_crit) ** (1.0 / 3.0)
