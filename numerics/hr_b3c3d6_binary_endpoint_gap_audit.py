"""Exact rational audit of binary64 abscissae in the Step55/58 candidate.

The SciPy solver sees exact binary64 times, whereas mpmath(str(float))
recovers the shortest printed decimal, not the exact binary64 rational.
This is numerical metrology, not an error bound on physical coefficients.
"""
from decimal import Decimal
from fractions import Fraction
from math import isfinite, ulp

RADII = ('0.25', '0.5', '0.7', '0.85')


def endpoint_record(radius):
    target = Fraction(Decimal(str(radius))) ** 2
    solver_end = float(Decimal(str(radius)) ** 2)
    if not isfinite(solver_end) or solver_end <= 0:
        raise ValueError('endpoint must be finite and positive')
    exact_binary = Fraction.from_float(solver_end)
    gap = exact_binary - target
    half_ulp = Fraction.from_float(ulp(solver_end)) / 2
    if abs(gap) > half_ulp:
        raise AssertionError('float endpoint is not correctly rounded')
    return {
        'radius': str(radius), 'solver_end_repr': repr(solver_end),
        'binary_gap': str(gap), 'binary_gap_float': float(gap),
        'shortest_decimal_gap': str(Fraction(Decimal(str(solver_end))) - target),
        'half_ulp': str(half_ulp),
    }


def start_record():
    binary_s0 = Fraction.from_float(1e-4)
    exact_s0 = Fraction(1, 10000)
    return {'binary_s0_gap': str(binary_s0 - exact_s0),
            'binary_s0_gap_float': float(binary_s0 - exact_s0)}


def diagnostics():
    return {'radii': [endpoint_record(r) for r in RADII], 'start': start_record(),
            'interpretation': 'SciPy binary64 time != mpmath(str(time)) decimal time; no Step58 coefficient error bound'}


if __name__ == '__main__':
    import json
    print(json.dumps(diagnostics(), indent=2))
