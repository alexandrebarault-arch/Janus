"""Exact two-parameter LOCAL primary shell of authentic Step45/Step58.

This is not the physical Step55 profile, a universal ideal membership proof,
or a positive-lapse boundary-value solution. Step57 is a minimal import shim.
"""
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as S
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator

ORIGINAL_BLOBS = {
    'hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def authenticate():
    for filename, expected in ORIGINAL_BLOBS.items():
        raw = Path(__file__).with_name(filename).read_bytes()
        actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        assert actual == expected, (filename, actual, expected)
    return True

@lru_cache(1)
def exact_family():
    authenticate()
    p = exact_physical_ward()
    o = physical_operator()
    q = dict(zip(p['Q'], p['q']))
    qp = dict(zip(p['Q'], p['dq']))
    a, b = S.symbols('a b', real=True)
    mg, mf, m2, b0, b1, b2, b3, b4, z, zr, zrr = p['parameters']
    x, w, v, u = qp['pLg'], o['qpp'][2], o['qpp'][1], o['qppp'][2]
    fields = (*o['q'], *o['qp'], *o['qpp'], *o['qppp'], *o['q4'],
              o['z'], o['zr'], o['zrr'], o['zrrr'], *p['parameters'][:8])
    data = {k: S.S.Zero for k in fields}
    for name in ('Lg', 'Lf', 'Sg', 'Sf'):
        data[q[name]] = S.S.One
    for k in (mg, mf, m2):
        data[k] = S.S.One
    data.update({b0: -5, b1: 1, b4: -2, z: S.Rational(3, 5),
                 zr: a, qp['Sf']: b})
    for k in (qp['Sg'], q['pSg'], q['pLf'], q['pSf'], q['pf']):
        data[k] = S.S.One
    data[q['pg']] = S.Rational(7, 4)
    for k in (x, w, v, u):
        del data[k]

    def ev(expr):
        return S.cancel(expr.subs(data))

    F, H = o['Fz'], p['Hg']
    Fr, Hr = o['Dt'](F), o['Dt'](H)
    xv = S.solve(ev(F), x)[0]
    wv = S.solve(ev(H).subs(x, xv), w)[0]
    vv = S.solve(ev(Fr).subs({x: xv, w: wv}), v)[0]
    uv = S.solve(ev(Hr).subs({x: xv, w: wv, v: vv}), u)[0]
    solved = {x: xv, w: wv, v: vv, u: uv}
    results = {key: S.factor(S.cancel(ev(expr).subs(solved))) for key, expr in {
        'Fz': F, 'Fz_r': Fr, 'Hg': H, 'Hg_r': Hr,
        'C': o['C'], 'B_N': o['operator']['N'][1],
        'B_M': o['operator']['M'][1],
        'E_N': o['operator']['N'][2], 'E_M': o['operator']['M'][2],
        'K': o['K'],
    }.items()}
    return a, b, solved, results

def certificate():
    a, b, solved, r = exact_family()
    assert all(r[k] == 0 for k in ('Fz', 'Fz_r', 'Hg', 'Hg_r', 'B_M', 'E_N', 'E_M'))
    assert r['K'] == 1
    assert solved[next(k for k in solved if str(k) == 'pLgr')] == S.Rational(1, 4)
    assert S.cancel(r['C'] + (25*a + 24*b + 12)/20) == 0
    assert S.cancel(r['B_N'] + 3*(25*a + 24*b + 12)/100) == 0
    assert S.cancel(r['B_N'] - S.Rational(3, 5)*r['C']) == 0
    assert S.cancel(r['C'].subs(b, -(25*a+12)/24)) == 0
    assert r['C'].subs({a: 0, b: 1}) == -S.Rational(9, 5)
    return {
        'original_git_blobs': ORIGINAL_BLOBS,
        'scope': 'EXACT TWO-PARAMETER NONPHYSICAL LOCAL SLICE, NOT UNIVERSAL',
        'parameters': ['a=z_r', 'b=Sf_r'], 'K': '1', 'z': '3/5',
        'positive_dust': ['pg=7/4', 'pf=1'],
        'solved_jets': {str(k): str(S.factor(v)) for k, v in solved.items()},
        'full_primary_and_first_jet': 'Fz=Fz_r=Hg=Hg_r=0',
        'C': str(r['C']), 'B_N': str(r['B_N']),
        'B_M_E_N_E_M': 'EXACT_ZERO',
        'C_zero_curve': 'b=-(25*a+12)/24',
        'identity_on_slice': 'B_N=3*C/5',
        'universal_B_N_factorization': 'NOT_PROVED',
        'physical_step55_six_coefficients': 'NOT_CERTIFIED',
        'two_boundary_positive_lapse_BVP': 'NOT_CERTIFIED',
        'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED',
    }

if __name__ == '__main__':
    import json
    print(json.dumps(certificate(), indent=2))
