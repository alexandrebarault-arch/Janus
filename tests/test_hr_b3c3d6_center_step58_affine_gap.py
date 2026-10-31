"""Exact-rational regression of a conditional Step58 center comparison."""
import unittest
from fractions import Fraction as F
from numerics.hr_b3c3d6_center_step58_affine_gap import (
    U_SS_LO,U_SS_HI,global_center_bound,certify_at,
)

class TestCenterGap(unittest.TestCase):
    def test_archived_uss_strict_negative(self):
        self.assertLess(U_SS_LO,U_SS_HI)
        self.assertLess(U_SS_HI,0)
    def test_normalized_rational_sandwich(self):
        lo,hi=global_center_bound()
        self.assertLess(F(63,100000),lo)
        self.assertLess(lo,hi)
        self.assertLess(hi,F(13,20000))
    def test_continuum_radius_and_r6(self):
        for r in (F(1,10000),F(1,64),F(1,32)):
            row=certify_at(r)
            a,b=map(F,row['A_M_actual_minus_holonomic_affine_strict'])
            self.assertLess(0,a)
            self.assertLess(a,b)
            self.assertLess(b,F(13,20000)*r**6)
    def test_rejects_outside_center_domain(self):
        for r in (F(0),F(-1,10),F(1,16),F(17,20)):
            with self.assertRaises(ValueError): certify_at(r)
    def test_rejects_unproved_uss_sign(self):
        with self.assertRaises(ValueError):global_center_bound(F(-1,100),F(1,100))
    def test_rejects_inverted_uss_interval(self):
        with self.assertRaises(ValueError):global_center_bound(F(-1,10000),F(-1,100))

if __name__ == '__main__':unittest.main()
