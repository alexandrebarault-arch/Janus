"""Exact rational independent audit of the archived Step58 sign *coverage*.

This verifies published certificate consistency, not the Step55 ODE or Step58
operator. In particular, four isolated certified radii never become an annular
continuum certificate. No interpolation or sign extrapolation is performed.
"""
from fractions import Fraction as F
from hashlib import sha1
import json
from pathlib import Path

CONTINUUM_REPORT = 'research/reports/gate2b-step68ad-C2d2e3-Step58-correlated-MVT.json'
POINT_REPORT = 'research/reports/gate2b-b3c3d6-step58-physical-ANAM-four-radii-sign.json'
EXPECTED_SHA = {
    CONTINUUM_REPORT: '0c688d6648e16064b1eb4e8ad9c55e7b44a95947',
    POINT_REPORT: 'c502b9779056e8a493c43d330696515a661128c4',
}
DOMAIN = (F(0), F(17, 20))
EXPECTED_CONTINUUM = (F(1, 64), F(1, 32))
EXPECTED_POINTS = tuple(map(F, ('1/4', '1/2', '7/10', '17/20')))


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def git_blob(raw):
    return sha1(b'blob ' + str(len(raw)).encode('ascii') + b'\0' + raw).hexdigest()


def load_pinned(root):
    root = Path(root)
    reports = []
    for path, expected in EXPECTED_SHA.items():
        raw = (root / path).read_bytes()
        _require(git_blob(raw) == expected, 'report blob SHA mismatch: ' + path)
        reports.append(json.loads(raw))
    return reports


def verify_continuum(report):
    _require(report.get('GATE_2B') == 'OPEN' and report.get('JANUS_R') == 'NOT_VALIDATED', 'status changed')
    _require(report.get('N_positive_continuum') is True and report.get('M_negative_continuum') is True, 'report status')
    _require(report.get('covered_r') == ['1/64', '1/32'], 'unexpected declared domain')
    _require(len(report['cells']) == 7, 'unexpected original cell count')
    _require(report.get('adaptive_bisections') == 1, 'unexpected refinement count')
    _require(report.get('total_leaves') == 225, 'unexpected declared leaf count')
    previous = None
    lower_n = None
    upper_m = None
    count = 0
    for cell in report['cells']:
        a, b = map(F, cell['r'])
        _require(a < b and cell['leaves'], 'invalid original cell')
        _require(F(cell['leaves'][0]['r'][0]) == a, 'cell start mismatch')
        _require(F(cell['leaves'][-1]['r'][1]) == b, 'cell end mismatch')
        for leaf in cell['leaves']:
            lo, hi = map(F, leaf['r'])
            nl, nu = map(F, leaf['N'])
            ml, mu = map(F, leaf['M'])
            _require(lo < hi and nl <= nu and ml <= mu, 'invalid interval')
            _require(nl > 0 and mu < 0, 'uncertified sign')
            _require(previous is None or previous == lo, 'gap or overlap')
            previous = hi
            lower_n = nl if lower_n is None else min(lower_n, nl)
            upper_m = mu if upper_m is None else max(upper_m, mu)
            count += 1
    _require(count == 225 and F(report['cells'][0]['r'][0]) == EXPECTED_CONTINUUM[0] and previous == EXPECTED_CONTINUUM[1], 'coverage incomplete')
    _require(lower_n == F(report['min_N_lower']), 'min N does not match leaves')
    _require(upper_m == F(report['max_M_upper']), 'max M does not match leaves')
    return {'verified_leaves': count, 'original_cells': len(report['cells']),
            'continuum_r': list(map(str, EXPECTED_CONTINUUM)),
            'min_A_N_lower': str(lower_n), 'max_A_M_upper': str(upper_m)}


def verify_points(report):
    _require(report.get('GATE_2B') == 'OPEN' and report.get('JANUS_R') == 'NOT_VALIDATED', 'point status changed')
    boxes = report['strict_bounds_integer']
    _require(set(boxes) == set(map(str, EXPECTED_POINTS)), 'unexpected point set')
    for r, row in boxes.items():
        nlo, nhi = row['A_N']
        mlo, mhi = row['A_M']
        slo, shi = row['sum']
        _require(all(isinstance(x, int) and not isinstance(x, bool) for x in (nlo, nhi, mlo, mhi, slo, shi)), 'noninteger bound')
        _require(0 < nlo <= nhi and mlo <= mhi < 0 and slo <= shi < 0, 'point sign failure: '+r)
        # Sum bounds are independently enclosed; they need not equal endpoint sums.
        _require(slo <= nhi + mhi and shi >= nlo + mlo, 'inconsistent sum intervals: '+r)
    return {'verified_point_radii': list(map(str, EXPECTED_POINTS)), 'point_count': len(boxes)}


def audit(continuum, points):
    a = verify_continuum(continuum)
    b = verify_points(points)
    # Isolated radii have zero interior: they do not fill any open interval.
    return {'step': 'b3c3d8_ARCHIVED_SIGN_COVERAGE_INDEPENDENT_INTEGRITY_AUDIT',
            'kind': 'EXACT_RATIONAL_REPORT_CONSISTENCY_ONLY',
            'source_report_git_blobs': EXPECTED_SHA.copy(),
            **a, **b,
            'uncertified_open_intervals_r': [
                ['0', '1/64'], ['1/32', '1/4'], ['1/4', '1/2'],
                ['1/2', '7/10'], ['7/10', '17/20']],
            'annular_target_r': ['1/4', '17/20'],
            'annular_continuum_certified': False,
            'operator_or_ODE_replayed': False,
            'limitations': 'Verifies archived rational report arithmetic and coverage, not physical Step55/58 recomputation; open gaps may contain unknown signs.',
            'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED'}


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--repo', type=Path, default=Path.cwd())
    p.add_argument('--out', type=Path)
    args = p.parse_args()
    result = audit(*load_pinned(args.repo))
    output = json.dumps(result, sort_keys=True, indent=2) + '\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(output, encoding='utf-8')
    else:
        print(output, end='')


if __name__ == '__main__':
    main()
