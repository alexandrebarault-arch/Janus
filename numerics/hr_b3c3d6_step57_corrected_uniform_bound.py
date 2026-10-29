"""Exact corrected Step57 eta''*N' sign on prescribed Step55, not Step58/Dirac.
Original source blobs: Step57 bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f;
Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe.
"""
import json
import sympy as sp

s=sp.symbols('s', nonnegative=True)
R2=sp.Rational(289,400)
A=sp.Rational(2,5)
Y=sp.Rational(5787707228025044,10**16)
B=A*Y
cg=sp.Rational(3,2000)
cf=-sp.Rational(3,2500)
ug=1+cg*s
uf=1+cf*s
Lg=A*ug**2
Lf=B*uf**2
Sg_over_r=A*ug
Sgprime=A*ug*(1+5*cg*s)
z2=s/62500
# Original Step57 eta2 N' on Fz=0, K>0: -2 Mg2 Sg Sg' (1-z²)/(Lg² Lf).
correct_over_r=sp.factor(-2*Sg_over_r*Sgprime*(1-z2)/(Lg**2*Lf))
legacy_over_r=sp.factor(correct_over_r*Lf)


def certificate():
    checks={
        'original_formula_reduction':correct_over_r+2*(1+5*cg*s)*(1-z2)/(B*ug**2*uf**2),
        'legacy_omitted_factor':legacy_over_r-Lf*correct_over_r,
        'center_correct':correct_over_r.subs(s,0)+2/B,
        'center_legacy':legacy_over_r.subs(s,0)+2,
        'radius_conversion':R2-sp.Rational(17,20)**2,
    }
    for name,expr in checks.items():
        assert sp.cancel(expr)==0, name
    # Rational monotone-factor enclosure valid for all 0<=s<=R2.
    guards={
        'B_positive':B>0,
        'B_below_7_over_30':B<sp.Rational(7,30),
        'ug_at_R_below_501_over_500':ug.subs(s,R2)<sp.Rational(501,500),
        'uf_at_R_positive':uf.subs(s,R2)>0,
        'cg_positive':cg>0,
        'cf_negative':cf<0,
        'z_factor_at_R_above_9999_over_10000':1-R2/62500>sp.Rational(9999,10000),
        'certified_lower_abs_over_r':sp.Rational(60,7)*sp.Rational(9999,10000)/sp.Rational(501,500)**2>sp.Rational(17,2),
        'legacy_center_does_not_pass_corrected_bound':-legacy_over_r.subs(s,0)<sp.Rational(17,2),
        'corrected_center_passes':-correct_over_r.subs(s,0)>sp.Rational(17,2),
    }
    assert all(guards.values()), [k for k,v in guards.items() if not v]
    return {
      'scope':'STEP57_ETA2_NPRIME_CORRECTED_UNIFORM_SIGN_ONLY',
      'radius':'17/20',
      'certified':'c_Nprime(r) < -(17/2)*r for 0<r<=17/20',
      'center_correct_over_r':str(correct_over_r.subs(s,0)),
      'center_legacy_over_r':str(legacy_over_r.subs(s,0)),
      'bound_lower_abs_over_r':str(sp.Rational(60,7)*sp.Rational(9999,10000)/sp.Rational(501,500)**2),
      'symbolic_zero_residuals':len(checks),
      'rational_guards':len(guards),
      'negative_control':'legacy eta2 Nprime cannot satisfy corrected -17r/2 bound near center',
      'original_step58_probe_executed':False,
      'eta2_N_term_evaluated':False,
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'
    }

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))
