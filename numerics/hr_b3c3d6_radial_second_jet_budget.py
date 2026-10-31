"""Exact Step55 -> radial pLf'' sensitivity, conditional on a common tube.

This module does not evaluate original physical G derivatives or certify Step58.
It makes explicit which additional enclosures are needed at exact s=r^2.
"""
from fractions import Fraction as Q

S_STAR = Q(289, 400)
GU_LO = Q('-10010994328099382599714479353/10000000000000000000000000000')
GU_HI = Q('-4969858031286385533119896427/5000000000000000000000000000')
EPS_BINARY_LEDGER = Q('2010134566357187513066947637443797853361850377220243123469020769798153468286503950710034790543827551251967223091638315397441252240354892553973625681393806408354412514537636449051257335533/414499450135323481331783822401740206151893861049810836432975178207163857161147268339490666228626723872819113159860205818972043445535476713878151048061262816356597760000000000000000000000000000')
S_BINARY = Q(6507701461550367, 9007199254740992)


def exact_radius_epsilon():
    """Conditional Step55 prefix ledger bound; never a binary endpoint proof."""
    assert S_STAR < S_BINARY
    return S_BINARY * EPS_BINARY_LEDGER / S_STAR


def max_abs_g_times_g_minus_one(lo, hi):
    """Exact sup |g(g-1)| on a rational closed interval."""
    lo, hi = Q(lo), Q(hi)
    if lo > hi:
        raise ValueError('invalid G_U interval')
    vals = [abs(x*(x-1)) for x in (lo, hi)]
    if lo <= Q(1,2) <= hi:
        vals.append(Q(1,4))
    return max(vals)


def radial_second_jet_error_bound(eps, s, gu_lo, gu_hi, g_su_abs, g_uu_abs, f_abs):
    """Bound |pLf''(U)-pLf''(P)| at the same exact s.

    Assumptions: U and P connected inside a common convex U-tube;
    |U-P|<=eps; G is C^2 there; G_U in [gu_lo,gu_hi];
    |G_sU|<=g_su_abs, |G_UU|<=g_uu_abs and
    |F|=|(G-2u)/(2s)|<=f_abs throughout the joining segment.
    pLf'' means the ODE-consistent physical jet, NOT P''.
    """
    eps,s,gu_lo,gu_hi,g_su_abs,g_uu_abs,f_abs = map(
        Q, (eps,s,gu_lo,gu_hi,g_su_abs,g_uu_abs,f_abs))
    if eps<0 or s<=0 or gu_lo>gu_hi or min(g_su_abs,g_uu_abs,f_abs)<0:
        raise ValueError('invalid bound or domain')
    base = max_abs_g_times_g_minus_one(gu_lo,gu_hi)
    return eps*(base+2*s*(g_su_abs+g_uu_abs*f_abs))


def physical_known_component():
    """Known term only: the remaining derivative terms are NOT zero."""
    eps=exact_radius_epsilon()
    base=max_abs_g_times_g_minus_one(GU_LO,GU_HI)
    return {'epsilon':eps,'base_coefficient':base,
            'known_term':eps*base,
            'unknown_multiplier':2*S_STAR*eps,
            'formula':'known_term + unknown_multiplier*(sup|G_sU|+sup|G_UU|*sup|F|)',
            'scope':'CONDITIONAL_EXACT_RADIUS_JET_BUDGET_NOT_PHYSICAL_SECOND_JET_CERTIFICATE'}


def symbolic_identities():
    """Prove ODE-consistent radial identities from 2s U_s=G-2U."""
    import sympy as sp
    s,u=sp.symbols('s u', positive=True)
    g=sp.Function('G')(s,u)
    f=(g-2*u)/(2*s)
    q=(sp.diff(g,s)+(sp.diff(g,u)-4)*f)/(2*s)
    d=sp.simplify(2*u+10*s*f+4*s*s*q)
    direct=g+2*s*sp.diff(g,s)+sp.diff(g,u)*(g-2*u)
    sensitivity=sp.diff(g,u)*(sp.diff(g,u)-1)+2*s*(sp.diff(g,s,u)+sp.diff(g,u,2)*f)
    return {'pLf_prime_over_r':sp.simplify(2*u+2*s*f-g),
            'pLf_second_derivative':sp.simplify(d-direct),
            'radial_sensitivity':sp.simplify(sp.diff(direct,u)-sensitivity),
            'D':direct,'D_u':sensitivity,'F':f,'U_ss':q}


if __name__=='__main__':
    import json
    z=physical_known_component()
    print(json.dumps({k:str(v) for k,v in z.items()},indent=2))
