"""Linear Candidate-C dust action in a pre-BD relative Stueckelberg basis.

This module is an exact time-dependent change of coordinates of the already
validated De Felice two-dust action.  It does not assume a finite-H one-field
pi map.  Instead the pre-BD variables are

    (Y1, Y2, L, T, p_g, p_f),

with ``Y3=-2L`` and ``Z=-nHf*T+k^2 L/3``.  The temporal relative displacement
``T`` is therefore the kinetic-null/algebraic coordinate, while ``L`` remains
the helicity-0 spatial coordinate.  The two dust phase variables are retained
throughout the reduction.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import numpy as np

from numerics.bd_time_canonicalization import canonicalize_linear_rate_time_dependent
from numerics.candidate_c_dust_background import candidate_c_dust_background_point
from numerics.de_felice_dust_local_modes import (
    DustDAELocalSystem,
    dust_dae_local_system,
    local_phase_squared_speeds,
)
from numerics.de_felice_dust_physical_action import _candidate_transformed
from numerics.prebd_stueckelberg_transform import (
    prebd_bridge_matrices,
    transform_state_rate_hessian,
)


@dataclass(frozen=True)
class CandidateCStueckelbergPhysicalAction:
    prebd_hessian: np.ndarray
    canonical_hessian: np.ndarray
    physical_phase_hessian: np.ndarray
    nHf: float
    nHf_dot: float
    tdot_kinetic_residual: float
    t_algebraic_coefficient: float
    pdot_residual: float


def _bridge_rates(point) -> tuple[float, float]:
    """Return ``n H_f`` and its g-cosmic-time derivative."""
    bg = point.metric
    bgp = point.derivatives
    nHf = bg.H_omega / bg.a
    nHf_dot = (bgp.H_omega_prime - bg.H_omega*bg.H) / (bg.a*bg.a)
    if not (math.isfinite(nHf) and nHf > 0.0 and math.isfinite(nHf_dot)):
        raise ValueError("invalid n H_f bridge rate")
    return float(nHf), float(nHf_dot)


def _candidate_stueckelberg_prebd(a: float, k_hmpc: float):
    H, point = _candidate_transformed(float(a), float(k_hmpc))
    nHf, nHf_dot = _bridge_rates(point)
    R, Rdot = prebd_bridge_matrices(
        k=math.sqrt(point.metric.k2), nHf=nHf, nHf_dot=nHf_dot,
    )
    transformed = transform_state_rate_hessian(H, R, Rdot)
    return transformed, point, nHf, nHf_dot


def candidate_c_stueckelberg_physical_action(
    a: float,
    *,
    k_hmpc: float,
    derivative_step_N: float = 2.0e-3,
) -> CandidateCStueckelbergPhysicalAction:
    """Eliminate the temporal Stückelberg/BD coordinate on the on-shell path."""
    if not (a > 0.0 and math.isfinite(a)):
        raise ValueError("a must be finite and positive")
    h = float(derivative_step_N)
    if not (h > 0.0 and h < 0.03 and math.isfinite(h)):
        raise ValueError("derivative_step_N must lie in (0,0.03)")

    H, point, nHf, nHf_dot = _candidate_stueckelberg_prebd(a, k_hmpc)
    n = 6
    t_index = 3
    Kraw = H[n:, n:]
    scale = max(1.0, float(np.linalg.norm(Kraw, ord=np.inf)))
    tdot_residual = float(max(
        np.linalg.norm(Kraw[t_index, :], ord=np.inf),
        np.linalg.norm(Kraw[:, t_index], ord=np.inf),
    ) / scale)

    columns = []
    for offset in (-2.0, -1.0, 1.0, 2.0):
        Hn, _, _, _ = _candidate_stueckelberg_prebd(
            a*math.exp(offset*h), k_hmpc,
        )
        columns.append(Hn[:n, n+t_index])
    dm2, dm1, dp1, dp2 = columns
    dc_dN = (dm2 - 8.0*dm1 + 8.0*dp1 - dp2) / (12.0*h)
    H_g = point.metric.H / point.metric.a
    dot_c = H_g * dc_dN

    canonical = canonicalize_linear_rate_time_dependent(
        H, dot_c=dot_c, mu_measure=3.0*H_g, z_index=t_index,
    )

    keep11 = [i for i in range(12) if i != n+t_index]
    H11 = canonical[np.ix_(keep11, keep11)]
    htt = float(H11[t_index, t_index])
    hscale = max(1.0, float(np.linalg.norm(H11, ord=np.inf)))
    if abs(htt) <= 1.0e-14*hscale:
        raise np.linalg.LinAlgError("temporal Stueckelberg scalar is not algebraically invertible")
    phys = [i for i in range(11) if i != t_index]
    hpt = H11[np.ix_(phys, [t_index])]
    physical = H11[np.ix_(phys, phys)] - hpt @ hpt.T / htt
    physical = 0.5*(physical + physical.T)

    # Physical order: (Y1,Y2,L,p_g,p_f,Y1dot,Y2dot,Ldot,p_gdot,p_fdot).
    p_rate = [8, 9]
    pscale = max(1.0, float(np.linalg.norm(physical, ord=np.inf)))
    pdot_residual = float(max(
        np.linalg.norm(physical[p_rate, :], ord=np.inf),
        np.linalg.norm(physical[:, p_rate], ord=np.inf),
    ) / pscale)
    if pdot_residual > 1.0e-8:
        raise np.linalg.LinAlgError(
            f"unexpected dust-momentum rate residual {pdot_residual:.6g}"
        )

    return CandidateCStueckelbergPhysicalAction(
        prebd_hessian=np.asarray(H, dtype=float),
        canonical_hessian=np.asarray(canonical, dtype=float),
        physical_phase_hessian=np.asarray(physical, dtype=float),
        nHf=nHf,
        nHf_dot=nHf_dot,
        tdot_kinetic_residual=tdot_residual,
        t_algebraic_coefficient=htt,
        pdot_residual=pdot_residual,
    )


def candidate_c_stueckelberg_local_system(
    a: float,
    *,
    k_hmpc: float,
    action_derivative_step_N: float = 2.0e-3,
    trajectory_derivative_step_N: float = 2.0e-3,
) -> DustDAELocalSystem:
    """Return the regular six-dimensional local DAE in ``(Y1,Y2,L)``."""
    h = float(trajectory_derivative_step_N)
    if not (h > 0.0 and h < 0.03 and math.isfinite(h)):
        raise ValueError("trajectory_derivative_step_N must lie in (0,0.03)")
    center = candidate_c_stueckelberg_physical_action(
        a, k_hmpc=k_hmpc, derivative_step_N=action_derivative_step_N,
    )
    samples = {}
    for offset in (-3, -2, -1, 1, 2, 3):
        samples[offset] = candidate_c_stueckelberg_physical_action(
            a*math.exp(offset*h), k_hmpc=k_hmpc,
            derivative_step_N=action_derivative_step_N,
        ).physical_phase_hessian
    HN = (
        -samples[-3] + 9.0*samples[-2] - 45.0*samples[-1]
        + 45.0*samples[1] - 9.0*samples[2] + samples[3]
    ) / (60.0*h)
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    return dust_dae_local_system(
        center.physical_phase_hessian, HN,
        H_g=point.metric.H/point.metric.a,
    )


def candidate_c_stueckelberg_local_squared_speeds(
    a: float,
    *,
    k_hmpc: float,
    action_derivative_step_N: float = 2.0e-3,
    trajectory_derivative_step_N: float = 2.0e-3,
) -> np.ndarray:
    point = candidate_c_dust_background_point(a, k_hmpc=k_hmpc)
    system = candidate_c_stueckelberg_local_system(
        a,
        k_hmpc=k_hmpc,
        action_derivative_step_N=action_derivative_step_N,
        trajectory_derivative_step_N=trajectory_derivative_step_N,
    )
    return local_phase_squared_speeds(
        system, a=a, k=math.sqrt(point.metric.k2),
    )
