"""Exact Step55 primary-shell audit by independent algebraic transcription.

The formula for H_g is the Step45 A_g - d_r B_g (not Step58's full
operator). The Step55 pLf ODE is NOT solved here; H_g and F_z do not
require its value. This does not certify C=0, H_f=0, temporal lower
coefficients or positive global lapses.
"""
from fractions import Fraction
import sympy as sp

SOURCE_BLOBS = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
    'numerics/hr_step58_temporal_operator.py': '802c23aebd41780d8c462f1aa1711707fe4ee88f',
}

def exact_shell():
    r=sp.symbols('r',positive=True)
    a,b,cg,cf,kg,z1,mg,m2,pg0=sp.symbols('a b cg cf kg z1 mg m2 pg0',positive=True)
    b0,b1,b2,b3=sp.symbols('b0 b1 b2 b3',real=True)
    s=r*r
    ug=1+cg*s; uf=1+cf*s
    Lg=a*ug**2; Lf=b*uf**2; Sg=r*Lg; Sf=r*Lf
    Sgr=sp.diff(Sg,r); Lgr=sp.diff(Lg,r)
    Rg=-48*cg/(a*a*ug**5)
    Gmom=pg0*(1+sp.Rational(5,2)*cg*s)
    Gprime=2*pg0*(1+5*cg*s)
    pLg=s*Gmom
    T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2
    T0=b0*Lg**2+2*b1*Lg*Lf+b2*Lf**2
    z=r*z1; root=sp.sqrt(1-z*z)
    Dbar=m2*mg*Lg*Lf*T*z1/root
    Wgbar=m2*mg*(Lg*T0+Lf*T*root)
    fac=Gmom/(2*mg*Lg*Sgr)
    betag=sp.sqrt(1+kg*kg*s)
    numerator=Gmom**2/(4*mg*Lg)-fac*(s*Dbar+Lg*Gprime)-mg*Lg**3*Rg/2+s*z1*Dbar/Lg+Wgbar
    Rhog=-numerator/(betag+s*fac*kg*Lg)
    Psg=(s*Dbar+Lg*Gprime-Rhog*s*kg*Lg)/Sgr
    pSg=r*Psg; pg=s*Rhog; tgr=r*kg*Lg
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    K=m2*mg*Lg*Lf*At
    D=pSg*Sgr-Lg*sp.diff(pLg,r)+pg*tgr
    # Original Step45: H_g=A_g - d_r B_g; radial geometric and shift pieces
    kgrav=Lg*pLg**2/(4*mg*Sg**2)-pLg*pSg/(2*mg*Sg)
    Ag=kgrav+pg*betag-mg*Lg-mg*Sgr**2/Lg+s*Wgbar+z*(pSg*Sgr+pg*tgr)/Lg+z1*pLg
    Bg=-2*mg*Sg*Sgr/Lg+z*pLg
    Hg=Ag-sp.diff(Bg,r)
    # Intermediate algebraic identities prove the cancellation without a
    # high-cost expansion of the full symbolic physical expressions.
    checks={
      'Sgprime':sp.factor(Sgr-a*ug*(1+5*cg*s)),
      'pLgprime':sp.factor(sp.diff(pLg,r)-r*Gprime),
      'radial_curvature':sp.factor(-Lg-Sgr**2/Lg+2*sp.diff(Sg*Sgr/Lg,r)+s*Lg**3*Rg/2),
      'D_shift':sp.factor(D-r*s*Dbar),
      'K_shift':sp.factor(K-s*m2*mg*Lg*Lf*T),
      'Fz':sp.factor(D-K*z/root),
      'Hg':sp.factor(Hg),
      'Hg_div_s':sp.factor(Hg/s),
    }
    assert all(v==0 for v in checks.values()), {k:str(v)[:300] for k,v in checks.items() if v!=0}
    # This is a separate structural identity previously certified by
    # ORIGINAL Step58: E_M|Fz=0=0; E_N|Fz=0=(z^2-1)Hg/(Lg Lf).
    EN=(z*z-1)*Hg/(Lg*Lf)
    assert sp.factor(EN)==0
    eps=sp.symbols('eps',real=True)
    # Negative controls: a perturbed canonical momentum spoils Fz, while
    # a perturbed dust momentum spoils Hg (holding pSg fixed).
    shift_fault=sp.factor((D+eps*r*Sgr)-K*z/root)
    dust_fault=sp.factor(Ag-sp.diff(Bg,r))+eps*s*betag
    assert sp.factor(shift_fault-eps*r*Sgr)==0 and shift_fault!=0
    assert sp.factor(dust_fault-eps*s*betag)==0 and dust_fault!=0
    R=sp.Rational(17,20)
    aval=sp.Rational(2,5);bval=aval*sp.Rational('0.5787707228025044')
    outer_factor=sp.factor(((z*z-1)/(Lg*Lf)).subs({r:R,a:aval,b:bval,cg:sp.Rational('0.0015'),cf:sp.Rational('-0.0012'),z1:sp.Rational('0.004')}))
    assert -11<outer_factor<-10
    return {'identities':list(checks), 'exact_residuals_zero':len(checks)+1,'negative_controls':2,
            'outer_factor':str(outer_factor),'outer_factor_sign':'-11<factor<-10',
            'physical_scope':'Fz=Hg=0 exact on transcribed Step55 prescribed geometry; E_N=E_M=0 follows from authentic Step58 highjet certificate; no original full Step58 execution this run',
            'source_blobs':SOURCE_BLOBS,'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 import json
 print(json.dumps(exact_shell(),indent=2))
