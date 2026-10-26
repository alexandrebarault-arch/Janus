"""Authenticated, conditional seven-cell evaluation of original Step60 lower-jet quotient.

This evaluates the exact original Step60 q'''-free representatives, NOT a
new Hamiltonian and NOT a Dirac-rank/lapse certificate.  The sole algebraic
rewrite is the proven on-shell interaction denominator T.  No continuum
sign is asserted for intervals overlapping zero.
"""
from __future__ import annotations
from functools import lru_cache
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch
import json
import sympy as sp

from . import hr_step68o_temporal_interval_annulus as annulus
from . import hr_step55_global_barrier as old
from .hr_step68n_interval_ode_jets import I, Jet
from .hr_step68ad_c2b_center_boxes import load_pinned, certify_cells, Q, validate_reports
from .hr_step68ad_c2d2a_temporal_replay import (
    verify_original_files, box_for_rounded_s, inject_s_jet, classify_sign,
)
from .hr_step68ad_c2d2b_executed_temporal_probe import factored_compiled
from .hr_step60_full_constraint_prolongation import (
    full_constraint_prolongation, verified_original_sources,
)
from .hr_step58_temporal_operator import physical_operator
from .hr_step45_exact_physical_ward import exact_physical_ward

# These CSE positions are tied to the pinned original Step60 SHA, and checked
# against the original T expression on EVERY compilation; fail closed on drift.
CSE_T = {'BN': 103, 'AM': 107}
LOWER_KEYS = {'BN': 'third_free_BN_on_Fz', 'AM': 'third_free_AM_on_Fz'}


def shell_denominator_cse(exps, syms, index):
    repl, reduced = sp.cse(exps)
    if index >= len(repl):
        raise AssertionError('Original Step60 CSE index absent')
    sg, sf, lg, lf = (next(x for x in syms if str(x) == name)
                      for name in ('Sg', 'Sf', 'Lg', 'Lf'))
    b1, b2, b3 = (next(x for x in syms if str(x) == name)
                  for name in ('beta1', 'beta2', 'beta3'))
    expanded = repl[index][1]
    for symbol, sub in reversed(repl[:index]):
        expanded = expanded.xreplace({symbol: sub})
    T = b1 * sg**2 + 2*b2*sg*sf + b3*sf**2
    if sp.simplify(expanded - T) != 0:
        raise AssertionError('Step60 denominator not original interaction T')
    factored = sg**2*(b1 + 2*b2*(lf/lg) + b3*(lf/lg)**2)
    if sp.simplify((T-factored).subs(sf,sg*lf/lg)) != 0:
        raise AssertionError('Step60 on-shell denominator identity failed')
    repl[index] = (repl[index][0], factored)
    return repl, reduced


@lru_cache(maxsize=1)
def compiled_lower_quotient():
    verified_original_sources()
    original = full_constraint_prolongation()
    pair = {}
    for label, name in LOWER_KEYS.items():
        expr = original[name]
        o = physical_operator()
        if any(expr.has(q) for q in (*o['qppp'], *o['q4'])):
            raise AssertionError('Step60 representative still has higher jets')
        halfpow = sp.Function('interval_halfpow')
        safe = expr.replace(
            lambda x: x.is_Pow and x.exp.is_Rational and x.exp.q == 2,
            lambda x: halfpow(x.base, sp.Integer(x.exp.p)))
        syms = tuple(sorted(expr.free_symbols, key=str))
        idx = CSE_T[label]
        def transform(exps, _syms=syms, _idx=idx):
            return shell_denominator_cse(exps, _syms, _idx)
        fn = sp.lambdify(syms, safe,
            modules=[{'interval_halfpow': lambda x,p: x.sqrt()**int(p),
                      'sqrt': lambda x: x.sqrt(), 'Abs': abs}, 'math'],
            cse=transform)
        pair[label] = (syms, fn)
    return pair


def canonical_symbol_values(rlo, rhi):
    canonical, R, si, _ = annulus.canonical_jets_cell(rlo, rhi)
    o = physical_operator()
    p = exact_physical_ward()
    vals = {}
    for keys, degree in ((o['q'],0),(o['qp'],1),(o['qpp'],2),(o['qppp'],3)):
        for symbol, name in zip(keys, p['Q']):
            vals[symbol] = canonical[name].a[degree]*{0:1,1:1,2:2,3:6}[degree]
    for symbol in o['q4']:
        vals[symbol] = I.c(0)
    for symbol, value in zip((o['z'],o['zr'],o['zrr'],o['zrrr']),
                             (R*old.Z1, old.Z1, I.c(0), I.c(0))):
        vals[symbol] = value
    for symbol, name in zip(p['parameters'][:8],
                            ('MG','MF','M2','B0','B1','B2','B3','B4')):
        vals[symbol] = getattr(old,name)
    return vals


