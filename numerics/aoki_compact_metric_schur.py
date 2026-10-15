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
    total_gradient: np.ndarray
    total_hessian: np.ndarray
    metric_condition_number: float
    metric_rank: int
    reduced_pi_gradient: float
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

    hr_out=compact_hr_five_field_hessian(
        betas=betas,K=K,w=w,mu=mu,conformal_H=conformal_H,
        time_radius=time_radius,radial_radius=radial_radius,
        amplitude_step=amplitude_step,quadrature_order=quadrature_order,
    )
    hr=hr_out.hessian
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

    total_gradient=-float(interaction_mass2)*np.asarray(hr_out.gradient,dtype=float)
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
    reduced_gradient=float(total_gradient[0]-coupling@np.linalg.solve(mm,total_gradient[1:]))
    reduced=float(total[0,0]-coupling@np.linalg.solve(mm,coupling))
    return CompactMetricSchurResult(
        hr_hessian=hr,total_gradient=total_gradient,total_hessian=total,
        metric_condition_number=cond,metric_rank=rank,
        reduced_pi_gradient=reduced_gradient,reduced_pi_hessian=reduced,
    )

@dataclass(frozen=True)
class ReducedCompactPiCoefficients:
    kinetic_hessian_coefficient: float
    gradient_hessian_coefficient: float
    sound_speed_squared: float
    fit_residual: float


def _profile_integrals(T,R,order):
    xt,wt=np.polynomial.legendre.leggauss(order)
    xr,wr=np.polynomial.legendre.leggauss(order)
    t=T*xt; r=0.5*R*(xr+1.0)
    tw=T*wt; rw=0.5*R*wr
    x=t[:,None]/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    rr=r[None,:]
    F=rr*rr-3.0*rr**4/R**2+3.0*rr**6/R**4-rr**8/R**6
    Fr=2.0*rr-12.0*rr**3/R**2+18.0*rr**5/R**4-8.0*rr**7/R**6
    W=tw[:,None]*rw[None,:]
    ik=float(np.sum(W*rr**2*(At*F)**2))
    ig=float(np.sum(W*rr**2*(A*Fr)**2))
    return ik,ig


def recover_reduced_pi_coefficients(*, betas,K,w,mu,interaction_mass2,planck_ratio,
                                    time_scales=(0.5,1.0,2.0),radius=1.0,
                                    hubble_step=0.007,amplitude_step=2e-3,
                                    quadrature_order=18):
    rows=[]; rhs=[]
    for T in time_scales:
        common=dict(
            betas=betas,K=K,w=w,mu=mu,time_radius=float(T),radial_radius=radius,
            interaction_mass2=interaction_mass2,planck_ratio=planck_ratio,
            amplitude_step=amplitude_step,quadrature_order=quadrature_order,
        )
        hp=reduce_compact_metric_block(conformal_H=+hubble_step,**common).reduced_pi_hessian
        hm=reduce_compact_metric_block(conformal_H=-hubble_step,**common).reduced_pi_hessian
        h0=reduce_compact_metric_block(conformal_H=0.0,**common).reduced_pi_hessian
        h2=(hp+hm-2.0*h0)/(2.0*hubble_step*hubble_step)
        ik,ig=_profile_integrals(float(T),radius,quadrature_order)
        rows.append((ik,ig)); rhs.append(h2)
    X=np.asarray(rows,dtype=float); y=np.asarray(rhs,dtype=float)
    coeff,_,rank,_=np.linalg.lstsq(X,y,rcond=None)
    if rank!=2 or abs(coeff[0])<1e-20:
        raise np.linalg.LinAlgError("reduced compact pi fit is rank deficient")
    residual=float(np.linalg.norm(X@coeff-y)/max(1.0,np.linalg.norm(y)))
    return ReducedCompactPiCoefficients(
        kinetic_hessian_coefficient=float(coeff[0]),
        gradient_hessian_coefficient=float(coeff[1]),
        sound_speed_squared=float(-coeff[1]/coeff[0]),
        fit_residual=residual,
    )
