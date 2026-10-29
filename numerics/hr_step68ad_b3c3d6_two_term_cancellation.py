"""Exact conditional exclusion of a restricted Step57 two-term cancellation ansatz.

This is NOT the full eta'' coefficient (the Step57 N term remains), nor
Step58 outer probe, nor a Dirac constraint or physical no-go theorem.
"""
from fractions import Fraction
import json
import sympy as sp

STEP55_BLOB = 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'
STEP57_BLOB = 'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f'
STEP58_BLOB = '802c23aebd41780d8c462f1aa1711707fe4ee88f'
R=sp.Rational(17,20)
S=R**2
cg=sp.Rational(15,10000)
cf=-sp.Rational(12,10000)
A=sp.Rational(2,5)
Y=sp.Rational('0.5787707228025044')
B=A*Y
m2=sp.Rational('23.3348939346')
b2=sp.Rational('-4.2383993109')
b3=sp.Rational('13.6801214252')

def exact_terms():
    r=sp.symbols('r', positive=True)
    s=r*r
    Lg=A*(1+cg*s)**2
    Lf=B*(1+cf*s)**2
    T=(A*(1+cg*s)**2)**2+2*b2*Lg*Lf+b3*Lf**2
    z=r/250
    K=m2*Lg*Lf*T*r*r
    cM=-K*sp.sqrt(1-z*z)/(Lg*Lf**2)
    cNp=-2*r*(1+5*cg*s)/(1+cg*s)*(1-z*z)
    q=m2*r*T*(1+cg*s)/(2*Lf*(1+5*cg*s)*sp.sqrt(1-z*z))
    return r,cM,cNp,q,T

def certificate():
    r,cM,cNp,q,T=exact_terms()
    checks={
      'ratio_identity':sp.simplify(cM-q*cNp),
      'center_odd_ratio':sp.simplify(sp.limit(q/r,r,0)-m2*T.subs(r,0)/(2*B)),
      'cNp_center':sp.simplify(sp.limit(cNp/r,r,0)+2),
      'cM_center':sp.simplify(sp.limit(cM/r**2,r,0)+m2*T.subs(r,0)/B),
      'R2':sp.simplify(S-sp.Rational(289,400)),
      'cancel_for_M1_Nprime_minus_q':sp.simplify(cM-cNp*q),
    }
    assert all(v==0 for v in checks.values()),checks
    # The first inequality is the previously authenticated Step55/Step57
    # uniform cM<-10*r^2 certificate, NOT independently re-proved here.
    upper_Nprime=2*(1+4*cg*S)
    assert 0<cg and cf<0 and 0<S<1
    assert upper_Nprime < sp.Rational(201,100)
    assert sp.simplify(2*(1+5*cg*S)/(1+cg*S)-upper_Nprime)<0
    assert sp.Rational(1000,201)*S/2 == sp.Rational(1445,804)
    upper_rho=sp.Rational(804,2249)
    assert upper_rho == 1/(1+sp.Rational(1445,804))
    assert upper_rho < sp.Rational(1037,2000)
    assert sp.limit(q/r,r,0)>0
    # Positive T(r^2) on [0,R] is an input from earlier Bernstein cert.
    return {
      'step':'b3c3d6_PARTIAL',
      'scope':'RESTRICTED_TWO_TERM_STEP57_ETA2_CANCELLATION_WITH_M_CONSTANT_NOT_FULL_ETA2_NOT_STEP58',
      'original_source_blobs':{'Step55':STEP55_BLOB,'Step57':STEP57_BLOB,'Step58_reference':STEP58_BLOB},
      'assumptions':['Step55 prescribed positive K chart','prior exact cM<-10*r^2','Step57 cNp formula',
                     'M(r)=1','N(R)=M(R)=1','cM*M+cNp*Nprime=0 for 0<r<=R'],
      'construction':'N(r)=1+integral_r^R q(t)dt, q=cM/cNp>1000*r/201; M(r)=1',
      'N0_strict_lower':str(1+sp.Rational(1445,804)),
      'central_M0_over_N0_strict_upper':str(upper_rho),
      'prior_conditional_Step58_center_ratio_strict_lower':'1037/2000',
      'compatibility_with_prior_Step58_center_ratio':'EXCLUDED_ONLY_WITHIN_THIS_RESTRICTED_ANSATZ',
      'symbolic_zero_residuals':len(checks),'rational_guard_asserts':7,
      'original_step58_outer_probe_executed':False,
      'full_eta2_N_coefficient_included':False,
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
