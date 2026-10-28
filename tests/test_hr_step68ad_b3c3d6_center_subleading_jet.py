"""Regression guards for the conditional central lapse-jet identity."""
import unittest
import sympy as s
from numerics.hr_step68ad_b3c3d6_center_subleading_jet import certificate


class CenterSubleadingTest(unittest.TestCase):
    def test_certificate(self):
        self.assertEqual(certificate()['symbolic_zero_residuals'],8)
    def test_models(self):
        self.assertEqual(certificate()['exact_positive_models'],3)
    def test_r4_includes_second_derivatives(self):
        r=s.symbols('r'); m=s.Rational(1,2)+s.Rational(3,2)*r*r
        self.assertEqual(s.expand((2*r*r+3*r**4)-4*r*r*m+r**4*s.diff(m,r,2)),0)
    def test_not_step58(self):
        d=certificate()
        self.assertFalse(d['original_step58_replay'])
        self.assertEqual(d['JANUS_R'],'NOT_VALIDATED')


if __name__=='__main__':unittest.main()
