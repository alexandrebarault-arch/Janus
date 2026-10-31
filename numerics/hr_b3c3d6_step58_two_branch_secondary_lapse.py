"""Exact LOCAL two-branch secondary and formal lapse sign diagnostic.

Authentic Step45/58, minimal Step57 import shim. Fz_rr, Hf_r and C_r
are deliberately checked and NONZERO: no claim of a physical solution.
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
        'C': o['C'], 'A_N':o['operator']['N'][0], 'A_M':o['operator']['M'][0],
        'B_N': o['operator']['N'][1],
        'B_M': o['operator']['M'][1],
        'E_N': o['operator']['N'][2], 'E_M': o['operator']['M'][2],
        'Hf':p['Hf'],
        'Fz_rr':o['Dt'](Fr), 'Hf_r':o['Dt'](p['Hf']),
        'C_r':o['Dt'](o['C']), 'K': o['K'],
    }.items()}
    return a, b, solved, results


def certificate():
    a,b,solved,r=exact_family()
    expected={
        'C':-(25*a+24*b+12)/20,
        'Hf':b*b-1,
        'A_N':(1200*a*b-3775*a-2048*b*b+2952*b+4408)/1000,
        'A_M':(625*a*a-9600*a*b+3600*a+2400*b*b-4704*b-22336)/4000,
        'B_N':-3*(25*a+24*b+12)/100,
    }
    for k,e in expected.items():
        assert S.cancel(r[k]-e)==0,(k,r[k],e)
    for k in ('Fz','Fz_r','Hg','Hg_r','B_M','E_N','E_M'):
        assert r[k]==0,(k,r[k])
    assert r['K']==1
    branches=[]
    for bb,aa in ((S.S.One,-S.Rational(36,25)),(-S.S.One,S.Rational(12,25))):
        sub={a:aa,b:bb}
        vals={k:S.cancel(v.subs(sub)) for k,v in r.items()}
        for k in ('Fz','Fz_r','Hg','Hg_r','Hf','C','B_N','B_M','E_N','E_M'):
            assert vals[k]==0,(bb,k,vals[k])
        ratio=S.cancel(-vals['A_N']/vals['A_M'])
        assert vals['A_M']!=0
        branches.append({'b':str(bb),'a':str(aa),
                         'A_N':str(vals['A_N']),'A_M':str(vals['A_M']),
                         'formal_M_over_N':str(ratio),
                         'positive_lapses_pointwise':bool(ratio>0),
                         'Fz_rr':str(vals['Fz_rr']),
                         'Hf_r':str(vals['Hf_r']),
                         'C_r':str(vals['C_r'])})
    assert branches[0]['formal_M_over_N']=='2255/919'
    assert branches[1]['formal_M_over_N']=='-745/547'
    assert (branches[0]['Fz_rr'],branches[0]['Hf_r'],branches[0]['C_r'])==('65/64','-51/16','349/100')
    assert (branches[1]['Fz_rr'],branches[1]['Hf_r'],branches[1]['C_r'])==('-191/64','113/16','-59/100')
    return {'source_blobs':ORIGINAL_BLOBS,'step57':'MINIMAL_IMPORT_SHIM',
            'scope':'NONPHYSICAL LOCAL FROZEN-JET SLICE; NOT FULL HOLONOMIC SHELL',
            'two_parameter_polynomials':{k:str(S.factor(v)) for k,v in expected.items()},
            'two_pointwise_branches':branches,
            'caution':'Fz_rr, Hf_r and C_r nonzero on BOTH branches: not a full radial solution or Step55.',
            'universal_BN_factorization':'NOT_PROVED',
            'physical_step55_six_coefficients':'NOT_CERTIFIED',
            'two_boundary_positive_lapse_BVP':'NOT_CERTIFIED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(certificate(),indent=2))
