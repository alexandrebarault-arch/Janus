"""Exact, conditional Step55 endpoint ODE-jet transfer, not Step58 validation.

For 2*s*U_s=G(s,U)-2*U and a certified |U-P|<=eps at s>0,
compare U derivatives to ODE-consistent jets evaluated at P, NOT to
uncontrolled derivatives of a dense polynomial interpolant P.
All physical numbers are exact rational strings from the authenticated
2026-10-30 Step55 correlated DOP853 report.
"""
from fractions import Fraction as Q

GU_LO = Q('-10010994328099382599714479353/10000000000000000000000000000')
GU_HI = Q('-4969858031286385533119896427/5000000000000000000000000000')
EPS = Q('2010134566357187513066947637443797853361850377220243123469020769798153468286503950710034790543827551251967223091638315397441252240354892553973625681393806408354412514537636449051257335533/414499450135323481331783822401740206151893861049810836432975178207163857161147268339490666228626723872819113159860205818972043445535476713878151048061262816356597760000000000000000000000000000')
S_END = Q.from_float(float('0.7225'))


def endpoint_bounds(eps=EPS, s=S_END, gu_lo=GU_LO, gu_hi=GU_HI):
    """Exact errors at binary64 s; requires both U,P in the certified G_U tube.

    The third bound is for pLf'/r=G(s,U), not for pLf' at decimal R.
    """
    eps, s, gu_lo, gu_hi = map(Q, (eps, s, gu_lo, gu_hi))
    if eps < 0 or s <= 0 or gu_lo > gu_hi:
        raise ValueError('invalid error/domain/G_U interval')
    max_gu = max(abs(gu_lo), abs(gu_hi))
    max_gu_minus_2 = max(abs(gu_lo-2), abs(gu_hi-2))
    return {
        'U': eps,
        'U_s_vs_ODE_jet_at_P': max_gu_minus_2*eps/(2*s),
        'pLf=sU': s*eps,
        'pLf_prime_over_r=G': max_gu*eps,
    }


def ode_jet_maps(G, s, u):
    """Symbolic exact first/second ODE jets, no derivative of interpolant P.

    Q_u is the Lipschitz sensitivity for the second ODE jet. Its physical
    interval requires G_sU and G_UU, which are NOT supplied by G_U alone.
    """
    import sympy as sp
    gu = sp.diff(G, u)
    f = (G-2*u)/(2*s)
    q = (sp.diff(G,s)+(gu-4)*f)/(2*s)
    return {'F':f, 'F_u':sp.diff(f,u), 'Q':q,
            'Q_u':sp.diff(q,u),
            'Q_u_expanded':(sp.diff(G,s,u)+sp.diff(G,u,2)*f
                            +(gu-4)*sp.diff(f,u))/(2*s)}


def exact_physical_endpoint_record():
    b=endpoint_bounds()
    assert GU_HI<0 and EPS<Q(1,200000) and S_END>0
    assert b['U_s_vs_ODE_jet_at_P'] < Q(11,1000000)
    assert b['pLf_prime_over_r=G'] < Q(51,10000000)
    return {k:str(v) for k,v in b.items()}


if __name__=='__main__':
    import json
    print(json.dumps(exact_physical_endpoint_record(),indent=2))
