import unittest
from fractions import Fraction as Q
from pathlib import Path
from numerics.hr_b3c3d6_monotone_physical_four_radii import (
    authenticate_originals, monotone_decreasing_box, certify_four_radii, RADII)
from numerics.hr_step55_global_barrier import I, S


class TestPhysicalMonotoneG(unittest.TestCase):
    def test_original_blobs_authenticated(self):
        self.assertEqual(len(authenticate_originals()), 4)

    def test_monotone_endpoint_toy(self):
        # Natural interval dependency of 2-u+u-u can be arbitrarily broad;
        # derivative must be of the TRUE function, not of its interval syntax.
        box = I.c(Q(1, 2))
        ui = I.hull(Q(1, 4), Q(3, 4))
        fn = lambda s, u: 2-u+u-u
        sharp = monotone_decreasing_box(fn, box, ui, I.c(-1), I)
        self.assertEqual(Q(sharp.lo, S), Q(5, 4))
        self.assertEqual(Q(sharp.hi, S), Q(7, 4))

    def test_reject_missing_strict_derivative_sign(self):
        with self.assertRaises(ArithmeticError):
            monotone_decreasing_box(lambda s,u:u, I.c(1), I.hull(0,1),
                                    I.hull(-1,0), I)

    def test_four_physical_radii_and_signs(self):
        report = certify_four_radii()
        self.assertEqual(report['original_barrier_cells_rerun'], 256)
        self.assertEqual([x['r'] for x in report['radii']], list(map(str,RADII)))
        for row in report['radii']:
            self.assertTrue(row['G_s_strictly_positive'])
            self.assertTrue(row['G_U_strictly_negative'])
            self.assertTrue(row['pLf_second_strictly_negative'])
            self.assertGreater(Q(row['width_ratio_natural_over_monotone']), 18)
            self.assertLess(Q(row['jets']['pLf_second'][1]), 0)
            if row['r'] != '1/4':
                self.assertTrue(row['U_s_strictly_positive'])
        self.assertEqual(report['JANUS_R'], 'NOT_VALIDATED')


if __name__ == '__main__':
    unittest.main()
