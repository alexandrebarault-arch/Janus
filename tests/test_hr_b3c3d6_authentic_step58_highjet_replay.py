import unittest
from fractions import Fraction as F
from numerics.hr_b3c3d6_authentic_step58_highjet_replay import replay,outer_geometry_factor,source_hashes

class TestAuthenticHighJet(unittest.TestCase):
    def test_byte_authentic_originals(self):
        self.assertEqual(len(source_hashes()),2)
    def test_original_operator_executed(self):
        self.assertTrue(replay()['original_Step58_executed'])
    def test_outer_factor_negative(self):
        self.assertLess(outer_geometry_factor(),F(-10,1))
    def test_no_false_global_claim(self):
        d=replay()
        self.assertFalse(d['original_Step58_full_six_coefficients_on_Step55_executed'])
        self.assertEqual(d['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
