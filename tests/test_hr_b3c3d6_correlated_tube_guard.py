import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_correlated_tube_guard import (
    RI, bernstein_interval, difference_enclosure, certify_correlated_tube,
    physical_center_intervals, certify_dense_cells)


class GuardTests(unittest.TestCase):
    def test_old_separate_hulls_false_positive(self):
        # star=s on [0,1], P=1/2, delta=1/100.
        # Old guard: P.lo>=star.lo-delta and P.hi<=star.hi+delta: PASS.
        p_lo=p_hi=Q(1,2); star_lo=Q(0); star_hi=Q(1); d=Q(1,100)
        self.assertTrue(p_lo>=star_lo-d and p_hi<=star_hi+d)
        self.assertEqual(difference_enclosure([Q(1,2)],0,1,0,1,[0,1,0]),RI(-Q(1,2),Q(1,2)))
        with self.assertRaises(ArithmeticError):
            certify_correlated_tube([Q(1,2)],0,1,0,1,[0,1,0],d)

    def test_correlated_identity(self):
        self.assertEqual(certify_correlated_tube([0,1],0,1,0,1,[0,1,0],0),RI(0,0))

    def test_exact_nonzero_offset(self):
        self.assertEqual(certify_correlated_tube([Q(1,100),1],0,1,0,1,[0,1,0],Q(1,100)),RI(Q(1,100),Q(1,100)))

    def test_interval_center_uncertainty(self):
        r=certify_correlated_tube([0,1],0,1,0,1,[(0,Q(1,1000)),1,0],Q(1,100))
        self.assertEqual(r,RI(-Q(1,1000),0))
        with self.assertRaises(ArithmeticError):
            certify_correlated_tube([0,1],0,1,0,1,[(0,Q(1,1000)),1,0],Q(1,2000))

    def test_quadratic_true_domain(self):
        # x spans [0,3/4], s=1/4+(1/2)x; center Ustar=s^2.
        p=[Q(1,16),Q(1,4),Q(1,4)]
        self.assertEqual(certify_correlated_tube(p,Q(1,4),Q(1,2),0,Q(3,4),[0,0,1],0),RI(0,0))

    def test_polynomial_bernstein_range(self):
        # x(1-x) on [0,1] has exact range [0,1/4]; Bernstein hull [0,1/2].
        self.assertEqual(bernstein_interval([0,1,-1],0,1),RI(0,Q(1,2)))

    def test_negative_width_and_invalid_domain(self):
        with self.assertRaises(ValueError):
            certify_correlated_tube([0],0,1,0,1,[0,0,0],-1)
        with self.assertRaises(ValueError):
            difference_enclosure([0],0,0,0,1,[0,0,0])
        with self.assertRaises(ValueError):
            bernstein_interval([0],1,0)

    def test_dense_cells_entire_true_domain(self):
        # Polynomial x, center s=x, all 7 cells must certify exactly.
        rows=certify_dense_cells([0,1],0,1,Q(7,8),[0,1,0],0,7)
        self.assertEqual(len(rows),7)
        self.assertTrue(all(x==RI(0,0) for x in rows))

    def test_dense_cells_local_failure(self):
        # Constant candidate and moving center: a narrow first cell can pass,
        # but the full domain must fail at a later cell.
        with self.assertRaises(ArithmeticError):
            certify_dense_cells([Q(1,2)],0,1,1,[0,1,0],Q(1,10),8)

    def test_integer_scale(self):
        class I:
            def __init__(self,lo,hi): self.lo,self.hi=lo,hi
        self.assertEqual(physical_center_intervals(I(1,2),I(-3,-2),I(0,0),10),
                         (RI(Q(1,10),Q(1,5)),RI(-Q(3,10),-Q(1,5)),RI(0,0)))

if __name__ == '__main__':
    unittest.main()
