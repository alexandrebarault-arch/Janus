"""Finite-difference diagnostic for exported time-symmetric Lane-Emden constraints."""
from __future__ import annotations
import numpy as np


def constraint_residuals(
    r,
    psi_g,
    psi_f,
    Dg,
    Df,
    *,
    beta,
    interaction,
    kappa_g=1.0,
    kappa_f=1.0,
):
    r = np.asarray(r, dtype=float)
    pg = np.asarray(psi_g, dtype=float)
    pf = np.asarray(psi_f, dtype=float)
    dg = np.asarray(Dg, dtype=float)
    df = np.asarray(Df, dtype=float)
    n = len(r)
    if n < 5 or any(x.shape != (n,) for x in (pg, pf, dg, df)):
        raise ValueError("all profiles must be same-length 1D arrays with at least 5 points")
    h = np.diff(r)
    if not np.allclose(h, h[0], rtol=1e-10, atol=1e-14):
        raise ValueError("diagnostic requires a uniform radial grid")
    dr = float(h[0])
    if dr <= 0 or np.any(r <= 0) or np.any(pg <= 0) or np.any(pf <= 0):
        raise ValueError("invalid radial grid or conformal factor")

    b0, b1, b2, b3, b4 = (float(x) for x in beta)
    ug = (
        b0 * pg**6
        + 3 * b1 * pf**2 * pg**4
        + 3 * b2 * pf**4 * pg**2
        + b3 * pf**6
    )
    uf = (
        b1 * pg**6
        + 3 * b2 * pf**2 * pg**4
        + 3 * b3 * pf**4 * pg**2
        + b4 * pf**6
    )

    sl = slice(1, -1)
    dpg = (pg[2:] - pg[:-2]) / (2 * dr)
    dpf = (pf[2:] - pf[:-2]) / (2 * dr)
    ddpg = (pg[2:] - 2 * pg[1:-1] + pg[:-2]) / dr**2
    ddpf = (pf[2:] - 2 * pf[1:-1] + pf[:-2]) / dr**2
    lapg = ddpg + 2 * dpg / r[1:-1]
    lapf = ddpf + 2 * dpf / r[1:-1]
    rg = 4 * pg[sl] * lapg + float(kappa_g) * (
        float(interaction) * ug[sl] + dg[sl]
    )
    rf = 4 * pf[sl] * lapf + float(kappa_f) * (
        float(interaction) * uf[sl] + df[sl]
    )
    return rg, rf
