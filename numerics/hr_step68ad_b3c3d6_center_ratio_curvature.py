"""b3c3d6: formal center lapse-ratio curvature; NOT original Step58 execution."""
import sympy as s

r,a,b,c,d,e,f,n0,n2=s.symbols('r a b c d e f n0 n2', real=True)
rho0=-a/c
rho2_shell=-(b+d*rho0)/c
rho2_full=-((b+d*rho0)+2*(e+f*rho0)*n2/n0)/(c+2*f)

def check():
    assert s.simplify(a+c*rho0)==0
    assert s.simplify(a*n2+c*(rho0*n2+n0*rho2_shell)+(b+d*rho0)*n0)==0
    assert s.simplify((a+2*e)*n2+(c+2*f)*(rho0*n2+n0*rho2_full)+(b+d*rho0)*n0)==0
    assert s.simplify(rho2_full.subs({e:0,f:0})-rho2_shell)==0
    assert s.simplify(s.diff(rho2_shell,n2))==0
    assert s.simplify(s.diff(rho2_full,n2)+2*(e+f*rho0)/(n0*(c+2*f)))==0
    N=1+n2*r**2
    M=N*(s.Rational(1,2)+r**2/4)
    ME=((2+r**2)*N+r**2*s.diff(N,r,2))/4
    assert s.expand((2*r**2+r**4)*N-4*r**2*M)==0
    assert s.expand((2*r**2+r**4)*N-4*r**2*ME+r**4*s.diff(N,r,2))==0
    assert s.simplify(s.diff(M/N,r,2).subs(r,0)-s.Rational(1,2))==0
    assert s.simplify(s.diff(ME/N,r,2).subs(r,0)-(s.Rational(1,2)+n2))==0
    for u in (0,1):
        for lapse in (N,M,ME):
            poly=s.Poly(lapse.subs(n2,u),r)
            assert all(coef>=0 for coef in poly.all_coeffs())
            assert lapse.subs({n2:u,r:0})>0
    return {'symbolic_residuals':11,'positive_toy_families':2,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__': print(check())
