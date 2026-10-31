"""Exact-radius Step55 prefix certificate from the *previously certified* ledger.

This does not extend the physical Step55 barrier past s*=289/400.
The previous DOP853 endpoint is binary64 s_b > s*. The published
nonnegative total defect/jump budget B=s_b*epsilon also bounds every
prefix up to s*. The exact physical U(s*) is therefore compared with
P(s*) (the appropriate dense polynomial at s*), not with P(s_b).

Conditional on the authenticated Step55 barrier, common-tube G_U<=0,
correlated polynomial/residual certificates and initial error ledger.
No new physical originals are executed here. Not a Step58 certificate.
"""
from fractions import Fraction as Q

S_EXACT = Q(289, 400)
S_BINARY = Q(6507701461550367, 9007199254740992)
EPS_BINARY_LEDGER = Q('2010134566357187513066947637443797853361850377220243123469020769798153468286503950710034790543827551251967223091638315397441252240354892553973625681393806408354412514537636449051257335533/414499450135323481331783822401740206151893861049810836432975178207163857161147268339490666228626723872819113159860205818972043445535476713878151048061262816356597760000000000000000000000000000')
GU_LO = Q('-10010994328099382599714479353/10000000000000000000000000000')
GU_HI = Q('-4969858031286385533119896427/5000000000000000000000000000')


def prefix_ledger_bound(s_star=S_EXACT, s_binary=S_BINARY, eps_binary=EPS_BINARY_LEDGER):
    """Nonnegative prefix ledger: s*|e(s*)| <= s_binary*eps_binary.

    eps_binary here is the EXACT NUMERIC LEDGER RATIO, not an independently
    established physical error at s_binary beyond the certified domain.
    Requires s* inside the certified common-tube interval and the dense
    polynomial partition. Domain and hypotheses must be checked externally.
    """
    s_star, s_binary, eps_binary = map(Q, (s_star, s_binary, eps_binary))
    if s_star <= 0 or s_binary < s_star or eps_binary < 0:
        raise ValueError('invalid prefix/ledger domain')
    return s_binary * eps_binary / s_star


def exact_radius_first_jets(eps=None):
    """ODE-consistent jets at s*=289/400; never differentiates dense P."""
    if eps is None:
        eps = prefix_ledger_bound()
    eps = Q(eps)
    if eps < 0 or GU_LO > GU_HI or GU_HI >= 0:
        raise ValueError('invalid common-tube assumptions')
    return {
        'U': eps,
        'U_s_vs_F_at_P': max(abs(GU_LO-2), abs(GU_HI-2))*eps/(2*S_EXACT),
        'pLf_vs_sP': S_EXACT*eps,
        'pLf_prime_over_r_vs_G_at_P': max(abs(GU_LO),abs(GU_HI))*eps,
    }


def exact_record():
    b=exact_radius_first_jets()
    assert S_BINARY-S_EXACT == Q(7,225179981368524800)
    assert b['U'] < Q(1,200000)
    assert b['U_s_vs_F_at_P'] < Q(11,1000000)
    assert b['pLf_prime_over_r_vs_G_at_P'] < Q(51,10000000)
    return {'s_exact':str(S_EXACT),'s_binary':str(S_BINARY),
            'positive_binary_overshoot':str(S_BINARY-S_EXACT),
            'ledger_ratio_not_physical_error_at_binary':str(EPS_BINARY_LEDGER),
            'exact_radius_error_bounds':{k:str(v) for k,v in b.items()},
            'scientific_scope':'CONDITIONAL_STEP55_EXACT_RADIUS_PREFIX_CERTIFICATE',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(exact_record(),indent=2))
