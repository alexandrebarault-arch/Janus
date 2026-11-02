"""Exact Step55 ODE jet-closure formulas for a future continuous Step58 gate.

Generic algebra only. No physical Step55/58 coefficient or derivative is enclosed.
The physical coefficients may depend on U, U_s, U_ss after spatial reduction;
that dependency must be independently checked on the original operators.
"""
import sympy as sp

s, u, v, w = sp.symbols('s u v w', real=True)


def ode_jet_closure(G):
    """For 2*s*U_s=G(s,U)-2*U, derive U_s,U_ss,U_sss for s>0."""
    gs, gu = sp.diff(G, s), sp.diff(G, u)
    gss, gsu, guu = sp.diff(G, s, 2), sp.diff(G, s, u), sp.diff(G, u, 2)
    u1 = (G - 2*u)/(2*s)
    u2 = (gs + (gu - 4)*u1)/(2*s)
    u3 = (gss + 2*gsu*u1 + guu*u1**2 + (gu - 6)*u2)/(2*s)
    return tuple(sp.factor(x) for x in (u1, u2, u3))


def normalized_coefficient_derivative(A, u3):
    """D_s(A/s) for A=A(s,U,U_s,U_ss), via exact holonomic chain rule."""
    total = sp.diff(A, s) + sp.diff(A, u)*v + sp.diff(A, v)*w + sp.diff(A, w)*u3
    return sp.factor((s*total - A)/s**2)


def center_coefficients(G, u0):
    """Regular nonresonant center U=U0+U1*s+U2*s**2+... .

    Requires G(0,U0)=2U0 and nonzero (4-G_U),(6-G_U).
    Returns U1,U2, or raises on resonance. NOT a physical center enclosure.
    """
    z = {s: sp.Integer(0), u: u0}
    g0, gu = sp.simplify(G.subs(z)), sp.simplify(sp.diff(G, u).subs(z))
    if sp.simplify(g0-2*u0) != 0:
        raise ValueError('center regularity condition G(0,U0)=2U0 fails')
    if sp.simplify(4-gu)==0 or sp.simplify(6-gu)==0:
        raise ValueError('resonant center: separate Frobenius analysis needed')
    u1 = sp.factor(sp.diff(G,s).subs(z)/(4-gu))
    numerator = (sp.diff(G,s,2)+2*sp.diff(G,s,u)*u1+sp.diff(G,u,2)*u1**2).subs(z)
    u2 = sp.factor(numerator/(2*(6-gu)))
    return u1, u2


def missing_second_partial_witness(s0, epsilon=1):
    """Two analytic toy G share G,G_s,G_U at s0 but have different U_sss.

    This shows pointwise G/G_s/G_U data cannot by themselves bound U_sss.
    It says nothing about the FIXED original physical G, which is known.
    """
    s0, epsilon = sp.Rational(s0), sp.Rational(epsilon)
    if s0 <= 0: raise ValueError('witness requires s0>0')
    g0 = 2*u + 2*s*(1+s+s*s)
    g1 = g0 + epsilon*(s-s0)**2
    jet0, jet1 = ode_jet_closure(g0), ode_jet_closure(g1)
    at = {s:s0}
    assert all(sp.simplify(sp.diff(g1-g0,x).subs(at))==0 for x in (s,u))
    assert sp.simplify((g1-g0).subs(at))==0
    assert sp.simplify((jet1[0]-jet0[0]).subs(at))==0
    assert sp.simplify((jet1[1]-jet0[1]).subs(at))==0
    delta3 = sp.factor((jet1[2]-jet0[2]).subs(at))
    assert sp.simplify(delta3-epsilon/s0)==0
    return delta3


def audit():
    G = 2*u+2*s*(1+2*s+3*s*s)
    jets = ode_jet_closure(G)
    assert all(sp.simplify(a-b)==0 for a,b in zip(jets,(1+2*s+3*s*s,2+6*s,6)))
    assert center_coefficients(G,sp.Integer(0)) == (sp.Integer(1),sp.Integer(1))
    return {'scope':'EXACT_GENERIC_JET_BUDGET_ONLY_NOT_PHYSICAL_STEP58_DERIVATIVE_ENCLOSURE',
            'U_sss_requires':'G_ss, G_sU, G_UU and U_s,U_ss on s>0',
            'normalized_derivative':'D_s(A/s)=(s*D_s A-A)/s**2',
            'missing_partial_witness_s0':'1/4',
            'missing_partial_witness_delta_U_sss':str(missing_second_partial_witness(sp.Rational(1,4))),
            'physical_derivative_bounds_certified':False,
            'physical_center_certified':False,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}


if __name__=='__main__':
    import json
    print(json.dumps(audit(),indent=2))
