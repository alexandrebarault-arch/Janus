"""Necessary integrated sign conditions for a nonnegative weak-dual multiplier.

Pure operator-level theorem, not a physical Step58 certificate.
"""
import sympy as sp


def dual_density(phi, A, B, E, x):
    return sp.diff(phi*E, x, 2) - sp.diff(phi*B, x) + phi*A


def integral_identity(phi, A, B, E, x, a=0, b=1):
    """Return (direct dual integral, bulk A integral, boundary correction)."""
    q = dual_density(phi, A, B, E, x)
    left = sp.integrate(q, (x, a, b))
    bulk = sp.integrate(phi*A, (x, a, b))
    bdry = (phi*E).diff(x).subs(x,b) - (phi*E).diff(x).subs(x,a) - (phi*B).subs(x,b) + (phi*B).subs(x,a)
    assert sp.simplify(left-bulk-bdry) == 0
    return sp.simplify(left), sp.simplify(bulk), sp.simplify(bdry)


def witness():
    x=sp.symbols('x', real=True)
    phi=x**2*(1-x)**2
    A_M=-2-x**2
    B_M=x**3*(1-x)
    E_M=x**2*(1-x)**2/sp.Integer(100)
    q=sp.factor(dual_density(phi,A_M,B_M,E_M,x))
    lhs,bulk,bdry=integral_identity(phi,A_M,B_M,E_M,x)
    return dict(x=x,phi=phi,A_M=A_M,B_M=B_M,E_M=E_M,Q_M=q,integral_Q_M=lhs,integral_phi_A_M=bulk,boundary=bdry)
