"""Exact decimal-square regression, not a physical Step58 coefficient replay."""
import unittest
from decimal import Decimal, localcontext
from fractions import Fraction
from numerics.hr_b3c3d6_decimal_radius_endpoint import endpoint_s, old_endpoint_error, new_endpoint_error
from numerics.hr_b3c3d6_exact_binary_rhs_transport import decimal_square_target, transport_endpoint


class DecimalContextInvariance(unittest.TestCase):
    def test_nontrivial_square_exact_independent_of_context(self):
        r='0.1234567890123456'
        expected=Fraction(Decimal(r))**2
        for prec in (6,7,16,28,50):
            with self.subTest(precision=prec), localcontext() as ctx:
                ctx.prec=prec
                sf, target=endpoint_s(r)
                self.assertEqual(Fraction(target),expected)
                self.assertEqual(decimal_square_target(r),expected)
                self.assertEqual(sf,float(expected))
                self.assertEqual(new_endpoint_error(r),Fraction.from_float(sf)-expected)
                self.assertEqual(old_endpoint_error(r),Fraction.from_float(float(r)**2)-expected)

    def test_regression_default_decimal_rounding_was_real(self):
        r=Decimal('0.1234567890123456')
        with localcontext() as ctx:
            ctx.prec=28
            old=Fraction(r*r)
        self.assertNotEqual(old,Fraction(r)**2)

    def test_four_original_radii_unchanged(self):
        for r in ('0.25','0.5','0.7','0.85'):
            with self.subTest(radius=r):
                self.assertEqual(Fraction(endpoint_s(r)[1]),Fraction(Decimal(r))**2)
                self.assertEqual(decimal_square_target(r),Fraction(Decimal(r))**2)

    def test_transport_delta_uses_exact_decimal_square(self):
        r='0.1234567890123456'
        sf=endpoint_s(r)[0]
        with localcontext() as ctx:
            ctx.prec=7
            out=transport_endpoint(r,sf,1.0,lambda s,u:s*0+3*u)
        self.assertEqual(out['delta'],Fraction(Decimal(r))**2-Fraction.from_float(sf))

    def test_nonpositive_and_nonfinite_rejected(self):
        for r in ('0','-1','NaN','Infinity'):
            with self.subTest(radius=r):
                with self.assertRaises(ValueError):endpoint_s(r)
                with self.assertRaises(ValueError):decimal_square_target(r)

    def test_exact_transport_dyadic_identity(self):
        for r in ('0.25','0.5'):
            sf=endpoint_s(r)[0]
            self.assertEqual(transport_endpoint(r,sf,2.0,lambda s,u:3*u)['delta'],0)

if __name__=='__main__':unittest.main()