def evaluate_lower_quotient(rlo, rhi, reports):
    lo, hi = F(rlo), F(rhi)
    if not (F(0) < lo <= hi <= F(1,32)):
        raise ValueError('Outside positive seven-cell chart')
    si = I.hull(lo,hi)**2
    box = box_for_rounded_s(reports,si,{'r':[str(lo),str(hi)]},Q,validate_reports)
    with inject_s_jet(annulus,box,Jet,I,si):
        vals = canonical_symbol_values(lo,hi)
    result = {}
    for label,(syms,fn) in compiled_lower_quotient().items():
        if not all(x in vals for x in syms):
            raise AssertionError('Missing canonical jet in original Step60')
        raw = fn(*[vals[x] for x in syms])
        if isinstance(raw, list) and len(raw)==1:
            raw=raw[0]
        value = I.c(raw)
        result[label] = {'enclosure':[str(F(value.lo,10**28)),str(F(value.hi,10**28))],
                         'sign':classify_sign(value)}
    return result


def run(repo):
    repo = Path(repo).resolve()
    provenance = verify_original_files(repo/'numerics')
    provenance.update(verified_original_sources())
    reports = load_pinned(repo/'research'/'reports')
    boxes = certify_cells(reports)
    if boxes['cell_count']!=7 or boxes['closed_radius_domain']!=['1/64','1/32']:
        raise AssertionError('Unexpected physical radial cover')
    cells = []
    for box in boxes['cells']:
        lo,hi = map(F,box['r'])
        cells.append({'r':box['r'],'lower_quotient':evaluate_lower_quotient(lo,hi,reports)})
    edges = [F(cells[0]['r'][0])] + [F(x['r'][1]) for x in cells]
    if len(edges)!=8 or edges[-1]!=F(1,32):
        raise AssertionError('Incomplete edge coverage')
    pointwise=[]
    with patch.object(annulus,'_compiled',factored_compiled):
        for r in edges:
            lower = evaluate_lower_quotient(r,r,reports)
            si = I.hull(r,r)**2
            box = box_for_rounded_s(reports,si,{'r':[str(r),str(r)]},Q,validate_reports)
            with inject_s_jet(annulus,box,Jet,I,si):
                original = annulus.evaluate_cell(r,r)
            # A_M and lower A_M must overlap on the prescribed spatial shell.
            l0,l1=map(F,lower['AM']['enclosure'])
            if max(l0,F(original['M'].lo,10**28)) > min(l1,F(original['M'].hi,10**28)):
                raise AssertionError('Step60 lower A_M incompatible with Step58 on physical shell')
            pointwise.append({'r':str(r),'lower_quotient':lower,
                              'AM_overlaps_original_Step58':True})
    return {'step':'68ad-C2d2c-Step60-lower-jet-quotient-executed',
            'original_source_git_blobs':provenance,
            'original_input_report_git_blobs':boxes['pinned_original_report_git_blobs'],
            'method':'Original Step60 third-free BN/AM evaluated with original Step68o canonical jets; exact on-shell T CSE factorization verified against original expressions',
            'shell_assumptions':'r>0, Lg>0, K>0, Sf=Sg*Lf/Lg, stationary Fz=0 and pLgprime elimination; original Step60 third-jet cancellation',
            'seven_cell_lower_quotient':cells,'eight_pointwise_edges':pointwise,
            'continuous_signs_certified':sum(row['lower_quotient'][name]['sign']!='INCOMPLETE' for row in cells for name in ('BN','AM')),
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'limitations':'This is a conditional enclosure of two Step60 lower-jet representatives, NOT a rank, lapse, boundary, or 4D consistency proof. Step58 original 14 continuum signs remain uncertified.'}


def main():
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    report=run(args.repo)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'cells':len(report['seven_cell_lower_quotient']),
                      'edges':len(report['eight_pointwise_edges']),
                      'continuous_signs_certified':report['continuous_signs_certified'],
                      'out':str(args.out)}))

if __name__=='__main__':main()
