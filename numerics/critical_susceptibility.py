"""Compare twin-sector susceptibility directly with the healthy-branch margin.

This diagnostic combines two already independent pieces of JANUS-R V2:

1. the infinitesimal twin-sector top-hat response;
2. the De Felice et al. healthy-branch quantity W.

The goal is to test whether a large Janus-like response appears comfortably
inside the healthy branch or only as W approaches zero.  The latter is a
warning sign because the bimetric background analysis shows that the relative
lapse and time derivative of the metric ratio become singular when W crosses
zero, signalling exit from the EFT regime.
"""

from __future__ import annotations

from dataclasses import dataclass

from numerics.stability_mixing import higuchi_w_flat
from numerics.tophat_susceptibility import initial_twin_growth_slope
from numerics.two_matter_flrw import Model, j_mix
from numerics.two_matter_tophat import _background_history


@dataclass(frozen=True)
class SusceptibilityHealthPoint:
    z: float
    y: float
    h2: float
    w: float
    w_over_h2: float
    twin_growth_slope: float
    slope_times_w_over_h2: float


def susceptibility_health_point(
    m: Model,
    *,
    z: float,
    epsilon: float = 1.0e-5,
) -> SusceptibilityHealthPoint:
    """Evaluate twin susceptibility and W/H^2 at the same background epoch."""
    if z < 0.0:
        raise ValueError("z must be non-negative")
    if m.m2 is None:
        raise ValueError("model must be calibrated()")

    a = 1.0 / (1.0 + z)
    _, y_history, h_history, _ = _background_history(m, a, points=500)
    y = float(y_history[0])
    h2 = float(h_history[0] ** 2)
    j = float(j_mix(y, m.beta))
    w = float(
        higuchi_w_flat(
            m2=float(m.m2),
            alpha=m.alpha,
            y=y,
            j=j,
            h2=h2,
        )
    )
    w_over_h2 = w / h2
    slope = initial_twin_growth_slope(m, z=z, epsilon=epsilon)

    return SusceptibilityHealthPoint(
        z=z,
        y=y,
        h2=h2,
        w=w,
        w_over_h2=w_over_h2,
        twin_growth_slope=slope,
        slope_times_w_over_h2=slope * w_over_h2,
    )
