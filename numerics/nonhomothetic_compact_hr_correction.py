"""Compact-support finite-mu HR correction in native relative variables."""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.nonhomothetic_hr_relative_native import relative_native_hr_density


@dataclass(frozen=True)
class CompactRelativeHRCorrection:
    gradient: np.ndarray
    hessian: np.ndarray
    background_action: float


def _profile(t,r,T,R):
    """C2 compact profile and the derivatives needed by the pullback."""
    if abs(t) >= T or r <= 0.0 or r >= R:
        return (0.0,)*6
    x=t/T
    A=(1.0-x*x)**3
    At=(-6.0*x*(1.0-x*x)**2)/T
    F=r*r-3.0*r**4/R**2+3.0*r**6/R**4-r**8/R**6
    Fr=2.0*r-12.0*r**3/R**2+18.0*r**5/R**4-8.0*r**7/R**6
    Frr=2.0-36.0*r**2/R**2+90.0*r**4/R**4-56.0*r**6/R**6
    return A*F, At*F, A*Fr, At*Fr, A*Frr, F


def _compact_action(x,*,betas,a,n,alpha,n_dot_over_n,n_ddot_over_n,
                    alpha_dot_over_alpha,alpha_ddot_over_alpha,
                    mu,mu_dot,s,s_dot,time_radius,radial_radius,
                    quadrature_order,m2,Mg2):
    q=np.asarray(x,float)
    if q.shape!=(6,) or not np.all(np.isfinite(q)):
        raise ValueError('compact amplitudes must be six finite values')
    L0,T0,Pg0,Pf0,Bg0,Bf0=[float(v) for v in q]
    xt,wt=np.polynomial.legendre.leggauss(int(quadrature_order))
    xr,wr=np.polynomial.legendre.leggauss(int(quadrature_order))
    ts=time_radius*xt; rs=.5*radial_radius*(xr+1.0)
    tw=time_radius*wt; rw=.5*radial_radius*wr
    total=0.0
    for i,t in enumerate(ts):
        for j,r in enumerate(rs):
            chi,chi_t,chi_r,chi_tr,chi_rr,_=_profile(float(t),float(r),time_radius,radial_radius)
            Tfield=T0*chi; Tdot=T0*chi_t; Tr=T0*chi_r
            Lr=L0*chi_r; Ldotr=L0*chi_tr; Lrr=L0*chi_rr
            Pg=Pg0*chi; Bg_r=Bg0*chi_r

            # Evaluate the native f perturbation profile separately in the
            # finite-mu and mu=0 pullbacks. Reusing the finite-mu sample in
            # the reference action would not be a genuine action subtraction.
            tf=.5*s*r*r-Tfield
            Rf=(1.0+mu)*r-Lr
            chif,_,chif_r,_,_,_=_profile(float(tf),float(Rf),time_radius,radial_radius)
            finite=relative_native_hr_density(
                betas=betas,m2=m2,Mg2=Mg2,
                a=a,n=n,alpha=alpha,r=float(r),
                n_dot_over_n=n_dot_over_n,n_ddot_over_n=n_ddot_over_n,
                alpha_dot_over_alpha=alpha_dot_over_alpha,
                alpha_ddot_over_alpha=alpha_ddot_over_alpha,
                mu=mu,mu_dot=mu_dot,s=s,s_dot=s_dot,
                T=Tfield,T_dot=Tdot,T_r=Tr,
                L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
                Phi_g=Pg,B_g_r=Bg_r,Phi_f=Pf0*chif,B_f_r=Bf0*chif_r,
            )
            tf0=-Tfield
            Rf0=r-Lr
            chif0,_,chif0_r,_,_,_=_profile(float(tf0),float(Rf0),time_radius,radial_radius)
            reference=relative_native_hr_density(
                betas=betas,m2=m2,Mg2=Mg2,
                a=a,n=n,alpha=alpha,r=float(r),
                n_dot_over_n=n_dot_over_n,n_ddot_over_n=n_ddot_over_n,
                alpha_dot_over_alpha=alpha_dot_over_alpha,
                alpha_ddot_over_alpha=alpha_ddot_over_alpha,
                mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,
                T=Tfield,T_dot=Tdot,T_r=Tr,
                L_r=Lr,L_dot_r=Ldotr,L_rr=Lrr,
                Phi_g=Pg,B_g_r=Bg_r,Phi_f=Pf0*chif0,B_f_r=Bf0*chif0_r,
            )
            total += tw[i]*rw[j]*(finite-reference)
    return float(total)


def compact_relative_hr_correction_hessian(*,betas,a,n,alpha,
        n_dot_over_n=0.0,n_ddot_over_n=0.0,
        alpha_dot_over_alpha=0.0,alpha_ddot_over_alpha=0.0,
        mu=0.0,mu_dot=0.0,s=0.0,s_dot=0.0,
        time_radius,radial_radius,m2=1.0,Mg2=1.0,
        amplitude_step=5e-4,quadrature_order=18):
    vals=(a,n,alpha,n_dot_over_n,n_ddot_over_n,alpha_dot_over_alpha,
          alpha_ddot_over_alpha,mu,mu_dot,s,s_dot,time_radius,radial_radius,
          m2,Mg2,amplitude_step)
    if not all(math.isfinite(float(v)) for v in vals):
        raise ValueError('compact correction inputs must be finite')
    if a<=0 or n<=0 or alpha<=0 or mu<=-1 or time_radius<=0 or radial_radius<=0 or amplitude_step<=0:
        raise ValueError('invalid compact correction inputs')
    if quadrature_order < 12:
        raise ValueError('quadrature_order must be at least 12')
    kw=dict(betas=tuple(betas),a=float(a),n=float(n),alpha=float(alpha),
        n_dot_over_n=float(n_dot_over_n),n_ddot_over_n=float(n_ddot_over_n),
        alpha_dot_over_alpha=float(alpha_dot_over_alpha),alpha_ddot_over_alpha=float(alpha_ddot_over_alpha),
        mu=float(mu),mu_dot=float(mu_dot),s=float(s),s_dot=float(s_dot),
        time_radius=float(time_radius),radial_radius=float(radial_radius),
        quadrature_order=int(quadrature_order),m2=float(m2),Mg2=float(Mg2))
    z=np.zeros(6); f0=_compact_action(z,**kw)
    # The profile carries two radial derivatives of L, so scale its probe with R^2.
    h=float(amplitude_step)
    scales=np.array([h*radial_radius**2,h,h,h,h*radial_radius,h*radial_radius],float)
    g=np.zeros(6); H=np.zeros((6,6))
    for i in range(6):
        ei=np.zeros(6); ei[i]=scales[i]
        fp=_compact_action(ei,**kw); fm=_compact_action(-ei,**kw)
        g[i]=(fp-fm)/(2*scales[i])
        H[i,i]=(fp-2*f0+fm)/(scales[i]**2)
        for j in range(i+1,6):
            ej=np.zeros(6); ej[j]=scales[j]
            hij=(_compact_action(ei+ej,**kw)-_compact_action(ei-ej,**kw)
                 -_compact_action(-ei+ej,**kw)+_compact_action(-ei-ej,**kw))/(4*scales[i]*scales[j])
            H[i,j]=H[j,i]=hij
    return CompactRelativeHRCorrection(np.asarray(g),0.5*(H+H.T),float(f0))
