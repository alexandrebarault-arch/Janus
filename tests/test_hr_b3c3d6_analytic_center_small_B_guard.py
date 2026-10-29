import unittest
import sympy as sp
from numerics.hr_b3c3d6_analytic_center_small_B_guard import (
    r, eps, R, C, N, residual, boundary_constant,
    terminal_slope, center_taylor_coefficients,
)

class AnalyticCenterSmallBGuard(unittest.TestCase):
    def test_exact_equation_all_constants(self):
        self.assertEqual(residual(), 0)

    def test_terminal_and_positive_interval(self):
        nt = N.subs(C, boundary_constant())
        self.assertEqual(sp.simplify(nt.subs(r, R)), 1)
        self.assertEqual(sp.limit(nt, r, 0, dir='+'), 2)
        # r<=R => (1/R-1/r)/eps<=0, hence 1<=N(r)<2.
        self.assertEqual(sp.simplify(nt.subs({eps:sp.Rational(1,10), R:sp.Rational(17,20), r:sp.Rational(1,2)})) > 1, True)

    def test_flat_but_nonanalytic_center(self):
        for k in range(1, 6):
            self.assertEqual(sp.limit(sp.diff(N-2, r, k), r, 0, dir='+'), 0)
        self.assertNotEqual(boundary_constant(), 0)

    def test_unique_formal_analytic_germ(self):
        self.assertEqual(center_taylor_coefficients(12), [sp.Integer(2)] + [sp.Integer(0)]*12)

    def test_exact_unbounded_terminal_slope(self):
        self.assertEqual(terminal_slope(), -1/(eps*R**2))
        self.assertEqual(sp.limit(terminal_slope(), eps, 0, dir='+'), -sp.oo)

if __name__ == '__main__':
    unittest.main()
