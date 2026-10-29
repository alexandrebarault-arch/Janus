import unittest
from numerics.hr_step68ad_b3c3d6_step55_k_chart import certificate

class Step55KChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certificate()
    def test_exact_bernstein_positive(self):
        self.assertEqual(self.c['T_bernstein_signs'],['POS']*5)
    def test_exact_monotonicity(self):
        self.assertEqual(self.c['T_bernstein_adjacent_differences'],['NEG']*4)
    def test_k_lower(self):
        self.assertEqual(self.c['K_over_r2_strict_lower'],'9/40')
        self.assertTrue(self.c['K_outer_positive'])
    def test_center_and_shift(self):
        self.assertEqual(self.c['z_outer'],'17/5000')
        self.assertEqual(self.c['GATE_2B'],'OPEN')
        self.assertEqual(self.c['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
