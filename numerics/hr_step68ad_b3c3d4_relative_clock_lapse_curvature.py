"""Exact lapse-extended outer boundary curvature under relative clock preservation.

Restricted Step55 spatial lambda-family, not a Dirac-tangent result.
Source provenance: Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe;
original Step45 66aa43841dccfe4a5d586a49be9c10af3a67a10e;
previous boundary d1 1ba6d012133a92b69a8c91498d065b22649afbe0;
clock evolution b3a f0756adb6b98574700591ae8cb8a1b10bbc60eb9.
"""
import json
import sympy as s

def run():
    Lg,Lf,a,b,T,U,sg,sf=s.symbols('Lg Lf a b T U sg sf',positive=True)
    N,M,z=s.symbols('N M z',real=True)
    q=Lg/Lf
    delta=T+U
    H=Lg*a+Lf*b
    Q=N/Lg+M/Lf
    Vrel=(M*sf-N*sg-z*Q*T)/delta
    F=-z*a*(N+q*M)-H*Vrel
    cN=s.diff(F,N)
    cM=s.diff(F,M)
    checks={
      'Vrel_preserves_relative_clock':s.simplify((N*sg+(z*Q+Vrel)*T)-(M*sf-Vrel*U)),
      'Vrel_N':s.simplify(s.diff(Vrel,N)+(sg+z*T/Lg)/delta),
      'Vrel_M':s.simplify(s.diff(Vrel,M)-(sf-z*T/Lf)/delta),
      'F_linear':s.simplify(F-N*cN-M*cM),
      'cN_formula':s.simplify(cN+z*a-H*(sg+z*T/Lg)/delta),
      'cM_formula':s.simplify(cM+z*q*a+H*(sf-z*T/Lf)/delta),
      'nonzero_combination':s.simplify(cM-q*cN+H*(sf+q*sg)/delta),
      'shift_cancel':s.simplify(s.diff(cM-q*cN,z)),
      'a_cancel':s.simplify(s.diff(cM-q*cN,a)+Lg*(sf+q*sg)/delta),
      'b_cancel':s.simplify(s.diff(cM-q*cN,b)+Lf*(sf+q*sg)/delta),
      'linear_lapse_differential':s.simplify(s.diff(F,N, M)),
      'shift_independent_relative_velocity_gap':s.simplify(s.diff(Vrel,M)-q*s.diff(Vrel,N)-(sf+q*sg)/delta),
      'positive_factor':s.simplify(H*(sf+q*sg)/delta - (Lg*a+Lf*b)*(sf+Lg*sg/Lf)/(T+U)),
    }
    for name,val in checks.items():
        if val!=0: raise AssertionError((name,val))
    # Exact rational endpoint witness, not claimed to be Step55 data.
    witness={Lg:s.Rational(2,5),Lf:s.Rational(3,5),a:s.Rational(3,4),b:s.Rational(1,200),T:s.Rational(3,10),U:s.Rational(1,4),sg:s.Rational(5,4),sf:s.Rational(13,12),z:s.Rational(1,5)}
    wN=s.cancel(cN.subs(witness));wM=s.cancel(cM.subs(witness));wq=q.subs(witness)
    assert s.simplify(wM-wq*wN+H.subs(witness)*(sf+q*sg).subs(witness)/delta.subs(witness))==0
    assert s.simplify(wM-wq*wN)<0
    assert s.simplify(s.Rational(5,4)**2-1-(s.Rational(3,10)/s.Rational(2,5))**2)==0
    assert s.simplify(s.Rational(13,12)**2-1-(s.Rational(1,4)/s.Rational(3,5))**2)==0
    assert s.simplify(wN)!=0 or s.simplify(wM)!=0
    # Negative-control: H=0 destroys strict obstruction, so H>0 is essential.
    assert s.simplify((cM-q*cN).subs({a:0,b:0}))==0
    return {'step':'b3c3d4','symbolic_zero_residuals':len(checks),
      'exact_rational_checks':6,'witness_cN':str(wN),'witness_cM':str(wM),
      'witness_combination':str(s.cancel(wM-wq*wN)),
      'theorem':'c_M-(Lg/Lf)c_N=-(Lg*a+Lf*b)*(sf+(Lg/Lf)*sg)/(T+U)<0',
      'scope':'lapse-extended restricted Step55 spatial lambda family, with V=Vrel, not temporal Dirac tangent',
      'original_python_import_replay':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__': print(json.dumps(run(),indent=2))
