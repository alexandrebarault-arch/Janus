"""Step55 physical monotone-in-U endpoint enclosure at four exact radii.

Original Step45/46/55 SHA-authenticated, original 256-cell barrier rerun.
G_U<0 on each certified U tube allows replacing a broad natural interval
G(s,[u-,u+]) with the narrower outward endpoints [G(s,u+),G(s,u-)].
The physical composed G_s includes all prescribed geometry derivatives.
This certifies Step55 pointwise spatial jets, NOT Step58, BVP, or Dirac.
"""
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path

from . import hr_step55_global_barrier as b
from .hr_b3c3d6_composed_dual_interval_jets import evaluate_composed
from .hr_b3c3d6_direct_first_partial_jet_enclosure import (
    RInterval, enclose_second_jet)

ORIGINAL_SHA = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step55_normalized_secondary.py': 'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}
RADII = (Q(1, 4), Q(1, 2), Q(7, 10), Q(17, 20))


def authenticate_originals(root=None):
    root = Path(root) if root else Path(__file__).resolve().parents[1]
    for path, expected in ORIGINAL_SHA.items():
        data = (root / path).read_bytes()
        actual = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if actual != expected:
            raise ValueError(f'original SHA mismatch {path}: {actual} != {expected}')
    return ORIGINAL_SHA.copy()


def monotone_decreasing_box(original_G, si, ui, derivative_box, interval_class):
    """Rigorous endpoint hull if dG/dU is strictly negative throughout ui."""
    if derivative_box.hi >= 0:
        raise ArithmeticError('G_U<0 not established on full U interval')
    left = original_G(si, interval_class(ui.hi, ui.hi))
    right = original_G(si, interval_class(ui.lo, ui.lo))
    if left.lo > right.hi:
        raise ArithmeticError('endpoint order inconsistent with G_U<0')
    return interval_class(left.lo, right.hi)


def certify_four_radii():
    authenticate_originals()
    barrier = b.certify_global_barrier(cells=256)
    assert barrier['cells'] == 256
    symbols, compiled = b.compiled()
    records = []
    for r in RADII:
        s = r * r
        si = b.I.c(s)
        star = b.stars(si)[0]
        delta = b.I.c(Q(1, 10000))
        ui = b.I(star.lo - delta.hi, star.hi + delta.hi)
        gs = evaluate_composed(symbols, compiled, b.geometry, b.I,
                               si, ui, True, False)
        gu = evaluate_composed(symbols, compiled, b.geometry, b.I,
                               si, ui, False, True)
        if gs.d.lo <= 0 or gu.d.hi >= 0:
            raise ArithmeticError('composed G_s>0 or G_U<0 not certified')
        wide = b.G(si, ui)
        sharp = monotone_decreasing_box(b.G, si, ui, gu.d, b.I)
        if sharp.lo < wide.lo or sharp.hi > wide.hi:
            raise ArithmeticError('endpoint box not contained in natural interval')
        def rational_box(x):
            return RInterval(Q(x.lo, b.S), Q(x.hi, b.S))
        jets = enclose_second_jet(s, rational_box(ui), rational_box(sharp),
                                  rational_box(gs.d), rational_box(gu.d))
        if jets['pLf_second'].hi >= 0:
            raise ArithmeticError('pLf second derivative negativity not certified')
        if r != Q(1, 4) and jets['U_s'].lo <= 0:
            raise ArithmeticError('U_s positivity not certified at this radius')
        def pair(x):
            return [str(Q(x.lo, b.S)), str(Q(x.hi, b.S))]
        def jet_pair(x):
            return [str(x.lo), str(x.hi)]
        records.append({
            'r': str(r), 's': str(s), 'U': pair(ui),
            'G_natural': pair(wide), 'G_monotone': pair(sharp),
            'G_s_composed': pair(gs.d), 'G_U': pair(gu.d),
            'width_ratio_natural_over_monotone': str(Q(wide.hi-wide.lo,
                                                        sharp.hi-sharp.lo)),
            'jets': {name: jet_pair(value) for name, value in jets.items()},
            'G_s_strictly_positive': True, 'G_U_strictly_negative': True,
            'pLf_second_strictly_negative': True,
            'U_s_strictly_positive': jets['U_s'].lo > 0,
        })
    return {'step': 'b3c3d6_PARTIAL_PHYSICAL_MONOTONE_G',
            'original_source_blobs': ORIGINAL_SHA,
            'original_barrier_cells_rerun': barrier['cells'],
            'radii': records,
            'claim': 'STEP55_SPATIAL_EXACT_RADIUS_POINTWISE_INTERVAL_ENCLOSURES',
            'DOP853_replayed': False, 'Step58_six_A_B_E': 'NOT_CERTIFIED',
            'positive_two_boundary_BVP': 'NOT_CERTIFIED',
            'Dirac_4D_stability_observables': 'NOT_CERTIFIED',
            'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED'}


if __name__ == '__main__':
    import json
    print(json.dumps(certify_four_radii(), indent=2))
