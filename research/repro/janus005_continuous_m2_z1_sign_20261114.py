from fractions import Fraction as F
from math import isqrt
class I:
 def __init__(self,a,b=None): self.a=F(a);self.b=F(a if b is None else b);assert self.a<=self.b
 def __add__(self,o):
  o=iv(o);return I(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return I(-self.b,-self.a)
 def __sub__(self,o):return self+-iv(o)
 def __rsub__(self,o):return iv(o)+-self
 def __mul__(self,o):
  o=iv(o);v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(v),max(v))
 __rmul__=__mul__
 def __truediv__(self,o):
  o=iv(o);assert o.a*o.b>0;return self*I(1/o.b,1/o.a)
 def __pow__(self,n):
  assert n>=0 and isinstance(n,int)
  if n==0:return I(1)
  if n%2==0:
   hi=max(self.a*self.a,self.b*self.b);lo=F(0) if self.a<=0<=self.b else min(self.a*self.a,self.b*self.b)
   return I(lo,hi)**(n//2) if n>2 else I(lo,hi)
  return self*(self**(n-1))
 def sqrt(self):
  assert self.a>=0
  scale=10**22
  def low(q):return F(isqrt(q.numerator*scale*scale//q.denominator),scale)
  a=low(self.a);b=low(self.b)+F(1,scale)
  return I(a,b)
 def __repr__(self):return str((float(self.a),float(self.b)))
def iv(x):return x if isinstance(x,I) else I(x)
A=I(F('0.4'));Y=I(F('0.5787707228025044'));B=A*Y
b1,b2,b3,b4=[I(F(x)) for x in ('1','-4.2383993109','13.6801214252','-38.5117901844')]
cg=F('.0015');cf=F('-.0012');z=F('.004');m=F('23.3348939346')
N=256; allT=[];allQ=[];allDet=[]
for k in range(N):
 s=I(F('0.7225')*k/N,F('0.7225')*(k+1)/N)
 Lg=A*(1+cg*s)**2;Lf=B*(1+cf*s)**2
 T=b1*Lg**2+2*b2*Lg*Lf+b3*Lf**2
 Tf=b2*Lg**2+2*b3*Lg*Lf+b4*Lf**2
 r=(1-z*z*s).sqrt()
 Q=Lf*Tf+Lg*T*r*(1+s*z*z)
 det=m*Lg*Lf*T*Q/(r**3)
 allT.append(T);allQ.append(Q);allDet.append(det)
print('T positive all:',all(v.a>0 for v in allT),'Q negative all:',all(v.b<0 for v in allQ),'det negative all:',all(v.b<0 for v in allDet))
for name,arr in [('T',allT),('Q',allQ),('det',allDet)]:print(name,'global enclosure',float(min(v.a for v in arr)),float(max(v.b for v in arr)))
