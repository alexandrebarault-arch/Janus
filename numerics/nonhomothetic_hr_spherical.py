"""Exact HR square-root invariants for spherical metric pairs."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_stueckelberg_spherical import pullback_f_metric


@dataclass(frozen=True)
class SphericalSquareRootInvariants:
    radial_g_inverse_f: np.ndarray
    radial_square_root: np.ndarray
    angular_eigenvalue: float
    elementary_symmetric: np.ndarray


def square_root_invariants_from_blocks(
    *,
    g_radial,
    g_angular: float,
    f_radial,
    f_angular: float,
) -> SphericalSquareRootInvariants:
    """Return principal HR invariants when both metrics are in common coordinates."""
    g = np.asarray(g_radial, dtype=float)
    f = np.asarray(f_radial, dtype=float)
    if g.shape != (2, 2) or f.shape != (2, 2):
        raise ValueError("radial blocks must be 2x2")
    if not (
        np.all(np.isfinite(g)) and np.all(np.isfinite(f))
        and math.isfinite(float(g_angular)) and math.isfinite(float(f_angular))
    ):
        raise ValueError("metric blocks must be finite")
    if g_angular <= 0.0 or f_angular <= 0.0:
        raise ValueError("angular coefficients must be positive")

    A = np.linalg.solve(g, f)
    det_A = float(np.linalg.det(A))
    tr_A = float(np.trace(A))
    if det_A <= 0.0:
        raise ValueError("radial g^-1 f determinant must be positive")

    sqrt_det = math.sqrt(det_A)
    denominator = tr_A + 2.0*sqrt_det
    if denominator <= 0.0:
        raise ValueError("principal radial square root is not real")
    S = (A + sqrt_det*np.eye(2))/math.sqrt(denominator)

    radial_trace = float(np.trace(S))
    radial_det = float(np.linalg.det(S))
    ell = math.sqrt(float(f_angular)/float(g_angular))
    elementary = np.array([
        1.0,
        radial_trace + 2.0*ell,
        radial_det + 2.0*ell*radial_trace + ell*ell,
        2.0*ell*radial_det + ell*ell*radial_trace,
        ell*ell*radial_det,
    ], dtype=float)
    return SphericalSquareRootInvariants(
        radial_g_inverse_f=np.asarray(A, dtype=float),
        radial_square_root=np.asarray(S, dtype=float),
        angular_eigenvalue=float(ell),
        elementary_symmetric=elementary,
    )


def square_root_invariants(
    *,
    a: float,
    b: float,
    c_background: float,
    r: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> SphericalSquareRootInvariants:
    """Return the principal spherical square root and ``e_0..e_4``."""
    if not (math.isfinite(a) and a > 0.0):
        raise ValueError("a must be finite and positive")
    if r <= 0.0:
        raise ValueError("r must be positive for spherical invariants")

    f = pullback_f_metric(
        b=b, c_background=c_background, r=r,
        sigma_dot=sigma_dot, sigma_prime=sigma_prime,
        mu=mu, mu_dot=mu_dot, mu_prime=mu_prime,
    )
    return square_root_invariants_from_blocks(
        g_radial=np.diag([-a*a, a*a]),
        g_angular=a*a*r*r,
        f_radial=f.radial_block,
        f_angular=f.angular_coefficient,
    )
