"""Self-consistent late-transition upper-bound diagnostic for JANUS-R.

This toy model couples two ingredients already used separately:

1. the low-energy Higuchi crossing m_eff^2 ~= 2 H^2, which fixes an
   approximate transition redshift for a chosen Compton length; and
2. the quasi-static two-fluid kernel x(k,a)=k^2/(k^2+a^2 m_eff^2), evolved
   after that transition on an Einstein-de Sitter background.

It is intentionally optimistic: once the transition is reached the linear
kernel is used without additional screening. The output is therefore a useful
upper bound / feasibility diagnostic, not a prediction.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from numerics.asymmetric_twofluid import coupling_matrix
from numerics.higuchi_scale_window import (
    mass_ratio_from_compton_mpc,
    matter_higuchi_crossing_redshift,
)


@dataclass(frozen=True)
class TransitionResult:
    z_transition: float
    q0: float
    x_today: float
    delta_g: float
    delta_f: float
    velocity_g: float
    velocity_f: float


def integrate_transition(
    *,
    f_g: float,
    structure_mpc: float,
    lambda_mpc: float,
    seed: float = 1.0,
    k_factor: float = math.pi,
    h0_km_s_mpc: float = 70.0,
    omega_m0: float = 0.30,
) -> TransitionResult:
    """Evolve an initially common growing mode from the Higuchi crossing.

    `structure_mpc` is a comoving characteristic size and `k_factor/R` is used
    as its representative wavenumber. `k_factor=pi` is a conservative default
    for a compensated structure whose dominant radial mode is of order pi/R.
    """
    if structure_mpc <= 0 or lambda_mpc <= 0 or k_factor <= 0:
        raise ValueError("scales and k_factor must be positive")

    mass_ratio = mass_ratio_from_compton_mpc(
        lambda_mpc, h0_km_s_mpc=h0_km_s_mpc
    )
    z_transition = matter_higuchi_crossing_redshift(
        mass_ratio, omega_m0=omega_m0
    )
    if z_transition <= 0:
        raise ValueError("chosen mass does not give a positive matter-era crossing")

    q0 = k_factor * lambda_mpc / structure_mpc
    n_start = -math.log1p(z_transition)

    def rhs(n: float, state: np.ndarray) -> np.ndarray:
        a = math.exp(n)
        x = q0 * q0 / (q0 * q0 + a * a)
        matrix = coupling_matrix(f_g, x)
        dg, vg, df, vf = state
        src = 1.5 * matrix @ np.array([dg, df])
        return np.array([vg, src[0] - 0.5 * vg, vf, src[1] - 0.5 * vf])

    sol = solve_ivp(
        rhs,
        (n_start, 0.0),
        (seed, seed, seed, seed),
        rtol=1e-10,
        atol=1e-12,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    dg, vg, df, vf = sol.y[:, -1]
    x_today = q0 * q0 / (q0 * q0 + 1.0)
    return TransitionResult(
        z_transition=float(z_transition),
        q0=float(q0),
        x_today=float(x_today),
        delta_g=float(dg),
        delta_f=float(df),
        velocity_g=float(vg),
        velocity_f=float(vf),
    )


def sign_flip_band(
    *,
    f_g: float,
    structure_mpc: float,
    lambda_min: float = 5.0,
    lambda_max: float = 1000.0,
    samples: int = 240,
    **kwargs,
) -> tuple[float, float]:
    """Return the first finite lambda interval where final delta_f changes sign.

    The initial seed is positive. Inside the returned interval delta_f<0, so a
    negative common proto-void seed evolves into a positive twin overdensity.
    """
    if not (lambda_max > lambda_min > 0):
        raise ValueError("require lambda_max > lambda_min > 0")

    grid = np.geomspace(lambda_min, lambda_max, samples)

    def twin(lam: float) -> float:
        return integrate_transition(
            f_g=f_g,
            structure_mpc=structure_mpc,
            lambda_mpc=lam,
            **kwargs,
        ).delta_f

    vals = np.array([twin(float(lam)) for lam in grid])
    roots: list[float] = []
    for a, b, fa, fb in zip(grid[:-1], grid[1:], vals[:-1], vals[1:]):
        if fa == 0.0:
            roots.append(float(a))
        elif fa * fb < 0.0:
            roots.append(
                float(brentq(twin, float(a), float(b), xtol=1e-9, rtol=1e-10))
            )

    if len(roots) < 2:
        raise ValueError("no bounded sign-flip band found in scan interval")
    return roots[0], roots[1]


def common_band(
    *,
    f_g: float,
    structures_mpc: Iterable[float],
    **kwargs,
) -> tuple[float, float]:
    """Intersect sign-flip bands for multiple structure scales."""
    bands = [
        sign_flip_band(f_g=f_g, structure_mpc=float(r), **kwargs)
        for r in structures_mpc
    ]
    lo = max(b[0] for b in bands)
    hi = min(b[1] for b in bands)
    if lo >= hi:
        raise ValueError("no common sign-flip band across requested scales")
    return float(lo), float(hi)
