"""Binary64-faithful RHS and first-order endpoint transport for Step55 probes.

The input to SciPy's RHS is a binary64 number. mp.mpf(str(x)) is not
that number. The transport removes the deterministic O(delta) mismatch
between the binary64 solver endpoint and the exact decimal r**2, but
is NOT an integration-error enclosure or a Step58 physical certificate.
"""
from decimal import Decimal
from fractions import Fraction
import mpmath as mp


def exact_binary(x):
    """Exact binary64 float embedded in mpmath (no shortest-decimal hop)."""
    if not isinstance(x, float):
        raise TypeError('expected Python binary64 float')
    return mp.mpf(x)


def decimal_square_target(radius):
    """Target r**2 interpreted as an exact finite decimal rational."""
    r = Decimal(str(radius))
    if not r.is_finite() or r <= 0:
        raise ValueError('radius must be finite and positive')
    return Fraction(r)**2


def exact_fraction_mp(q):
    q = Fraction(q)
    return mp.mpf(q.numerator) / q.denominator


def transport_endpoint(radius, solver_s, solver_y, rhs, dps=80):
    """Taylor transport y(s*) ~= y(sf) + (s*-sf) f(sf,y(sf)).

    Returns mpmath values and exact rational delta; the remainder is
    O(delta**2) only for a smooth ODE with controlled derivatives.
    The SciPy integration error in solver_y is NOT controlled here.
    """
    with mp.workdps(dps):
        sf = exact_binary(solver_s)
        yf = exact_binary(solver_y)
        target = decimal_square_target(radius)
        delta = target - Fraction.from_float(solver_s)
        slope = rhs(sf, yf)
        corrected = yf + exact_fraction_mp(delta) * slope
        return {'value': +corrected, 'delta': delta,
                'slope': +slope, 'raw': +yf}


def transport_endpoint_second_order(radius, solver_s, solver_y, rhs, dps=80):
    """Holonomic second-order transport from a binary64 endpoint.

    y''=f_s+f_y*f for y'=f(s,y). For a C3 exact solution, the Taylor
    remainder is bounded by |delta|**3/6 * sup|y'''| on the short interval.
    No bound on y''' or SciPy's accumulated state error is provided here.
    """
    if dps < 30:
        raise ValueError('second-order transport requires dps >= 30')
    with mp.workdps(dps):
        sf = exact_binary(solver_s)
        yf = exact_binary(solver_y)
        delta = decimal_square_target(radius) - Fraction.from_float(solver_s)
        h = exact_fraction_mp(delta)
        slope = rhs(sf, yf)
        fs = mp.diff(lambda s: rhs(s, yf), sf)
        fy = mp.diff(lambda y: rhs(sf, y), yf)
        acceleration = fs + fy * slope
        corrected = yf + h*slope + h*h*acceleration/2
        return {'value': +corrected, 'delta': delta, 'slope': +slope,
                'acceleration': +acceleration, 'raw': +yf,
                'remainder': 'CONDITIONAL_C3_SUP_Y3_TIMES_ABS_DELTA_CUBED_OVER_6',
                'solver_state_error_enclosed': False}
