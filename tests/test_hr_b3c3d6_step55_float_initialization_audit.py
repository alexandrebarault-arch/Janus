import unittest
import mpmath as mp
from numerics.hr_b3c3d6_step55_float_initialization_audit import center_initial_value, diagnostics

class Step55FloatInitializationTests(unittest.TestCase):
    def test_source_constants_reproduce_center_initial_value(self):
        with mp.workdps(110):
            v = center_initial_value(110)
            self.assertTrue(mp.almosteq(v,mp.mpf('-0.005252347922344801514364923472998400505989718191313428996077244359492678'),rel_eps=mp.mpf('1e-65')))

    def test_float_rounding_exceeds_tiny_step58_reported_scale(self):
        with mp.workdps(110):
            v = center_initial_value(110)
            e = abs(mp.mpf(float(v))-v)
            self.assertTrue(mp.mpf('1e-20') < e < mp.mpf('1e-18'))
            self.assertGreater(e/mp.mpf('1e-44'),mp.mpf('1e24'))

    def test_decimal_string_conversion_is_not_exact_binary_value(self):
        with mp.workdps(110):
            v = center_initial_value(110)
            binary = mp.mpf(float(v))
            shortest = mp.mpf(str(float(v)))
            self.assertNotEqual(binary,shortest)
            self.assertGreater(abs(binary-shortest),mp.mpf('1e-19'))

    def test_high_precision_input_stability(self):
        with mp.workdps(125):
            a = center_initial_value(90)
            b = center_initial_value(120)
            self.assertLess(abs(a-b),mp.mpf('1e-85'))

    def test_diagnostics_agree_with_recomputation(self):
        d = diagnostics(110)
        with mp.workdps(110):
            v = center_initial_value(110)
            self.assertEqual(d['float_repr'],repr(float(v)))
            self.assertLess(abs(mp.mpf(d['binary_rounding_error'])-abs(mp.mpf(float(v))-v)),mp.mpf('1e-65'))

    def test_negative_control_roundtrip_is_not_1e_minus_40(self):
        with mp.workdps(110):
            v = center_initial_value(110)
            self.assertFalse(abs(mp.mpf(float(v))-v) < mp.mpf('1e-40'))

if __name__ == '__main__': unittest.main()
