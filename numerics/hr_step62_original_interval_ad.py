"""Step62: ORIGINAL Step55 physical G(s,U) total (geometry-aware) derivative intervals.

Six-pair positive-EH HR/two dust source comes unchanged from actual GitHub
Step45/46/55 and original 256-cell interval radial geometry of Step55. Each
quadratic Taylor jet coefficient encloses the corresponding 2-var derivative
(without divided-factor for mixed jets); no finite difference and no plain
partial G_s with frozen geometric parameters. Strict interval arithmetic is
provided by original integer outward-rounding I lattice (10**28).

Proof applies to the prescribed radial initial-data benchmark only. NOT full
spacetime Dirac preservation, lapse fixing or ghost-freedom.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
import sympy as sp
from . import hr_step55_global_barrier as original

EXPECTED={
 'hr_step45_exact_physical_ward.py':'66aa43841dccfe4a5d586a49be9c10af3a67a10e',
 'hr_step46_exact_secondary_ode.py':'bac025c28dbe1561c0c36c56dbfda46dc326f804',
 'hr_step55_normalized_secondary.py':'a54a6acf2f7ad2f64c500faecfa1406ecbf7b862',
 'hr_step55_global_barrier.py':'a6e7004120d0a166a3a8973c2fbe1487a8eb70fe'}
I=original.I
KEYS=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))


def verify_original_blobs():
 for f,expected in EXPECTED.items():
  raw=(Path(__file__).parent/f).read_bytes()
  computed=sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
  if computed!=expected:raise ValueError(f'Original changed {f}: {computed}')
 return EXPECTED.copy()

class Jet2:
 """Bivariate order-two Taylor coefficients over rigorously enclosing I."""
 __slots__=('c',)
 def __init__(self,c):
  self.c={k:I.c(v) for k,v in c.items()}
 @classmethod
 def const(cls,v):
  if isinstance(v,Jet2):return v
  return cls({(0,0):v})
 @classmethod
 def s(cls,v):return cls({(0,0):v,(1,0):1})
 @classmethod
 def u(cls,v):return cls({(0,0):v,(0,1):1})
 def coeff(self,k):return self.c.get(k,I.c(0))
 def __add__(self,o):
  o=self.const(o)
  return Jet2({k:self.coeff(k)+o.coeff(k) for k in KEYS})
 __radd__=__add__
 def __neg__(self):return Jet2({k:-v for k,v in self.c.items()})
 def __sub__(self,o):return self+-self.const(o)
 def __rsub__(self,o):return self.const(o)+-self
 def __mul__(self,o):
  o=self.const(o);out={}
  for (i,j),a in self.c.items():
   for (k,l),b in o.c.items():
    pair=(i+k,j+l)
    if pair[0]+pair[1]<=2:
     out[pair]=out.get(pair,I.c(0))+a*b
  return Jet2(out)
 __rmul__=__mul__
 def inv(self):
  a=self.coeff((0,0));ai=a.inv()
  h=self-Jet2.const(a)
  return Jet2.const(ai)-h*(ai**2)+(h*h)*(ai**3)
 def __truediv__(self,o):return self*self.const(o).inv()
 def __rtruediv__(self,o):return self.const(o)*self.inv()
 def __pow__(self,p):
  if isinstance(p,float) and p in (-.5,.5):p=F(str(p))
  if isinstance(p,sp.Rational):p=F(int(p.p),int(p.q))
  if isinstance(p,int) or isinstance(p,F) and p.denominator==1:
   n=int(p)
   if n<0:return (self.inv())**(-n)
   out=Jet2.const(1);b=self
   while n:
    if n&1:out=out*b
    n//=2
    if n:b=b*b
   return out
  if p not in (F(1,2),F(-1,2)):raise ValueError('power outside original G interval chart '+str(p))
  a=self.coeff((0,0))
  if a.lo<=0:raise ValueError('fractional power outside strictly positive chart')
  h=self-Jet2.const(a)
  ap=a.sqrt() if p==F(1,2) else a.sqrt().inv()
  return Jet2.const(ap)*(1+F(p)*h/a+F(p*(p-1)/2)*h*h/(a*a))
 def sqrt(self):return self**F(1,2)
 def __abs__(self):
  a=self.coeff((0,0))
  if a.lo>0:return self
  if a.hi<0:return -self
  raise ValueError('Abs derivative on a zero-crossing interval; subdivide')
 def derivatives(self):
  return {'G':self.coeff((0,0)),
   'G_s':self.coeff((1,0)),'G_U':self.coeff((0,1)),
   'G_ss':self.coeff((2,0))*2,'G_sU':self.coeff((1,1)),
   'G_UU':self.coeff((0,2))*2}

def _override_original_constants():
 keys='A Y B MG MF M2 B0 B1 B2 B3 B4 CG CF KG KF Z1 H2 PG U0 U1 U2'.split()
 saved={k:getattr(original,k) for k in keys}
 for k,v in saved.items():setattr(original,k,Jet2.const(v))
 return saved

def _restore_original_constants(saved):
 for k,v in saved.items():setattr(original,k,v)

def physical_G_jet(s_range,u_range):
 """Original G evaluated on full benchmark geometry and s,U intervals.

 Interval centers in derivative slots are themselves interval sets: returned
 G_ss etc rigorously enclose each physical partial over the entire tile.
 """
 verify_original_blobs()
 saved=_override_original_constants()
 try:
  return original.G(Jet2.s(s_range),Jet2.u(u_range)).derivatives()
 finally:_restore_original_constants(saved)

def _tube_at_s(s_range):
 # Polynomial Step55 barrier: U*(s)=U0+U1*s+U2*s².
 ss=Jet2.const(s_range)
 uu=Jet2.const(original.U0)+Jet2.const(original.U1)*ss+Jet2.const(original.U2)*ss*ss
 return I(uu.coeff((0,0)).lo-I.c(F('0.0001')).hi,
          uu.coeff((0,0)).hi+I.c(F('0.0001')).hi)

def cover_derivatives(cells=256):
 """All continuous s∈[0,289/400], U in Step55 1e-4 tube.

 The proof is conditional ONLY on the already certified Step55 radial tube.
 Values are exact rational outward-rounded interval bounds and can be
 serialized with fractions of denominator original.S (10^28).
 """
 if not isinstance(cells,int) or cells<1 or cells>8192:raise ValueError('invalid cells')
 verify_original_blobs()
 bound={}
 for i in range(cells):
  low=F(289,400)*i/cells;high=F(289,400)*(i+1)/cells
  tile=I.hull(low,high)
  jets=physical_G_jet(tile,_tube_at_s(tile))
  for k,value in jets.items():
   if k not in bound:bound[k]=[value.lo,value.hi]
   else:
    bound[k][0]=min(bound[k][0],value.lo)
    bound[k][1]=max(bound[k][1],value.hi)
 return {k:(F(v[0],original.S),F(v[1],original.S)) for k,v in bound.items()}


def manifest(cells=256):
 a=cover_derivatives(cells)
 radial=certify_radial_jet_bounds(cells)
 return {'step':62,'original_git_blobs':EXPECTED,'cells':cells,
  'geometry_parameter_dependence_in_G_s':True,
  'coverage':'ALL s in [0,289/400], U in Step55 certified Ustar±1/10000',
  'interval_scale':str(original.S),
  'derivative_intervals':{k:[str(x) for x in v] for k,v in a.items()},
  'derived_radial_jet_intervals':{k:[str(x) for x in v] for k,v in radial.items()},
  'P_third_first_cell':'NOT CERTIFIED: broad Step55 tube cannot bound (G-2U)/s at zero',
  'physical_lapse_coefficients':'NOT COMPUTED','Dirac_rank':'NOT COMPUTED',
  'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED'}

def certify_radial_jet_bounds(cells=256):
    """Bound P second derivative on all cells and P third on interior cells.

    The Step55 fixed-width U tube is insufficient to control (G-2U)/s at
    zero. No claim for P third derivative on the first cell.
    """
    if cells<8 or cells>8192:raise ValueError('8..8192 cells needed')
    bounds={}
    for i in range(cells):
        lo=F(289,400)*i/cells;hi=F(289,400)*(i+1)/cells
        s=I.hull(lo,hi);u=_tube_at_s(s)
        e=physical_G_jet(s,u)
        G,Gs,Gu,Gss,Gsu,Guu=(e[k] for k in ('G','G_s','G_U','G_ss','G_sU','G_UU'))
        ff=G-2*u
        H=G+2*s*Gs+ff*Gu
        Hs=3*Gs+2*s*Gss+Gs*Gu+ff*Gsu
        Hu=Gu*Gu-Gu+2*s*Gsu+ff*Guu
        quantities={'P_second':H}
        if i>0:
            third_by_r=2*Hs+(ff/s)*Hu
            quantities['P_third_over_r_interior']=third_by_r
            quantities['P_third_interior']=s.sqrt()*third_by_r
        for k,val in quantities.items():
            if k not in bounds:bounds[k]=[val.lo,val.hi]
            else:
                bounds[k][0]=min(bounds[k][0],val.lo)
                bounds[k][1]=max(bounds[k][1],val.hi)
    return {k:(F(a,original.S),F(b,original.S)) for k,(a,b) in bounds.items()}

if __name__=='__main__':
 import json,sys
 n=int(sys.argv[1]) if len(sys.argv)>1 else 256
 print(json.dumps(manifest(n),indent=2))
