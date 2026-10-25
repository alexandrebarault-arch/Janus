"""Step68v: signed cubic spatial center barrier and U_s>0 for entire Step55 radius.

This builds on rigorous original Step49 analytic recurrence, original Step67b
U3 inclusion, original Step68m U_s interval annulus proof, and original Step68l
continuous existence. The new center certificate itself uses the authentic
Step55 G on [0,1/64] with outward integer 3rd derivative and G_U intervals.
No claim about temporal Dirac lapse coefficient signs at r=0.
"""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha1
import json
from .hr_step55_global_barrier import I,S,U0,U1,U2,stars
from .hr_step68n_interval_ode_jets import Jet,jet_G,certify_sources,coefficient_interval
from .hr_step68u_cubic_center_barrier import STEP67B_U3_LO,STEP67B_U3_HI

MAX_S=F(1,64)  # r<=1/8
KAPPA=F(1,10_000_000)
PINS={'hr_step68u_cubic_center_barrier.py':'4249c1a8c1f60071612c52d756d9f4ff753f22e3',
      'hr_step68m_positive_radial_slope.py':'639c88563411ad6d69298f36cf878f46c0e7be79'}


def authentic():
    original=certify_sources()
    for name,wanted in PINS.items():
        raw=Path(__file__).with_name(name).read_bytes()
        got=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if got!=wanted:raise ValueError('Original Step68u/m source drift: '+name)
    return original


def abs_upper(x):
    return I(0,max(abs(x.lo),abs(x.hi)))


def certificate(smax=MAX_S,kappa=KAPPA):
    authentic()
    sm,kappa=F(smax),F(kappa)
    if not 0<sm<=MAX_S or kappa!=KAPPA:
        raise ValueError('Unproved center chart/width')
    si=I.hull(0,sm)
    s=Jet([si,I.c(1)])
    ustar=Jet(U0)+Jet(U1)*s+Jet(U2)*s**2
    dstar=Jet(U1)+2*Jet(U2)*s
    d=Jet(kappa)*s**3
    dd=3*Jet(kappa)*s**2
    base=(jet_G(s,ustar)-2*ustar-2*s*dstar).a[3]
    ups=(jet_G(s,ustar+d)-2*(ustar+d)-2*s*(dstar+dd)).a[3]
    dws=(jet_G(s,ustar-d)-2*(ustar-d)-2*s*(dstar-dd)).a[3]
    if not ups.hi<0 and dws.lo>0:
        raise ArithmeticError('not sign certified')
    if not ups.hi<0 or not dws.lo>0:
        raise ArithmeticError('Cubic inward barrier not strict')
    if not -kappa<STEP67B_U3_LO<=STEP67B_U3_HI<kappa:
        raise ArithmeticError('Step67b center U3 not strictly interior')
    # Bound G_U(s,U) for all s and all U between true solution and Ustar.
    center,_,_=stars(si)
    delta_max=I.c(kappa)*I.c(sm)**3
    u_tube=I(center.lo-delta_max.hi,center.hi+delta_max.hi)
    gu=jet_G(Jet(si),Jet([u_tube,I.c(1)])).a[1]
    # With F0(s)=G(s,Ustar)-2 Ustar-2s Ustar' and original exact
    # center recurrence, F0(0)=F0'(0)=F0''(0)=0. Thus |F0(s)|<=s^3
    # max|F0'''|/6. Mean-value estimate controls G(s,U)-G(s,Ustar).
    error=I.c(sm)**2*(abs_upper(base)+(abs_upper(gu)+2)*I.c(kappa))/2
    central_reference_slope=U1+2*U2*si
    lower=central_reference_slope-error
    upper=central_reference_slope+error
    if not lower.lo>0:raise ArithmeticError('U_s sign unresolved in inner disk')
    return {'step':'68v','center_s_range':['0',str(sm)],'center_r_range':'0<=r<=1/8' if sm==MAX_S else '0<=r<=sqrt(smax)',
      'original_physical_shas':authentic(),'upstream_shas':PINS,
      'center_cubic_barrier_kappa':str(kappa),
      'center_spatial_inclusion':'|U(s)-Ustar(s)|<=kappa*s^3 by Step49 analytic center recurrence, Step67b strict U3 bound and third-derivative comparison',
      'Fplus_third_over6':coefficient_interval(ups),'Fminus_third_over6':coefficient_interval(dws),
      'F0_third_over6':coefficient_interval(base),
      'G_U_center_interval':coefficient_interval(gu),
      'U_s_deviation_absolute_upper':coefficient_interval(error),
      'reference_Ustar_slope':coefficient_interval(central_reference_slope),
      'U_s_center_lower_rational':str(F(lower.lo,S)),
      'U_s_center_upper_rational':str(F(upper.hi,S)),
      'U_s_strict_positive_inner':True,
      'outer_proof_step68m_domain':'s in [1/64,289/400], r in [1/8,17/20] original certified strict U_s > 0',
      'new_full_radius_radial_U_monotonicity':'U_s>0 for every s in [0,289/400] conditional on original Step49/67b and 68l/m',
      'time_coefficient_A_N_A_M_at_r0':'NOT_CERTIFIED','Dirac_rank':'NOT_COMPUTED',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
