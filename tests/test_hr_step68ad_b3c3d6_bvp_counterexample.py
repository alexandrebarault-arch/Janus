"""Regression checks for the exact toy BVP counterexample; not independent physics."""
import unittest
from fractions import Fraction
import sympy as sp
from numerics.hr_step68ad_b3c3d6_bvp_counterexample import certificate

class TestBVP(unittest.TestCase):
    def test_symbolic_residuals(self):
        c=certificate()
        self.assertEqual(c['symbolic_zero_residuals'],10)
        self.assertEqual(c['exact_sign_checks'],6)
    def test_same_nonzero_first_jet(self):
        c=certificate()
        self.assertEqual(c['B_both'],['1','-1'])
        self.assertEqual(c['pointwise_endpoint_projection_rank_both'],2)
    def test_opposite_global_outcomes(self):
        c=certificate()
        self.assertTrue(c['good_global_positive_even_solution'])
        self.assertFalse(c['bad_global_solution_with_same_center_and_equal_outer'])
    def test_not_step58(self):
        c=certificate()
        self.assertFalse(c['original_step58_probe_executed'])
        self.assertEqual(c['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
