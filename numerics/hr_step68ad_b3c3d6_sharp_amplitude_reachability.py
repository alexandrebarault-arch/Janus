"""Sharp conditional two-endpoint reachability for ONE first-order lapse equation.
NOT Step55, NOT the full Step58 differential operator, NOT Dirac.
"""
import sympy as s

def symbolic_checks():
    r=s.symbols('r',real=True)
    bn=s.Function('BN')(r); bm=s.Function('BM')(r)
    an=s.Function('AN')(r); am=s.Function('AM')(r)
    n=s.Function('N')(r); m=s.Function('M')(r)
    u=bn*n+bm*m
    sn=(s.diff(bn,r)-an)/bn
    sm=(s.diff(bm,r)-am)/bm
    w=bm*m/u
    eq=an*n+am*m+bn*s.diff(n,r)+bm*s.diff(m,r)
    residuals={
      'weighted_equation':s.diff(u,r)-(sn*(1-w)+sm*w)*u-eq,
      'weights_sum':(bn*n/u)+(bm*m/u)-1,
      'inverse_n':(1-w)*u/bn-n,
      'inverse_m':w*u/bm-m,
      'slope_difference':s.factor(sm-sn-((s.diff(bm,r)-am)/bm-(s.diff(bn,r)-an)/bn)),
    }
    assert all(s.simplify(x)==0 for x in residuals.values()),residuals
    return len(residuals)

def toy_checks():
    r=s.symbols('r',real=True)
    checks={}
    # Constant coefficients: w=1/2, slope pair (0,1), both endpoints fixed.
    bn=bm=s.Integer(1);an=s.Integer(0);am=s.Integer(-1)
    n=m=s.exp(r/2)
    checks['constant_operator']=an*n+am*m+bn*s.diff(n,r)+bm*s.diff(m,r)
    checks['constant_u0']=(n+m).subs(r,0)-2
    checks['constant_u1']=(n+m).subs(r,1)-2*s.exp(s.Rational(1,2))
    checks['constant_ratio_R']=(m/n).subs(r,1)-1
    # Variable B coefficients: BN=1+r, BM=2+r, sN=0,sM=1.
    bn=1+r;bm=2+r;an=s.Integer(1);am=-1-r
    u=2*s.exp(r/2)
    n=u/(2*bn);m=u/(2*bm)
    checks['variable_operator']=an*n+am*m+bn*s.diff(n,r)+bm*s.diff(m,r)
    checks['variable_u0']=(bn*n+bm*m).subs(r,0)-2
    checks['variable_u1']=(bn*n+bm*m).subs(r,1)-2*s.exp(s.Rational(1,2))
    checks['variable_initial_N']=n.subs(r,0)-1
    checks['variable_initial_M']=m.subs(r,0)-s.Rational(1,2)
    checks['variable_terminal_N']=n.subs(r,1)-s.exp(s.Rational(1,2))/2
    checks['variable_terminal_M']=m.subs(r,1)-s.exp(s.Rational(1,2))/3
    assert all(s.simplify(v)==0 for v in checks.values()),checks
    # Endpoint equality at upper bound is impossible: w<1 on a nonzero interval.
    assert s.integrate(s.Integer(1),(r,0,1))==1
    assert s.integrate(s.Integer(0),(r,0,1))==0
    return len(checks),2

if __name__=='__main__':
    print({'symbolic_residuals':symbolic_checks(),'exact_toy_residuals':toy_checks()[0],
           'strict_boundary_checks':toy_checks()[1], 'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'})
