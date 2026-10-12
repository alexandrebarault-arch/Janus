"""Two-matter time-symmetric initial-data solver for JANUS-R Gate A0.

Implements the conformally-flat generalized Lane-Emden constraints of
Kocic, Torsello, Högås & Mörtsell, arXiv:1904.08617, Eqs. (2.20)-(2.21),
extended by allowing a separately coupled dust source in the f sector.

This module answers only an initial-data existence question. It does NOT evolve
the data and it is NOT a cosmological FLRW void solution.
"""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_bvp


@dataclass(frozen=True)
class Interaction:
    beta0: float
    beta1: float
    beta2: float
    beta3: float
    beta4: float
    m2: float
    kappa_g: float = 1.0
    kappa_f: float = 1.0

    @classmethod
    def from_internal(
        cls,
        *,
        beta1: float,
        beta2: float,
        beta3: float,
        m2: float,
        kappa_g: float = 1.0,
        kappa_f: float = 1.0,
    ) -> "Interaction":
        """Complete beta0,beta4 for the R_infinity=1 asymptotically-flat branch."""
        beta0 = -3.0 * beta1 - 3.0 * beta2 - beta3
        beta4 = -beta1 - 3.0 * beta2 - 3.0 * beta3
        return cls(beta0, beta1, beta2, beta3, beta4, m2, kappa_g, kappa_f)


@dataclass(frozen=True)
class Profiles:
    dg_fn: object
    df_fn: object

    def dg(self, r):
        return np.asarray(self.dg_fn(np.asarray(r)), dtype=float)

    def df(self, r):
        return np.asarray(self.df_fn(np.asarray(r)), dtype=float)

    @classmethod
    def zero(cls) -> "Profiles":
        return cls(
            lambda r: np.zeros_like(r, dtype=float),
            lambda r: np.zeros_like(r, dtype=float),
        )

    @classmethod
    def central_f_and_g_shell(
        cls,
        *,
        f_amp: float,
        f_sigma: float,
        g_amp: float,
        g_radius: float,
        g_sigma: float,
    ) -> "Profiles":
        """Positive f central lump plus positive g compensating shell.

        In an asymptotically-vacuum slice this is only a wall/regularity proxy,
        not a literal negative-density cosmological void.
        """

        def df(r):
            return f_amp * np.exp(-0.5 * (r / f_sigma) ** 2)

        def dg(r):
            return g_amp * np.exp(-0.5 * ((r - g_radius) / g_sigma) ** 2)

        return cls(dg, df)


@dataclass
class InitialDataSolution:
    r: np.ndarray
    psi_g: np.ndarray
    dpsi_g: np.ndarray
    psi_f: np.ndarray
    dpsi_f: np.ndarray
    success: bool
    message: str
    rms_residual_max: float


def _interaction_g(pg, pf, p: Interaction):
    return p.m2 * (
        p.beta0 * pg**6
        + 3.0 * p.beta1 * pf**2 * pg**4
        + 3.0 * p.beta2 * pf**4 * pg**2
        + p.beta3 * pf**6
    )


def _interaction_f(pg, pf, p: Interaction):
    return p.m2 * (
        p.beta1 * pg**6
        + 3.0 * p.beta2 * pf**2 * pg**4
        + 3.0 * p.beta3 * pf**4 * pg**2
        + p.beta4 * pf**6
    )


def solve_initial_data(
    p: Interaction,
    profiles: Profiles,
    *,
    r_max: float = 25.0,
    n: int = 400,
    tol: float = 1.0e-6,
    max_nodes: int = 20000,
) -> InitialDataSolution:
    """Solve the two coupled spherical conformal-factor constraints.

    Boundary conditions:
      d psi_g/dr = d psi_f/dr = 0 at the centre,
      psi_g = psi_f = 1 at the finite outer approximation to infinity.
    """
    r0 = max(1.0e-6, r_max / (n * 1.0e5))
    r = np.linspace(r0, r_max, n)

    def fun(x, y):
        pg, ug, pf, uf = y
        dg = profiles.dg(x)
        df = profiles.df(x)
        srcg = p.kappa_g * (_interaction_g(pg, pf, p) + dg)
        srcf = p.kappa_f * (_interaction_f(pg, pf, p) + df)

        # Eq. (2.20) generalized to include separately-coupled f dust:
        # 4 psi (psi'' + 2 psi'/r) + source = 0.
        pg2 = -2.0 * ug / x - srcg / (4.0 * pg)
        pf2 = -2.0 * uf / x - srcf / (4.0 * pf)
        return np.vstack((ug, pg2, uf, pf2))

    def bc(ya, yb):
        return np.array([ya[1], ya[3], yb[0] - 1.0, yb[2] - 1.0])

    y0 = np.vstack(
        (
            np.ones_like(r),
            np.zeros_like(r),
            np.ones_like(r),
            np.zeros_like(r),
        )
    )

    sol = solve_bvp(fun, bc, r, y0, tol=tol, max_nodes=max_nodes, verbose=0)
    rms = float(np.max(sol.rms_residuals)) if len(sol.rms_residuals) else 0.0
    return InitialDataSolution(
        sol.x,
        sol.y[0],
        sol.y[1],
        sol.y[2],
        sol.y[3],
        sol.success,
        sol.message,
        rms,
    )


def residual_max(sol: InitialDataSolution, p: Interaction, profiles: Profiles) -> float:
    """Maximum normalized collocation residual reported by solve_bvp."""
    return sol.rms_residual_max
