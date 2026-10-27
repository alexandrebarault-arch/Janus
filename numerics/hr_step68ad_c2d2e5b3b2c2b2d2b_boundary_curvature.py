"""Exact boundary-one-form curvature after HR shift elimination (regular K>0 chart).

This is an ambient-jet no-go for unrestricted coordinate-Dirichlet variations,
NOT a statement about Dirac-tangent variations or physical boundary data.
"""
import sympy as sp


def run_checks():
    Lg, Lf, Sg, Sf, Sgr, Sfr, N, M, mg, mf, K = sp.symbols(
        'Lg Lf Sg Sf Sgr Sfr N M mg mf K', positive=True)
    V, pLg, pLf, pSg, pLgr, pg, tgr = sp.symbols(
        'V pLg pLf pSg pLgr pg tgr', real=True)
    D = pSg*Sgr - Lg*pLgr + pg*tgr
    z = D/sp.sqrt(K**2 + D**2)  # K>0; the K<0 chart has opposite sign
    A = N + M*Lg/Lf
    Ag = 2*mg*N*Sg/Lg
    Af = 2*mf*M*Sf/Lf
    theta_pLg = -A*z - V*Lg
    theta_pLf = -V*Lf
    checks = 0

    def check(expr, target=0):
        nonlocal checks
        assert sp.simplify(expr-target) == 0, (expr, target)
        checks += 1

    check(sp.diff(z, pSg), Sgr*K**2/(K**2+D**2)**sp.Rational(3,2))
    check(sp.diff(z, pLgr), -Lg*K**2/(K**2+D**2)**sp.Rational(3,2))
    # dTheta(X,Y) = X[Theta(Y)] - Y[Theta(X)] for coordinate directions.
    c_sg = sp.diff(theta_pLg,pSg)  # Theta(dpSg)=0
    c_lgr = sp.diff(theta_pLg,pLgr)  # Theta(dpLg')=0
    check(c_sg, -A*Sgr*K**2/(K**2+D**2)**sp.Rational(3,2))
    check(c_lgr, A*Lg*K**2/(K**2+D**2)**sp.Rational(3,2))
    w = {Lg:2,Lf:3,Sg:5,Sf:7,Sgr:1,Sfr:1,N:1,M:1,
         mg:1,mf:1,K:3,V:0,pLg:2,pLf:3,pSg:4,pLgr:0,pg:1,tgr:0}
    check(D.subs(w),4)
    check(z.subs(w),sp.Rational(4,5))
    check(c_sg.subs(w),-sp.Rational(3,25))
    check(c_lgr.subs(w),sp.Rational(6,25))
    check((c_lgr.subs({Sgr:0})), A*Lg*K**2/(K**2+D.subs({Sgr:0})**2)**sp.Rational(3,2))

    # A restricted, fixed-multiplier polarization does admit an exact primitive.
    # Fix all six coordinates, pLg, and N,M,V; leave Sg', Sf', pLf free.
    C_fix_pLg = -Ag*Sgr-Af*Sfr+V*Lf*pLf
    check(sp.diff(C_fix_pLg,Sgr),-Ag)
    check(sp.diff(C_fix_pLg,Sfr),-Af)
    check(sp.diff(C_fix_pLg,pLf),-theta_pLf)
    check(sp.diff(C_fix_pLg,pSg),0)

    # Alternatively fix z* itself as a boundary datum and keep pLg free.
    Z=sp.symbols('Z',real=True)
    C_fix_z = -Ag*Sgr-Af*Sfr+(A*Z+V*Lg)*pLg+V*Lf*pLf
    check(sp.diff(C_fix_z,Sgr),-Ag)
    check(sp.diff(C_fix_z,Sfr),-Af)
    check(sp.diff(C_fix_z,pLg),-(-A*Z-V*Lg))
    check(sp.diff(C_fix_z,pLf),-theta_pLf)
    check(sp.diff(C_fix_z,Z),A*pLg)  # nonzero if z* is allowed to vary
    check((A*pLg*sp.diff(z,pSg)).subs(w),sp.Rational(6,25))
    check(sp.diff(Ag,N),2*mg*Sg/Lg)  # lapse variation needs additional treatment
    check(sp.diff(Af,M),2*mf*Sf/Lf)
    print('EXACT_SYMPY_ASSERTIONS_PASS',checks,'FAIL',0)
    print('WITNESS_D',D.subs(w),'WITNESS_Z',z.subs(w))
    print('CURVATURE_pSg_pLg',c_sg.subs(w))
    print('CURVATURE_pLgr_pLg',c_lgr.subs(w))
    return checks


if __name__ == '__main__':
    run_checks()
