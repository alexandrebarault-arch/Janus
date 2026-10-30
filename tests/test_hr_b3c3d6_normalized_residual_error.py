import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_normalized_residual_error import (
    GU_UPPER,R_PHYSICAL_STRICT,endpoint_bound_rational,
    archived_strict_residual_screen)

class NormalizedResidualError(unittest.TestCase):
    def test_physical_alpha_exact(self):
        self.assertEqual((2-GU_UPPER)/2,Q(299,200))
    def test_equilibrium_strict_margin(self):
        self.assertLess(R_PHYSICAL_STRICT*Q(100,299),Q(1,20000))
    def test_zero_initial_error(self):
        x=endpoint_bound_rational(Q(1,100),Q(17,20),0,R_PHYSICAL_STRICT/2)
        self.assertEqual(x['bound'],R_PHYSICAL_STRICT*Q(50,299))
    def test_positive_initial_error_rational_bound(self):
        r=Q(1,10000);e=Q(1,100)
        x=endpoint_bound_rational(Q(1,100),Q(17,20),e,r)
        eq=r*Q(100,299)
        self.assertEqual(x['bound'],eq+(e-eq)*Q(1,7225))
    def test_negative_coefficient_not_mishandled(self):
        x=endpoint_bound_rational(Q(1,100),Q(17,20),0,Q(1,10000))
        self.assertEqual(x['bound'],Q(1,10000)*Q(100,299))
    def test_zero_residual_contraction(self):
        x=endpoint_bound_rational(Q(1,100),Q(17,20),Q(1,1000),0)
        self.assertEqual(x['bound'],Q(1,7225000))
    def test_reject_threshold_equality(self):
        with self.assertRaises(ValueError):
            archived_strict_residual_screen(Q(1,100),Q(17,20),0,R_PHYSICAL_STRICT)
    def test_reject_negative(self):
        with self.assertRaises(ValueError):
            endpoint_bound_rational(Q(1,100),Q(17,20),0,-1)
    def test_reject_gu_positive(self):
        with self.assertRaises(ValueError):
            endpoint_bound_rational(Q(1,100),Q(17,20),0,0,Q(1,2))
    def test_saturation_toy_constant_residual(self):
        # Toy G=-U, U=0: v(s)=R/3*(1-(a/s)**(3/2)), v(a)=0.
        # At b/a=4, exact error =R/3*(1-1/8), strictly <= rational screen.
        R=Q(3,1000)
        exact=R/3*(1-Q(1,8))
        screen=endpoint_bound_rational(Q(1,4),Q(1,2),0,R,Q(-1))
        self.assertLessEqual(exact,screen['bound'])
    def test_toy_node_zero_residual_not_continuous(self):
        import sympy as s
        t=s.symbols('t'); a=s.Rational(1,16);b=s.Rational(1,4)
        v=(t-a)**2*(t-b)**2
        rho=s.expand(2*t*s.diff(v,t)+3*v)
        self.assertEqual(rho.subs(t,a),0)
        self.assertEqual(rho.subs(t,b),0)
        self.assertNotEqual(rho.subs(t,(a+b)/2),0)

if __name__=='__main__': unittest.main()
