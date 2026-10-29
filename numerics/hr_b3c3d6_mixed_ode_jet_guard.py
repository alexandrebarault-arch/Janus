"""Exact local guard for Step55 mixed algebraic/ODE jet dependencies.

For s=r**2, p=s*U(s), v=r*G(s,U), and 2*s*U_s=G-2*U,
using v=r*G (rather than d(s*U_cubic)/dr) is necessary when
third derivatives of dependent fields F(r,U,v) are requested.
This is a formal toy check, not a numerical physical Step58 replay.
"""
import sympy as sp

r=sp.symbols('r', positive=True)
s=sp.symbols('s', positive=True)
u=sp.symbols('u')


def example():
    r0=sp.Rational(1,2)
    s0=r0*r0
    f=3+2*s+s**3+s**4
    fprime=sp.diff(f,s)
    # Exact analytic solution of the scalar ODE, with G depending on U.
    G=2*u+2*s*fprime
    uc=sp.series(f,s,s0,4).removeO().expand()
    uq=f
    gc=G.subs(u,uc)
    gq=G.subs(u,uq)
    vc=r*gc.subs(s,r*r)
    vq=r*gq.subs(s,r*r)
    wrong=sp.diff((r*r)*uc.subs(s,r*r),r)
    D=wrong-vc
    return dict(r=r,r0=r0,s=s,u=u,G=G,uc=uc,uq=uq,
                vc=vc,vq=vq,wrong=wrong,D=D,
                U4=sp.diff(f,s,4))


def jets_at(expr,r,r0,max_order=3):
    return tuple(sp.simplify(sp.diff(expr,r,k).subs(r,r0)) for k in range(max_order+1))


def composite_guard():
    d=example();r=d['r'];r0=d['r0'];s=d['s']
    x,v=sp.symbols('x v')
    # Nonlinear dependence on v mirrors algebraic dust momentum elimination.
    F=r**2+3*x-2*v+5*x*v+7*v*v
    h_true=F.subs({x:d['uq'].subs(s,r*r),v:d['vq']})
    h_good=F.subs({x:d['uc'].subs(s,r*r),v:d['vc']})
    h_wrong=F.subs({x:d['uc'].subs(s,r*r),v:d['wrong']})
    d3=sp.simplify(sp.diff(h_wrong-h_good,r,3).subs(r,r0))
    predicted=sp.simplify(sp.diff(F,v).subs({x:d['uc'].subs(s,r0*r0),v:d['vc'].subs(r,r0)})*(-16*r0**6*d['U4']))
    return dict(**d,F=F,true=h_true,good=h_good,bad=h_wrong,
                d3=d3,predicted=predicted)
