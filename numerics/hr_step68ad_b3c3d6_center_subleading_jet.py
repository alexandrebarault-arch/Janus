"""b3c3d6: conditional central r^4 compatibility of full lapse operator.

FORMAL lemma only: coefficients are symbolic Taylor jets, NOT evaluated Step58.
The E_N N'' + E_M M'' terms must be kept until the genuine primary
shell is imposed; B_i=O(r^4) contributes only at O(r^5) for even lapses.
"""
import json
import sympy as s


def certificate():
    r=s.symbols('r', real=True)
    a,c,b,d,u,v,e,f,n0,m0,n2,m2=s.symbols('a c b d u v e f n0 m0 n2 m2')
    N=n0+n2*r**2
    M=m0+m2*r**2
    AN=a*r**2+b*r**4
    AM=c*r**2+d*r**4
    BN=u*r**4
    BM=v*r**4
    EN=e*r**4
    EM=f*r**4
    op=s.expand(AN*N+AM*M+BN*s.diff(N,r)+BM*s.diff(M,r)
                +EN*s.diff(N,r,2)+EM*s.diff(M,r,2))
    lead=a*n0+c*m0
    sub=(a+2*e)*n2+(c+2*f)*m2+b*n0+d*m0
    odd=2*(u*n2+v*m2)
    checks={
        'r0':op.coeff(r,0),'r1':op.coeff(r,1),
        'r2':op.coeff(r,2)-lead,'r3':op.coeff(r,3),
        'r4':op.coeff(r,4)-sub,'r5':op.coeff(r,5)-odd,
        'r6':op.coeff(r,6)-b*n2-d*m2,
        'exact_polynomial':op-(lead*r**2+sub*r**4+odd*r**5+(b*n2+d*m2)*r**6),
    }
    # The r^6 residual is zero after the correct coefficient is subtracted.
    checks['r6']=op.coeff(r,6)-(b*n2+d*m2)
    for key,val in checks.items():
        if s.simplify(val)!=0:raise AssertionError((key,val))
    # Three exact positive-even lapse witnesses with identical a,c and N0/M0.
    models={
      'flat':(2*r**2,-4*r**2,s.Integer(0),s.Rational(1,2)),
      'subleading_A':(2*r**2+3*r**4,-4*r**2,s.Integer(0),s.Rational(1,2)+s.Rational(3,4)*r**2),
      'subleading_E':(2*r**2+3*r**4,-4*r**2,r**4,s.Rational(1,2)+s.Rational(3,2)*r**2),
    }
    for name,(an,am,em,mm) in models.items():
        residual=s.expand(an+am*mm+em*s.diff(mm,r,2))
        if residual!=0:raise AssertionError((name,residual))
        if not (mm.subs(r,0)>0 and s.expand(mm).coeff(r,2)>=0):
            raise AssertionError('positivity witness invalid')
    return {'stage':'b3c3d6_PARTIAL','scope':'FORMAL_CENTER_SUBLEADING_LAPSE_JET_NOT_STEP58_EVALUATION',
      'central_r2':'a*N0+c*M0=0',
      'central_r4':'(a+2e)*N2+(c+2f)*M2+b*N0+d*M0=0',
      'assumptions':'A_N=a*r^2+b*r^4+o(r^4); A_M=c*r^2+d*r^4+o(r^4); B_N,B_M=O(r^4); E_N=e*r^4+o(r^4); E_M=f*r^4+o(r^4); N,M even C^2',
      'on_exact_primary_shell':'If E_N=E_M identically 0, set e=f=0; mere O(r^4) does NOT suffice.',
      'odd_r5':'2*(u*N2+v*M2) for B_N=u*r^4, B_M=v*r^4 in polynomial model; NOT universal if A has r^5 terms.',
      'counterexample':'Three exact analytic positive even lapse models have a=2,c=-4,N0=1,M0=1/2, but M2=0,3/4,3/2.',
      'symbolic_zero_residuals':len(checks),'exact_positive_models':len(models),
      'original_step58_replay':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2,ensure_ascii=False))
