"""Formal exact Laurent expansion of original Step58 on Step55 regular center.
Quadratic field Q(sqrt(H2)); u1..u7 are arbitrary Taylor coefficients.
No full Dirac/gauge/boundary theorem follows from this local calculation.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha1
import sympy as sp
from .hr_step58_temporal_operator import physical_operator
from .hr_step45_exact_physical_ward import exact_physical_ward

MAX=18
PINNED={
 "hr_step45_exact_physical_ward.py":"66aa43841dccfe4a5d586a49be9c10af3a67a10e",
 "hr_step58_temporal_operator.py":"802c23aebd41780d8c462f1aa1711707fe4ee88f",
 "hr_step55_global_barrier.py":"a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
}
def check_sources():
 for name,expected in PINNED.items():
  raw=Path(__file__).with_name(name).read_bytes()
  got=sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
  if got!=expected:raise ValueError(f"source changed: {name}: {got}")
 return PINNED.copy()

H2=(sp.Rational('0.9')/(3*sp.Rational(2,5)**3)
 +sp.Rational('23.3348939346')*(3*sp.Rational(5787707228025044,10**16)
 +3*sp.Rational('-4.2383993109')*sp.Rational(5787707228025044,10**16)**2
 +sp.Rational('13.6801214252')*sp.Rational(5787707228025044,10**16)**3)/3)

class E:
 """a+b*sqrt(H2), with symbolic rational-polynomial a,b."""
 __slots__=('a','b')
 def __init__(self,a=0,b=0):
  if isinstance(a,float) or isinstance(b,float):raise ValueError("floating constant forbidden")
  self.a=sp.sympify(a);self.b=sp.sympify(b)
 @staticmethod
 def c(x):return x if isinstance(x,E) else E(x)
 def __add__(self,o):o=E.c(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E.c(o)
 def __rsub__(self,o):return E.c(o)+-self
 def __mul__(self,o):
  o=E.c(o);return E(self.a*o.a+H2*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  norm=self.a*self.a-H2*self.b*self.b
  if norm==0:raise ZeroDivisionError("quadratic norm zero")
  return E(self.a/norm,-self.b/norm)
 def __truediv__(self,o):return self*E.c(o).inv()
 def __rtruediv__(self,o):return E.c(o)*self.inv()
 def sqrt(self):
  if self.b==0:
   if self.a==H2:return E(0,1)
   if self.a==1:return E(1)
   if self.a==0:return E(0)
  raise ValueError("unsupported square root in exact field")
 def __pow__(self,n):
  if n==.5:return self.sqrt()
  if n==-.5:return self.sqrt().inv()
  if int(n)!=n:raise ValueError("unsupported power")
  n=int(n)
  if n<0:return self.inv()**(-n)
  out=E(1)
  while n:
   if n&1:out=out*self
   n//=2
   if n:self=self*self
  return out
 def zero(self):return sp.cancel(self.a)==0 and sp.cancel(self.b)==0
 def nonzero(self):
  if self.zero():return False
  if self.a.free_symbols or self.b.free_symbols:
   raise ValueError("unresolved symbolic leading coefficient")
  return True

class Laurent:
 """Truncated exact formal Laurent series, with quadratic-field coefficients."""
 __slots__=('a',)
 def __init__(self,x=0):
  if isinstance(x,Laurent):self.a=x.a.copy()
  elif isinstance(x,dict):self.a={int(k):E.c(v) for k,v in x.items() if int(k)<=MAX}
  else:self.a={0:E.c(x)}
 @staticmethod
 def c(x):return x if isinstance(x,Laurent) else Laurent(x)
 @staticmethod
 def var():return Laurent({1:E(1)})
 def __add__(self,o):
  o=Laurent.c(o)
  return Laurent({k:self.a.get(k,E())+o.a.get(k,E()) for k in self.a.keys()|o.a.keys() if k<=MAX})
 __radd__=__add__
 def __neg__(self):return Laurent({k:-v for k,v in self.a.items()})
 def __sub__(self,o):return self+-Laurent.c(o)
 def __rsub__(self,o):return Laurent.c(o)+-self
 def __mul__(self,o):
  o=Laurent.c(o);out={}
  for i,a in self.a.items():
   for j,b in o.a.items():
    k=i+j
    if k<=MAX:out[k]=out.get(k,E())+a*b
  return Laurent(out)
 __rmul__=__mul__
 def lead(self):
  for k in sorted(self.a):
   if self.a[k].nonzero():return k,self.a[k]
  raise ZeroDivisionError("zero Laurent series")
 def inv(self):
  v,a0=self.lead();b={-v:a0.inv()}
  for n in range(1,MAX+v+1):
   acc=E()
   for j in range(1,n+1):acc=acc+self.a.get(v+j,E())*b.get(-v+n-j,E())
   b[-v+n]=-(acc*b[-v])
  return Laurent(b)
 def __truediv__(self,o):return self*Laurent.c(o).inv()
 def __rtruediv__(self,o):return Laurent.c(o)*self.inv()
 def sqrt(self):
  v,a0=self.lead()
  if v%2:raise ValueError("odd square-root valuation")
  b={v//2:a0.sqrt()}
  for n in range(1,MAX-v//2+1):
   acc=E()
   for j in range(1,n):acc=acc+b.get(v//2+j,E())*b.get(v//2+n-j,E())
   b[v//2+n]=(self.a.get(v+n,E())-acc)/(2*b[v//2])
  return Laurent(b)
 def __pow__(self,n):
  if n==.5 or n==sp.Rational(1,2):return self.sqrt()
  if n==-.5 or n==sp.Rational(-1,2):return self.sqrt().inv()
  if int(n)!=n:raise ValueError("unsupported Laurent power")
  n=int(n)
  if n<0:return self.inv()**(-n)
  out=Laurent(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
 def diff(self,n=1):
  out=self
  for _ in range(n):out=Laurent({k-1:a*k for k,a in out.a.items() if k!=0})
  return out
 def integ(self):return Laurent({k+1:a/(k+1) for k,a in self.a.items() if k!=-1})
 def coeff(self,n):return self.a.get(n,E())

def step55_center():
 """Reconstruct original Step55 geometry and both dust-primary solutions."""
 r=Laurent.var();s=r*r
 A=Laurent(F(2,5));Y=Laurent(F(5787707228025044,10**16));B=A*Y
 MG=Laurent(1);MF=Laurent(F(10879548725,10**11)**2)
 M2=Laurent(F('23.3348939346'))
 B0,B1,B2,B3,B4=[Laurent(F(x)) for x in ('0','1','-4.2383993109','13.6801214252','-38.5117901844')]
 CG=Laurent(F('0.0015'));CF=Laurent(F('-0.0012'))
 KG=Laurent(F('0.0012'));KF=Laurent(F('-0.0016'));Z1=Laurent(F('0.004'))
 ug=1+CG*s;uf=1+CF*s;Lg=A*ug**2;Lf=B*uf**2
 Sgr=A*ug*(1+5*CG*s);Sfr=B*uf*(1+5*CF*s)
 T=B1*Lg**2+2*B2*Lg*Lf+B3*Lf**2
 T0=B0*Lg**2+2*B1*Lg*Lf+B2*Lf**2
 Tf=B2*Lg**2+2*B3*Lg*Lf+B4*Lf**2
 root=(1-Z1**2*s).sqrt();Dbar=M2*MG*Lg*Lf*T*Z1/root
 Wgbar=M2*MG*(Lg*T0+Lf*T*root)
 Wfbar=M2*MG*(Lf*Tf+Lg*T*root)
 Rg=-48*CG/(A**2*ug**5);Rf=-48*CF/(B**2*uf**5)
 Hsq=Laurent(F('0.9'))/(3*A**3)+M2*(B0+3*B1*Y+3*B2*Y**2+B3*Y**3)/3
 PG=-2*A**2*Hsq.sqrt()
 U0=MF*B*(PG/A-2*Z1)
 U=U0+sum((Laurent(sp.Symbol('u'+str(k)))*s**k for k in range(1,8)),Laurent(0))
 G=2*U+r*U.diff() # 2U+2s*U_s, the genuine radial pLf'/r
 Gmom=PG*(1+F(5,2)*CG*s);Gprime=2*PG*(1+5*CG*s)
 fac=Gmom/(2*MG*Lg*Sgr)
 betag=(1+KG**2*s).sqrt()+s*fac*KG*Lg
 Rhog=-(Gmom**2/(4*MG*Lg)-fac*(s*Dbar+Lg*Gprime)-MG*Lg**3*Rg/2+s*Z1*Dbar/Lg+Wgbar)/betag
 Psg=(s*Dbar+Lg*Gprime-Rhog*s*KG*Lg)/Sgr
 Ffac=U/(2*MF*Lf*Sfr);betaf=(1+KF**2*s).sqrt()
 Rhof=-(U**2/(4*MF*Lf)-Ffac*(-s*Dbar+Lf*G)-MF*Lf**3*Rf/2+s*Z1*Dbar/Lf+Wfbar)/(betaf+s*Ffac*KF*Lf)
 Psf=(-s*Dbar+Lf*G-Rhof*s*KF*Lf)/Sfr
 data={'Lg':Lg,'pLg':s*Gmom,'Sg':r*Lg,'pSg':r*Psg,'tg':(r*KG*Lg).integ(),'pg':s*Rhog,
       'Lf':Lf,'pLf':s*U,'Sf':r*Lf,'pSf':r*Psf,'tf':(r*KF*Lf).integ(),'pf':s*Rhof}
 return data,(MG,MF,M2,B0,B1,B2,B3,B4),r,Z1

def compute():
 check_sources()
 o=physical_operator();p=exact_physical_ward()
 data,params,r,z1=step55_center();vals={}
 for degree,keys in enumerate((o['q'],o['qp'],o['qpp'],o['qppp'],o['q4'])):
  for sy,name in zip(keys,p['Q']):vals[sy]=data[name].diff(degree)
 for name,v in [('z',r*z1),('zr',z1),('zrr',Laurent(0)),('zrrr',Laurent(0))]:vals[o[name]]=v
 for sy,value in zip(p['parameters'][:8],params):vals[sy]=value
 out={}
 for label in ('N','M'):
  for degree in (0,1,2):
   ex=o['operator'][label].get(degree,sp.S.Zero)
   safe=ex.replace(lambda x:x.is_Pow and x.exp.is_Rational and x.exp.q==2,
                   lambda x:sp.Function('halfpow')(x.base,sp.Integer(x.exp.p)))
   safe=safe.replace(lambda x:x.is_Rational and x.q!=1,
                     lambda x:sp.Function('exactrat')(sp.Integer(x.p),sp.Integer(x.q)))
   syms=sorted(ex.free_symbols,key=str)
   fn=sp.lambdify(syms,safe,modules=[{'exactrat':lambda a,b:Laurent(F(a,b)),
                                     'halfpow':lambda x,n:x.sqrt()**int(n),
                                     'sqrt':lambda x:x.sqrt()},'math'],cse=True)
   out[label+str(degree)]=Laurent.c(fn(*[vals[s] for s in syms]))
 return out

if __name__=='__main__':
 import json
 out=compute();n=out['N0'].coeff(2);m=out['M0'].coeff(2)
 print(json.dumps({'N2':[str(sp.cancel(n.a)),str(sp.cancel(n.b))],
                   'M2':[str(sp.cancel(m.a)),str(sp.cancel(m.b))],
                   'H2':str(H2),'status':'FORMAL_CENTER_ONLY'},indent=2))
