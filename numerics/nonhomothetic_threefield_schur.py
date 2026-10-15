"""Compact three-physical-field Schur system: (pi, q_g, q_f) plus four metrics."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.nonhomothetic_linear_pi_action import compact_hr_linear_pi_five_field_hessian
from numerics.spherical_eh_compact_action import compact_eh_amplitude_derivatives_taylor
from numerics.spherical_kessence_compact_action import compact_kessence_hessian

@dataclass(frozen=True)
class NonhomotheticThreeFieldSchurResult:
    total_hessian: np.ndarray
    reduced_physical_hessian: np.ndarray
    metric_rank: int
    metric_condition_number: float


def _embed(dst,src,indices):
    for i,ii in enumerate(indices):
        for j,jj in enumerate(indices):
            dst[ii,jj]+=src[i,j]


def reduce_nonhomothetic_threefield_metric_block(*,betas,jet,time_radius,radial_radius,
        interaction_mass2,planck_ratio,rho_g,rho_f,cs2_g,cs2_f,
        pressure_g=0.0,pressure_f=0.0,amplitude_step=2e-5,quadrature_order=14):
    vals=(time_radius,radial_radius,interaction_mass2,planck_ratio,rho_g,rho_f,cs2_g,cs2_f,amplitude_step,jet.c)
    if not all(math.isfinite(float(v)) for v in vals): raise ValueError('inputs must be finite')
    if min(time_radius,radial_radius,planck_ratio,rho_g,rho_f,cs2_g,cs2_f,amplitude_step,jet.c)<=0 or interaction_mass2<0:
        raise ValueError('invalid three-field inputs')
    T=float(time_radius); R=float(radial_radius); h=float(amplitude_step); n=int(quadrature_order)
    # Ordering: pi,qg,qf,phi_g,psi_g,phi_f,psi_f
    total=np.zeros((7,7),float)
    hr=compact_hr_linear_pi_five_field_hessian(betas=betas,jet=jet,time_radius=T,radial_radius=R,amplitude_step=h,quadrature_order=n)
    _embed(total,-float(interaction_mass2)*hr.hessian,[0,3,4,5,6])
    eg=compact_eh_amplitude_derivatives_taylor(a0=jet.a,ap0=jet.a_p,app0=jet.a_pp,time_radius=T,radial_radius=R,amplitude_step=h,quadrature_order=n)
    _embed(total,.5*eg.hessian,[3,4])
    f=jet.f_native; Tf=jet.c*T
    ef=compact_eh_amplitude_derivatives_taylor(a0=f.b,ap0=f.b_f_p,app0=f.b_f_pp,time_radius=Tf,radial_radius=R,amplitude_step=h,quadrature_order=n)
    _embed(total,.5*float(planck_ratio)*ef.hessian,[5,6])
    mg=compact_kessence_hessian(a0=jet.a,ap0=jet.a_p,app0=jet.a_pp,rho=rho_g,pressure=pressure_g,cs2=cs2_g,time_radius=T,radial_radius=R,amplitude_step=h,quadrature_order=n)
    _embed(total,mg.hessian,[1,3,4])
    mf=compact_kessence_hessian(a0=f.b,ap0=f.b_f_p,app0=f.b_f_pp,rho=rho_f,pressure=pressure_f,cs2=cs2_f,time_radius=Tf,radial_radius=R,amplitude_step=h,quadrature_order=n)
    _embed(total,mf.hessian,[2,5,6])
    mm=total[3:,3:]; scale=float(np.linalg.norm(mm,2))
    if not math.isfinite(scale) or scale<=0: raise np.linalg.LinAlgError('metric block scale invalid')
    rank=int(np.linalg.matrix_rank(mm,tol=1e-11*scale))
    if rank<4: raise np.linalg.LinAlgError('metric block rank deficient')
    Hpm=total[:3,3:]
    red=total[:3,:3]-Hpm@np.linalg.solve(mm,total[3:,:3])
    return NonhomotheticThreeFieldSchurResult(total_hessian=total,reduced_physical_hessian=red,metric_rank=rank,metric_condition_number=float(np.linalg.cond(mm)))
