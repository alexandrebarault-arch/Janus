"""Exact Step57 eta'' N' Lf-factor erratum on prescribed Step55 geometry.

The original Step57 code has -2*Mg2*Sg*Sg'*K**2/(Lg**2*Lf*Rshift**2).
Earlier b3c3d6 transcriptions dropped 1/Lf. This module checks the
corrected two-term cancellation ONLY, not the full eta'' symbol, Step58 BVP,
or physical Dirac rank. No original engines are executed here.
"""
from fractions import Fraction
import json
import sympy as sp

S55='a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
S57='bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f'
S58='802c23aebd41780d8c462f1aa1711707fe4ee88f'
R=sp.Rational(17,20)
S=R*R

def symbols():
    r=sp.symbols('r',positive=True)
    s=r*r
    A=sp.Rational(2,5)
    B=A*sp.Rational('0.5787707228025044')
    cg=sp.Rational('0.0015')
    cf=sp.Rational('-0.0012')
    m2=sp.Rational('23.3348939346')
    b2=sp.Rational('-4.2383993109')
    b3=sp.Rational('13.6801214252')
    Lg=A*(1+cg*s)**2
    Lf=B*(1+cf*s)**2
    T=Lg**2+2*b2*Lg*Lf+b3*Lf**2
    z=r/250
    K=m2*Lg*Lf*T*r*r
    Sg=r*Lg
    Sgr=sp.diff(Sg,r)
    cM=-K*sp.sqrt(1-z*z)/(Lg*Lf**2)
    cNp=-2*Sg*Sgr*(1-z*z)/(Lg**2*Lf) # Original Step57: Lf IN denominator.
    old_cNp=-2*Sg*Sgr*(1-z*z)/Lg**2 # ERRONEOUS earlier b3c3d6.
    q=m2*r*T*(1+cg*s)/(2*(1+5*cg*s)*sp.sqrt(1-z*z))
    old_q=q/Lf
    return locals()

def bernstein_coeffs(poly, var, radius2, n=4):
    p=sp.Poly(poly,var)
    assert p.degree()<=n
    a=[p.nth(j) for j in range(n+1)]
    return [sp.factor(sum(a[j]*radius2**j*sp.binomial(k,j)/sp.binomial(n,j)
                          for j in range(k+1))) for k in range(n+1)]

def certificate():
    d=symbols()
    r=d['r']; s=r*r
    cM,cNp,old_cNp,q,old_q,Lf,T=d['cM'],d['cNp'],d['old_cNp'],d['q'],d['old_q'],d['Lf'],d['T']
    mg=sp.S.One
    Lg,Sg,Sgr,z,K=d['Lg'],d['Sg'],d['Sgr'],d['z'],d['K']
    original_shift_R=K/sp.sqrt(1-z*z)
    identities={
      'original_Step57_Nprime_factor':cNp+2*mg*Sg*Sgr*K**2/(Lg**2*Lf*original_shift_R**2),
      'original_Step57_M_factor':cM+K**2/(Lg*Lf**2*original_shift_R),
      'correct_ratio':cM-cNp*q,
      'old_ratio_is_correct_ratio_over_Lf':old_q*Lf-q,
      'old_coefficient_is_correct_coefficient_times_Lf':old_cNp-cNp*Lf,
      'correct_Nprime_center':sp.limit(cNp/r,r,0)+2/d['B'],
      'old_Nprime_center':sp.limit(old_cNp/r,r,0)+2,
      'correct_ratio_center':sp.limit(q/r,r,0)-d['m2']*T.subs(r,0)/2,
      'old_ratio_center':sp.limit(old_q/r,r,0)-d['m2']*T.subs(r,0)/(2*d['B']),
      'T_polynomial_even':sp.factor(T.subs(r,-r)-T),
    }
    bad={k:str(sp.simplify(v)) for k,v in identities.items() if sp.simplify(v)!=0}
    assert not bad,bad
    x=sp.Symbol('x')
    Tx=sp.expand(T.subs(r,sp.sqrt(x)))
    bs=bernstein_coeffs(Tx,x,S)
    assert len(bs)==5
    assert all(sp.Rational(53,500)<v<sp.Rational(109,1000) for v in bs),bs
    assert all(bs[i]>bs[i+1] for i in range(4))
    assert d['B']<1 and d['B']>0
    assert d['m2']<24
    assert (1-R**2/sp.Integer(62500))>sp.Rational(99999,100000)**2
    q_slope_upper=24*sp.Rational(109,1000)/(2*sp.Rational(99999,100000))
    integral_upper=q_slope_upper*S/2
    assert integral_upper<sp.Rational(1,2)
    rho_lower=1/(1+integral_upper)
    assert rho_lower>sp.Rational(2,3)>sp.Rational(2593,5000)
    q_slope_center=sp.limit(q/r,r,0)
    assert q_slope_center<2<sp.Rational(1000,201)
    assert sp.limit(cNp/r,r,0)<-8
    assert sp.limit(old_cNp/r,r,0)==-2
    # This proves corrected q(r)<q_slope_upper*r for all 0<r<=R,
    # using Bernstein T upper, cg>0 and sqrt lower.
    assert d['cg']>0 and d['cf']<0 and d['m2']>0
    assert all(v>0 for v in bs)
    return {
      'step':'b3c3d6_PARTIAL_CORRECTIVE_ERRATUM',
      'scope':'ORIGINAL_STEP57_ETA2_NPRIME_LF_FACTOR_CORRECTION_TWO_TERM_ONLY_NOT_FULL_ETA2_NOT_STEP58_NOT_DIRAC',
      'original_source_blobs':{'Step55':S55,'Step57':S57,'Step58_context':S58},
      'correct_eta2_Nprime':'-2*Mg2*Sg*Sgprime*(1-z^2)/(Lg^2*Lf)',
      'previous_eta2_Nprime':'-2*Mg2*Sg*Sgprime*(1-z^2)/Lg^2',
      'correct_eta2_M':'-K*sqrt(1-z^2)/(Lg*Lf^2)',
      'correct_ratio_q':'m2*r*T*(1+cg*r^2)/(2*(1+5cg*r^2)*sqrt(1-r^2/62500))',
      'previous_q':'correct_q/Lf',
      'correct_center_eta2_Nprime_over_r':str(sp.factor(sp.limit(cNp/r,r,0))),
      'correct_center_q_over_r':str(q_slope_center),
      'Bernstein_T_coefficients':[str(v) for v in bs],
      'T_bound':'53/500 < T(r^2) < 109/1000 on [0,17/20]',
      'two_term_M1_NR1_center_ratio_lower':str(rho_lower),
      'two_term_M1_NR1_center_ratio_conclusion':'M(0)/N(0) > 2/3 > 2593/5000; incompatible with conditional Step58 central ratio, opposite direction to prior erroneous bound',
      'previous_claim_q_gt_1000r_over_201':'FALSE: corrected q/r at center < 2',
      'exact_zero_residuals':len(identities),'rational_inequality_guards':15,
      'original_engine_reexecuted':False,'original_step58_outer_probe_executed':False,
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    print(json.dumps(certificate(),ensure_ascii=False,indent=2))
