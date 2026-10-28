import unittest
from numerics.hr_step68ad_b3c3d4_relative_clock_lapse_curvature import run
class RestrictedOuterLapseCurvature(unittest.TestCase):
    def test_exact_symbolic(self): self.assertEqual(run()['symbolic_zero_residuals'],13)
    def test_rational(self): self.assertEqual(run()['exact_rational_checks'],6)
    def test_not_dirac(self): self.assertIn('not temporal Dirac',run()['scope'])
    def test_gate(self): self.assertEqual(run()['JANUS_R'],'NOT_VALIDATED')
if __name__=='__main__': unittest.main()
