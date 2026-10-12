"""Static spherical Case-A branch-selection diagnostic for JANUS-R.

This reproduces, in a controlled dimensionless form, the branch topology of
Appendix A of Aoki-Maeda-Namba (2015) for

    beta2 = -3, beta3 = 3, m_g^2 = m_f^2,
    Lambda_g = 0, K = 1,

and equal matter-coupling normalization.

The radial variable is

    u = (R_V / R)^3,

where R_V is the Vainshtein radius estimated from their Eq. (A22). The source
ratio is

    q = M_f / M_g

under the K=1/equal-coupling specialization.

For point sources outside both matter distributions, inserting Eq. (A20) into
Eq. (A13) gives a degree-7 algebraic equation for mu. We track a chosen real
root continuously as u increases (moving inward).

This is a branch-topology diagnostic only. A real continuous algebraic root is
not by itself a proof of full dynamical stability, especially near sharp radial
transitions where gradient terms neglected in the adiabatic/static ansatz may
matter.
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


BETA2 = -3.0
BETA3 = 3.0
MG2 = 0.5
MF2 = 0.5
MEFF2 = MG2 + MF2


@dataclass(frozen=True)
class StaticBranchResult:
    last_u: float
    last_mu: float
    failed_at_u: float | None
    failure_reason: str | None


def _c_m2(mu: float | np.ndarray) -> float | np.ndarray:
    b2, b3 = BETA2, BETA3
    g = MG2 * (1.0 + mu) ** 2 * (
        9.0
        + 18.0 * b2 * mu
        + (6.0 * b2**2 + 4.0 * b3) * mu**2
        - b3**2 * mu**4
    )
    f = MF2 * (
        9.0
        + 18.0 * (1.0 + b2) * mu
        + (10.0 + 34.0 * b2 + 4.0 * b3 + 6.0 * b2**2) * mu**2
        + (2.0 + 14.0 * b2 + 8.0 * b3 + 12.0 * b2**2) * mu**3
        + (2.0 * b2 + 2.0 * b3 + 2.0 * b2**2 - b3**2 + 4.0 * b2 * b3)
        * mu**4
    )
    return mu * (g + f)


def static_equation(mu: float | np.ndarray, *, u: float, q: float):
    """Return the Case-A static algebraic equation at dimensionless radius u.

    From Eq. (A22), for K=1 and equal couplings,

        kappa_g^2 rho_g = 9 m_eff^2 u / |1-q|.

    The f-sector average density contains `(1+mu)^-3`; after insertion into
    `C_matter`, those factors simplify to the expression below.
    """
    if u < 0.0 or q < 0.0:
        raise ValueError("u and q must be non-negative")
    if abs(1.0 - q) < 1e-10:
        raise ValueError("q too close to 1: R_V normalization degenerates")

    source_g = 9.0 * MEFF2 * u / abs(1.0 - q)
    relative_source_poly = (
        (1.0 + mu) ** 2 * (1.0 - BETA3 * mu**2)
        - q * (1.0 + 2.0 * mu + (2.0 * BETA2 - BETA3) * mu**2)
    )
    return _c_m2(mu) + source_g * relative_source_poly


def real_roots(*, u: float, q: float, tol: float = 1e-7) -> np.ndarray:
    """Recover all admissible real roots of the degree<=7 equation."""
    xs = np.arange(8, dtype=float)
    ys = np.array([static_equation(x, u=u, q=q) for x in xs], dtype=float)
    asc = np.polynomial.polynomial.polyfit(xs, ys, 7)
    scale = max(1.0, float(np.max(np.abs(asc))))
    asc[np.abs(asc) < 1e-10 * scale] = 0.0
    coeff = np.trim_zeros(asc[::-1], trim="f")
    roots = np.roots(coeff)
    return np.asarray(
        sorted(r.real for r in roots if abs(r.imag) < tol and r.real > -0.999999)
    )


def track_case_a_branch(
    *,
    q: float,
    start_mu: float,
    u_max: float = 100.0,
    u_min: float = 1e-8,
    points: int = 1200,
    max_jump: float = 0.08,
) -> StaticBranchResult:
    """Track the nearest real root while moving from R>>R_V toward R<R_V."""
    if not (u_max > u_min > 0.0):
        raise ValueError("require u_max > u_min > 0")
    if points < 2 or max_jump <= 0:
        raise ValueError("invalid continuation controls")

    previous = float(start_mu)
    last_u = float(u_min)
    last_mu = previous

    for index, u in enumerate(np.geomspace(u_min, u_max, points)):
        roots = real_roots(u=float(u), q=q)
        if len(roots) == 0:
            return StaticBranchResult(last_u, last_mu, float(u), "no_real_root")
        mu = float(roots[np.argmin(np.abs(roots - previous))])
        if index > 0 and abs(mu - previous) > max_jump:
            return StaticBranchResult(
                last_u,
                last_mu,
                float(u),
                f"root_jump:{previous:.9g}->{mu:.9g}",
            )
        last_u = float(u)
        last_mu = mu
        previous = mu

    return StaticBranchResult(last_u, last_mu, None, None)
