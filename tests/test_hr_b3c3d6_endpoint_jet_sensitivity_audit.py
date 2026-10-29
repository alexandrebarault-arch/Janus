import unittest
from numerics.hr_b3c3d6_endpoint_jet_sensitivity_audit import certificate

class JetSensitivityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.data=certificate()
    def test_eight_exact_jet_identities(self):
        self.assertEqual(len(self.data['residuals']),8)
        self.assertTrue(all(v==0 for v in self.data['residuals'].values()))
    def test_generic_field_second_jet(self):
        self.assertEqual(self.data['generic_residual'],0)
    def test_first_jets_unchanged(self):
        self.assertTrue(all(self.data['toy_deltas'][k]==0 for k in ('pLf_q','pLf_q1','pLfr_q','pLfr_q1')))
    def test_second_jets_change(self):
        self.assertTrue(all(self.data['toy_deltas'][k]!=0 for k in ('pLf_q2','pLfr_q2')))
    def test_third_jets_change(self):
        self.assertTrue(all(self.data['toy_deltas'][k]!=0 for k in ('pLf_q3','pLfr_q3')))

if __name__=='__main__':unittest.main()
