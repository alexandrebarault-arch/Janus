"""Exact conditional initial-error bootstrap from Step55's global barrier.

If the *true* regular-center Step55 solution U obeys
  |U(s)-Ustar(s)| <= delta
and the exact rationalized DOP853 polynomial P obeys
  P(s0)-Ustar(s0) in [lo,hi],
then |U(s0)-P(s0)| <= delta + max(|lo|,|hi|).
No Taylor-remainder C is required.  This does NOT certify a physical
DOP853 trajectory until the original Step55 barrier and correlated
candidate tube have been checked for the SAME Ustar and true binary64 s0.
"""
from fractions import Fraction as Q


def _q(x):
    if isinstance(x, Q): return x
    if isinstance(x, int): return Q(x)
    if isinstance(x, float): return Q.from_float(x)
    raise TypeError('only exact rational or binary64 values allowed')


def initial_error_from_barrier(delta, difference_lo, difference_hi,
                               require_candidate_tube=True):
    """Exact E0 upper bound; [lo,hi] encloses P(s0)-Ustar(s0).

    Candidate tube is required by default to support the subsequent
    G_U-based propagation.  If absent, the triangle bound remains true,
    but the global comparison theorem is not automatically applicable.
    """
    d, lo, hi = map(_q, (delta, difference_lo, difference_hi))
    if d < 0 or lo > hi:
        raise ValueError('invalid barrier width or difference enclosure')
    if require_candidate_tube and (lo < -d or hi > d):
        raise ArithmeticError('candidate outside common Step55 barrier tube')
    return d + max(abs(lo), abs(hi))


def propagated_initial_contribution(s0, sR, E0, upper_Gu=0):
    """Exact weighted initial term under G_U<=upper_Gu<=0.

    For 2s U_s=G(s,U)-2U, d|e|/ds <=
    -(2-upper_Gu)/(2s)|e| + |H|/(2s).  The initial contribution is
    (s0/sR)**((2-upper_Gu)/2) * E0.  This routine restricts the exponent
    to an integer so the result is rational; the default
    upper_Gu=0 yields the basic exact ledger multiplier s0/sR.
    """
    a,b,E,g=map(_q,(s0,sR,E0,upper_Gu))
    if not (0<a<=b and E>=0 and g<=0):
        raise ValueError('invalid ordered times, error or contraction')
    power=(Q(2)-g)/2
    if power.denominator!=1:
        raise ValueError('noninteger exponent: use basic G_U<=0 ledger')
    return E*(a/b)**power.numerator


def dense_initial_error_from_step55_barrier(dense, delta=Q(1,10000)):
    """Exact candidate-specific E0 budget using original correlated guard.

    This function must run with SHA-authenticated original Step55 sources.
    The separate Step55 barrier theorem is a prerequisite, NOT executed here.
    """
    from .hr_b3c3d6_dop853_dense_rational_defect import (
        dop853_dense_coefficients, dense_exact_domain)
    from .hr_b3c3d6_correlated_tube_guard import (
        difference_enclosure, physical_center_intervals)
    from .hr_step55_global_barrier import U0,U1,U2,S
    from .hr_step55_normalized_secondary import check_original_source_blobs
    check_original_source_blobs()
    t0,_,h,_=dense_exact_domain(dense)
    p=dop853_dense_coefficients(dense)
    center=physical_center_intervals(U0,U1,U2,S)
    difference=difference_enclosure(p,t0,h,Q(0),Q(0),center)
    bound=initial_error_from_barrier(delta,difference.lo,difference.hi)
    return {'initial_error_bound':bound,'initial_time':t0,
            'initial_candidate_minus_center_interval':(difference.lo,difference.hi),
            'conditional_on':'original Step55 global Ustar barrier, same center coefficients, common candidate tube',
            'physical_execution':'NOT_CLAIMED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


def ledger_with_barrier_bootstrap(pieces, initial_difference_lo,
                                  initial_difference_hi, delta=Q(1,10000)):
    """Combine independent barrier E0 with exact defect+jump ledger.

    Piecewise defects, jumps and G_U<=0 still need independent certification.
    """
    from .hr_b3c3d6_global_piecewise_defect_budget import ledger
    E0=initial_error_from_barrier(delta,initial_difference_lo,initial_difference_hi)
    result=ledger(pieces,initial_error=E0)
    result['E0_from_global_barrier_not_center_Taylor']=E0
    result['global_ODE_certificate']='CONDITIONAL_ON_GU_AND_CONTINUOUS_DEFECTS_AND_JUMPS'
    return result
