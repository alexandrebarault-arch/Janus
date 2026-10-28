"""Tests of the b3c3d5 exact local linear-algebra statements (not independent replay)."""
import unittest
from fractions import Fraction as F
from numerics.hr_step68ad_b3c3d5_temporal_boundary_jet_rank import (
    algebraic_checks,classify,center_clock_drift)

class TemporalBoundaryJetRank(unittest.TestCase):
    def test_symbolic(self):
        self.assertEqual(algebraic_checks()['symbolic_zero_residuals'],12)
    def test_first_jet_surjectivity(self):
        self.assertEqual(classify(2,3,1,0,4,5)['endpoint_projection_rank'],2)
        self.assertEqual(classify(2,3,0,1,4,5)['derivative_to_solve'],'Mprime')
    def test_algebraic_boundary_projection(self):
        self.assertEqual(classify(2,-3,0,0,3,2)['endpoint_tangent'],['-3','-2'])
        self.assertFalse(classify(2,3,0,0,3,2)['positive_lapse_pair_possible'])
    def test_center_drift_mvt(self):
        v=center_clock_drift()
        self.assertEqual(v['center_clock_rate_over_N0_strict'],['2407/5000','963/2000'])
        self.assertEqual(F(v['some_radial_derivative_over_N0_strict_upper']),-F(2407,4250))

if __name__=='__main__':unittest.main()
