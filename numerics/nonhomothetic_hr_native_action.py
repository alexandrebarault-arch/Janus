"""Exact Hassan-Rosen interaction density from two native spherical metric charts.

The two radial 2x2 metric blocks are specified in their own native coordinates.
``jacobian_g`` and ``jacobian_f`` are ``d x_native / d x_common``.  Angular
coordinates are shared.  The returned quantity is the standard-beta HR action
density per ``sin(theta)`` in the common radial chart.
"""
from __future__ import annotations

import math
import numpy as np


def _matrix(name: str, value) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.shape != (2, 2) or not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must be a finite 2x2 matrix")
    return arr


def native_hr_potential_density(
    *,
    g_radial_native,
    f_radial_native,
    g_angular_native: float,
    f_angular_native: float,
    jacobian_g,
    jacobian_f,
    betas,
    m2: float,
    Mg2: float,
) -> float:
    """Return ``m^2 Mg^2 sqrt(-g) sum beta_n e_n(sqrt(g^-1 f))``.

    The density is reduced by the common ``sin(theta)`` factor.  No background
    subtraction or De-Felice sign conversion is applied here; this is the exact
    standard-beta native-chart interaction scalar used as a nonlinear audit
    primitive.
    """
    gn = _matrix("g_radial_native", g_radial_native)
    fn = _matrix("f_radial_native", f_radial_native)
    Jg = _matrix("jacobian_g", jacobian_g)
    Jf = _matrix("jacobian_f", jacobian_f)
    beta = tuple(float(x) for x in betas)
    vals = (g_angular_native, f_angular_native, m2, Mg2, *beta)
    if len(beta) != 5 or not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("invalid native HR inputs")
    if g_angular_native <= 0.0 or f_angular_native <= 0.0:
        raise ValueError("angular metric coefficients must be positive")
    if abs(np.linalg.det(Jg)) <= 1e-14 or abs(np.linalg.det(Jf)) <= 1e-14:
        raise np.linalg.LinAlgError("native coordinate Jacobian is singular")

    gc = Jg.T @ gn @ Jg
    fc = Jf.T @ fn @ Jf
    det_g = float(np.linalg.det(gc))
    if det_g >= 0.0:
        raise ValueError("common g radial block must remain Lorentzian")

    A = np.linalg.solve(gc, fc)
    det_A = float(np.linalg.det(A))
    tr_A = float(np.trace(A))
    if det_A <= 0.0:
        raise ValueError("radial g^-1 f determinant must be positive")
    sqrt_det = math.sqrt(det_A)
    denominator = tr_A + 2.0*sqrt_det
    if denominator <= 0.0:
        raise ValueError("principal radial square root is not real")
    S = (A + sqrt_det*np.eye(2)) / math.sqrt(denominator)
    radial_trace = float(np.trace(S))
    radial_det = float(np.linalg.det(S))
    ell = math.sqrt(float(f_angular_native/g_angular_native))

    elementary = np.array([
        1.0,
        radial_trace + 2.0*ell,
        radial_det + 2.0*ell*radial_trace + ell*ell,
        2.0*ell*radial_det + ell*ell*radial_trace,
        ell*ell*radial_det,
    ], dtype=float)
    sqrt_minus_g_reduced = math.sqrt(-det_g) * float(g_angular_native)
    return float(
        float(m2)*float(Mg2)*sqrt_minus_g_reduced
        * np.dot(np.asarray(beta, dtype=float), elementary)
    )
