import unittest
import sympy as sp
from numerics.hr_step68ad_b3c3d6_two_term_cancellation import certificate,exact_terms,R

class TestTwoTermCancellation(unittest.TestCase):
    def test_certificate(self):
        d=certificate()
        self.assertEqual(d['symbolic_zero_residuals'],6)
        self.assertEqual(d['GATE_2B'],'OPEN')
    def test_exact_cancel_at_three_points(self):
        r,cM,cNp,q,_=exact_terms()
        for x in (sp.Rational(1,4),sp.Rational(1,2),R):
            self.assertEqual(sp.simplify((cM-q*cNp).subs(r,x)),0)
    def test_center_ratio_incompatible(self):
        self.assertLess(sp.Rational(804,2249),sp.Rational(1037,2000))
    def test_negative_guard(self):
        r,cM,cNp,q,_=exact_terms()
        self.assertNotEqual(sp.simplify(cM+cNp*q),0)

if __name__=='__main__':unittest.main()
