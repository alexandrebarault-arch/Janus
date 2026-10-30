"""Exact rational polynomial defect and Gronwall-free local error bound.

For y'=f(s,y), polynomial approximate v, defect d=v'-f(s,v).
Bernstein coefficients enclose a polynomial d on a closed rational cell.
If |d|<=D and f is L-Lipschitz in y on a certified solution tube,
then E_out <= (E_in+D*h)/(1-L*h), provided 0<=L*h<1.
No Step55 physical tube or DOP853 continuous residual is certified here.
"""
from fractions import Fraction
from math import comb


def bernstein_coefficients(power, a, b):
    """Bernstein coefficients of sum power[k]*s**k on [a,b]."""
    a, b = Fraction(a), Fraction(b)
    if not b > a:
        raise ValueError('nonempty ascending cell required')
    p = tuple(Fraction(c) for c in power)
    if not p:
        raise ValueError('nonempty polynomial required')
    n = len(p)-1
    h = b-a
    # Coefficients of p(a+h*x) in the power basis x^j.
    c = [sum(p[k]*comb(k,j)*a**(k-j)*h**j for k in range(j,n+1))
         for j in range(n+1)]
    return tuple(sum(c[j]*Fraction(comb(i,j),comb(n,j)) for j in range(i+1))
                 for i in range(n+1))


def polynomial_defect_bound(power, a, b):
    """Exact upper bound sup |d|; power represents the FULL defect."""
    return max(map(abs, bernstein_coefficients(power,a,b)))


def rational_error_step(error_in, defect_bound, lipschitz, a, b):
    """Exact rational one-cell upper bound, assuming a certified tube.

    Proof: sup E <= E_in + h*D + L*h*sup E. The same upper bound
    controls the endpoint. Rejects L*h>=1 rather than extrapolating.
    """
    e, d, L, a, b = map(Fraction,(error_in,defect_bound,lipschitz,a,b))
    h=b-a
    if min(e,d,L) < 0 or h <= 0:
        raise ValueError('nonnegative bounds and ascending cell required')
    if L*h >= 1:
        raise ValueError('L*h must be strictly below one; subdivide cell')
    return (e+d*h)/(1-L*h)


def chained_error_bound(error_in, cells):
    """cells = [(a,b,D,L), ...], all exact rational, contiguous."""
    error=Fraction(error_in)
    if error < 0:
        raise ValueError('initial error bound must be nonnegative')
    previous=None
    for a,b,d,L in cells:
        if previous is not None and Fraction(a)!=previous:
            raise ValueError('cells must be contiguous')
        error=rational_error_step(error,d,L,a,b)
        previous=Fraction(b)
    return error
