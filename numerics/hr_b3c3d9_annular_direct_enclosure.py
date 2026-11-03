"""Attempt direct outward Step55/Step58 lapse-coefficient enclosures on an annulus.

This module is an executable research candidate, NOT a precomputed physical
certificate. A positive result is conditional on authentic Step55 source,
its invariant barrier, the prescribed Step55 chart and the Step58 shell.
Any inconclusive interval is explicitly retained; no point interpolation.
"""
from fractions import Fraction as F
import json

R0, R1 = F(1, 4), F(17, 20)


def uniform_r_cells(count, left=R0, right=R1):
    if not isinstance(count, int) or not 1 <= count <= 8192:
        raise ValueError('invalid cell count')
    left, right = F(left), F(right)
    if not 0 < left < right:
        raise ValueError('requires a positive nonempty annulus')
    step = (right - left) / count
    return [(left + i * step, left + (i + 1) * step)
            for i in range(count)]


def certify_cover(rows, left=R0, right=R1):
    """Strict signs AND gapless exact rational coverage are both necessary."""
    if not rows:
        return False
    at = F(left)
    for row in rows:
        lo, hi = map(F, row['r'])
        if lo != at or lo >= hi or row.get('status') != 'CERTIFIED':
            return False
        an_lo, an_hi = map(F, row['A_N'])
        am_lo, am_hi = map(F, row['A_M'])
        if an_lo > an_hi or am_lo > am_hi:
            return False
        if an_lo <= 0 or am_hi >= 0:
            return False
        at = hi
    return at == F(right)


def classify(a_n, a_m):
    """Never confuse an inconclusive interval with a physical zero."""
    if a_n.lo > a_n.hi or a_m.lo > a_m.hi:
        return 'INCONCLUSIVE'
    if a_n.lo > 0 and a_m.hi < 0:
        return 'CERTIFIED'
    return 'INCONCLUSIVE'


def ode_jets(s, u, g, gs, gu):
    """On 2s U_s=G-2U, return U_s,U_ss with first partials only."""
    us = (g-2*u)/(2*s)
    uss = (gs+(gu-4)*us)/(2*s)
    return us, uss


def _pair(value, scale):
    return [str(F(value.lo, scale)), str(F(value.hi, scale))]


def _lift(source, source_scale, dest):
    return dest.hull(F(source.lo, source_scale), F(source.hi, source_scale))


