"""Compact metric Schur reduction for the linear non-homothetic pi map."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.nonhomothetic_linear_pi_action import compact_hr_linear_pi_five_field_hessian
from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives_taylor

@dataclass(frozen=True)
class NonhomotheticLinearPiSchurResult:
    total_hessian: np.ndarray
    reduced_pi_hessian: float
    metric_condition_number: float


def reduce_nonhomothetic_linear_pi_metric_block(*,betas,jet,time_radius,radial_radius,
        interaction_mass2,planck_ratio=1.0,amplitude_step=3e-5,quadrature_order=14):
    vals=(time_radius,radial_radius,interaction_mass2,planck_ratio,amplitude_step,jet.c)
    if not all(math.isfinite(float(v)) for v in vals) or min(time_radius,radial_radius,planck_ratio,amplitude_step,jet.c)<=0 or interaction_mass2<0:
        raise ValueError('invalid linear-pi Schur inputs')
    hr=compact_hr_linear_pi_five_field_hessian(betas=betas,jet=jet,time_radius=time_radius,
        radial_radius=radial_radius,amplitude_step=amplitude_step,quadrature_order=quadrature_order)
    eg=compact_eh_amplitude_derivatives_taylor(a0=jet.a,ap0=jet.a_p,app0=jet.a_pp,
        time_radius=time_radius,radial_radius=radial_radius,amplitude_step=amplitude_step,quadrature_order=quadrature_order)
    f=jet.f_native
    ef=compact_eh_amplitude_derivatives_taylor(a0=f.b,ap0=f.b_f_p,app0=f.b_f_pp,
        time_radius=jet.c*time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order)
    total=-float(interaction_mass2)*np.asarray(hr.hessian,float)
    total=total.copy(); total[1:3,1:3]+=.5*eg.hessian; total[3:5,3:5]+=.5*float(planck_ratio)*ef.hessian
    mm=total[1:,1:]; scale=float(np.linalg.norm(mm,2))
    if not math.isfinite(scale) or scale<=0: raise np.linalg.LinAlgError('metric block has zero/nonfinite scale')
    if np.linalg.matrix_rank(mm,tol=1e-11*scale)<4: raise np.linalg.LinAlgError('metric block rank deficient')
    cp=total[0,1:]
    red=float(total[0,0]-cp@np.linalg.solve(mm,cp))
    return NonhomotheticLinearPiSchurResult(total_hessian=total,reduced_pi_hessian=red,metric_condition_number=float(np.linalg.cond(mm)))
