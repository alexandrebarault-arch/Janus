"""Build the reference JANUS-R twin-wall initial state for bim-solver STD.

This module composes three already-tested pieces:
- the time-symmetric twin Lane-Emden constraint solver;
- the exact time-symmetric lapse-ratio gate;
- the patched bim-solver 26-column input mapper.

It does not evolve the spacetime.
"""
from __future__ import annotations

from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    gaussian_profile,
    shell_profile,
    solve_initial_data,
)
from numerics.time_symmetric_lapse_gate import time_symmetric_w
from numerics.bim_solver_twin_input import build_rows, uniform_centers, write_text_input


def cubic_resample(x, y, x_target):
    """Smoothly resample a BVP field and its radial derivative."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xt = np.asarray(x_target, dtype=float)
    if x.ndim != 1 or y.shape != x.shape or xt.ndim != 1 or len(x) < 4:
        raise ValueError("invalid spline inputs")
    if np.any(np.diff(x) <= 0):
        raise ValueError("source radius must be strictly increasing")
    if xt.size and (xt[0] < x[0] or xt[-1] > x[-1]):
        raise ValueError("target radii must lie inside the BVP domain")
    spline = CubicSpline(x, y, bc_type="not-a-knot")
    return np.asarray(spline(xt)), np.asarray(spline(xt, 1))


def reference_wall_rows(
    *,
    n: int,
    delta_r: float,
    solve_points: int = 600,
    tol: float = 2.0e-7,
):
    """Return the reference constrained twin-wall state on solver cell centers."""
    if n < 4 or delta_r <= 0 or solve_points < 20:
        raise ValueError("invalid grid or constraint-solver resolution")

    beta = flat_beta_from123(1.0, -0.2, 0.0)
    interaction = 0.02
    params = Params(beta=beta, interaction=interaction, kappa_g=1.0, kappa_f=1.0)
    Dg_fn = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    Df_fn = lambda r: gaussian_profile(r, 0.04, 2.0)

    r_outer = n * float(delta_r)
    sol = solve_initial_data(
        params,
        Dg_fn,
        Df_fn,
        r_max=r_outer,
        points=solve_points,
        tol=tol,
    )
    if not sol.success:
        raise RuntimeError("reference initial-constraint solve failed")
    if np.any(np.asarray(sol.psi_g) <= 0) or np.any(np.asarray(sol.psi_f) <= 0):
        raise RuntimeError("constraint solve produced a non-positive conformal factor")

    r = uniform_centers(n, delta_r)
    solve_r = np.asarray(sol.r, dtype=float)
    solve_pg = np.asarray(sol.psi_g, dtype=float)
    solve_pf = np.asarray(sol.psi_f, dtype=float)

    pg, dpg = cubic_resample(solve_r, solve_pg, r)
    pf, dpf = cubic_resample(solve_r, solve_pf, r)
    Dg = np.asarray(Dg_fn(r), dtype=float)
    Df = np.asarray(Df_fn(r), dtype=float)

    Ag = Bg = pg**2
    Af = Bf = pf**2
    gDB = 2.0 * dpg / pg
    fDB = 2.0 * dpf / pf
    b = np.asarray(beta, dtype=float) * interaction

    W = np.empty(n, dtype=float)
    Wg = np.empty(n, dtype=float)
    Wf = np.empty(n, dtype=float)
    for i, rr in enumerate(r):
        wi, wgi, wfi = time_symmetric_w(
            r=float(rr),
            Ag=float(Ag[i]),
            Af=float(Af[i]),
            Bg=float(Bg[i]),
            Bf=float(Bf[i]),
            gDB=float(gDB[i]),
            fDB=float(fDB[i]),
            b0=float(b[0]),
            b1=float(b[1]),
            b2=float(b[2]),
            b3=float(b[3]),
            b4=float(b[4]),
            kg=1.0,
            kf=1.0,
            Dg=float(Dg[i]),
            Df=float(Df[i]),
        )
        W[i] = wi
        Wg[i] = wgi
        Wf[i] = wfi

    if not np.all(np.isfinite(W)) or np.any(W <= 0):
        raise RuntimeError("reference wall is not on a finite same-oriented lapse branch")

    rows = build_rows(r, pg, dpg, pf, dpf, Dg, Df, W)
    return {
        "rows": rows,
        "r": r,
        "W": W,
        "Wg": Wg,
        "Wf": Wf,
        "W_min": float(np.min(W)),
        "W_max": float(np.max(W)),
        "solution": sol,
        "beta": tuple(float(x) for x in beta),
        "interaction": interaction,
    }


def write_reference_wall_input(
    path: Path,
    *,
    n: int,
    delta_r: float,
    solve_points: int = 600,
    tol: float = 2.0e-7,
):
    """Generate and write a human-inspectable `input.binary=false` file."""
    result = reference_wall_rows(
        n=n,
        delta_r=delta_r,
        solve_points=solve_points,
        tol=tol,
    )
    write_text_input(Path(path), result["rows"])
    return result
