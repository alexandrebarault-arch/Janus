"""b3c3d7: exact conditional annular sign gate for Step58 lapse coefficients.

Only the FOUR already-published physical Step55/Step58 A_N,A_M point boxes
are authenticated and reused. NO physical derivative bound is established.
A separate even-analytic nonphysical countermodel proves pointwise data and
center leading/subleading jets do not imply continuum positivity.
"""
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path
import json

ARCHIVE = 'research/reports/gate2b-b3c3d6-step58-physical-ANAM-four-radii-sign.json'
ARCHIVE_BLOB = 'c502b9779056e8a493c43d330696515a661128c4'
SOURCE_BLOBS = {
    'step45': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'step58': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
    'physical_step55_four_radius_archive': 'e74057dcf741bcdb655c7d9be48c6a9650d7ff3f',
}
RADII = (Q(1, 4), Q(1, 2), Q(7, 10), Q(17, 20))


def git_blob(raw):
    return sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def pinned_boxes(root=None):
    """Authenticate full report bytes and extract strictly signed point boxes."""
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    raw = (root / ARCHIVE).read_bytes()
    if git_blob(raw) != ARCHIVE_BLOB:
        raise ValueError('source Step58 four-radius report Git blob mismatch')
    data = json.loads(raw)
    if data['source_blobs']['step45'] != SOURCE_BLOBS['step45'] or \
       data['source_blobs']['step58'] != SOURCE_BLOBS['step58'] or \
       data['source_blobs']['physical_step55_four_radius_archive'] != SOURCE_BLOBS['physical_step55_four_radius_archive']:
        raise ValueError('original source pin mismatch')
    if set(data['strict_bounds_integer']) != {str(r) for r in RADII}:
        raise ValueError('unexpected sample radii')
    result = []
    for r in RADII:
        row = data['strict_bounds_integer'][str(r)]
        an = tuple(map(Q, row['A_N']))
        am = tuple(map(Q, row['A_M']))
        if not (0 < an[0] < an[1] and am[0] < am[1] < 0):
            raise ValueError('invalid source sign boxes')
        result.append((r*r, an, am))
    return tuple(result)


def normalized_rows(root=None):
    """At s=r², a(s)=A_N(sqrt(s))/s, q(s)=-A_M(sqrt(s))/s."""
    return tuple((s, (an[0]/s, an[1]/s), (-am[1]/s, -am[0]/s))
                 for s, an, am in pinned_boxes(root))


def sharp_lipschitz_thresholds(root=None):
    """Critical L infima from adjacent strict lower boxes, in variable s.

    If a or q is C1 on the annulus and |d/ds| <= L strictly below its
    respective minimum threshold, it is positive everywhere. These are
    sharp infima given ONLY the endpoint lower boxes and a Lipschitz bound.
    No claim is made that the actual physical derivatives meet the gates.
    """
    rows = normalized_rows(root)
    thresholds = []
    for (s0, a0, q0), (s1, a1, q1) in zip(rows, rows[1:]):
        ds = s1-s0
        thresholds.append((ds, (a0[0]+a1[0])/ds, (q0[0]+q1[0])/ds))
    return {'A_N_over_s': min(x[1] for x in thresholds),
            'minus_A_M_over_s': min(x[2] for x in thresholds),
            'by_gap': thresholds}


def conditional_continuum_certificate(L_an, L_am, root=None):
    """Compute strict annular rho bounds IF two global derivative gates hold.

    Assumptions (not checked): a,q C1 on [1/16,289/400], and
    |a_s|<=L_an, |q_s|<=L_am EVERYWHERE. A failure to pass means this
    sufficient test is inconclusive, not that physical positive lapses fail.
    """
    ln, lm = Q(L_an), Q(L_am)
    if ln < 0 or lm < 0:
        raise ValueError('Lipschitz constants must be nonnegative')
    rows = normalized_rows(root)
    gate = sharp_lipschitz_thresholds(root)
    if not (ln < gate['A_N_over_s'] and lm < gate['minus_A_M_over_s']):
        raise ValueError('assumed derivative bounds do not pass sufficient sign gate')
    minima_a, maxima_a, minima_q, maxima_q = [], [], [], []
    for (s0, a0, q0), (s1, a1, q1) in zip(rows, rows[1:]):
        ds = s1-s0
        # Two endpoint Lipschitz cones: max(lower0-L*x,lower1-L*(ds-x))
        # is >= their arithmetic mean, independent of x. Likewise upper.
        minima_a.append((a0[0]+a1[0]-ln*ds)/2)
        maxima_a.append((a0[1]+a1[1]+ln*ds)/2)
        minima_q.append((q0[0]+q1[0]-lm*ds)/2)
        maxima_q.append((q0[1]+q1[1]+lm*ds)/2)
    a_min, a_max = min(minima_a), max(maxima_a)
    q_min, q_max = min(minima_q), max(maxima_q)
    assert 0 < a_min < a_max and 0 < q_min < q_max
    return {'annulus_r': ('1/4','17/20'),
            'a_strict': (a_min, a_max),
            'q_strict': (q_min, q_max),
            'rho_strict': (a_min/q_max, a_max/q_min),
            'assumed_derivative_bounds_in_s': (ln, lm),
            'scope': 'CONDITIONAL_ONLY_NOT_ACTUAL_PHYSICAL_CONTINUUM_ENCLOSURE'}


