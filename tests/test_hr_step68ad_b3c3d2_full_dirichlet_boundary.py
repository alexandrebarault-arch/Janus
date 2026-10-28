"""Replays b3c3d2 exact non-IBP endpoint identities; not independent physics."""
import unittest
import sympy as s
from numerics import hr_step68ad_b3c3d2_full_dirichlet_boundary as m

class TestFullDirichlet(unittest.TestCase):
    def test_symbolic_replay(self):
        self.assertEqual(m.run()['exact_symbolic_zero_residuals'],29)
    def test_stationary_shift(self):
        self.assertEqual(s.simplify(s.diff(m.F,m.z).subs(m.z,m.Z)),0)
    def test_boundary_curvature_nonzero(self):
        value=s.diff(m.P,m.p)*s.diff(m.Z,m.pr)
        self.assertEqual(s.simplify(value.subs({m.Lg:s.Rational(2,5),m.Lf:s.Rational(3,5),m.N:1,m.M:1,m.K:4,m.D:3})),-s.Rational(32,375))
    def test_lapse_cross_witness(self):
        self.assertEqual(s.diff(m.A,m.N).subs({m.mg:1,m.Sg:1,m.Lg:1}),2)

if __name__=='__main__':unittest.main()
