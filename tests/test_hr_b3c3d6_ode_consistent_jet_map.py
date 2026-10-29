"""Independent toy ODE checks only; full original Step55/58 integration not run here."""
import unittest
import mpmath as mp
from numerics.hr_b3c3d6_ode_consistent_jet_map import endpoint_jets,cubic_U

class ODEJetMapTests(unittest.TestCase):
    def test_toy_quadratic_exact(self):
        with mp.workdps(50):
            s=mp.mpf(1)/4;u=mp.mpf(1)/2
            j=endpoint_jets(lambda s,u:s*s+u*u,s,u)
            self.assertEqual(j['U_s'],mp.mpf(-11)/8)
            self.assertEqual(j['U_ss'],mp.mpf(37)/4)
            self.assertEqual(j['affine_defect_second'],mp.mpf(37)/16)
            self.assertEqual(j['affine_defect_third'],mp.mpf(1369)/64)
            self.assertLess(max(map(abs,j['holonomic_residuals'])),mp.mpf('1e-45'))

    def test_exact_affine_solution(self):
        # U(s)=2+3s => G(s,U)=2U+6s, exact nonautonomous ODE.
        with mp.workdps(50):
            s=mp.mpf(2)/5;u=2+3*s
            j=endpoint_jets(lambda s,u:2*u+6*s,s,u)
            self.assertLess(abs(j['U_s']-3),mp.mpf('1e-45'))
            self.assertLess(abs(j['U_ss']),mp.mpf('1e-45'))
            self.assertLess(abs(j['U_sss']),mp.mpf('1e-45'))
            self.assertLess(abs(j['affine_defect_second']),mp.mpf('1e-45'))
            self.assertLess(abs(j['affine_defect_third']),mp.mpf('1e-45'))

    def test_cubic_taylor_matches_radial_three_jets(self):
        with mp.workdps(60):
            s=mp.mpf(1)/4;u=mp.mpf(1)/2;r=mp.sqrt(s)
            j=endpoint_jets(lambda s,u:s*s+u*u,s,u)
            f=lambda t:t*t*cubic_U(t,s,u,j)
            for order,key in ((1,'pLf_prime'),(2,'pLf_second'),(3,'pLf_third')):
                self.assertLess(abs(mp.diff(f,r,order)-j[key]),mp.mpf('1e-50'))

    def test_nonzero_third_order_defect(self):
        with mp.workdps(50):
            j=endpoint_jets(lambda s,u:s*s+u*u,mp.mpf(1)/4,mp.mpf(1)/2)
            self.assertNotEqual(j['affine_defect_third'],0)
            self.assertNotEqual(j['U_sss'],0)

    def test_precision_scaling(self):
        for dps in (30,50,70):
            with mp.workdps(dps):
                j=endpoint_jets(lambda s,u:mp.exp(s)+u*u,mp.mpf(7)/20,mp.mpf(3)/5)
                self.assertLess(max(map(abs,j['holonomic_residuals'])),mp.power(10,-dps+8))

    def test_center_guard(self):
        with self.assertRaisesRegex(ValueError,'center'):
            endpoint_jets(lambda s,u:s+u,mp.mpf(0),mp.mpf(1))

if __name__=='__main__': unittest.main()
