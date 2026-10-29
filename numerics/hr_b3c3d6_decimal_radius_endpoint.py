"""Decimal-radius endpoint guard for the Step55->Step58 four-radius probe.

Numerical hygiene only.  Does not bound ODE integration or prove Step58.
"""
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from math import isfinite


def endpoint_s(radius):
    """Return nearest float to the *decimal* r**2, and exact decimal target.

    Unlike float(radius)**2, float(Decimal(str(radius))**2) rounds only
    after the square, avoiding an extra floating-point multiplication error.
    """
    try:
        r = Decimal(str(radius))
    except InvalidOperation as exc:
        raise ValueError("radius must be a finite positive decimal") from exc
    if not r.is_finite() or r <= 0:
        raise ValueError("radius must be finite and positive")
    target = r*r
    sf = float(target)
    if not isfinite(sf) or sf <= 0:
        raise ValueError("radius square is outside finite positive float range")
    return sf, target


def old_endpoint_error(radius):
    """Exact rational difference between old binary square and decimal r**2."""
    sf_old = float(radius)**2
    target = Decimal(str(radius))**2
    return Fraction.from_float(sf_old) - Fraction(target)


def new_endpoint_error(radius):
    """Exact rational difference between nearest float and decimal r**2."""
    sf, target = endpoint_s(radius)
    return Fraction.from_float(sf) - Fraction(target)
