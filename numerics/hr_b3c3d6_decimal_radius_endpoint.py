"""Decimal-radius endpoint guard for the Step55->Step58 four-radius probe.

Numerical hygiene only.  Does not bound ODE integration or prove Step58.
"""
from decimal import Decimal, InvalidOperation, localcontext
from fractions import Fraction
from math import isfinite


def _exact_decimal_square(r):
    """Square a finite Decimal exactly, regardless of ambient Decimal precision."""
    with localcontext() as ctx:
        # A product of two n-significant-digit decimals has <= 2n digits.
        ctx.prec = max(ctx.prec, 2 * len(r.as_tuple().digits) + 2)
        return r * r


def endpoint_s(radius):
    """Return nearest float to exact decimal r**2, and exact Decimal target.

    Unlike float(radius)**2, float(Decimal(str(radius))**2) rounds only
    after the square, avoiding an extra floating-point multiplication error.
    The square is independent of the caller's Decimal context precision.
    """
    try:
        r = Decimal(str(radius))
    except InvalidOperation as exc:
        raise ValueError("radius must be a finite positive decimal") from exc
    if not r.is_finite() or r <= 0:
        raise ValueError("radius must be finite and positive")
    target = _exact_decimal_square(r)
    sf = float(target)
    if not isfinite(sf) or sf <= 0:
        raise ValueError("radius square is outside finite positive float range")
    return sf, target


def old_endpoint_error(radius):
    """Exact rational difference between old binary square and decimal r**2."""
    sf_old = float(radius)**2
    r = Decimal(str(radius))
    return Fraction.from_float(sf_old) - Fraction(r)**2


def new_endpoint_error(radius):
    """Exact rational difference between nearest float and decimal r**2."""
    sf, target = endpoint_s(radius)
    return Fraction.from_float(sf) - Fraction(target)
