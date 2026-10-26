"""Authenticated seven-cell Step58 replay, with an exact on-shell CSE rewrite.

This does NOT prove continuum temporal signs.  It executes the unmodified
original Step58 expression and Step68o canonical profile through an equivalent
factorization of ONE interaction denominator, then runs the original Step60
symbolic quotient.  Interval bounds crossing zero remain INCOMPLETE.

The CSE rewrite is valid only on Sg=r*Lg, Sf=r*Lf, r>0, Lg>0.  It is
explicitly verified against the original symbolic CSE for pinned sources.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from unittest.mock import patch
import json
import sympy as sp
from . import hr_step68o_temporal_interval_annulus as annulus
from .hr_step68ad_c2d2a_temporal_replay import (
    run as run_original_replay, box_for_rounded_s, inject_s_jet, git_blob,
)
from .hr_step68ad_c2b_center_boxes import load_pinned, Q, validate_reports
from .hr_step68n_interval_ode_jets import Jet, I

ORIGINAL_COMPILED = annulus._compiled
CSE_INDICES = {"N": 79, "M": 75}


def denominator_identity(original_operator, label):
    """Prove original CSE denominator = T and its shell factorization."""
    expr = original_operator['operator'][label][0]
    P = sp.Function('interval_halfpow')
    safe = expr.replace(lambda x: x.is_Pow and x.exp.is_Rational and x.exp.q == 2,
                        lambda x: P(x.base, sp.Integer(x.exp.p)))
    syms = tuple(sorted(expr.free_symbols, key=str))
    repl, reduced = sp.cse(safe)
    index = CSE_INDICES[label]
    symbol, original = repl[index]
    symbols = {str(x): x for x in syms}
    sg, sf, lg, lf = (symbols[x] for x in ('Sg', 'Sf', 'Lg', 'Lf'))
    b1, b2, b3 = (symbols[x] for x in ('beta1', 'beta2', 'beta3'))
    expanded = original
    for key, sub in reversed(repl[:index]):
        expanded = expanded.xreplace({key: sub})
    T = b1*sg**2 + 2*b2*sg*sf + b3*sf**2
    if sp.simplify(expanded - T) != 0:
        raise AssertionError(f'{label}: original CSE denominator drift')
    alternative = sg**2*(b1 + 2*b2*(lf/lg) + b3*(lf/lg)**2)
    if sp.simplify((T - alternative).subs(sf, sg*lf/lg)) != 0:
        raise AssertionError(f'{label}: on-shell factorization failed')
    return syms, safe, repl, reduced, index, alternative


@lru_cache(maxsize=1)
def factored_compiled():
    op, _ = ORIGINAL_COMPILED()
    pair = {}
    for label in ('N', 'M'):
        syms, safe, _, _, index, alternative = denominator_identity(op, label)
        def cse_factored(exps, _index=index, _alternative=alternative):
            replacements, reduced = sp.cse(exps)
            replacements[_index] = (replacements[_index][0], _alternative)
            return replacements, reduced
        fn = sp.lambdify(syms, safe,
                         modules=[{'interval_halfpow': lambda x,p: x.sqrt()**int(p),
                                   'sqrt': lambda x: x.sqrt(), 'Abs': abs}, 'math'],
                         cse=cse_factored)
        def unwrap(*args, _fn=fn):
            out = _fn(*args)
            return out[0] if isinstance(out, list) and len(out) == 1 else out
        pair[label] = (syms, unwrap)
    return op, pair


def run(repo: Path):
    """Return exact rational interval report, fail closed on source drift."""
    repo = Path(repo).resolve()
    reports = load_pinned(repo / 'research' / 'reports')
    with patch.object(annulus, '_compiled', factored_compiled):
        result = run_original_replay(repo)
        if len(result['cells']) != 7:
            raise AssertionError('Expected exactly seven continuous cells')
        edges = [F(result['cells'][0]['r'][0])]
        edges += [F(row['r'][1]) for row in result['cells']]
        if edges[0] != F(1,64) or edges[-1] != F(1,32) or len(edges) != 8:
            raise AssertionError('Unexpected radial edge coverage')
        pointwise = []
        for r in edges:
            si = I.hull(r,r)**2
            box = box_for_rounded_s(reports, si, {'r':[str(r),str(r)]}, Q, validate_reports)
            with inject_s_jet(annulus, box, Jet, I, si):
                coefficients = annulus.evaluate_cell(r,r)
            pointwise.append({'r':str(r), 'temporal': {
                name: {'enclosure':[str(F(v.lo,10**28)),str(F(v.hi,10**28))],
                       'sign':'POSITIVE_CERTIFIED' if v.lo>0 else
                              'NEGATIVE_CERTIFIED' if v.hi<0 else 'INCOMPLETE'}
                for name,v in coefficients.items()}})
    from .hr_step60_full_constraint_prolongation import manifest
    quotient = manifest()  # The genuine original symbolic Step60; not a seven-cell quotient.
    if quotient['GATE_2B']!='OPEN' or quotient['JANUS_R']!='NOT_VALIDATED':
        raise AssertionError('Original Step60 status drift')
    return {
        'step':'68ad-C2d2b-authentic-temporal-execution',
        'method':'Original Step58 operator/Step68o canonical jets with exactly proven on-shell CSE denominator factorization',
        'original_source_git_blobs':result['provenance'],
        'original_input_report_git_blobs':result['input_report_blobs'],
        'CSE_denominator_rewrite':'beta1*Sg**2+2*beta2*Sg*Sf+beta3*Sf**2 = Sg**2*(beta1+2*beta2*(Lf/Lg)+beta3*(Lf/Lg)**2) on Sg=r*Lg, Sf=r*Lf, Lg>0',
        'seven_cell_continuum':result['cells'],
        'continuum_sign_audit':result['temporal_sign_pattern_audit'],
        'pointwise_eight_edges':pointwise,
        'Step60_original_symbolic_manifest':quotient,
        'Step60_seven_cell_lower_jet_quotient':'NOT_EVALUATED',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
        'limitations':'All 14 seven-cell interval enclosures cross zero; eight pointwise signs are not a continuum certificate. Step60 symbolic third-jet cancellation is not a seven-cell quotient or lapse-rank proof.'
    }


def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path,default=Path.cwd())
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    result=run(a.repo)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    signs=result['continuum_sign_audit']
    print(json.dumps({'cells':len(result['seven_cell_continuum']),
                      'pointwise':len(result['pointwise_eight_edges']),
                      'incomplete':len(signs['incomplete_coefficients']),
                      'Step60_symbolic':'EXECUTED',
                      'Step60_seven_cell':'NOT_EVALUATED',
                      'out':str(a.out)}))

if __name__=='__main__': main()
