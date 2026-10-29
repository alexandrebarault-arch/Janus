import unittest
import sympy as sp
from numerics.hr_b3c3d6_cubic_jet_order_certificate import certificate, exact_polynomial_witness

class CubicOrderCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.c=certificate()
    def test_zero_order_ode(self): self.assertEqual(sp.cancel(self.c['ode_residual_coefficients'][0]),0)
    def test_first_order_ode(self): self.assertEqual(sp.cancel(self.c['ode_residual_coefficients'][1]),0)
    def test_second_order_ode(self): self.assertEqual(sp.cancel(self.c['ode_residual_coefficients'][2]),0)
    def test_third_order_defect(self):
        s0,_,_=self.c['symbols'];self.assertEqual(sp.cancel(self.c['ode_residual_coefficients'][3]+s0*self.c['fourth_jet']/3),0)
    def test_radial_third_defect(self):
        _,_,r0=self.c['symbols'];self.assertEqual(sp.cancel((self.c['radial_third_defect']+16*r0**6*self.c['fourth_jet']).subs(self.c['symbols'][0],r0*r0)),0)
    def test_nonzero_analytic_ode_witness(self):
        w=exact_polynomial_witness();self.assertNotEqual(w['radial_third_defect'],0)

if __name__=='__main__':unittest.main()
