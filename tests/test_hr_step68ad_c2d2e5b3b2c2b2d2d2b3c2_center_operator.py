"""Exact algebraic regression for b3c2. Run: python -m unittest tests.test_hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator"""
import unittest
from fractions import Fraction as F
import sympy as sp
from numerics.hr_step68ad_c2d2e5b3b2c2b2d2d2b3c2_center_operator import (
    compute, H2, check_sources, PINNED
)

def qsign(a,b):
 """Exact sign of a+b*sqrt(H2), a,b rational."""
 a=F(a);b=F(b);h=F(int(H2.p),int(H2.q))
 if b==0:return (a>0)-(a<0)
 if a==0:return (b>0)-(b<0)
 if (a>0)==(b>0):return (a>0)-(a<0)
 d=a*a-h*b*b
 if d==0:return 0
 return ((a>0)-(a<0))*(1 if d>0 else -1)

class TestCenterOperator(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.out=compute()
  cls.n=cls.out['N0'].coeff(2)
  cls.m=cls.out['M0'].coeff(2)
  cls.na,cls.nb,cls.ma,cls.mb=map(sp.cancel,(cls.n.a,cls.n.b,cls.m.a,cls.m.b))

 def test_pinned_sources(self):
  self.assertEqual(check_sources(),PINNED)
  self.assertEqual(len(PINNED),3)

 def test_all_lower_laurent_coefficients(self):
  for lab in ('N','M'):
   for order in (0,1,2):
    threshold=2 if order==0 else 4
    for k in range(-8,threshold):
     v=self.out[lab+str(order)].coeff(k)
     self.assertEqual(sp.cancel(v.a),0,(lab,order,k,'a'))
     self.assertEqual(sp.cancel(v.b),0,(lab,order,k,'b'))
    for k in (2,3):
     if order==0 and k==2:continue
     v=self.out[lab+str(order)].coeff(k)
     self.assertEqual(sp.cancel(v.a),0,(lab,order,k,'a'))
     self.assertEqual(sp.cancel(v.b),0,(lab,order,k,'b'))

 def test_independent_of_seven_free_taylor_coefficients(self):
  for k in range(1,8):
   u=sp.Symbol('u'+str(k))
   for expr in (self.na,self.nb,self.ma,self.mb):
    self.assertEqual(sp.cancel(sp.diff(expr,u)),0)

 def test_exact_signs_and_ratio(self):
  a,b,c,d=self.na,self.nb,self.ma,self.mb
  self.assertGreater(qsign(a-3507,b),0)
  self.assertGreater(qsign(3508-a,-b),0)
  self.assertGreater(qsign(c+6765,d),0)
  self.assertGreater(qsign(-6764-c,-d),0)
  lo=F(1037,2000);hi=F(2593,5000)
  self.assertGreater(qsign(a+lo*c,b+lo*d),0)
  self.assertLess(qsign(a+hi*c,b+hi*d),0)

if __name__=='__main__':unittest.main()
