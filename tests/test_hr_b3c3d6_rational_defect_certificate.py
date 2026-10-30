import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_rational_defect_certificate import (
    bernstein_coefficients, polynomial_defect_bound,
    rational_error_step, chained_error_bound,
)

class RationalDefectTests(unittest.TestCase):
    def test_exact_zero_defect(self):
        self.assertEqual(polynomial_defect_bound([0,0],0,1),0)
        self.assertEqual(rational_error_step(0,0,0,0,1),0)

    def test_bernstein_quadratic_enclosure(self):
        self.assertEqual(bernstein_coefficients([0,1,-1],0,1),(Q(0),Q(1,2),Q(0)))
        self.assertEqual(polynomial_defect_bound([0,1,-1],0,1),Q(1,2))

    def test_affine_time_rescaling(self):
        self.assertEqual(bernstein_coefficients([0,1],Q(1,4),Q(3,4)),(Q(1,4),Q(3,4)))

    def test_linear_ode_yprime_y_approximation(self):
        # v=1+s; f=y; defect v'-f=-s on [0,1/2].
        d=polynomial_defect_bound([0,-1],0,Q(1,2))
        self.assertEqual(d,Q(1,2))
        self.assertEqual(rational_error_step(0,d,1,0,Q(1,2)),Q(1,2))

    def test_nonlinear_ode_defect(self):
        # v=1+s, f=y^2; defect=-2s-s^2 (exact polynomial).
        self.assertEqual(polynomial_defect_bound([0,-2,-1],0,Q(1,4)),Q(9,16))

    def test_chain(self):
        self.assertEqual(chained_error_bound(0,[(0,Q(1,4),Q(1,4),1),
                                               (Q(1,4),Q(1,2),Q(1,2),1)]),Q(5,18))

    def test_sampling_zero_is_not_certification(self):
        # v=s^2(1-s)^2, f=0; d=v'=2s-6s^2+4s^3.
        # d(0)=d(1/2)=d(1)=0, but d not identically zero.
        p=[0,2,-6,4]
        def eval_at(s):return sum(Q(c)*Q(s)**k for k,c in enumerate(p))
        self.assertTrue(all(eval_at(x)==0 for x in (Q(0),Q(1,2),Q(1))))
        self.assertGreater(polynomial_defect_bound(p,0,1),0)

    def test_reject_uncontrolled_cell(self):
        with self.assertRaises(ValueError):rational_error_step(0,1,2,0,Q(1,2))
        with self.assertRaises(ValueError):rational_error_step(0,-1,0,0,1)
        with self.assertRaises(ValueError):bernstein_coefficients([1],1,1)
        with self.assertRaises(ValueError):chained_error_bound(0,[(0,1,0,0),(2,3,0,0)])
        with self.assertRaises(ValueError):chained_error_bound(-1,[])

if __name__=='__main__': unittest.main()
