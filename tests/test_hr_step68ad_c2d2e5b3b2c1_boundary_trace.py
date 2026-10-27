"""Independent exact-rational tests of the conditional Step55 boundary trace."""
import unittest
from fractions import Fraction as F
from hr_step68ad_c2d2e5b3b2c1_boundary_trace import (
    A, B, CG, MF2, MG2, R_OUT, certificate,
    reconstruction_Dg_residual, trace_coefficients,
)


class BoundaryTraceTests(unittest.TestCase):
    def test_outer_momentum_exact(self):
        self.assertEqual(trace_coefficients()['delta_pLg_over_lambda'], F(92730563, 128000000))

    def test_outer_momentum_derivative_exact(self):
        self.assertEqual(trace_coefficients()['delta_pLg_prime_over_lambda'], F(2734739, 1600000))

    def test_center_sensitivity_exact(self):
        self.assertEqual(trace_coefficients()['delta_U0_over_lambda'], MF2 * B / (MG2 * A))

    def test_nonzero_all_three(self):
        self.assertTrue(all(x > 0 for x in trace_coefficients().values()))

    def test_center_momentum_zero(self):
        self.assertEqual(trace_coefficients(F(0))['delta_pLg_over_lambda'], 0)

    def test_center_momentum_derivative_zero(self):
        self.assertEqual(trace_coefficients(F(0))['delta_pLg_prime_over_lambda'], 0)

    def test_generic_radius_formula(self):
        r = F(1, 2)
        self.assertEqual(trace_coefficients(r)['delta_pLg_over_lambda'], r*r*(1+F(5,2)*CG*r*r))

    def test_nonzero_lambda_violates_fixed_outer_momentum(self):
        for lam in (F(1,100), F(-1,100), F(1,1000000)):
            self.assertNotEqual(lam * trace_coefficients()['delta_pLg_over_lambda'], 0)

    def test_nonzero_lambda_violates_fixed_outer_derivative(self):
        for lam in (F(1,100), F(-1,100)):
            self.assertNotEqual(lam * trace_coefficients()['delta_pLg_prime_over_lambda'], 0)

    def test_reconstruction_Dg_independent_of_pg_parameter(self):
        for r in (F(1,4), F(17,20)):
            for rho in (F(-2), F(3,2)):
                self.assertEqual(reconstruction_Dg_residual(r,F(2,5),rho,F(1,800),F(-9,7),F(9,10)),0)

    def test_certificate_status(self):
        c=certificate()
        self.assertEqual(c['GATE_2B'], 'OPEN')
        self.assertEqual(c['JANUS_R'], 'NOT_VALIDATED')
        self.assertEqual(c['outer_r'], str(R_OUT))


if __name__ == '__main__':
    unittest.main()
