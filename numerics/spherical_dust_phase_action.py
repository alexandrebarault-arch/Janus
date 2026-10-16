"""Pressureless matter phase action in native/pulled-back spherical conformal charts."""
from __future__ import annotations

import math
import numpy as np


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


def pulled_back_conformal_dust_phase_density(
    *,
    scale_factor: float,
    conformal_H: float,
    native_r: float,
    rho: float,
    Phi: float,
    q: float,
    q_t_common: float,
    q_r_common: float,
    momentum: float,
    jacobian,
) -> float:
    """Pull one native dust sector into a common radial chart.

    ``jacobian`` is ``d(eta_native,r_native)/d(eta_common,r_common)``.
    Scalar-field derivatives therefore transform as covectors,

    ``grad_native(q) = jacobian^{-T} grad_common(q)``,

    while the integration measure contributes ``abs(det(jacobian))``.
    """
    J = np.asarray(jacobian, dtype=float)
    if J.shape != (2, 2) or not np.all(np.isfinite(J)):
        raise ValueError("jacobian must be a finite 2x2 matrix")
    determinant = float(np.linalg.det(J))
    if abs(determinant) <= 1e-14:
        raise np.linalg.LinAlgError("dust pullback jacobian is singular")
    grad_common = np.array([q_t_common, q_r_common], dtype=float)
    grad_native = np.linalg.solve(J.T, grad_common)
    native = native_conformal_dust_phase_density(
        scale_factor=scale_factor,
        conformal_H=conformal_H,
        r=native_r,
        rho=rho,
        Phi=Phi,
        q=q,
        q_t=float(grad_native[0]),
        q_r=float(grad_native[1]),
        momentum=momentum,
    )
    return float(abs(determinant)*native)
