"""68ad-C2d2e2: independent exact Step45/46/55/68o shell composition audit.

This is a RECONSTRUCTION of explicitly SHA-pinned original formulas, not an
execution of the original modules. It proves the stated identities under the
same smooth positive-chart assumptions; it is not a Dirac rank or lapse proof.
"""
from __future__ import annotations
import json
import sympy as sp

SOURCE_BLOBS = {
    'numerics/hr_step45_exact_physical_ward.py': '66aa43841dccfe4a5d586a49be9c10af3a67a10e',
    'numerics/hr_step46_exact_secondary_ode.py': 'bac025c28dbe1561c0c36c56dbfda46dc326f804',
    'numerics/hr_step55_normalized_secondary.py': 'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
    'numerics/hr_step55_global_barrier.py': 'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
    'numerics/hr_step68o_temporal_interval_annulus.py': 'c99caebc17f243784450ddff94fb061767e6d8e7',
    'numerics/hr_step68j_BN_exact_secondary_identity.py': 'a500cdb1a09c853d46848719e26be9bbec55fb64',
}

def assert_zero(expr, label):
    v=sp.cancel(sp.together(expr))
    if v != 0 and sp.simplify(v) != 0:
        raise AssertionError(f'{label}: {v}')
    return True

def curvature_geometry():
    r,a,c=sp.symbols('r a c', positive=True)
    L=a*(1+c*r**2)**2
    S=r*L
    R=2/S**2*(1-(sp.diff(S,r)/L)**2-2*S*sp.diff(S,r,2)/L**2+2*S*sp.diff(S,r)*sp.diff(L,r)/L**3)
    expected=-48*c/(a*a*(1+c*r*r)**5)
    assert_zero(R-expected,'original 3-curvature profile')
    return True

def original_primary_density_reduction():
    # Directly rebuild Step45 Ag,Bg,Af,Bf with arbitrary C^2 radial fields.
    r=sp.symbols('r',real=True)
    Lg,Sg,Lf,Sf,z,plg,psg,plf,psf,pg,pf,tg,tf=(sp.Function(k)(r) for k in
        ('Lg','Sg','Lf','Sf','z','pLg','pSg','pLf','pSf','pg','pf','tg','tf'))
    mg,mf,m2,b0,b1,b2,b3,b4=sp.symbols('mg mf m2 b0 b1 b2 b3 b4',nonzero=True)
    root=sp.sqrt(1-z*z)
    At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf
    A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf
    Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
    Wg=m2*mg*(Lg*A0+Lf*At*root)
    Wf=m2*mg*(Lf*Af+Lg*At*root)
    D=psg*sp.diff(Sg,r)-Lg*sp.diff(plg,r)+pg*sp.diff(tg,r)
    kg=Lg*plg**2/(4*mg*Sg**2)-plg*psg/(2*mg*Sg)
    kf=Lf*plf**2/(4*mf*Sf**2)-plf*psf/(2*mf*Sf)
    dustg=pg*sp.sqrt(1+sp.diff(tg,r)**2/Lg**2)
    dustf=pf*sp.sqrt(1+sp.diff(tf,r)**2/Lf**2)
    Ag=kg+dustg-mg*Lg-mg*sp.diff(Sg,r)**2/Lg+Wg+z*(psg*sp.diff(Sg,r)+pg*sp.diff(tg,r))/Lg+sp.diff(z,r)*plg
    Bg=-2*mg*Sg*sp.diff(Sg,r)/Lg+z*plg
    Afull=kf+dustf-mf*Lf-mf*sp.diff(Sf,r)**2/Lf+Wf+z*(psg*sp.diff(Sg,r)+pg*sp.diff(tg,r))/Lf
    Afull+=plg*(sp.diff(z,r)*Lg/Lf+z*sp.diff(Lg,r)/Lf-z*Lg*sp.diff(Lf,r)/Lf**2)
    Bf=-2*mf*Sf*sp.diff(Sf,r)/Lf+z*Lg*plg/Lf
    def scalar_curvature(L,S):
        return 2/S**2*(1-(sp.diff(S,r)/L)**2-2*S*sp.diff(S,r,2)/L**2+2*S*sp.diff(S,r)*sp.diff(L,r)/L**3)
    redg=kg+dustg-mg*Lg*Sg**2*scalar_curvature(Lg,Sg)/2+Wg+z*D/Lg
    redf=kf+dustf-mf*Lf*Sf**2*scalar_curvature(Lf,Sf)/2+Wf+z*D/Lf
    assert_zero(sp.expand(Ag-sp.diff(Bg,r)-redg),'Step45 Hg reduced identity')
    assert_zero(sp.expand(Afull-sp.diff(Bf,r)-redf),'Step45 Hf reduced identity')
    return True

