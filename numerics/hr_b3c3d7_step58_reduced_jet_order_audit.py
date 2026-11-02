"""Exact Step45/46/58 dependency audit on the prescribed Step55 spatial chart.

No continuous interval enclosure is computed. This proves the maximal U-jet
order of the *zero-lapse-derivative* Step58 coefficients before numerical
substitution, on the Step46 primary map and Fz=0 shell only.
"""
from hashlib import sha1
from pathlib import Path
import sympy as sp
from .hr_step45_exact_physical_ward import exact_physical_ward
from .hr_step46_exact_secondary_ode import exact_f_momentum_ode
from .hr_step58_temporal_operator import physical_operator

SOURCE_SHA = {
    'hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
}
VARIABLE_ORDER = {'pLf': 0, 'pSf': 1, 'pf': 1}


def verify_sources(root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for filename, expected in SOURCE_SHA.items():
        raw = (root / 'numerics' / filename).read_bytes()
        actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if actual != expected:
            raise ValueError(f'original source mismatch {filename}: {actual}')
    return SOURCE_SHA.copy()


def dependency_rows():
    op = physical_operator()
    names = exact_physical_ward()['Q']
    result = {}
    for label in ('N', 'M'):
        expr = op['operator'][label][0]
        by_order = {}
        for order, group in enumerate((op['q'], op['qp'], op['qpp'], op['qppp'], op['q4'])):
            by_order[order] = tuple(name for name, symbol in zip(names, group)
                                    if symbol in expr.free_symbols)
        relevant = [(name, base + order)
                    for order, row in by_order.items()
                    for name in row if (base := VARIABLE_ORDER.get(name)) is not None]
        result[label] = {'all_fields_by_radial_jet_order': by_order,
                         'U_dependent_fields_and_U_order': tuple(relevant),
                         'max_U_derivative_order': max((order for _, order in relevant), default=-1)}
    return result


def exact_shell_sensitivity():
    p = exact_physical_ward()
    op = physical_operator()
    primary = exact_f_momentum_ode()
    q = dict(zip(p['Q'], p['q']))
    dq = dict(zip(p['Q'], p['dq']))
    z, Lg, Lf = op['z'], q['Lg'], q['Lf']
    shift_root = sp.sqrt(1 - z*z)
    Fz_zero = {dq['pLg']: (q['pSg']*dq['Sg'] + q['pg']*dq['tg']
                           - op['K']*z/shift_root)/Lg}
    an = op['operator']['N'][0]
    am = op['operator']['M'][0]
    C_pSf = sp.diff(p['C_exact'], q['pSf'])
    d_am = sp.diff(am, dq['pSf'])
    assert sp.diff(an, dq['pSf']) == 0
    assert sp.diff(d_am, dq['pSf']) == 0
    assert sp.cancel(d_am.subs(Fz_zero) - z/Lf*C_pSf) == 0
    V = primary['V']
    dpSf_dV = sp.diff(primary['pS_f'], V)
    fac = q['pLf']/(2*p['parameters'][1]*q['Sf']*dq['Sf'])
    beta = sp.sqrt(1+dq['tf']**2/Lf**2)
    assert sp.cancel(dpSf_dV - Lf*beta/(dq['Sf']*(beta+fac*dq['tf']))) == 0
    assert sp.cancel(primary['coefficient'] - C_pSf*dpSf_dV) == 0
    # For pLf=r² U(r²), pLf''=2U+10r² U_s+4r⁴ U_ss.
    # Hence d(pSf_r)/d(U_ss)=4r⁴ * d(pSf)/d(pLf_r).
    r = sp.symbols('r', positive=True)
    d_am_d_Uss = 4*r**4*z/Lf*primary['coefficient']
    assert sp.simplify(d_am_d_Uss - 4*r**4*z/Lf*C_pSf*dpSf_dV) == 0
    return {'A_N_max_U_order': 1, 'A_M_max_U_order': 2,
            'dA_N_dUss': '0',
            'dA_M_dUss_on_Fz_primary': '4*r**4*z*C1/Lf',
            'C1': 'Step46 coefficient dC/d(pLf_prime), nonzero on positive regular chart',
            'dA_M_d(pSf_r)_on_Fz': 'z*C_pSf/Lf',
            'physical_continuum_enclosure': False}


def audit(root=None):
    verify_sources(root)
    rows = dependency_rows()
    assert rows['N']['max_U_derivative_order'] == 1
    assert rows['M']['max_U_derivative_order'] == 2
    assert all(not row['all_fields_by_radial_jet_order'][4] for row in rows.values())
    sensitivity = exact_shell_sensitivity()
    return {'scope': 'EXACT_ORIGINAL_STEP45_46_58_JET_DEPENDENCE_ON_PRESCRIBED_STEP55_CHART',
            'source_blobs': SOURCE_SHA,
            'zero_lapse_derivative_coefficients': {k: {'U_dependent_fields': [f'{name}:U_order_{n}' for name,n in v['U_dependent_fields_and_U_order']],
                                                     'max_U_order': v['max_U_derivative_order']}
                                                   for k,v in rows.items()},
            'sensitivity': sensitivity,
            'direct_interval_gate_requires_G_second_partials': False,
            'direct_interval_gate_requires_G_first_partials': True,
            'note': 'Derivative-of-A_M gate still requires U_sss and second partials of G; direct sign enclosures need only U_ss. No continuous physical signs evaluated.',
            'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED'}


if __name__ == '__main__':
    import json
    print(json.dumps(audit(), indent=2))
