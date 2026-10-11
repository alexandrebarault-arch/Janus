"""Dynamically on-shell Comelli Case-C benchmark for Gate 2B.

This module codifies the exact a1-only radiation+dust background used to
reproduce Appendix B.2 of Comelli, Crisostomi & Pilo. The benchmark is
intentionally dimensionless: k is supplied directly in the same units as the
conformal-time equations.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives


@dataclass(frozen=True)
class CaseCBackgroundPoint:
    metric: ScalarBackground
    derivatives: ScalarBackgroundDerivatives
    rho1: float
    rho2: float
    xi_da: float
    xi_daa: float
    a_prime: float


def case_c_xi_of_a(a: float) -> float:
    """Positive exact root of a^4 xi^2 + xi - a - a^4/3 = 0.

    The rationalized form avoids catastrophic cancellation for a << 1.
    """
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    disc_minus_one = 4.0*a**5 + (4.0/3.0)*a**8
    return (2.0*a + (2.0/3.0)*a**4) / (
        math.sqrt(1.0 + disc_minus_one) + 1.0
    )


def _xi_derivatives(a: float, xi: float) -> tuple[float, float]:
    # F(a,xi)=a^4 xi^2 + xi - a - a^4/3 = 0.
    F_xi = 1.0 + 2.0*a**4*xi
    F_a = 4.0*a**3*xi**2 - 1.0 - (4.0/3.0)*a**3
    xi_a = -F_a/F_xi

    F_xixi = 2.0*a**4
    F_axi = 8.0*a**3*xi
    F_aa = 12.0*a**2*xi**2 - 4.0*a**2
    xi_aa = -(
        F_aa + 2.0*F_axi*xi_a + F_xixi*xi_a**2
    ) / F_xi
    return float(xi_a), float(xi_aa)


def _a_prime(a: float) -> float:
    xi = case_c_xi_of_a(a)
    return math.sqrt(1.0 + a**4*xi)


def case_c_tau_of_a(a: float, *, quadrature_order: int = 48) -> float:
    """Conformal time from the Big Bang to scale factor ``a``.

    Uses fixed Gauss-Legendre quadrature on
        tau(a) = integral_0^a da_tilde / sqrt(1+a_tilde^4 xi(a_tilde)).
    This stays on the exact Case-C branch and adds no SciPy dependency.
    """
    if not (a >= 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and non-negative")
    if a == 0.0:
        return 0.0
    if quadrature_order < 8:
        raise ValueError("quadrature_order must be at least 8")

    nodes, weights = np.polynomial.legendre.leggauss(int(quadrature_order))
    aa = 0.5*a*(nodes + 1.0)
    vals = np.empty_like(aa)
    for i, ai in enumerate(aa):
        vals[i] = 1.0/_a_prime(float(ai))
    return float(0.5*a*np.dot(weights, vals))


def case_c_a_of_tau(tau: float, *, quadrature_order: int = 48) -> float:
    """Invert ``case_c_tau_of_a`` monotonically by bisection."""
    if not (tau >= 0.0 and math.isfinite(tau)):
        raise ValueError("tau must be finite and non-negative")
    if tau == 0.0:
        return 0.0

    lo = 0.0
    hi = max(1.05*tau, 1.0e-12)
    while case_c_tau_of_a(hi, quadrature_order=quadrature_order) < tau:
        hi *= 2.0

    for _ in range(80):
        mid = 0.5*(lo + hi)
        value = case_c_tau_of_a(mid, quadrature_order=quadrature_order)
        if value < tau:
            lo = mid
        else:
            hi = mid
    return float(0.5*(lo + hi))


def case_c_background_from_a(a: float, *, k: float) -> CaseCBackgroundPoint:
    """Return the exact on-shell Case-C background at scale factor ``a``.

    Conventions are 8piG=kappa=m^2=a1=1, a0=a2=a3=a4=0,
    w1=1/3 and w2=0. The Friedmann equation is a'^2=1+a^4 xi.
    """
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    if not (k >= 0.0 and math.isfinite(k)):
        raise ValueError("k must be finite and non-negative")

    xi = case_c_xi_of_a(a)
    xi_a, xi_aa = _xi_derivatives(a, xi)

    q = 1.0 + a**4*xi
    a_prime = math.sqrt(q)
    q_a = 4.0*a**3*xi + a**4*xi_a
    a_prime_a = q_a/(2.0*a_prime)

    H = a_prime/a
    H_a = a_prime_a/a - a_prime/a**2
    H_prime = H_a*a_prime

    xi_prime = xi_a*a_prime
    c = 1.0 + a*xi_a/xi
    c_a = xi_a/xi + a*(xi_aa/xi - (xi_a/xi)**2)
    c_prime = c_a*a_prime

    H_omega = c*H
    H_omega_prime = c_prime*H + c*H_prime

    # For the a1-only benchmark f1=f2=xi.
    f1 = xi
    f2 = xi
    f1_prime = xi_prime
    f2_prime = xi_prime

    metric = ScalarBackground(
        a=float(a),
        m2=1.0,
        f1=float(f1),
        f2=float(f2),
        H=float(H),
        H_omega=float(H_omega),
        c=float(c),
        xi=float(xi),
        kappa=1.0,
        k2=float(k*k),
        G8pi=1.0,
    )
    derivatives = ScalarBackgroundDerivatives(
        H_prime=float(H_prime),
        H_omega_prime=float(H_omega_prime),
        c_prime=float(c_prime),
        xi_prime=float(xi_prime),
        f1_prime=float(f1_prime),
        f2_prime=float(f2_prime),
    )

    rho1 = 3.0/a**4
    rho2 = 3.0/(a*xi)**3
    return CaseCBackgroundPoint(
        metric=metric,
        derivatives=derivatives,
        rho1=float(rho1),
        rho2=float(rho2),
        xi_da=float(xi_a),
        xi_daa=float(xi_aa),
        a_prime=float(a_prime),
    )


def case_c_background_from_tau(tau: float, *, k: float) -> CaseCBackgroundPoint:
    """Return the exact on-shell Case-C background at conformal time ``tau``."""
    if not (tau > 0.0 and math.isfinite(tau)):
        raise ValueError("tau must be finite and positive")
    a = case_c_a_of_tau(tau)
    return case_c_background_from_a(a, k=k)


def scaled_derivative_coefficients(
    p: float,
    x: float,
    f: float,
    f_x: float,
    f_xx: float,
) -> tuple[float, float]:
    """Coefficients after differentiating tau^p f(k tau).

    Returns the bracket multiplying tau^(p-1) after one derivative and the
    bracket multiplying tau^(p-2) after two derivatives. This keeps the
    non-commuting x d/dx structure explicit during the Case-C hierarchy.
    """
    first = p*f + x*f_x
    second = p*(p-1.0)*f + 2.0*p*x*f_x + x*x*f_xx
    return float(first), float(second)
