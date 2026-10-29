"""Exact cubic/quartic endpoint invariance for Step58's jet order.

This is a formal source-structure lemma, NOT an original Step58 replay or
physical coefficient calculation. Source blob 802c23a... was inspected via
GitHub: returned physical_operator uses canonical jets through q''' only.
"""
import sympy as sp


def certificate():
    r,r0,u0,u1,u2,u3,u4=sp.symbols('r r0 u0 u1 u2 u3 u4',positive=True)
    s,U,e=sp.symbols('s U e')
    d=r*r-r0*r0
    uc=u0+u1*d+u2*d*d/2+u3*d**3/6
    uq=uc+u4*d**4/24
    assert sp.expand(uq-uc-u4*d**4/24)==0
    g=1+2*s+3*U+4*s*U+5*U**2+6*s*s*U**3
    F=2+3*s+5*U+7*s*U+11*U**2+13*s*s*U**2+17*U**3
    forms={
      'U':U,
      'pLf':r*r*U,
      'pLfr':r*g.subs(s,r*r),
      'nonlinear_field':F.subs(s,r*r),
      'rational_field':(1+r*r*U)/(2+U**2+r*r),
    }
    fourth={}
    for name,expr in forms.items():
        # Exact divided difference: F(U+e)-F(U)=e*Q(U,e).
        # Regularity of Q at e=0 proves O((r-r0)^4) without
        # differentiating huge quartic rational compositions.
        numerator=sp.together(expr.subs(U,U+e)-expr)
        quotient=sp.cancel(numerator/e)
        at_e0=sp.cancel(quotient.subs(e,0))
        assert sp.cancel(at_e0-sp.diff(expr,U))==0,name
        # First nonzero difference in fourth radial derivative is exact.
        jump=sp.factor(16*r0**4*u4*sp.diff(expr,U).subs({r:r0,U:u0}))
        assert jump!=0,name
        fourth[name]=jump
    # Independently differentiate the simple U and pLf differences.
    assert sp.factor(sp.diff(uq-uc,r,4).subs(r,r0)-fourth['U'])==0
    assert sp.factor(sp.diff(r*r*(uq-uc),r,4).subs(r,r0)-fourth['pLf'])==0
    return {'through_order':3,'forms':tuple(forms),'fourth_order_differences':fourth,
            'divided_differences_verified':len(forms),
            'original_step58_executed':False,
            'step58_original_blob':'802c23aebd41780d8c462f1aa1711707fe4ee88f'}


def source_order_contract():
    """Source reading, NOT original executable/AST replay.

    Step58: X(q,q') -> Xr=Dt(X)(q,q',q'') -> deltaZ(q,q',q'')
    -> Dt(deltaZ)(q,q',q'',q'''); direct C(q,q',z,z') is first order.
    """
    return {'max_canonical_jet':3,'max_shift_jet':3,
            'original_source_reexecuted':False,'verified_by':'source reading'}

if __name__=='__main__':
    v=certificate()
    print('PASS five divided differences and two fourth-jet checks')
