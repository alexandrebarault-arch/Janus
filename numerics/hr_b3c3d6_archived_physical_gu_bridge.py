"""Authenticated Step63 physical G_U certificate -> conditional Step55 ODE error bounds.

This bridges a *previously executed* 256-cell physical interval certificate
with a new exact integrating-factor estimate. It does not rerun Step45/46/55
or certify any DOP853 residual, initial error, numerical tube or Step58 data.
"""
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path
import json
import sympy as sp

ARCHIVE = 'research/reports/gate2b-step63-original-interval-report.json'
ARCHIVE_GIT_BLOB = '8a6ff87fdde3efbf26fa81d20ddb2623c161c9c1'
ORIGINAL_BLOBS = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step55_normalized_secondary.py': 'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}
ARCHIVED_GU_LO = Q('-2505544668941123497720438919/2500000000000000000000000000')
ARCHIVED_GU_HI = Q('-2482092799488383772425301393/2500000000000000000000000000')
CERTIFIED_GAMMA = Q(-99, 100)  # a deliberately weaker exact upper bound
MAX_R = Q(17, 20)


def git_blob_sha(raw):
    return sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def check_report_fields(report):
    """Check the archived statement's *scope*; this is not a fresh interval run."""
    if report['step'] != 63 or report['provenance']['original_byte_pins'] != ORIGINAL_BLOBS:
        raise ValueError('Step63 provenance mismatch')
    if report['coverage'] != ('All s∈[0,289/400], U inside exact Step55 '
                              'Ustar(s)±1/10000, 256 continuous cells, '
                              'scale 10^28 integer outward rounding'):
        raise ValueError('Step63 tube or continuous coverage mismatch')
    p = report['provenance']
    if not (p['all_four_sources_git_hash_verified_locally']
            and p['global_step55_256_cell_barrier_reexecuted']
            and p['geometric_chain_rule_includes_s_dependence_of_all_benchmark_background_functions']):
        raise ValueError('original-source verification or geometry dependency missing')
    if not (Q(p['step55_original_strict_barrier_max_Fplus']) < 0
            < Q(p['step55_original_strict_barrier_min_Fminus'])):
        raise ValueError('Step55 invariant barrier absent')
    lo, hi = map(Q, report['rigorous_fractions']['G_U'])
    if (lo, hi) != (ARCHIVED_GU_LO, ARCHIVED_GU_HI):
        raise ValueError('Step63 G_U interval drift')
    if not lo < hi < CERTIFIED_GAMMA < 0:
        raise ValueError('physical G_U sign/upper-bound gate failed')
    if report['scope']['Gate2B'] != 'OPEN' or report['scope']['JANUS_R'] != 'NOT_VALIDATED':
        raise ValueError('unexpected scientific status')
    return lo, hi


def read_authenticated_step63(root=None):
    """Verify actual Git blob bytes, then physical provenance and interval."""
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    raw = (root / ARCHIVE).read_bytes()
    got = git_blob_sha(raw)
    if got != ARCHIVE_GIT_BLOB:
        raise ValueError(f'archived Step63 blob mismatch: {got}')
    return check_report_fields(json.loads(raw))


def _validate(error, defect, ra, rb):
    e, d, a, b = map(Q, (error, defect, ra, rb))
    if not (0 < a < b <= MAX_R):
        raise ValueError('physical radius chart requires 0<ra<rb<=17/20')
    if e < 0 or d < 0:
        raise ValueError('error and continuous residual bounds must be nonnegative')
    return e, d, a, b


def rational_physical_cell(error, defect, ra, rb):
    """Exact rational consequence of archived G_U<0, IF both curves stay in tube.

    E(rb) <= (ra/rb)^2 E(ra) + D/2 * (rb^2-ra^4/rb^2).
    The continuous residual D, initial E, and numerical-tube membership
    are REQUIRED EXTERNAL CERTIFICATES; this routine does not infer them.
    """
    e, d, a, b = _validate(error, defect, ra, rb)
    return (a/b)**2*e + d/2*(b*b-a**4/b**2)


def stronger_physical_cell(error, defect, ra, rb):
    """Exact radical expression from certified G_U<-99/100, not float.

    lambda=(2-gamma)/2=299/200, with s=r^2. This is sharper
    than rational_physical_cell for the same E,D, but algebraic at rational r.
    """
    e, d, a, b = _validate(error, defect, ra, rb)
    lam = sp.Rational(299, 200)
    a, b, e, d = (sp.Rational(x.numerator, x.denominator) for x in (a,b,e,d))
    return (a/b)**(2*lam)*e + d/(lam+1)*(b*b-a**(2*lam+2)/b**(2*lam))


def rational_chain(error, cells):
    """Chain (ra,rb,D) with exact rational arithmetic and strict continuity."""
    result = Q(error)
    previous = None
    for a,b,d in cells:
        if previous is not None and Q(a) != previous:
            raise ValueError('noncontiguous cells')
        result = rational_physical_cell(result,d,a,b)
        previous = Q(b)
    return result


def four_radius_rational(error, defects):
    if len(defects) != 4:
        raise ValueError('four continuous residual bounds required')
    rr = [Q(1,100),Q(1,4),Q(1,2),Q(7,10),Q(17,20)]
    return rational_chain(error, [(rr[i],rr[i+1],defects[i]) for i in range(4)])
