"""Exact sufficient residual threshold for a numerical Step55 curve to stay in the physical tube.

Uses the *archived*, not rerun, Step55/Step63 256-cell barrier.  This does
not estimate a DOP853 residual and does not certify Step58 coefficients.
"""
from fractions import Fraction as Q
from hashlib import sha1
from pathlib import Path
import json

STEP63_BLOB = '8a6ff87fdde3efbf26fa81d20ddb2623c161c9c1'
STEP63_PATH = 'research/reports/gate2b-step63-original-interval-report.json'
FUPPER_MAX = Q('-1480966474499367232302129/10000000000000000000000000000')
FLOWER_MIN = Q('295653233337826329055403/2000000000000000000000000000')
S_MAX = Q(289, 400)
R_MAX = Q(17, 20)
TUBE_HALF = Q(1, 10000)
ORIGINAL_PINS = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step55_normalized_secondary.py': 'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
}


def git_blob(raw):
    return sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def authenticate_archive(root=None):
    """Verify historical report's exact bytes and the relevant physical claims."""
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    raw = (root / STEP63_PATH).read_bytes()
    if git_blob(raw) != STEP63_BLOB:
        raise ValueError('Step63 report blob changed')
    report = json.loads(raw)
    prov = report['provenance']
    if (report['step'] != 63 or prov['original_byte_pins'] != ORIGINAL_PINS
            or not prov['global_step55_256_cell_barrier_reexecuted']
            or '256 continuous cells' not in report['coverage']
            or Q(prov['step55_original_strict_barrier_max_Fplus']) != FUPPER_MAX
            or Q(prov['step55_original_strict_barrier_min_Fminus']) != FLOWER_MIN):
        raise ValueError('Step63 physical barrier provenance or margin mismatch')
    return FUPPER_MAX, FLOWER_MIN


def global_residual_threshold():
    """D < threshold suffices for |v_s-(G(s,v)-2v)/(2s)| <= D on (0,S_MAX]."""
    return min(-FUPPER_MAX, FLOWER_MIN) / (2 * S_MAX)


def boundary_slacks(defect, rb):
    """Strict positive slacks imply inward vector field at both tube walls."""
    d, b = Q(defect), Q(rb)
    if d < 0 or not 0 < b <= R_MAX:
        raise ValueError('require nonnegative continuous defect and 0<rb<=17/20')
    return -FUPPER_MAX - 2*b*b*d, FLOWER_MIN - 2*b*b*d


def candidate_tube_sufficient(ra, rb, initial_offset, defect):
    """A posteriori SUFFICIENT criterion; does not calculate or assume D.

    Let v be continuous, piecewise C1 on [ra²,rb²], and d=v_s-f(s,v).
    If |v(ra²)-Ustar(ra²)|<1/10000 and |d|<=D CONTINUOUSLY,
    both slacks >0 prohibit first contact with either tube boundary.
    Thus v remains strictly inside the certified Step55 physical tube.
    No interpolation-node samples alone can establish |d|<=D.
    """
    a, b, off, d = map(Q, (ra, rb, initial_offset, defect))
    if not 0 < a < b <= R_MAX:
        raise ValueError('invalid radial interval')
    if not -TUBE_HALF < off < TUBE_HALF:
        raise ValueError('initial candidate must be strictly inside tube')
    up, down = boundary_slacks(d, b)
    if not (up > 0 and down > 0):
        raise ValueError('continuous defect too large for robust tube proof')
    return {'upper_slack': up, 'lower_slack': down,
            'sufficient_D_strict': min(-FUPPER_MAX, FLOWER_MIN)/(2*b*b)}


def conditional_endpoint_error(e0, defect, ra, rb):
    """Once the candidate tube is certified, use physical Step63 G_U<0."""
    a, b, e, d = map(Q, (ra, rb, e0, defect))
    if not 0 < a < b <= R_MAX or e < 0 or d < 0:
        raise ValueError('invalid error parameters')
    return (a/b)**2*e + d/2*(b*b-a**4/b**2)


def normalized_defect_sufficient(ra, rb, initial_offset, normalized_defect):
    """Sharper gate: |2s*v_s-G(s,v)+2v|<=R < min archived margins.

    This avoids dividing by 2s near the center. A bound on R must hold
    CONTINUOUSLY on all dense-output cells, not just at sampled nodes.
    """
    a, b, off, d = map(Q, (ra, rb, initial_offset, normalized_defect))
    if not 0 < a < b <= R_MAX or not -TUBE_HALF < off < TUBE_HALF:
        raise ValueError('invalid radius or initial tube offset')
    if d < 0 or d >= min(-FUPPER_MAX, FLOWER_MIN):
        raise ValueError('normalized continuous residual lacks strict margin')
    return {'upper_slack': -FUPPER_MAX-d, 'lower_slack': FLOWER_MIN-d,
            'normalized_D_strict': min(-FUPPER_MAX, FLOWER_MIN)}
