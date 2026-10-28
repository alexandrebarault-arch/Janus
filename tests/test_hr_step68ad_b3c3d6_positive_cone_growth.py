"""Regression guards, not independent validation of the physical model."""
import unittest
from numerics.hr_step68ad_b3c3d6_positive_cone_growth import algebraic_certificate,toy_certificate,audit

class PositiveConeGrowthTests(unittest.TestCase):
    def test_six_exact_algebraic_residuals(self):
        self.assertEqual(algebraic_certificate(),6)
    def test_six_exact_toy_residuals(self):
        self.assertEqual(toy_certificate(),6)
    def test_status_guard(self):
        a=audit()
        self.assertEqual((a['GATE_2B'],a['JANUS_R']),('OPEN','NOT_VALIDATED'))
    def test_original_probe_guard(self):
        self.assertFalse(audit()['original_outer_probe_executed'])

if __name__=='__main__':unittest.main()
