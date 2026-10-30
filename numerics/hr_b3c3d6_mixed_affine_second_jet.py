"""Exact off-point second-jet defect: historical mixed-affine versus ODE cubic.

This module proves a formal local identity for a smooth G(s,U), not a
physical Step58 numerical replay. It does not assert that the six Step58
coefficients use second radial jets of the U-dependent fields.
"""
import sympy as sp


def identities():
    h, s0, r0, u0, u1 = sp.symbols('h s0 r0 u0 u1', nonzero=True, real=True)
    gs, gu, gss, gsu, guu = sp.symbols('G_s G_U G_ss G_sU G_UU', real=True)
    u2 = (gs + (gu-4)*u1)/(2*s0)
    u3 = (gss+2*gsu*u1+guu*u1**2+(gu-6)*u2)/(2*s0)
    ua = u0+u1*h
    uc = ua+u2*h**2/2+u3*h**3/6
    g0 = 2*u0+2*s0*u1
    def gtaylor(u):
        du=u-u0
        return g0+gs*h+gu*du+(gss*h*h+2*gsu*h*du+guu*du*du)/2
    # r*G(s,Ua) is historical mixed-affine; 2*r*(U+s U_s) is holonomic.
    mixed_reduced = gtaylor(ua)
    cubic_reduced = 2*uc+2*(s0+h)*sp.diff(uc,h)
    gap = sp.expand(mixed_reduced-cubic_reduced)
    coeff0=sp.factor(gap.coeff(h,0))
    coeff1=sp.factor(gap.coeff(h,1))
    coeff2=sp.factor(gap.coeff(h,2))
    plf_gap=sp.expand((s0+h)*(ua-uc))
    assert coeff0==0 and coeff1==0
    assert sp.simplify(coeff2+gu*u2/2)==0
    assert sp.simplify(plf_gap.coeff(h,2)+s0*u2/2)==0
    # For any h=r^2-r0^2 and s0=r0^2, second r derivative of h^2 at r0=8*r0^2.
    pLfr_second_gap=sp.factor(8*r0**2 * r0*coeff2)
    pLf_second_gap=sp.factor(8*r0**2 * plf_gap.coeff(h,2).subs(s0,r0**2))
    assert sp.simplify(pLfr_second_gap+4*r0**3*gu*u2)==0
    assert sp.simplify(pLf_second_gap+4*r0**4*u2.subs(s0,r0**2))==0
    return dict(u2=u2,u3=u3,gap0=coeff0,gap1=coeff1,gap2=coeff2,
                pLfr_second_gap=pLfr_second_gap,pLf_second_gap=pLf_second_gap,
                symbols=(h,s0,r0,u0,u1,gs,gu,gss,gsu,guu),
                mixed_reduced=mixed_reduced,cubic_reduced=cubic_reduced)


def rational_witness():
    d=identities()
    h,s0,r0,u0,u1,gs,gu,gss,gsu,guu=d['symbols']
    # Nonzero curvature, nonlinear G and G_U; all substitutions exact.
    vals={s0:sp.Rational(1,4),r0:sp.Rational(1,2),u0:sp.Rational(3,5),
          u1:sp.Rational(1,7),gs:sp.Rational(2,3),gu:-sp.Rational(3,2),
          gss:sp.Rational(5,4),gsu:sp.Rational(2,5),guu:sp.Rational(1,3)}
    u2v=sp.factor(d['u2'].subs(vals))
    return dict(u2=u2v,u3=sp.factor(d['u3'].subs(vals)),
                second_pLfr=sp.factor(d['pLfr_second_gap'].subs(vals)),
                second_pLf=sp.factor(d['pLf_second_gap'].subs(vals)),
                coeff2=sp.factor(d['gap2'].subs(vals)))


if __name__=='__main__':
    print(rational_witness())