def primary_shell_algebra():
    # Exact Step55 geometry definitions, but with independent reduced symbols
    # so the cancellations test the dust formulas rather than a numeric sample.
    s,Lg,Lf,Sgr,Sfr,Gmom,Gprime,Dbar,Rg,Rf,Wg,Wf,U,V,z1,mg,mf,kg,kf=sp.symbols(
        's Lg Lf Sgr Sfr Gmom Gprime Dbar Rg Rf Wg Wf U V z1 mg mf kg kf', real=True)
    rootg=sp.sqrt(1+s*kg**2);rootf=sp.sqrt(1+s*kf**2)
    facg=Gmom/(2*mg*Lg*Sgr)
    betag=rootg+s*facg*kg*Lg
    rhog=-(Gmom**2/(4*mg*Lg)-facg*(s*Dbar+Lg*Gprime)-mg*Lg**3*Rg/2+s*z1*Dbar/Lg+Wg)/betag
    psg=(s*Dbar+Lg*Gprime-rhog*s*kg*Lg)/Sgr
    reducedg=Gmom**2/(4*mg*Lg)-Gmom*psg/(2*mg*Lg)+rhog*rootg-mg*Lg**3*Rg/2+Wg+s*z1*Dbar/Lg
    facf=U/(2*mf*Lf*Sfr)
    betaf=rootf+s*facf*kf*Lf
    rhof=-(U**2/(4*mf*Lf)-facf*(-s*Dbar+Lf*V)-mf*Lf**3*Rf/2+s*z1*Dbar/Lf+Wf)/betaf
    psf=(-s*Dbar+Lf*V-rhof*s*kf*Lf)/Sfr
    reducedf=U**2/(4*mf*Lf)-U*psf/(2*mf*Lf)+rhof*rootf-mf*Lf**3*Rf/2+Wf+s*z1*Dbar/Lf
    assert_zero(reducedg,'Step55 g primary Hg/r^2')
    assert_zero(reducedf,'Step55 f primary Hf/r^2')
    # Fz stationarity is independent of either dust density once pSg is used.
    Dfromg=psg*Sgr-Lg*Gprime+rhog*s*kg*Lg
    assert_zero(Dfromg-s*Dbar,'Dg/r = s*Dbar')
    # Nonzero denominator is essential: do not silently prove existence.
    return {'Hg':True,'Hf':True,'Fz_Dg':True}

def stationary_shift_shell():
    r,z1,Lg,Lf,T,m2,mg=sp.symbols('r z1 Lg Lf T m2 mg',real=True)
    s=r*r
    root=sp.sqrt(1-s*z1*z1)
    k=m2*mg*Lg*Lf*T
    Dg=r**3*k*z1/root
    K=r*r*k
    z=r*z1
    assert_zero(Dg-K*z/sp.sqrt(1-z*z),'Step68o Fz=0')
    return True


def lapse_derivative_shell_composition():
    # These three identities are ORIGINAL, PREVIOUSLY PROVED (Step58/68h/68j).
    # This independent composition does not re-prove the underlying identities.
    z,Lg,Lf,Hg,Hgp,C,Fzp,beta=sp.symbols(
        'z Lg Lf Hg Hgp C Fzp beta',real=True)
    alpha=(1-z*z)/(Lg*Lf)
    N2=(z*z-1)*Hg/(Lg*Lf)
    M2=sp.S.Zero
    BN=-alpha*Hgp+beta*Hg+(z/Lg)*C
    BM=3*z*(z*z-1)/(Lg*Lf**2)*Fzp
    for name,expr in [('Nsecond',N2),('Msecond',M2),('Nfirst',BN),('Mfirst',BM)]:
        assert_zero(expr.subs({Hg:0,Hgp:0,C:0,Fzp:0}),name+' shell')
    # Negative control: imposing ONLY pointwise Hg=C=Fz=0 is insufficient.
    residual=BN.subs({Hg:0,C:0,Hgp:1})
    assert_zero(residual+alpha,'Hgprime not optional')
    assert residual!=0
    return {'vanishing_lapse_derivative_coefficients':4,
            'requires_Hgprime_and_Fzprime':True}


