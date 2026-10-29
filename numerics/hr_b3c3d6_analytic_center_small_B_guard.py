"""Exact toy-only analytic-center guard for singular small-B lapse equations.

Not Step55/58, not Dirac. Positive eps and R, 0<r<=R.
"""
import sympy as sp

r, eps, R, C = sp.symbols('r eps R C', positive=True)
N = 2 + C * sp.exp(-1 / (eps * r))
M = sp.S.One
A_N, A_M = r**2, -2 * r**2
B_N, B_M = -eps * r**4, sp.S.Zero

def residual(n=N):
    return sp.simplify(A_N*n + A_M*M + B_N*sp.diff(n, r))

def boundary_constant():
    return -sp.exp(1 / (eps * R))

def terminal_slope():
    return sp.simplify(sp.diff(N, r).subs(C, boundary_constant()).subs(r, R))

def center_taylor_coefficients(n):
    """Recurrence from eps*r**2*n' = n-2 for formal n=sum a_k*r**k."""
    a0 = sp.Integer(2)
    coeffs = [a0]
    for k in range(1, n + 1):
        coeffs.append(sp.simplify(eps * (k-1) * coeffs[k-1]))
    return coeffs
