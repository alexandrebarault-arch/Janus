"""Restricted flat-spatial-gauge native EH control on the finite-mu HR+dust basis.

Only lapse/shift perturbations are included in EH: native psi and E
remain zero in THIS EH sub-block even though HR has those slots. This
restriction prevents treating the result as a complete Einstein-Hilbert
scalar action. No chart-perturbation variation of native EH is included.
The native f shift derivative uses the full background inverse Jacobian.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np
from numerics.hr_compact_radial_interaction import compact_scalar_profile
from numerics.hr_two_dust_preconstraint import assemble_hr_two_dust_preconstraint

@dataclass(frozen=True)
class FlatEHRestrictedBridge:
    hessian: np.ndarray
    eh_hessian: np.ndarray
    hr_hessian: np.ndarray
    dust_hessian: np.ndarray
    gradient: np.ndarray
    radius: float
    quadrature_order: int
    metric_subblock_rank: int
    metric_subblock_condition: float


def native_flat_eh_local_hessian(*,scale,rate,lapse,r,phi,shift,shift_r):
    """Exact second derivative of N sqrt(h)(Kij Kij-K^2) in Phi and U.

    Vectors phi, shift, shift_r are linear forms in action amplitudes.
    The native spatial metric is EXACTLY a^2 diag(1,r^2,r^2 sin²theta).
    No overall M^2/2 or angular measure is included.
    """
    a=float(scale); ad=float(rate); n=float(lapse); R=float(r)
    if not all(math.isfinite(x) for x in (a,ad,n,R)) or min(a,n,R)<=0:
        raise ValueError('regular positive native flat EH background required')
    p,u,ur=[np.asarray(v,dtype=float) for v in (phi,shift,shift_r)]
    if p.ndim!=1 or u.shape!=p.shape or ur.shape!=p.shape or not np.all(np.isfinite(np.stack((p,u,ur)))):
        raise ValueError('finite same-size linear amplitude vectors required')
    h=ad/a;g=n/a
    sym=lambda x,y:np.outer(x,y)+np.outer(y,x)
    factor=a**3*R**2/n
    H=factor*(
        -18*h*h*np.outer(p,p)
        -4*h*g*sym(p,ur)
        -8*h*g/R*sym(p,u)
        +(6*h*h-4*g*g/R**2)*np.outer(u,u)
        -4*g*g/R*sym(u,ur)
    )
    return .5*(H+H.T)


def flat_eh_compact_restricted_hessian(*,radius,quadrature_order=24,
         N,a,g_scale_rate,n,alpha,n_dot=0.,alpha_dot=0.,
         n_ddot=0.,alpha_ddot=0.,mu=0.,mu_dot=0.,sigma_r=0.,
         sigma_dot=0.,planck_ratio=1.):
    """Return 22x22 g/f native flat-gauge ADM EH Hessian in existing basis.

    Time-local common coordinate r quadrature. Native f rate alpha_dot is
    d(alpha)/dT in f-native time; n(T),alpha(T) Taylor-sampled at
    T-t=sigma*r²/2. f lapse/shift and shift time derivative are common-
    chart amplitudes, but f shift radial derivative uses the inverse J.
    EH evaluated on the *unperturbed* chart only, so T/L chart columns
    are intentionally zero here; full finite-mu EH assembly still RED.
    """
    values=(radius,N,a,g_scale_rate,n,alpha,n_dot,alpha_dot,n_ddot,
            alpha_ddot,mu,mu_dot,sigma_r,sigma_dot,planck_ratio)
    if not all(math.isfinite(float(x)) for x in values) or min(radius,N,a,n,alpha,planck_ratio)<=0 or mu<=-1:
        raise ValueError('invalid restricted EH/background inputs')
    if type(quadrature_order) is not int or quadrature_order<8:
        raise ValueError('quadrature_order must be an integer >= 8')
    nodes,ws=np.polynomial.legendre.leggauss(quadrature_order)
    H=np.zeros((22,22))
    unit=np.eye(22)
    for q,w in zip(nodes,ws):
        r=.5*radius*(1+q)
        F,Fr,Frr,_=compact_scalar_profile(r,radius)
        weight=2*math.pi*radius*w
        # g native chart exactly the common chart.
        Hg=native_flat_eh_local_hessian(scale=a,rate=g_scale_rate,lapse=N,r=r,
            phi=F*unit[0],shift=Fr*unit[1],shift_r=Frr*unit[1])
        # f native chart: radial profiles are common-r functions;
        # use J^-T before evaluating the native ADM shift derivative.
        t_t=1+.5*sigma_dot*r*r
        t_r=sigma_r*r
        r_t=mu_dot*r
        r_r=1+mu
        D=t_t*r_r-t_r*r_t
        if D<=0:raise ValueError('f chart Jacobian has nonpositive determinant')
        offset=.5*sigma_r*r*r
        nt=n+n_dot*offset+.5*n_ddot*offset*offset
        at=alpha+alpha_dot*offset+.5*alpha_ddot*offset*offset
        arate=alpha_dot+alpha_ddot*offset
        if min(nt,at)<=0:raise ValueError('native f background Taylor sample invalid')
        rf=r_r*r
        # Native f shift U_f = B_f(t) * F_r(r), including B_fdot in U_R.
        # Scalar radial profile is the one inherited from k B_f in HR.
        U=Fr*unit[5]
        U_R=(t_t*Frr*unit[5]-t_r*Fr*unit[13])/D
        Hf=native_flat_eh_local_hessian(scale=at,rate=arate,lapse=nt,r=rf,
            phi=F*unit[4],shift=U,shift_r=U_R)
        H+=weight*(.5*Hg +.5*planck_ratio*D*Hf)
    return .5*(H+H.T)


def assemble_flat_eh_hr_two_dust_restricted(*,radius,quadrature_order=24,
         rho_g,rho_f,g_scale_rate,planck_ratio=1.,
         log_phidot_rate_g=0.,log_phidot_rate_f=0.,**hr_parameters):
    """Combine restricted EH with earlier HR + exact-dust action, no Schur.

    Important: the result is an interface test only. Missing spatial
    scalar EH trace/shear and EH chart perturbation columns MUST be
    supplied before any physical metric or BD reduction.
    """
    old=assemble_hr_two_dust_preconstraint(
        radius=radius,quadrature_order=quadrature_order,rho_g=rho_g,
        rho_f=rho_f,log_phidot_rate_g=log_phidot_rate_g,
        log_phidot_rate_f=log_phidot_rate_f,**hr_parameters)
    H_eh=flat_eh_compact_restricted_hessian(
        radius=radius,quadrature_order=quadrature_order,
        N=hr_parameters['N'],a=hr_parameters['a'],
        g_scale_rate=g_scale_rate,n=hr_parameters['n'],
        alpha=hr_parameters['alpha'],n_dot=hr_parameters.get('n_dot',0.),
        alpha_dot=hr_parameters.get('alpha_dot',0.),
        n_ddot=hr_parameters.get('n_ddot',0.),
        alpha_ddot=hr_parameters.get('alpha_ddot',0.),
        mu=hr_parameters['mu'],mu_dot=hr_parameters['mu_dot'],
        sigma_r=hr_parameters['sigma_r'],
        sigma_dot=hr_parameters['sigma_dot'],planck_ratio=planck_ratio)
    H=old.hessian+H_eh
    # These are only the four lapse/shift columns in a REDUCED flat gauge.
    # Do not confuse the rank with the complete four-metric auxiliary block.
    metric=np.array([0,1,4,5],dtype=int)
    block=H[np.ix_(metric,metric)]
    rank=int(np.linalg.matrix_rank(block,tol=1.e-12))
    cond=float(np.linalg.cond(block)) if rank==4 else float('inf')
    return FlatEHRestrictedBridge(H,.5*(H_eh+H_eh.T),old.interaction_hessian,
           old.dust_hessian,old.gradient,float(radius),quadrature_order,rank,cond)
