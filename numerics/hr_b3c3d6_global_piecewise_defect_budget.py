"""Exact rational *conditional* Step55 error ledger for discontinuous dense pieces.

For 2s U'=G(s,U)-2U and a piecewise differentiable candidate P,
H=2s P'-G(s,P)+2P. If both U,P stay in a common tube and G_U<=0,
then d(s|U-P|)/ds <= |H|/2 on each open piece. At a boundary s_j,
|e(s_j+)|<=|e(s_j-)|+|P(s_j+)-P(s_j-)|. Thus

 sR |e(sR-)| <= s0 |e(s0+)| + 1/2 sum(R_i*(b_i-a_i))
                                      + sum(s_j*abs(jump_j)).

All ledger arithmetic is exact Fraction; R_i must be outward bounds of
continuous residuals, not sampled maxima. This is NOT a physical Step55
certificate without the true DOP853 residuals, tube, G_U and initial error.
"""
from dataclasses import dataclass
from fractions import Fraction as Q


def _q(x):
    if isinstance(x, Q): return x
    if isinstance(x, int): return Q(x)
    if isinstance(x, float): return Q.from_float(x)
    raise TypeError('Only Fraction, integer or exact binary64 float; no decimal strings')


@dataclass(frozen=True)
class Piece:
    left: Q
    right: Q
    defect: Q
    jump_after: Q = Q(0)


def ledger(pieces, initial_error=None):
    """Return |e_R| <= initial_multiplier*E0 + additive_error.

    If E0 is missing, return only a *conditional* affine bound. Jumps are
    at the right endpoint of the preceding piece. The final jump must be 0.
    """
    ps = [Piece(*map(_q, (p.left,p.right,p.defect,p.jump_after))) for p in pieces]
    if not ps: raise ValueError('at least one piece required')
    if ps[0].left <= 0: raise ValueError('strictly positive initial s required')
    for i,p in enumerate(ps):
        if not (p.left < p.right and p.defect >= 0):
            raise ValueError('positive ordered step and nonnegative defect required')
        if i and ps[i-1].right != p.left:
            raise ValueError('non-contiguous true binary64 domains')
    if ps[-1].jump_after: raise ValueError('last piece has no next-side jump')
    s0,sR=ps[0].left,ps[-1].right
    integrated=sum((p.defect*(p.right-p.left)/2 for p in ps),Q(0))
    jumps=sum((p.right*abs(p.jump_after) for p in ps[:-1]),Q(0))
    result={'start':s0,'end':sR,'initial_multiplier':s0/sR,
            'defect_numerator':integrated,'jump_numerator':jumps,
            'additive_error':(integrated+jumps)/sR,
            'piece_count':len(ps),'nonzero_jumps':sum(p.jump_after!=0 for p in ps[:-1]),
            'assumptions':'G_U<=0 and U,P in common tube; outward continuous defect per true step',
            'physical_initial_error':'NOT_CERTIFIED' if initial_error is None else 'SUPPLIED_NOT_INDEPENDENTLY_VERIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}
    if initial_error is not None:
        E0=_q(initial_error)
        if E0<0:raise ValueError('initial error must be nonnegative')
        result['conditional_final_error']=result['initial_multiplier']*E0+result['additive_error']
    return result


def physical_step55_dense_ledger(sol, subcells=256):
    """Try actual SHA-authenticated Step55 outward interval residuals.

    This runs the existing physical adapter for EVERY DOP853 dense piece,
    reconstructs exact binary64 jumps and never invents initial/transport
    error. Raises if any piece fails tube/interval verification.
    """
    from .hr_b3c3d6_dop853_dense_rational_defect import (
        dense_exact_domain,dense_boundary_jump)
    from .hr_b3c3d6_correlated_tube_guard import physical_step55_dense_defect_correlated
    if not getattr(sol,'success',False) or getattr(sol,'sol',None) is None:
        raise ValueError('successful solve_ivp dense_output required')
    ds=sol.sol.interpolants
    if not ds:raise ValueError('no dense pieces')
    ps=[]
    for i,d in enumerate(ds):
        a,b,_,_=dense_exact_domain(d)
        cert=physical_step55_dense_defect_correlated(d,subcells)
        jump=dense_boundary_jump(d,ds[i+1]) if i+1<len(ds) else Q(0)
        ps.append(Piece(a,b,_q(cert['bound']),jump))
    result=ledger(ps)
    result.update({'source':'SHA_GUARDED_ORIGINAL_STEP55_OUTWARD_G',
        'continuous_defect':'ATTEMPTED_ON_ALL_DENSE_PIECES',
        'correlated_center_tube':'REQUIRED_FOR_EVERY_DENSE_SUBCELL',
        'GU_LE_ZERO':'REQUIRES_SEPARATE_PHYSICAL_TUBE_CERTIFICATE',
        'true_center_initial_error':'NOT_CERTIFIED',
        'binary64_initialization_error':'NOT_CERTIFIED',
        'Step58_decimal_endpoint_transport':'NOT_CERTIFIED',
        'Step58_six_coefficient_enclosures':'NOT_CERTIFIED',
        'positive_two_boundary_lapses':'NOT_CERTIFIED'})
    return result


def json_safe(result):
    return {k:(str(v) if isinstance(v,Q) else v) for k,v in result.items()}
