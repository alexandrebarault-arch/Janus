"""Local Aoki-Maeda-Namba screening proxy for Candidate-C dust.

This module is deliberately a *diagnostic proxy*, not a nonlinear Candidate-C
solver.  Aoki, Maeda & Namba (2015) derive their early nonlinear Stueckelberg
branches around a homothetic background ``f = K^2 g`` with constant ``K``.
Candidate C is non-homothetic.  Here we insert the instantaneous Candidate-C
ratio ``K -> xi(a)`` only to ask a narrow question: do the local interaction
couplings even lie in the class that admits an Aoki-type stable early branch?

A positive result is non-exclusion.  It neither establishes branch continuity
through ``H ~ m_eff`` nor determines the two dynamical helicity-0 matching data
required by the exact-dust late transfer system.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_params,
)


@dataclass(frozen=True)
class AokiCouplingCondition:
    beta1_raw: float
    beta2_raw: float
    beta3_raw: float
    discriminant: float
    sufficient_condition: bool


@dataclass(frozen=True)
class AokiRootStability:
    mu: float
    kinetic: float
    sound_speed_squared: float
    stable: bool


@dataclass(frozen=True)
class CandidateCAokiProxyPoint:
    a: float
    xi: float
    lapse_ctilde: float
    beta2_aoki: float
    beta3_aoki: float
    all_roots: tuple[AokiRootStability, ...]
    admissible_roots: tuple[AokiRootStability, ...]
    homothetic_proxy_only: bool = True


def candidate_c_aoki_coupling_condition() -> AokiCouplingCondition:
    """Return the Aoki sufficient early-stability condition in raw couplings.

    Aoki et al. Eq. (4.63) gives ``b2 < 0`` and
    ``b2^2 - b1*b3 > 0`` (assuming positive effective graviton mass) as a
    sufficient interaction-parameter condition for existence of a stable
    nonlinear early branch away from the exactly radiation-degenerate case.
    """
    p = candidate_c_dust_params()
    disc = float(p.beta2*p.beta2 - p.beta1*p.beta3)
    return AokiCouplingCondition(
        beta1_raw=float(p.beta1),
        beta2_raw=float(p.beta2),
        beta3_raw=float(p.beta3),
        discriminant=disc,
        sufficient_condition=bool(p.beta2 < 0.0 and disc > 0.0),
    )


def aoki_normalized_couplings(
    K: float,
    *,
    beta1_raw: float,
    beta2_raw: float,
    beta3_raw: float,
) -> tuple[float, float]:
    """Evaluate Aoki Eqs. (4.29)-(4.30) for one homothetic ratio ``K``."""
    k = float(K)
    vals = (k, beta1_raw, beta2_raw, beta3_raw)
    if not all(math.isfinite(float(v)) for v in vals) or k <= 0.0:
        raise ValueError("K must be positive and all couplings finite")
    den = beta1_raw*k + 2.0*beta2_raw*k*k + beta3_raw*k**3
    scale = max(1.0, abs(beta1_raw*k), abs(2.0*beta2_raw*k*k), abs(beta3_raw*k**3))
    if abs(den) <= 1.0e-14*scale:
        raise np.linalg.LinAlgError("Aoki normalized-coupling denominator is singular")
    beta2 = (beta2_raw*k*k + beta3_raw*k**3) / den
    beta3 = beta3_raw*k**3 / den
    return float(beta2), float(beta3)


def aoki_early_mu_roots(beta2: float, beta3: float, *, w: float = 0.0) -> tuple[float, float]:
    """Return the two nonlinear early roots ``mu_+`` and ``mu_-`` of Eq. (4.35)."""
    b2 = float(beta2); b3 = float(beta3); ww = float(w)
    if not all(math.isfinite(v) for v in (b2, b3, ww)):
        raise ValueError("Aoki root inputs must be finite")
    disc = (
        1.0 - 4.0*b2 + (1.0-3.0*ww)**2*b2*b2
        + 3.0*(1.0-ww)*(1.0+3.0*ww)*b3
    )
    scale = max(1.0, abs(b2*b2), abs(b3))
    if disc < -1.0e-13*scale:
        raise ValueError("Aoki early nonlinear roots are complex")
    disc = max(0.0, disc)
    den = -2.0*b2 + (1.0+3.0*ww)*b3
    if abs(den) <= 1.0e-14*max(1.0, abs(b2), abs(b3)):
        raise np.linalg.LinAlgError("Aoki early-root denominator is singular")
    center = 1.0 + (1.0-3.0*ww)*b2
    root = math.sqrt(disc)
    return float((center+root)/den), float((center-root)/den)


def aoki_scalar_stability(
    mu: float,
    beta2: float,
    beta3: float,
    *,
    w: float = 0.0,
) -> AokiRootStability:
    """Return Aoki Eqs. (4.55)-(4.57) for one nonlinear early root."""
    u = float(mu); b2 = float(beta2); b3 = float(beta3); ww = float(w)
    if not all(math.isfinite(v) for v in (u, b2, b3, ww)):
        raise ValueError("Aoki stability inputs must be finite")
    q = 1.0 + 2.0*b2*u + b3*u*u
    kinetic = 0.75*(3.0*ww-1.0)*(2.0+u)*q
    den = 3.0*(3.0*ww-1.0)*(2.0+u)*q
    scale = max(1.0, abs((2.0+u)*q))
    if abs(den) <= 1.0e-14*scale:
        cs2 = math.copysign(math.inf, den if den != 0.0 else 1.0)
    else:
        numerator = 2.0*(
            3.0*(1.0-ww) + (1.0-(3.0*ww-1.0)*b2)*u
        )
        cs2 = numerator/den
    return AokiRootStability(
        mu=u,
        kinetic=float(kinetic),
        sound_speed_squared=float(cs2),
        stable=bool(kinetic > 0.0 and cs2 > 0.0 and u > -1.0),
    )


def candidate_c_aoki_local_proxy(a: float, *, w: float = 0.0) -> CandidateCAokiProxyPoint:
    """Evaluate the instantaneous homothetic Aoki proxy at Candidate-C ``xi(a)``."""
    aa = float(a)
    if not (math.isfinite(aa) and aa > 0.0):
        raise ValueError("a must be finite and positive")
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(aa, k_hmpc=0.0)
    b2, b3 = aoki_normalized_couplings(
        point.y,
        beta1_raw=p.beta1,
        beta2_raw=p.beta2,
        beta3_raw=p.beta3,
    )
    roots = tuple(
        aoki_scalar_stability(mu, b2, b3, w=w)
        for mu in aoki_early_mu_roots(b2, b3, w=w)
    )
    admissible = tuple(root for root in roots if root.mu > -1.0)
    return CandidateCAokiProxyPoint(
        a=aa,
        xi=float(point.y),
        lapse_ctilde=float(point.metric.c),
        beta2_aoki=float(b2),
        beta3_aoki=float(b3),
        all_roots=roots,
        admissible_roots=admissible,
        homothetic_proxy_only=True,
    )


def candidate_c_aoki_proxy_track(a_grid, *, w: float = 0.0) -> tuple[CandidateCAokiProxyPoint, ...]:
    a = np.asarray(a_grid, dtype=float)
    if a.ndim != 1 or len(a) < 1 or not np.all(np.isfinite(a)) or np.any(a <= 0.0):
        raise ValueError("a_grid must be a finite positive one-dimensional array")
    if len(a) > 1 and not np.all(np.diff(a) > 0.0):
        raise ValueError("a_grid must be strictly increasing")
    return tuple(candidate_c_aoki_local_proxy(float(x), w=w) for x in a)
