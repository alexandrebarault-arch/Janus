"""Rational non-regression tests for actual SciPy binary64 abscissae."""
import unittest
from fractions import Fraction
from numerics.hr_b3c3d6_binary_endpoint_gap_audit import endpoint_record, start_record, diagnostics


class BinaryEndpointGapTests(unittest.TestCase):
    def test_dyadic_endpoints_exact(self):
        for r in ('0.25', '0.5'):
            self.assertEqual(endpoint_record(r)['binary_gap'], '0')

    def test_seven_tenths_binary_gap(self):
        self.assertEqual(endpoint_record('0.7')['binary_gap'], '-1/112589990684262400')

    def test_seventeen_twentieths_binary_gap(self):
        self.assertEqual(endpoint_record('0.85')['binary_gap'], '7/225179981368524800')

    def test_shortest_decimal_masks_binary_gap(self):
        for r in ('0.7', '0.85'):
            record = endpoint_record(r)
            self.assertEqual(record['shortest_decimal_gap'], '0')
            self.assertNotEqual(record['binary_gap'], '0')

    def test_start_time_mismatch(self):
        self.assertEqual(start_record()['binary_s0_gap'], '221/46116860184273879040000')

    def test_all_within_half_ulp_and_negative_control(self):
        for row in diagnostics()['radii']:
            self.assertLessEqual(abs(Fraction(row['binary_gap'])), Fraction(row['half_ulp']))
        # This deliberately falsifies the incorrect 1e-40 *binary* endpoint claim.
        self.assertGreater(abs(Fraction(endpoint_record('0.85')['binary_gap'])), Fraction(1, 10**40))


if __name__ == '__main__':
    unittest.main()
