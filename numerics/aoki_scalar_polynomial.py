"""Numerical diagnostics for the nonlinear scalar (Stueckelberg) equation.

Implements Eqs. (5.8)-(5.11) of:
K. Aoki, K.-i. Maeda, R. Namba,
"Stability of the Early Universe in Bigravity Theory",
Phys. Rev. D 92, 044054 (2015), arXiv:1506.04543.

This is a research diagnostic, not a full cosmological solver.

Conventions
-----------
All squared mass/Hubble/source quantities can be supplied in any common units.

source_g = kappa_g^2 rho_g delta_g
source_f = K^2 kappa_f^2 rho_f delta_f

The polynomial solved is
    C_m2(mu) + C_H2(mu) + C_matter(mu) = 0.

The code deliberately exposes source_g/source_f directly so that no hidden
assumption about the background Friedmann equations is introduced.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Params:
    beta2: float
    beta3: float
    mg2: float
    mf2: float
    H2: float = 0.0
    w: float = 0.0
    source_g: float = 0.0
    source_f: float = 0.0


def C_m2(mu: float | np.ndarray, p: Params):
    b2, b3 = p.beta2, p.beta3
    g = p.mg2 * (1 + mu) ** 2 * (
        9
        + 18 * b2 * mu
        + (6 * b2**2 + 4 * b3) * mu**2
        - b3**2 * mu**4
    )
    f = p.mf2 * (
        9
        + 18 * (1 + b2) * mu
        + (10 + 34 * b2 + 4 * b3 + 6 * b2**2) * mu**2
        + (2 + 14 * b2 + 8 * b3 + 12 * b2**2) * mu**3
        + (2 * b2 + 2 * b3 + 2 * b2**2 - b3**2 + 4 * b2 * b3)
        * mu**4
    )
    return mu * (g + f)


def C_H2(mu: float | np.ndarray, p: Params):
    b2, b3, w = p.beta2, p.beta3, p.w
    return (
        -3
        * p.H2
        * mu
        * (1 + mu) ** 2
        * (
            3 * (1 - w)
            + 2 * (1 + (1 - 3 * w) * b2) * mu
            + (2 * b2 - (1 + 3 * w) * b3) * mu**2
        )
    )


def C_matter(mu: float | np.ndarray, p: Params):
    b2, b3 = p.beta2, p.beta3
    return (1 + mu) ** 2 * (
        p.source_g * (1 - b3 * mu**2)
        - p.source_f
        * (1 + mu)
        * (1 + 2 * mu + (2 * b2 - b3) * mu**2)
    )


def equation(mu: float | np.ndarray, p: Params):
    return C_m2(mu, p) + C_H2(mu, p) + C_matter(mu, p)


def polynomial_coefficients(p: Params) -> np.ndarray:
    """Recover descending polynomial coefficients by exact-value sampling.

    The equation has degree <= 7. Vandermonde interpolation is sufficient for
    diagnostics and avoids a symbolic dependency in the repository.
    """
    xs = np.arange(8, dtype=float)
    ys = np.array([equation(x, p) for x in xs], dtype=float)
    # numpy.polynomial.polynomial.polyfit returns ascending coefficients.
    asc = np.polynomial.polynomial.polyfit(xs, ys, 7)
    # Remove interpolation noise.
    asc[np.abs(asc) < 1e-10 * max(1.0, np.max(np.abs(asc)))] = 0.0
    return asc[::-1]


def real_roots(p: Params, mu_min: float = -0.999999, tol: float = 1e-7):
    coeff = polynomial_coefficients(p)
    coeff = np.trim_zeros(coeff, trim="f")
    roots = np.roots(coeff)
    out = sorted(
        r.real
        for r in roots
        if abs(r.imag) < tol and r.real > mu_min
    )
    return np.array(out)


def published_regression_checks() -> None:
    """Reproduce several roots quoted by Aoki-Maeda-Namba (2015)."""
    # Case A, late-time H << m_eff: stable nonlinear root quoted as 0.698872.
    case_a_late = Params(beta2=-3, beta3=3, mg2=0.5, mf2=0.5)
    roots = real_roots(case_a_late)
    assert np.min(np.abs(roots - 0.698872)) < 2e-5, roots

    # Case A, early matter-era H >> m_eff: stable root quoted ~0.40.
    case_a_early = Params(beta2=-3, beta3=3, mg2=0.0, mf2=0.0, H2=1.0, w=0.0)
    roots = real_roots(case_a_early)
    assert np.min(np.abs(roots - 0.396418)) < 2e-5, roots

    # Case B, early matter-era root quoted ~1.1.
    case_b_early = Params(beta2=-1, beta3=0.5, mg2=0.0, mf2=0.0, H2=1.0, w=0.0)
    roots = real_roots(case_b_early)
    assert np.min(np.abs(roots - 1.095445)) < 2e-5, roots


def demo() -> None:
    published_regression_checks()
    print("Regression checks: PASS")
    print("Case A late real roots:", real_roots(Params(-3, 3, 0.5, 0.5)))
    print("Case B late real roots:", real_roots(Params(-1, 0.5, 0.5, 0.5)))


if __name__ == "__main__":
    demo()
