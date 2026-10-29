"""Exact SymPy tests; not independent validation of physical Step58."""
import unittest
import sympy as sp
from numerics.hr_b3c3d6_analytic_even_two_lapse_boundary_layer import witness, certificate, r, eps, R, k

class AnalyticEvenTwoLapseToy(unittest.TestCase):
    def test_exact_operator_zero(self):
        self.assertEqual(certificate()['operator_exact_zero'], 0)

    def test_two_positive_outer_amplitudes(self):
        c=certificate()
        self.assertEqual((c['N_outer'],c['M_outer']), (1,1))
        self.assertEqual(c['center_ratio'], k)
        self.assertTrue(sp.Rational(1037,2000)<k<sp.Rational(2593,5000))

    def test_even_entire_and_positive(self):
        w=witness()
        self.assertEqual(sp.simplify(w['N'].subs(r,-r)-w['N']),0)
        self.assertEqual(sp.simplify(w['M'].subs(r,-r)-w['M']),0)
        self.assertEqual(certificate()['N_prime_center'],0)
        self.assertEqual(certificate()['M_prime_center'],0)
        # For eps>0 and 0<=r<=R, N>0, k+(1-k)*(r/R)^4>=k>0.
        self.assertGreater(k,0)
        self.assertLess(k,1)

    def test_small_B_large_endpoint_derivative(self):
        c=certificate()
        self.assertEqual(c['endpoint_derivative'], -1/(eps*R**3))
        self.assertEqual(c['endpoint_BN_Nprime'],R**2)
        self.assertEqual(c['endpoint_A_sum'],-R**2)
        self.assertEqual(sp.limit(witness()['BN'].subs(r,R),eps,0,dir='+'),0)

    def test_zero_B_operator_excludes_positive_terminal(self):
        c=certificate()
        self.assertEqual(c['algebraic_limit_ratio'],k)
        self.assertNotEqual(k,1)
        # B=0 gives M=kN; at R, N=M=u>0 would imply (1-k)u=0.
        self.assertNotEqual(sp.simplify((1-k)*sp.Integer(1)),0)

    def test_center_amplitude_exponential_budget(self):
        c=certificate()
        self.assertEqual(c['N_center'],sp.exp(1/(2*eps*R**2)))
        self.assertEqual(sp.limit(c['N_center'],eps,0,dir='+'),sp.oo)
        self.assertEqual(sp.simplify(sp.log(c['N_center'])*2*eps*R**2),1)

if __name__=='__main__': unittest.main()
