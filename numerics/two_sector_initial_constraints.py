"""Time-symmetric two-sector spherical constraint solver for HR bigravity.

Implements the conformally-flat generalized Lane-Emden constraints of
Kocic et al. (2019), Eqs. (2.20a,b), with the matter term in the f-sector
restored in the second Hamiltonian constraint. The paper sets that term to
zero only because it chooses matter coupled to g alone; Eq. (2.11b) contains
it explicitly.

This is an initial-data existence diagnostic, not a time evolution solver.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
import numpy as np
from scipy.integrate import solve_bvp


@dataclass(frozen=True)
class Interaction:
    beta0: float
    beta1: float
    beta2: float
    beta3: float
    beta4: float
    mass2: float
    kappa_g: float = 1.0
    kappa_f: float = 1.0

    @classmethod
    def symmetric(
        cls,
        *,
        beta1: float,
        beta2: float,
        beta3: float,
        mass2: float,
        kappa: float = 1.0,
    ) -> "Interaction":
        """Return an asymptotically bi-Minkowski interaction.

        beta0 and beta4 are fixed by the R_infinity=1 conditions of Eq. (2.21).
        Exact g<->f exchange symmetry additionally requires beta1 == beta3 and
        equal couplings, which is the case used in the symmetry regression test.
        """
        beta0 = -(3.0 * beta1 + 3.0 * beta2 + beta3)
        beta4 = -(beta1 + 3.0 * beta2 + 3.0 * beta3)
        return cls(beta0, beta1, beta2, beta3, beta4, mass2, kappa, kappa)


@dataclass(frozen=True)
class MatterProfile:
    fn: Callable[[np.ndarray], np.ndarray]

    def __call__(self, r: np.ndarray) -> np.ndarray:
        return np.asarray(self.fn(np.asarray(r, dtype=float)), dtype=float)

    @classmethod
    def zero(cls) -> "MatterProfile":
        return cls(lambda r: np.zeros_like(r, dtype=float))

    @classmethod
    def gaussian_core(cls, *, amplitude: float, width: float) -> "MatterProfile":
        if amplitude < 0.0 or width <= 0.0:
            raise ValueError("amplitude must be non-negative and width positive")
        return cls(lambda r: amplitude * np.exp(-0.5 * (r / width) ** 2))

    @classmethod
    def gaussian_shell(
        cls, *, amplitude: float, radius: float, width: float
    ) -> "MatterProfile":
        if amplitude < 0.0 or radius < 0.0 or width <= 0.0:
            raise ValueError("invalid shell parameters")
        return cls(
            lambda r: amplitude * np.exp(-0.5 * ((r - radius) / width) ** 2)
        )


@dataclass(frozen=True)
class ConstraintSolution:
    r: np.ndarray
    psi_g: np.ndarray
    psi_f: np.ndarray
    success: bool
    message: str
    max_constraint_residual: float


def _interaction_polynomials(psi_g, psi_f, p: Interaction):
    pg = (
        p.beta0 * psi_g**6
        + 3.0 * p.beta1 * psi_f**2 * psi_g**4
        + 3.0 * p.beta2 * psi_f**4 * psi_g**2
        + p.beta3 * psi_f**6
    )
    pf = (
        p.beta1 * psi_g**6
        + 3.0 * p.beta2 * psi_f**2 * psi_g**4
        + 3.0 * p.beta3 * psi_f**4 * psi_g**2
        + p.beta4 * psi_f**6
    )
    return pg, pf


def solve_constraints(
    *,
    interaction: Interaction,
    g_profile: MatterProfile,
    f_profile: MatterProfile,
    r_max: float,
    points: int = 600,
    r_epsilon: float = 1.0e-4,
    tolerance: float = 1.0e-6,
) -> ConstraintSolution:
    """Solve the time-symmetric conformally-flat two-sector constraints.

    Boundary conditions are regularity at the center (psi'_g=psi'_f=0)
    and asymptotic bi-Minkowski normalization at finite r_max
    (psi_g=psi_f=1). r_epsilon avoids the coordinate singularity while
    preserving the regular-center condition to the numerical tolerance.
    """
    if r_max <= r_epsilon or points < 20:
        raise ValueError("invalid radial domain")
    if interaction.mass2 < 0.0:
        raise ValueError("mass2 must be non-negative")

    r = np.linspace(r_epsilon, r_max, points)

    def ode(x, y):
        psi_g, dpsi_g, psi_f, dpsi_f = y
        pg, pf = _interaction_polynomials(psi_g, psi_f, interaction)
        dg = g_profile(x)
        df = f_profile(x)
        lap_g = -(
            interaction.kappa_g * interaction.mass2 * pg
            + interaction.kappa_g * dg
        ) / (4.0 * psi_g)
        lap_f = -(
            interaction.kappa_f * interaction.mass2 * pf
            + interaction.kappa_f * df
        ) / (4.0 * psi_f)
        return np.vstack(
            [dpsi_g, lap_g - 2.0 * dpsi_g / x, dpsi_f, lap_f - 2.0 * dpsi_f / x]
        )

    def boundary(ya, yb):
        return np.array([ya[1], ya[3], yb[0] - 1.0, yb[2] - 1.0])

    guess = np.vstack(
        [np.ones_like(r), np.zeros_like(r), np.ones_like(r), np.zeros_like(r)]
    )
    sol = solve_bvp(
        ode,
        boundary,
        r,
        guess,
        tol=tolerance,
        max_nodes=30000,
        verbose=0,
    )

    sample = np.linspace(r_epsilon, r_max, points)
    y = sol.sol(sample)
    derivative = sol.sol(sample, 1)
    residual = derivative - ode(sample, y)
    max_residual = float(np.max(np.abs(residual)))

    return ConstraintSolution(
        r=sample,
        psi_g=np.asarray(y[0]),
        psi_f=np.asarray(y[2]),
        success=bool(sol.success),
        message=str(sol.message),
        max_constraint_residual=max_residual,
    )
