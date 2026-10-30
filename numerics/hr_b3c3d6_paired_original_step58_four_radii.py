"""Paired-state four-radius runner for original Step58, not a certification.

One DOP853 integration per radius is shared by historical mixed affine,
true holonomic affine (negative control), quadratic and cubic. Requires
original SHA-guarded Step45/46/55/58 modules in the JANUS repository.
No independent per-mode integrations, no claims about Dirac or BVP.
"""
import json
from contextlib import contextmanager
from copy import copy

RADII = (0.25, 0.5, 0.7, 0.85)
MODES = ('historical_mixed_affine', 'holonomic_affine',
         'holonomic_quadratic', 'holonomic_cubic')

@contextmanager
def temporarily(module, **replacements):
    old = {key: getattr(module, key) for key in replacements}
    try:
        for key, value in replacements.items():
            setattr(module, key, value)
        yield
    finally:
        for key, value in old.items():
            setattr(module, key, value)


def truncate_jets(jets, s, mode, mp):
    """Keep exact ODE U_s and U_ss; truncate only the chosen Taylor order.

    The pLf derivatives used by the candidate's internal consistency checks
    must refer to the SAME truncated holonomic polynomial, not the full ODE.
    """
    if mode not in ('holonomic_affine', 'holonomic_quadratic', 'holonomic_cubic'):
        raise ValueError(mode)
    out = copy(jets)
    if mode == 'holonomic_cubic':
        return out
    r = mp.sqrt(s)
    if mode == 'holonomic_affine':
        out['U_ss'] = mp.mpf(0)
    out['U_sss'] = mp.mpf(0)
    u, u1 = jets['U_value'], jets['U_s']
    u2 = out['U_ss']
    out['pLf_second'] = 2*u + 10*s*u1 + 4*s*s*u2
    out['pLf_third'] = 24*r*u1 + 36*r*s*u2
    return out


def compare_coefficients(reports):
    base = reports['historical_mixed_affine']['coefficients']
    differences = {}
    for mode in MODES[1:]:
        current = reports[mode]['coefficients']
        diff = {}
        for lapse in ('N', 'M'):
            for order in ('0', '1', '2'):
                a, b = base[lapse][order], current[lapse][order]
                diff[f'{lapse}{order}'] = b-a
        differences[mode] = diff
    return differences


def run_radius(radius, affine_module, cubic_module, mp):
    """Run original Step58 using ONE candidate DOP853 terminal state.

    Caller provides imported original modules. This module deliberately
    does not monkeypatch the original source hash checks or physical operator.
    """
    if radius not in RADII:
        raise ValueError('Only the four historical radii are supported')
    state = cubic_module.u_solution(radius)
    ur, gr, sol = state
    s = cubic_module.F(radius)**2
    def common_solution(_radius):
        if _radius != radius:
            raise AssertionError('radius changed inside paired probe')
        return state
    original_jet_map = cubic_module.endpoint_jets
    def make_jets(mode):
        def evaluate(G, s0, u):
            if abs(s0-s) > mp.mpf('1e-38') or abs(u-ur) > mp.mpf('1e-38'):
                raise AssertionError('unpaired endpoint state')
            jets = original_jet_map(G, s0, u)
            if mode == 'holonomic_cubic':
                return jets
            augmented = dict(jets, U_value=u)
            return truncate_jets(augmented, s0, mode, mp)
        return evaluate
    reports = {}
    with temporarily(affine_module, u_solution=common_solution):
        reports['historical_mixed_affine'] = affine_module.main(radius)
    with temporarily(cubic_module, u_solution=common_solution):
        for mode in MODES[1:]:
            with temporarily(cubic_module, endpoint_jets=make_jets(mode)):
                reports[mode] = cubic_module.main(radius)
    for mode, report in reports.items():
        report['paired_jet_mode'] = mode
        report['paired_state_from_one_DOP853'] = True
        # The original candidate's own cubic metadata applies only to cubic.
        if mode != 'holonomic_cubic':
            report['ode_jet_map'] = 'TRUNCATED_HOLONOMIC_' + mode.upper()
            report.pop('holonomic_residuals', None)
            report.pop('affine_jet_defects', None)
    return {'radius':str(radius), 'shared_U':str(ur), 'shared_G':str(gr),
            'nfev':sol.nfev, 'reports':reports,
            'differences_from_historical_mixed_affine':compare_coefficients(reports),
            'interpretation':'NUMERICAL_POINT_COMPARISON_ONLY_NO_INTERVAL_CERTIFICATE'}


def run_all():
    import mpmath as mp
    from . import hr_b3c3d6_full_original_step58_point_probe as affine
    from . import hr_b3c3d6_corrected_step58_point_probe_candidate as cubic
    return {'radii':[run_radius(r, affine, cubic, mp) for r in RADII],
            'GATE_2B':'OPEN', 'JANUS_R':'NOT_VALIDATED',
            'physical_BVP':'NOT_TESTED', 'Dirac':'NOT_TESTED'}

if __name__ == '__main__':
    print(json.dumps(run_all(), indent=2))
