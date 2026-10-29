"""Exact rational regression tests; not an independent physical Step58 replay."""
import unittest
import sympy as sp
from numerics.hr_b3c3d6_cone_adapted_dual import (
    x, eps, phi, B, E, lo, hi, A_N, A_M, coefficients, toy_certificates,
    exact_lower_margin,
)


class ConeDualTests(unittest.TestCase):
    def test_exact_derivatives(self):
        c = toy_certificates()
        self.assertEqual(c['d1_identity'], 0)
        self.assertEqual(c['d2_identity'], 0)

    def test_boundary_vanishes(self):
        c = toy_certificates()
        self.assertEqual(c['boundary_phi'], (0,0))
        self.assertEqual(c['boundary_dphi'], (0,0))

    def test_componentwise_dual_impossible(self):
        c = toy_certificates()
        self.assertEqual(c['integrated_Q_M'], sp.Rational(-1,10))
        self.assertEqual(c['integrated_Q_M'], c['integrated_phi_A_M'])

    def test_cone_margin_positive(self):
        self.assertEqual(exact_lower_margin(), sp.Rational(318401,640000))
        self.assertGreater(exact_lower_margin(), 0)

    def test_endpoint_cone_inequality_exact(self):
        qn, qm = coefficients()
        # Derivative bounds: |(phi B)'| <= (5eps/16)*phi,
        # |(phi E)''| <= (33eps²/16)*phi on [0,1].
        for rho in (lo, hi):
            for t in (sp.Rational(1,10),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(9,10)):
                v=sp.factor((qn+rho*qm-exact_lower_margin()*phi).subs(x,t))
                self.assertGreaterEqual(v,0)

    def test_outside_cone_positive_solution(self):
        c=toy_certificates()
        self.assertEqual(c['outside_cone_solution'],0)
        self.assertGreater(sp.Rational(2,3),hi)
        self.assertLess(sp.Rational(2,3),1)

    def test_nonzero_derivative_coefficients(self):
        self.assertNotEqual(B,0)
        self.assertNotEqual(E,0)
        self.assertEqual(A_N,2)
        self.assertEqual(A_M,-3)


if __name__=='__main__':
    unittest.main()
