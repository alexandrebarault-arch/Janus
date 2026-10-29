"""Pending full-original Step58 integration checks on cubic Step55 jets.

These tests were PUBLISHED but NOT EXECUTED in the authoring session,
because the complete authenticated original modules were unavailable locally.
Do not infer numerical coefficient cancellation from these guards.
"""
import contextlib
import io
import unittest
from numerics.hr_b3c3d6_corrected_step58_point_probe_candidate import main, source_checks

class CorrectedStep58CandidateIntegration(unittest.TestCase):
    def test_original_five_source_hashes(self):
        self.assertEqual(len(source_checks()),5)

    def test_four_radii_holonomic_and_full_operator(self):
        for r in (0.25,0.5,0.7,0.85):
            with self.subTest(r=r),contextlib.redirect_stdout(io.StringIO()):
                report=main(r)
            self.assertEqual(report['ode_jet_map'],'CUBIC_STEP55_ODE_CONSISTENT_THROUGH_ORDER_3')
            self.assertLess(max(abs(float(v)) for v in report['holonomic_residuals']),1e-30)
            self.assertLess(max(abs(v) for v in report['shell_residuals'].values()),1e-30)
            self.assertEqual(set(report['coefficients']),{'N','M'})
            for sector in ('N','M'):
                self.assertEqual(set(report['coefficients'][sector]),{'0','1','2'})
            self.assertEqual(report['GATE_2B'],'OPEN')
            self.assertEqual(report['JANUS_R'],'NOT_VALIDATED')

    def test_actual_affine_defect_at_outer_radius_is_reported(self):
        with contextlib.redirect_stdout(io.StringIO()):
            report=main(0.85)
        self.assertIn('second',report['affine_jet_defects'])
        self.assertIn('third',report['affine_jet_defects'])

if __name__=='__main__': unittest.main()
