"""Exact toy counterexample: small first-jet coefficient does not imply algebraic lapse fixing.
NOT a Step55 background or Step58 evaluation; smooth-flat, nonanalytic center.
"""
import sympy as sp
r,R,eps=sp.symbols('r R eps',positive=True)
E=sp.exp((1/R-1/r)/eps)
N=2-E
M=sp.Integer(1)
A_N=r**2
A_M=-2*r**2
B_N=-eps*r**4
B_M=sp.Integer(0)

def certificate():
    residual=sp.simplify(A_N*N+A_M*M+B_N*sp.diff(N,r)+B_M*sp.diff(M,r))
    assert residual==0
    assert sp.simplify(N.subs(r,R)-M.subs(r,R))==0
    assert sp.limit(N,r,0,dir='+')==2
    assert sp.limit(sp.diff(N,r),r,0,dir='+')==0
    assert sp.simplify(sp.diff(N,r).subs(r,R))==-1/(eps*R**2)
    for k in (1,2,3,4,5):
        assert sp.limit(sp.diff(N,r,k),r,0,dir='+')==0
    # At eps=0 the differential equation becomes r^2(N-2M)=0;
    # positive N(R)=M(R) is impossible for this algebraic equation.
    assert sp.simplify((A_N*N+A_M*M).subs(r,R))==-R**2
    assert sp.simplify((-B_N*sp.diff(N,r)).subs(r,R))==-R**2
    assert sp.simplify((sp.Abs(B_N)*(-sp.diff(N,r))).subs(r,R))==R**2
    return {'residual':residual,'center_N':2,'terminal_N':1,
            'terminal_derivative':-1/(eps*R**2),
            'max_abs_BN':eps*R**4,
            'center_regular_Cinfty':True,'center_analytic':False,
            'scope':'EXACT_TOY_COUNTEREXAMPLE_NOT_STEP55_NOT_DIRAC'}

if __name__=='__main__':
    print(certificate())
