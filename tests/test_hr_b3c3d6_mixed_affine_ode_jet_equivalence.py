import unittest
import sympy as sp
from numerics.hr_b3c3d6_mixed_affine_ode_jet_equivalence import exact_jet_identities,smooth_field_jet_guard

class MixedAffineODEJetEquivalence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d=exact_jet_identities()

    def test_pLf_value(self):
        self.assertEqual(self.d['pLf_value_mixed_minus_quad'],0)

    def test_pLf_first_jet(self):
        self.assertEqual(self.d['pLf_first_mixed_minus_quad'],0)

    def test_pLfr_value(self):
        self.assertEqual(self.d['pLfr_value_mixed_minus_quad'],0)

    def test_pLfr_first_jet(self):
        self.assertEqual(self.d['pLfr_first_mixed_minus_quad'],0)

    def test_affine_holonomic_gap_nonzero(self):
        d=self.d
        values={d['r0']:sp.Rational(1,2),d['u0']:sp.Rational(1,3),
                d['u1']:sp.Rational(1,5),d['gs']:sp.Rational(2,7),d['gu']:-sp.Rational(1,2)}
        self.assertEqual(d['u2'].subs(values),-sp.Rational(43,35))
        self.assertEqual(d['pLfr_first_mixed_minus_holonomic_affine'].subs(values),-sp.Rational(43,140))
        self.assertEqual(d['pLfr_first_holonomic_affine_minus_quad'].subs(values),sp.Rational(43,140))

    def test_nonholonomic_pLf_second_jet_gap(self):
        d=self.d
        self.assertEqual(sp.factor(d['pLf_second_holonomic_affine_minus_quad']+4*d['r0']**4*d['u2']),0)

    def test_rational_pf_value(self):
        self.assertEqual(smooth_field_jet_guard()['pf_0'],0)

    def test_rational_pf_first(self):
        self.assertEqual(smooth_field_jet_guard()['pf_1'],0)

    def test_rational_pSf_value(self):
        self.assertEqual(smooth_field_jet_guard()['pSf_0'],0)

    def test_rational_pSf_first(self):
        self.assertEqual(smooth_field_jet_guard()['pSf_1'],0)

if __name__=='__main__':unittest.main()
