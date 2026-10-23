"""Outward-integer interval proof of a GLOBAL RADIAL INVARIANT BARRIER.

Given the Step49 local analytic regular center solution U(0)=U0, and the
original Step45/46 physical spherical primary-reduced equation
2*s*U_s=G(s,U)-2*U, this script certifies an inward-pointing pair of
barriers |U-Ustar|<=1/10000 over ALL s in [0,0.7225]. It also verifies
|G(s,U)-Vstar|<0.01 there, implying the Step54 rigorous positive two-dust
CONTINUUM tube applies to the exact radial solution. This is not the
full six-pair TEMPORAL Dirac preservation, lapse fixing or 4D evolution.
"""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
from .hr_step55_normalized_secondary import normalized_symbolic,check_original_source_blobs
import sympy as sp
S=10**28
class I:
 __slots__=('lo','hi')
 def __init__(self,lo,hi=None):
  self.lo=int(lo);self.hi=int(lo if hi is None else hi)
  if self.hi<self.lo:raise ValueError('bad interval')
 @staticmethod
 def c(x):
  if isinstance(x,I):return x
  f=F(str(x)) if isinstance(x,float) else F(x)
  return I(f.numerator*S//f.denominator,-((-f.numerator*S)//f.denominator))
 @staticmethod
 def hull(a,b):
  a,b=F(a),F(b)
  return I(a.numerator*S//a.denominator, -((-b.numerator*S)//b.denominator))
 def __add__(self,o):
  o=I.c(o);return I(self.lo+o.lo,self.hi+o.hi)
 __radd__=__add__
 def __neg__(self):return I(-self.hi,-self.lo)
 def __sub__(self,o):return self+-I.c(o)
 def __rsub__(self,o):return I.c(o)+-self
 def __mul__(self,o):
  o=I.c(o);v=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
  return I(min(v)//S,-((-max(v))//S))
 __rmul__=__mul__
 def inv(self):
  if self.lo<=0<=self.hi:raise ZeroDivisionError('crossing zero '+str((self.lo,self.hi)))
  return I((S*S)//self.hi, -((-S*S)//self.lo))
 def __truediv__(self,o):return self*I.c(o).inv()
 def __rtruediv__(self,o):return I.c(o)*self.inv()
 def __pow__(self,k):
  if k==0:return I.c(1)
  if k==sp.Rational(1,2) or k==.5:return self.sqrt()
  if k==sp.Rational(-1,2) or k==-.5:return self.sqrt().inv()
  if int(k)!=k:raise ValueError('fractional unsupported')
  k=int(k)
  if k<0:return self.inv()**(-k)
  if k%2==0:
   if self.lo<=0<=self.hi:return I(0,-((-max(self.lo*self.lo,self.hi*self.hi))//S)) if k==2 else (self*self)**(k//2)
   if k==2:return I(min(self.lo*self.lo,self.hi*self.hi)//S,-((-max(self.lo*self.lo,self.hi*self.hi))//S))
  out=I.c(1);v=self
  while k:
   if k&1:out=out*v
   k//=2
   if k:v=v*v
  return out
 def sqrt(self):
  if self.lo<0:raise ValueError('negative sqrt')
  lo=isqrt(self.lo*S);hi=isqrt(self.hi*S)
  if hi*hi<self.hi*S:hi+=1
  return I(lo,hi)
 def __abs__(self):
  if self.lo>=0:return self
  if self.hi<=0:return -self
  return I(0,max(-self.lo,self.hi))
 def lt(self,a):return self.hi<I.c(a).lo
 def gt(self,a):return self.lo>I.c(a).hi
 def disp(self):return (self.lo/S,self.hi/S)
 def __repr__(self):return str(self.disp())


A=I.c(F('.4'));Y=I.c(F('.5787707228025044'));B=A*Y
MG=I.c(1);MF=I.c(F('.10879548725')**2);M2=I.c(F('23.3348939346'))
B0,B1,B2,B3,B4=[I.c(F(x)) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
CG=I.c(F('.0015'));CF=I.c(F('-.0012'));KG=I.c(F('.0012'));KF=I.c(F('-.0016'));Z1=I.c(F('.004'))
H2=I.c(F('.9'))/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
PG=-2*A**2*H2.sqrt();U0=MF*B*(PG/A-2*Z1)
U1=I.hull('0.0007897451667202464909325108904961683602148118201690','0.0007897451667202464909325108904961683602148118201692')
U2=I.hull('-0.00001007385348674382817573689095286393593388364194376377344','-0.00001007385348674382817573689095286393593388364194376377342')

def geometry(s):
 ug=1+CG*s;uf=1+CF*s
 Lg=A*ug**2;Lf=B*uf**2
 Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
 T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
 T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
 Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
 root=(1-Z1**2*s).sqrt()
 Dbar=M2*MG*Lg*Lf*T*Z1/root
 Wgbar=M2*MG*(Lg*T0+Lf*T*root)
 Wfbar=M2*MG*(Lf*Tf+Lg*T*root)
 Rg=-48*CG/(A**2*ug**5)
 Rf=-48*CF/(B**2*uf**5)
 Gmom=PG*(1+F(5,2)*CG*s)
 Gprime=2*PG*(1+5*CG*s)
 fac=Gmom/(2*MG*Lg*Sgr)
 betag=(1+KG**2*s).sqrt()+s*fac*KG*Lg
 Rhog=-(Gmom**2/(4*MG*Lg)-fac*(s*Dbar+Lg*Gprime)-MG*Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag
 Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr
 return dict(Lg0=Lg,Lf0=Lf,Sgr0=Sgr,Sfr0=Sfr,Gmom=Gmom,Psg0=Psg,Rhog=Rhog,Gprime=Gprime,tg0=KG*Lg,tf0=KF*Lf,z1=Z1,Dbar=Dbar,Wfbar=Wfbar,Rf=Rf,Lgr0=4*A*CG*ug,Lfr0=4*B*CF*uf,
   Mg2=MG,Mf2=MF,m2=M2,beta0=B0,beta1=B1,beta2=B2,beta3=B3,beta4=B4)

@lru_cache(maxsize=1)
def compiled():
 expr,s,U,v=normalized_symbolic()
 xs=sorted(expr.free_symbols,key=str)
 fn=sp.lambdify(xs,expr,modules=[{'sqrt':lambda x: x.sqrt(),'Abs':abs},'math'],cse=True)
 return xs,fn

def G(s,u):
 inputs=geometry(s);inputs['s']=s;inputs['U']=u
 syms,fn=compiled()
 return fn(*[inputs[str(v)] for v in syms])

def stars(s):
 u=U0+U1*s+U2*s*s
 v=2*U0+4*U1*s+6*U2*s*s
 # s u'(s) for upper and lower residual
 ud=U1+2*U2*s
 return u,v,ud

def residual(s,delta):
 us,vs,uds=stars(s)
 upper=G(s,us+delta)-2*(us+delta)-2*s*uds
 lower=G(s,us-delta)-2*(us-delta)-2*s*uds
 return upper,lower



def certify_global_barrier(cells=256,delta_U='0.0001',delta_V='0.01'):
 """All branch-sign inequalities use outward integer intervals, no sampling.

 Exact rational cells partition s=r² from 0 to (17/20)². Upper bound
 Fplus<0 and lower Fminus>0 imply invariance of the barrier for the
 unique bounded analytic center branch (Step49). On that barrier G(s,U)
 is enclosed and Vstar proximity is rigorously checked against Step54.
 """
 if not isinstance(cells,int) or not 64<=cells<=8192:raise ValueError('unsupported cells')
 du=F(delta_U);dv=F(delta_V)
 if not F(0)<du<=F('0.001') or not F(0)<dv<=F('0.01'):
  raise ValueError('delta outside supported proof chart')
 blobs=check_original_source_blobs()
 # Force the exact symbolic normalization to compile before checking cells.
 syms,fn=compiled()
 if not syms or fn is None:raise AssertionError('no normalized physical ODE')
 D=I.c(du)
 mu=-10**80;ml=10**80;mvlo=10**80;mvhi=-10**80
 Glo=10**80;Ghi=-10**80
 for i in range(cells):
  ss=I.hull(F('0.7225')*i/cells,F('0.7225')*(i+1)/cells)
  up,down=residual(ss,D)
  mu=max(mu,up.hi);ml=min(ml,down.lo)
  if up.hi>=0 or down.lo<=0:
   raise ArithmeticError(f'invariance NOT certified at slab {i}: Fplus={up}, Fminus={down}')
  u,v,_=stars(ss)
  vel=G(ss,I(u.lo-D.hi,u.hi+D.hi))
  err=vel-v
  mvlo=min(mvlo,err.lo);mvhi=max(mvhi,err.hi)
  Glo=min(Glo,vel.lo);Ghi=max(Ghi,vel.hi)
  if err.lo<=-I.c(dv).lo or err.hi>=I.c(dv).lo:
   raise ArithmeticError(f'normalized V missing Step54 tube at slab {i}: {err}')
 # By Step49: locally analytic U(s) satisfying U(0)=U0 exists uniquely.
 # With Fplus<0 and Fminus>0 on the WHOLE interval, first-contact
 # comparison prevents leaving |U-Ustar|<=du for all s>0.
 # The interval implementation enforces positive original denominators;
 # smooth RHS on the compact tube gives continuation to s=0.7225.
 # Both U, V meet the earlier Step54 delta=.01 condition, whose
 # independent integer proof gives all dust/J/K signs strictly positive.
 def frac(i):return str(F(i,S))
 return {'step':55,'mode':'CERTIFIED_GLOBAL_RADIAL_BARRIER_ON_PRESCRIBED_SPHERICAL_INITIAL_DATA',
  's_interval':['0','0.7225'],'r_interval':['0','0.85'],'cells':cells,
  'U_delta_bound_rational':str(du),'V_delta_bound_rational':str(dv),
  'strict_max_Fupper_rational':frac(mu),'strict_min_Flower_rational':frac(ml),
  'V_minus_Vstar_lower_rational':frac(mvlo),'V_minus_Vstar_upper_rational':frac(mvhi),
  'V_actual_min_enclosure':frac(Glo),'V_actual_max_enclosure':frac(Ghi),
  'original_G_normalized':'G(s,U)=pLf_prime_rhs(sqrt(s),pLf=sU)/sqrt(s) from Step45/46 exact physical action after rational radial factor cancellation',
  'comparison_reason':'Original Step49 center analytic regular U(0)=U0 exists locally. Inward strict barriers on all cells prevent a first exit for s>0; smooth nonzero denominators on compact tube permit standard ODE continuation through smax. G provides V=pLf_prime/r for all s. Step54 independent positive dust/J/K interval theorem applies.',
  'logical_scope':'EXACT spatial spherical constrained radial profile on the prescribed benchmark (two positive dusts). NOT original 4D time evolution or full temporal Dirac ghost proof.',
  'Step54_tube_hypothesis_proved_for_exact_radial_solution':True,
  'Step54_positive_two_dust_and_JK_signs_apply':True,
  'original_physical_source_sha':blobs,
  'integer_outward_lattice':'10^-28 integer rational',
  'Dirac_secondary_time_preservation':'NOT_COMPUTED',
  'lapse_fixing':'NOT_COMPUTED','GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

if __name__=='__main__':
 import json
 print(json.dumps(certify_global_barrier(),indent=2))
