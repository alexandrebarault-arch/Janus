"""Infinitesimal twin-sector response of a homogeneous bimetric patch.

The diagnostic linearizes the two-matter separate-universe construction around
an initial anti-correlated seed

    delta_g = -epsilon,  delta_f = +epsilon.

Rather than evolving an arbitrary finite time step, it differentiates the
algebraic bimetric FLRW constraint F(y,a)=0 to obtain dy/d ln(a) on the
background and inside the homogeneous patch.  Matter conservation then gives
the instantaneous logarithmic growth rate of the twin contrast.

This is a susceptibility diagnostic.  A large value near a health/strong-
coupling boundary is not, by itself, a viable structure-growth prediction.
"""

from __future__ import annotations

import numpy as np

from numerics.two_matter_flrw import Model, densities, u_f, u_g
from numerics.two_matter_tophat import (
    _background_history,
    _fixed_density_roots,
    _nearest_root,
)


def _constraint_with_conserved_densities(
    y: float,
    a: float,
    m: Model,
    *,
    c_g_m: float,
    c_g_r: float,
    c_f: float,
) -> float:
    rho_g = c_g_m * a**-3 + c_g_r * a**-4
    rho_f = c_f / (y * a) ** 3
    return (
        m.alpha**2 * rho_g
        - y**2 * rho_f
        + float(m.m2)
        * (m.alpha**2 * u_g(y, m.beta) - y**2 * u_f(y, m.beta))
    )


def _dy_dln_a(
    y: float,
    a: float,
    m: Model,
    *,
    c_g_m: float,
    c_g_r: float,
    c_f: float,
) -> float:
    """Implicit derivative from F(y,a)=0 along a conserved-density branch."""
    rho_g_m = c_g_m * a**-3
    rho_g_r = c_g_r * a**-4
    rho_f = c_f / (y * a) ** 3

    # Partial derivative at fixed y.
    d_f_dln_a = (
        m.alpha**2 * (-3.0 * rho_g_m - 4.0 * rho_g_r)
        + 3.0 * y**2 * rho_f
    )

    # Numerical y derivative of the *same* conserved-density constraint.  A
    # centered relative step is accurate enough for the susceptibility gate and
    # avoids duplicating a long analytic derivative of the interaction terms.
    h = 1.0e-6 * max(1.0, abs(y))
    f_plus = _constraint_with_conserved_densities(
        y + h, a, m, c_g_m=c_g_m, c_g_r=c_g_r, c_f=c_f
    )
    f_minus = _constraint_with_conserved_densities(
        y - h, a, m, c_g_m=c_g_m, c_g_r=c_g_r, c_f=c_f
    )
    d_f_dy = (f_plus - f_minus) / (2.0 * h)
    if not np.isfinite(d_f_dy) or abs(d_f_dy) < 1.0e-14:
        raise RuntimeError("algebraic FLRW constraint is singular in y")

    return float(-d_f_dln_a / d_f_dy)


def initial_twin_growth_slope(
    m: Model,
    *,
    z: float,
    epsilon: float = 1.0e-5,
    visible_growth_slope: float = 1.0,
) -> float:
    """Return `(d delta_f/d ln a_bg)/delta_f` at the initial epoch.

    The initial perturbation is `delta_g=-epsilon`, `delta_f=+epsilon`.
    `visible_growth_slope` specifies the visible growing-mode velocity through

        d delta_g / d ln a_bg = visible_growth_slope * delta_g.

    The f-sector velocity is not chosen independently; it follows from the
    bimetric algebraic branch and separate matter conservation.
    """
    if z < 0.0:
        raise ValueError("z must be non-negative")
    if not (0.0 < epsilon < 1.0):
        raise ValueError("epsilon must satisfy 0 < epsilon < 1")
    if m.m2 is None or m.omega_f_m0 is None:
        raise ValueError("model must be calibrated()")

    a = 1.0 / (1.0 + z)
    _, y_bg_history, h_bg_history, _ = _background_history(m, a, points=500)
    y_bg = float(y_bg_history[0])
    h_bg = float(h_bg_history[0])

    rho_g_m = 3.0 * m.omega_g_m0 * a**-3
    rho_g_r = 3.0 * m.omega_g_r0 * a**-4
    _, rho_f_bg = densities(a, y_bg, m)

    delta_g = -epsilon
    delta_f = +epsilon
    rho_g_patch = (1.0 + delta_g) * rho_g_m + rho_g_r
    rho_f_patch = (1.0 + delta_f) * rho_f_bg
    y_patch = _nearest_root(
        _fixed_density_roots(rho_g_patch, rho_f_patch, m), y_bg
    )

    # Conserved-density normalizations.
    c_bg_g_m = 3.0 * m.omega_g_m0
    c_bg_g_r = 3.0 * m.omega_g_r0
    c_bg_f = rho_f_bg * (y_bg * a) ** 3

    c_patch_g_m = 3.0 * m.omega_g_m0 * (1.0 + delta_g)
    c_patch_g_r = 3.0 * m.omega_g_r0
    c_patch_f = rho_f_patch * (y_patch * a) ** 3

    yprime_bg = _dy_dln_a(
        y_bg,
        a,
        m,
        c_g_m=c_bg_g_m,
        c_g_r=c_bg_g_r,
        c_f=c_bg_f,
    )
    yprime_patch = _dy_dln_a(
        y_patch,
        a,
        m,
        c_g_m=c_patch_g_m,
        c_g_r=c_patch_g_r,
        c_f=c_patch_f,
    )

    # Visible growing-mode continuity fixes the local g expansion rate.
    h_patch_over_h_bg = 1.0 - (
        visible_growth_slope * delta_g / (3.0 * (1.0 + delta_g))
    )

    # In g-coordinate time, rho_f is conserved with b=a_g*y.  Synchronizing
    # patch and background at the same cosmic time gives the relative rate.
    dln_rhof_patch_dln_abg = -3.0 * (
        1.0 + yprime_patch / y_patch
    ) * h_patch_over_h_bg
    dln_rhof_bg_dln_abg = -3.0 * (1.0 + yprime_bg / y_bg)

    d_delta_f_dln_a = (1.0 + delta_f) * (
        dln_rhof_patch_dln_abg - dln_rhof_bg_dln_abg
    )
    return float(d_delta_f_dln_a / delta_f)
