"""HR square-root invariants with weak metric potentials and nonlinear spherical Stueckelberg fields."""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_stueckelberg_weak_metric import (
    pullback_weak_f_metric,
    weak_g_inverse_radial,
)


@dataclass(frozen=True)
class WeakSquareRootInvariants:
    radial_g_inverse_f: np.ndarray
    radial_square_root: np.ndarray
    angular_eigenvalue: float
    elementary_symmetric: np.ndarray


def weak_square_root_invariants(
    *,
    a: float,
    b: float,
    c_background: float,
    r: float,
    Phi_g: float,
    Psi_g: float,
    Phi_f: float,
    Psi_f: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> WeakSquareRootInvariants:
    """Return the principal HR square root while keeping ``mu,sigma`` nonlinear."""
    if r <= 0.0:
        raise ValueError("r must be positive")

    g_inverse = weak_g_inverse_radial(a=a, Phi_g=Phi_g, Psi_g=Psi_g)
    f = pullback_weak_f_metric(
        b=b, c_background=c_background, r=r,
        Phi_f=Phi_f, Psi_f=Psi_f,
        sigma_dot=sigma_dot, sigma_prime=sigma_prime,
        mu=mu, mu_dot=mu_dot, mu_prime=mu_prime,
    )
    A = g_inverse @ f.radial_block
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
    ell = (
        (b/a)*(1.0 + mu)
        * math.sqrt((1.0 - 2.0*Psi_f)/(1.0 - 2.0*Psi_g))
    )
    elementary = np.array([
        1.0,
        radial_trace + 2.0*ell,
        radial_det + 2.0*ell*radial_trace + ell*ell,
        2.0*ell*radial_det + ell*ell*radial_trace,
        ell*ell*radial_det,
    ], dtype=float)
    return WeakSquareRootInvariants(
        radial_g_inverse_f=np.asarray(A, dtype=float),
        radial_square_root=np.asarray(S, dtype=float),
        angular_eigenvalue=float(ell),
        elementary_symmetric=elementary,
    )


def standard_beta_potential_reduced_density(
    *,
    a: float,
    b: float,
    c_background: float,
    r: float,
    betas,
    m2: float,
    Mg2: float,
    Phi_g: float,
    Psi_g: float,
    Phi_f: float,
    Psi_f: float,
    sigma_dot: float,
    sigma_prime: float,
    mu: float,
    mu_dot: float,
    mu_prime: float,
) -> float:
    """Return ``m^2 M_g^2 sqrt(-g) sum beta_n e_n`` per ``r^2 sin(theta)``."""
    beta = tuple(float(x) for x in betas)
    if len(beta) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    inv = weak_square_root_invariants(
        a=a, b=b, c_background=c_background, r=r,
        Phi_g=Phi_g, Psi_g=Psi_g, Phi_f=Phi_f, Psi_f=Psi_f,
        sigma_dot=sigma_dot, sigma_prime=sigma_prime,
        mu=mu, mu_dot=mu_dot, mu_prime=mu_prime,
    )
    sqrt_minus_g_reduced = a**4*math.sqrt(
        (1.0 + 2.0*Phi_g)*(1.0 - 2.0*Psi_g)**3
    )
    return float(
        m2*Mg2*sqrt_minus_g_reduced
        * np.dot(np.asarray(beta, dtype=float), inv.elementary_symmetric)
    )
