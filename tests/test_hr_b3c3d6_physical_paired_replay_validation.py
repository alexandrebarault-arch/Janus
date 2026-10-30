"""Physical Step58 replay regression: opt-in, never a validation of JANUS."""
import os
import unittest
import mpmath as mp
from numerics.hr_b3c3d6_physical_paired_replay_validation import (
    validate, printed_coefficients, physical_sensitivity)


class ValidationUnitTests(unittest.TestCase):
    def test_reject_incomplete_six_coefficients(self):
        with self.assertRaisesRegex(AssertionError, 'incomplete'):
            printed_coefficients({'original_probe_stdout':'N 0 1\nM 0 -2\n'})

    def test_reject_duplicate_coefficient(self):
        with self.assertRaisesRegex(AssertionError, 'duplicate'):
            printed_coefficients({'original_probe_stdout':'N 0 1\nN 0 2\n'})

    def test_reject_unvalidated_gate_promotion(self):
        with self.assertRaisesRegex(AssertionError, 'gate'):
            validate({'GATE_2B':'CLOSED','JANUS_R':'VALIDATED','radii':[]})

    def test_reject_missing_four_radii(self):
        with self.assertRaisesRegex(AssertionError, 'four'):
            validate({'GATE_2B':'OPEN','JANUS_R':'NOT_VALIDATED','radii':[]})

    def test_physical_sensitivity_sign_at_r_half(self):
        from numerics import hr_b3c3d6_corrected_step58_point_probe_candidate as c
        with mp.workdps(45):
            self.assertLess(physical_sensitivity(0.5, c.U0), 0)


@unittest.skipUnless(os.environ.get('JANUS_RUN_PHYSICAL_STEP58') == '1',
                     'physical Step58 original replay is opt-in')
class PhysicalIntegrationTest(unittest.TestCase):
    def test_full_original_four_radius_paired_replay(self):
        from numerics.hr_b3c3d6_paired_original_step58_four_radii import run_all
        result = validate(run_all())
        self.assertEqual(len(result['radii']), 4)
        self.assertEqual(result['GATE_2B'], 'OPEN')
        self.assertTrue(all(x['mixed_quadratic_cubic_identical_22digit'] for x in result['radii']))


if __name__ == '__main__':
    unittest.main()
