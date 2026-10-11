"""Low-energy scale-window diagnostics for JANUS-R.

This module uses the low-energy/pure-gravity healthy-branch relation

    W = m_eff^2/2 - H^2,

so the linear Higuchi-safe regime requires m_eff^2 > 2 H^2.

For a constant effective mass in a matter-dominated background this gives a
simple estimate for the redshift at which the linear regime can become healthy.
It is a scaling diagnostic, not a full FLRW stability calculation.
"""
from __future__ import annotations

import math

C_KM_S = 299_792.458
P_REL_MAX = (-1.0 + math.sqrt(33.0)) / 4.0


def hubble_length_mpc(h0_km_s_mpc: float) -> float:
    if h0_km_s_mpc <= 0:
        raise ValueError("H0 must be positive")
    return C_KM_S / h0_km_s_mpc


def mass_ratio_from_compton_mpc(
    lambda_mpc: float, *, h0_km_s_mpc: float = 70.0
) -> float:
    """Return m_eff/H0 from lambda=c/m_eff in the c=1 cosmological scaling."""
    if lambda_mpc <= 0:
        raise ValueError("Compton length must be positive")
    return hubble_length_mpc(h0_km_s_mpc) / lambda_mpc


def matter_higuchi_crossing_redshift(
    m_eff_over_h0: float, *, omega_m0: float = 0.30
) -> float:
    """Matter-era estimate from m_eff^2 = 2 H^2.

    Uses H^2/H0^2 ~= Omega_m0 (1+z)^3. A negative result means the constant
    mass proxy would not satisfy the low-energy bound even today in this
    approximation.
    """
    if m_eff_over_h0 <= 0 or omega_m0 <= 0:
        raise ValueError("mass ratio and Omega_m0 must be positive")
    return (m_eff_over_h0**2 / (2.0 * omega_m0)) ** (1.0 / 3.0) - 1.0


def eds_relative_growth(z_start: float, *, p: float = P_REL_MAX) -> float:
    """Maximum toy growth factor a^p from z_start to today."""
    if z_start < 0:
        raise ValueError("z_start must be non-negative")
    return (1.0 + z_start) ** p
