"""Step68y: SHA-authenticated exact signed center residual and momentum jets.

Conditional corollary of ORIGINAL Steps49/67b/68u/68v; no rerun of Step58.
Use the third-derivative residual enclosures from 68u and the signed G_U
range from 68v. The original physical ODE is 2*s*U_s=G(s,U)-2*U.
This module proves a ONE-SIDED U envelope on s<=1/1024, then signed
U_s and original f canonical momentum p_Lf=s*U, p'_Lf/r=G(s,U) tubes.
All operations here are EXACT fractions (no floating-point arithmetic).
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
import sys

ORIGINAL = {
    '68u': ('gate2b-step68u-center-cubic-barrier.json',
            'aaacd0064e04cb0f5d596aa3df042a4c9a4c751d'),
    '68v': ('gate2b-step68v-global-monotone-radial-U.json',
            'd83a3b80862a2e990a4c4879ec8745a4e91c8b34'),
}
MAX_S = F(1, 1024)
KAPPA = F(1, 10_000_000)


def blob_sha(raw: bytes) -> str:
    return sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def _interval(values):
    if len(values) != 2:
        raise ValueError('Expected two interval endpoints')
    lo, hi = map(F, values)
    if lo > hi:
        raise ValueError('Unordered original interval')
    return lo, hi


def load_originals(root: str | Path):
    documents = {}
    for step, (filename, expected) in ORIGINAL.items():
        raw = (Path(root) / filename).read_bytes()
        if blob_sha(raw) != expected:
            raise ValueError(f'Original Step{step} certificate SHA drift')
        documents[step] = json.loads(raw)
    u, v = documents['68u'], documents['68v']
    if (u['step'] != '68u' or v['step'] != '68v'
        or u['s_range'] != ['0', '1/1024']
        or v['center_s_range'] != ['0', '1/64']
        or F(u['cubic_width_coeff']) != KAPPA
        or F(v['center_cubic_barrier_kappa']) != KAPPA
        or v['U_s_strict_positive_inner'] is not True
        or any(d['GATE_2B'] != 'OPEN' or d['JANUS_R'] != 'NOT_VALIDATED'
               for d in (u, v))
        or u['original_source_sha'] != v['original_physical_shas']):
        raise ValueError('Original constraints, scope or provenance mismatch')
    ulo, uhi = F(u['U3_lower_from_published_Step67b']), F(u['U3_upper_from_published_Step67b'])
    if not -KAPPA < ulo <= uhi < 0:
        raise ValueError('No strictly negative Step67b Taylor coefficient')
    return u, v


def bounds(root: str | Path):
    u, v = load_originals(root)
    fp_lo, fp_hi = _interval(u['upper_F_third_over_6_interval'])
    fm_lo, fm_hi = _interval(u['lower_F_third_over_6_interval'])
    gu_lo, gu_hi = _interval(v['G_U_center_interval'])
    f0_old_lo, f0_old_hi = _interval(v['F0_third_over6'])
    if not fp_hi < 0 < fm_lo or not gu_lo <= gu_hi < 0:
        raise ValueError('Original signed residual or G_U hypothesis broken')
    # F_plus = F0 + (G_U(xi_plus)-8)*kappa*s**3;
    # F_minus= F0 + (8-G_U(xi_minus))*kappa*s**3.
    # Exact Taylor: each F_{+-}(s)/s**3 is enclosed by its original
    # globally bounded F'''/6, since coefficients of s^0,s^1,s^2 vanish.
    plus = (fp_lo + (8-gu_hi)*KAPPA, fp_hi + (8-gu_lo)*KAPPA)
    minus = (fm_lo - (8-gu_lo)*KAPPA, fm_hi - (8-gu_hi)*KAPPA)
    f0_lo, f0_hi = max(plus[0], minus[0]), min(plus[1], minus[1])
    if not f0_old_lo <= f0_lo <= f0_hi <= f0_old_hi or not f0_hi < 0:
        raise ArithmeticError('Strict signed F0 residual not proved')
    # U3<0 implies U<Ustar for small s>0.  F0<0 at U=Ustar is
    # the strict upper-barrier inequality for the original ODE, hence
    # a no-first-exit argument gives -kappa*s^3<=deltaU<=0.
    # Since gu<0, deltaU<=0 implies G(s,U)-G(s,Ustar)>=0.
    dus_lo, dus_hi = f0_lo/2, (f0_hi + (2-gu_lo)*KAPPA)/2
    gv_lo, gv_hi = f0_lo, f0_hi - gu_lo*KAPPA
    if dus_lo > dus_hi or gv_lo > gv_hi:
        raise AssertionError('Invalid derived interval')
    return {
      'step': '68y',
      'authenticated_original_blobs': {k:sha for k,(_,sha) in ORIGINAL.items()},
      'domain_s': ['0',str(MAX_S)], 'domain_r':['0','1/32'],
      'kappa': str(KAPPA),
      'F0_over_s_cubed_via_plus': list(map(str,plus)),
      'F0_over_s_cubed_via_minus': list(map(str,minus)),
      'F0_over_s_cubed_intersection': [str(f0_lo),str(f0_hi)],
      'F0_strict_negative_for_s_positive': True,
      'U_minus_Ustar_over_s_cubed': [str(-KAPPA),'0'],
      'U_s_minus_Ustar_s_over_s_squared':[str(dus_lo),str(dus_hi)],
      'G_minus_Vstar_over_s_cubed':[str(gv_lo),str(gv_hi)],
      'pLf_minus_s_Ustar_over_s_fourth':[str(-KAPPA),'0'],
      'pLf_prime_over_r_minus_Vstar_over_s_cubed':[str(gv_lo),str(gv_hi)],
      'physical_identification':'Step45/46: pLf=s*U, pLf_prime/r=G(s,U)=2*(U+s*U_s), Vstar=2*Ustar+2*s*Ustar_s',
      'analytic_preconditions':'Step49 actual center solution, Step67b negative U3, Step68u exact Fplus/Fminus third derivative bounds and cubic comparison, Step68v signed G_U enclosure',
      'at_r_1_over_32':at_s(MAX_S, (dus_lo,dus_hi),(gv_lo,gv_hi)),
      'at_r_1_over_64':at_s(F(1,4096), (dus_lo,dus_hi),(gv_lo,gv_hi)),
      'temporal_A_N_A_M_near_center':'NOT_COMPUTED',
      'Dirac_rank':'NOT_COMPUTED',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
    }


def at_s(s: F, dus_coeff, gv_coeff):
    s = F(s)
    if not 0 <= s <= MAX_S:
        raise ValueError('Outside proved Step68y chart')
    r = F(1,32) if s == MAX_S else F(1,64) if s==F(1,4096) else None
    return {
        's':str(s),
        'r': str(r) if r is not None else 'sqrt(s)',
        'U_minus_Ustar':[str(-KAPPA*s**3),'0'],
        'U_s_minus_Ustar_s':[str(x*s**2) for x in dus_coeff],
        'G_minus_Vstar':[str(x*s**3) for x in gv_coeff],
        'pLf_minus_s_Ustar':[str(-KAPPA*s**4),'0'],
        'pLf_prime_over_r_minus_Vstar':[str(x*s**3) for x in gv_coeff],
    }


def main():
    if len(sys.argv) != 2:
        print('usage: python -m numerics.hr_step68y_signed_center_residual RESEARCH_REPORTS',file=sys.stderr)
        return 2
    print(json.dumps(bounds(sys.argv[1]), indent=2, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
