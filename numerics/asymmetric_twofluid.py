"""Transparent EdS two-fluid control model for JANUS-R.

Not a full bimetric FLRW perturbation solver. It only tests how unequal
background weights break the exactly symmetric common/relative decomposition
in the V1 quasi-static kernel.
"""

from __future__ import annotations

import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def coupling_matrix(f_g: float, x: float) -> np.ndarray:
    if not 0.0 < f_g < 1.0:
        raise ValueError("f_g must lie strictly between 0 and 1")
    if not 0.0 <= x <= 1.0:
        raise ValueError("x must lie in [0,1]")
    f_f = 1.0 - f_g
    q_self = 1.0 + 4.0 * x / 3.0
    q_cross = 1.0 - 4.0 * x / 3.0
    return np.array(
        [
            [f_g * q_self, f_f * q_cross],
            [f_g * q_cross, f_f * q_self],
        ],
        dtype=float,
    )


def eds_growth_exponents(f_g: float, x: float) -> np.ndarray:
    vals = np.linalg.eigvals(coupling_matrix(f_g, x)).real
    return np.array(
        [(-1.0 + math.sqrt(1.0 + 24.0 * mu)) / 4.0 for mu in vals]
    )


def integrate_equal_seed(
    f_g: float,
    x: float,
    z_start: float,
    seed: float = 1.0e-5,
) -> dict[str, float]:
    if z_start < 0:
        raise ValueError("z_start must be non-negative")
    matrix = coupling_matrix(f_g, x)

    def rhs(_n: float, state: np.ndarray) -> np.ndarray:
        dg, vg, df, vf = state
        src = 1.5 * matrix @ np.array([dg, df])
        # EdS: 2 + d ln H/d ln a = 1/2.
        return np.array([vg, src[0] - 0.5 * vg, vf, src[1] - 0.5 * vf])

    n_start = -math.log1p(z_start)
    sol = solve_ivp(
        rhs,
        (n_start, 0.0),
        (seed, seed, seed, seed),
        rtol=1e-10,
        atol=1e-13,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    dg, vg, df, vf = sol.y[:, -1]
    return {
        "delta_g": float(dg),
        "velocity_g": float(vg),
        "delta_f": float(df),
        "velocity_f": float(vf),
    }


def critical_visible_fraction_for_twin_sign_flip(
    *,
    z_start: float,
    x: float = 1.0,
    f_min: float = 0.500001,
    f_max: float = 0.999999,
) -> float:
    """Return f_g for which an initially common seed ends with delta_f=0.

    For a negative common seed (a proto-void), f_g above this threshold makes
    the final twin perturbation positive: true anti-correlation. This is only
    an EdS constant-x upper-bound diagnostic.
    """

    def final_twin(f_g: float) -> float:
        return integrate_equal_seed(
            f_g=f_g, x=x, z_start=z_start, seed=1.0
        )["delta_f"]

    lo, hi = final_twin(f_min), final_twin(f_max)
    if lo == 0.0:
        return f_min
    if hi == 0.0:
        return f_max
    if lo * hi > 0.0:
        raise ValueError("no twin sign-flip threshold in the requested f_g interval")
    return float(brentq(final_twin, f_min, f_max, xtol=1e-12, rtol=1e-12))


def critical_unscreened_strength_for_twin_sign_flip(
    *,
    f_g: float,
    z_start: float,
    x_min: float = 0.0,
    x_max: float = 1.0,
) -> float:
    """Return x for which an initially common seed ends with delta_f=0."""

    def final_twin(x: float) -> float:
        return integrate_equal_seed(
            f_g=f_g, x=x, z_start=z_start, seed=1.0
        )["delta_f"]

    lo, hi = final_twin(x_min), final_twin(x_max)
    if lo == 0.0:
        return x_min
    if hi == 0.0:
        return x_max
    if lo * hi > 0.0:
        raise ValueError("no twin sign-flip threshold in the requested x interval")
    return float(brentq(final_twin, x_min, x_max, xtol=1e-12, rtol=1e-12))
