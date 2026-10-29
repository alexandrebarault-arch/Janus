"""Exact rational Step55 *geometric* K>0 chart certificate, NOT Step58/Dirac.

Constants transcribed from GitHub blob a6e7004120d0a166a3a8973c2fbe1487a8eb70fe
(numerics/hr_step55_global_barrier.py). Optional byte verification when the
original source is present. No claim to re-execute original Step55 dynamics.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
import json
from math import comb
import sympy as sp

ORIGINAL_STEP55_BLOB = 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
S_MAX = F(289, 400)
R_MAX = F(17, 20)

def original_blob_check(path: str | Path) -> bool:
    raw = Path(path).read_bytes()
    actual = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if actual != ORIGINAL_STEP55_BLOB:
        raise ValueError(f'Step55 original SHA drift: {actual}')
    return True

def certificate():
    s, t = sp.symbols('s t', real=True)
    rat = sp.Rational
    A, Y = rat('0.4'), rat('0.5787707228025044')
    B = A*Y
    cg, cf = rat('0.0015'), rat('-0.0012')
    b1, b2, b3 = rat(1), rat('-4.2383993109'), rat('13.6801214252')
    m2, mg, z1 = rat('23.3348939346'), rat(1), rat('0.004')
    Lg = A*(1+cg*s)**2
    Lf = B*(1+cf*s)**2
    T = sp.expand(b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2)
    # The Step55 physical K is m2*mg*Lg*Lf*At, At=r^2*T(r^2).
    K_over_r2 = m2*mg*Lg*Lf*T
    z_outer = z1*rat(R_MAX.numerator,R_MAX.denominator)
    scaled = sp.Poly(T.subs(s,rat(S_MAX.numerator,S_MAX.denominator)*t), t)
    degree = scaled.degree()
    bern = [sp.factor(sum(scaled.nth(k)*rat(comb(j,k),comb(degree,k))
                          for k in range(j+1))) for j in range(degree+1)]
    assert degree == 4
    assert all(v > 0 for v in bern)
    # Stronger than mere positivity: T is strictly decreasing in s.
    assert all(bern[j+1]-bern[j] < 0 for j in range(degree))
    assert bern[0] == T.subs(s,0)
    assert bern[-1] == T.subs(s,rat(S_MAX.numerator,S_MAX.denominator))
    T_min = bern[-1]
    assert T_min > rat(53,500)
    assert bern[0] < rat(109,1000)
    Lf_min = Lf.subs(s,rat(S_MAX.numerator,S_MAX.denominator))
    K_lower = sp.factor(m2*mg*A*Lf_min*T_min)
    assert K_lower > rat(9,40)
    assert sp.simplify(K_over_r2 - m2*mg*Lg*Lf*T) == 0
    assert z_outer == rat(17,5000)
    assert 0 < z_outer < 1
    # On the stationary shift shell, D=K*z/sqrt(1-z^2).
    # Thus D/K -> 0 at the center, while K=O(r^2), D=O(r^3).
    r = sp.symbols('r', real=True)
    K_r = (r*r*K_over_r2.subs(s,r*r))
    assert sp.limit(K_r/r**2,r,0) > 0
    D_r = K_r*(z1*r)/sp.sqrt(1-(z1*r)**2)
    assert sp.limit(D_r/r**3,r,0) > 0
    assert sp.limit(D_r/K_r,r,0) == 0
    return {
        'scope':'EXACT_RATIONAL_STEP55_PRESCRIBED_GEOMETRY_ONLY_NOT_STEP58_NOT_DIRAC',
        'step55_original_blob':ORIGINAL_STEP55_BLOB,
        'r_interval':['0','17/20'], 's_interval':['0','289/400'],
        'T_polynomial_degree':degree,
        'T_bernstein_signs':['POS']*len(bern),
        'T_bernstein_adjacent_differences':['NEG']*degree,
        'T_bounds_simple':['53/500','109/1000'],
        'K_over_r2_strict_lower':'9/40',
        'K_outer_positive':bool(K_over_r2.subs(s,rat(S_MAX.numerator,S_MAX.denominator))>0),
        'z_outer':str(z_outer),
        'center_orders':{'K':'r^2 times positive smooth coefficient','D':'r^3 times positive smooth coefficient'},
        'symbolic_assert_statements':14,
        'critical_limit':'Does NOT certify B_N,B_M of Step58, lapse positivity, Dirac or physical boundary data',
        'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))
