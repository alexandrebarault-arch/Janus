"""JANUS 68ad-C2d2e5b3a: exact K=0 shift-chart audit.

This is a finite-dimensional pointwise algebraic lemma, NOT a full
functional Poisson/Dirac matrix, nor a solution of the Step55 ODE.
Original Step55 geometry SHA: a6e7004120d0a166a3a8973c2fbe1487a8eb70fe.
Original Step68o shell SHA: c99caebc17f243784450ddff94fb061767e6d8e7.
"""
from fractions import Fraction as F
import json
import sympy as sp

A=F('0.4'); Y=F('0.5787707228025044'); B=A*Y
CG=F('0.0015'); CF=F('-0.0012')
B1=F('1'); B2=F('-4.2383993109'); B3=F('13.6801214252')
M2=F('23.3348939346'); MG=F(1); Z1=F('0.004')
SMAX=F(289,400); RMAX=F(17,20)

def rational_chart_bounds():
    """Outward elementary rational lower bound on k=K/r^2.

    y=Lf/Lg lies in [ylo,Y]. With B2<0,B3>0, the independent
    lower enclosure 1+2 B2*Y+B3*ylo^2 bounds T/Lg^2.
    """
    ylo=Y*(1+CF*SMAX)**2/(1+CG*SMAX)**2
    tlo=B1+2*B2*Y+B3*ylo**2
    lflo=B*(1+CF*SMAX)**2
    klo=M2*MG*A*lflo*A**2*tlo
    assert 0<ylo<=Y and tlo>0 and klo>0
    return {'r_domain':['0','17/20'], 'y_lower':str(ylo),
            'y_upper':str(Y),'T_over_Lg_squared_lower':str(tlo),
            'K_over_r_squared_lower':str(klo),
            'K_over_r_squared_lower_decimal':format(float(klo),'.12f'),
            'max_abs_z':str(RMAX*Z1)}

def physical_k(s):
    s=F(s)
    assert 0<=s<=SMAX
    lg=A*(1+CG*s)**2;lf=B*(1+CF*s)**2
    t=B1*lg**2+2*B2*lg*lf+B3*lf**2
    return M2*MG*lg*lf*t

def exact_symbolic_checks():
    K,D,z,k,r,a,eps=sp.symbols('K D z k r a eps',real=True)
    root=sp.sqrt(1-z*z)
    f=D*z+K*root
    fz=sp.diff(f,z)
    checks={}
    checks['shift_stationarity']=sp.simplify(fz-(D-K*z/root))==0
    zp=D/sp.sqrt(K*K+D*D)
    zn=-zp
    kp=sp.symbols('kp',positive=True)
    checks['positive_K_root']=sp.simplify(fz.subs({K:kp,z:D/sp.sqrt(kp*kp+D*D)}, simultaneous=True))==0
    checks['negative_K_root']=sp.simplify(fz.subs({K:-kp,z:-D/sp.sqrt(kp*kp+D*D)}, simultaneous=True))==0
    checks['negative_K_wrong_sign']=sp.simplify(fz.subs({K:-3,D:4,z:sp.Rational(4,5)}))==8
    checks['positive_K_extremum']=sp.simplify(f.subs({K:3,D:4,z:sp.Rational(4,5)}))==5
    checks['negative_K_extremum']=sp.simplify(f.subs({K:-3,D:4,z:sp.Rational(-4,5)}))==-5
    checks['implicit_derivative']=sp.simplify(sp.diff(zp,D)-K*K/(K*K+D*D)**sp.Rational(3,2))==0
    checks['ray_z_3_4']=sp.simplify(zp.subs({K:3*eps,D:4*eps}, simultaneous=True).subs(eps,1))==sp.Rational(4,5)
    checks['ray_z_1_0']=sp.simplify(zp.subs({K:eps,D:0}, simultaneous=True).subs(eps,1))==0
    checks['ray_derivative_diverges']=sp.simplify((sp.diff(zp,D)*eps).subs({K:3*eps,D:4*eps}, simultaneous=True).subs(eps,1))==sp.Rational(9,125)
    zphys=r*a
    Kphys=r*r*k
    Dphys=r**3*k*a/sp.sqrt(1-r*r*a*a)
    checks['physical_path_Fz']=sp.simplify(fz.subs({K:Kphys,D:Dphys,z:zphys}, simultaneous=True))==0
    checks['physical_path_zprime']=sp.diff(zphys,r)==a
    checks['physical_path_zsecond']=sp.diff(zphys,r,2)==0
    checks['K_zero_D_nonzero_no_root']=sp.simplify(fz.subs({K:0,D:1}))==1
    checks['origin_shift_flat']=sp.simplify(fz.subs({K:0,D:0}))==0
    checks['origin_implicit_rank_zero']=sp.simplify(sp.diff(fz,z).subs({K:0,D:0}))==0
    if not all(checks.values()):raise AssertionError({x:v for x,v in checks.items() if not v})
    return checks

def manifest():
    bounds=rational_chart_bounds()
    checks=exact_symbolic_checks()
    samples=[F(0),F(1,4096),F(1,1024),SMAX]
    klo=F(bounds['K_over_r_squared_lower'])
    sample_values=[{'s':str(s),'k':str(physical_k(s)),
                    'k_gt_rational_lower':physical_k(s)>=klo} for s in samples]
    assert all(x['k_gt_rational_lower'] for x in sample_values)
    return {'step':'68ad-C2d2e5b3a','kind':'EXACT_POINTWISE_K_ZERO_CHART_AND_PHYSICAL_PATH_GUARD',
      'original_blobs_read_not_executed':{
       'numerics/hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe',
       'numerics/hr_step68o_temporal_interval_annulus.py':'c99caebc17f243784450ddff94fb061767e6d8e7'},
      'rational_bounds':bounds,'symbolic_checks':checks,'sample_checks':sample_values,
      'theorem':'K>0 for 0<r<=17/20 on prescribed Step55 geometry; K=D=0 at center. z*=D/sqrt(K^2+D^2) has no continuous ambient extension at origin (different rays), and its derivative diverges along rays; the prescribed smooth shell D=r^3*k*Z1/sqrt(1-r^2*Z1^2) has z=r*Z1 and a unique pathwise limit 0.',
      'not_proved':['Step55 U(s) solution or full on-shell Poisson/Dirac matrix',
                    'Dirac rank, tertiary constraints, boundary admissibility',
                    'extension of reduced shift chart through arbitrary K=D=0 configurations',
                    '4D dynamics, stability, observables'],
      'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':print(json.dumps(manifest(),indent=2))