def run_physical(count=256, max_cells=None):
    """Run original physical operators; never manufacture an all-pass report.

    The finite Step55 barrier is re-executed first. A failed or overly wide
    Step58 interval is an INCONCLUSIVE cell, not evidence of a physical zero.
    `max_cells` permits a bounded smoke attempt but never certifies the whole
    annulus unless every exact cell was actually checked.
    """
    from . import hr_step55_global_barrier as b
    from .hr_b3c3d6_monotone_physical_four_radii import authenticate_originals
    from .hr_b3c3d7_step58_reduced_jet_order_audit import verify_sources
    from .hr_b3c3d6_composed_dual_interval_jets import evaluate_composed
    from .hr_b3c3d6_boundary_ANAM_interval_certificate import (
        I, Jet, physical_jet, MG, MF, M2, B0, B1, B2, B3, B4, Z1)
    from .hr_step45_exact_physical_ward import exact_physical_ward
    from .hr_step58_temporal_operator import physical_operator
    import sympy as sp

    sources = {**authenticate_originals(), **verify_sources()}
    barrier = b.certify_global_barrier(cells=256)
    if barrier['cells'] != 256 or not barrier['Step54_tube_hypothesis_proved_for_exact_radial_solution']:
        raise ArithmeticError('original Step55 global invariant barrier did not pass')
    syms_g, fn_g = b.compiled()
    p, op = exact_physical_ward(), physical_operator()
    functions = {}
    for label in ('N', 'M'):
        expression = op['operator'][label][0]
        syms = tuple(sorted(expression.free_symbols, key=str))
        functions[label] = (syms, sp.lambdify(
            syms, expression, modules=[{'sqrt': lambda x: x.sqrt(), 'Abs': abs}, 'math'], cse=True))

    all_cells = uniform_r_cells(count)
    limit = count if max_cells is None else max_cells
    if not isinstance(limit, int) or not 0 <= limit <= count:
        raise ValueError('invalid execution budget')
    rows = []
    for lo, hi in all_cells[:limit]:
        row = {'r': [str(lo), str(hi)], 's': [str(lo*lo), str(hi*hi)]}
        try:
            sb = b.I.hull(lo*lo, hi*hi)
            rb = I.hull(lo, hi)
            star = b.stars(sb)[0]
            delta = b.I.c(F(1, 10000))
            ub = b.I(star.lo-delta.hi, star.hi+delta.hi)
            gb = b.G(sb, ub)
            gs = evaluate_composed(syms_g, fn_g, b.geometry, b.I,
                                   sb, ub, True, False)
            gu = evaluate_composed(syms_g, fn_g, b.geometry, b.I,
                                   sb, ub, False, True)
            if gs.v.hi < gb.lo or gb.hi < gs.v.lo or gu.v.hi < gb.lo or gb.hi < gu.v.lo:
                raise ArithmeticError('inconsistent original G value/AD boxes')
            s, u, g = I.hull(lo*lo, hi*hi), _lift(ub,b.S,I), _lift(gb,b.S,I)
            gs_i, gu_i = _lift(gs.d,b.S,I), _lift(gu.d,b.S,I)
            us, uss = ode_jets(s,u,g,gs_i,gu_i)
            # Original physical_jet computes a Taylor jet at each r in rb.
            # Its interval h=(r²-r0²) overestimates zero, but encloses it;
            # the overestimation can require subdivision, never gives false PASS.
            fields, clocks = physical_jet(rb, Jet.c(u), Jet.c(us), Jet.c(uss))
            sub = {}
            for name, var in zip(p['Q'], p['q']):
                sub[var] = fields[name].val(0)
            for n, vector in ((1,op['qp']), (2,op['qpp']), (3,op['qppp'])):
                for name, var in zip(p['Q'], vector):
                    sub[var] = clocks[name].val(n-1) if name in clocks else fields[name].val(n)
            sub.update({op['z']:Z1*rb,op['zr']:Z1,op['zrr']:I.c(0),op['zrrr']:I.c(0)})
            sub.update(zip(p['parameters'][:8], (MG,MF,M2,B0,B1,B2,B3,B4)))
            vals = {}
            for label, (symbols, func) in functions.items():
                vals[label] = func(*[sub[sym] for sym in symbols])
                if not isinstance(vals[label], I):
                    raise TypeError('Step58 expression lost interval type')
            row.update({'A_N':_pair(vals['N'],I.c(1).lo),
                        'A_M':_pair(vals['M'],I.c(1).lo),
                        'G':_pair(gb,b.S),'G_s':_pair(gs.d,b.S),
                        'G_U':_pair(gu.d,b.S),
                        'U_s':_pair(us,I.c(1).lo),'U_ss':_pair(uss,I.c(1).lo),
                        'status':classify(vals['N'],vals['M'])})
        except (ArithmeticError, ValueError, ZeroDivisionError, TypeError, KeyError, OverflowError) as exc:
            row.update({'status':'INCONCLUSIVE','blocker':type(exc).__name__+': '+str(exc)[:300]})
        rows.append(row)
    full = len(rows)==len(all_cells)
    return {'stage':'b3c3d9_DIRECT_PHYSICAL_INTERVAL_ATTEMPT',
            'source_blobs':sources, 'original_step55_barrier_cells_executed':256,
            'target_r':[str(R0),str(R1)], 'target_s':[str(R0*R0),str(R1*R1)],
            'requested_cells':count,'executed_cells':len(rows),
            'certified_cells':sum(x['status']=='CERTIFIED' for x in rows),
            'all_annular_signs_certified':full and certify_cover(rows),
            'rows':rows,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
            'limits':'Only Step58 A_N,A_M on the prescribed Step55 shell. Even all cells passing would NOT certify center, two-lapse boundary-value problem, Dirac rank, 4D, stability or observables.'}


def main():
    import argparse
    p=argparse.ArgumentParser()
    p.add_argument('--cells',type=int,default=256)
    p.add_argument('--max-cells',type=int)
    p.add_argument('--out')
    args=p.parse_args()
    result=run_physical(args.cells,args.max_cells)
    out=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.out:
        from pathlib import Path
        Path(args.out).write_text(out,encoding='utf-8')
    else:
        print(out,end='')

if __name__=='__main__':
    main()
