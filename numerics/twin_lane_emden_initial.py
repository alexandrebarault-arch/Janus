"""Twin-matter time-symmetric bimetric initial-data diagnostic.

Implements the conformally-flat, time-symmetric constraint system of
Kocic, Torsello, Hogas & Mortsell (CQG 37, 165010, 2020), Eqs. (2.20a,b),
extended by the symmetric matter term in the f-sector.

This is an INITIAL-DATA existence test only. It does not evolve the spacetime
and does not establish perturbative/dynamical stability.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
import numpy as np
from scipy.integrate import solve_bvp

Array = np.ndarray


def flat_beta_from123(beta1: float, beta2: float, beta3: float):
    """Return beta0..beta4 so psi_g=psi_f=1 is a flat vacuum asymptote."""
    beta0 = -(3.0 * beta1 + 3.0 * beta2 + beta3)
    beta4 = -(beta1 + 3.0 * beta2 + 3.0 * beta3)
    return (beta0, beta1, beta2, beta3, beta4)


@dataclass(frozen=True)
class Params:
    beta: tuple[float, float, float, float, float]
    interaction: float = 0.0  # ell^{-2} in the paper's convention
    kappa_g: float = 1.0
    kappa_f: float = 1.0


@dataclass(frozen=True)
class InitialDataSolution:
    success: bool
    message: str
    r: Array
    psi_g: Array
    psi_f: Array
    min_psi_g: float
    min_psi_f: float
    max_constraint_residual: float
    niter: int


def gaussian_profile(r: Array, amplitude: float, width: float) -> Array:
    r = np.asarray(r, dtype=float)
    return amplitude * np.exp(-0.5 * (r / width) ** 2)


def shell_profile(r: Array, amplitude: float, radius: float, width: float) -> Array:
    r = np.asarray(r, dtype=float)
    x = r / radius
    return amplitude * x**2 * np.exp(-0.5 * ((r - radius) / width) ** 2)


def _interaction_polys(pg: Array, pf: Array, beta):
    b0, b1, b2, b3, b4 = beta
    ug = (
        b0 * pg**6
        + 3.0 * b1 * pf**2 * pg**4
        + 3.0 * b2 * pf**4 * pg**2
        + b3 * pf**6
    )
    uf = (
        b1 * pg**6
        + 3.0 * b2 * pf**2 * pg**4
        + 3.0 * b3 * pf**4 * pg**2
        + b4 * pf**6
    )
    return ug, uf


def solve_initial_data(
    p: Params,
    Dg: Callable[[Array], Array],
    Df: Callable[[Array], Array],
    *,
    r_max: float = 25.0,
    points: int = 500,
    r_min: float = 1.0e-5,
    tol: float = 1.0e-6,
    max_nodes: int = 20000,
) -> InitialDataSolution:
    """Solve the coupled generalized Lane-Emden constraints.

    Boundary conditions:
      psi_g'(0)=psi_f'(0)=0,
      psi_g(r_max)=psi_f(r_max)=1.

    Dg/Df are conserved-density profiles in the respective matter sectors.
    """
    if r_max <= r_min or points < 20:
        raise ValueError("invalid radial domain")

    r = np.linspace(r_min, r_max, points)
    guess = np.ones((4, points), dtype=float)
    guess[1, :] = 0.0
    guess[3, :] = 0.0

    def ode(rr, y):
        pg, dpg, pf, dpf = y
        pg_safe = np.where(np.abs(pg) < 1e-10, 1e-10, pg)
        pf_safe = np.where(np.abs(pf) < 1e-10, 1e-10, pf)
        ug, uf = _interaction_polys(pg, pf, p.beta)
        dg = np.asarray(Dg(rr), dtype=float)
        df = np.asarray(Df(rr), dtype=float)
        ddpg = -2.0 * dpg / rr - p.kappa_g * (p.interaction * ug + dg) / (4.0 * pg_safe)
        ddpf = -2.0 * dpf / rr - p.kappa_f * (p.interaction * uf + df) / (4.0 * pf_safe)
        return np.vstack((dpg, ddpg, dpf, ddpf))

    def bc(ya, yb):
        return np.array([ya[1], ya[3], yb[0] - 1.0, yb[2] - 1.0])

    sol = solve_bvp(ode, bc, r, guess, tol=tol, max_nodes=max_nodes, verbose=0)
    residual = float(np.max(sol.rms_residuals)) if len(sol.rms_residuals) else float("nan")
    pg, pf = sol.y[0], sol.y[2]
    return InitialDataSolution(
        success=bool(sol.success and np.all(np.isfinite(sol.y))),
        message=str(sol.message),
        r=sol.x,
        psi_g=pg,
        psi_f=pf,
        min_psi_g=float(np.min(pg)),
        min_psi_f=float(np.min(pf)),
        max_constraint_residual=residual,
        niter=int(sol.niter),
    )
