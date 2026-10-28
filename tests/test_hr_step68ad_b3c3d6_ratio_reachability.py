import unittest
from numerics.hr_step68ad_b3c3d6_ratio_reachability import symbolic_certificate, exact_example, certificate

class RatioReachability(unittest.TestCase):
    def test_generic_identity(self):
        self.assertEqual(symbolic_certificate()['algebraic_residuals_passed'],3)
    def test_exact_analytic_example(self):
        self.assertEqual(exact_example()['exact_example_residuals_passed'],5)
    def test_positive_ends(self):
        d=exact_example()
        self.assertEqual(d['k0'],'10371/20000')
        self.assertEqual(d['kR'],'1')
        self.assertTrue(d['analytic_positive_on_closed_interval'])
    def test_status(self):
        d=certificate()
        self.assertEqual(d['GATE_2B'],'OPEN')
        self.assertEqual(d['JANUS_R'],'NOT_VALIDATED')
        self.assertIn('NOT_STEP55',d['status'])

if __name__=='__main__': unittest.main()
