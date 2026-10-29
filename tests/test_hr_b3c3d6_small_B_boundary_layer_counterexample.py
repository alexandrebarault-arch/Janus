import unittest
import sympy as sp
from numerics.hr_b3c3d6_small_B_boundary_layer_counterexample import (
    r,R,eps,E,N,M,A_N,A_M,B_N,B_M,certificate)

class SmallBLayer(unittest.TestCase):
    def test_exact_original_operator_shape(self):
        self.assertEqual(certificate()['residual'],0)
    def test_positive_lapses_and_both_borders(self):
        self.assertEqual(sp.limit(N,r,0,dir='+'),2)
        self.assertEqual(sp.simplify(N.subs(r,R)),1)
        self.assertEqual(M,1)
        self.assertEqual(sp.simplify(sp.diff(N,r)/(-E/(eps*r**2))),1)
        # 0<exp((1/R-1/r)/eps)<=1 for 0<r<=R, hence 1<=N<2.
    def test_arbitrarily_small_coefficient(self):
        self.assertEqual(sp.simplify(B_N.subs(r,R)/eps),-R**4)
        self.assertEqual(sp.limit(B_N,eps,0,dir='+'),0)
        self.assertEqual(sp.simplify(sp.diff(N,r).subs(r,R)),-1/(eps*R**2))
    def test_algebraic_limit_is_incompatible(self):
        self.assertEqual(sp.simplify((A_N*N+A_M*M).subs(r,R)),-R**2)
    def test_smooth_flat_center_not_analytic(self):
        self.assertEqual(sp.limit(N,r,0,dir='+'),2)
        for k in range(1,7):
            self.assertEqual(sp.limit(sp.diff(N,r,k),r,0,dir='+'),0)
        self.assertNotEqual(sp.simplify(N.subs(r,R/2)),2)

if __name__=='__main__':unittest.main()
