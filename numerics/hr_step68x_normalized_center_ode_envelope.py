"""Exact radius-dependent U, U_s tubes derived from SHA-pinned Step68v proof.

This is a new conditional corollary of the original Step49 analytic-center
recurrence + Step68v interval barrier and G_U enclosure; it does NOT compute
Step58 temporal A_N,A_M at r=0 or certify lapse rank.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
import sys

EXPECTED_BLOB = 'd83a3b80862a2e990a4c4879ec8745a4e91c8b34'
KAPPA = F(1, 10_000_000)
MAX_S = F(1, 64)
OLD_CONSTANT_TUBE = F(1, 1_000_000)


def git_blob(raw: bytes) -> str:
    return sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()


def coefficient(root: str | Path) -> F:
    root = Path(root)
    raw = (root / 'gate2b-step68v-global-monotone-radial-U.json').read_bytes()
    if git_blob(raw) != EXPECTED_BLOB:
        raise ValueError('Original Step68v certificate SHA drift')
    data = json.loads(raw)
    if (data.get('step') != '68v' or data.get('center_s_range') != ['0','1/64']
        or data.get('center_cubic_barrier_kappa') != str(KAPPA)
        or data.get('GATE_2B') != 'OPEN'
        or data.get('JANUS_R') != 'NOT_VALIDATED'
        or data.get('U_s_strict_positive_inner') is not True):
        raise ValueError('Step68v certificate scope or status mismatch')
    f0lo, f0hi = (F(x) for x in data['F0_third_over6'])
    gulo, guhi = (F(x) for x in data['G_U_center_interval'])
    if f0lo > f0hi or gulo > guhi:
        raise ValueError('Invalid original interval ordering')
    residual_abs = max(abs(f0lo),abs(f0hi))
    derivative_lipschitz = max(abs(gulo),abs(guhi))
    return (residual_abs + (derivative_lipschitz+2)*KAPPA)/2


def tube_at_s(s: F, C: F) -> dict:
    s = F(s)
    if s < 0 or s > MAX_S:
        raise ValueError('Outside proven central radius')
    du = KAPPA*s**3
    dus = C*s**2
    if du>OLD_CONSTANT_TUBE:
        raise AssertionError('New cubic tube unexpectedly wider than old uniform tube')
    return {'s': str(s), 'U_minus_Ustar_absolute': str(du),
            'U_s_minus_Ustar_s_absolute': str(dus),
            'spatial_shrink_factor_vs_1e_minus_6':str(OLD_CONSTANT_TUBE/du) if du else 'INFINITE_AT_CENTER'}


def manifest(root: str | Path) -> dict:
    C = coefficient(root)
    # The 1/s in ODE is cancelled analytically BEFORE evaluating at the center.
    # For s>0: 2s (U_s-Ustar_s) = F0(s)+G(s,U)-G(s,Ustar)-2(U-Ustar).
    # F0(0)=F0'(0)=F0''(0)=0 EXACT by original center recurrence;
    # hence |F0| <= R0*s^3; |U-Ustar| <= KAPPA*s^3.
    # |G(s,U)-G(s,Ustar)| <= LG*KAPPA*s^3.
    # Therefore |U_s-Ustar_s| <= C*s^2, valid at s=0 by continuity.
    x = {
      'step':'68x','source_git_blob_sha':EXPECTED_BLOB,
      'derivation':'Full original ODE, exact central recurrence and SHA-pinned interval F0third/G_U bounds imply |U_s-Ustar_s|<=C*s^2 for all 0<=s<=1/64',
      'C_exact':str(C), 'kappa_exact':str(KAPPA),
      'domain_s':['0','1/64'], 'domain_r':['0','1/8'],
      'at_r_1_over_32':tube_at_s(F(1,1024),C),
      'at_r_1_over_8':tube_at_s(F(1,64),C),
      'at_center':tube_at_s(F(0),C),
      'temporal_A_N_A_M_signs_for_r_lt_1_over_32':'NOT_COMPUTED',
      'full_Dirac_rank':'NOT_COMPUTED',
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }
    assert F(x['at_r_1_over_32']['U_minus_Ustar_absolute']) == F(1,10737418240000000)
    return x


def main() -> int:
    if len(sys.argv)!=2:
        print('usage: python -m numerics.hr_step68x_normalized_center_ode_envelope /path/to/research/reports', file=sys.stderr)
        return 2
    print(json.dumps(manifest(sys.argv[1]),indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
