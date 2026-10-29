"""Exact endpoint jet sensitivity, no original JANUS physical operator replay."""
import sympy as sp

def certificate():
    r,t,s,u,u0,u1,u2,u3=sp.symbols('r t s u u0 u1 u2 u3',real=True,positive=True)
    # A nonlinear polynomial G makes all partials explicit, including mixed terms.
    a,b,c,d,e=sp.symbols('a b c d e',real=True)
    G=a*s**2+b*s*u+c*u**2+d*s+e*u
    S=r*r; delta=t*t-S
    Ua=u0+u1*delta
    Uc=Ua+u2*delta**2/sp.Integer(2)+u3*delta**3/sp.Integer(6)
    def diff_at(expr,order): return sp.diff(expr,t,order).subs(t,r).expand()
    def difference(expr,order): return sp.factor(diff_at(expr(Uc),order)-diff_at(expr(Ua),order))
    plf=lambda U:t*t*U
    plfr=lambda U:t*G.subs({s:t*t,u:U})
    G_u=sp.diff(G,u).subs({s:S,u:u0});G_su=sp.diff(G,s,u).subs({s:S,u:u0});G_uu=sp.diff(G,u,2).subs({s:S,u:u0})
    expected={
        'pLf_q':sp.Integer(0), 'pLf_q1':sp.Integer(0),
        'pLf_q2':4*r**4*u2,
        'pLf_q3':36*r**3*u2+8*r**5*u3,
        'pLfr_q':sp.Integer(0), 'pLfr_q1':sp.Integer(0),
        'pLfr_q2':4*r**3*G_u*u2,
        'pLfr_q3':24*r**2*G_u*u2+24*r**4*(G_su+G_uu*u1)*u2+8*r**4*G_u*u3,
    }
    residuals={}
    for name,fun in [('pLf',plf),('pLfr',plfr)]:
        for k in range(4):
            key=f'{name}_q{k}' if k else f'{name}_q'
            residuals[key]=sp.factor(difference(fun,k)-expected[key])
    if any(v!=0 for v in residuals.values()):raise AssertionError(residuals)
    # Generic nonlinear dependence F(s,U), applicable to other fields including pf,pSf.
    f0,f1,f2=sp.symbols('f0 f1 f2')
    F=f0*s+f1*u+f2*u*u
    generic=lambda U:F.subs({s:t*t,u:U})
    generic_residual=sp.factor(difference(generic,2)-4*r*r*(f1+2*f2*u0)*u2)
    if generic_residual!=0:raise AssertionError(generic_residual)
    # A toy off-shell example demonstrates a genuinely nonzero third-jet correction.
    witness={r:sp.Rational(1,2),u0:sp.Rational(1,3),u1:sp.Rational(1,5),u2:sp.Rational(2,7),u3:sp.Rational(-1,11),a:1,b:2,c:3,d:4,e:5}
    delta={key:sp.factor(value.subs(witness)) for key,value in expected.items()}
    assert delta['pLf_q2']!=0 and delta['pLf_q3']!=0 and delta['pLfr_q2']!=0 and delta['pLfr_q3']!=0
    return {'residuals':residuals,'generic_residual':generic_residual,'toy_deltas':delta}

if __name__=='__main__':
    import json
    d=certificate();print(json.dumps({'exact_zero_residuals':len(d['residuals'])+1,'toy_deltas':{k:str(v) for k,v in d['toy_deltas'].items()}},indent=2))
