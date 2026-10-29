import unittest
import sympy as sp
from numerics import hr_b3c3d6_step57_corrected_uniform_bound as c

class TestCorrectedStep57UniformBound(unittest.TestCase):
    def test_formula_from_original(self):
        self.assertEqual(sp.cancel(c.correct_over_r+2*(1+5*c.cg*c.s)*(1-c.z2)/(c.B*c.ug*c.uf**2)),0)
    def test_missing_lf_detected(self):
        self.assertEqual(sp.cancel(c.legacy_over_r-c.Lf*c.correct_over_r),0)
        self.assertNotEqual(c.correct_over_r.subs(c.s,0),c.legacy_over_r.subs(c.s,0))
    def test_exact_center(self):
        self.assertEqual(c.correct_over_r.subs(c.s,0),-2/c.B)
        self.assertEqual(c.legacy_over_r.subs(c.s,0),-2)
    def test_uniform_enclosure(self):
        cert=c.certificate()
        self.assertEqual(cert['rational_guards'],10)
        self.assertTrue(sp.Rational(60,7)*sp.Rational(9999,10000)/sp.Rational(501,500)**2>sp.Rational(17,2))
    def test_negative_control(self):
        self.assertFalse(bool(-c.legacy_over_r.subs(c.s,0)>sp.Rational(17,2)))
        self.assertTrue(bool(-c.correct_over_r.subs(c.s,0)>sp.Rational(17,2)))

if __name__=='__main__': unittest.main()
