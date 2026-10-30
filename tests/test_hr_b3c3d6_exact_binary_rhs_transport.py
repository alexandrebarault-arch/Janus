import unittest
from fractions import Fraction
import mpmath as mp
from numerics.hr_b3c3d6_exact_binary_rhs_transport import (
    exact_binary, decimal_square_target, transport_endpoint, exact_fraction_mp)

class ExactBinaryTransportTests(unittest.TestCase):
    def test_binary_exactness_and_shortest_decimal_mismatch(self):
        with mp.workdps(100):
            for x in (1e-4, 0.7, 0.85, 0.85**2):
                q = Fraction.from_float(x)
                self.assertEqual(exact_binary(x), exact_fraction_mp(q))
            self.assertNotEqual(exact_binary(0.85**2), mp.mpf(str(0.85**2)))

    def test_reject_nonbinary_and_invalid_radius(self):
        with self.assertRaises(TypeError): exact_binary('0.85')
        for x in ('0', '-1', 'NaN', 'Infinity'):
            with self.assertRaises(ValueError): decimal_square_target(x)

    def test_exact_endpoint_gaps(self):
        self.assertEqual(decimal_square_target('0.7') - Fraction.from_float(float(0.49)), Fraction(1, 112589990684262400))
        self.assertEqual(decimal_square_target('0.85') - Fraction.from_float(float(0.7225)), Fraction(-7, 225179981368524800))

    def test_toy_linear_ode_removes_first_order_endpoint_error(self):
        with mp.workdps(100):
            for r in ('0.7', '0.85'):
                sf = float(decimal_square_target(r))
                s = exact_binary(sf)
                # y'=3y, exact y(sf)=exp(3sf), then rounded to binary64 as SciPy would return.
                y_binary = float(mp.exp(3*s))
                got = transport_endpoint(r, sf, y_binary, lambda t,y: 3*y, dps=100)
                delta = exact_fraction_mp(got['delta'])
                # Separate the unavoidable y_binary rounding error from transport truncation.
                exact_yf = mp.exp(3*s)
                transport_from_exact = exact_yf + delta*3*exact_yf
                target = mp.exp(3*(s+delta))
                self.assertLess(abs(transport_from_exact-target), 5*abs(delta)**2*abs(exact_yf))
                self.assertLess(abs(got['value']-transport_from_exact), 2*abs(exact_binary(y_binary)-exact_yf))

    def test_toy_nonlinear_rhs_binary_vs_decimal(self):
        with mp.workdps(100):
            s = 0.85**2
            self.assertNotEqual(1/exact_binary(s), 1/mp.mpf(str(s)))

    def test_dyadic_endpoint_transport_zero(self):
        for r in ('0.25', '0.5'):
            sf = float(decimal_square_target(r))
            got = transport_endpoint(r, sf, 1.0, lambda t,y:t+y)
            self.assertEqual(got['delta'], 0)
            self.assertEqual(got['value'], 1)

if __name__ == '__main__': unittest.main()
