"""Targeted initial-slice lapse-basin diagnostic for JANUS-R.

This is deliberately not an unconstrained parameter optimizer. It solves the
Gate-A0 time-symmetric two-matter constraints for one wall configuration and
then evaluates the exact specialized secondary-constraint lapse ratio.
"""
from __future__ import annotations

import numpy as np

from numerics.twin_lane_emden_initial import (
    Params,
    flat_beta_from123,
    gaussian_profile,
    shell_profile,
    solve_initial_data,
)
from numerics.time_symmetric_lapse_gate import time_symmetric_w


def _zero_brackets(r, values):
    r = np.asarray(r)
    values = np.asarray(values)
    idx = np.where(np.signbit(values[:-1]) != np.signbit(values[1:]))[0]
    return [(float(r[i]), float(r[i + 1])) for i in idx]


def evaluate_wall(
    *,
    beta1=1.0,
    beta2=-0.2,
    beta3=0.0,
    interaction=0.02,
    f_amp=0.04,
    f_sigma=2.0,
    g_amp=0.025,
    g_radius=5.0,
    g_sigma=1.0,
    r_max=25.0,
    points=260,
    tol=8.0e-7,
):
    """Solve one initial wall and classify its same-oriented lapse branch."""
    beta = flat_beta_from123(beta1, beta2, beta3)
    params = Params(beta=beta, interaction=interaction, kappa_g=1.0, kappa_f=1.0)
    Dg = lambda r: shell_profile(r, g_amp, g_radius, g_sigma)
    Df = lambda r: gaussian_profile(r, f_amp, f_sigma)
    sol = solve_initial_data(params, Dg, Df, r_max=r_max, points=points, tol=tol)

    result = {"bvp_success": bool(sol.success), "solution": sol}
    if not sol.success or sol.min_psi_g <= 0 or sol.min_psi_f <= 0:
        result.update(admissible=False, reason="initial_constraints")
        return result

    r = sol.r
    pg = sol.psi_g
    pf = sol.psi_f
    dpg = np.gradient(pg, r, edge_order=2)
    dpf = np.gradient(pf, r, edge_order=2)
    Ag = Bg = pg**2
    Af = Bf = pf**2
    gDB = 2 * dpg / pg
    fDB = 2 * dpf / pf
    b = np.asarray(beta, dtype=float) * interaction

    W, Wg, Wf = [], [], []
    for i, rr in enumerate(r):
        wi, wgi, wfi = time_symmetric_w(
            r=float(rr),
            Ag=float(Ag[i]),
            Af=float(Af[i]),
            Bg=float(Bg[i]),
            Bf=float(Bf[i]),
            gDB=float(gDB[i]),
            fDB=float(fDB[i]),
            b0=float(b[0]), b1=float(b[1]), b2=float(b[2]), b3=float(b[3]), b4=float(b[4]),
            kg=1.0, kf=1.0,
            Dg=float(Dg(rr)), Df=float(Df(rr)),
        )
        W.append(wi)
        Wg.append(wgi)
        Wf.append(wfi)

    W = np.asarray(W)
    Wg = np.asarray(Wg)
    Wf = np.asarray(Wf)
    finite = bool(np.all(np.isfinite(W)))
    positive = finite and bool(np.nanmin(W) > 0.0)

    result.update(
        r=r,
        W=W,
        Wg=Wg,
        Wf=Wf,
        W_min=float(np.nanmin(W)),
        W_max=float(np.nanmax(W)),
        W_outer=float(W[-1]),
        Wg_zero_brackets=_zero_brackets(r, Wg),
        Wf_zero_brackets=_zero_brackets(r, Wf),
        admissible=positive,
        reason=None if positive else "lapse_branch",
    )
    return result
