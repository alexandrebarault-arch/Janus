"""Step55 exact uniform bounds for the original Step57 eta'' principal symbols.

This evaluates two already-derived Step57 six-pair formulas on prescribed
Step55 geometry, using exact rational data. NOT an original Step58 execution,
not a proof of Dirac rank or of a lapse boundary-value problem.
"""
from __future__ import annotations
from hashlib import sha1
from pathlib import Path
import json
import sympy as sp

STEP55_SHA = 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
STEP57_SHA = 'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f'
STEP58_SHA = '802c23aebd41780d8c462f1aa1711707fe4ee88f'
R = sp.Rational(17, 20)
S = R**2

def verify_original_blob(path: str | Path, expected: str) -> bool:
    raw = Path(path).read_bytes()
    digest = sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if digest != expected:
        raise ValueError(f'Git blob mismatch: {digest} != {expected}')
    return True

def certificate():
    s = sp.symbols('s', real=True, nonnegative=True)
    r = sp.symbols('r', real=True, positive=True)
    rat = sp.Rational
    A, Y = rat(2,5), rat('0.5787707228025044')
    B, cg, cf, z1 = A*Y, rat('0.0015'), rat('-0.0012'), rat(1,250)
    mg, m2 = rat(1), rat('23.3348939346')
    b1,b2,b3 = rat(1),rat('-4.2383993109'),rat('13.6801214252')
    Lg = A*(1+cg*s)**2
    Lf = B*(1+cf*s)**2
    Sg = r*Lg.subs(s,r*r)
    Sgr = sp.diff(Sg,r)
    T = Lg**2+2*b2*Lg*Lf+b3*Lf**2
    K = m2*mg*(Lg*Lf*T).subs(s,r*r)*r*r
    z = z1*r
    # Original Step57 on Fz=0,K>0: Rshift=sqrt(D²+K²)=K/sqrt(1-z²).
    # eta'' coefficients of M and N' in {int eta C_red,H_tot}.
    C_M = -K*sp.sqrt(1-z*z)/(Lg.subs(s,r*r)*Lf.subs(s,r*r)**2)
    C_Np = -2*mg*Sg*Sgr*(1-z*z)/Lg.subs(s,r*r)**2
    assert sp.simplify(C_Np/r+2*mg*(1+5*cg*r*r)/(1+cg*r*r)*(1-z*z))==0
    assert sp.simplify(C_M/r**2 + m2*mg*T.subs(s,r*r)*sp.sqrt(1-z*z)/Lf.subs(s,r*r))==0
    # Source-certified Step55 geometry: K/r² > 9/40 (prior Bernstein proof).
    # The following bounds are all independent rational inequalities.
    Lgmax=Lg.subs(s,S)
    Lfmax=Lf.subs(s,0)
    zmax=z1*R
    sqrtlower=rat(99999,100000)
    assert (1-zmax*zmax)-sqrtlower**2 > 0
    assert Lgmax > 0 and Lfmax > 0
    assert sp.factor(Lgmax-Lg.subs(s,0))>0
    assert sp.factor(Lf.subs(s,0)-Lf.subs(s,S))>0
    lower_M = rat(9,40)*sqrtlower/(Lgmax*Lfmax**2)
    assert lower_M > 10
    lower_Np = 2*(1-zmax*zmax)
    assert lower_Np > rat(19999,10000)
    assert sp.simplify(Sgr.subs(r,sp.sqrt(s))/Lg- (1+5*cg*s)/(1+cg*s))==0
    assert cg>0 and cf<0 and mg>0 and m2>0
    assert zmax==rat(17,5000)
    center_M=sp.factor(sp.limit(C_M/r**2,r,0))
    center_Np=sp.factor(sp.limit(C_Np/r,r,0))
    assert center_M < -10
    assert center_Np == -2
    assert sp.simplify(K/r**2-m2*mg*Lg.subs(s,r*r)*Lf.subs(s,r*r)*T.subs(s,r*r))==0
    return {
      'scope':'STEP55_PRESCRIBED_GEOMETRY_STEP57_SMEARED_ETA2_PRINCIPAL_SYMBOL_NOT_STEP58_OR_DIRAC_RANK',
      'source_blobs':{'Step55':STEP55_SHA,'Step57':STEP57_SHA,'Step58_reference_only':STEP58_SHA},
      'domain':'0<r<=17/20',
      'original_step55_K_over_r2_lower':'9/40 (prior Bernstein certificate)',
      'eta2_M':'-K*sqrt(1-z^2)/(Lg*Lf^2)',
      'eta2_Nprime':'-2*Mg2*Sg*Sgprime*(1-z^2)/Lg^2',
      'eta2_M_strict_bound':'eta2_M < -10*r^2',
      'eta2_Nprime_strict_bound':'eta2_Nprime < -(19999/10000)*r',
      'center_limits':{'eta2_M_over_r2':str(center_M),'eta2_Nprime_over_r':str(center_Np)},
      'rational_lower_bounds':{'abs_eta2_M_over_r2':str(lower_M),'abs_eta2_Nprime_over_r':str(lower_Np)},
      'exact_assert_statements':14,
      'original_step58_outer_probe_executed':False,
      'original_step55_57_executed':False,
      'Dirac_rank_certified':False,
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))