def secondary_ode_composition():
    # Step46 original: C=C0+C1 V, C1 != 0, V=pLf'(r).
    # Step55 original: G=V_rhs/r, pLf=r^2 U(s), 2s U_s=G-2U.
    r,s,U,Us,C0,C1=sp.symbols('r s U Us C0 C1',nonzero=True)
    V_rhs=-C0/C1
    G=V_rhs/r
    V_profile=r*(2*U+2*s*Us)
    assert_zero((C0+C1*V_profile).subs(Us,(G-2*U)/(2*s)),
                'Step46/55 C exact zero on physical ODE')
    # Negative control: arbitrary deviation from physical ODE gives C != 0.
    epsilon=sp.symbols('epsilon',nonzero=True)
    wrong=sp.factor((C0+C1*V_profile).subs(Us,(G-2*U)/(2*s)+epsilon))
    assert_zero(wrong-2*r*s*C1*epsilon,'off-ODE C obstruction')
    return {'C_on_ODE':True,'off_ODE_residual':'2*r*s*C1*epsilon'}

def dust_clock_primitives():
    # Step68o stores t_g=t_f=0 at EACH point, but t'_g,t'_f !=0.
    # Those pointwise values are NOT a single global scalar function.
    r,a,b,cg,cf,kg,kf=sp.symbols('r a b cg cf kg kf',real=True)
    def primitive(a,c,k):
        return k*a*(r*r/sp.Integer(2)+c*r**4/sp.Integer(2)+c*c*r**6/sp.Integer(6))
    for a0,c0,k0 in ((a,cg,kg),(b,cf,kf)):
        L=a0*(1+c0*r*r)**2
        tp=r*k0*L
        T=primitive(a0,c0,k0)
        assert_zero(sp.diff(T,r)-tp,'dust clock primitive')
        for n in (1,2,3):
            assert_zero(sp.diff(T,r,n)-sp.diff(tp,r,n-1),f'dust jet order {n}')
    return {'clock_primitives':2,'jet_orders_verified':3,
            'local_t_zero_not_global_if_k_nonzero':True}

def prolongation_logic():
    # For an analytic solution on an open radial interval, an identically
    # vanishing constraint has all derivatives identically zero. This is
    # CONDITIONAL on exact original shell, not a finite-grid inference.
    r=sp.symbols('r',real=True)
    h,c,f=(sp.Function(x)(r) for x in ('Hg','C','Fz'))
    zero={h:sp.S.Zero,c:sp.S.Zero,f:sp.S.Zero}
    for expr in (h,c,f):
        for n in (1,2,3):
            assert_zero(sp.diff(expr.subs(zero),r,n),'smooth prolongation')
    return True

def manifest():
    curvature_geometry();original_primary_density_reduction();primary_shell_algebra();stationary_shift_shell();lapse_derivative_shell_composition()
    secondary_ode_composition();dust_clock_primitives();prolongation_logic()
    return {'step':'68ad-C2d2e2','kind':'CONDITIONAL_EXACT_COMPOSITION_OF_AUTHENTIC_STEP45_46_55_68O_FORMULAS',
            'original_source_blobs_read_from_GitHub':SOURCE_BLOBS,
            'reproduces_original_modules_byte_for_byte':False,
            'verified_conditional':['Step45 unsmeared Hg/Hf equal curvature+dust+shift reduced forms',
                'Step55 dust definitions force Hg=Hf=0 algebraically for r>0',
                'Step55 g momentum definition gives Dg=r^3 Dbar and Fz=0 with positive shift root',
                'historical Step58/68h/68j identities composed with shell give four vanishing lapse derivative coefficients',
                'Step46 affine C plus Step55 ODE forces C=0 for C1!=0',
                'smooth exact shell implies Hgprime=Cprime=Fzprime=0',
                'Step68o dust clock jets admit explicit global primitives despite local t=0 placeholders'],
            'conditional_on':['Step46 original C affine and nonzero coefficient',
                'Step55 normalized G exactly Step46 V_rhs/r',
                'Step55 physical U(s) exactly solves ODE, not arbitrary interval box',
                'positive regular chart r>0, K>0, |z|<1 and nonzero dust denominators',
                'original Step68o jets are evaluations of smooth physical branch',
                'Step58/68h/68j historical exact lapse-jet identities are accepted as previously certified, not re-proved here'],
            'Step58_continuum':'INCOMPLETE','Dirac_rank':'NOT_PROVED',
            'lapse_boundary':'NOT_PROVED','4D_stability_observables':'NOT_PROVED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(manifest(),indent=2,ensure_ascii=False))
