"""Non-independent numerical regression tests, NOT a global interval proof."""
import contextlib
import io
import unittest
import mpmath as mp
from numerics.hr_step55_global_barrier import certify_global_barrier
from numerics.hr_b3c3d6_full_original_step58_point_probe import main, source_checks

class OriginalStep58Step55NumericalProbe(unittest.TestCase):
    def test_five_source_blob_hashes(self):
        self.assertEqual(len(source_checks()),5)

    def test_original_step55_global_barrier_replay(self):
        report=certify_global_barrier(cells=256)
        self.assertEqual(report['cells'],256)
        self.assertTrue(report['Step54_tube_hypothesis_proved_for_exact_radial_solution'])

    def test_full_original_step58_four_radial_points(self):
        for radius in (0.25,0.5,0.7,0.85):
            with self.subTest(radius=radius),contextlib.redirect_stdout(io.StringIO()):
                x=main(radius)
            self.assertLess(max(abs(v) for v in x['shell_residuals'].values()),1e-30)
            n=x['coefficients']['N'];m=x['coefficients']['M']
            self.assertGreater(n['0'],0)
            self.assertLess(m['0'],0)
            self.assertLess(max(abs(n['1']),abs(m['1']),abs(n['2']),abs(m['2'])),1e-30)
            self.assertTrue(0.518 < -n['0']/m['0'] < 0.522)
            self.assertEqual(x['GATE_2B'],'OPEN')
            self.assertEqual(x['JANUS_R'],'NOT_VALIDATED')

    def test_off_shell_negative_controls(self):
        with contextlib.redirect_stdout(io.StringIO()):
            x=main(0.85)
        self.assertLess(x['negative_controls']['pSgr']['N'],-0.08)
        self.assertLess(x['negative_controls']['pSgr']['M'],-0.001)
        self.assertLess(x['negative_controls']['pSf']['N'],-0.03)

    def test_high_precision_70_digit_roundoff_scaling(self):
        with mp.workdps(70),contextlib.redirect_stdout(io.StringIO()):
            x=main(0.85)
        self.assertLess(max(abs(v) for v in x['shell_residuals'].values()),1e-60)
        self.assertLess(max(abs(x['coefficients'][sector][jet]) for sector in ('N','M') for jet in ('1','2')),1e-60)

if __name__=='__main__':unittest.main()
