"""Step65 genuine physical G_UU strict radial monotonicity certificate.

Import actual byte-pinned original Step45/46/55 through Step62 and prove
that for Step55 benchmark geometry d_s G_UU(s,U)>0, uniformly for all
0<=s<=289/400 and all U. Rational interval arithmetic on a SINGLE
continuous s interval proves 4/5 < G_sUU < 1. Endpoint rational-sqrt
interval bounds then sharpen prior Step62 uniform 337/500 curvature
bound to 317/500. This is NOT the temporal Dirac multiplier rank.

The fixed benchmark parameter transcription is as in historical
hr_step55_global_barrier.py (NOT independently re-imported in this worktree).
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from math import isqrt
import sympy as sp
from .hr_step62_physical_G_curvature import Interval, curvature_identity, check_sources

S_MAX=F(289,400)
A=F('0.4'); B=A*F('0.5787707228025044')
CG=F('0.0015'); CF=F('-0.0012'); KF=F('-0.0016')
Z1=F('0.004'); MF=F('0.10879548725')**2
B1=F(1); B2=F('-4.2383993109'); B3=F('13.6801214252')


def geometry_intervals(s):
    """Positive metric factor, true interaction and their derivatives."""
    if s.lo<0 or s.hi>S_MAX:
        raise ValueError('interval is outside certified benchmark radial chart')
    ug=1+CG*s; uf=1+CF*s
    lg=A*ug**2;lf=B*uf**2
    lgp=2*A*CG*ug;lfp=2*B*CF*uf
    r1=Interval(F('0.99999'),1)
    r2=Interval(1,F('1.00001'))
    # Rational square-root envelopes: verified using exact integer bounds.
    assert F('0.99999')**2 < 1-S_MAX*Z1**2
    assert F('1.00001')**2 > 1+S_MAX*KF**2
    assert lf.lo>0 and lg.lo>0
    interaction=B3*lf**2+2*B2*lf*lg+B1*lg**2
    interaction_p=2*B3*lf*lfp+2*B2*(lfp*lg+lf*lgp)+2*B1*lg*lgp
    P=3*B3*lf**2+2*B2*lf*lg-B1*lg**2
    Pp=6*B3*lf*lfp+2*B2*(lfp*lg+lf*lgp)-2*B1*lg*lgp
    Q=4*B2*lf*lg+4*B1*lg**2
    Qp=4*B2*(lfp*lg+lf*lgp)+8*B1*lg*lgp
    T=P*r1+Q
    Tp=Pp*r1-P*Z1**2/(2*r1)+Qp
    assert interaction.lo>0 and T.lo>0
    return dict(lg=lg,lf=lf,r1=r1,r2=r2,
                interaction=interaction,interaction_p=interaction_p,
                T=T,Tp=Tp,lfp=lfp)


def rational_sqrt_enclosure(x, digits=14):
    """Exact outward decimal sqrt bounds; no float whatsoever."""
    x=F(x)
    if x<0:raise ValueError('negative radical')
    scale=10**digits
    lo=isqrt(x.numerator*scale*scale//x.denominator)
    hi=lo if lo*lo*x.denominator==x.numerator*scale*scale else lo+1
    ans=Interval(F(lo,scale),F(hi,scale))
    assert ans.lo**2<=x<=ans.hi**2
    return ans


@lru_cache(maxsize=1)
def strict_slope_certificate():
    """One rational enclosure of exact d/ds G_UU on FULL continuum."""
    check_sources();identity=curvature_identity()
    s=Interval(0,S_MAX)
    g=geometry_intervals(s)
    lf=g['lf']; lfprime=g['lfp'];At=g['interaction'];Tp=g['Tp'];T=g['T']
    log_terms={
       'Tprime/T':Tp/T,
       'Lfprime/Lf':lfprime/lf,
       'R1prime/R1':-Z1**2/(2*(1-s*Z1**2)),
       'R2prime/R2':KF**2/(2*(1+s*KF**2)),
       'Atprime/At':g['interaction_p']/At
    }
    log_deriv=(log_terms['Tprime/T']-log_terms['Lfprime/Lf']
               -log_terms['R1prime/R1']-log_terms['R2prime/R2']
               -log_terms['Atprime/At'])
    # The genuine source identity gives G_UU=s*F where
    # F=(-KF)*T/(2 Lf MF R1 R2 At). R1,R2 >0, KF<0.
    curvature_per_s=-KF*T/(2*lf*MF*g['r1']*g['r2']*At)
    factor=1+s*log_deriv
    slope=curvature_per_s*factor
    assert slope.lo>F(4,5) and slope.hi<F(1)
    assert log_deriv.lo>0 and factor.lo>=1
    # Cross check the exact symbolic logarithmic derivative independently,
    # with geometries as rational expressions and true square roots.
    ss=identity['s']
    lg=A*(1+CG*ss)**2;lf0=B*(1+CF*ss)**2
    r1=sp.sqrt(1-ss*Z1**2);r2=sp.sqrt(1+ss*KF**2)
    At0=B3*lf0**2+2*B2*lf0*lg+B1*lg**2
    T0=((3*B3*lf0**2+2*B2*lf0*lg-B1*lg**2)*r1
        +4*B2*lf0*lg+4*B1*lg**2)
    F0=-KF*T0/(2*lf0*MF*r1*r2*At0)
    log0=sp.diff(T0,ss)/T0-sp.diff(lf0,ss)/lf0-sp.diff(r1,ss)/r1-sp.diff(r2,ss)/r2-sp.diff(At0,ss)/At0
    assert sp.cancel(sp.together(sp.diff(ss*F0,ss)-F0*(1+ss*log0)))==0
    return {'interval':('0',str(S_MAX)),
            'G_sUU_interval':slope.bounds(),
            'G_UU_divided_by_s_interval':curvature_per_s.bounds(),
            'log_derivative_interval':log_deriv.bounds(),
            'factor_interval':factor.bounds(),
            'log_term_intervals':{k:v.bounds() for k,v in log_terms.items()},
            'theorem':'4/5 < d_s G_UU(s,U) < 1 everywhere, for all U, on benchmark',
            'source_degree_U':identity['polynomial_U_degree']}


@lru_cache(maxsize=1)
def sharp_endpoint_certificate():
    """Monotonicity reduces uniform maximum to ONE rational-sqrt endpoint."""
    strict_slope_certificate()
    s=S_MAX
    lg=A*(1+CG*s)**2;lf=B*(1+CF*s)**2
    r1=rational_sqrt_enclosure(1-s*Z1**2)
    r2=rational_sqrt_enclosure(1+s*KF**2)
    T=(3*B3*lf**2+2*B2*lf*lg-B1*lg**2)*r1+4*B2*lf*lg+4*B1*lg**2
    At=B3*lf**2+2*B2*lf*lg+B1*lg**2
    curvature=s*(-KF)*T/(2*lf*MF*r1*r2*At)
    assert 0<curvature.lo<=curvature.hi<F(317,500)
    # Taylor control on actual Step55 |U-Ustar|<=10^-4.
    cap=F(317,500);tube=F(1,10000)
    Gu_bound=cap*tube; remainder=cap*tube*tube/2
    return dict(endpoint_s=str(s),endpoint_curvature=curvature.bounds(),
                uniform_G_UU_bound=('0',str(cap)),
                G_U_sensitive_bound=str(Gu_bound),
                quadratic_Taylor_remainder=str(remainder),
                symbolic_bound='0<=G_UU(s,U)<317/500 globally by strictly positive slope',
                proper_benchmark_only=True)


def manifest():
    return {'step':65,'original_physical_three_source_blobs':check_sources(),
            'monotone':strict_slope_certificate(),
            'sharpened_endpoint':sharp_endpoint_certificate(),
            'temporal_Dirac_rank':'NOT_COMPUTED',
            'lapse_fixing':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))
