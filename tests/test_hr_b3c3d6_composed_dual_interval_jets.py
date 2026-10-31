import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_composed_dual_interval_jets import (
    Dual, lift_global_constants, evaluate_composed)

A = Q(3, 2)
B = Q(2, 5)

def fake_geometry(s):
    return {'a': A * (1 + B * s)**2, 's': s}

class RationalInterval:
    def __init__(self, lo, hi=None):
        self.lo = Q(lo)
        self.hi = Q(lo if hi is None else hi)
        if self.lo > self.hi: raise ValueError
    @staticmethod
    def c(v): return v if isinstance(v, RationalInterval) else RationalInterval(v)
    def __add__(self, o):
        o = self.c(o)
        return RationalInterval(self.lo+o.lo, self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return RationalInterval(-self.hi, -self.lo)
    def __sub__(self,o):return self+-self.c(o)
    def __rsub__(self,o):return self.c(o)+-self
    def __mul__(self,o):
        o=self.c(o)
        z=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return RationalInterval(min(z),max(z))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=self.c(o)
        if o.lo<=0<=o.hi:raise ZeroDivisionError
        return self*RationalInterval(1/o.hi,1/o.lo)
    def __rtruediv__(self,o):return self.c(o)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        out=self.c(1)
        for _ in range(n):out=out*self
        return out
    def sqrt(self):
        from math import isqrt
        def rt(q):
            a,b=isqrt(q.numerator),isqrt(q.denominator)
            if a*a!=q.numerator or b*b!=q.denominator:raise ValueError('non-square test')
            return Q(a,b)
        return RationalInterval(rt(self.lo),rt(self.hi))

class TestComposedAD(unittest.TestCase):
    def test_basic_polynomial(self):
        x=Dual(Q(2),Q(1)); y=(x**3+2*x-1)
        self.assertEqual((y.v,y.d),(Q(11),Q(14)))
    def test_rational_inverse(self):
        x=Dual(Q(3),Q(1));y=5/(x+2)
        self.assertEqual((y.v,y.d),(Q(1),Q(-1,5)))
    def test_sqrt(self):
        x=Dual(RationalInterval(9),RationalInterval(1));y=x.sqrt()
        self.assertEqual((y.v.lo,y.d.lo),(Q(3),Q(1,6)))
    def test_abs_strict_sign(self):
        self.assertEqual(abs(Dual(Q(-3),Q(2))).d,Q(-2))
        with self.assertRaises(ValueError):abs(Dual(RationalInterval(-1,1),RationalInterval(1)))
    def test_zero_derivative_constants_cloned_not_mutated(self):
        cloned=lift_global_constants(fake_geometry,RationalInterval)
        x=cloned(Dual(RationalInterval(1),RationalInterval(1)))['a']
        self.assertEqual(x.v.lo,Q(147,50))
        self.assertEqual(x.d.lo,Q(42,25))
        self.assertEqual(A,Q(3,2))
    def test_full_chain_vs_frozen_geometry(self):
        symbols=['a','s','U']
        fn=lambda a,s,U:a*U*U+s
        for r in (Q(1,4),Q(1,2),Q(7,10),Q(17,20)):
            s=r*r;u=Q(3,4)
            ds=evaluate_composed(symbols,fn,fake_geometry,RationalInterval,
                                 RationalInterval(s),RationalInterval(u),True,False)
            du=evaluate_composed(symbols,fn,fake_geometry,RationalInterval,
                                 RationalInterval(s),RationalInterval(u),False,True)
            a=A*(1+B*s)**2
            expected_s=2*A*B*(1+B*s)*u*u+1
            self.assertEqual(ds.d.lo,expected_s)
            self.assertEqual(du.d.lo,2*a*u)
            self.assertNotEqual(ds.d.lo,Q(1))
    def test_interval_inclusion(self):
        symbols=['a','s','U']; fn=lambda a,s,U:a*U*U+s
        sbox=RationalInterval(Q(1,4),Q(9,25))
        ubox=RationalInterval(Q(1,2),Q(3,4))
        result=evaluate_composed(symbols,fn,fake_geometry,RationalInterval,
                                 sbox,ubox,True,False)
        for s in (Q(1,4),Q(3,10),Q(9,25)):
            for u in (Q(1,2),Q(5,8),Q(3,4)):
                exact=2*A*B*(1+B*s)*u*u+1
                self.assertLessEqual(result.d.lo,exact)
                self.assertGreaterEqual(result.d.hi,exact)
    def test_missing_symbol_rejected(self):
        with self.assertRaises(KeyError):
            evaluate_composed(['a','bogus'],lambda a,b:a+b,fake_geometry,
                              RationalInterval,RationalInterval(1),RationalInterval(1),True,False)
    def test_zero_crossing_division_rejected(self):
        with self.assertRaises(ZeroDivisionError):
            (Dual(RationalInterval(1),RationalInterval(1))/
             Dual(RationalInterval(-1,1),RationalInterval(1)))

if __name__=='__main__':unittest.main()