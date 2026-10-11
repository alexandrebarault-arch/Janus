"""Adiabatic cosmological continuation diagnostic for the AMN nonlinear scalar.

This is a branch-topology test, not a full time-dependent solution. It fixes
the dimensional-source ambiguity of the earlier fixed-H continuation by
scaling source terms with H^2 and a bounded density-contrast history.

The default matter-era toy model uses

    H^2(a) = H0_proxy^2 a^-3

and

    source_g = N_g H^2 delta_g(a),
    source_f = N_f H^2 delta_f(a).

For a matter-dominated GR-like regime, N~3 is the natural order of magnitude
because kappa^2 rho ~ 3 H^2. The exact normalizations in a full two-metric
background are time dependent and must eventually come from the FLRW solver.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.aoki_scalar_polynomial import Params, real_roots


@dataclass(frozen=True)
class TrajectorySpec:
    beta2: float
    beta3: float
    start_mu: float
    h2_today: float = 0.01
    delta_g0: float = -0.8
    delta_f0: float = 1.0
    source_norm_g: float = 3.0
    source_norm_f: float = 3.0
    growth_power: float = 1.0
    a_min: float = 0.01
    points: int = 500
    mg2: float = 0.5
    mf2: float = 0.5
    w: float = 0.0
    max_jump: float = 0.15


@dataclass(frozen=True)
class TrajectoryResult:
    last_a: float
    last_mu: float
    failed_at: float | None
    min_mu: float
    max_mu: float


def source_to_contrast_ratio(source: float, h2: float, norm: float) -> float:
    """Return delta implied by source = norm * H^2 * delta."""
    if h2 <= 0 or norm <= 0:
        raise ValueError("h2 and norm must be positive")
    return source / (norm * h2)


def _contrast(a: float, delta0: float, power: float) -> float:
    return delta0 * a**power


def track_case(spec: TrajectorySpec) -> TrajectoryResult:
    """Track the real AMN scalar root along a toy matter-era trajectory.

    A failure means that no nearby real root can be followed with the chosen
    discretization. Survival does not prove ghost/gradient stability.
    """
    if not (-1.0 <= spec.delta_g0 <= 0.0):
        raise ValueError("visible void contrast delta_g0 must lie in [-1, 0]")
    if spec.delta_f0 < 0:
        raise ValueError("twin overdensity delta_f0 must be non-negative")
    if spec.h2_today <= 0 or spec.a_min <= 0 or spec.a_min > 1:
        raise ValueError("invalid H0/a_min")

    previous = float(spec.start_mu)
    values: list[float] = []
    last_a = spec.a_min
    a_values = np.geomspace(spec.a_min, 1.0, spec.points)

    for a in a_values:
        h2 = spec.h2_today * a**-3
        delta_g = _contrast(a, spec.delta_g0, spec.growth_power)
        delta_f = _contrast(a, spec.delta_f0, spec.growth_power)

        p = Params(
            beta2=spec.beta2,
            beta3=spec.beta3,
            mg2=spec.mg2,
            mf2=spec.mf2,
            H2=h2,
            w=spec.w,
            source_g=spec.source_norm_g * h2 * delta_g,
            source_f=spec.source_norm_f * h2 * delta_f,
        )
        roots = real_roots(p)
        if len(roots) == 0:
            return TrajectoryResult(
                last_a, previous, float(a), min(values), max(values)
            )

        mu = float(roots[np.argmin(np.abs(roots - previous))])
        if values and abs(mu - previous) > spec.max_jump:
            return TrajectoryResult(
                last_a, previous, float(a), min(values), max(values)
            )

        values.append(mu)
        previous = mu
        last_a = float(a)

    return TrajectoryResult(last_a, previous, None, min(values), max(values))
