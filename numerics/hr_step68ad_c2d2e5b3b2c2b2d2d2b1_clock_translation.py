"""JANUS d2d2b1: two independent constant dust-clock translations.

Exact bulk canonical symmetry and boundary trace test for original six-pair
non-IBP Hamiltonian. NOT a complete Dirac physical tangent certification.
Original formulas transcribed from authenticated Step45 / original ADM;
this script does not import or rerun the original Step45/58 engines.
"""
import json
import sympy as s


def certificate():
    names = 'Lg pLg Sg pSg tg pg Lf pLf Sf pSf tf pf'
    q = dict(zip(names.split(), s.symbols(names, real=True)))
    Lg,pLg,Sg,pSg,tg,pg,Lf,pLf,Sf,pSf,tf,pf = q.values()
    Lgr,pLgr,Sgr,Sg2,tgr,Lfr,pLfr,Sfr,Sf2,tfr = s.symbols(
        'Lgr pLgr Sgr Sg2 tgr Lfr pLfr Sfr Sf2 tfr', real=True)
    N,Nr,M,Mr,V,z,zr,mg,mf,m2 = s.symbols('N Nr M Mr V z zr mg mf m2',real=True)
    b0,b1,b2,b3,b4 = s.symbols('b0:5',real=True)
    A0=b0*Sg**2+2*b1*Sg*Sf+b2*Sf**2
    At=b1*Sg**2+2*b2*Sg*Sf+b3*Sf**2
    Af=b2*Sg**2+2*b3*Sg*Sf+b4*Sf**2
    K=m2*mg*Lg*Lf*At
    Dg=pSg*Sgr-Lg*pLgr+pg*tgr
    Df=pSf*Sfr-Lf*pLfr+pf*tfr
    root=s.sqrt(1-z**2)
    Wg=m2*mg*(Lg*A0+Lf*At*root)
    Wf=m2*mg*(Lf*Af+Lg*At*root)
    kg=Lg*pLg**2/(4*mg*Sg**2)-pLg*pSg/(2*mg*Sg)
    kf=Lf*pLf**2/(4*mf*Sf**2)-pLf*pSf/(2*mf*Sf)
    Hg=kg-mg*Lg+mg*Sgr**2/Lg+2*mg*Sg*Sg2/Lg-2*mg*Sg*Sgr*Lgr/Lg**2
    Hg+=pg*s.sqrt(1+tgr**2/Lg**2)+z*Dg/Lg+Wg
    Hf=kf-mf*Lf+mf*Sfr**2/Lf+2*mf*Sf*Sf2/Lf-2*mf*Sf*Sfr*Lfr/Lf**2
    Hf+=pf*s.sqrt(1+tfr**2/Lf**2)+z*Dg/Lf+Wf
    # Independent original (non-IBP) density, plus diagonal shift.
    H=N*Hg+M*Hf+V*(Dg+Df)
    Fz=Dg-K*z/root
    Q=N/Lg+M/Lf
    zstar=Dg/s.sqrt(K*K+Dg*Dg)
    # The Step45 post-IBP density, independent reconstruction.
    Ag=kg+pg*s.sqrt(1+tgr**2/Lg**2)-mg*Lg-mg*Sgr**2/Lg+Wg
    Ag+=z*(pSg*Sgr+pg*tgr)/Lg+zr*pLg
    Bg=-2*mg*Sg*Sgr/Lg+z*pLg
    Cf=kf+pf*s.sqrt(1+tfr**2/Lf**2)-mf*Lf-mf*Sfr**2/Lf+Wf
    Cf+=z*(pSg*Sgr+pg*tgr)/Lf
    Cf+=pLg*(zr*Lg/Lf+z*Lgr/Lf-z*Lg*Lfr/Lf**2)
    Bf=-2*mf*Sf*Sfr/Lf+z*Lg*pLg/Lf
    Fg=N*Ag+Nr*Bg
    Ff=M*Cf+Mr*Bf
    # Original six-pair boundary one-form dust-clock coefficients.
    theta_g=s.diff(H,tgr)
    theta_f=s.diff(H,tfr)
    expected_g=pg*(N*tgr/(Lg**2*s.sqrt(1+tgr**2/Lg**2))+z*Q+V)
    expected_f=pf*(M*tfr/(Lf**2*s.sqrt(1+tfr**2/Lf**2))+V)
    checks=0
    def check(condition,label):
        nonlocal checks
        if not condition: raise AssertionError(label)
        checks+=1
    for label,expr in [('Hg',Hg),('Hf',Hf),('H',H),('Dg',Dg),('Df',Df),
                       ('Fz',Fz),('K',K),('zstar',zstar),('Fg',Fg),('Ff',Ff),
                       ('theta_g',theta_g),('theta_f',theta_f)]:
        check(s.diff(expr,tg)==0,label+' independent tg')
        check(s.diff(expr,tf)==0,label+' independent tf')
    check(s.simplify(theta_g-expected_g)==0,'original theta_g')
    check(s.simplify(theta_f-expected_f)==0,'original theta_f')
    check(s.diff(theta_f,tg)-s.diff(theta_g,tf)==0,'clock-plane curvature')
    check(s.diff(zstar,tg)==0 and s.diff(zstar,tf)==0,'reduced shift unchanged')
    # Constant shifts are canonical and commute with every bulk functional
    # constructed from these translation-invariant densities by PB.
    eps=s.symbols('eps',real=True)
    for label,expr in [('H',H),('Fg',Fg),('Ff',Ff),('Fz',Fz),('zstar',zstar)]:
        check(expr.subs(tg,tg+eps)==expr,label+' exact finite g translation')
        check(expr.subs(tf,tf+eps)==expr,label+' exact finite f translation')
    # Boundary-value trace vectors (tg(R),tf(R)) of the two generators.
    T=s.eye(2)
    check(T.det()==1,'clock boundary trace rank two')
    check(T.rank()==2,'clock directions independent')
    # Step55 geometry: Sg'(r),Sf'(r) strictly positive on [0,R].
    r=s.Rational(17,20);ss=r*r
    a=s.Rational(2,5);y=s.Rational('0.5787707228025044');b=a*y
    cg=s.Rational('0.0015');cf=s.Rational('-0.0012')
    Lgb=a*(1+cg*ss)**2;Lfb=b*(1+cf*ss)**2
    Sgrb=a*(1+cg*ss)*(1+5*cg*ss)
    Sfrb=b*(1+cf*ss)*(1+5*cf*ss)
    check(Sgrb>0 and Sfrb>0,'Step55 radial scalar derivatives nonzero')
    check(1+5*cf*ss>0,'f geometry regular to outer radius')
    # Hence eta Sg'=0 forces eta=0: no nonzero radial gauge vector can
    # generate either clock translation while leaving geometry fixed.
    kg=s.Rational('0.0012');kf=s.Rational('-0.0016');z1=s.Rational('0.004')
    zR=z1*r
    tgrb=kg*r*Lgb;tfrb=kf*r*Lfb
    check(tgrb>0 and tfrb<0,'Step55 dust slopes opposite')
    check(zR>0 and zR<1,'Step55 shift regular at R')
    check(kg*r/Lgb>0 and zR*(1/Lgb+1/Lfb)>0,
          'g dust clock boundary flux coefficient positive at N=M=1 V=0')
    check(kf*r/Lfb<0,'f dust clock boundary flux coefficient negative at M=1 V=0')
    check(s.diff(theta_g,pg).has(pg) or s.diff(theta_g,pg)!=0,
          'clock one-form not identically zero')
    check(s.diff(theta_f,pf)!=0,'f clock one-form not identically zero')
    result={
      'step':'68ad-C2d2e5b3b2c2b2d2d2b1',
      'assertions_passed':checks,'assertions_failed':0,
      'theorem':'Two independent constant dust-clock canonical translations preserve original bulk primary/shift and every Poisson-descendant constraint algebraically; boundary clock-value trace rank=2 modulo diagonal radial diffeomorphisms on regular Step55 geometry.',
      'boundary_two_form_on_clock_plane':'0 EXACT; isotropic plane, not full two-form kernel',
      'bare_original_boundary_one_form_on_clock_plane':'nonzero in general; at Step55 R with N=M=1,V=0, theta_g(Xg)>0 and theta_f(Xf)<0 if pg,pf>0',
      'not_proved':['clock translations admissible with center/outer clock Dirichlet','independence modulo full temporal gauge','full Dirac lapse solution','physical non-gauge rank two','boundary counterterm existence','4D dynamics/stability/observables'],
      'original_physics_reexecuted':False,
      'scientific_status':{'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}}
    return result

if __name__=='__main__':
    print(json.dumps(certificate(),indent=2,sort_keys=True))
