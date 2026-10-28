"""Exact regular lapse frame on annuli where B_N**2+B_M**2>0.

Applies to any first-order scalar operator A_N*N+A_M*M+B_N*N'+B_M*M'=0.
Does NOT evaluate original Step55/Step58 radial profile or establish Dirac tangency.
"""
import sympy as s


def certificate():
    r=s.symbols('r', real=True)
    bn,bm,an,am,n,m=[s.Function(k)(r) for k in ('bn','bm','an','am','n','m')]
    delta=bn**2+bm**2
    u=bn*n+bm*m
    v=-bm*n+bn*m
    x=s.diff(bn,r)-an
    y=s.diff(bm,r)-am
    alpha=(x*bn+y*bm)/delta
    beta=(-x*bm+y*bn)/delta
    operator=bn*s.diff(n,r)+bm*s.diff(m,r)+an*n+am*m
    checks={
        'frame_u':s.expand(u-(bn*n+bm*m)),
        'frame_v':s.expand(v-(-bm*n+bn*m)),
        'inverse_n':(bn*u-bm*v)/delta-n,
        'inverse_m':(bm*u+bn*v)/delta-m,
        'operator_equivalence':s.diff(u,r)-alpha*u-beta*v-operator,
        'terminal_difference':((bm-bn)*u+(bn+bm)*v)/delta-(m-n),
        'orthogonality':bn*(-bm)+bm*bn,
        'determinant':s.det(s.Matrix([[bn,bm],[-bm,bn]]))-delta,
    }
    for k,expr in checks.items():
        assert s.simplify(expr)==0,(k,expr)
    return len(checks)


def toy_crossing():
    r=s.symbols('r',real=True)
    bn=s.Integer(1);bm=r-s.Rational(1,2)
    n=m=1+r**2
    an=-s.factor((s.diff(n,r)+bm*s.diff(m,r))/n)
    am=s.Integer(0)
    d=bn**2+bm**2
    u=bn*n+bm*m
    v=-bm*n+bn*m
    x=s.diff(bn,r)-an;y=s.diff(bm,r)-am
    alpha=(x*bn+y*bm)/d
    beta=(-x*bm+y*bn)/d
    residuals={
        'original':an*n+am*m+bn*s.diff(n,r)+bm*s.diff(m,r),
        'frame':s.diff(u,r)-alpha*u-beta*v,
        'terminal':(m-n).subs(r,s.Rational(17,20)),
        'crossing':bm.subs(r,s.Rational(1,2)),
        'crossing_u':u.subs(r,s.Rational(1,2))-s.Rational(5,4),
        'crossing_v':v.subs(r,s.Rational(1,2))-s.Rational(5,4),
    }
    for k,expr in residuals.items():
        assert s.factor(expr)==0,(k,expr)
    assert d.subs(r,s.Rational(1,2))==1
    assert n.subs(r,s.Rational(1,4))>0 and n.subs(r,s.Rational(17,20))>0
    return len(residuals)


def original_witness_frame():
    # Authenticated Step45/Step58 pointwise values from the prior published
    # certificate, NOT an independent replay of those source modules.
    bn=s.Rational(224,125);bm=s.Integer(0)
    an=s.Rational(1293,250);am=-s.Rational(79093,12500)
    d=bn**2+bm**2
    assert d==s.Rational(50176,15625)
    assert s.cancel(an/bn)==s.Rational(1293,448)
    assert s.cancel(am/bn)==-s.Rational(79093,22400)
    return {'B_N':str(bn),'B_M':str(bm),'delta':str(d),
            'A_N_over_B_N':str(s.cancel(an/bn)),
            'A_M_over_B_N':str(s.cancel(am/bn)),
            'unknown':'B_N_prime and B_M_prime, hence alpha and beta at the witness'}


def audit():
    return {'stage':'b3c3d6_PARTIAL','symbolic_residuals':certificate(),
            'toy_residuals':toy_crossing(),'original_pointwise_witness':original_witness_frame(),
            'scope':'ALGEBRAIC_FRAME_THEOREM_AND_TOY_NOT_STEP55_NOT_DIRAC',
            'gate':'OPEN','janus':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(audit(),indent=2))
