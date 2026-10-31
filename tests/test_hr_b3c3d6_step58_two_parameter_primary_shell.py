import unittest
import sympy as S
from numerics.hr_b3c3d6_step58_two_parameter_primary_shell import authenticate, exact_family, certificate

class TestTwoParameterPrimaryShell(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a, cls.b, cls.solved, cls.r = exact_family()

    def test_byte_authenticated_originals(self):
        self.assertTrue(authenticate())

    def test_four_primary_and_first_jet_constraints(self):
        self.assertTrue(all(self.r[k] == 0 for k in ('Fz','Fz_r','Hg','Hg_r')))

    def test_positive_chart_and_dust(self):
        self.assertEqual(self.r['K'], 1)
        self.assertEqual(certificate()['positive_dust'], ['pg=7/4','pf=1'])

    def test_secondary_nonzero_generic(self):
        self.assertEqual(S.cancel(self.r['C']+(25*self.a+24*self.b+12)/20),0)
        self.assertEqual(self.r['C'].subs({self.a:0,self.b:1}), -S.Rational(9,5))

    def test_BN_exact_secondary_relation(self):
        self.assertEqual(S.cancel(self.r['B_N']+3*(25*self.a+24*self.b+12)/100),0)
        self.assertEqual(S.cancel(self.r['B_N']-S.Rational(3,5)*self.r['C']),0)

    def test_other_lapse_jet_coefficients_zero(self):
        self.assertTrue(all(self.r[k]==0 for k in ('B_M','E_N','E_M')))

    def test_C_zero_curve_nontrivial(self):
        curve=-(25*self.a+12)/24
        self.assertEqual(S.cancel(self.r['C'].subs(self.b,curve)),0)
        self.assertEqual(S.cancel(self.r['B_N'].subs(self.b,curve)),0)

    def test_two_independent_parameter_derivatives(self):
        self.assertEqual(S.diff(self.r['C'],self.a),-S.Rational(5,4))
        self.assertEqual(S.diff(self.r['C'],self.b),-S.Rational(6,5))

    def test_scientific_scope_not_exaggerated(self):
        c=certificate()
        self.assertEqual(c['universal_B_N_factorization'],'NOT_PROVED')
        self.assertEqual((c['GATE_2B'],c['JANUS_R']),('OPEN','NOT_VALIDATED'))

if __name__=='__main__': unittest.main()
