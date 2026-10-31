"""Exact algebraic FAMILY probes for original Step58 first-lapse jets.

Not a universal factorization or Step55 four-radius enclosure. On Fz=Fz'=Hg=Hg'=0,
check B_M=0 and B_N=z*C/Lg on two explicit positive-chart algebraic slices.
Original Step45 and Step58 sources must match their authenticated Git blobs.
"""
from hashlib import sha1
from pathlib import Path
from functools import lru_cache
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step58_temporal_operator import physical_operator, highest_lapse_certificate

ORIGINAL = {
    'hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def check_blobs():
    for name, expected in ORIGINAL.items():
        raw = Path(__file__).with_name(name).read_bytes()
        assert sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest() == expected
    return True

@lru_cache(maxsize=1)
def make_operator():
    check_blobs()
    op = physical_operator()
    original = exact_physical_ward()
    q = dict(zip(original['Q'], original['q']))
    qp = dict(zip(original['Q'], original['dq']))
    root = sp.sqrt(1-op['z']**2)
    # Fz=0 determines pLg'.  Hg=0 then determines pg linearly.
    plgr = (q['pSg']*qp['Sg']+q['pg']*qp['tg']-op['K']*op['z']/root)/q['Lg']
    hg = original['Hg'].subs({qp['pLg']: plgr})
    # Fz'=0 determines pLg''.  Hg'=0 determines Sg'''.
    dhg = op['Dt'](original['Hg'])
    expressions = {
        'pg0': hg.subs(q['pg'], 0), 'pgcoef': sp.diff(hg, q['pg']),
        'plgr': plgr, 'plgrr': op['Dt'](plgr),
        'sgrrr0': dhg.subs(op['qppp'][2], 0),
        'sgrrrcoef': sp.diff(dhg, op['qppp'][2]),
        'Fz': op['Fz'], 'dFz': op['Dt'](op['Fz']),
        'Hg': original['Hg'], 'dHg': dhg,
        'C': op['C'], 'BN': op['operator']['N'][1],
        'BM': op['operator']['M'][1],
    }
    return op, original, q, qp, expressions

@lru_cache(maxsize=2)
def exact_family(kind):
    """Return exact residuals and a NONZERO C witness on an algebraic slice.

    z_rational: 6 symbolic canonical/jet variables, z=2t/(1+t^2), 0<t<1.
    fixed_z: 20 symbolic variables including Lg,Lf,Sg,Sf, z=3/5.
    In both slices tgr=3*Lg/4, so the dust square root is 5/4.
    No claim that these slices equal the physical Step55 radial solution.
    """
    op, original, q, qp, expr = make_operator()
    s = {v: sp.Rational(1, 3) for v in
         (*op['q'], *op['qp'], *op['qpp'], *op['qppp'], *op['q4'],
          op['z'], op['zr'], op['zrr'], op['zrrr'])}
    s.update({v: sp.Integer(1) for v in original['parameters'][:8]})
    s.update({q['Lg']: sp.Integer(2), q['Lf']: sp.Integer(3),
              q['Sg']: sp.Integer(4), q['Sf']: sp.Integer(5),
              q['pLg']: sp.Rational(1, 2), q['pLf']: sp.Rational(2, 3),
              q['pSg']: sp.Rational(1, 4), q['pSf']: sp.Rational(-1, 5),
              op['zr']: sp.Rational(1, 7), op['zrr']: sp.Integer(0),
              op['zrrr']: sp.Integer(0), original['parameters'][2]: sp.Rational(1, 10)})
    if kind == 'z_rational':
        tau = sp.symbols('tau', positive=True)
        s[op['z']] = 2*tau/(1+tau*tau)
        varying = (q['pLg'], q['pLf'], q['pSg'], q['pSf'], qp['pSg'], qp['pg'])
    elif kind == 'fixed_z':
        tau = None
        s[op['z']] = sp.Rational(3, 5)
        varying = (q['Lg'], q['Lf'], q['Sg'], q['Sf'], q['pLg'], q['pLf'],
                   q['pSg'], q['pSf'], q['pf'], qp['pSg'], qp['pg'],
                   qp['Lg'], qp['Sg'], qp['Lf'], qp['Sf'], qp['pLf'],
                   op['qpp'][0], op['qpp'][2], op['qpp'][4], op['zr'])
    else:
        raise ValueError(kind)
    for v, x in zip(varying, sp.symbols('x0:'+str(len(varying)), real=True)):
        s[v] = x
    s[qp['tg']] = sp.Rational(3, 4)*s[q['Lg']]
    s[qp['tf']] = sp.Integer(0)
    def ev(name):
        e = expr[name]
        if tau is not None:
            z = op['z']; root = (1-tau*tau)/(1+tau*tau)
            e = e.replace(lambda x: isinstance(x, sp.Pow) and
                          x.base == 1-z*z and x.exp.is_Rational and x.exp.q == 2,
                          lambda x: root**(2*x.exp))
        return e.xreplace({v: s[v] for v in e.free_symbols if v in s})
    # Solve all four shell equations in a causally ordered, exact way.
    s[q['pg']] = -ev('pg0')/ev('pgcoef')
    s[qp['pLg']] = ev('plgr')
    s[op['qpp'][1]] = ev('plgrr')
    s[op['qppp'][2]] = -ev('sgrrr0')/ev('sgrrrcoef')
    shell = {k: sp.simplify(ev(k)) for k in ('Fz', 'dFz', 'Hg', 'dHg')}
    c = ev('C'); bn = ev('BN'); bm = ev('BM')
    return {
        'kind': kind, 'symbolic_variables': len(varying),
        'shell_zero': all(x == 0 for x in shell.values()),
        'BM_zero': sp.simplify(bm) == 0,
        'BN_minus_zC_over_Lg_zero': sp.simplify(bn-s[op['z']]*c/s[q['Lg']]) == 0,
        'C_nonzero_as_expression': sp.simplify(c) != 0,
        'C_operations': sp.count_ops(c),
    }

def run():
    high = highest_lapse_certificate()
    assert high['N2_and_M2_vanish_on_Fz_and_Hg']
    rows = [exact_family('z_rational'), exact_family('fixed_z')]
    for row in rows:
        assert all(row[k] for k in ('shell_zero','BM_zero',
                                   'BN_minus_zC_over_Lg_zero','C_nonzero_as_expression'))
    return {'source_blobs': ORIGINAL, 'algebraic_family_probes': rows,
            'E_N_E_M': 'EXACT_ZERO_ON_Fz_Hg_FROM_ORIGINAL_STEP58',
            'B_N_B_M': 'CANDIDATE_SHELL_FACTOR_NOT_UNIVERSALLY_PROVED',
            'physical_Step55_four_radii_B_enclosures': 'NOT_CERTIFIED',
            'lapse_BVP': 'NOT_CERTIFIED', 'GATE_2B': 'OPEN',
            'JANUS_R': 'NOT_VALIDATED'}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
