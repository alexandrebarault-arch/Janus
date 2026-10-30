"""Exact rational regression witnesses; not independent physical validation."""
from fractions import Fraction as Q
import unittest
from numerics.hr_b3c3d6_step55_center_contraction import (
    half_contractive_cell, half_contractive_chain, four_radius_example)


class TestStep55CenterContraction(unittest.TestCase):
    def test_exact_saturation_step55_form(self):
        # Exact U=0, approximate v=c*s, G(s,U)=U, f=-U/(2*s).
        # Its continuous defect is 3*c/2; e(ra)=c*ra^2.
        c, a, b = Q(7, 5), Q(1, 100), Q(17, 20)
        self.assertEqual(half_contractive_cell(c*a*a, Q(3, 2)*c, a, b, 1), c*b*b)

    def test_chained_saturation(self):
        c=Q(7, 5)
        radii=[Q(1,100),Q(1,4),Q(1,2),Q(7,10),Q(17,20)]
        cells=[(a,b,Q(3,2)*c,Q(1)) for a,b in zip(radii,radii[1:])]
        self.assertEqual(half_contractive_chain(c*radii[0]**2,cells),c*radii[-1]**2)

    def test_zero_defect_damps(self):
        self.assertEqual(half_contractive_cell(1,0,Q(1,100),Q(17,20),1),Q(1,85))

    def test_no_Lh_smallness_needed(self):
        a,b=Q(1,100),Q(17,20)
        # The naive |f_U|=1/(2*s) bound at a has L*(b²-a²)>1.
        self.assertGreater((b*b-a*a)/(2*a*a),1)
        self.assertEqual(half_contractive_cell(0,0,a,b,1),0)

    def test_four_radii_exact(self):
        self.assertEqual(four_radius_example(0,[Q(1,2)]*4,1),
                         half_contractive_cell(0,Q(1,2),Q(1,100),Q(17,20),1))

    def test_reject_unproved_slope(self):
        with self.assertRaises(ValueError):
            half_contractive_cell(0,0,Q(1,100),Q(1,4),Q(10001,10000))

    def test_reject_negative_defect(self):
        with self.assertRaises(ValueError):
            half_contractive_cell(0,-1,Q(1,100),Q(1,4),1)

    def test_reject_disconnected_cells(self):
        with self.assertRaises(ValueError):
            half_contractive_chain(0,[(Q(1,100),Q(1,4),0,1),(Q(1,3),Q(1,2),0,1)])

    def test_reject_zero_center(self):
        with self.assertRaises(ValueError):
            half_contractive_cell(0,0,0,Q(1,4),1)

    def test_reject_invalid_radii(self):
        with self.assertRaises(ValueError):
            half_contractive_cell(0,0,Q(1,4),Q(1,4),1)


if __name__=='__main__':
    unittest.main()
