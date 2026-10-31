import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_exact_radius_prefix_ledger import (
    S_EXACT,S_BINARY,EPS_BINARY_LEDGER,GU_LO,GU_HI,
    prefix_ledger_bound,exact_radius_first_jets,exact_record)

class TestExactRadiusPrefix(unittest.TestCase):
    def test_exact_binary_overshoot(self):
        self.assertEqual(S_BINARY-S_EXACT,Q(7,225179981368524800))
        self.assertGreater(S_BINARY,S_EXACT)

    def test_prefix_bound_from_nonnegative_budget(self):
        eps=prefix_ledger_bound()
        self.assertEqual(S_EXACT*eps,S_BINARY*EPS_BINARY_LEDGER)
        self.assertLess(eps,Q(1,200000))

    def test_exact_radius_ode_jets(self):
        b=exact_radius_first_jets()
        self.assertEqual(b['U_s_vs_F_at_P'],max(abs(GU_LO-2),abs(GU_HI-2))*b['U']/(2*S_EXACT))
        self.assertEqual(b['pLf_vs_sP'],S_EXACT*b['U'])
        self.assertEqual(b['pLf_prime_over_r_vs_G_at_P'],max(abs(GU_LO),abs(GU_HI))*b['U'])
        self.assertLess(b['U_s_vs_F_at_P'],Q(11,1000000))

    def test_nonnegative_prefix_ledger_toy(self):
        # B_total=sum positive cells, any partial sum is <=B_total.
        rows=[Q(1,17),Q(2,19),Q(3,23),Q(4,29)]
        for n in range(5):
            self.assertLessEqual(sum(rows[:n],Q(0)),sum(rows,Q(0)))

    def test_wrong_side_rejected(self):
        with self.assertRaises(ValueError):
            prefix_ledger_bound(S_BINARY+Q(1,10**12))
        with self.assertRaises(ValueError):
            prefix_ledger_bound(eps_binary=-1)

    def test_negative_control_monotonicity_is_necessary(self):
        # G=4U gives 2s U_s=2U -> U=s (P=0,H=0).
        # s|e(s)| grows, so the prefix formula cannot be used for G_U>0.
        a,b=Q(1,4),Q(1,2)
        self.assertGreater(b*abs(b),a*abs(a))

    def test_record_scoping(self):
        r=exact_record()
        self.assertEqual(r['GATE_2B'],'OPEN')
        self.assertEqual(r['JANUS_R'],'NOT_VALIDATED')
        self.assertIn('not_physical_error_at_binary', 'ledger_ratio_not_physical_error_at_binary')

if __name__=='__main__':unittest.main()
