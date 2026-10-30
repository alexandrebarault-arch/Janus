import unittest
from fractions import Fraction
from decimal import Decimal
import mpmath as mp
from numerics.hr_b3c3d6_exact_binary_rhs_transport import (
    transport_endpoint, transport_endpoint_second_order, decimal_square_target,
    exact_binary,
)

class TransportTests(unittest.TestCase):
    def test_quadratic_exact_at_four_radii(self):
        with mp.workdps(80):
            for r in (0.25, 0.5, 0.7, 0.85):
                sf = float(Decimal(str(r))**2)
                yf = float(sf*sf)
                z = transport_endpoint_second_order(r, sf, yf, lambda s,y: 2*s)
                h = mp.mpf(z['delta'].numerator)/z['delta'].denominator
                self.assertEqual(z['acceleration'], 2)
                self.assertLess(abs(z['value']-(exact_binary(yf)+2*exact_binary(sf)*h+h*h)), mp.mpf('1e-70'))
                self.assertFalse(z['solver_state_error_enclosed'])

    def test_first_order_misses_quadratic_delta_squared(self):
        with mp.workdps(80):
            r=0.85; sf=float(Decimal(str(r))**2); yf=float(sf*sf)
            first=transport_endpoint(r,sf,yf,lambda s,y:2*s)
            second=transport_endpoint_second_order(r,sf,yf,lambda s,y:2*s)
            d=mp.mpf(second['delta'].numerator)/second['delta'].denominator
            self.assertLess(abs(second['value']-first['value']-d*d),mp.mpf('1e-70'))
            self.assertGreater(abs(d*d),mp.mpf('1e-34'))

    def test_cubic_exact_remainder(self):
        with mp.workdps(80):
            r=0.7; sf=float(Decimal(str(r))**2); yf=float(sf**3)
            out=transport_endpoint_second_order(r,sf,yf,lambda s,y:3*s*s)
            d=mp.mpf(out['delta'].numerator)/out['delta'].denominator
            target=exact_binary(yf)+3*exact_binary(sf)**2*d+3*exact_binary(sf)*d*d+d**3
            self.assertLess(abs(target-out['value']-d**3),mp.mpf('1e-65'))

    def test_state_dependent_rhs(self):
        with mp.workdps(80):
            r=0.85; sf=float(Decimal(str(r))**2); yf=0.125
            out=transport_endpoint_second_order(r,sf,yf,lambda s,y:3*y+s)
            self.assertLess(abs(out['acceleration']-(9*exact_binary(yf)+3*exact_binary(sf)+1)),mp.mpf('1e-65'))

    def test_exact_binary_gap(self):
        self.assertEqual(decimal_square_target(0.85)-Fraction.from_float(float(Decimal("0.85")**2)),Fraction(-7,225179981368524800))
        self.assertEqual(decimal_square_target(0.7)-Fraction.from_float(float(Decimal("0.7")**2)),Fraction(1,112589990684262400))

    def test_precision_guard(self):
        with self.assertRaises(ValueError):
            transport_endpoint_second_order(0.85,0.85**2,1.0,lambda s,y:s,dps=20)

if __name__=='__main__': unittest.main()
