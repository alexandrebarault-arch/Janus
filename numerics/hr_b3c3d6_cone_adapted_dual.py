"""Exact ratio-cone weak-dual screen; toy only, not Step58 physical.

If N>0 and lo<=M/N<=hi, min(QN+lo*QM, QN+hi*QM)>=0
with strict positivity on an open set excludes a positive solution of T=0.
"""
import sympy as sp

x = sp.symbols('x', real=True)
eps = sp.Rational(1, 100)
phi = x**2 * (1-x)**2
B = eps*x**3*(1-x)**3
E = eps**2*x**4*(1-x)**4
lo, hi = sp.Rational(1, 4), sp.Rational(1, 2)
A_N, A_M = sp.Integer(2), sp.Integer(-3)


def dual(A, b, e):
    return sp.factor(phi*A - sp.diff(phi*b, x) + sp.diff(phi*e, x, 2))


def coefficients():
    return dual(A_N, B, E), dual(A_M, -B, -E)


def exact_lower_margin():
    """Elementary uniform lower bound on (QN+rho QM)/phi, rho in [lo,hi]."""
    return sp.Rational(1, 2) - sp.Rational(3, 4)*(5*eps/16 + 33*eps**2/16)


def toy_certificates():
    qn, qm = coefficients()
    d1 = sp.factor(sp.diff(phi*B, x))
    d2 = sp.factor(sp.diff(phi*E, x, 2))
    return {
        'd1_identity': sp.factor(d1-5*eps*x**4*(1-x)**4*(1-2*x)),
        'd2_identity': sp.factor(d2-6*eps**2*x**4*(1-x)**4*(5*(1-2*x)**2-2*x*(1-x))),
        'Q_N': qn, 'Q_M': qm,
        'integrated_Q_M': sp.integrate(qm, (x,0,1)),
        'integrated_phi_A_M': sp.integrate(phi*A_M, (x,0,1)),
        'lower_margin': exact_lower_margin(),
        'outside_cone_solution': sp.simplify(A_N + A_M*sp.Rational(2,3)),
        'boundary_phi': tuple(phi.subs(x,t) for t in (0,1)),
        'boundary_dphi': tuple(sp.diff(phi,x).subs(x,t) for t in (0,1)),
    }
