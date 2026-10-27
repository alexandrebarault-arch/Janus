"""Replay test for JANUS d2d2b1; not independent of source assertions."""
import unittest
from numerics.hr_step68ad_c2d2e5b3b2c2b2d2d2b1_clock_translation import certificate

class ClockTranslationReplay(unittest.TestCase):
    def test_exact_replay(self):
        result=certificate()
        self.assertEqual(result['assertions_passed'],48)
        self.assertEqual(result['assertions_failed'],0)
        self.assertEqual(result['boundary_two_form_on_clock_plane'].split()[0],'0')
        self.assertEqual(result['scientific_status']['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':
    unittest.main()
