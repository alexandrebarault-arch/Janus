"""Schur reduction of compact weak-metric amplitudes on non-homothetic jets."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_compact_sixfield_action import compact_hr_six_field_hessian_nonhomothetic
from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives_taylor


@dataclass(frozen=True)
class NonhomotheticCompactMetricSchurResult:
    total_gradient: np.ndarray
    total_hessian: np.ndarray
    reduced_stueckelberg_gradient: np.ndarray
    reduced_stueckelberg_hessian: np.ndarray
    metric_rank: int
    metric_condition_number: float


def reduce_nonhomothetic_compact_metric_block(*,betas,jet,mu,mu_p=0.0,mu_pp=0.0,
                                               time_radius,radial_radius,
                                               interaction_mass2,planck_ratio=1.0,
                                               amplitude_step=7e-4,quadrature_order=16):
    vals=(mu,mu_p,mu_pp,time_radius,radial_radius,interaction_mass2,planck_ratio,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError("nonhomothetic Schur inputs must be finite")
    if mu<=-1 or time_radius<=0 or radial_radius<=0 or interaction_mass2<0 or planck_ratio<=0 or amplitude_step<=0:
        raise ValueError("invalid nonhomothetic Schur inputs")

    hr=compact_hr_six_field_hessian_nonhomothetic(
        betas=betas,jet=jet,mu=mu,mu_p=mu_p,mu_pp=mu_pp,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    )
    eg=compact_eh_amplitude_derivatives_taylor(
        a0=jet.a,ap0=jet.a_p,app0=jet.a_pp,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    )
    fj=jet.f_native
    ef=compact_eh_amplitude_derivatives_taylor(
        a0=fj.b,ap0=fj.b_f_p,app0=fj.b_f_pp,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    )

    total_gradient=-float(interaction_mass2)*np.asarray(hr.gradient,float)
    total=-float(interaction_mass2)*np.asarray(hr.hessian,float)
    total=total.copy()
    total[2:4,2:4]+=0.5*np.asarray(eg.hessian,float)
    total[4:6,4:6]+=0.5*float(planck_ratio)*np.asarray(ef.hessian,float)

    Hmm=total[2:,2:]
    Hsm=total[:2,2:]
    Hms=total[2:,:2]
    scale=float(np.linalg.norm(Hmm,ord=2))
    if not math.isfinite(scale) or scale <= 0.0:
        raise np.linalg.LinAlgError("nonhomothetic compact metric block has zero/nonfinite scale")
    rank=int(np.linalg.matrix_rank(Hmm,tol=1e-11*scale))
    if rank<4:
        raise np.linalg.LinAlgError("nonhomothetic compact metric block is rank deficient")
    cond=float(np.linalg.cond(Hmm))
    reduced_H=total[:2,:2]-Hsm@np.linalg.solve(Hmm,Hms)
    reduced_g=total_gradient[:2]-Hsm@np.linalg.solve(Hmm,total_gradient[2:])
    return NonhomotheticCompactMetricSchurResult(
        total_gradient=np.asarray(total_gradient,float),
        total_hessian=np.asarray(total,float),
        reduced_stueckelberg_gradient=np.asarray(reduced_g,float),
        reduced_stueckelberg_hessian=np.asarray(reduced_H,float),
        metric_rank=rank,metric_condition_number=cond,
    )
