import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_physical_correlated_replay import (
    authenticate_originals,gu_on_original_tube,run)


class PhysicalCorrelatedReplayTests(unittest.TestCase):
    def test_four_original_sha_authenticated(self):
        self.assertEqual(len(authenticate_originals()),4)

    def test_gu_same_tube_outward(self):
        lo,hi=gu_on_original_tube(256)
        self.assertLess(lo,hi)
        self.assertLess(hi,-Q(99,100))

    def test_full_physical_256_cell_replay(self):
        result=run(256)
        self.assertTrue(result['DOP853_success'])
        self.assertEqual(result['step55_barrier_cells'],256)
        self.assertEqual(result['total_correlated_cells'],256*result['DOP853_steps'])
        self.assertLess(result['gu_upper_float'],-0.99)
        self.assertLess(result['terminal_error_bound_float'],5e-6)
        self.assertGreater(result['terminal_error_bound_float'],0)
        self.assertEqual(result['GATE_2B'],'OPEN')
        self.assertEqual(result['JANUS_R'],'NOT_VALIDATED')
        self.assertEqual(result['Step58_A_B_E'],'NOT_CERTIFIED')


if __name__=='__main__': unittest.main()
