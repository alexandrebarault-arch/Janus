"""Convergence scan for reference twin-wall constraints after uniform-grid export."""
from __future__ import annotations
import numpy as np

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    gaussian_profile,
    shell_profile,
    solve_initial_data,
)
from numerics.uniform_constraint_residual import constraint_residuals
from numerics.reference_bim_solver_twin_input import cubic_resample


def scan_reference_constraints(
    *,
    n_values=(100, 200, 400),
    r_max: float = 25.0,
    solve_points: int = 800,
    tol: float = 1e-7,
):
    beta = flat_beta_from123(1.0, -0.2, 0.0)
    interaction = 0.02
    p = Params(beta=beta, interaction=interaction, kappa_g=1.0, kappa_f=1.0)
    Dg = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    Df = lambda r: gaussian_profile(r, 0.04, 2.0)
    sol = solve_initial_data(
        p,
        Dg,
        Df,
        r_max=r_max,
        points=solve_points,
        tol=tol,
        max_nodes=50000,
    )
    levels = []
    for n in n_values:
        if n < 8:
            raise ValueError("each n must be at least 8")
        dr = float(r_max) / int(n)
        r = (np.arange(int(n), dtype=float) + 0.5) * dr
        pg, _ = cubic_resample(sol.r, sol.psi_g, r)
        pf, _ = cubic_resample(sol.r, sol.psi_f, r)
        rg, rf = constraint_residuals(
            r,
            pg,
            pf,
            Dg(r),
            Df(r),
            beta=beta,
            interaction=interaction,
            kappa_g=1.0,
            kappa_f=1.0,
        )
        core_g = rg[2:-2] if len(rg) > 4 else rg
        core_f = rf[2:-2] if len(rf) > 4 else rf
        both = np.concatenate((core_g, core_f))
        levels.append(
            {
                "n": int(n),
                "dr": dr,
                "core_max": float(np.max(np.abs(both))),
                "core_rms": float(np.sqrt(np.mean(both**2))),
            }
        )
    return {
        "bvp_success": bool(sol.success),
        "bvp_residual": float(sol.max_constraint_residual),
        "bvp_nodes": int(len(sol.r)),
        "levels": levels,
    }
