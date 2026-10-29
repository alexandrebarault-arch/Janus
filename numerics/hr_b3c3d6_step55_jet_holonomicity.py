"""Exact endpoint-jet consistency audit for the published Step55/Step58 probe.

Scope: a mathematical audit of the interpolation in
numerics/hr_b3c3d6_full_original_step58_point_probe.py (Git blob
643d90183367e74a28ed453d93f5489074b75b08).
This module does NOT execute the original Step55 or Step58 engines.
"""
import sympy as sp


def ode_jets(G, s, u):
    """For 2*s*U_s=G(s,U)-2*U, s>0: return U_s,U_ss,U_sss."""
    u1 = sp.factor((G - 2*u)/(2*s))
    u2 = sp.factor((sp.diff(G, s) + (sp.diff(G, u)-4)*u1)/(2*s))
    u3 = sp.factor((sp.diff(G, s, 2) + 2*sp.diff(G,s,u)*u1
                    + sp.diff(G,u,2)*u1**2 + (sp.diff(G,u)-6)*u2)/(2*s))
    return u1,u2,u3


def certificate():
    s,u=sp.symbols('s u',positive=True)
    G=sp.Function('G')(s,u)
    u1,u2,u3=ode_jets(G,s,u)
    # True pLf = r^2 U(r^2) and derivative pLf'=r*G(s,U).
    # The current point probe uses Ulin(s)=u+u1*(s-s0), so Ulin''=0.
    # Its pLf'' and pLf''' therefore omit the terms below.
    defect2=sp.factor(4*s**2*u2)
    defect3=sp.factor(36*sp.sqrt(s)*s*u2+8*sp.sqrt(s)*s**2*u3)
    # Differentiate the original ODE twice (formal total derivative).
    D=lambda e:sp.diff(e,s)+sp.diff(e,u)*u1
    assert sp.simplify(2*s*u2-sp.diff(G,s)-(sp.diff(G,u)-4)*u1)==0
    assert sp.simplify(2*s*u3-sp.diff(G,s,2)-2*sp.diff(G,s,u)*u1
        -sp.diff(G,u,2)*u1**2-(sp.diff(G,u)-6)*u2)==0
    # Check holonomic pLf'' via derivative of r*G, rather than a
    # separately linearized r^2*U. They agree only when Uss=0.
    true_p2=sp.factor(G+2*s*(sp.diff(G,s)+sp.diff(G,u)*u1))
    linear_p2=sp.factor(2*u+10*s*u1)
    assert sp.simplify(true_p2-linear_p2-defect2)==0
    # Direct third derivative of r^2 U(r^2):
    # p'''=24*r*U_s+36*r*s*U_ss+8*r*s^2*U_sss.
    return {'U_s':u1,'U_ss':u2,'U_sss':u3,'pLf_second_jet_defect':defect2,
            'pLf_third_jet_defect':defect3,
            'true_pLf_second':true_p2,'linear_pLf_second':linear_p2,
            'scope':'formal exact ODE chain rule, not actual Step55 numerical evaluation'}


def toy_witness():
    s,u=sp.symbols('s u',positive=True)
    G=s*s+u*u
    jets=ode_jets(G,s,u)
    sub={s:sp.Rational(1,4),u:sp.Rational(1,2)}
    v=[sp.factor(x.subs(sub)) for x in jets]
    d2=sp.factor((4*s*s*jets[1]).subs(sub))
    d3=sp.factor((36*sp.sqrt(s)*s*jets[1]+8*sp.sqrt(s)*s*s*jets[2]).subs(sub))
    assert d2!=0 and d3!=0
    return {'G':'s^2+u^2','s':'1/4','u':'1/2',
            'U_s':str(v[0]),'U_ss':str(v[1]),'U_sss':str(v[2]),
            'pLf_second_jet_defect':str(d2),'pLf_third_jet_defect':str(d3)}

if __name__=='__main__':
    import json
    certificate()
    print(json.dumps(toy_witness(),indent=2))
