"""Non-independent tests of the Step55 algebraic transcription."""
import unittest
from numerics.hr_b3c3d6_step55_primary_shell_audit import exact_shell, SOURCE_BLOBS

class ShellAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=exact_shell()
    def test_exact_zero_residuals(self):
        self.assertEqual(self.result['exact_residuals_zero'],9)
    def test_negative_controls(self):
        self.assertEqual(self.result['negative_controls'],2)
    def test_outer_factor(self):
        from fractions import Fraction
        x=Fraction(self.result['outer_factor'])
        self.assertTrue(-11<x<-10)
    def test_pinned_original_sources(self):
        self.assertEqual(self.result['source_blobs'],SOURCE_BLOBS)
        self.assertEqual(self.result['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
