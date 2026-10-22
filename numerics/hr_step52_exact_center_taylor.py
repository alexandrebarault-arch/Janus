"""Exact Step52 algebraic regular-center U1 certificate for the fixed spherical benchmark.

Formal Laurent jets in Q(sqrt(H²)) with rational benchmark inputs, algebraic
spherical original six-canonical-pair secondary RHS, and conservative
truncation error order. This is NOT global Dirac time preservation.
"""
from __future__ import annotations
from fractions import Fraction as F
import os,hashlib, json
from pathlib import Path
from math import isqrt
from sympy import Rational
import sympy as sp, time, sys
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode

SOURCE_PINS={'numerics/hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e','numerics/hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804'}
def verify_source_pins(root=None):
 root=Path(root) if root else Path(__file__).resolve().parents[1]
 for rel,expected in SOURCE_PINS.items():
  raw=(root/rel).read_bytes()
  got=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
  if got!=expected:raise ValueError('original source SHA drift: '+rel)
 return SOURCE_PINS.copy()

# Exact quadratic algebra Q[H] where H^2 = exact rational positive Friedmann background.
a=F('0.4');y=F('0.5787707228025044'); b=a*y; mg=F(1);mf=F('0.10879548725')**2;m2=F('23.3348939346');
beta=list(map(F,('0','1','-4.2383993109','13.6801214252','-38.5117901844')))
H2=F('.9')/(3*a**3)+m2*(beta[0]+3*beta[1]*y+3*beta[2]*y*y+beta[3]*y**3)/3
class Q:
 __slots__=('a','b')
 def __init__(self,a=0,b=0): self.a=F(a);self.b=F(b)
 @staticmethod
 def c(x):return x if isinstance(x,Q) else Q(x)
 def __add__(self,o):
  if isinstance(o,J):return NotImplemented
  o=Q.c(o);return Q(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q(-self.a,-self.b)
 def __sub__(self,o):return self+-Q.c(o)
 def __rsub__(self,o):return Q.c(o)+-self
 def __mul__(self,o):
  if isinstance(o,J):return NotImplemented
  o=Q.c(o);return Q(self.a*o.a+self.b*o.b*H2,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  n=self.a*self.a-self.b*self.b*H2
  if not n:raise ZeroDivisionError('quadratic zero')
  return Q(self.a/n,-self.b/n)
 def __truediv__(self,o):return self*Q.c(o).inv()
 def __rtruediv__(self,o):return Q.c(o)*self.inv()
 def __eq__(self,o):o=Q.c(o);return self.a==o.a and self.b==o.b
 def __bool__(self):return bool(self.a or self.b)
 def __repr__(self):return f'Q({self.a}, {self.b}*H)'
 def __pow__(self,n):
  if n<0:return (self.inv())**(-n)
  out=Q(1); x=self
  while n:
   if n&1:out=out*x
   x=x*x;n//=2
  return out

def sqrt_q(x):
 x=Q.c(x)
 if x==Q(1):return Q(1)
 if x==Q(0):return Q(0)
 raise NotImplementedError('non-unit sqrt constant: '+repr(x)[:200])

P=int(os.environ.get("JANUS_JET_ORDER","20"))
if not 12<=P<=32:raise ValueError("Jet order 12..32 required")
INF=1000000
class J:
 __slots__=('d','cutoff')
 def __init__(self,d=None,cutoff=INF):
  d=d or {}
  self.d={int(k):Q.c(v) for k,v in d.items() if v and k<=P}
  self.cutoff=min(cutoff,P+1) if any(v and k>P for k,v in d.items()) else cutoff
 @staticmethod
 def c(x):return x if isinstance(x,J) else J({0:Q.c(x)})
 def val(self):return min(self.d) if self.d else (self.cutoff if self.cutoff!=INF else None)
 def __add__(self,b):
  b=J.c(b); d=self.d.copy()
  for k,v in b.d.items():d[k]=d.get(k,Q())+v
  return J(d,min(self.cutoff,b.cutoff))
 __radd__=__add__
 def __neg__(self):return J({k:-v for k,v in self.d.items()},self.cutoff)
 def __sub__(self,b):return self+-J.c(b)
 def __rsub__(self,b):return J.c(b)+-self
 def __mul__(self,b):
  b=J.c(b); d={}
  v1=self.val();v2=b.val()
  if v1 is None or v2 is None:return J()
  cutoff=min(self.cutoff+v2,b.cutoff+v1)
  for i,x in self.d.items():
   for j,y in b.d.items():
    if i+j<=P:d[i+j]=d.get(i+j,Q())+x*y
    else:cutoff=min(cutoff,P+1)
  return J(d,cutoff)
 __rmul__=__mul__
 def inv(self):
  if not self.d:raise ZeroDivisionError
  v=self.val();a=[self.d.get(v+i,Q()) for i in range(P+abs(v)+5)]
  b=[a[0].inv()]
  for n in range(1,P+v+1 if v>=0 else P+v+1):
   s=Q()
   for k in range(1,n+1):s=s+a[k]*b[n-k]
   b.append(-s*b[0])
  return J({-v+n:x for n,x in enumerate(b) if x},min(P+1,self.cutoff-2*v))
 def __truediv__(self,b):return self*J.c(b).inv()
 def __rtruediv__(self,b):return J.c(b)*self.inv()
 def __pow__(self,n):
  if n==0:return J.c(1)
  if n<0:return (self.inv())**(-n)
  out=J.c(1);x=self
  while n:
   if n&1:out=out*x
   n//=2
   if n:x=x*x
  return out
 def sqrt(self):
  v=self.val()
  if v is None:return J()
  if v%2:raise ValueError('sqrt odd valuation')
  a=[self.d.get(v+k,Q()) for k in range(P+abs(v)+5)]
  b0=sqrt_q(a[0]);b=[b0]
  # b_n=(a_n-sum(b_k*b_n-k))/(2*b0)
  for n in range(1,P-v//2+1):
   s=Q()
   for k in range(1,n):s=s+b[k]*b[n-k]
   b.append((a[n]-s)/(2*b0))
  return J({v//2+n:x for n,x in enumerate(b) if x},min(P+1,self.cutoff-v//2))
 def __repr__(self):return 'J('+','.join(f'{k}:{v}' for k,v in list(sorted(self.d.items()))[:5])+')'

r=J({1:Q(1)});s=r*r
cg=F('0.0015');cf=F('-0.0012');z1=F('0.004');kg=F('0.0012');kf=F('-0.0016');H=Q(0,1)
b0,b1,b2,b3,b4=beta
ug=1+cg*s;uf=1+cf*s; Lg=a*ug**2;Lf=b*uf**2;Sg=r*Lg;Sf=r*Lf
Lgr=4*a*cg*r*ug;Lfr=4*b*cf*r*uf;Sgr=a*ug*(1+5*cg*s);Sfr=b*uf*(1+5*cf*s)
Pg=-2*a*a*H;plg=Pg*s*(1+F(5,2)*cg*s);plgr=2*r*(1+5*cg*s)*Pg
trg=kg*r*Lg;trf=kf*r*Lf;z=z1*r;root=(1-z*z).sqrt()
At=b1*Sg*Sg+2*b2*Sg*Sf+b3*Sf*Sf;A0=b0*Sg*Sg+2*b1*Sg*Sf+b2*Sf*Sf;Af=b2*Sg*Sg+2*b3*Sg*Sf+b4*Sf*Sf
K=m2*mg*Lg*Lf*At;Dg=K*z/root;Wg=m2*mg*(Lg*A0+Lf*At*root);Wf=m2*mg*(Lf*Af+Lg*At*root)
Rg=-48*cg/(a*a*ug**5);Rf=-48*cf/(b*b*uf**5)
fac=plg/(2*mg*Sg*Sgr);kin=Lg*plg**2/(4*mg*Sg**2);curv=-mg*Lg*Sg*Sg*Rg/2
numerator=kin-fac*(Dg+Lg*plgr)+curv+z*Dg/Lg+Wg
beta_g=(1+(trg/Lg)**2).sqrt()+fac*trg;pg=-numerator/beta_g;psg=(Dg+Lg*plgr-pg*trg)/Sgr
U0=mf*b*(Pg/(mg*a)-2*z1)
fields={'Lg':Lg,'Lf':Lf,'Sg':Sg,'Sf':Sf,'pLg':plg,'pLf':s*U0,
    'pSg':psg,'pg':pg,'Lgr':Lgr,'Lfr':Lfr,'Sgr':Sgr,'Sfr':Sfr,
    'pLgr':plgr,'tgr':trg,'tfr':trf,
    'Mg2':mg,'Mf2':mf,'m2':m2,
    **{f'beta{i}':x for i,x in enumerate(beta)},
    'z':z,'zr':z1,'zrr':0,'Dg_original':Dg,'Wf_original':Wf,'R3f_original':Rf}

def exact_jets():
 verify_source_pins()
 expr=exact_f_momentum_ode()['pLf_prime_rhs']
 cache={}
 def evaluate(expr):
  if expr in cache:return cache[expr]
  if expr.is_Symbol:
   if str(expr) not in fields:raise KeyError(expr)
   ans=J.c(fields[str(expr)])
  elif expr.is_Rational:ans=J.c(F(int(expr.p),int(expr.q)))
  elif expr.is_Add:
   ans=J()
   for a in expr.args:ans+=evaluate(a)
  elif expr.is_Mul:
   ans=J.c(1)
   for a in expr.args:ans*=evaluate(a)
  elif expr.is_Pow:
   base=evaluate(expr.base); e=expr.exp
   if e.is_Integer:ans=base**int(e)
   elif e.q==2 and e.p in (1,-1):ans=base.sqrt() if e.p==1 else base.sqrt().inv()
   else:raise TypeError(f'power {expr.exp}')
  else:raise TypeError(expr)
  cache[expr]=ans
  return ans
 x=evaluate(expr)
 assert x.cutoff>3, ('unknown tails can reach target r³',x.cutoff)
 assert x.d.get(0,Q())==Q()
 assert x.d.get(1,Q())==2*U0
 assert x.d.get(2,Q())==Q()
 assert x.d.get(4,Q())==Q()
 # For P=r²(U0+U1 r²+...), P'=2U0*r+4U1*r³.
 # HOWEVER evaluating F(r,P=r²U0) freezes U at U0, so
 # the implicit G(s,U) has dG/dU=-1 at center and 5*U1=coef(r³).
 u1=x.d.get(3,Q())/5
 scale=10**90
 hlower=F(isqrt((H2.numerator*scale*scale)//H2.denominator),scale)
 hupper=hlower+F(1,scale)
 assert hlower*hlower<=H2<=hupper*hupper
 lo=u1.a+u1.b*(hlower if u1.b>=0 else hupper)
 hi=u1.a+u1.b*(hupper if u1.b>=0 else hlower)
 assert lo<=hi and hi-lo<F('1e-80')
 import mpmath as mp
 mp.mp.dps=100
 approx=mp.mpf(u1.a.numerator)/u1.a.denominator+mp.mpf(u1.b.numerator)/u1.b.denominator*mp.sqrt(mp.mpf(H2.numerator)/H2.denominator)
 return {'step':52,'jet_order':P,'rhs_remainder_unknown_from_r_power':x.cutoff,
       'symbolic_expression_nodes':len(cache),'H2_exact':str(H2),
       'U1_rational_A':str(u1.a),'U1_rational_B':str(u1.b),
       'exact_formula':'U1=A+B*sqrt(H2), H2 exact rational and positive',
       'strict_lower_rational':str(lo),'strict_upper_rational':str(hi),
       'decimal_display':mp.nstr(approx,80),
       'center_rhs_coefficients_checked':True,
       'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED',
       'global_continuum_radial_solution':'NOT_PROVED',
       'Dirac_time_preservation':'NOT_COMPUTED'}

if __name__=='__main__':print(json.dumps(exact_jets(),indent=2))
