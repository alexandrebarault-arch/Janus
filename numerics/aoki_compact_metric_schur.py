"""Compact quadratic Schur reduction of weak metric potentials around Aoki control backgrounds."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from numerics.aoki_compact_metric_pi_action import compact_hr_five_field_hessian
from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives


@dataclass(frozen=True)
class CompactMetricSchurResult:
    hr_hessian: np.ndarray
    total_hessian: np.ndarray
    metric_condition_number: float
    metric_rank: int
    reduced_pi_hessian: float


def reduce_compact_metric_block(*, betas,K,w,mu,conformal_H,
                                time_radius,radial_radius,
                                interaction_mass2,planck_ratio=1.0,
                                amplitude_step=7e-4,quadrature_order=16):
    vals=(K,w,mu,conformal_H,time_radius,radial_radius,
          interaction_mass2,planck_ratio,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("all compact Schur inputs must be finite")
    if K<=0 or mu<=-1 or time_radius<=0 or radial_radius<=0 or amplitude_step<=0:
        raise ValueError("invalid compact Schur inputs")
    if interaction_mass2<0 or planck_ratio<=0:
        raise ValueError("mass squared must be nonnegative and Planck ratio positive")

    hr=compact_hr_five_field_hessian(
        betas=betas,K=K,w=w,mu=mu,conformal_H=conformal_H,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    ).hessian
    eg=compact_eh_amplitude_derivatives(
        a0=1.0,conformal_H=conformal_H,w=w,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    ).hessian
    ef=compact_eh_amplitude_derivatives(
        a0=K,conformal_H=conformal_H,w=w,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    ).hessian

    total=-float(interaction_mass2)*hr
    total=np.asarray(total,dtype=float).copy()
    total[1:3,1:3] += 0.5*eg
    total[3:5,3:5] += 0.5*float(planck_ratio)*ef
    mm=total[1:,1:]
    scale=max(1.0,float(np.linalg.norm(mm,ord=2)))
    rank=int(np.linalg.matrix_rank(mm,tol=1e-11*scale))
    cond=float(np.linalg.cond(mm))
    if rank<4:
        raise np.linalg.LinAlgError("compact weak-metric block is rank deficient")
    coupling=total[0,1:]
    reduced=float(total[0,0]-coupling@np.linalg.solve(mm,coupling))
    return CompactMetricSchurResult(
        hr_hessian=hr,total_hessian=total,
        metric_condition_number=cond,metric_rank=rank,
        reduced_pi_hessian=reduced,
    )
