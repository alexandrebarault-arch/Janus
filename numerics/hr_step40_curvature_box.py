"""Exact rational, parameter-uniform HR relative-shift chart certificate.

For an INDEPENDENT bounded-curvature two-metric conformal family, prove
strict J(Sf/Sg)>1/2 and K(r)/r^2>0 on a full radial continuum including
r=0 in the regularized sense. Explicitly locate a curvature amplitude
where J CAN vanish. This is neither a Dirac rank test nor a BD theorem.

All decimal calibrations are treated as exact terminating fractions.
"""
from fractions import Fraction as F
import json

M2 = F('23.3348939346')
MG2 = F('1')
B1,B2,B3 = (F('1'),F('-4.2383993109'),F('13.6801214252'))
A0 = F('.4')
Y0 = F('.5787707228025044')
R = F('.85')
CURV_SAFE = F('.015')


def j_eta(y):
    y=F(y)
    return B1+2*B2*y+B3*y*y


def eta(cg,cf,s,y=Y0):
    cg,cf,s,y=map(F,(cg,cf,s,y))
    if s<0 or 1+cg*s<=0 or 1+cf*s<=0:
        raise ValueError('singular or negative conformal factor')
    return y*((1+cf*s)/(1+cg*s))**2


def k_over_r2(a,y,cg,cf,s):
    a,y,cg,cf,s=map(F,(a,y,cg,cf,s))
    if a<=0 or y<=0:raise ValueError('positive scale factors required')
    qg=1+cg*s; qf=1+cf*s
    if qg<=0 or qf<=0:raise ValueError('conformal singularity')
    # Lg=a*qg^2, Lf=a*y*qf^2, Sf/Sg=y*(qf/qg)^2.
    return M2*MG2*a**4*y*qg**6*qf**2*j_eta(y*(qf/qg)**2)


def exact_box_certificate(cmax=CURV_SAFE,rmax=R,amin=A0,amax=A0,
                          ymin=Y0,ymax=Y0):
    """All inequalities exact, valid for EVERY independent cg,cf in [-c,c].

    For s=r^2 <=R^2: 1-cR² <= 1+c_i*s <= 1+cR².
    Therefore ylocal belongs to [ymin*(lo/hi)^2,ymax*(hi/lo)^2].
    The J parabola increases throughout if B2+B3*eta_min>0;
    then J>=J(eta_min)>1/2. The interaction K/r² factor is
    M2 Mg2 a^4 y qg^6 qf^2 J, giving exact uniform positive lower bound.
    """
    cmax,rmax,amin,amax,ymin,ymax=map(F,(cmax,rmax,amin,amax,ymin,ymax))
    if cmax<0 or rmax<=0 or amin<=0 or amax<amin or ymin<=0 or ymax<ymin:
        raise ValueError('invalid compact background parameter box')
    t=cmax*rmax*rmax
    if t>=1:raise ValueError('box includes singular conformal factor')
    lo,hi=1-t,1+t
    eta_min=ymin*(lo/hi)**2
    eta_max=ymax*(hi/lo)**2
    if not (B2+B3*eta_min>0):
        raise ValueError('J monotonicity certificate does not cover this box')
    jl=j_eta(eta_min);ju=j_eta(eta_max)
    if not jl>F(1,2):
        raise ValueError('J>1/2 certificate fails; box cannot be certified')
    kl=M2*MG2*amin**4*ymin*lo**8*jl
    ku=M2*MG2*amax**4*ymax*hi**8*ju
    assert 0<kl<ku
    return {'curvature_abs_max':str(cmax),'r_max':str(rmax),
       'a_interval':[str(amin),str(amax)],'y_interval':[str(ymin),str(ymax)],
       'eta_strict_lower':str(eta_min),'eta_upper':str(eta_max),
       'J_uniform_lower_exact':str(jl),'K_div_r2_uniform_lower_exact':str(kl),
       'J_uniform_lower_float':float(jl),'K_div_r2_uniform_lower_float':float(kl),
       'K_div_r2_uniform_upper_float':float(ku),
       'proof':'r2 bound, conformal interval inclusion, monotone J and product lower bounds using exact Fraction',
       'physical_scope':'fixed conformal metric FAMILY only; no dust positivity, Dirac rank, lapse fixing or on-shell evolution'}


def failure_at_antialigned(c):
    """Worst geometry: cg=+c, cf=-c at radius R; returns exact J."""
    c=F(c)
    if not 0<=c and c*R*R<1:
        raise ValueError('invalid c')
    if c*R*R>=1:raise ValueError('singular conformal factor')
    return j_eta(eta(c,-c,R*R))


def critical_curvature_bracket(iterations=72):
    """Exact dyadic rational isolation of J=0 inside [.078,.08].

    For c in this bracket the minimum eta(c)>=eta(.08)>.31,
    above J's vertex -B2/B3, hence J strictly decreases with c.
    The IVT gives exactly ONE c* in the bracket; not a cosmological
    physical fold, just an algebraic metric-chart zero with no dust data.
    """
    if not isinstance(iterations,int) or not 1<=iterations<=128:
        raise ValueError('invalid bisection depth')
    low,high=F('.078'),F('.08')
    assert eta(high,-high,R*R)>-B2/B3
    assert failure_at_antialigned(low)>0>failure_at_antialigned(high)
    for _ in range(iterations):
        mid=(low+high)/2
        if failure_at_antialigned(mid)>0:low=mid
        else:high=mid
    assert failure_at_antialigned(low)>0>failure_at_antialigned(high)
    return low,high


def manifest():
    baseline=exact_box_certificate()
    # Distinct metric family: y,a allowed to vary independently around Step37.
    neighborhood=exact_box_certificate(amin=F('.395'),amax=F('.405'),
                                       ymin=F('.5787'),ymax=F('.5789'))
    lo,hi=critical_curvature_bracket()
    return {'step':40,'date':'2026-10-20',
       'single_reference_background_box':baseline,
       'finite_background_uncertainty_box':neighborhood,
       'metric_curvature_algebraic_J_zero_bracket':[str(lo),str(hi)],
       'metric_curvature_algebraic_J_zero_approx':float((lo+hi)/2),
       'negative_control_J_at_c_008':float(failure_at_antialigned(F('.08'))),
       'limits':['Only conformal spatial family, not generic HR metric configurations',
                 'Requires c curvature bound and y branch bound',
                 'No continuous positivity theorem for canonical dust momenta',
                 'K(0)=0 due to r^2 spherical factor; K/r^2 is positive',
                 'No local C=0 exact, full Dirac algorithm, physical fold or JANUS-R proof'],
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(manifest(),indent=2))
