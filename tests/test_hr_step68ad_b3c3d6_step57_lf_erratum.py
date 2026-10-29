"""Regression tests for original Step57 Nprime 1/Lf erratum (not independent)."""
import unittest
import sympy as sp
from numerics.hr_step68ad_b3c3d6_step57_lf_erratum import certificate,symbols,R

class TestStep57LfErratum(unittest.TestCase):
    def test_full_certificate(self):
        self.assertEqual(certificate()['exact_zero_residuals'],10)
    def test_missing_factor_is_not_one(self):
        d=symbols()
        self.assertNotEqual(d['B'],1)
        self.assertEqual(sp.simplify(d['old_cNp']/d['cNp']-d['Lf']),0)
    def test_old_bound_disproved_at_center(self):
        d=symbols()
        self.assertLess(sp.limit(d['q']/d['r'],d['r'],0),sp.Rational(1000,201))
    def test_reversed_ratio_bound(self):
        self.assertGreater(sp.Rational(certificate()['two_term_M1_NR1_center_ratio_lower']),sp.Rational(2593,5000))
    def test_original_sha_pins(self):
        d=certificate()['original_source_blobs']
        self.assertEqual(d['Step57'],'bf8e0bdfb7c6705d8c30d4afc79003483e3ab33f')

if __name__=='__main__': unittest.main()
