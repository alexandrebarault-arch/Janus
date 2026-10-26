"""Exact shift-shell consistency of Step68o's explicit Step55 canonical profile.

Independent algebraic replay of the *formulas* in SHA-pinned originals:
Step55 a6e7004120d0a166a3a8973c2fbe1487a8eb70fe;
Step68o c99caebc17f243784450ddff94fb061767e6d8e7;
Step58 802c23aebd41780d8c462f1aa1711707fe4ee88f.
This does not execute the full Step58 or Step60 operator.
"""
import sympy as sp


def identities():
    r = sp.symbols('r', positive=True)
    a,b,cg,cf,pg,kg,z1,m2,mg,b1,b2,b3 = sp.symbols(
        'a b cg cf pg kg z1 m2 mg b1 b2 b3', real=True)
    s = r*r
    lg = a*(1+cg*s)**2
    lf = b*(1+cf*s)**2
    sgr = a*(1+cg*s)*(1+5*cg*s)
    gmom = pg*(1+sp.Rational(5,2)*cg*s)
    gprime = 2*pg*(1+5*cg*s)
    rhog = sp.Symbol('rhog', real=True)  # Arbitrary: cancels identically.
    t = b1*lg**2 + 2*b2*lg*lf + b3*lf**2
    k = m2*mg*lg*lf*t
    dbar = k*z1/sp.sqrt(1-z1*z1*s)
    psg = (s*dbar+lg*gprime-rhog*s*kg*lg)/sgr
    # Original canonical fields: Sg=r Lg, pSg=r Psg,
    # pLg=r² Gmom, pg_dust=r² Rhog, tg'=r kg Lg.
    D = sp.expand(r*psg*sp.diff(r*lg,r)-lg*sp.diff(s*gmom,r)
                  +s*rhog*(r*kg*lg))
    K = m2*mg*lg*lf*(b1*(r*lg)**2+2*b2*(r*lg)*(r*lf)+b3*(r*lf)**2)
    # Factor before expensive rational cancellation.
    assert sp.simplify(sp.diff(r*lg,r)-sgr) == 0
    assert sp.simplify(sp.diff(s*gmom,r)-r*gprime) == 0
    assert sp.cancel(D-r**3*dbar) == 0
    assert sp.cancel(K-r**2*k) == 0
    # Avoid unlicensed sqrt(k²)=k: identity at squared level first.
    assert sp.cancel((D*D+K*K)*(1-z1*z1*s)-r**4*k*k) == 0
    z = r*z1
    # The physical Fz=0 equation is D-K*z/sqrt(1-z²)=0
    # on k>0, 1-z²>0, r>0. This is exact by D=r³ dbar, K=r²k.
    assert sp.cancel(D-K*z/sp.sqrt(1-z*z)) == 0
    assert sp.diff(z,r)==z1
    assert sp.diff(z,r,2)==0
    assert sp.diff(z,r,3)==0
    # Shift quotient, when k>0 and sqrt positive, is exactly z.
    return {'r':r,'s':s,'K':K,'k':k,'D':D,'dbar':dbar,'z':z,'z1':z1,
            'rhog':rhog,'pSg':psg,'Lg':lg,'Lf':lf,'T':t}


def counterexample_negative_k():
    """If k<0, the principal positive sqrt reverses the sign of D/R."""
    from fractions import Fraction as F
    r=F(1,32); z1=F(1,250); k=F(-1)
    # D=r³*k*z1/sqrt(1-z1²*r²), K=r²*k.
    # Hence D/sqrt(D²+K²) = -r*z1 for negative k.
    assert k<0
    return {'sign_of_D_over_root':-1,'sign_of_r_z1':1,'r':str(r)}


def manifest():
    identities()
    return {'step':'68ad-C2d2b-shift-shell-exact',
            'kind':'CONDITIONAL_EXACT_PHYSICAL_PROFILE_SHIFT_SHELL',
            'identities':['D=r^3 Dbar','K=r^2 k',
                          '(D^2+K^2)(1-z1^2 r^2)=r^4 k^2',
                          'Fz(r*z1)=0','z=r*z1','zprime=z1',
                          'zsecond=0','zthird=0'],
            'assumptions':['r>0','k>0','1-z1^2*r^2>0',
                           'Step55/68o canonical formulas are the physical profile'],
            'original_sources_executed':False,
            'Step58_7_cells':'NOT_EXECUTED', 'Step60_quotient':'NOT_EXECUTED',
            'new_temporal_signs':0,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
    import json
    print(json.dumps(manifest(),indent=2))
