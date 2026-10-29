"""Exact formal local order certificate for cubic Step55 endpoint jets.

Not an original Step58 execution and not a physical solution certificate.
For 2s U_s=G(s,U)-2U on s0>0, a cubic endpoint Taylor jet
is holonomic through the third radial derivative of pLf=r^2 U(r^2),
but generally fails the next radial derivative. Uses only exact SymPy.
"""
import sympy as sp
from math import factorial


def certificate():
    s0, u0, r0, h = sp.symbols('s0 u0 r0 h', positive=True)
    g = {(i,j):sp.Symbol(f'g{i}{j}') for i in range(4) for j in range(4-i)}
    G = lambda x,y: sum(g[i,j]*x**i*y**j/(factorial(i)*factorial(j)) for i,j in g)
    u1 = (g[0,0]-2*u0)/(2*s0)
    u2 = (g[1,0]+(g[0,1]-4)*u1)/(2*s0)
    u3 = (g[2,0]+2*g[1,1]*u1+g[0,2]*u1**2+(g[0,1]-6)*u2)/(2*s0)
    u4 = (g[3,0]+3*g[2,1]*u1+3*g[1,2]*u1**2+g[0,3]*u1**3
          +3*g[1,1]*u2+3*g[0,2]*u1*u2+(g[0,1]-8)*u3)/(2*s0)
    cubic = u0+u1*h+u2*h**2/2+u3*h**3/6
    H = 2*cubic+2*(s0+h)*sp.diff(cubic,h)-G(h,cubic-u0)
    coeff = [sp.expand(H).coeff(h,k) for k in range(4)]
    assert all(sp.cancel(c)==0 for c in coeff[:3]), 'Cubic ODE residual not O(h^3)'
    assert sp.cancel(coeff[3]+s0*u4/3)==0, 'Wrong fourth-jet defect'
    # D(r) = pLf'(r) - r G(r²,U(r²)) = r H(r²-s0).
    # D, D', D'' vanish at r0; D''' = 3! * r0 * (2r0)^3 * [h^3]H.
    # Hence D'''(r0) = -16 r0^6 U_ssss(s0).
    radial_third = sp.factor(6*r0*(2*r0)**3*coeff[3])
    assert sp.cancel((radial_third+16*r0**6*u4).subs(s0,r0*r0))==0
    return {'ode_residual_coefficients':coeff,
            'fourth_jet':u4,'radial_third_defect':radial_third,
            'symbols':(s0,u0,r0), 'G_coefficients':g,
            'checked_equalities':5}


def exact_polynomial_witness():
    """A genuine analytic ODE solution with nonzero U_ssss, not JANUS."""
    r=sp.symbols('r',positive=True)
    s=sp.symbols('s')
    a,b,c,d=map(sp.Rational,('2/5','-1/7','3/11','1/13'))
    u=sp.Rational(1,3)+a*s+b*s*s+c*s**3+d*s**4
    r0=sp.Rational(1,2); s0=r0*r0
    uc=sum(sp.diff(u,s,k).subs(s,s0)*(s-s0)**k/sp.factorial(k) for k in range(4))
    # G must be evaluated at (s,uc) not at the exact solution u(s).
    U=sp.symbols('U')
    Gfun=2*U+2*s*(a+2*b*s+3*c*s*s+4*d*s**3)
    defect=sp.diff(r*r*uc.subs(s,r*r),r)-r*Gfun.subs(U,uc).subs(s,r*r)
    assert all(sp.simplify(sp.diff(defect,r,k).subs(r,r0))==0 for k in range(3))
    expected=-16*r0**6*sp.diff(u,s,4)
    assert sp.simplify(sp.diff(defect,r,3).subs(r,r0)-expected)==0
    assert expected!=0
    return {'radius':r0,'U4':sp.diff(u,s,4),'radial_third_defect':expected}


if __name__=='__main__':
    c=certificate();w=exact_polynomial_witness()
    print('PASS formal identities',c['checked_equalities'])
    print('PASS analytic ODE witness',w)
