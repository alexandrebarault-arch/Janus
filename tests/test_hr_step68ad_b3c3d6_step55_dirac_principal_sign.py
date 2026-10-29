"""Non-independent regression tests for the Step55/Step57 sign certificate."""
import unittest
from pathlib import Path
from numerics.hr_step68ad_b3c3d6_step55_dirac_principal_sign import certificate,verify_original_blob

class Step55DiracPrincipalSign(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.report=certificate()
    def test_M_strict_uniform(self):
        self.assertEqual(self.report['eta2_M_strict_bound'],'eta2_M < -10*r^2')
    def test_Nprime_strict_uniform(self):
        self.assertEqual(self.report['eta2_Nprime_strict_bound'],'eta2_Nprime < -(19999/10000)*r')
    def test_center_scaling(self):
        self.assertEqual(self.report['center_limits']['eta2_Nprime_over_r'],'-2')
    def test_not_step58_dirac(self):
        self.assertFalse(self.report['original_step58_outer_probe_executed'])
        self.assertFalse(self.report['Dirac_rank_certified'])
    def test_blob_negative_guard(self):
        with self.assertRaises(ValueError):
            verify_original_blob(Path(__file__), '0'*40)

if __name__=='__main__': unittest.main()
