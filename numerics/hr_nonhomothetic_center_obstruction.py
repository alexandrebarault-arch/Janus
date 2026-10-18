"""Candidate-C homogeneous-to-nonhomothetic background substitution audit.

This is an exact local g-lapse source at the *spherical centre*, plus an
independently finite-differenced Hassan--Rosen potential at finite radius.
It deliberately does NOT claim a no-go for all nonhomothetic backgrounds:
a relabelled f-native spatial scale, nontrivial lapse/shift and metric
backreaction can change the source. It falsifies *naive substitution* of
an on-shell homogeneous metric into R_f=(1+mu) r while holding its native
f scale and density constants unchanged.

The g lapse source is computed with two comoving canonical dust charges,
never by substituting a normalized covariant dust clock into its action
before varying. Positive EH Planck coefficients and HR mass are assumed.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class HomogeneousSnapshot:
    a: float
    b: float
    adot: float
    Ng: float
    Nf: float
    m2: float
    Mg2: float
    Cg: float
    beta: tuple[float, float, float, float, float]


@dataclass(frozen=True)
class CenterSource:
    g_lapse_original: float
    g_lapse_mapped: float
    obstruction: float
    spatial_ratio_before: float
    spatial_ratio_after: float
    radial_scale: float


def _validated(q: HomogeneousSnapshot, radial_scale: float):
    vals=(q.a,q.b,q.adot,q.Ng,q.Nf,q.m2,q.Mg2,q.Cg,radial_scale,*q.beta)
    if len(q.beta)!=5 or not all(math.isfinite(float(v)) for v in vals):
        raise ValueError('finite homogeneous parameters and five HR beta required')
    if min(q.a,q.b,q.Ng,q.Nf,q.Mg2,radial_scale)<=0 or min(q.m2,q.Cg)<0:
        raise ValueError('positive scales/lapses/Planck, nonnegative mass and dust')


def Vg(y: float, beta):
    b0,b1,b2,b3,_=beta
    return b0+3*b1*y+3*b2*y*y+b3*y**3


def Jg(y: float, beta):
    _,b1,b2,b3,_=beta
    return b1+2*b2*y+b3*y*y


def center_g_lapse_source(q: HomogeneousSnapshot, *, radial_scale:float=1.) -> CenterSource:
    """Exact central g lapse residual, holding native b fixed when R=lambda*r.

    At r=0 the pulled-back f metric has *three* spatial eigenvalues
    (lambda*b/a)^2 and f temporal lapse Nf, so the beta0..beta4 HR
    source seen by the g lapse is Vg(lambda*b/a), independent of beta4.
    The gravitational/dust lapse source is unchanged by an f-only chart.
    """
    _validated(q,radial_scale)
    y=q.b/q.a
    source=3*q.Mg2*q.a*q.adot**2/q.Ng**2-q.Cg
    before=source-q.m2*q.Mg2*q.a**3*Vg(y,q.beta)
    after=source-q.m2*q.Mg2*q.a**3*Vg(radial_scale*y,q.beta)
    obstruction=-q.m2*q.Mg2*q.a**3*(Vg(radial_scale*y,q.beta)-Vg(y,q.beta))
    return CenterSource(float(before),float(after),float(obstruction),
                        float(y),float(radial_scale*y),float(radial_scale))


def _interaction_at_radius(*,g_lapse,a,f_lapse,b,b_rate,fn_rate,
        radius,radial_scale,radial_scale_rate=0.,sigma=0.,sigma_rate=0.,
        beta,m2,Mg2):
    """Exact nonlinear spherical 2x2 + angular HR Lagrangian per dOmega.

    At the time origin use native f T=sigma*r²/2, R=lambda*r.
    f scale and lapse are independently Taylor sampled at native T.
    Native lapse sampling gradients need not be on shell for this local
    principal-square-root regression; centre value is exact for any jets.
    """
    r=float(radius)
    if not math.isfinite(r) or r<=0:raise ValueError('positive finite radius required')
    if not all(math.isfinite(float(x)) for x in (radial_scale_rate,sigma,sigma_rate,
               g_lapse,a,f_lapse,b,b_rate,fn_rate,m2,Mg2)):
        raise ValueError('finite background chart samples required')
    if min(g_lapse,a,f_lapse,b,radial_scale,Mg2)<=0 or m2<0:
        raise ValueError('invalid metric domain')
    if len(beta)!=5 or not all(math.isfinite(float(x)) for x in beta):
        raise ValueError('five finite HR betas required')
    T=.5*sigma*r*r
    native_b=b+b_rate*T
    native_n=f_lapse+fn_rate*T
    Tt=1+.5*sigma_rate*r*r
    Tr=sigma*r
    Rt=radial_scale_rate*r
    Rr=radial_scale
    if Tt*Rr-Tr*Rt<=0 or min(native_n,native_b)<=0:
        raise ValueError('invalid nonhomothetic native chart')
    # g spherical t,r and f native FLRW(T,R) pulled back to g chart.
    gtt=-g_lapse**2
    grr=a*a
    ftt=-native_n**2*Tt**2+native_b**2*Rt**2
    ftr=-native_n**2*Tt*Tr+native_b**2*Rt*Rr
    frr=-native_n**2*Tr**2+native_b**2*Rr**2
    dg=gtt*grr
    df=ftt*frr-ftr*ftr
    if dg>=0 or df>=0:raise ValueError('not Lorentzian')
    s=math.sqrt(df/dg)
    tau_sq=(grr*ftt+gtt*frr)/dg+2*s
    if tau_sq<=0:raise ValueError('complex HR square-root branch')
    tau=math.sqrt(tau_sq)
    ell=native_b*radial_scale/a
    e=(1.,tau+2*ell,s+2*ell*tau+ell**2,
       2*ell*s+ell**2*tau,ell*ell*s)
    # 4pi was not inserted: density per dOmega includes g angular area.
    return -m2*Mg2*math.sqrt(-dg)*a*a*r*r*sum(float(bt)*ei for bt,ei in zip(beta,e))


def independent_g_lapse_hr_derivative(q:HomogeneousSnapshot, *,radius:float,
         radial_scale:float=1., radial_scale_rate:float=0.,sigma:float=0.,
         sigma_rate:float=0., b_rate:float=0.,fn_rate:float=0.,step:float=1e-5):
    """Numerical partial dL_HR/dNg /r² at constant g,f fields and native chart.

    This independently checks the analytic centre formula from the exact
    nonlinear 2x2 principal-square-root potential, not its Taylor jet.
    """
    _validated(q,radial_scale)
    if not math.isfinite(step) or step<=0 or step>=.25*q.Ng:
        raise ValueError('valid centered lapse variation step required')
    kw=dict(a=q.a,f_lapse=q.Nf,b=q.b,b_rate=b_rate,fn_rate=fn_rate,
            radius=radius,radial_scale=radial_scale,
            radial_scale_rate=radial_scale_rate,sigma=sigma,
            sigma_rate=sigma_rate,beta=q.beta,m2=q.m2,Mg2=q.Mg2)
    plus=_interaction_at_radius(g_lapse=q.Ng+step,**kw)
    minus=_interaction_at_radius(g_lapse=q.Ng-step,**kw)
    return float((plus-minus)/(2*step*radius*radius))


def independent_total_g_lapse_residual(q:HomogeneousSnapshot, **kwargs):
    """Actual full g lapse witness: its EH and Routhian dust part are fixed.

    Only interaction is independently finite differenced. For nonzero r,
    an f-only radial chart gives a radius-dependent local lapse source;
    this number is not a FULL coupled-field Euler solution.
    """
    return (3*q.Mg2*q.a*q.adot**2/q.Ng**2-q.Cg
            +independent_g_lapse_hr_derivative(q,**kwargs))


def snapshot_on_homogeneous_g_constraint(*,a,y,Ng=1.,Nf=.6,
                                          m2=23.3348939346,Mg2=1.,Cg=.9,
                                          beta=(0.,1.,-4.2383993109,13.6801214252,-38.5117901844)):
    """Construct on-g-Friedmann control WITHOUT asserting the f equations.

    For full Candidate-C two-lapse/scale on-shell checks, caller should
    pass the independently computed q from hr_minisuperspace_onshell.
    """
    if min(a,y,Ng,Nf,Mg2)<=0:raise ValueError('invalid homogeneous snapshot')
    E2=Cg/(3*Mg2*a**3)+m2*Vg(y,beta)/3
    if E2<=0:raise ValueError('negative g Hubble square')
    q=HomogeneousSnapshot(float(a),float(a*y),float(a*math.sqrt(E2)*Ng),
              float(Ng),float(Nf),float(m2),float(Mg2),float(Cg),tuple(beta))
    _validated(q,1.)
    return q


def compact_g_lapse_first_variation(q:HomogeneousSnapshot, *,support_radius=.2,
       radial_scale=1.,radial_scale_rate=0.,sigma=0.,sigma_rate=0.,
       b_rate=0.,fn_rate=0.,quadrature_order=32,amplitude_step=3e-6):
    """Independent compact action first variation in the g-lapse direction.

    On one time slice vary Ng(r)=Ng+eps F(r), F=(1-r²/Rmax²)^4,
    in g EH+canonical g dust+HR only; f EH and f dust do not depend
    on the g metric lapse and therefore contribute zero to this variation.
    Local test of a necessary full field equation, NOT complete action
    time-domain stationary proof.
    """
    _validated(q,radial_scale)
    if (not math.isfinite(support_radius) or support_radius<=0
            or type(quadrature_order)!=int or quadrature_order<8
            or not math.isfinite(amplitude_step) or amplitude_step<=0):
        raise ValueError('invalid compact lapse variation domain')
    nodes,ws=np.polynomial.legendre.leggauss(quadrature_order)
    rr=.5*support_radius*(nodes+1)
    ww=.5*support_radius*ws
    F=(1-(rr/support_radius)**2)**4
    def S(sign):
        out=0.
        for r,w,f in zip(rr,ww,F):
            lapse=q.Ng+sign*amplitude_step*f
            if lapse<=0:raise ValueError('nonpositive perturbed g lapse')
            gh=(-3*q.Mg2*q.a*q.adot**2/lapse-lapse*q.Cg)*r*r
            hr=_interaction_at_radius(g_lapse=lapse,a=q.a,f_lapse=q.Nf,
                  b=q.b,b_rate=b_rate,fn_rate=fn_rate,radius=r,
                  radial_scale=radial_scale,radial_scale_rate=radial_scale_rate,
                  sigma=sigma,sigma_rate=sigma_rate,beta=q.beta,
                  m2=q.m2,Mg2=q.Mg2)
            out+=4*math.pi*w*(gh+hr)
        return out
    return float((S(1)-S(-1))/(2*amplitude_step))


def radial_bump_norm(support_radius):
    """Exact 4pi int r² [1-r²/R²]^4 dr via beta function."""
    if support_radius<=0 or not math.isfinite(support_radius):
        raise ValueError('positive finite radius required')
    # 4pi R³/2 B(3/2,5).
    return float(2*math.pi*support_radius**3 *
                math.gamma(1.5)*math.gamma(5)/math.gamma(6.5))


def central_linearized_chart_sensitivity(q:HomogeneousSnapshot):
    """d R_g/dlambda at lambda=1 for fixed native scale b."""
    _validated(q,1.)
    return float(-3*q.m2*q.Mg2*q.a**3*(q.b/q.a)*Jg(q.b/q.a,q.beta))


def f_common_slice_spatial_anisotropy(*,f_native_lapse,radial_coordinate,
                                      sigma, f_native_lapse_rate=0.):
    """f_rr - f_theta_theta/r² from T=t+sigma*r²/2, R=lambda*r.

    It is a common-t slicing component difference, NOT a native f
    intrinsic curvature invariant and NOT by itself a physical anisotropic
    stress. It is exactly -n(T)^2 sigma² r² for any positive lambda.
    """
    if not all(math.isfinite(float(x)) for x in
         (f_native_lapse,radial_coordinate,sigma,f_native_lapse_rate)):
        raise ValueError('finite local chart parameters required')
    if f_native_lapse<=0 or radial_coordinate<=0:
        raise ValueError('native lapse and radius must be positive')
    T=.5*sigma*radial_coordinate**2
    n=f_native_lapse+f_native_lapse_rate*T
    if n<=0:raise ValueError('nonpositive sampled f lapse')
    return float(-n*n*sigma*sigma*radial_coordinate**2)
