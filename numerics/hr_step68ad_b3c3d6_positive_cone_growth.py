"""b3c3d6: exact positivity cone and necessary annular growth screen.

First-order shell only: A_N*N+A_M*M+B_N*N'+B_M*M'=0.
No original Step55/58 replay or physical Dirac claim.
"""
from fractions import Fraction as F
import sympy as s


def algebraic_certificate():
    bn,bm,n,m,an,am,bnp,bmp=s.symbols('bn bm n m an am bnp bmp', real=True)
    delta=bn**2+bm**2
    u=bn*n+bm*m
    v=-bm*n+bn*m
    alpha=((bnp-an)*bn+(bmp-am)*bm)/delta
    beta=(-(bnp-an)*bm+(bmp-am)*bn)/delta
    # These are identities for nonzero bn,bm and delta, not sign certificates.
    checks={
        'cone_lower':s.factor(v+bm*u/bn)-(delta*m/bn),
        'cone_upper':s.factor(bn*u/bm-v)-(delta*n/bm),
        'endpoint_equal':s.factor(v/u-(bn-bm)/(bn+bm)).subs(m,n),
        'frame_alpha_beta':s.factor(alpha*u+beta*v-((bnp-an)*n+(bmp-am)*m)),
        'endpoint_amplitude':s.factor((bn+bm)*n-u).subs(m,n),
        'cone_width':s.factor(bn/bm+bm/bn-delta/(bn*bm)),
    }
    for name,value in checks.items():
        assert s.cancel(value)==0,(name,value)
    return len(checks)


def toy_certificate():
    r=s.symbols('r', real=True)
    bn=bm=s.Integer(1)
    an=-s.Integer(1);am=s.Integer(1)
    n=m=s.Integer(1)
    delta=bn**2+bm**2
    alpha=((0-an)*bn+(0-am)*bm)/delta
    beta=(-(0-an)*bm+(0-am)*bn)/delta
    u=bn*n+bm*m;v=-bm*n+bn*m
    checks={
        'alpha_zero':alpha,
        'beta_plus_one':beta+1,
        'positive_solution':an*n+am*m+bn*s.diff(n,r)+bm*s.diff(m,r),
        'solution_initial_u':u-2,
        'solution_terminal_ratio':n-m,
        'cone_ratio':v/u,
    }
    for name,value in checks.items():
        assert s.simplify(value)==0,(name,value)
    # For arbitrary positive lapses: -1<v/u<1, hence |(log u)'|<1.
    # R=17/20<1 and e<3 imply u(R)<u(0)*3=6 if u(0)=2.
    # The requested toy terminal N(R)=M(R)=3 requires u(R)=6: impossible.
    assert F(17,20)<1 and F(3,1)*2==6
    assert s.exp(1)<3  # exact symbolic inequality handled by SymPy
    return len(checks)


def audit():
    return {'stage':'b3c3d6_PARTIAL','algebraic_residuals':algebraic_certificate(),
            'toy_residuals':toy_certificate(),
            'scope':'CONDITIONAL_POSITIVE_CONE_AND_NECESSARY_ANNULAR_GROWTH_NOT_STEP55_NOT_DIRAC',
            'original_outer_probe_executed':False,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(audit(),indent=2))
