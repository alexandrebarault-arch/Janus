import unittest
from numerics.hr_step68ad_b3c3d6_authentic_shift_jet_chart_witness import original_witness

class OriginalShiftJetChartWitness(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=original_witness()
    def test_shift_jets_and_primaries(self):
        self.assertEqual(len(self.result['constraints_zero']),7)
    def test_exact_lapse_coefficients(self):
        self.assertEqual(self.result['operator_N'],['1293/250','224/125','0'])
        self.assertEqual(self.result['operator_M'],['-79093/12500','0','0'])
    def test_positive_chart(self):
        self.assertEqual(self.result['K'],'1')
        self.assertEqual(self.result['z'],'3/5')
        self.assertTrue(self.result['B_M_zero'])
    def test_gate_not_validated(self):
        self.assertEqual(self.result['GATE_2B'],'OPEN')
        self.assertEqual(self.result['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
