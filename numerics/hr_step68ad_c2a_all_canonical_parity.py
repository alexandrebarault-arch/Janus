"""JANUS 68ad-C2a: exact center-safe radial jets of ALL 12 canonical fields.

This is a kinematic chain-rule lemma on the physical Step68o radial ansatz,
not a numerical evaluation of the Step58 temporal Dirac operator.  It removes
all artificial divisions by r or s=r**2 when forming q, q', q'', q'''.

All profile derivatives F_s, F_ss, F_sss must be *certified independently*
for any subsequent interval claim.  In particular the B2 certificates cover
U(s) alone and cannot silently certify the f-dust profiles and their jets.
"""
from __future__ import annotations
from fractions import Fraction
from hashlib import sha1
from pathlib import Path

ORIGINAL_68O_BLOB = 'c99caebc17f243784450ddff94fb061767e6d8e7'
ORIGINAL_58_BLOB = '802c23aebd41780d8c462f1aa1711707fe4ee88f'
ORIGINAL_60_BLOB = '9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509'

# Exact original Step68o data={...} dictionary, grouped by powers of r.
CANONICAL_PROFILE_POWERS = {
    'Lg': 0, 'Lf': 0,
    'Sg': 1, 'Sf': 1, 'pSg': 1, 'pSf': 1,
    'pLg': 2, 'pLf': 2, 'pg': 2, 'pf': 2,
}
CLOCK_FIELDS = ('tg', 'tf')
ALL_FIELDS = ('Lg', 'pLg', 'Sg', 'pSg', 'tg', 'pg',
              'Lf', 'pLf', 'Sf', 'pSf', 'tf', 'pf')


def git_blob(data: bytes) -> str:
    return sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def authenticate_temporal_sources(folder: str | Path):
    """Fail closed before *future* physical integration, no web dependence."""
    folder = Path(folder)
    pins = {'hr_step68o_temporal_interval_annulus.py': ORIGINAL_68O_BLOB,
            'hr_step58_temporal_operator.py': ORIGINAL_58_BLOB,
            'hr_step60_full_constraint_prolongation.py': ORIGINAL_60_BLOB}
    for name, expected in pins.items():
        actual = git_blob((folder / name).read_bytes())
        if actual != expected:
            raise ValueError(f'Physical temporal source changed: {name}: {actual}')
    return pins


def radial_jet(power, r, f0, f1, f2, f3):
    """Return (X,X_r,X_rr,X_rrr) for X=r**power F(r**2).

    f1,f2,f3 are actual s derivatives, NOT factorial-normalized Taylor
    coefficients. No division, including when r=0 or r is an interval
    containing 0. Supports exact Fraction, SymPy and outward interval rings.
    """
    s = r*r
    if power == 0:
        return (f0, 2*r*f1, 2*f1+4*s*f2,
                r*(12*f2+8*s*f3))
    if power == 1:
        return (r*f0, f0+2*s*f1, r*(6*f1+4*s*f2),
                6*f1+24*s*f2+8*s*s*f3)
    if power == 2:
        return (s*f0, 2*r*(f0+s*f1),
                2*f0+10*s*f1+4*s*s*f2,
                r*(24*f1+36*s*f2+8*s*s*f3))
    raise ValueError('Only original radial parity powers 0,1,2 supported')


def dust_clock_jet(r, k, metric0, metric1, metric2):
    """Clock jet when t'(r)=r*k*L(r²), t(r0) chosen as local gauge 0.

    The value of t is shift-symmetric; only t' enters the original ADM
    Hamiltonian. At a nonzero radius, q[0]=0 is a *pointwise gauge value*,
    not a claim that the clock is globally the zero function.
    """
    s = r*r
    return (0, r*k*metric0, k*(metric0+2*s*metric1),
            r*k*(6*metric1+4*s*metric2))


def all_canonical_jets(r, profiles, kg, kf):
    """Pure kinematic assembler for the original six canonical pairs.

    profiles[name] = (F,F_s,F_ss,F_sss) for the TEN non-clock fields,
    where X(r)=r**CANONICAL_PROFILE_POWERS[name] * F(r²).
    Does not manufacture or infer the needed profile derivative bounds.
    """
    if set(profiles) != set(CANONICAL_PROFILE_POWERS):
        raise ValueError('Expected all ten and only ten original non-clock profiles')
    if any(len(x)!=4 for x in profiles.values()):
        raise ValueError('Each profile needs independently justified 0..3 s jets')
    out = {name: radial_jet(power, r, *profiles[name])
           for name,power in CANONICAL_PROFILE_POWERS.items()}
    out['tg'] = dust_clock_jet(r, kg, *profiles['Lg'][:3])
    out['tf'] = dust_clock_jet(r, kf, *profiles['Lf'][:3])
    assert set(out) == set(ALL_FIELDS) and len(out)==12
    return {name:out[name] for name in ALL_FIELDS}


def certified_scope():
    return {
        'step':'68ad-C2a',
        'source':'Original Step68o radial profile structure, Step58 and Step60 pinned for subsequent physical use',
        'original_temporal_git_blob_pins':{
            '68o':ORIGINAL_68O_BLOB,'58':ORIGINAL_58_BLOB,'60':ORIGINAL_60_BLOB},
        'all_twelve_canonical_fields':list(ALL_FIELDS),
        'parity_powers':CANONICAL_PROFILE_POWERS.copy(),
        'clock_derivatives':'tprime=r*k*L(r²), t gauge value arbitrary',
        'exact_chain_rule_to_order':3,
        'singular_division_by_r_or_s':False,
        'physical_interval_profile_derivatives':'REQUIRED_NOT_COMPUTED',
        'temporal_Step58_AN_AM':'NOT_EVALUATED',
        'seven_pending_cells':'NOT_CERTIFIED',
        'full_Dirac_rank':'NOT_COMPUTED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
    }
