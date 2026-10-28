"""Non-independent b3c3d regression of the exact boundary-sector identities."""
import unittest
import sympy as s
from numerics import hr_step68ad_b3c3d_boundary_sector_rank as b

class TestBoundarySector(unittest.TestCase):
    def test_exact_certificate(self):
        self.assertEqual(b.run()['exact_sympy_assertions'],16)
    def test_rank_two_free_slice(self):
        self.assertEqual(s.simplify(b.curvature-b.expected),0)
        self.assertNotEqual(b.expected,0)
    def test_integrable_mixed_graph(self):
        self.assertEqual(s.simplify(s.diff(b.B,b.p)-b.P*s.diff(b.F,b.p)),0)
    def test_fixed_shift_and_fixed_momentum(self):
        w=s.Symbol('w')
        self.assertEqual(s.diff(b.P*w,w),b.P)
        self.assertEqual(s.diff(b.P,s.Symbol('dummy')),0)

if __name__=='__main__':unittest.main()
