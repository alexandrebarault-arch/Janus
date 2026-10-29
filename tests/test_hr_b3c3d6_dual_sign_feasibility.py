import unittest
import sympy as sp
from numerics.hr_b3c3d6_dual_sign_feasibility import dual_density,integral_identity,witness

class DualSignFeasibility(unittest.TestCase):
    def test_nontrivial_B_E_exact_identity(self):
        w=witness()
        self.assertEqual(w['boundary'],0)
        self.assertEqual(w['integral_Q_M'],w['integral_phi_A_M'])
        self.assertLess(w['integral_Q_M'],0)

    def test_independent_manual_integral(self):
        w=witness();x=w['x']
        self.assertEqual(w['integral_phi_A_M'], -sp.Rational(2,30)-sp.Rational(1,105))
        self.assertEqual(sp.integrate(w['Q_M'],(x,0,1)),-sp.Rational(8,105))

    def test_both_endpoint_derivatives_zero(self):
        w=witness();x=w['x'];phi=w['phi']
        for endpoint in (0,1):
            self.assertEqual(phi.subs(x,endpoint),0)
            self.assertEqual(sp.diff(phi,x).subs(x,endpoint),0)

    def test_no_derivative_boundary_guard_is_insufficient(self):
        x=sp.symbols('x');phi=x*(1-x);A=0;B=0;E=1
        lhs,bulk,bdry=integral_identity(phi,A,B,E,x)
        self.assertEqual((lhs,bulk,bdry),(-2,0,-2))

    def test_positive_A_can_admit_nonnegative_dual(self):
        x=sp.symbols('x');phi=x**2*(1-x)**2
        q=dual_density(phi,1,0,0,x)
        self.assertEqual(sp.simplify(q-phi),0)
        self.assertGreater(sp.integrate(q,(x,0,1)),0)

if __name__=='__main__': unittest.main()
