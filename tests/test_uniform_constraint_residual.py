import numpy as np

from numerics.uniform_constraint_residual import constraint_residuals


def manufactured(n, dr, a=1e-4):
    r = (np.arange(n) + 0.5) * dr
    pg = 1 + a * r**4
    pf = np.ones_like(r)
    Dg = -80 * a * r**2 * pg
    Df = np.zeros_like(r)
    return r, pg, pf, Dg, Df


def test_second_order_residual_converges_for_manufactured_solution():
    vals = []
    for n, dr in [(100, 0.1), (200, 0.05), (400, 0.025)]:
        r, pg, pf, Dg, Df = manufactured(n, dr)
        rg, rf = constraint_residuals(
            r,
            pg,
            pf,
            Dg,
            Df,
            beta=(0, 0, 0, 0, 0),
            interaction=0,
            kappa_g=1,
            kappa_f=1,
        )
        vals.append(max(np.max(np.abs(rg)), np.max(np.abs(rf))))
    assert vals[0] > vals[1] > vals[2]
    assert vals[0] / vals[1] > 3.5
    assert vals[1] / vals[2] > 3.5
