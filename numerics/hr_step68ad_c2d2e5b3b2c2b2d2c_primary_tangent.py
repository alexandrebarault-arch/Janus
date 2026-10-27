"""JANUS d2c: exact primary-constraint tangent boundary-curvature witness.

A deliberately NON-Step55 interaction. Only pointwise primary constraints
(Hg=Hf=Dtotal=Fz=0) are imposed, not the secondary/Dirac chain.
"""
import json
import sympy as sp


def run_checks():
    x, y = sp.symbols('x y', real=True)
    Lg, Lf, Sg, Sf = map(sp.Integer, (2, 3, 5, 7))
    Sgr = Sfr = sp.Integer(1)
    Sg2 = Sf2 = sp.Integer(-2)
    pSg, pLf, pSf = sp.Integer(4), sp.Integer(3), sp.Integer(0)
    N = M = sp.Integer(1)
    V = sp.Integer(0)
    mg = mf = m2 = sp.Integer(1)
    b1 = sp.Rational(1, 50)
    A0, At, As = 2*b1*Sg*Sf, b1*Sg**2, sp.Integer(0)
    K = m2*mg*Lg*Lf*At
    Dg = pSg*Sgr-Lg*y  # tg'=0
    root = sp.sqrt(K**2+Dg**2)
    z = Dg/root
    rHR = K/root
    pLfr = Dg/Lf  # Dg + Df = 0; pSf=0, tf'=0
    Rg = 2/Sg**2*(1-(Sgr/Lg)**2-2*Sg/Lg*(Sg2/Lg))
    Rf = 2/Sf**2*(1-(Sfr/Lf)**2-2*Sf/Lf*(Sf2/Lf))
    Hg0 = (Lg*x**2/(4*mg*Sg**2)-x*pSg/(2*mg*Sg)
           -mg*Lg*Sg**2*Rg/2+z*Dg/Lg
           +m2*mg*(Lg*A0+Lf*At*rHR))
    Hf0 = (Lf*pLf**2/(4*mf*Sf**2)-pLf*pSf/(2*mf*Sf)
           -mf*Lf*Sf**2*Rf/2+z*Dg/Lf
           +m2*mg*(Lf*As+Lg*At*rHR))
    pg, pf = -Hg0, -Hf0  # positive dust on an open neighborhood of x=2,y=0
    A = N+M*Lg/Lf
    curvature = sp.diff(-A*z, y)  # dTheta(∂y,∂x)
    checks = 0

    def check(expr, expected=0):
        nonlocal checks
        assert sp.simplify(expr-expected) == 0, (expr, expected)
        checks += 1

    check(A0, sp.Rational(7, 5))
    check(At, sp.Rational(1, 2))
    check(K, 3)
    check(Rg, sp.Rational(23, 50))
    check(Rf, sp.Rational(8, 49))
    check(Dg + pSf*Sfr - Lf*pLfr)  # D_total=0
    check(sp.simplify(Dg-K*z/rHR))  # Fz/Q=0
    check(Hg0+pg)  # original g primary, exact in x,y
    check(Hf0+pf)  # original f primary, exact in x,y
    check(curvature, A*Lg*K**2/root**3)
    check(curvature.subs({x: 2, y: 0}), sp.Rational(6, 25))
    check(z.subs(y, 0), sp.Rational(4, 5))
    check(pg.subs({x: 2, y: 0}), sp.Rational(173, 25))
    check(pf.subs({x: 2, y: 0}), sp.Rational(5995, 588))
    check(pLfr.subs(y, 0), sp.Rational(4, 3))
    assert pg.subs({x: 2, y: 0}) > 0; checks += 1
    assert pf.subs({x: 2, y: 0}) > 0; checks += 1
    assert curvature.subs(y, 0) > 0; checks += 1
    assert sp.simplify(curvature - 30/root**3) == 0; checks += 1
    result = {
        'assertions_passed': checks, 'assertions_failed': 0,
        'scope': 'two-dimensional pointwise primary-constraint submanifold; NOT full Dirac tangent',
        'interaction': {'beta0': '0', 'beta1': '1/50', 'beta2': '0', 'beta3': '0', 'beta4': '0'},
        'witness': {'x_pLg': '2', 'y_pLg_prime': '0', 'K': '3', 'Dg': '4',
                    'z': '4/5', 'pg': '173/25', 'pf': '5995/588',
                    'pLf_prime': '4/3', 'dTheta_dy_dx': '6/25'},
        'curvature_general': '30/(9+(4-2*y)^2)^(3/2)',
        'scientific_status': {'GATE_2B': 'OPEN', 'JANUS_R': 'NOT_VALIDATED'},
    }
    return result


if __name__ == '__main__':
    print(json.dumps(run_checks(), indent=2, sort_keys=True))
