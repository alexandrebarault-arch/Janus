"""Exact conditional state-error budget for Step55 endpoint Taylor transport.

For U'=f(s,U)=(G(s,U)-2U)/(2s), s>0. This is NOT a
validated physical Step55 enclosure: it requires independently certified
solver error, derivative envelopes, and a third-derivative bound.
"""
from fractions import Fraction


def step55_partials(s, u, g, gs, gu, gsu, guu):
    """Return f, f_y, f_sy, f_yy for exact scalar Step55 RHS data."""
    if s <= 0:
        raise ValueError('Step55 radial center s=0 is excluded')
    f = (g - 2*u)/(2*s)
    fy = (gu - 2)/(2*s)
    fsy = gsu/(2*s) - (gu-2)/(2*s*s)
    fyy = guu/(2*s)
    return f, fy, fsy, fyy


def second_order_transport(s, y, h, f, fs, fy):
    """Second-order Taylor map T2(s,y;h), not a validated flow map."""
    return y+h*f+h*h*(fs+fy*f)/2


def second_order_error_budget(h, state_error, L_y, L_sy, L_yy, F, M3):
    """Conditional bound on |U(s+h)-T2(s,y_num;h)|.

    Assumptions: |U(s)-y_num| <= state_error; f and its indicated
    partial derivatives bounded on the entire segment between the
    two endpoint states; |U'''| <= M3 on the exact solution interval.
    All bounds must be NONNEGATIVE and supplied externally.
    """
    values=(state_error,L_y,L_sy,L_yy,F,M3)
    if any(v<0 for v in values):
        raise ValueError('all bound inputs must be nonnegative')
    a=abs(h)
    amplification=1+a*L_y+a*a*(L_sy+L_yy*F+L_y*L_y)/2
    truncation=M3*a*a*a/6
    return {'amplification':amplification,
            'propagated_state_error':amplification*state_error,
            'taylor_remainder':truncation,
            'total':amplification*state_error+truncation}
