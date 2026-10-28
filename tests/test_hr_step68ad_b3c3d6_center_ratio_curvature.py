"""Non-independent regression checks for the formal b3c3d6 center lemma."""
import unittest
import sympy as s
from center_ratio_curvature import check, rho2_shell, rho2_full, a,b,c,d,e,f,n0,n2

class CenterRatioTests(unittest.TestCase):
    def test_all_exact_residuals_and_toys(self):
        self.assertEqual(check()['symbolic_residuals'],11)
    def test_shell_curvature(self):
        self.assertEqual(s.simplify((2*rho2_shell).subs({a:2,b:1,c:-4,d:0})-s.Rational(1,2)),0)
    def test_nonzero_second_jet_changes_curvature(self):
        vals={a:2,b:1,c:-4,d:0,e:1,f:0,n0:1}
        self.assertEqual(s.simplify(2*rho2_full.subs({**vals,n2:1})-2*rho2_full.subs({**vals,n2:0})),1)
    def test_degenerate_denominator_is_excluded(self):
        self.assertEqual(s.simplify((c+2*f).subs({c:-4,f:2})),0)

if __name__=='__main__': unittest.main()
