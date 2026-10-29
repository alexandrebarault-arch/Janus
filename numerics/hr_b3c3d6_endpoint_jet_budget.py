"""Exact rational endpoint-jet budget for the full six-coefficient Step58 form.

Conditional algebraic screen, NOT a certified Step55 coefficient enclosure,
positive-lapse BVP, gauge-invariant bound or Dirac result.
"""
from fractions import Fraction as Q


def endpoint_budget(a_n, a_m, b_n, b_m, e_n, e_m, u=1, residual_cap=0):
    """Necessary max(|N'|,|M'|,|N''|,|M''|) at N=M=u>0.

    If the total derivative coefficient norm is zero and the algebraic
    defect exceeds the residual cap, the endpoint equation is impossible.
    All inputs are exact rational numbers (or strings convertible to Q).
    """
    an, am, bn, bm, en, em, amp, tau = map(Q,
        (a_n, a_m, b_n, b_m, e_n, e_m, u, residual_cap))
    if amp <= 0 or tau < 0:
        raise ValueError('positive endpoint lapse and nonnegative residual cap required')
    defect = abs(an + am) * amp
    first = abs(bn) + abs(bm)
    second = abs(en) + abs(em)
    needed = max(Q(0), defect - tau)
    total = first + second
    return {'defect': defect, 'first_weight': first,
            'second_weight': second, 'required_weighted_budget': needed,
            'min_common_jet_cap': None if total == 0 and needed > 0
            else (Q(0) if total == 0 else needed / total),
            'incompatible_with_finite_jets': total == 0 and needed > 0}


def operator_residual(coeff, u, jets):
    """Evaluate endpoint equation, jets=(N',M',N'',M'')."""
    an, am, bn, bm, en, em = map(Q, coeff)
    n1, m1, n2, m2 = map(Q, jets)
    return (an + am) * Q(u) + bn*n1 + bm*m1 + en*n2 + em*m2


def verify_necessary_inequality(coeff, u, jets):
    """Exact triangle inequality, independently of any ODE solution."""
    an, am, bn, bm, en, em = map(Q, coeff)
    n1, m1, n2, m2 = map(Q, jets)
    residual = operator_residual(coeff, u, jets)
    lhs = abs(an + am) * Q(u)
    rhs = (abs(residual) + (abs(bn)+abs(bm))*max(abs(n1),abs(m1))
           + (abs(en)+abs(em))*max(abs(n2),abs(m2)))
    return lhs <= rhs
