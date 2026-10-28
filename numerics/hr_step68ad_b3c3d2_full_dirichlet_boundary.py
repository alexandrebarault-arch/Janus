"""b3c3d2: full original non-IBP boundary form on fixed-coordinate Dirichlet jets.

Algebraic, unconstrained endpoint result only; not physical Dirac tangency.
Sources: Step37 blob 005449ade6e3582e3b9a5c3374a881a77e73e3f6;
Step45 blob 66aa43841dccfe4a5d586a49be9c10af3a67a10e;
previous six-pair non-IBP audit blob 94bd7e089ebb0978569361c03a4f3ab950b950df.
"""
import json
import sympy as s

Lg,Lf,Sg,Sf,N,M,mg,mf,K=s.symbols('Lg Lf Sg Sf N M mg mf K',positive=True)
Nr,Mr,V=s.symbols('Nr Mr V',real=True)
p,pr,pf,ps,pg,psf,psfr,tfp,tgp,Sgr,Sfr,Sg2,Sf2,Lgr,Lfr,z=s.symbols(
    'p pr pf ps pg psf psfr tfp tgp Sgr Sfr Sg2 Sf2 Lgr Lfr z',real=True)
Q=N/Lg+M/Lf
a=N+M*Lg/Lf
D=ps*Sgr-Lg*pr+pg*tgp
Df=psf*Sfr-Lf*psfr+pf*tfp
Z=D/s.sqrt(D**2+K**2)
P=a*p
curvg=mg*(-Lg+Sgr**2/Lg+2*Sg*Sg2/Lg-2*Sg*Sgr*Lgr/Lg**2)
curvf=mf*(-Lf+Sfr**2/Lf+2*Sf*Sf2/Lf-2*Sf*Sfr*Lfr/Lf**2)
F=N*(curvg+pg*s.sqrt(1+(tgp/Lg)**2))+M*(curvf+pf*s.sqrt(1+(tfp/Lf)**2))
F+=z*Q*D+V*(D+Df)+Q*K*s.sqrt(1-z*z)

def boundary():
    # Euler endpoint coefficients for second-derivative curvature terms.
    dSg2=s.diff(F,Sg2);dSf2=s.diff(F,Sf2)
    Dt_g=s.diff(dSg2,N)*Nr+s.diff(dSg2,Sg)*Sgr+s.diff(dSg2,Lg)*Lgr
    Dt_f=s.diff(dSf2,M)*Mr+s.diff(dSf2,Sf)*Sfr+s.diff(dSf2,Lf)*Lfr
    return {"Sgr":dSg2,"Sfr":dSf2,"Sg":s.diff(F,Sgr)-Dt_g,
            "Sf":s.diff(F,Sfr)-Dt_f,"Lg":s.diff(F,Lgr),"Lf":s.diff(F,Lfr),
            "p":s.diff(F,pr),"pf":s.diff(F,psfr),
            "tg":s.diff(F,tgp),"tf":s.diff(F,tfp)}

A=2*mg*N*Sg/Lg
B=2*mf*M*Sf/Lf
C=A*Sgr+B*Sfr-V*Lg*p-V*Lf*pf


def run():
    c=boundary()
    expected={"Sgr":A,"Sfr":B,
              "Sg":-2*mg*Nr*Sg/Lg+(z*Q+V)*ps,
              "Sf":-2*mf*Mr*Sf/Lf+V*psf,
              "Lg":-2*mg*N*Sg*Sgr/Lg**2,
              "Lf":-2*mf*M*Sf*Sfr/Lf**2,
              "p":-z*a-V*Lg,"pf":-V*Lf,
              "tg":pg*(N*tgp/(Lg**2*s.sqrt(1+(tgp/Lg)**2))+z*Q+V),
              "tf":pf*(M*tfp/(Lf**2*s.sqrt(1+(tfp/Lf)**2))+V)}
    checks={"endpoint_"+k:s.simplify(c[k]-v) for k,v in expected.items()}
    checks['shift_stationarity']=s.simplify(s.diff(F,z)-Q*(D-K*z/s.sqrt(1-z*z)))
    # Fixed canonical configuration q=(Lg,Sg,tg,Lf,Sf,tf), fixed N,M,V.
    # Other endpoint momenta and first jets are independent ambient variables.
    theta={Sgr:A,Sfr:B,p:(-z*a-V*Lg).subs(z,Z),pf:-V*Lf}
    for v in (Sgr,Sfr,p,pf,pr,ps,pg,tgp,psf,tfp):
        checks['dirichlet_'+str(v)]=s.simplify(theta.get(v,0)-s.diff(C,v)+Z*s.diff(P,v))
    checks['free_curvature']=s.simplify(s.diff(P,p)*s.diff(Z,pr)+a*Lg*K**2/(D**2+K**2)**s.Rational(3,2))
    checks['rank_equivalence']=s.simplify(s.diff(P,p)*s.diff(Z,pr)-s.diff(P,pr)*s.diff(Z,p)+a*Lg*K**2/(D**2+K**2)**s.Rational(3,2))
    c0,c1,c2=s.symbols('c0 c1 c2',real=True)
    graph=c0+c1*P+c2*P**2
    primitive=C-(c0*P+c1*P**2/2+c2*P**3/3)
    checks['graph_primitive_p']=s.simplify(s.diff(primitive,p)-(-V*Lg-a*graph))
    checks['graph_primitive_Sgr']=s.simplify(s.diff(primitive,Sgr)-A)
    checks['graph_primitive_Sfr']=s.simplify(s.diff(primitive,Sfr)-B)
    checks['graph_primitive_pf']=s.simplify(s.diff(primitive,pf)+V*Lf)
    checks['graph_realization']=s.simplify((1-graph**2)*(K*graph/s.sqrt(1-graph**2))**2-K**2*graph**2)
    checks['lapse_cross_curvature']=s.simplify(s.diff(A,N)-2*mg*Sg/Lg)
    for name,residual in checks.items():
        if residual!=0:raise AssertionError((name,residual))
    assert s.simplify(s.diff(P,p)*s.diff(Z,pr)).subs({Lg:s.Rational(2,5),Lf:s.Rational(3,5),N:1,M:1,K:4,D:3})==-s.Rational(32,375)
    assert s.diff(A,N).subs({mg:1,Sg:1,Lg:1})==2
    return {'exact_symbolic_zero_residuals':len(checks), 'rational_witnesses':2,
            'theta_dirichlet':'dC-Z dP; C=A Sgprime+B Sfprime-V Lg pLg-V Lf pLf',
            'curvature_dirichlet':'dP wedge dZ',
            'closed_iff':'rank(d(P,Z)) <=1 on fixed-q, fixed-lapse endpoint submanifold',
            'lapse_variation_caveat':'dTheta(dN,dSgprime)=2 mg Sg/Lg, not covered by rank criterion',
            'original_step45_55_58_import_replay':False,
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(run(),indent=2))
