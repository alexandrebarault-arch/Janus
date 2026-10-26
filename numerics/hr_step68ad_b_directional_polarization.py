"""Step68ad-B1: rigorous mixed partials of the ORIGINAL fixed physical G.

Use four degree-3 *directional* interval Taylor jets of the existing,
SHA-authenticated Step68n `jet_G` rather than differentiating U enclosures.
The polarization identities are exact; interval additions/subtractions
are inclusions, although dependency may make them too wide for Step58.
This module DOES NOT claim that the physical 0..1/1024 continuum run or
R2/R3/temporal certificates have been performed merely by defining it.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path

ORIGINAL_STEP68N_BLOB='96370e0599748c6dc07faf339ab3646ae3474e7d'


def reconstruct(s_axis, u_axis, plus, minus):
    """Factorial-UNnormalized partials from factorial-normalized jets.

    Input: arrays of coefficients [t^0..t^3] of
      G(s+t,u), G(s,u+t), G(s+t,u+t), G(s+t,u-t).
    Entries may be exact Fraction or outward interval objects supporting
    +,-,*, division by strictly positive integers. All operations enclose
    the exact derivatives for each (s,u) in the input rectangular box.
    """
    if any(len(x)!=4 for x in (s_axis,u_axis,plus,minus)):
        raise ValueError('Exactly four degree-three coefficients per direction')
    a,b,c,d=s_axis,u_axis,plus,minus
    # The four constant terms must overlap; never use this diagnostic to
    # intersect higher-order derivatives, as their correlations are unknown.
    return {
        'G':a[0],
        'G_s':a[1], 'G_U':b[1],
        'G_ss':2*a[2], 'G_sU':c[2]-a[2]-b[2], 'G_UU':2*b[2],
        'G_sss':6*a[3],
        'G_ssU':c[3]-d[3]-2*b[3],
        'G_sUU':c[3]+d[3]-2*a[3],
        'G_UUU':6*b[3],
    }


def source_R2(partials, U_s):
    """Original chain-rule R2, requiring genuine physical partial boxes."""
    return (partials['G_ss']+2*partials['G_sU']*U_s
            +partials['G_UU']*U_s**2)


def source_R3(partials, U_s, U_ss):
    """Original chain-rule R3; only valid with certified U_ss on same slab."""
    return (partials['G_sss']+3*partials['G_ssU']*U_s
            +3*partials['G_sUU']*U_s**2
            +partials['G_UUU']*U_s**3
            +3*partials['G_sU']*U_ss
            +3*partials['G_UU']*U_s*U_ss)


def physical_G_partials(s_box,u_box):
    """Original six-pair G partials on a continuous (s,U) rectangle.

    Only called in a checkout containing authentic Step45/46/55/68l/68n.
    Uses the exact existing Step68n outward-integer interval jet engine;
    no surrogate G and no finite differences. `s_box`,`u_box` are old.I.
    """
    from . import hr_step68n_interval_ode_jets as j
    from . import hr_step55_global_barrier as old
    if j.K!=3:raise ValueError('Original Step68n Taylor order K must equal 3')
    raw=Path(j.__file__).read_bytes()
    blob=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if blob!=ORIGINAL_STEP68N_BLOB:
        raise ValueError('Original physical Step68n source changed: '+blob)
    j.certify_sources()  # Original Step45/46/55 and Step68l source blobs.
    if not isinstance(s_box,old.I) or not isinstance(u_box,old.I):
        raise TypeError('Only original outward-integer Step55 interval boxes')
    if s_box.lo<0 or s_box.hi>old.I.c(F(1,1024)).hi:
        raise ValueError('Outside Step68u certified center s chart')
    if s_box.lo>s_box.hi or u_box.lo>u_box.hi:
        raise ValueError('Malformed original interval box')
    z=old.I.c(0);one=old.I.c(1)
    directions=((one,z),(z,one),(one,one),(one,-one))
    series=[]
    for ds,du in directions:
        sj=j.Jet([s_box,ds]);uj=j.Jet([u_box,du])
        series.append(j.jet_G(sj,uj).a)
    return reconstruct(*series)


def physical_R2_cell(s_box,u_box,us_box):
    """Pointwise continuum enclosure for R2 on a supplied proven slab.

    The CALLER must establish that the exact physical (U,U_s) curve lies
    inside (u_box,us_box) on every s of s_box. This function cannot certify
    that geometric inclusion and cannot by itself prove global U_ss.
    """
    from . import hr_step55_global_barrier as old
    if not isinstance(us_box,old.I):raise TypeError('Original Step55 U_s interval required')
    partials=physical_G_partials(s_box,u_box)
    return source_R2(partials,us_box),partials


def partials_as_rationals(partials):
    from . import hr_step55_global_barrier as old
    return {k:[str(F(v.lo,old.S)),str(F(v.hi,old.S))]
            for k,v in partials.items()}


if __name__=='__main__':
    print('Step68ad-B1 library only: run physical_G_partials on proven cells in the original repository; no temporal claims.')


def physical_R2_global(folder, cells=32):
    """Attempt genuine physical U_ss certificate, fail closed on missing inputs.

    Reuse Step68v's SHA-authentic U_s bound and cubic U tube, Step68n's
    original six-pair G, and Step68ad-A positive-kernel theorem. Every
    closed slab is evaluated, including s=0, with no division by s.
    Returns a certificate ONLY if all original computations complete.
    """
    if not isinstance(cells,int) or not 8<=cells<=2048:
        raise ValueError('Unsupported exact rational cell count')
    from . import hr_step55_global_barrier as old
    from .hr_step68ad_center_derivative_transport import (
        load_physical_reports, damping_bounds, ratio_enclosure)
    reports=load_physical_reports(folder)
    v=reports['68v']
    if v.get('center_cubic_barrier_kappa')!='1/10000000' or not v.get('U_s_strict_positive_inner'):
        raise ValueError('Missing certified Step68v cubic tube or slope')
    uslo=F(v['U_s_center_lower_rational'])
    ushi=F(v['U_s_center_upper_rational'])
    if not 0<uslo<=ushi:
        raise ValueError('Invalid physical slope interval')
    us=old.I.hull(uslo,ushi)
    kap=old.I.c(F(1,10000000))
    max_s=F(1,1024)
    R2lo=10**100;R2hi=-10**100
    rows=[]
    for i in range(cells):
        left=max_s*i/cells;right=max_s*(i+1)/cells
        s=old.I.hull(left,right)
        ustar,_,_=old.stars(s)
        delta=kap*s**3
        utube=old.I(ustar.lo-delta.hi,ustar.hi+delta.hi)
        r2,_=physical_R2_cell(s,utube,us)
        R2lo=min(R2lo,r2.lo);R2hi=max(R2hi,r2.hi)
        rows.append({'s_lo':str(left),'s_hi':str(right),
                     'R2':[str(F(r2.lo,old.S)),str(F(r2.hi,old.S))]})
    if len(rows)!=cells or rows[0]['s_lo']!='0' or rows[-1]['s_hi']!=str(max_s):
        raise AssertionError('Missing continuous closed cell cover')
    g_bounds=tuple(map(F,v['G_U_center_interval']))
    damping=damping_bounds(g_bounds,2)
    r2global=(F(R2lo,old.S),F(R2hi,old.S))
    uss=ratio_enclosure(r2global,damping)
    return {'step':'68ad-B1',
            'mode':'ORIGINAL_SIX_PAIR_G_CONTINUOUS_R2_AND_U_SS_INTERVAL',
            'physical_s_domain':['0','1/1024'],
            'physical_r_domain':['0','1/32'],
            'cell_count':cells,'cells':rows,
            'R2_global_enclosure':list(map(str,r2global)),
            'a2_global_enclosure':list(map(str,damping)),
            'U_ss_global_enclosure':list(map(str,uss)),
            'method':'Four original Step68n SHA-verified interval directional Taylor jets per cell, exact polarization; Step68v SHA-verified cubic U and U_s tube; Step68ad-A positive-kernel theorem.',
            'U_sss':'NOT_COMPUTED',
            'temporal_Step58_A_N_A_M':'NOT_COMPUTED',
            'full_Dirac_rank':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
