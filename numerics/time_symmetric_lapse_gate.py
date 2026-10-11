"""Time-symmetric initial lapse-ratio diagnostic for JANUS-R.

Specializes the pinned nubirel/bim-solver standard-3+1 lapse factors to
p=K=KD=S=tau=0 and adds the independently derived f-dust W2 terms.
This is an initial-slice diagnostic only, not a time evolution.
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


def _gW0(r, Ag, Af, Bg, R, gDB, fDB, b1, b2, b3):
    P = b1 + R * (2 * b2 + b3 * R)
    t1 = -4 * fDB**2 * Bg**2 * (b1 + b2 * R) ** 2 * Ag**3 * R**3
    a = (
        -3 * b1**2
        - 4 * b2**2 * R**2
        + b3**2 * R**4
        - 6 * b1 * b2 * R
        + 2 * b3 * R**2 * (b1 + b2 * R)
    )
    c = -(b2 * R * (2 * b2 + 3 * b3 * R)) - b1 * (3 * b2 + 4 * b3 * R)
    inner1 = (
        Bg**2 * gDB**2 * a
        + Ag**2 * (b1 - b3 * R**2) * P
        + 2 * fDB * gDB * Bg**2 * R * c
    )
    d = (b2 + b3 * R) * (3 * b1 + R * (2 * b2 - b3 * R))
    inner2 = Ag**2 * (-b1 + b3 * R**2) * P + Bg**2 * gDB**2 * R * d
    e = (
        b1**2
        + 5 * b1 * R * (b2 + b3 * R)
        + b2 * R**2 * (2 * b2 + 3 * b3 * R)
    )
    f = 2 * (b1 - b3 * R**2) * (b1 + b2 * R) + (b1 + 2 * b2 * R) * P
    inner3 = fDB * e + 2 * gDB * f
    return -R * (
        t1
        + Ag * Af**2 * R * inner1
        + Af**3 * inner2
        + Af * fDB * Ag**2 * Bg**2 * R**2 * inner3
    )


def _fW0(r, Ag, Af, Bg, R, gDB, fDB, b1, b2, b3):
    P = b1 + R * (2 * b2 + b3 * R)
    q = b2 + b3 * R
    t1 = Af**2 * (
        -4 * Bg**2 * gDB**2 * R**2 * q**2 * (Af + Ag * R)
        + Ag
        * P
        * (
            Bg**2 * gDB**2 * R**2 * (3 * b2 + 5 * b3 * R)
            - Ag * (-b1 + b3 * R**2) * (-Af + Ag * R)
        )
    )
    c = b2 * R * (2 * b2 + 3 * b3 * R) + b1 * (3 * b2 + 4 * b3 * R)
    t2 = -2 * Af * fDB * Ag * gDB * Bg**2 * R**3 * (
        Ag * c + Af * (-4 * q**2 + b3 * P)
    )
    e = (
        b1**2
        + 2 * b1 * R * (b2 + b3 * R)
        - R**2 * (4 * b2**2 + 3 * b3**2 * R**2 + 6 * b2 * b3 * R)
    )
    h = -(b1 + b2 * R) * (b1 - R * (2 * b2 + 3 * b3 * R))
    t3 = fDB**2 * Ag**2 * Bg**2 * R**2 * (Af * e + Ag * R * h)
    return t1 + t2 + t3


def _gW2_upstream_rest(Ag, Af, Bg, R, b0, b1, b2, b3, b4, kg, kf, Dg):
    """Pinned upstream gW2 at p=K=KD=S=tau=0."""
    P = b1 + R * (2 * b2 + b3 * R)
    Gf = (
        -b1**2
        + 2 * b1 * R * (b2 + R * (3 * b3 + b4 * R))
        + R**2
        * (6 * b2**2 + 3 * b3**2 * R**2 + 2 * b2 * R * (6 * b3 + b4 * R))
    )
    A = (
        0.5
        * kf
        * Af**2
        * Ag**2
        * Bg**2
        * P
        * (6 * Ag * R * (b1 + b2 * R) * P + Af * Gf)
    )
    Gg = (
        -2 * b0 * b2
        + b3**2 * R**4
        - 3 * (b1**2 + 2 * b2**2 * R**2 + 4 * b1 * b2 * R)
        - 2 * b3 * R * (b0 + R * (3 * b1 + b2 * R))
    )
    B = (
        0.5
        * kg
        * Ag
        * Af**2
        * R**2
        * P
        * (
            -2 * Ag**2 * Bg**2 * (2 * b0 - b3 * R**3 + 3 * b1 * R) * (b1 + b2 * R)
            + Ag * (-Dg * (b1 - b3 * R**2) + Af * Bg**2 * Gg)
        )
    )
    # Important: upstream C++ is `-A - B + (extrinsic block)`, not `-(A-B+...)`.
    return -A - B


def _fW2_upstream_rest(Ag, Af, Bg, R, b0, b1, b2, b3, b4, kg, kf, Dg):
    """Pinned upstream fW2 at p=K=KD=S=tau=0."""
    P = b1 + R * (2 * b2 + b3 * R)
    q = b2 + b3 * R
    F = (
        3 * b1**2
        + 2 * b2 * (b0 + 3 * b2 * R**2)
        - b3**2 * R**4
        + 2 * b3 * (b0 + b2 * R**2) * R
        + 6 * b1 * R * (2 * b2 + b3 * R)
    )
    A = (
        0.5
        * kg
        * Af**2
        * Ag**2
        * R**2
        * P
        * (Ag * Bg**2 * F + 2 * q * (Dg + 3 * Af * Bg**2 * P))
    )
    H = (
        -b1**2
        + 2 * b1 * R * (b2 + R * (3 * b3 + b4 * R))
        + R**2
        * (6 * b2**2 + 3 * b3**2 * R**2 + 2 * b2 * R * (6 * b3 + b4 * R))
    )
    B = (
        0.5
        * kf
        * Af
        * Ag**2
        * Bg**2
        * P
        * (Af * (2 * Af * q * (-b1 + R**2 * (3 * b3 + 2 * b4 * R)) + Ag * H))
    )
    return A - B


def _f_matter_additions(Ag, Af, R, b1, b2, b3, kf, Df):
    """Exact f-dust additions derived by published sector duality at rest."""
    P = b1 + 2 * b2 * R + b3 * R**2
    Qf = b1 + b2 * R
    C = b1 - b3 * R**2
    dWg = -kf * Ag**2 * Af**2 * P * Qf * Df / R**5
    dWf = +kf * Ag**2 * Af**2 * P * C * Df / (2 * R**6)
    return dWg, dWf


def time_symmetric_w(
    *, r, Ag, Af, Bg, Bf, gDB, fDB,
    b0, b1, b2, b3, b4, kg, kf, Dg, Df
):
    """Return `(W=-Wf/Wg, Wg, Wf)` for p=K=KD=S=tau=0."""
    R = Bf / Bg
    Wg0 = _gW0(r, Ag, Af, Bg, R, gDB, fDB, b1, b2, b3)
    Wf0 = _fW0(r, Ag, Af, Bg, R, gDB, fDB, b1, b2, b3)
    Wg2 = _gW2_upstream_rest(Ag, Af, Bg, R, b0, b1, b2, b3, b4, kg, kf, Dg)
    Wf2 = _fW2_upstream_rest(Ag, Af, Bg, R, b0, b1, b2, b3, b4, kg, kf, Dg)
    dWg, dWf = _f_matter_additions(Ag, Af, R, b1, b2, b3, kf, Df)
    Wg = Wg0 + r * r * (Wg2 + dWg)
    Wf = Wf0 + r * r * (Wf2 + dWf)
    return -Wf / Wg, Wg, Wf


def reference_initial_lapse_profile(*, points=420, tol=2.0e-7):
    """Evaluate the reference Gate-A0 Lane–Emden slice in the lapse relation."""
    beta = flat_beta_from123(1.0, -0.2, 0.0)
    interaction = 0.02
    params = Params(beta=beta, interaction=interaction, kappa_g=1.0, kappa_f=1.0)
    Dg = lambda r: shell_profile(r, 0.025, 5.0, 1.0)
    Df = lambda r: gaussian_profile(r, 0.04, 2.0)
    sol = solve_initial_data(params, Dg, Df, r_max=25.0, points=points, tol=tol)

    r = sol.r
    pg = sol.psi_g
    pf = sol.psi_f
    dpg = np.gradient(pg, r, edge_order=2)
    dpf = np.gradient(pf, r, edge_order=2)

    Ag = Bg = pg**2
    Af = Bf = pf**2
    gDB = 2 * dpg / pg
    fDB = 2 * dpf / pf
    b = np.asarray(beta) * interaction

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

    return {
        "solution": sol,
        "W": np.asarray(W),
        "Wg": np.asarray(Wg),
        "Wf": np.asarray(Wf),
    }
