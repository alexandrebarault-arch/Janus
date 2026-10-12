"""Connected-root continuation for the Aoki-Maeda-Namba nonlinear scalar gate.

This diagnostic varies an anti-correlated two-matter source at fixed H^2 and
tracks the real scalar root continuously connected to a chosen starting root.
It is a branch-topology test only: it does not by itself prove ghost/gradient
stability or solve the full time-dependent nonlinear system.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np

from numerics.aoki_scalar_polynomial import Params, real_roots


@dataclass(frozen=True)
class ContinuationResult:
    last_source: float
    last_mu: float
    failed_at: float | None


def connected_branch_until(
    *,
    beta2: float,
    beta3: float,
    h2: float,
    start_mu: float,
    source_max: float,
    source_step: float,
    mg2: float = 0.5,
    mf2: float = 0.5,
    w: float = 0.0,
    max_jump: float = 0.02,
) -> ContinuationResult:
    """Track an anti-correlated source: source_g=-s, source_f=+s.

    A branch is flagged as lost when no admissible real root remains close
    enough to the previous continuation point. The finite-step `max_jump`
    criterion is a numerical topology diagnostic, not a physical singularity
    theorem; suspected endpoints should be refined with smaller source_step and
    the full dynamical equations.
    """
    if source_step <= 0 or source_max < 0:
        raise ValueError("source_step must be positive and source_max non-negative")

    previous = float(start_mu)
    last_source = 0.0
    last_mu = previous

    for s in np.arange(0.0, source_max + 0.5 * source_step, source_step):
        p = Params(
            beta2=beta2,
            beta3=beta3,
            mg2=mg2,
            mf2=mf2,
            H2=h2,
            w=w,
            source_g=-float(s),
            source_f=float(s),
        )
        roots = real_roots(p)
        if len(roots) == 0:
            return ContinuationResult(last_source, last_mu, float(s))

        mu = float(roots[np.argmin(np.abs(roots - previous))])
        if s > 0 and abs(mu - previous) > max_jump:
            return ContinuationResult(last_source, last_mu, float(s))

        last_source = float(s)
        last_mu = mu
        previous = mu

    return ContinuationResult(last_source, last_mu, None)
