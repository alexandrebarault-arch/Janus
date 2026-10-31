"""Exact one-parameter lower-jet witness in the BYTE-AUTHENTIC Step45/58 operator.

This is a NONPHYSICAL local algebraic slice, not a universal identity or BVP.
It isolates why eliminating the highest B_N jets does not remove Hg itself.
Step57 is imported through a minimal shim; full Step57 is NOT replayed.
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
        data = Path(__file__).with_name(filename).read_bytes()
        digest = sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if digest != expected:
            raise AssertionError((filename, digest, expected))
    return True

@lru_cache(maxsize=1)
def exact_family():
    authenticate()
    p = exact_physical_ward()
    o = physical_operator()
    q = dict(zip(p['Q'], p['q']))
    qp = dict(zip(p['Q'], p['dq']))
    mg, mf, m2, b0, b1, b2, b3, b4, z, zr, zrr = p['parameters']
    t = S.Symbol('t', real=True)
    fields = (*o['q'], *o['qp'], *o['qpp'], *o['qppp'], *o['q4'],
              o['z'], o['zr'], o['zrr'], o['zrrr'], *p['parameters'][:8])
    values = {x: S.S.Zero for x in fields}
    for name in ('Lg', 'Lf', 'Sg', 'Sf'):
        values[q[name]] = S.S.One
    for x in (mg, mf, m2):
        values[x] = S.S.One
    values[b0] = -5
    values[b1] = 1
    values[b4] = -2
    values[z] = S.Rational(3, 5)
    values[zr] = -S.Rational(36, 25)
    for x in (qp['Sg'], qp['Sf'], q['pSg'], q['pLf'], q['pSf'], q['pf']):
        values[x] = S.S.One
    values[q['pg']] = S.Rational(7, 4)
    values[qp['pLg']] = S.Rational(1, 4)
    values[o['qpp'][2]] = t  # Sg_rr: lower jet, NOT the selected highest jet.
    values[o['qpp'][1]] = t + S.Rational(21, 16)  # pLg_rr
    values[o['qppp'][2]] = S.Rational(85, 32) - 2*t  # Sg_rrr

    def ev(expr):
        return S.factor(S.cancel(expr.subs(values)))

    beta = -(1-z*z)/(q['Lg']*q['Lf'])
    delta = o['operator']['N'][1] - z*o['C']/q['Lg']
    residual = delta - beta*o['Dt'](p['Hg'])
    out = {
        'Fz': ev(o['Fz']),
        'Fz_r': ev(o['Dt'](o['Fz'])),
        'Hg': ev(p['Hg']),
        'Hg_r': ev(o['Dt'](p['Hg'])),
        'Hf': ev(p['Hf']),
        'C': ev(o['C']),
        'K': ev(o['K']),
        'B_N': ev(o['operator']['N'][1]),
        'B_M': ev(o['operator']['M'][1]),
        'E_N': ev(o['operator']['N'][2]),
        'E_M': ev(o['operator']['M'][2]),
        'Delta': ev(delta),
        'lower_residual': ev(residual),
    }
    return t, out


def certificate():
    t, f = exact_family()
    for key in ('Fz', 'Fz_r', 'Hg_r', 'Hf', 'C', 'B_M', 'E_M'):
        assert f[key] == 0, (key, f[key])
    assert f['K'] == 1
    assert f['Hg'] == 2*t
    assert f['B_N'] == f['Delta'] == f['lower_residual'] == -S.Rational(416,125)*t
    assert f['E_N'] == -S.Rational(32,25)*t
    assert S.cancel(f['lower_residual'] + S.Rational(208,125)*f['Hg']) == 0
    assert S.cancel(f['E_N'] + S.Rational(16,25)*f['Hg']) == 0
    assert f['lower_residual'].subs(t, 1) == -S.Rational(416,125)
    assert f['Hg'].subs(t, 1) == 2
    assert all(f[k].subs(t, 0) == 0 for k in ('Hg','B_N','B_M','E_N','E_M'))
    return {
        'original_git_blobs': ORIGINAL_BLOBS,
        'scope': 'exact one-parameter NONPHYSICAL local Step58 slice, minimal Step57 import shim',
        'identically_zero': ['Fz','Fz_r','Hg_r','Hf','C','B_M','E_M'],
        'K': '1', 'z': '3/5', 'positive_dust': ['7/4','1'],
        'Hg': '2*t', 'B_N': '-416*t/125', 'E_N': '-32*t/25',
        'lower_residual': 'B_N-z*C/Lg-beta*Hg_r=-208*Hg/125 on this slice',
        'counterexample_t_1': 'Fz=Fz_r=Hg_r=Hf=C=B_M=E_M=0 but Hg=2, B_N=-416/125',
        'on_full_primary_t_0': 'Hg=B_N=E_N=0; does not prove universal factorization',
        'universal_B_N_factorization': 'NOT_PROVED_OR_REFUTED_ON_FULL_PRIMARY_SHELL',
        'physical_six_A_B_E': 'NOT_CERTIFIED',
        'two_boundary_BVP': 'NOT_CERTIFIED',
        'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED',
    }

if __name__ == '__main__':
    import json
    print(json.dumps(certificate(), indent=2))
