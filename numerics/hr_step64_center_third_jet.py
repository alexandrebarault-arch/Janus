"""Step64 center-to-boundary P''' enclosure from original physical Step55 ODE.

Use uniform U hull for the mean-value G_s(s,U(s)) at ANY intermediate
radial coordinate, then derive |U_s|<=4/5 sup|G_s| from the regular-singular
ODE. This avoids dividing the Step55 finite-width tube by s at the center.
No temporal Dirac/lapse rank or ghost absence follows.
"""
from fractions import Fraction as F
from functools import lru_cache
from .hr_step62_original_interval_ad import (I,original,physical_G_jet,
    verify_original_blobs,_tube_at_s)

RMAX=F(17,20)
SMAX=RMAX*RMAX


def _hull(values):
    return I(min(v.lo for v in values),max(v.hi for v in values))


def uniform_center_input(cells=256):
    """Enclose any U(t) for t in [0,S_MAX] independently of its location.

    Step55 U(t) belongs to Ustar(t)±1e-4; the single broad hull also covers
    U(t) when G is integrated from 0 to t at FIXED U(t).
    """
    if not 8<=cells<=8192:raise ValueError('8..8192 cells')
    verify_original_blobs()
    u=_tube_at_s(I.hull(F(0),SMAX))
    bound=None
    for i in range(cells):
        s=I.hull(SMAX*i/cells,SMAX*(i+1)/cells)
        gs=physical_G_jet(s,u)['G_s']
        bound=gs if bound is None else _hull((bound,gs))
    B=F(max(abs(bound.lo),abs(bound.hi)),original.S)
    return dict(uniform_U=u,uniform_Gs=bound,
        A_max=B,Uprime_max=F(4,5)*B,
        W_over_s_max=B/5)


def full_radius_Pthird(cells=256):
    """Rigorous outer interval P''' on all 256 cells including the center.

    G(0,U)=3U0-U for all U on this physical chart. Thus
       2s W_s+3W=s A(s,U), W=U-U0,
       A(s,U)=integral_0^1 G_s(ts,U) dt
    and bounded regular W at center implies
       W(s)/s=1/(2 s**(5/2)) integral_0^s t**(3/2) A(t,U(t)) dt,
    so |W/s|<=Amax/5 and |U_s|<=4 Amax/5.
    Amax MUST cover G_s(t,U(s)) with U(s) fixed for 0<=t<=s:
    hence the global uniform U hull, not the moving tube.
    """
    certificate=uniform_center_input(cells)
    upr=certificate['Uprime_max']
    upr_box=I.hull(-upr,upr)
    minima,maxima=None,None
    first=None
    for i in range(cells):
        s=I.hull(SMAX*i/cells,SMAX*(i+1)/cells)
        U=_tube_at_s(s)
        e=physical_G_jet(s,U)
        G,Gs,Gu,Gss,Gsu,Guu=(e[k] for k in ('G','G_s','G_U','G_ss','G_sU','G_UU'))
        f=G-2*U
        Hs=3*Gs+2*s*Gss+Gs*Gu+f*Gsu
        Hu=Gu*Gu-Gu+2*s*Gsu+f*Guu
        outer=2*s.sqrt()*(Hs+Hu*upr_box)
        if first is None:first=outer
        if minima is None:
            minima,maxima=outer.lo,outer.hi
        else:
            minima=min(minima,outer.lo)
            maxima=max(maxima,outer.hi)
    return {**certificate,'Pthird_full':(F(minima,original.S),F(maxima,original.S)),
         'Pthird_first_cell':(F(first.lo,original.S),F(first.hi,original.S)),
         'first_cell_includes_center':True,'last_cell_includes_smax':True,
         'proof':'Uniform physical G_s bound + exact regular-singular integrating factor; outward interval AD 256 cells'}


def manifest(cells=256):
    c=full_radius_Pthird(cells)
    return dict(step=64,source_exact_git_blobs=verify_original_blobs(),cells=cells,
        uniform_U=[str(F(v,original.S)) for v in (c['uniform_U'].lo,c['uniform_U'].hi)],
        uniform_G_s=[str(F(v,original.S)) for v in (c['uniform_Gs'].lo,c['uniform_Gs'].hi)],
        sup_G_s_absolute=str(c['A_max']),
        absolute_U_s_bound=str(c['Uprime_max']),
        W_over_s_bound=str(c['W_over_s_max']),
        Pthird_full=[str(v) for v in c['Pthird_full']],
        Pthird_first_cell=[str(v) for v in c['Pthird_first_cell']],
        status='RIGOROUS_ORIGINAL_STEP55_FULL_RADIAL_PTHIRD_NOT_TEMPORAL_DIRAC',
        GATE_2B='OPEN',JANUS_R='NOT_VALIDATED',lapse_rank='NOT_COMPUTED')

if __name__=='__main__':
    import json,sys
    print(json.dumps(manifest(int(sys.argv[1]) if len(sys.argv)>1 else 256),indent=2))
