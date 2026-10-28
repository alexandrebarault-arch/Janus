"""Replays the same b3c3b symbolic proof; not independent validation."""
import unittest
from numerics.hr_step68ad_b3c3b_cred_lie_identity import run

class TestReducedLie(unittest.TestCase):
    def test_exact_covariance_and_reduction(self):
        r=run()
        self.assertEqual(r['exact_assertions'],34)
        self.assertEqual(r['C_red_weight'],1)
        self.assertEqual(r['GATE_2B'],'OPEN')
        self.assertEqual(r['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
