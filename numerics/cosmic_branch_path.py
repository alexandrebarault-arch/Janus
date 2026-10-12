"""Adiabatic matter-era continuation through H~m for the Aoki-Maeda-Namba scalar root.

This is a branch-topology diagnostic, not a full nonlinear time evolution.
It evolves a proxy matter-era path with H^2 proportional to a^-3 and a
relative density contrast delta_rel proportional to a^p. The two matter
sources are taken anti-correlated:

    source_g = -s(a), source_f = +s(a),
    s(a) = source_coeff * H^2(a) * delta_rel(a).

The purpose is to test whether a root that is stable/interesting in the early
nonlinear GR-like phase can remain continuously connected to a late-time
bigravity root while the background curvature and perturbation source evolve
together.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.aoki_scalar_polynomial import Params, real_roots


@dataclass(frozen=True)
class CosmicPathResult:
    last_h2: float
    last_delta: float
    last_source: float
    last_mu: float
    failed_at_h2: float | None
    failure_reason: str | None


def track_matter_era_path(
    *,
    beta2: float,
    beta3: float,
    start_mu: float,
    h2_early: float,
    h2_late: float,
    delta_i: float,
    growth_exponent: float,
    steps: int = 1000,
    source_coeff: float = 1.0,
    mg2: float = 0.5,
    mf2: float = 0.5,
    w: float = 0.0,
    max_jump: float = 0.05,
) -> CosmicPathResult:
    """Track the nearest real scalar root along a matter-era proxy trajectory.

    Assumptions
    -----------
    - H^2 is used as the trajectory variable and decreases geometrically.
    - Matter-era scaling H^2 proportional to a^-3 gives
      a/a_i = (H_i^2/H^2)^(1/3).
    - The relative density contrast grows as delta_rel proportional to a^p.
    - Equal-magnitude anti-correlated matter sources are used as a Janus-like
      diagnostic: source_g=-s and source_f=+s.

    The finite-step jump criterion is a branch-topology diagnostic only. A
    detected jump means that this adiabatic root tracker cannot continue the
    same nearby real branch. It does not prove that the full time-dependent
    nonlinear field equations are singular.
    """
    if not (h2_early > h2_late > 0):
        raise ValueError("require h2_early > h2_late > 0")
    if delta_i < 0 or source_coeff < 0:
        raise ValueError("delta_i and source_coeff must be non-negative")
    if steps < 2:
        raise ValueError("steps must be >= 2")

    h2_values = np.geomspace(h2_early, h2_late, steps)
    previous = float(start_mu)
    last_h2 = float(h2_early)
    last_delta = float(delta_i)
    last_source = float(source_coeff * h2_early * delta_i)
    last_mu = previous

    for h2 in h2_values:
        # In the matter-era proxy H^2 proportional to a^-3.
        a_ratio = (h2_early / h2) ** (1.0 / 3.0)
        delta = delta_i * a_ratio**growth_exponent
        source = source_coeff * h2 * delta

        roots = real_roots(
            Params(
                beta2=beta2,
                beta3=beta3,
                mg2=mg2,
                mf2=mf2,
                H2=float(h2),
                w=w,
                source_g=-float(source),
                source_f=float(source),
            )
        )
        if len(roots) == 0:
            return CosmicPathResult(
                last_h2,
                last_delta,
                last_source,
                last_mu,
                float(h2),
                "no_real_root",
            )

        mu = float(roots[np.argmin(np.abs(roots - previous))])
        if h2 != h2_values[0] and abs(mu - previous) > max_jump:
            return CosmicPathResult(
                last_h2,
                last_delta,
                last_source,
                last_mu,
                float(h2),
                f"root_jump:{previous:.9g}->{mu:.9g}",
            )

        last_h2 = float(h2)
        last_delta = float(delta)
        last_source = float(source)
        last_mu = mu
        previous = mu

    return CosmicPathResult(
        last_h2,
        last_delta,
        last_source,
        last_mu,
        None,
        None,
    )
