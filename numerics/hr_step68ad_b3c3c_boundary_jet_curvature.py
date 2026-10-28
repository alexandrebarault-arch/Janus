"""b3c3c: restricted endpoint-jet non-integrability of the original
Step45 post-IBP lapse generator after positive-K algebraic shift reduction.
This is NOT a physical Dirac obstruction: endpoint jets need not be admissible
variations tangent to all functional constraints or boundary conditions.

Run: python hr_step68ad_b3c3c_boundary_jet_curvature.py
Original Step45 source Git blob: 66aa43841dccfe4a5d586a49be9c10af3a67a10e
"""
import json
import sympy as s

Lg,Lf,pLg,pLgr,Sg,Sgr,Sf,Sfr,pSg,pg,tgr=s.symbols(
    'Lg Lf pLg pLgr Sg Sgr Sf Sfr pSg pg tgr', real=True)
mg,mf,m2,N,M,Nr,Mr=s.symbols('mg mf m2 N M Nr Mr', real=True)
z,zr=s.symbols('z zr',real=True)
b1,b2,b3=s.symbols('b1 b2 b3',real=True)
K=m2*mg*Lg*Lf*(b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2)
D=pSg*Sgr-Lg*pLgr+pg*tgr
# Extract only the original Step45 terms that contain radial derivatives
# of pLg or of the auxiliary relative shift z. All other Step45 terms are
# independent of pLgr and zr, and cannot contribute to these two coefficients.
Ag_dep=zr*pLg
Af_dep=pLg*(zr*Lg/Lf+z*s.Symbol('Lgr')/Lf-z*Lg*s.Symbol('Lfr')/Lf**2)
Bg_dep=z*pLg
Bf_dep=z*Lg*pLg/Lf
F_dep=N*Ag_dep+M*Af_dep+Nr*Bg_dep+Mr*Bf_dep
alpha_z=s.diff(F_dep,zr)
alpha_pLg=s.diff(F_dep,pLgr)
# Fz=0 and K>0, z*=D/sqrt(D^2+K^2), exact derivative.
Z=D/s.sqrt(D**2+K**2)
ZD=K**2/(D**2+K**2)**s.Rational(3,2)
alpha_pLgr=s.factor(alpha_z*s.diff(Z,pLgr))
# Restrict all other endpoint jets (and lapse values/jets) to constants.
# The resulting 1-form is alpha=alpha_pLgr d(pLgr), alpha_pLg=0.
curvature=s.factor(s.diff(alpha_pLgr,pLg)-s.diff(alpha_pLg,pLgr))
expected=-Lg*(N+M*Lg/Lf)*K**2/(D**2+K**2)**s.Rational(3,2)

def run():
    checks={
      'zprime_coefficient':s.simplify(alpha_z-pLg*(N+M*Lg/Lf)),
      'pLgprime_direct_coefficient':alpha_pLg,
      'D_independent_pLg_value':s.diff(D,pLg),
      'D_derivative_pLgprime':s.diff(D,pLgr)+Lg,
      'K_independent_pLg_value':s.diff(K,pLg),
      'K_independent_pLgprime':s.diff(K,pLgr),
      'Z_derivative_pLgprime':s.simplify(s.diff(Z,pLgr)+Lg*ZD),
      'alpha_pLgprime_chain_rule':s.simplify(alpha_pLgr+Lg*pLg*(N+M*Lg/Lf)*ZD),
      'restricted_curvature':s.simplify(curvature-expected),
      'curvature_independent_pLg':s.diff(curvature,pLg),
      'curvature_independent_lapse_derivatives_N':s.diff(curvature,Nr),
      'curvature_independent_lapse_derivatives_M':s.diff(curvature,Mr),
    }
    for name,res in checks.items():
        assert res==0,(name,res)
    # Rational witness for D=3, K=4, Lg=2/5, Lf=3/5, N=M=1.
    vals={Lg:s.Rational(2,5),Lf:s.Rational(3,5),N:1,M:1,
          K:s.Integer(4),D:s.Integer(3)}
    # Direct substitution into the reduced analytic formula, not a Step55 point.
    w=s.simplify(expected.subs(vals))
    assert w==-s.Rational(32,375),w
    assert s.simplify((pLg*expected).subs(vals).subs(pLg,2))==-s.Rational(64,375)
    assert s.simplify(w)<0
    return {'exact_sympy_assertions':len(checks)+3,
            'restricted_boundary_curvature':'-Lg*(N+M*Lg/Lf)*K**2/(D**2+K**2)**(3/2)',
            'strictly_negative_if':'Lg,Lf,N,M,K positive, D finite',
            'rational_witness_non_Step55':'-32/375',
            'scope':'unrestricted endpoint jet slice (pLg,pLgprime), fixed remaining fields and lapse jets; positive K',
            'limits':'NOT a Dirac-tangent or admissible boundary slice; no physical no-go, no improved generator proven',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
