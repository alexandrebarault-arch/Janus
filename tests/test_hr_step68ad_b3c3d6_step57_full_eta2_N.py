"""Non-independent regression guards for corrected complete eta'' coefficient."""
import unittest
from fractions import Fraction as F
from numerics.hr_step68ad_b3c3d6_step57_full_eta2_N import I,coefficients,consts,certificate,symbolic_residuals

class Step57FullEta2N(unittest.TestCase):
    def test_original_step45_contraction(self):
        self.assertEqual(symbolic_residuals(),3)
    def test_uniform_outward_enclosure(self):
        result=certificate(256)
        self.assertEqual(result['rational_cell_sign_guards'],256*7+3)
    def test_center_sign_and_curvature(self):
        c=coefficients(I.c(0),consts())
        self.assertTrue(c['cN_over_s'].gt(6))
        self.assertTrue(c['cM_over_s'].lt(-10))
        self.assertTrue(c['cNprime_over_r'].lt(-F(17,2)))
        rho=I.hull(F(1037,2000),F(2593,5000))
        n2=-(c['cN_over_s']+c['cM_over_s']*rho)/(2*c['cNprime_over_r'])
        self.assertTrue(n2.gt(F(1,25)) and n2.lt(F(1,20)))
    def test_negative_control_zero_curvature(self):
        c=coefficients(I.c(0),consts())
        rho=I.hull(F(1037,2000),F(2593,5000))
        self.assertTrue((c['cN_over_s']+c['cM_over_s']*rho).gt(0))
    def test_fail_closed_bad_interval(self):
        with self.assertRaises(ZeroDivisionError):
            I.hull(-1,1).inv()
if __name__=='__main__':unittest.main()
