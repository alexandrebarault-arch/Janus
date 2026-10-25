"""Step68l: 100x narrower rigorous global U(s) and V(s) barrier, original Step55.

This is a rigorous continuum *spatial* enclosure, not the temporal Dirac rank.
Reuse original exact outward-integer interval operators, original symbolic
six-pair G(s,U), and all 4 byte-authenticated historical source files.
An increased rational grid resolution refines interval dependency widths.
Never conflate a failed interval enclosure at coarse resolution with a
counterexample to the true radial solution.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from functools import lru_cache
import json
from . import hr_step55_global_barrier as original

EXPECTED = {
    'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def authentic_originals(root: Path | None = None):
    root = root or Path(__file__).resolve().parent
    for name, expected in EXPECTED.items():
        raw=(root/name).read_bytes()
        actual=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected:
            raise ValueError(f'historical original hash mismatch: {name} {actual}')
    return EXPECTED.copy()


def narrowed_global_barrier(cells=16384,delta_U='0.000001',delta_V='0.00005'):
    """Rational closed slabs + original integer outward arithmetic, no sampling.

    Original Step55 has already proved unique analytic center solution and
    continuation logic. This proof keeps its center polynomial exactly and
    only narrows the invariant barrier by proving *all* slab signs.
    """
    authentic_originals()
    if not isinstance(cells,int) or not 256<=cells<=32768:
        raise ValueError('cells outside separately supported refined verifier')
    du,dv=F(delta_U),F(delta_V)
    if not F(0)<du<=F('0.0001') or not F(0)<dv<=F('0.01'):
        raise ValueError('positive limited tube required')
    xs,fn=original.compiled()
    if not xs or fn is None:
        raise AssertionError('original normalized physical G missing')
    I=original.I;S=original.S;D=I.c(du)
    upper=-10**100;lower=10**100
    velo=10**100;vehi=-10**100
    gmin=10**100;gmax=-10**100
    dv_bound=I.c(dv)
    for i in range(cells):
        s=I.hull(F(289,400)*i/cells,F(289,400)*(i+1)/cells)
        fplus,fminus=original.residual(s,D)
        if fplus.hi>=0 or fminus.lo<=0:
            raise ArithmeticError(f'slab {i}/{cells}: upper={fplus} lower={fminus}')
        upper=max(upper,fplus.hi);lower=min(lower,fminus.lo)
        u,v,ud=original.stars(s)
        vel=original.G(s,I(u.lo-D.hi,u.hi+D.hi))
        diff=vel-v
        if diff.lo<=-dv_bound.lo or diff.hi>=dv_bound.lo:
            raise ArithmeticError(f'original velocity V tube fails slab {i}: {diff}')
        velo=min(velo,diff.lo);vehi=max(vehi,diff.hi)
        gmin=min(gmin,vel.lo);gmax=max(gmax,vel.hi)
    def rational(integer):return str(F(integer,S))
    return {
        'step':'68l',
        'mode':'RIGOROUS_GLOBAL_RADIAL_BARRIER_WITH_ORIGINAL_INTEGER_OUTWARD_INTERVALS',
        'all_original_blobs_verified':authentic_originals(),
        'continuous_s_domain':['0','289/400'],
        'continuous_r_domain':['0','17/20'],
        'rational_slabs':cells,
        'U_minus_Ustar_abs_lt':str(du),
        'V_minus_Vstar_abs_lt':str(dv),
        'strict_max_Fupper':rational(upper),
        'strict_min_Flower':rational(lower),
        'strict_V_minus_Vstar_lower':rational(velo),
        'strict_V_minus_Vstar_upper':rational(vehi),
        'V_actual_min_enclosure':rational(gmin),
        'V_actual_max_enclosure':rational(gmax),
        'outward_integer_scale':S,
        'original_center_polynomial':'Ustar=U0+U1*s+U2*s**2 (unchanged original Step55)',
        'source':'identical original Step45/46/55norm/55global, original interval I and G',
        'historical_bound_U':'1/10000',
        'factor_stronger_than_historical':str(F('0.0001')/du),
        'scope':'continuum spatial original constrained branch; original Step49 center uniqueness and Step55 first-contact argument imported as established; not full temporal Dirac or 4D',
        'temporal_A_N_A_M_signs':'NOT_CERTIFIED',
        'full_Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN',
        'JANUS_R':'NOT_VALIDATED',
    }


def main():
    print(json.dumps(narrowed_global_barrier(),indent=2,ensure_ascii=False))

if __name__=='__main__':main()