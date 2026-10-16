"""Native cosmic-time background jets for the finite-mu Candidate-C HR pullback."""
from __future__ import annotations

from dataclasses import dataclass
import math

from numerics.candidate_c_dust_background import candidate_c_dust_background_point


@dataclass(frozen=True)
class CandidateCNativeHRJets:
    a: float
    n: float
    alpha: float
    H_g: float
    n_dot_over_n: float
    n_ddot_over_n: float
    alpha_dot_over_alpha: float
    alpha_ddot_over_alpha: float


def _five_point_derivatives(samples: dict[int, float], step_N: float) -> tuple[float, float]:
    h = float(step_N)
    fm2 = float(samples[-2]); fm1 = float(samples[-1]); f0 = float(samples[0])
    fp1 = float(samples[1]); fp2 = float(samples[2])
    fN = (fm2 - 8.0*fm1 + 8.0*fp1 - fp2)/(12.0*h)
    fNN = (-fm2 + 16.0*fm1 - 30.0*f0 + 16.0*fp1 - fp2)/(12.0*h*h)
    return float(fN), float(fNN)


def cosmic_jet_from_log_samples(
    field_samples: dict[int, float],
    H_samples: dict[int, float],
    step_N: float,
) -> tuple[float, float]:
    """Return ``(fdot/f, fddot/f)`` from five samples in ``N=ln a``.

    ``H_samples`` are the g-sector cosmic Hubble values, so ``d/dt=H d/dN``.
    """
    h = float(step_N)
    if not (math.isfinite(h) and 0.0 < h < 0.05):
        raise ValueError("step_N must lie in (0,0.05)")
    if set(field_samples) != {-2,-1,0,1,2} or set(H_samples) != {-2,-1,0,1,2}:
        raise ValueError("five-point samples must use offsets -2,-1,0,1,2")
    if not all(math.isfinite(float(v)) for v in (*field_samples.values(), *H_samples.values())):
        raise ValueError("samples must be finite")
    f0 = float(field_samples[0]); H0 = float(H_samples[0])
    if f0 == 0.0:
        raise ValueError("central field value must be nonzero")
    fN, fNN = _five_point_derivatives(field_samples, h)
    HN, _ = _five_point_derivatives(H_samples, h)
    rate = H0*fN/f0
    accel = (H0*HN*fN + H0*H0*fNN)/f0
    return float(rate), float(accel)


def candidate_c_native_hr_jets(
    a: float,
    *,
    k_hmpc: float,
    step_N: float = 5.0e-4,
) -> CandidateCNativeHRJets:
    """Return native f lapse/scale jets along the strict on-shell dust branch."""
    a = float(a); h = float(step_N)
    if not (math.isfinite(a) and a > 0.0):
        raise ValueError("a must be finite and positive")
    if not (math.isfinite(h) and 0.0 < h < 0.02):
        raise ValueError("step_N must lie in (0,0.02)")

    points = {
        j: candidate_c_dust_background_point(a*math.exp(j*h), k_hmpc=k_hmpc)
        for j in (-2,-1,0,1,2)
    }
    n_samples = {j: points[j].metric.xi*points[j].metric.c for j in points}
    alpha_samples = {j: points[j].metric.a*points[j].metric.xi for j in points}
    H_samples = {j: points[j].metric.H/points[j].metric.a for j in points}
    nd, ndd = cosmic_jet_from_log_samples(n_samples, H_samples, h)
    ad, add = cosmic_jet_from_log_samples(alpha_samples, H_samples, h)
    return CandidateCNativeHRJets(
        a=a,
        n=float(n_samples[0]),
        alpha=float(alpha_samples[0]),
        H_g=float(H_samples[0]),
        n_dot_over_n=nd,
        n_ddot_over_n=ndd,
        alpha_dot_over_alpha=ad,
        alpha_ddot_over_alpha=add,
    )
