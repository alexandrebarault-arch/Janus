"""Strictly on-shell dust+dust benchmark neighboring Candidate C."""
from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
import math
import numpy as np

from numerics.comelli_dae import ScalarBackground, ScalarBackgroundDerivatives
from numerics.candidate_c_transfer import k_hmpc_to_h0
from numerics.flrw_two_matter import (
    Params,
    branch_constraint,
    branch_log_derivatives,
    candidate_c,
    diagnostics,
    friedmann_g,
    positive_real_roots,
    polynomial_coefficients,
)


@dataclass(frozen=True)
class CandidateCDustBackgroundPoint:
    y: float
    y_N: float
    y_NN: float
    metric: ScalarBackground
    derivatives: ScalarBackgroundDerivatives
    rho_g_m: float
    rho_f_m: float


def _present_dust_constraint(y: float, base: Params) -> float:
    p = replace(base, y0=float(y))
    return float(branch_constraint(1.0, float(y), p))


def _resolve_present_y0(base: Params) -> float:
    reference = candidate_c().y0
    xs = np.linspace(max(1.0e-4, 0.5 * reference), 1.5 * reference, 801)
    brackets: list[tuple[float, float]] = []
    x0 = float(xs[0])
    f0 = _present_dust_constraint(x0, base)
    for x1_raw in xs[1:]:
        x1 = float(x1_raw)
        f1 = _present_dust_constraint(x1, base)
        if f0 == 0.0:
            brackets.append((x0, x0))
        elif f0 * f1 < 0.0:
            brackets.append((x0, x1))
        x0, f0 = x1, f1
    if not brackets:
        raise RuntimeError("could not bracket the present Candidate-C dust branch")
    lo, hi = min(brackets, key=lambda br: abs(0.5 * (br[0] + br[1]) - reference))
    if lo == hi:
        return lo
    flo = _present_dust_constraint(lo, base)
    for _ in range(90):
        mid = 0.5 * (lo + hi)
        fm = _present_dust_constraint(mid, base)
        if flo * fm <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return float(0.5 * (lo + hi))


@lru_cache(maxsize=1)
def candidate_c_dust_params() -> Params:
    """Return Candidate-C interactions/matter with radiation removed on shell."""
    base = replace(candidate_c(), omega_g_r0=0.0)
    y0 = _resolve_present_y0(base)
    return replace(base, y0=y0)


def _dust_y(a: float, p: Params) -> float:
    roots = positive_real_roots(float(a), p)
    if roots.size == 0:
        raise RuntimeError(f"Candidate-C dust benchmark has no positive root at a={a}")
    y = float(roots[-1])
    coeff = np.trim_zeros(polynomial_coefficients(float(a), p), trim="f")
    deriv = np.polyder(coeff)
    for _ in range(3):
        slope = float(np.polyval(deriv, y))
        if slope == 0.0:
            break
        y -= float(np.polyval(coeff, y)) / slope
    return float(y)


def candidate_c_dust_background_point(
    a: float, *, k_hmpc: float,
) -> CandidateCDustBackgroundPoint:
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    p = candidate_c_dust_params()
    y = _dust_y(float(a), p)
    y_N, y_NN = branch_log_derivatives(float(a), y, p)
    c = 1.0 + y_N / y
    c_N = y_NN / y - (y_N / y) ** 2

    J = p.beta1 + 2.0 * p.beta2 * y + p.beta3 * y**2
    J_y = 2.0 * p.beta2 + 2.0 * p.beta3 * y
    J_yy = 2.0 * p.beta3
    f2 = y * J
    f2_N = y_N * (J + y * J_y)
    f1 = y * J + 0.5 * (c - 1.0) * y**2 * J_y
    f1_N = (
        f2_N
        + 0.5 * c_N * y**2 * J_y
        + 0.5 * (c - 1.0) * y_N * (2.0 * y * J_y + y**2 * J_yy)
    )

    E2 = float(friedmann_g(float(a), y, p))
    if E2 <= 0.0:
        raise RuntimeError("Candidate-C dust benchmark has non-positive H^2")
    E_phys = math.sqrt(E2)
    omega_m = p.omega_g_m0 * a**-3
    E2_N = -3.0 * omega_m + p.m2_over_H02 * J * y_N
    E_phys_N = E2_N / (2.0 * E_phys)

    H = a * E_phys
    H_N = H + a * E_phys_N
    H_prime = H * H_N
    H_omega = c * H
    H_omega_N = c_N * H + c * H_N
    H_omega_prime = H * H_omega_N

    k = k_hmpc_to_h0(k_hmpc)
    metric = ScalarBackground(
        a=float(a), m2=p.m2_over_H02, f1=float(f1), f2=float(f2),
        H=float(H), H_omega=float(H_omega), c=float(c), xi=float(y),
        kappa=float(p.alpha**2), k2=float(k*k), G8pi=1.0,
    )
    derivatives = ScalarBackgroundDerivatives(
        H_prime=float(H_prime), H_omega_prime=float(H_omega_prime),
        c_prime=float(H * c_N), xi_prime=float(H * y_N),
        f1_prime=float(H * f1_N), f2_prime=float(H * f2_N),
    )
    rho_g_m = 3.0 * p.omega_g_m0 * a**-3
    rho_f_m = 3.0 * p.omega_f_m0 * (p.y0 / (a * y))**3
    return CandidateCDustBackgroundPoint(
        y=float(y), y_N=float(y_N), y_NN=float(y_NN),
        metric=metric, derivatives=derivatives,
        rho_g_m=float(rho_g_m), rho_f_m=float(rho_f_m),
    )


def candidate_c_dust_meff_over_H(a: float) -> float:
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(float(a), k_hmpc=0.0)
    d = diagnostics(np.array([float(a)]), np.array([point.y]), p)
    ratio2 = float(d["meff2_over_H2"][0])
    if ratio2 < 0.0:
        raise RuntimeError("m_eff^2/H^2 is negative on the dust benchmark")
    return float(math.sqrt(ratio2))


@lru_cache(maxsize=1)
def candidate_c_dust_linear_start() -> float:
    """Return the scale factor of the unique late m_eff/H=1 crossing."""
    grid = np.geomspace(1.0, 1.0e-3, 1200)
    values = np.array([candidate_c_dust_meff_over_H(float(a)) - 1.0 for a in grid])
    hits = np.where(values[:-1] * values[1:] <= 0.0)[0]
    if hits.size != 1:
        raise RuntimeError(f"expected one late m_eff/H crossing, found {hits.size}")
    i = int(hits[0])
    hi = float(grid[i])
    lo = float(grid[i + 1])
    flo = candidate_c_dust_meff_over_H(lo) - 1.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        fm = candidate_c_dust_meff_over_H(mid) - 1.0
        if flo * fm <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return float(0.5 * (lo + hi))
