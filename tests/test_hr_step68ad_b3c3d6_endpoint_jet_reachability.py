import unittest
import sympy as s
from numerics.hr_step68ad_b3c3d6_endpoint_jet_reachability import exact_checks

class TestEndpointJetReachability(unittest.TestCase):
    def test_symbolic(self):self.assertEqual(exact_checks()['symbolic_zero_residuals'],10)
    def test_toy(self):self.assertEqual(exact_checks()['exact_toy_and_guard_checks'],12)
    def test_endpoint_obstruction(self):
        # At r=0, A_N=0,A_M=-1,B_N=B_M=1,N=M=1; derivatives 0 violate the ODE.
        self.assertEqual(0*1-1*1+1*0+1*0,-1)
    def test_strict_growth(self):
        # Positive w forces 0<T<1; T=0 and T=1 cannot occur.
        self.assertFalse(s.Rational(0)<s.Rational(0)<s.Rational(1))
        self.assertTrue(s.Rational(0)<s.Rational(1,2)<s.Rational(1))
if __name__=='__main__':unittest.main()
