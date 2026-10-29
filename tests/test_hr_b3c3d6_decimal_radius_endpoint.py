import unittest
from fractions import Fraction
from numerics.hr_b3c3d6_decimal_radius_endpoint import endpoint_s, old_endpoint_error, new_endpoint_error


class DecimalEndpointTests(unittest.TestCase):
    def test_all_four_radii_decimal_roundtrip(self):
        for r, expected in [(0.25,'0.0625'),(0.5,'0.25'),(0.7,'0.49'),(0.85,'0.7225')]:
            with self.subTest(r=r):
                sf, target = endpoint_s(r)
                self.assertEqual(str(sf),expected)
                self.assertEqual(str(target),expected)

    def test_old_binary_square_mismatch_at_two_radii(self):
        self.assertEqual(old_endpoint_error(0.7),Fraction(-29,450359962737049600))
        self.assertEqual(old_endpoint_error(0.85),Fraction(-9,112589990684262400))

    def test_exact_binary_radii_unchanged(self):
        for r in (0.25,0.5):
            self.assertEqual(old_endpoint_error(r),0)
            self.assertEqual(new_endpoint_error(r),0)

    def test_new_rounding_is_no_worse_at_all_four(self):
        for r in (0.25,0.5,0.7,0.85):
            self.assertLessEqual(abs(new_endpoint_error(r)),abs(old_endpoint_error(r)))

    def test_invalid_radii_rejected(self):
        for r in (0,-1,float('nan'),float('inf')):
            with self.subTest(r=r),self.assertRaises(ValueError):
                endpoint_s(r)

if __name__=='__main__': unittest.main()
