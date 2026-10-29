"""Exact weak dual positivity screen for a Step58-TYPE scalar lapse equation.

The polynomial witness is invented, NOT the physical Step58 operator.
For the physical operator the dual weights must be certified independently.
"""
import sympy as sp

x = sp.symbols('x', real=True)
R = sp.Rational(17, 20)
eps = sp.Rational(1, 100)
phi = x**2 * (1-x)**2
base = phi * x**2
B = eps*x**3*(1-x)**3
E = eps**2*x**4*(1-x)**4
c1 = 5*x**4*(1-x)**4*(1-2*x)
c2 = 6*x**4*(1-x)**4*(5*(1-2*x)**2-2*x*(1-x))


def dual_coefficients():
    """After two integrations by parts; no lapse derivative remains."""
    qn = sp.factor(base-sp.diff(phi*B, x)+sp.diff(phi*E, x, 2))
    qm = sp.factor(base+sp.diff(phi*B, x)-sp.diff(phi*E, x, 2))
    return qn, qm


def exact_certificate():
    qn, qm = dual_coefficients()
    margin = sp.Rational(9467, 10000)
    return {
        'd_phi_B': sp.factor(sp.diff(phi*B, x)-eps*c1),
        'dd_phi_E': sp.factor(sp.diff(phi*E, x, 2)-eps**2*c2),
        'qn_formula': sp.factor(qn-(base-eps*c1+eps**2*c2)),
        'qm_formula': sp.factor(qm-(base+eps*c1-eps**2*c2)),
        'sum_identity': sp.factor(qn+qm-2*base),
        'boundary_phi': (phi.subs(x, 0), phi.subs(x, 1)),
        'boundary_dphi': (sp.diff(phi, x).subs(x, 0), sp.diff(phi, x).subs(x, 1)),
        'lower_margin': margin,
        'qN': qn,
        'qM': qm,
    }


def point_checks():
    """Exact rational spot checks; not the proof of uniform positivity."""
    qn, qm = dual_coefficients()
    margin = sp.Rational(9467, 10000)
    return tuple(sp.factor((q-margin*base).subs(x, t))
                 for t in (sp.Rational(1,4), sp.Rational(1,2), sp.Rational(3,4))
                 for q in (qn, qm))


def zero_control():
    """If A_M=-A_N and B_M=-B_N, E_M=-E_N, N=M=1 solves T=0."""
    n = sp.S.One
    m = sp.S.One
    return sp.simplify(x**2*n-x**2*m+B*sp.diff(n,x)-B*sp.diff(m,x)
                       +E*sp.diff(n,x,2)-E*sp.diff(m,x,2))
