from __future__ import annotations

import numpy as np

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    shell_profile,
    solve_initial_data,
)
from numerics.reference_bim_solver_twin_input import cubic_resample
from numerics.bim_solver_twin_input import build_rows, uniform_centers
from numerics.time_symmetric_lapse_gate import time_symmetric_w


def _control_rows(
    *,
    beta,
    Dg_fn,
    Df_fn,
    interaction: float,
    n: int,
    delta_r: float,
    solve_points: int,
    tol: float,
):
    if n < 4 or delta_r <= 0 or solve_points < 20:
        raise ValueError("invalid grid or constraint-solver resolution")
    beta = tuple(float(x) for x in beta)
    if len(beta) != 5 or not np.all(np.isfinite(beta)):
        raise ValueError("beta must contain five finite coefficients")

    p = Params(beta=beta, interaction=float(interaction), kappa_g=1.0, kappa_f=1.0)
    r_outer = n * float(delta_r)
    sol = solve_initial_data(
        p,
        Dg_fn,
        Df_fn,
        r_max=r_outer,
        points=solve_points,
        tol=tol,
    )
    if not sol.success:
        raise RuntimeError("control initial-constraint solve failed")
    if np.any(np.asarray(sol.psi_g) <= 0) or np.any(np.asarray(sol.psi_f) <= 0):
        raise RuntimeError("control solve produced a non-positive conformal factor")

    r = uniform_centers(n, delta_r)
    sr = np.asarray(sol.r, dtype=float)
    pg, dpg = cubic_resample(sr, np.asarray(sol.psi_g, dtype=float), r)
    pf, dpf = cubic_resample(sr, np.asarray(sol.psi_f, dtype=float), r)
    Dg = np.asarray(Dg_fn(r), dtype=float)
    Df = np.asarray(Df_fn(r), dtype=float)

    Ag = Bg = pg**2
    Af = Bf = pf**2
    gDB = 2.0 * dpg / pg
    fDB = 2.0 * dpf / pf
    runtime_b = tuple(float(x) * float(interaction) for x in beta)

    W = np.empty(n, dtype=float)
    for i, rr in enumerate(r):
        W[i], _, _ = time_symmetric_w(
            r=float(rr),
            Ag=float(Ag[i]),
            Af=float(Af[i]),
            Bg=float(Bg[i]),
            Bf=float(Bf[i]),
            gDB=float(gDB[i]),
            fDB=float(fDB[i]),
            b0=runtime_b[0],
            b1=runtime_b[1],
            b2=runtime_b[2],
            b3=runtime_b[3],
            b4=runtime_b[4],
            kg=1.0,
            kf=1.0,
            Dg=float(Dg[i]),
            Df=float(Df[i]),
        )
    if not np.all(np.isfinite(W)) or np.any(W <= 0.0):
        raise RuntimeError("control slice is not on a finite same-oriented lapse branch")

    return {
        "rows": build_rows(r, pg, dpg, pf, dpf, Dg, Df, W),
        "r": r,
        "W": W,
        "W_min": float(np.min(W)),
        "W_max": float(np.max(W)),
        "solution": sol,
        "beta": beta,
        "interaction": float(interaction),
        "runtime_b": runtime_b,
    }


def reference_g_only_control_rows(
    *, n: int, delta_r: float, solve_points: int = 600, tol: float = 2.0e-7
):
    beta = flat_beta_from123(1.0, -0.2, 0.0)
    source = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    zero = lambda r: np.zeros_like(np.asarray(r, dtype=float))
    return _control_rows(
        beta=beta,
        Dg_fn=source,
        Df_fn=zero,
        interaction=0.02,
        n=n,
        delta_r=delta_r,
        solve_points=solve_points,
        tol=tol,
    )


def reference_f_only_dual_control_rows(
    *, n: int, delta_r: float, solve_points: int = 600, tol: float = 2.0e-7
):
    beta = flat_beta_from123(1.0, -0.2, 0.0)
    dual_beta = tuple(reversed(beta))
    source = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    zero = lambda r: np.zeros_like(np.asarray(r, dtype=float))
    return _control_rows(
        beta=dual_beta,
        Dg_fn=zero,
        Df_fn=source,
        interaction=0.02,
        n=n,
        delta_r=delta_r,
        solve_points=solve_points,
        tol=tol,
    )
