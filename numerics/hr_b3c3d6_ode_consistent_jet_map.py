"""Pointwise Step55 ODE jet map through order three (s>0).

For 2s U_s = G(s,U)-2U, returns U_s,U_ss,U_sss and verifies
independent radial chain-rule identities for pLf=r^2 U(r^2).
This module does not certify an ODE solution or physical lapse BVP.
"""
import mpmath as mp


def endpoint_jets(G, s, u):
    if not (s > 0):
        raise ValueError('ODE jet map requires s>0; center needs separate regular series')
    g = G(s, u)
    gs = mp.diff(lambda x: G(x, u), s)
    gu = mp.diff(lambda x: G(s, x), u)
    gss = mp.diff(lambda x: G(x, u), s, 2)
    gsu = mp.diff(lambda x: mp.diff(lambda y: G(x, y), u), s)
    guu = mp.diff(lambda x: G(s, x), u, 2)
    u1 = (g - 2*u)/(2*s)
    u2 = (gs + (gu-4)*u1)/(2*s)
    u3 = (gss + 2*gsu*u1 + guu*u1*u1 + (gu-6)*u2)/(2*s)
    r = mp.sqrt(s)
    # Independent ODE-side derivatives of pLf'=r G(s,U).
    h = gs + gu*u1
    dh = gss + 2*gsu*u1 + guu*u1*u1 + gu*u2
    p1 = r*g
    p2 = g + 2*s*h
    p3 = 6*r*h + 4*r*s*dh
    # Direct derivatives of r^2 U(r^2) through the cubic endpoint jet.
    p1_poly = 2*r*u + 2*r*s*u1
    p2_poly = 2*u + 10*s*u1 + 4*s*s*u2
    p3_poly = 24*r*u1 + 36*r*s*u2 + 8*r*s*s*u3
    residuals = (p1-p1_poly, p2-p2_poly, p3-p3_poly)
    tolerance = mp.power(10, -max(12, mp.mp.dps-12))
    if any(abs(x) > tolerance*max(1,abs(y)) for x,y in zip(residuals,(p1,p2,p3))):
        raise AssertionError(f'Nonholonomic Step55 jets: {residuals}')
    return {'U_s':u1,'U_ss':u2,'U_sss':u3,
            'pLf_prime':p1,'pLf_second':p2,'pLf_third':p3,
            'holonomic_residuals':residuals,
            'affine_defect_second':4*s*s*u2,
            'affine_defect_third':36*r*s*u2+8*r*s*s*u3}


def cubic_U(t, s, u, jets):
    delta=t*t-s
    return u+jets['U_s']*delta+jets['U_ss']*delta**2/2+jets['U_sss']*delta**3/6
