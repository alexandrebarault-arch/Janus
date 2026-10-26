"""Independent exact symbolic checks, including a negative-K chart witness."""
import unittest
import sympy as sp
from hr_step68ad_c2d2e5b_shift_boundary import exact_checks,rational_witness


class ShiftBoundaryTests(unittest.TestCase):
    def test_four_exact_identities(self):
        for name,residual in exact_checks().items():
            with self.subTest(name=name):
                self.assertEqual(residual,0)

    def test_regular_shift(self):
        self.assertEqual(rational_witness()['z_star'],sp.Rational(4,5))

    def test_stationarity(self):
        self.assertEqual(rational_witness()['F_positive'],0)

    def test_shift_jet_response(self):
        self.assertEqual(rational_witness()['dz_dpLg_prime'],-sp.Rational(18,125))

    def test_boundary_jet_response(self):
        self.assertEqual(rational_witness()['dB_dpLg_prime'],sp.Rational(42,25))

    def test_negative_K_correct_chart(self):
        self.assertEqual(rational_witness()['F_negative_K_correct'],0)

    def test_negative_K_wrong_chart(self):
        self.assertEqual(rational_witness()['F_negative_K_wrong'],8)

    def test_K_zero_nonzero_D_has_no_root(self):
        self.assertEqual(rational_witness()['F_K_zero_D_nonzero'],4)

    def test_K_D_zero_loses_shift_determination(self):
        self.assertEqual(rational_witness()['F_K_zero_D_zero'],0)


if __name__=='__main__':
    unittest.main()
