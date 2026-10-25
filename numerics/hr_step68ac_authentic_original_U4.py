"""Step68ac: exact-interval U4 coefficient of original Step45/46/55 physical G.

The original Step68n outward fixed-integer Taylor Jet is reused unchanged,
with its expansion order temporarily raised from 3 to 4 and restored.
Applies ONLY to central Taylor coefficient (r^10 term of pLf=r^2 U(r^2)).
This does NOT bound U_ss/U_sss on positive-radius cells or Step58 Dirac.
"""
from __future__ import annotations
from contextlib import contextmanager
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import json
import sympy as sp
from .hr_step55_normalized_secondary import normalized_symbolic
from . import hr_step55_global_barrier as original
from . import hr_step68n_interval_ode_jets as j
from .hr_step68l_refined_global_barrier import authentic_originals, EXPECTED
from .hr_step68aa_canonical_center_radial_jets import authenticated_inputs

EXTRA_BLOBS={
    'hr_step68l_refined_global_barrier.py':'2a1ffc026a30abf41208b44a707dc869daf0929d',
    'hr_step68n_interval_ode_jets.py':'96370e0599748c6dc07faf339ab3646ae3474e7d',
}


def preflight(root: Path | None = None):
    root=root or Path(__file__).resolve().parent
    originals=authentic_originals(root)
    for name,wanted in EXTRA_BLOBS.items():
        data=(root/name).read_bytes()
        digest=sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if digest!=wanted:
            raise ValueError(f'Original Step68n/68l source drift: {name}: {digest}')
    if originals!=EXPECTED:
        raise AssertionError('Original physical dependency manifest changed')
    return {**originals,**EXTRA_BLOBS}


@contextmanager
def original_jet_order4():
    """Use original verified K-dependent Step68n Jet without altering bytes."""
    old=j.K
    if old !=3:
        raise RuntimeError('Original Step68n K unexpectedly changed')
    j.K=4
    try:
        yield
    finally:
        j.K=old


def exact_GU_center_identity():
    """Fully symbolic ORIGINAL G: dG/dU at s=0 = -Sfr0/Lf0."""
    expr,s,u,vars=normalized_symbolic()
    target=-vars['Sfr']/vars['Lf']
    if sp.cancel(sp.diff(expr,u).subs(s,0)-target)!=0:
        raise AssertionError('Original Step55 central G_U identity broken')
    if sp.simplify(sp.diff(expr,u,2).subs(s,0))!=0:
        raise AssertionError('Original central G not affine in U')
    # On the specified regular center, Lf(0)=Sfr(0)>0.
    return {'unreduced_GU0':'-Sfr0/Lf0',
            'physical_center_Sfr0_equals_Lf0':True,
            'center_GU0_exact':'-1', 'U4_divisor_exact':'11'}


def as_frac(interval):
    return [str(F(interval.lo,original.S)),str(F(interval.hi,original.S))]


def intersect(a,b):
    lo=max(a.lo,b.lo)
    hi=min(a.hi,b.hi)
    if lo>hi:
        raise ArithmeticError('Independent input intervals do not overlap')
    return original.I(lo,hi)


def actual_U4(report_dir):
    source=preflight()
    u3lo,u3hi=authenticated_inputs(report_dir)
    symbolic=exact_GU_center_identity()
    oldS=original.S
    with original_jet_order4():
        s=j.Jet([original.I.c(0),original.I.c(1)])
        u0=original.U0
        # AD check against separately proven central symbolic G_U=-1.
        perturbed=j.Jet([u0,original.I.c(1)])
        slope=j.jet_G(j.Jet(0),perturbed).a[1]
        if not slope.lo<=-oldS<=slope.hi:
            raise ArithmeticError('Original interval jet conflicts with exact symbolic G_U0')
        slope_exact=original.I.c(-1)
        u=j.Jet([u0])
        recurrence=[]
        for n in range(1,5):
            # Evaluate [s^n] G(s, U0+...+U_(n-1)*s^(n-1))
            # with the true original 1048-op normalization and OUTWARD I arithmetic.
            numerator=j.jet_G(s,u).a[n]
            divisor=(2*n+2)-slope_exact
            coeff=numerator/divisor
            recurrence.append({'order':n,'G_numerator':as_frac(numerator),
                               'U_n':as_frac(coeff),
                               'divisor_exact':str(2*n+3)})
            u.a[n]=coeff
        # Pinned historical true U1/U2 and Step67b U3 are tighter input
        # enclosures than the sequential order-4 recurrence at scale 1e-28.
        pinned_u3=original.I.hull(u3lo,u3hi)
        pinned=j.Jet([u0,original.U1,original.U2,pinned_u3])
        for i,p in enumerate([original.U1,original.U2,pinned_u3],start=1):
            intersect(u.a[i],p)
        numerator4=j.jet_G(s,pinned).a[4]
        corrected_U4=numerator4/original.I.c(11)
        common_U4=intersect(u.a[4],corrected_U4)
        if common_U4.hi >= 0:
            raise ArithmeticError('Original U4 negative sign NOT certified')
        pinned.a[4]=common_U4
        # Validate entire original ODE at central Taylor coefficients 0-4.
        residual=j.jet_G(s,pinned)-2*pinned
        # 2*s*U_s = sum 2*n*U_n*s^n, coefficient 0 is zero.
        first_order_residual=[]
        for n in range(5):
            res=residual.a[n]-2*n*pinned.a[n]
            if not res.lo<=0<=res.hi:
                raise ArithmeticError(f'Original centered ODE coefficient n={n} fails')
            first_order_residual.append(as_frac(res))
        result={
            'step':'68ac',
            'type':'RIGOROUS_FIXED_POINT_OUTWARD_INTERVAL_ORIGINAL_PHYSICAL_U4_CENTER',
            'original_source_git_blob_shas':source,
            'source_68aa_U3_verified':True,
            'center_exact_symbolic_GU':symbolic,
            'central_GU_interval_oracle':as_frac(slope),
            'center_U0_interval':as_frac(u0),
            'original_U1_interval':as_frac(original.U1),
            'original_U2_interval':as_frac(original.U2),
            'original_Step67b_U3_interval':[str(u3lo),str(u3hi)],
            'raw_sequential_recurrence':recurrence,
            'pinned_input_U4_numerator':as_frac(numerator4),
            'pinned_input_U4_enclosure':as_frac(corrected_U4),
            'intersection_certified_U4':as_frac(common_U4),
            'original_ODE_coefficient_residuals_contain_zero':first_order_residual,
            'genuine_canonical_pLf_r10_coefficient_is_U4':True,
            'U4_sign_strict_negative':True,
            'method':'Byte-authentic original six-pair Step45/46/55 G, original Step68n integer outward Taylor jet extended in-memory to degree4, analytic G_U0=-1; Step67b U3 pinned, intersection of two independent-input evaluations.',
            'limitations':'Only Taylor coefficient U4 at s=0; NOT a C^3 remainder or uniform near-center temporal coefficient enclosure.',
            'continuous_r_0_to_1over32_higher_jet_enclosures':'NOT_COMPUTED',
            'temporal_Step58_AN_AM':'NOT_COMPUTED',
            'full_Dirac_rank':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
        }
    if j.K!=3:
        raise AssertionError('Original module Jet order not restored')
    return result

if __name__=='__main__':
    import sys
    if len(sys.argv)!=2:
        raise SystemExit('usage: python -m numerics.hr_step68ac_authentic_original_U4 research/reports')
    print(json.dumps(actual_U4(Path(sys.argv[1])),indent=2,ensure_ascii=False))
