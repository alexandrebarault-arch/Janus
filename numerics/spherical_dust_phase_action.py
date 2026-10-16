"""Pressureless matter phase action in a native spherical conformal chart."""
from __future__ import annotations

import math


def native_conformal_dust_phase_density(
    *,
    scale_factor: float,
    conformal_H: float,
    r: float,
    rho: float,
    Phi: float,
    q: float,
    q_t: float,
    q_r: float,
    momentum: float,
) -> float:
    """Return the quadratic dust density per ``sin(theta)``.

    The native metric has conformal lapse/scale factor ``a`` and no radial
    shift.  ``q=delta phi / phi'`` uses the native conformal-time background
    field derivative.  For pressureless P(X), ``phi'`` carries one factor of
    the scale factor, hence the finite canonical combination is

    ``p (q_t + H q)``.

    The returned density includes the background spherical measure ``a^4 r^2``.
    Spatial metric perturbations do not enter this quadratic dust phase block:
    multiplying ``q_r^2`` by a first-order spatial metric perturbation would be
    cubic.
    """
    vals = (scale_factor, conformal_H, r, rho, Phi, q, q_t, q_r, momentum)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all dust phase inputs must be finite")
    if scale_factor <= 0.0 or r < 0.0 or rho <= 0.0:
        raise ValueError("require scale_factor>0, rho>0 and r>=0")

    a = float(scale_factor)
    rr = float(r)
    density = (
        float(momentum)*(float(q_t) + float(conformal_H)*float(q))
        - float(momentum)*float(Phi)
        + 0.5*float(rho)*float(Phi)**2
        - 0.5*float(rho)*float(q_r)**2
    )
    return float(a**4 * rr**2 * density)
