"""Compact native flat-gauge EH+HR action for finite-mu spherical Stückelberg audits."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np

from numerics.nonhomothetic_compact_hr_correction import _profile
from numerics.nonhomothetic_hr_relative_native import relative_native_geometry, relative_native_hr_density
from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density


@dataclass(frozen=True)
class CompactNativeGravityHessian:
    gradient: np.ndarray
    hessian: np.ndarray
    metric_rank: int
    metric_condition_number: float


@dataclass(frozen=True)
class CompactNativeMetricSchur:
    total_gradient: np.ndarray
    total_hessian: np.ndarray
    reduced_gradient: np.ndarray
    reduced_hessian: np.ndarray
    metric_rank: int
    metric_condition_number: float


def _action(x, *, betas,a,n,alpha,a_dot_over_a,a_ddot_over_a,
            n_dot_over_n,n_ddot_over_n,alpha_dot_over_alpha,alpha_ddot_over_alpha,
            mu,mu_dot,s,s_dot,time_radius,radial_radius,interaction_mass2,
            planck_ratio,quadrature_order):
    q=np.asarray(x,float)
    if q.shape!=(6,) or not np.all(np.isfinite(q)):
        raise ValueError('native compact amplitudes must be six finite values')
    L0,T0,Pg0,Pf0,Bg0,Bf0=[float(v) for v in q]
    xt,wt=np.polynomial.legendre.leggauss(int(quadrature_order))
    xr,wr=np.polynomial.legendre.leggauss(int(quadrature_order))
    ts=time_radius*xt; rs=.5*radial_radius*(xr+1.0)
    tw=time_radius*wt; rw=.5*radial_radius*wr
    total=0.0
    for i,t in enumerate(ts):
        ac=a*(1+a_dot_over_a*t+.5*a_ddot_over_a*t*t)
        ac_dot=a*(a_dot_over_a+a_ddot_over_a*t)
        if ac<=0:
            raise ValueError('compact support left positive g background')
        for j,r in enumerate(rs):
            chi,chi_t,chi_r,chi_tr,chi_rr,_=_profile(float(t),float(r),time_radius,radial_radius)
            Tfield=T0*chi; Tdot=T0*chi_t; Tr=T0*chi_r
            Lr=L0*chi_r; Ldotr=L0*chi_tr; Lrr=L0*chi_rr
            Pg=Pg0*chi; Ug=Bg0*chi_r; Ug_r=Bg0*chi_rr

            geom=relative_native_geometry(
                a=a,n=n,alpha=alpha,r=float(r),
                a_dot_over_a=a_dot_over_a,a_ddot_over_a=a_ddot_over_a,
                common_time_offset=float(t),
                n_dot_over_n=n_dot_over_n,n_ddot_over_n=n_ddot_over_n,
                alpha_dot_over_alpha=alpha_dot_over_alpha,
                alpha_ddot_over_alpha=alpha_ddot_over_alpha,
                mu=mu,mu_dot=mu_dot,s=s,s_dot=s_dot,
                T=Tfield,T_dot=Tdot,T_r=Tr,
                L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
                Phi_g=Pg,B_g_r=Ug,Phi_f=0.0,B_f_r=0.0,
            )
            tf=geom.f_time; rf=geom.f_radius
            chif,_,chif_r,_,chif_rr,_=_profile(float(tf),float(rf),time_radius,radial_radius)
            Pf=Pf0*chif; Uf=Bf0*chif_r; Uf_r=Bf0*chif_rr

            geom=relative_native_geometry(
                a=a,n=n,alpha=alpha,r=float(r),
                a_dot_over_a=a_dot_over_a,a_ddot_over_a=a_ddot_over_a,
                common_time_offset=float(t),
                n_dot_over_n=n_dot_over_n,n_ddot_over_n=n_ddot_over_n,
                alpha_dot_over_alpha=alpha_dot_over_alpha,
                alpha_ddot_over_alpha=alpha_ddot_over_alpha,
                mu=mu,mu_dot=mu_dot,s=s,s_dot=s_dot,
                T=Tfield,T_dot=Tdot,T_r=Tr,
                L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
                Phi_g=Pg,B_g_r=Ug,Phi_f=Pf,B_f_r=Uf,
            )
            hr=relative_native_hr_density(
                betas=betas,m2=1.0,Mg2=1.0,
                a=a,n=n,alpha=alpha,r=float(r),
                a_dot_over_a=a_dot_over_a,a_ddot_over_a=a_ddot_over_a,
                common_time_offset=float(t),
                n_dot_over_n=n_dot_over_n,n_ddot_over_n=n_ddot_over_n,
                alpha_dot_over_alpha=alpha_dot_over_alpha,
                alpha_ddot_over_alpha=alpha_ddot_over_alpha,
                mu=mu,mu_dot=mu_dot,s=s,s_dot=s_dot,
                T=Tfield,T_dot=Tdot,T_r=Tr,
                L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
                Phi_g=Pg,B_g_r=Ug,Phi_f=Pf,B_f_r=Uf,
            )
            eg=flat_spherical_adm_eh_density(
                scale_factor=ac,scale_rate=ac_dot,background_lapse=1.0,r=float(r),
                Phi=Pg,shift=Ug,shift_r=Ug_r)
            alpha_f=geom.alpha_f
            alpha_f_dot=alpha*(alpha_dot_over_alpha+alpha_ddot_over_alpha*tf)
            ef_native=flat_spherical_adm_eh_density(
                scale_factor=alpha_f,scale_rate=alpha_f_dot,background_lapse=geom.n_f,r=float(rf),
                Phi=Pf,shift=Uf,shift_r=Uf_r)
            jac=abs(float(np.linalg.det(geom.jacobian_f)))
            dens=0.5*eg + 0.5*planck_ratio*jac*ef_native - interaction_mass2*hr
            total += tw[i]*rw[j]*dens
    return float(total)


def compact_native_gravity_hessian(*,betas,a,n,alpha,
        a_dot_over_a=0.0,a_ddot_over_a=0.0,n_dot_over_n=0.0,n_ddot_over_n=0.0,
        alpha_dot_over_alpha=0.0,alpha_ddot_over_alpha=0.0,
        mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,time_radius,radial_radius,
        interaction_mass2,planck_ratio=1.0,amplitude_step=5e-4,quadrature_order=16):
    vals=(a,n,alpha,a_dot_over_a,a_ddot_over_a,n_dot_over_n,n_ddot_over_n,
          alpha_dot_over_alpha,alpha_ddot_over_alpha,mu,mu_dot,s,s_dot,
          time_radius,radial_radius,interaction_mass2,planck_ratio,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError('native compact gravity inputs must be finite')
    if a<=0 or n<=0 or alpha<=0 or mu<=-1 or time_radius<=0 or radial_radius<=0 or planck_ratio<=0 or amplitude_step<=0:
        raise ValueError('invalid native compact gravity inputs')
    if interaction_mass2<0 or quadrature_order<12:
        raise ValueError('interaction mass must be nonnegative and quadrature_order >= 12')
    kw=dict(betas=tuple(betas),a=float(a),n=float(n),alpha=float(alpha),
        a_dot_over_a=float(a_dot_over_a),a_ddot_over_a=float(a_ddot_over_a),
        n_dot_over_n=float(n_dot_over_n),n_ddot_over_n=float(n_ddot_over_n),
        alpha_dot_over_alpha=float(alpha_dot_over_alpha),alpha_ddot_over_alpha=float(alpha_ddot_over_alpha),
        mu=float(mu),mu_dot=float(mu_dot),s=float(s),s_dot=float(s_dot),
        time_radius=float(time_radius),radial_radius=float(radial_radius),
        interaction_mass2=float(interaction_mass2),planck_ratio=float(planck_ratio),
        quadrature_order=int(quadrature_order))
    z=np.zeros(6); f0=_action(z,**kw); h=float(amplitude_step)
    scales=np.array([h*radial_radius**2,h,h,h,h*radial_radius,h*radial_radius],float)
    g=np.zeros(6); H=np.zeros((6,6))
    for i in range(6):
        ei=np.zeros(6); ei[i]=scales[i]
        fp=_action(ei,**kw); fm=_action(-ei,**kw)
        g[i]=(fp-fm)/(2*scales[i])
        H[i,i]=(fp-2*f0+fm)/(scales[i]**2)
        for j in range(i+1,6):
            ej=np.zeros(6); ej[j]=scales[j]
            H[i,j]=H[j,i]=(_action(ei+ej,**kw)-_action(ei-ej,**kw)-_action(-ei+ej,**kw)+_action(-ei-ej,**kw))/(4*scales[i]*scales[j])
    H=0.5*(H+H.T)
    mm=H[2:,2:]
    scale=max(1.0,float(np.linalg.norm(mm,ord=2)))
    rank=int(np.linalg.matrix_rank(mm,tol=1e-11*scale))
    cond=float(np.linalg.cond(mm)) if rank==4 else float('inf')
    return CompactNativeGravityHessian(g,H,rank,cond)


def reduce_compact_native_metric_block(**kwargs):
    out=compact_native_gravity_hessian(**kwargs)
    H=out.hessian; g=out.gradient; Hmm=H[2:,2:]
    if out.metric_rank<4:
        raise np.linalg.LinAlgError('native compact metric block is rank deficient')
    Hsm=H[:2,2:]
    redH=H[:2,:2]-Hsm@np.linalg.solve(Hmm,H[2:,:2])
    redg=g[:2]-Hsm@np.linalg.solve(Hmm,g[2:])
    return CompactNativeMetricSchur(g,H,np.asarray(redg),np.asarray(redH),out.metric_rank,out.metric_condition_number)
