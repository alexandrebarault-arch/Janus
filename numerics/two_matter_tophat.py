"""Homogeneous two-matter separate-universe diagnostic for JANUS-R V2.

This module evolves a homogeneous spherical *patch* as its own curved bimetric
FLRW universe.  It is an intermediate nonlinear diagnostic inspired by the
homogeneous-overdensity construction of Högås, Torsello & Mörtsell (2020), but
with both separately coupled dust sectors retained.

Important scope limitation
--------------------------
A real cosmic void has a radial profile and a compensation wall.  This module
contains no radial gradients and does not solve the matching problem to the
exterior universe.  It therefore tests homogeneous nonlinear growth only; it
is not a full void solution.

Conventions follow ``numerics.two_matter_flrw``.  The local g-sector curvature
K is fixed by the initial visible-matter velocity perturbation.  On the
bimetric dynamical FLRW branch the curvature term cancels when the two
Friedmann equations are combined, so the algebraic equation determining
``y = a_f/a_g`` retains the same form with local conserved densities.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import brentq

from numerics.two_matter_flrw import (
    Beta,
    Model,
    densities,
    hubble2_g,
    track_from_today,
    u_f,
    u_g,
)


@dataclass(frozen=True)
class TopHatResult:
    a_initial: float
    y_background_initial: float
    y_patch_initial: float
    curvature_k: float
    a_patch_final: float
    y_patch_final: float
    delta_g_final: float
    delta_f_final: float


def v2_tophat_control_candidate() -> Model:
    """Return a reproducible V2 scan point used only as a control model.

    The point was found in an exploratory background/stability scan.  It has
    ``beta0=0``, an expansion history close to flat Lambda-CDM at low redshift,
    and the simple W/Higuchi diagnostic remains positive to roughly z~19 in
    the scan.  That does *not* prove full scalar/vector/tensor stability and
    this function must not be interpreted as a viable-model claim.
    """

    return Model(
        beta=Beta(
            beta0=0.0,
            beta1=12.534085214003532,
            beta2=1.149521062632644,
            beta3=-15.975211739138032,
            beta4=-24.621659003672526,
        ),
        alpha=0.11184055950402368,
        y0=0.4846054559914972,
    ).calibrated()


def _fixed_density_equation(y: float, rho_g: float, rho_f: float, m: Model) -> float:
    return (
        m.alpha**2 * rho_g
        - y**2 * rho_f
        + float(m.m2)
        * (
            m.alpha**2 * u_g(y, m.beta)
            - y**2 * u_f(y, m.beta)
        )
    )


def _fixed_density_roots(
    rho_g: float,
    rho_f: float,
    m: Model,
    *,
    y_min: float = 1.0e-7,
    y_max: float = 1.0e3,
    samples: int = 360,
) -> np.ndarray:
    grid = np.logspace(np.log10(y_min), np.log10(y_max), samples)
    roots: list[float] = []
    x0 = grid[0]
    f0 = _fixed_density_equation(x0, rho_g, rho_f, m)
    for x1 in grid[1:]:
        f1 = _fixed_density_equation(x1, rho_g, rho_f, m)
        if np.isfinite(f0) and np.isfinite(f1) and f0 * f1 < 0.0:
            root = brentq(
                lambda yy: _fixed_density_equation(yy, rho_g, rho_f, m),
                x0,
                x1,
                maxiter=200,
            )
            if not roots or abs(root - roots[-1]) > 1e-8 * max(1.0, abs(root)):
                roots.append(root)
        x0, f0 = x1, f1
    return np.asarray(roots)


def _nearest_root(roots: np.ndarray, reference: float) -> float:
    if len(roots) == 0:
        raise RuntimeError("no positive real y root")
    return float(roots[np.argmin(np.abs(np.log(roots / reference)))])


def _background_history(m: Model, a_initial: float, points: int):
    a_desc, y_desc = track_from_today(m, a_min=a_initial, points=points)
    a = np.asarray(a_desc[::-1])
    y = np.asarray(y_desc[::-1])
    h = np.sqrt(np.asarray([hubble2_g(ai, yi, m) for ai, yi in zip(a, y)]))
    t = cumulative_trapezoid(1.0 / (a * h), a, initial=0.0)
    return a, y, h, t


def evolve_homogeneous_patch(
    m: Model,
    *,
    a_initial: float,
    delta_g_initial: float,
    delta_f_initial: float,
    visible_growth_slope: float = 1.0,
    background_points: int = 900,
    patch_points: int = 2400,
    patch_a_max: float = 2.0,
) -> TopHatResult:
    """Evolve a homogeneous two-sector patch until the background reaches a=1.

    ``delta_g_initial`` refers to the visible *dust* contrast; visible radiation
    is initialized unperturbed.  ``delta_f_initial`` refers to the twin-dust
    contrast.

    The initial visible velocity is fixed through

        d(delta_g)/d ln(a_bg) = visible_growth_slope * delta_g,

    which implies

        H_patch/H_bg = 1 - visible_growth_slope*delta_g/[3(1+delta_g)]

    for pressureless visible matter.  This determines the local curvature K.

    The f-sector initial velocity is not independently imposed; it follows
    from the bimetric branch and is one of the quantities being tested.
    """

    if not (0.0 < a_initial < 1.0):
        raise ValueError("a_initial must satisfy 0 < a_initial < 1")
    if delta_g_initial <= -1.0 or delta_f_initial <= -1.0:
        raise ValueError("density contrasts must be greater than -1")
    if patch_a_max <= a_initial:
        raise ValueError("patch_a_max must exceed a_initial")

    a_bg, y_bg, h_bg, t_bg = _background_history(m, a_initial, background_points)
    yb_i = float(y_bg[0])
    hb_i = float(h_bg[0])

    rho_g_m_i = 3.0 * m.omega_g_m0 * a_initial**-3
    rho_g_r_i = 3.0 * m.omega_g_r0 * a_initial**-4
    _, rho_f_bg_i = densities(a_initial, yb_i, m)

    rho_g_patch_i = (1.0 + delta_g_initial) * rho_g_m_i + rho_g_r_i
    rho_f_patch_i = (1.0 + delta_f_initial) * rho_f_bg_i

    initial_roots = _fixed_density_roots(rho_g_patch_i, rho_f_patch_i, m)
    yp_i = _nearest_root(initial_roots, yb_i)

    h_patch_i = hb_i * (
        1.0
        - visible_growth_slope
        * delta_g_initial
        / (3.0 * (1.0 + delta_g_initial))
    )
    curvature_k = a_initial**2 * (
        (rho_g_patch_i + float(m.m2) * u_g(yp_i, m.beta)) / 3.0
        - h_patch_i**2
    )

    # Conserved density normalizations in the local FLRW patch.
    c_g_m = rho_g_m_i * (1.0 + delta_g_initial) * a_initial**3
    c_g_r = rho_g_r_i * a_initial**4
    c_f = rho_f_patch_i * (yp_i * a_initial) ** 3

    a_patch = np.geomspace(a_initial, patch_a_max, patch_points)
    y_patch: list[float] = []
    h_patch: list[float] = []
    previous_y = yp_i

    for ap in a_patch:
        rho_g = c_g_m * ap**-3 + c_g_r * ap**-4

        # Search locally around the continuously connected root first.  Fall
        # back to the full positive-y interval if needed.
        y_lo = max(1.0e-8, previous_y / 8.0)
        y_hi = min(1.0e5, previous_y * 8.0)

        def local_equation(y: float) -> float:
            rho_f = c_f / (y * ap) ** 3
            return _fixed_density_equation(y, rho_g, rho_f, m)

        grid = np.logspace(np.log10(y_lo), np.log10(y_hi), 180)
        local_roots: list[float] = []
        f0 = local_equation(grid[0])
        x0 = grid[0]
        for x1 in grid[1:]:
            f1 = local_equation(x1)
            if np.isfinite(f0) and np.isfinite(f1) and f0 * f1 < 0.0:
                rr = brentq(local_equation, x0, x1, maxiter=200)
                if not local_roots or abs(rr - local_roots[-1]) > 1e-9:
                    local_roots.append(rr)
            x0, f0 = x1, f1

        if not local_roots:
            rho_f_reference = c_f / (previous_y * ap) ** 3
            broad_roots = _fixed_density_roots(
                rho_g,
                rho_f_reference,
                m,
                y_min=1.0e-8,
                y_max=1.0e5,
                samples=600,
            )
            # The broad helper holds rho_f fixed and therefore cannot directly
            # solve the conserved-f equation.  Re-bracket the full conserved-f
            # equation instead when the local search failed.
            del broad_roots
            broad_grid = np.logspace(-8, 5, 700)
            f0 = local_equation(broad_grid[0])
            x0 = broad_grid[0]
            for x1 in broad_grid[1:]:
                f1 = local_equation(x1)
                if np.isfinite(f0) and np.isfinite(f1) and f0 * f1 < 0.0:
                    local_roots.append(brentq(local_equation, x0, x1, maxiter=200))
                x0, f0 = x1, f1

        if not local_roots:
            raise RuntimeError(f"local y branch lost at a_patch={ap:g}")

        yp = float(
            local_roots[
                np.argmin(np.abs(np.log(np.asarray(local_roots) / previous_y)))
            ]
        )
        h2 = (
            rho_g + float(m.m2) * u_g(yp, m.beta)
        ) / 3.0 - curvature_k / ap**2
        if h2 <= 0.0:
            raise RuntimeError(f"patch reached turnaround at a_patch={ap:g}")

        y_patch.append(yp)
        h_patch.append(float(np.sqrt(h2)))
        previous_y = yp

    y_patch_arr = np.asarray(y_patch)
    h_patch_arr = np.asarray(h_patch)
    t_patch = cumulative_trapezoid(
        1.0 / (a_patch * h_patch_arr),
        a_patch,
        initial=0.0,
    )

    final_time = float(t_bg[-1])
    if final_time > float(t_patch[-1]):
        raise RuntimeError("patch_a_max too small to reach background a=1 time")

    ap_final = float(np.interp(final_time, t_patch, a_patch))
    yp_final = float(np.interp(ap_final, a_patch, y_patch_arr))

    rho_g_m_patch_final = c_g_m / ap_final**3
    rho_f_patch_final = c_f / (yp_final * ap_final) ** 3
    rho_g_m_background_final = 3.0 * m.omega_g_m0
    rho_f_background_final = 3.0 * m.alpha**2 * float(m.omega_f_m0)

    delta_g_final = rho_g_m_patch_final / rho_g_m_background_final - 1.0
    delta_f_final = rho_f_patch_final / rho_f_background_final - 1.0

    return TopHatResult(
        a_initial=a_initial,
        y_background_initial=yb_i,
        y_patch_initial=yp_i,
        curvature_k=float(curvature_k),
        a_patch_final=ap_final,
        y_patch_final=yp_final,
        delta_g_final=float(delta_g_final),
        delta_f_final=float(delta_f_final),
    )
