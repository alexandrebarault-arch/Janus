import unittest
from fractions import Fraction as Q
from numerics.hr_step68ad_c2d2e5b3b2c2b1_f_chart_coefficient import (
    S, A, B, CF, KF, MF, Z1, certificate, bernstein_on_closed_interval, mul)


class FChartTests(unittest.TestCase):
    def setUp(self):
        self.c = certificate()

    def test_bernstein_linear(self):
        self.assertEqual(bernstein_on_closed_interval([Q(2), Q(3)], Q(4)), [Q(2), Q(14)])

    def test_bernstein_quadratic(self):
        self.assertEqual(bernstein_on_closed_interval([Q(1), Q(0), Q(1)], Q(2)), [Q(1), Q(1), Q(5)])

    def test_multiply(self):
        self.assertEqual(mul([Q(1), Q(1)], [Q(1), Q(-1)]), [Q(1), Q(0), Q(-1)])

    def test_t_bernstein_positive(self):
        self.assertEqual(len(self.c['T_bernstein']), 5)
        self.assertTrue(all(Q(v)>Q(1, 10) for v in self.c['T_bernstein']))

    def test_t_bernstein_upper(self):
        self.assertTrue(all(Q(v)<Q(11, 100) for v in self.c['T_bernstein']))

    def test_f_sfr_positive(self):
        self.assertGreater(Q(self.c['Sfr_lower']), Q(23, 100))

    def test_denom_positive(self):
        self.assertGreater(Q(self.c['f_dust_denom_lower']), Q(3, 4))

    def test_denom_order(self):
        self.assertLess(Q(self.c['f_dust_denom_lower']), Q(self.c['f_dust_denom_upper']))

    def test_shift_root(self):
        self.assertGreater(Q(self.c['sqrt_1_minus_z2_lower']), Q(999, 1000))

    def test_cv_coefficient(self):
        self.assertGreater(Q(self.c['minus_CV_over_r_lower']), Q(372))

    def test_s_domain(self):
        self.assertEqual(S, Q(17,20)**2)

    def test_f_momentum_dust_reduction(self):
        # fac=pLf/(2*Mf2*Sf*Sfr), pLf=sU, Sf=rLf, tf=r KF Lf.
        # fac*tf=s*U*KF/(2*Mf2*Sfr), checked by symbolic cancellation.
        import sympy as sp
        r,u,lf,sfr=sp.symbols('r u lf sfr', nonzero=True)
        fac=(r**2*u)/(2*sp.Rational(MF.numerator,MF.denominator)*r*lf*sfr)
        tf=r*sp.Rational(KF.numerator,KF.denominator)*lf
        expected=r**2*u*sp.Rational(KF.numerator,KF.denominator)/(2*sp.Rational(MF.numerator,MF.denominator)*sfr)
        self.assertEqual(sp.cancel(fac*tf-expected), 0)

    def test_step46_affine_coefficient_reduction(self):
        import sympy as sp
        r,lf,sfr,t,beta,denom,root=sp.symbols('r lf sfr t beta denom root', nonzero=True)
        mg=sp.Integer(1); mf=sp.Rational(MF.numerator,MF.denominator)
        m2=sp.Rational('23.3348939346')
        # At=r^2*T; Sf=r*Lf; original C_V formula Step46.
        cv= -m2*mg*(r**2*t)*root/(2*mf*r*lf)*lf*beta/(sfr*denom)
        reduced=-r*m2*t*root*beta/(2*mf*sfr*denom)
        self.assertEqual(sp.cancel(cv-reduced),0)


if __name__ == '__main__':
    unittest.main()
