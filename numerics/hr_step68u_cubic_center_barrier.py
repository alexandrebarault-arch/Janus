"""Step68u: outward-rational cubic shrinking center barrier for original Step55 U.

Conditional on original Step49 exact analytic center recurrence U0,U1,U2 and
published Step67b rigorous U3 interval, plus Step68l global continuation.
Check third derivative of FULL original physical ODE barrier residual by
Taylor-jet interval arithmetic for every s in [0,1/1024]. Then F_{+/-}(s)
= s**3 F_{+/-}'''(xi)/6 (all lower exact Taylor coefficients vanish by
analytic recurrence), hence barrier orientation is certified on the continuum.
This certifies only the spatial center branch, NOT temporal lapse signs there.
"""
from __future__ import annotations
from fractions import Fraction as F
from . import hr_step55_global_barrier as old
from .hr_step68n_interval_ode_jets import Jet,jet_G,certify_sources,coefficient_interval

MAX_S=F(1,1024)
KAPPA=F(1,10_000_000)
# Published strict rational inclusion of the physical analytic-center U3, Step67b.
STEP67B_U3_LO=F(-31325163121998456229,2500000000000000000000000000)
STEP67B_U3_HI=F(-62650326243996887233,5000000000000000000000000000)


def third_derivative_certificate(smax=MAX_S,kappa=KAPPA):
    certify_sources()
    smax,kappa=F(smax),F(kappa)
    if not 0<smax<=MAX_S or not 0<kappa<=F(1,10000):
        raise ValueError('Outside pinned center barrier chart')
    S=Jet([old.I.hull(0,smax),old.I.c(1)])
    star=Jet(old.U0)+Jet(old.U1)*S+Jet(old.U2)*S**2
    dstar=Jet(old.U1)+2*Jet(old.U2)*S
    delta=Jet(kappa)*S**3
    ddelta=3*Jet(kappa)*S**2
    fs={}
    for sign,name in ((1,'upper'),(-1,'lower')):
        u=star+sign*delta
        uprime=dstar+sign*ddelta
        resid=jet_G(S,u)-2*u-2*S*uprime
        fs[name]=resid.a[3]
    if not fs['upper'].hi<0 or not fs['lower'].lo>0:
        raise ArithmeticError('Third-derivative barrier orientation unproved')
    if not -kappa<STEP67B_U3_LO<=STEP67B_U3_HI<kappa:
        raise ArithmeticError('Known center Taylor U3 fails strict initial interior condition')
    return {
        'step':'68u',
        'original_source_sha':certify_sources(),
        'center_analytic_recurrence':'Step49 true U0,U1,U2 satisfy F(0)=Fprime(0)=Fdoubleprime(0)=0 exactly, beyond interval containment',
        'U3_lower_from_published_Step67b':str(STEP67B_U3_LO),
        'U3_upper_from_published_Step67b':str(STEP67B_U3_HI),
        's_range':[str(F(0)),str(smax)],
        'r_range':['0',str(F(1,32))] if smax==MAX_S else 'r in [0,sqrt(smax)]',
        'cubic_width_coeff':str(kappa),
        'upper_F_third_over_6_interval':coefficient_interval(fs['upper']),
        'lower_F_third_over_6_interval':coefficient_interval(fs['lower']),
        'Taylor_mean_value':'For s>0 each F(s)=s^3 Fthird(xi)/6; orientation follows strict interval signs.',
        'center_entering':'Step67b strict |U3|<kappa gives |U(s)-Ustar(s)|<kappa*s^3 for sufficiently small s>0',
        'continued_comparison':'Original Step49 analytic existence and Step68l global tube/ODE smoothness enable no-first-exit comparison on [0,smax]',
        'proved_global_center_bound':'|U(s)-Ustar(s)|<=kappa*s^3 for all s in [0,smax]',
        'temporal_A_N_A_M_near_center':'NOT_YET_CERTIFIED',
        'Dirac_rank':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':
 import json
 print(json.dumps(third_derivative_certificate(),indent=2))
