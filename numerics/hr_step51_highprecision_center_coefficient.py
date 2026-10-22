"""Step51 arbitrary-precision leading center U1 from authentic Step45/46.

Compute G(s,U0)=pLf'(sqrt(s))/sqrt(s) on the exact-DECIMAL
spherical primary background at pLf=r² U0. For analytic G:
U1 = (partial_s G(0,U0))/5. Evaluate this as a high-precision
small-s extrapolation. This is *not* interval-certified; it is a
numerical coefficient study, not a global Dirac, ghost or lapse test.
"""
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
import hashlib
from pathlib import Path

GIT_BLOBS={
    "numerics/hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e",
    "numerics/hr_step46_exact_secondary_ode.py":"bac025c28dbe1561c0c36c56dbfda46dc326f804",
}

def verify_historical_providers(root=None):
    root=Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for path,expected in GIT_BLOBS.items():
        raw=(root/path).read_bytes()
        actual=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual!=expected:raise ValueError(f'historical source mismatch: {path}: {actual}')
    return GIT_BLOBS.copy()
import sympy as sp, mpmath as mp, json
from functools import lru_cache
@lru_cache(None)
def make_rhs():
 d=exact_f_momentum_ode();x=d['pLf_prime_rhs'];syms=sorted(x.free_symbols,key=str)
 return syms,sp.lambdify(syms,x,'mpmath',cse=True)

def data(rr):
 M=mp.mpf
 a=M('.4');y=M('.5787707228025044');b=a*y;mg=M(1);mf=M('.10879548725')**2;m2=M('23.3348939346');
 b0,b1,b2,b3,b4=map(M,('0','1','-4.2383993109','13.6801214252','-38.5117901844'))
 cg=M('.0015');cf=M('-.0012');z1=M('.004');kg=M('.0012');kf=M('-.0016')
 s=rr*rr; u_g=1+cg*s;u_f=1+cf*s
 h2=M('.9')/(3*a**3)+m2*(b0+3*b1*y+3*b2*y*y+b3*y**3)/3
 H=mp.sqrt(h2);Pg=-2*a*a*H;L_g=a*u_g**2;L_f=b*u_f**2;S_g=rr*L_g;S_f=rr*L_f
 Lgr=4*a*cg*rr*u_g; Lfr=4*b*cf*rr*u_f
 Sgr=a*u_g*(1+5*cg*s); Sfr=b*u_f*(1+5*cf*s)
 plg=Pg*s*(1+M('2.5')*cg*s);plgr=2*rr*(1+5*cg*s)*Pg
 tr_g=kg*rr*L_g;tr_f=kf*rr*L_f
 z=z1*rr;root=mp.sqrt(1-z*z)
 At=b1*S_g*S_g+2*b2*S_g*S_f+b3*S_f*S_f
 A0=b0*S_g*S_g+2*b1*S_g*S_f+b2*S_f*S_f
 Af=b2*S_g*S_g+2*b3*S_g*S_f+b4*S_f*S_f
 K=m2*mg*L_g*L_f*At; Dg=K*z/root
 Wg=m2*mg*(L_g*A0+L_f*At*root);Wf=m2*mg*(L_f*Af+L_g*At*root)
 Rg=-48*cg/(a*a*u_g**5); Rf=-48*cf/(b*b*u_f**5)
 fac=plg/(2*mg*S_g*Sgr);kin=L_g*plg*plg/(4*mg*S_g*S_g)
 curvature=-mg*L_g*S_g*S_g*Rg/2
 numerator=kin-fac*(Dg+L_g*plgr)+curvature+z*Dg/L_g+Wg
 beta=mp.sqrt(1+(tr_g/L_g)**2)+fac*tr_g
 pg=-numerator/beta
 psg=(Dg+L_g*plgr-pg*tr_g)/Sgr
 U0=mf*b*(Pg/(mg*a)-2*z1)
 q={'Lg':L_g,'Lf':L_f,'Sg':S_g,'Sf':S_f,'pLg':plg,'pLf':s*U0,
    'pSg':psg,'pg':pg,'Lgr':Lgr,'Lfr':Lfr,'Sgr':Sgr,'Sfr':Sfr,
    'pLgr':plgr,'tgr':tr_g,'tfr':tr_f,
    'Mg2':mg,'Mf2':mf,'m2':m2,'beta0':b0,'beta1':b1,'beta2':b2,'beta3':b3,'beta4':b4,
    'z':z,'zr':z1,'zrr':M(0),'Dg_original':Dg,'Wf_original':Wf,'R3f_original':Rf}
 return q,U0

def calculation(dps=90):
 if not isinstance(dps,int) or dps<50 or dps>200:raise ValueError('50..200 decimal digits required')
 verify_historical_providers()
 mp.mp.dps=dps
 syms,fn=make_rhs()
 out=[]
 for k in (2,3,4,5,6,7,8,9,10,11):
  r=mp.mpf(10)**(-k)
  q,U0=data(r)
  missing=[str(s) for s in syms if str(s) not in q]
  if missing:raise RuntimeError('Missing RHS symbols '+str(missing))
  v=fn(*[q[str(s)] for s in syms]); F1=(v/r-2*U0)/(r*r)
  out.append({'k':k,'estimate':mp.nstr(F1/5,55)})
 return out

def richardson_u1_at_decade(k=8,dps=100):
    """Cancel the leading O(r²) correction in two evaluations.

    Under analyticity the next remainder is O(r^4), but the returned
    finite-precision number is not an enclosure for the exact coefficient.
    """
    if not isinstance(k,int) or not (3<=k<=15):raise ValueError('3<=k<=15 required')
    if not isinstance(dps,int) or not (50<=dps<=200):raise ValueError('dps out of range')
    verify_historical_providers()
    mp.mp.dps=dps
    syms,fn=make_rhs()
    def at(radius):
        fields,u0=data(radius)
        return (fn(*[fields[str(z)] for z in syms])/radius-2*u0)/(5*radius**2)
    r=mp.power(10,-k)
    v1=at(r);v2=at(r/10)
    corrected=(100*v2-v1)/99
    return {'step':51,'radius_exponents':[k,k+1],
            'source_git_blobs':verify_historical_providers(),
            'working_decimal_precision':dps,
            'u1_at_r':mp.nstr(v1,55),
            'u1_at_r_div_10':mp.nstr(v2,55),
            'u1_extrapolated_unenclosed':mp.nstr(corrected,55),
            'historical_step49_double_estimate':'0.0007897451669079507',
            'scientific_status':'HIGH_PRECISION_NUMERICAL_ONLY, NOT PROVED/CERTIFIED',
            'global_secondary':'OPEN','Dirac_time_preservation':'NOT_COMPUTED',
            'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 print(json.dumps(richardson_u1_at_decade(),indent=2))
