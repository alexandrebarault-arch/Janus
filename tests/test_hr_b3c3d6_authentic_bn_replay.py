"""Compulsory authentic-source integration guards for the BN ideal proof."""
import unittest
from numerics.hr_b3c3d6_authentic_bn_replay import SOURCES, run, verify_blob_provenance

class TestAuthenticBNReplay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cert = run()

    def test_source_blobs_authenticated(self):
        self.assertEqual(verify_blob_provenance(), SOURCES)

    def test_original_ward_nine_residuals(self):
        self.assertEqual(self.cert["step45_original_Ward_nine_residuals"], "EXACT_ZERO")

    def test_original_highest_lapse_jet(self):
        self.assertEqual(self.cert["step58_original_highest_lapse_E_N_E_M"], "EXACT_ZERO_ON_Fz_Hg")

    def test_original_bn_first_jet_ideal(self):
        self.assertEqual(self.cert["step58_original_B_N_identity_on_Fz_Hg"], "EXACT")
        self.assertEqual(self.cert["on_full_shell_Fz_Hg_Hgr_C_zero_B_N"], "EXACT_ZERO")

    def test_avoids_physical_overclaim(self):
        self.assertEqual(self.cert["physical_step55_six_step58_coefficient_interval_enclosures"], "NOT_CERTIFIED")
        self.assertEqual(self.cert["JANUS_R"], "NOT_VALIDATED")

if __name__ == "__main__":
    unittest.main()