def toy_a(s):
    return 3500-175*Q(s)


def toy_m(s):
    return -6750+375*Q(s)


def sample_vanishing_polynomial(s):
    out = Q(1)
    for r in RADII:
        out *= Q(s)-r*r
    return out


INTERIOR_S = Q(9, 64)  # r=3/8, strictly between 1/4 and 1/2
PERTURBATION = -toy_m(INTERIOR_S)/(INTERIOR_S**2 * sample_vanishing_polynomial(INTERIOR_S))


def bad_m(s):
    """Analytic nonphysical coefficient with an interior zero.

    Preserves m(0),m_s(0), and EXACT toy values at all four samples.
    A_N=s*toy_a(s) is unchanged, while A_M=s*bad_m(s).
    """
    s = Q(s)
    return toy_m(s) + PERTURBATION*s*s*sample_vanishing_polynomial(s)


def audit(root=None):
    rows = normalized_rows(root)
    thresholds = sharp_lipschitz_thresholds(root)
    assert thresholds['A_N_over_s'] == Q(4123900,147)
    assert thresholds['minus_A_M_over_s'] == Q(378550,7)
    for s, (alo,ahi), (qlo,qhi) in rows:
        assert alo < toy_a(s) < ahi
        assert qlo < -toy_m(s) < qhi
        assert bad_m(s) == toy_m(s)
    assert toy_a(INTERIOR_S) > 0 and bad_m(INTERIOR_S) == 0
    assert toy_m(Q(0)) == bad_m(Q(0)) == -6750
    # Perturbation has factor s²: its first derivative at s=0 is zero.
    assert sample_vanishing_polynomial(0) != 0
    # Exact Taylor identity: (m_bad(s)-m_bad(0)-375*s)/s² = C*P(s).
    for s in (Q(1,100), Q(1,10**6)):
        assert (bad_m(s)-bad_m(0)-375*s)/s**2 == PERTURBATION*sample_vanishing_polynomial(s)
    assert Q(3500,6750) == Q(14,27)
    # By MVT the bad coefficient must violate the sufficient q-derivative gate.
    mvt_lower = -bad_m(Q(1,16))/(INTERIOR_S-Q(1,16))
    assert mvt_lower == 86100 > thresholds['minus_A_M_over_s']
    return {'step':'b3c3d7_CONDITIONAL_ANNULAR_SHARP_LIPSCHITZ_SIGN_GATE',
            'archive_git_blob':ARCHIVE_BLOB,
            'original_step45_step58_read_sha':SOURCE_BLOBS,
            'domain_r':['1/4','17/20'],
            'domain_s':['1/16','289/400'],
            'critical_derivative_in_s':{k:str(thresholds[k]) for k in ('A_N_over_s','minus_A_M_over_s')},
            'example_assumed_derivatives':{'A_N_over_s':'1000','minus_A_M_over_s':'1000'},
            'example_conditional_rho':{k:[str(x) for x in v] if isinstance(v,tuple) else v for k,v in conditional_continuum_certificate(1000,1000,root).items()},
            'nonphysical_analytic_countermodel':{
                'r_interior_zero':'3/8', 's_interior_zero':str(INTERIOR_S),
                'perturbation_coefficient':str(PERTURBATION),
                'lower_bound_on_sup_abs_m_derivative_from_MVT':str(mvt_lower),
                'center_m_value':'-6750','center_m_s_derivative':'375',
                'sample_values':'IDENTICAL_TO_POSITIVE_TOY_AT_ALL_FOUR_RADII'},
            'physical_continuum_derivative_bound_computed':False,
            'physical_center_0_to_1_over_4_certified':False,
            'physical_dirac_BVP_certified':False,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__ == '__main__':
    print(json.dumps(audit(), indent=2, ensure_ascii=False))
