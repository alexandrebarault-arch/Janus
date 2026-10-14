"""Exact HR square-root invariants for the spherical non-homothetic Stueckelberg map."""
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
    g_inverse_radial = np.diag([-1.0/(a*a), 1.0/(a*a)])
    A = g_inverse_radial @ f.radial_block
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
    ell = b*(1.0 + mu)/a

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
