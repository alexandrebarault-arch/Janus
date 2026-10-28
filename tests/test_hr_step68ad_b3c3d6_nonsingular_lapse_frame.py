"""Non-independent regression wrappers for the exact lapse frame certificate."""
import unittest
from numerics.hr_step68ad_b3c3d6_nonsingular_lapse_frame import certificate,toy_crossing,original_witness_frame,audit


class LapseFrameTest(unittest.TestCase):
    def test_symbolic_equivalence(self):
        self.assertEqual(certificate(),8)

    def test_positive_toy_crossing(self):
        self.assertEqual(toy_crossing(),6)

    def test_original_pointwise_witness_no_division_by_bm(self):
        self.assertEqual(original_witness_frame()['B_M'],'0')

    def test_scope_and_gate(self):
        x=audit()
        self.assertEqual((x['gate'],x['janus']),('OPEN','NOT_VALIDATED'))
        self.assertIn('NOT_STEP55',x['scope'])


if __name__=='__main__':
    unittest.main()
