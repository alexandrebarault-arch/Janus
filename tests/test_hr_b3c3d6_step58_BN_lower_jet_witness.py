import unittest
import sympy as S
from numerics.hr_b3c3d6_step58_BN_lower_jet_witness import authenticate, exact_family, certificate

class TestBNLowerJetWitness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t, cls.f = exact_family()
        cls.report = certificate()

    def test_original_step45_step58_git_blobs(self):
        self.assertTrue(authenticate())

    def test_chart_and_positive_dust(self):
        self.assertEqual(self.f['K'], 1)
        self.assertEqual(self.report['positive_dust'], ['7/4','1'])

    def test_other_constraints_and_derivatives_zero_identically(self):
        for key in ('Fz','Fz_r','Hg_r','Hf','C'):
            self.assertEqual(self.f[key], 0, key)

    def test_BM_and_EM_zero(self):
        self.assertEqual(self.f['B_M'], 0)
        self.assertEqual(self.f['E_M'], 0)

    def test_nonzero_lower_residual_when_Hg_not_zero(self):
        self.assertEqual(self.f['lower_residual'], -S.Rational(416,125)*self.t)
        self.assertEqual(self.f['lower_residual'].subs(self.t,1), -S.Rational(416,125))

    def test_exact_relation_to_primary_Hg_on_this_slice_only(self):
        self.assertEqual(self.f['Hg'], 2*self.t)
        self.assertEqual(S.cancel(self.f['lower_residual']+S.Rational(208,125)*self.f['Hg']),0)
        self.assertEqual(S.cancel(self.f['E_N']+S.Rational(16,25)*self.f['Hg']),0)

    def test_full_primary_restored_at_t_zero(self):
        for key in ('Hg','B_N','E_N'):
            self.assertEqual(self.f[key].subs(self.t,0),0)

    def test_scope_guard(self):
        self.assertEqual(self.report['universal_B_N_factorization'], 'NOT_PROVED_OR_REFUTED_ON_FULL_PRIMARY_SHELL')
        self.assertEqual((self.report['GATE_2B'],self.report['JANUS_R']),('OPEN','NOT_VALIDATED'))

if __name__ == '__main__':
    unittest.main()
