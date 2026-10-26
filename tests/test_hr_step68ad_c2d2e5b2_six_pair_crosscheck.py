import unittest
import numpy as np
from hr_step68ad_c2d2e5b2_six_pair_crosscheck import q_fields,deriv,densities,ibp_densities,smear,bracket,bracket_ibp,action_difference,sector_boundary,audit

class SixPairOriginalIBPAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=audit()

    def test_six_pairs_and_two_dust(self):
        for row in self.rows:
            self.assertEqual(len(row['pair_original']),6)
            self.assertEqual(len(row['pair_ibp']),6)
            self.assertGreater(abs(row['pair_original'][2]),1e-6)
            self.assertGreater(abs(row['pair_original'][4]),1e-5)
            self.assertEqual(row['pair_original'][5],0.0)  # tf/pf cross bracket vanishes for this benchmark, not omitted

    def test_envelope_theorem_frozen_vs_reduced(self):
        for row in self.rows:
            self.assertLess(abs(row['frozen_shift_bracket_difference']),1e-12)
            self.assertLess(max(abs(a-b) for a,b in zip(row['pair_original'],row['pair_frozen_shift'])),1e-12)

    def test_shift_equation_regular(self):
        for row in self.rows:
            self.assertGreater(row['K_min'],0)
            self.assertLess(row['shift_equation_max'],1e-12)

    def test_negative_K_rejected(self):
        r=np.linspace(.1,.9,41);q=q_fields(r)
        from hr_step68ad_c2d2e5b2_six_pair_crosscheck import BETA
        old=BETA
        import hr_step68ad_c2d2e5b2_six_pair_crosscheck as oracle
        try:
            oracle.BETA=(.2,-1.3,-.35,-.4,-.17)
            with self.assertRaisesRegex(ValueError,'K>0'): densities(q,r[1]-r[0])
            with self.assertRaisesRegex(ValueError,'K>0'): ibp_densities(q,r[1]-r[0],*smear(r))
        finally: oracle.BETA=old

    def test_compact_boundary_zero(self):
        for row in self.rows:
            self.assertEqual(row['compact_boundary'],[0.,0.])

    def test_compact_action_convergence(self):
        err=[max(abs(x) for x in row['compact_action_difference']) for row in self.rows]
        self.assertTrue(all(err[i+1]<err[i]/3.7 for i in range(3)),err)

    def test_noncompact_boundary_nonzero(self):
        for row in self.rows:
            self.assertGreater(row['noncompact_boundary'][0],2)
            self.assertGreater(row['noncompact_boundary'][1],.6)

    def test_noncompact_boundary_residual_convergence(self):
        err=[max(abs(x) for x in row['noncompact_boundary_residual']) for row in self.rows]
        self.assertTrue(all(err[i+1]<err[i]/3.7 for i in range(3)),err)

    def test_bracket_convergence_to_ibp(self):
        err=[abs(row['bracket_difference']) for row in self.rows]
        self.assertTrue(all(err[i+1]<err[i]/3.7 for i in range(3)),err)

    def test_bracket_nonzero_off_shell(self):
        for row in self.rows:
            self.assertGreater(row['bracket_original'],.04)
            self.assertLess(row['bracket_original'],.05)

    def test_individual_pair_convergence(self):
        for pair in [0,1,2,3,4]:
            err=[abs(row['pair_original'][pair]-row['pair_ibp'][pair]) for row in self.rows]
            self.assertTrue(all(err[i+1]<err[i]/3.3 for i in range(3)),(pair,err))

    def test_no_fake_dirac_rank(self):
        # A nonzero smeared mixed bracket does not specify a complete Dirac matrix.
        self.assertNotIn('dirac_rank',self.rows[-1])

if __name__=='__main__': unittest.main()
