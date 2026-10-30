"""Exact-rational reconstruction of SciPy DOP853 dense-output polynomial.

A certificate of the *interpolant* and polynomial residual only. For the
non-polynomial Step55 G, interval evaluation of G on every subcell is still
required; binary64 DOP853 is not an interval integrator. No physical result.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from math import comb


def rat(x):
    if isinstance(x, Q):
        return x
    if isinstance(x, int):
        return Q(x)
    if isinstance(x, float):
        return Q.from_float(x)
    raise TypeError('Use exact Fraction, integer or binary64 float, not decimal strings')


def add(a, b):
    z = [Q(0)] * max(len(a), len(b))
    for i, v in enumerate(a): z[i] += v
    for i, v in enumerate(b): z[i] += v
    return trim(z)


def trim(p):
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p


def mul(a, b):
    z = [Q(0)] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b): z[i+j] += v*w
    return trim(z)


def scale(a, c):
    return trim([v*rat(c) for v in a])


def power(a, n):
    if not isinstance(n, int) or n < 0: raise ValueError('nonnegative integer exponent required')
    out = [Q(1)]
    for _ in range(n): out = mul(out, a)
    return out


def diff(a):
    return trim([i*a[i] for i in range(1,len(a))] or [Q(0)])


def value(a, x):
    x = rat(x); out = Q(0)
    for c in reversed(a): out = out*x+c
    return out


def dop853_dense_coefficients(dense):
    """Exact polynomial in x=(t-t_old)/h of scipy Dop853DenseOutput.

    Supports a scalar state only. Uses exact binary64 floats from F/y_old;
    intentionally does NOT model floating-point roundoff in dense.__call__.
    """
    if type(dense).__name__ != 'Dop853DenseOutput':
        raise TypeError('requires actual SciPy Dop853DenseOutput')
    if len(dense.y_old) != 1 or len(dense.F.shape) != 2 or dense.F.shape[1] != 1:
        raise ValueError('scalar DOP853 only')
    if not (dense.h > 0): raise ValueError('positive steps only')
    p = [Q(0)]
    for i, row in enumerate(reversed(dense.F)):
        p = add(p, [rat(float(row[0]))])
        p = mul(p, [Q(0),Q(1)] if i%2 == 0 else [Q(1),Q(-1)])
    return add(p,[rat(float(dense.y_old[0]))])


def residual_polynomial(p, t_old, h, g_monomials):
    """H=2s*p_s-G(s,p)+2p, polynomial G=sum c_ij*s**i*u**j.

    g_monomials maps (i,j) to exact rational coefficient. This is exact
    algebra for the binary64 polynomial and rationalized t_old,h, NOT a
    certificate for a non-polynomial physical G.
    """
    t_old,h=rat(t_old),rat(h)
    if h<=0:raise ValueError('positive h required')
    s=[t_old,h]
    H=add(scale(mul(s,diff(p)),Q(2)/h),scale(p,2))
    for (i,j),c in g_monomials.items():
        if not isinstance(i,int) or not isinstance(j,int) or min(i,j)<0:
            raise ValueError('nonnegative integer monomial powers')
        H=add(H,scale(mul(power(s,i),power(p,j)),-rat(c)))
    return H


def bernstein_enclosure(p, lo=Q(0), hi=Q(1)):
    """Rational Bernstein convex-hull enclosure of polynomial on [lo,hi]."""
    lo,hi=rat(lo),rat(hi)
    if hi<lo:raise ValueError('reversed interval')
    # Compose polynomial p(lo+(hi-lo)*t), then power -> Bernstein basis.
    a=[Q(0)]
    for c in reversed(p): a=add(mul(a,[lo,hi-lo]),[c])
    n=len(a)-1
    b=[sum((a[j]*Q(comb(k,j),comb(n,j)) for j in range(k+1)),Q(0)) for k in range(n+1)]
    return min(b),max(b)


def polynomial_defect_certificate(p,t_old,h,g_monomials,subcells=1):
    """Exact supremum upper bound on |H|, not the exact supremum."""
    if not isinstance(subcells,int) or subcells<1:raise ValueError('subcells>=1')
    H=residual_polynomial(p,t_old,h,g_monomials)
    cells=[bernstein_enclosure(H,Q(i,subcells),Q(i+1,subcells)) for i in range(subcells)]
    return {'residual_polynomial':H,'max_abs_bound':max(max(abs(a),abs(b)) for a,b in cells),
            'cells':cells, 'exact_rational':True}


def center_initial_error_bound(s0, C, power, upper_Gu):
    """Conditional bound on |U(s0)-P(s0)| for regular center branch.

    Assumptions on 0<s<=s0: 2s U_s=G(s,U)-2U, U(0)=P(0),
    both paths remain in a common tube, G_U<=upper_Gu<2 and
    |G(s,P)-2P-2sP'|<=C*s**power, with C>=0, power>0.
    Then |U(s0)-P(s0)|<=C*s0**power/(2*power+2-upper_Gu).
    Does not include float initialization, endpoint transport or ODE defects.
    """
    s0,C,power,upper_Gu=map(rat,(s0,C,power,upper_Gu))
    if not (s0>0 and C>=0 and power>0 and upper_Gu<2):
        raise ValueError('missing positive radius/contractivity assumptions')
    return C*s0**power/(2*power+2-upper_Gu)


def interval_step_defect(dense, g_interval, interval_type, subcells=256,
                         tube_guard=None):
    """Rigorous continuous residual of exact DOP853 polynomial if G is enclosed.

    `g_interval(sI,uI)` MUST be an inclusion-isotonic outward interval
    extension of G, not point sampling. `interval_type` must implement
    `.c(Fraction)`, `.hull(Fraction,Fraction)`, interval arithmetic and
    `.lo/.hi`. A returned bound concerns this exact reconstructed polynomial;
    no floating-point dense evaluation or ODE solution error is certified.
    """
    if not isinstance(subcells,int) or subcells<1:raise ValueError('subcells>=1')
    p=dop853_dense_coefficients(dense)
    dp=diff(p)
    t0,h=rat(float(dense.t_old)),rat(float(dense.h))
    bounds=[]
    for i in range(subcells):
        a,b=Q(i,subcells),Q(i+1,subcells)
        slo,shi=t0+h*a,t0+h*b
        plo,phi=bernstein_enclosure(p,a,b)
        dlo,dhi=bernstein_enclosure(dp,a,b)
        sI=interval_type.hull(slo,shi)
        pI=interval_type.hull(plo,phi)
        dI=interval_type.hull(dlo/h,dhi/h)
        if tube_guard is not None:tube_guard(sI,pI)
        H=2*sI*dI-g_interval(sI,pI)+2*pI
        bounds.append(H)
    return bounds


def physical_step55_dense_defect(dense, subcells=256):
    """Attempt a continuous Step55 defect bound using original outward I.

    Requires authenticated Step45/46/55 sources in repository. This does NOT
    certify the initial center truncation, the DOP853 solution error, or Step58.
    If tube check fails, increase subcells or reject candidate, never waive it.
    """
    from .hr_step55_global_barrier import G, I, S, stars
    from .hr_step55_normalized_secondary import check_original_source_blobs
    check_original_source_blobs()
    delta=I.c(Q(1,10000))
    def guard(sI,pI):
        star,_,_=stars(sI)
        if pI.lo < star.lo-delta.hi or pI.hi > star.hi+delta.hi:
            raise ArithmeticError('DOP853 polynomial enclosure exits certified Step55 tube')
    cells=interval_step_defect(dense,G,I,subcells,tube_guard=guard)
    bound=Q(max(max(abs(cell.lo),abs(cell.hi)) for cell in cells),S)
    return {'bound':bound,'subcells':subcells,
            'scope':'EXACT_DOP853_INTERPOLANT_CONTINUOUS_STEP55_RESIDUAL_ONLY',
            'tube_guard':'PASS', 'center_initial_error':'NOT_CERTIFIED',
            'Step58_six_coefficients':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
