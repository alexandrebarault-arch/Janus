"""Leading non-homothetic adiabatic Stueckelberg branch jets for early Candidate C.

This helper is an early-branch architecture oracle only.  It follows the two
regular roots of the leading non-homothetic radial polynomial.  It must not be
used as the final finite-mass fold trajectory, whose corrected roots are
located independently by the weak-metric fold audit.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.candidate_c_dust_background import (
    candidate_c_dust_background_point,
    candidate_c_dust_params,
)
from numerics.nonhomothetic_stueckelberg import (
    nonhomothetic_adiabatic_radial_polynomial_coefficients,
    temporal_shift_coefficient,
)


@dataclass(frozen=True)
class CandidateCAdiabaticStueckelbergJets:
    a: float
    H_g: float
    c: float
    xi: float
    Hdot_over_H2: float
    polynomial: np.ndarray
    mu: float
    other_mu: float
    mu_N: float
    mu_dot: float
    s: float
    s_N: float
    s_dot: float


def _five_point_first(samples: dict[int, float], h: float) -> float:
    return float((samples[-2]-8.0*samples[-1]+8.0*samples[1]-samples[2])/(12.0*h))


def _background(a: float, k_hmpc: float):
    p = candidate_c_dust_params()
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    H_g = point.metric.H/point.metric.a
    return p, point, float(H_g)


def _root_at(a: float, k_hmpc: float, *, hubble_step_N: float = 5.0e-5):
    p, point, H_g = _background(a, k_hmpc)
    h = float(hubble_step_N)
    H = {
        j: _background(a*math.exp(j*h), k_hmpc)[2]
        for j in (-2,-1,1,2)
    }
    H_N = _five_point_first(H, h)
    epsilon_H = H_N/H_g
    poly = nonhomothetic_adiabatic_radial_polynomial_coefficients(
        beta1=p.beta1, beta2=p.beta2, beta3=p.beta3,
        xi=point.metric.xi, c=point.metric.c,
        Hdot_over_H2=epsilon_H,
    )
    roots = np.roots(poly)
    real = sorted(
        float(z.real) for z in roots
        if abs(z.imag) < 1.0e-8 and z.real > -1.0
    )
    if len(real) != 2:
        raise RuntimeError(
            f"expected two regular real adiabatic roots at a={a}, got {roots}"
        )
    return (
        real[0], real[1], np.asarray(poly,dtype=float), H_g,
        float(point.metric.c), float(point.metric.xi), float(epsilon_H),
    )


def candidate_c_adiabatic_stueckelberg_jets(
    a: float,
    *,
    k_hmpc: float,
    step_N: float = 6.0e-4,
) -> CandidateCAdiabaticStueckelbergJets:
    """Return leading early regular-branch ``mu,s`` cosmic-time jets.

    The more-negative member of the regular pair is followed.  The function
    intentionally raises once the leading quadratic no longer has two regular
    real roots; no algebraic branch jump is manufactured.
    """
    a = float(a); h = float(step_N)
    if not (math.isfinite(a) and a > 0.0):
        raise ValueError("a must be finite and positive")
    if not (math.isfinite(h) and 0.0 < h < 0.01):
        raise ValueError("step_N must lie in (0,0.01)")

    # +/-4 are needed because s(j) itself needs a five-point derivative of mu.
    roots = {
        j: _root_at(a*math.exp(j*h), k_hmpc)
        for j in range(-4,5)
    }
    mus = {j: roots[j][0] for j in roots}

    def mu_N_at(j: int) -> float:
        values = {d: mus[j+d] for d in (-2,-1,1,2)}
        return _five_point_first(values, h)

    s_values: dict[int,float] = {}
    for j in (-2,-1,0,1,2):
        aj = a*math.exp(j*h)
        mu_j = mus[j]
        mu_N_j = mu_N_at(j)
        _,_,_,H_g_j,c_j,_,_ = roots[j]
        mu_dot_j = H_g_j*mu_N_j
        s_values[j] = temporal_shift_coefficient(
            a=aj, H_g=H_g_j, c=c_j,
            mu=mu_j, mu_dot=mu_dot_j,
        )

    mu_N = mu_N_at(0)
    mu = mus[0]
    other_mu = roots[0][1]
    poly,H_g,c,xi,epsilon_H = roots[0][2:]
    mu_dot = H_g*mu_N
    s = s_values[0]
    s_N = _five_point_first(s_values, h)
    return CandidateCAdiabaticStueckelbergJets(
        a=a, H_g=H_g, c=c, xi=xi,
        Hdot_over_H2=epsilon_H,
        polynomial=np.asarray(poly,dtype=float),
        mu=mu, other_mu=other_mu,
        mu_N=float(mu_N), mu_dot=float(mu_dot),
        s=float(s), s_N=float(s_N), s_dot=float(H_g*s_N),
    )
