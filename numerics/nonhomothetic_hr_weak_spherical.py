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


def static_anisotropic_standard_beta_potential(
    *,
    a: float,
    b: float,
    c_background: float,
    betas,
    m2: float,
    Mg2: float,
    Phi_g: float,
    Psi_g_radial: float,
    Psi_g_angular: float,
    Phi_f: float,
    Psi_f_radial: float,
    Psi_f_angular: float,
    mu: float,
) -> float:
    """Static control with radial/angular weak potentials varied independently.

    This helper exists to validate individual spherical interaction-stress
    components before imposing the isotropic Newtonian-gauge spatial potential.
    ``mu`` is kept nonlinear and spatially constant for this local control.
    """
    beta = tuple(float(x) for x in betas)
    if len(beta) != 5:
        raise ValueError("betas must contain beta_0 through beta_4")
    vals = (
        a, b, c_background, Phi_g, Psi_g_radial, Psi_g_angular,
        Phi_f, Psi_f_radial, Psi_f_angular, mu, m2, Mg2,
    )
    if (
        not all(math.isfinite(float(x)) for x in vals)
        or a <= 0.0 or b <= 0.0 or c_background <= 0.0 or mu <= -1.0
    ):
        raise ValueError("invalid static anisotropic inputs")
    factors = (
        1.0 + 2.0*Phi_g,
        1.0 - 2.0*Psi_g_radial,
        1.0 - 2.0*Psi_g_angular,
        1.0 + 2.0*Phi_f,
        1.0 - 2.0*Psi_f_radial,
        1.0 - 2.0*Psi_f_angular,
    )
    if min(factors) <= 0.0:
        raise ValueError("metric factors must stay positive")

    lambda_t = (
        (b/a)*c_background
        * math.sqrt((1.0 + 2.0*Phi_f)/(1.0 + 2.0*Phi_g))
    )
    lambda_r = (
        (b/a)*(1.0 + mu)
        * math.sqrt((1.0 - 2.0*Psi_f_radial)/(1.0 - 2.0*Psi_g_radial))
    )
    lambda_a = (
        (b/a)*(1.0 + mu)
        * math.sqrt((1.0 - 2.0*Psi_f_angular)/(1.0 - 2.0*Psi_g_angular))
    )

    e0 = 1.0
    e1 = lambda_t + lambda_r + 2.0*lambda_a
    e2 = (
        lambda_t*lambda_r + 2.0*lambda_t*lambda_a
        + 2.0*lambda_r*lambda_a + lambda_a*lambda_a
    )
    e3 = (
        2.0*lambda_t*lambda_r*lambda_a
        + lambda_t*lambda_a*lambda_a
        + lambda_r*lambda_a*lambda_a
    )
    e4 = lambda_t*lambda_r*lambda_a*lambda_a
    sqrt_minus_g_reduced = a**4*math.sqrt(
        (1.0 + 2.0*Phi_g)
        * (1.0 - 2.0*Psi_g_radial)
        * (1.0 - 2.0*Psi_g_angular)**2
    )
    return float(
        m2*Mg2*sqrt_minus_g_reduced
        * np.dot(np.asarray(beta, dtype=float), np.array([e0, e1, e2, e3, e4]))
    )
