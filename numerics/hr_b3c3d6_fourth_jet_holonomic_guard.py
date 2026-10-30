"""Exact fourth Step55 ODE jet and derivative-dependent Step58 guard.

For 2*s*U_s=G(s,U)-2*U at s0>0, the quartic Taylor extension
matches the ODE through the THIRD radial derivative of pLf'=r*G.
A cubic matches only through the SECOND derivative of pLf'.

This is a formal point-jet certificate, not a physical Step58 replay,
continuous residual enclosure, or positive-lapse/Dirac result.
"""
import sympy as sp


def jets_through_four(G, s, u):
    """Return exact U_s through U_ssss for a differentiable G(s,u)."""
    gs = sp.diff(G, s)
    gu = sp.diff(G, u)
    u1 = (G-2*u)/(2*s)
    u2 = (gs+(gu-4)*u1)/(2*s)
    u3 = (sp.diff(G,s,2)+2*sp.diff(G,s,u)*u1
          +sp.diff(G,u,2)*u1**2+(gu-6)*u2)/(2*s)
    u4 = (sp.diff(G,s,3)+3*sp.diff(G,s,2,u)*u1
          +3*sp.diff(G,s,u,2)*u1**2+sp.diff(G,u,3)*u1**3
          +3*(sp.diff(G,s,u)+sp.diff(G,u,2)*u1)*u2
          +(gu-8)*u3)/(2*s)
    return (u1,u2,u3,u4)


def polynomial_extension(r, r0, u0, jet_values, degree):
    """Taylor polynomial of U(r^2) in h=r^2-r0^2."""
    if degree not in (3,4) or len(jet_values)<degree:
        raise ValueError('degree must be 3 or 4 with sufficient jets')
    h=r*r-r0*r0
    return u0+sum(jet_values[k-1]*h**k/sp.factorial(k)
                  for k in range(1,degree+1))


def endpoint_radial_residual_derivatives(G,s,u,s0,u0,order=3):
    """Exact radial jets of H=2U+2sU_s-G, cubic and quartic.

    H is the NORMALIZED ODE residual, not a DOP853 error estimate.
    """
    if order>3:raise ValueError('only order <=3 is certified here')
    r,r0=sp.symbols('r r0', positive=True)
    js=jets_through_four(G,s,u)
    vals=[sp.cancel(x.subs({s:s0,u:u0})) for x in js]
    out={}
    for deg in (3,4):
        poly=polynomial_extension(r,r0,u0,vals,deg)
        H=2*poly+r*sp.diff(poly,r)-G.subs({s:r*r,u:poly})
        out[deg]=[sp.factor(sp.diff(H,r,k).subs(r,r0).subs(r0,sp.sqrt(s0)))
                  for k in range(order+1)]
    return out,vals
