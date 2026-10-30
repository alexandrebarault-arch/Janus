"""Exact rational, non-independent regression tests; NOT a physical DOP853 replay."""
import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_robust_step55_barrier import (
    FUPPER_MAX, FLOWER_MIN, R_MAX, S_MAX, TUBE_HALF,
    global_residual_threshold, boundary_slacks, candidate_tube_sufficient,
    conditional_endpoint_error, normalized_defect_sufficient,
)

class RobustBarrier(unittest.TestCase):
    def test_historical_margin_signs(self):
        self.assertLess(FUPPER_MAX, 0)
        self.assertGreater(FLOWER_MIN, 0)

    def test_limiting_margin_is_lower(self):
        self.assertLess(FLOWER_MIN, -FUPPER_MAX)

    def test_exact_global_threshold(self):
        self.assertEqual(global_residual_threshold(), Q(295653233337826329055403, 2890000000000000000000000000))

    def test_global_threshold_approximation(self):
        self.assertTrue(Q(1023,10**7) < global_residual_threshold() < Q(1024,10**7))

    def test_zero_residual_slacks(self):
        self.assertEqual(boundary_slacks(0, R_MAX), (-FUPPER_MAX, FLOWER_MIN))

    def test_half_threshold_passes(self):
        x = candidate_tube_sufficient(Q(1,100),R_MAX,0,global_residual_threshold()/2)
        self.assertGreater(x['upper_slack'],0)
        self.assertGreater(x['lower_slack'],0)

    def test_threshold_equality_rejected(self):
        with self.assertRaises(ValueError):
            candidate_tube_sufficient(Q(1,100),R_MAX,0,global_residual_threshold())

    def test_above_threshold_rejected(self):
        with self.assertRaises(ValueError):
            candidate_tube_sufficient(Q(1,100),R_MAX,0,global_residual_threshold()*2)

    def test_smaller_radius_larger_allowable_defect(self):
        x = candidate_tube_sufficient(Q(1,100),Q(1,2),0,global_residual_threshold()*2)
        self.assertGreater(x['sufficient_D_strict'],global_residual_threshold())

    def test_initial_boundary_rejected(self):
        with self.assertRaises(ValueError):
            candidate_tube_sufficient(Q(1,100),R_MAX,TUBE_HALF,0)

    def test_negative_defect_rejected(self):
        with self.assertRaises(ValueError):
            candidate_tube_sufficient(Q(1,100),R_MAX,0,-1)

    def test_invalid_radius_rejected(self):
        with self.assertRaises(ValueError):
            candidate_tube_sufficient(0,R_MAX,0,0)

    def test_endpoint_exact_for_forced_toy(self):
        # G=0, U=0, v(s)=k*s: |d|=2k, |e(sa)|=k*sa.
        a,b,k=Q(1,4),Q(1,2),Q(1,1000)
        self.assertEqual(conditional_endpoint_error(k*a*a,2*k,a,b),k*b*b)

    def test_endpoint_exact_for_unforced_toy(self):
        # G=0, v=0, U(s)=c/s, d=0, e(sa)=c/sa.
        a,b,c=Q(1,4),Q(1,2),Q(1,1000)
        self.assertEqual(conditional_endpoint_error(c/(a*a),0,a,b),c/(b*b))

    def test_toy_large_residual_can_exit(self):
        # G=0, f=-U/s, Ustar=0, H=1/10, v(sa)=0, d=3/10.
        # v(s)=d/2*(s-sa²/s), v(1)=9/64>H: small D matters.
        sa,sb,d,H=Q(1,4),Q(1),Q(3,10),Q(1,10)
        self.assertGreater(d/2*(sb-sa*sa/sb),H)

class NormalizedResidual(unittest.TestCase):
    def test_zero_passes(self):
        self.assertGreater(normalized_defect_sufficient(Q(1,100),R_MAX,0,0)['lower_slack'],0)

    def test_half_margin_passes(self):
        x=normalized_defect_sufficient(Q(1,100),R_MAX,0,FLOWER_MIN/2)
        self.assertEqual(x['lower_slack'],FLOWER_MIN/2)

    def test_equality_fails(self):
        with self.assertRaises(ValueError):
            normalized_defect_sufficient(Q(1,100),R_MAX,0,FLOWER_MIN)

    def test_negative_fails(self):
        with self.assertRaises(ValueError):
            normalized_defect_sufficient(Q(1,100),R_MAX,0,-1)

if __name__=='__main__': unittest.main()
