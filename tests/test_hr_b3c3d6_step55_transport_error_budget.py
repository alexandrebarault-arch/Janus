import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_step55_transport_error_budget import (
    step55_partials, second_order_transport, second_order_error_budget)

class ErrorBudgetTests(unittest.TestCase):
    def test_step55_affine_rhs_partials(self):
        # G=2u+2s(3u+s) -> f=3u+s, f_y=3, f_sy=f_yy=0.
        s=Q(2,5); u=Q(7,11)
        g=2*u+2*s*(3*u+s)
        gs=6*u+4*s
        gu=2+6*s
        gsu=6
        self.assertEqual(step55_partials(s,u,g,gs,gu,gsu,0),(3*u+s,Q(3),Q(0),Q(0)))

    def test_step55_nonlinear_rhs_partials(self):
        # G=2u+2s(u²+s) -> f=u²+s, f_y=2u, f_sy=0, f_yy=2.
        s=Q(3,7);u=Q(5,8)
        g=2*u+2*s*(u*u+s)
        self.assertEqual(step55_partials(s,u,g,2*u*u+4*s,2+4*s*u,4*u,4*s),
                         (u*u+s,2*u,Q(0),Q(2)))

    def test_affine_taylor_sensitivity_exact(self):
        # T2 for f=3y+s has exact derivative 1+3h+9h²/2.
        h=Q(1,10);s=Q(1,2);y=Q(2,3);e=Q(1,1000)
        def t(v):return second_order_transport(s,v,h,3*v+s,1,3)
        self.assertEqual(t(y+e)-t(y),e*(1+3*h+Q(9,2)*h*h))

    def test_affine_amplification_bound_attained(self):
        h=Q(1,10);eps=Q(1,1000)
        b=second_order_error_budget(h,eps,3,0,0,10,0)
        self.assertEqual(b['propagated_state_error'],eps*(1+3*h+Q(9,2)*h*h))

    def test_cubic_taylor_remainder_sharp(self):
        # y=s³, f=3s²; at s=0, T2=0, true y(h)=h³, M3=6.
        h=Q(1,10)
        t=second_order_transport(Q(0),Q(0),h,Q(0),Q(0),Q(0))
        b=second_order_error_budget(h,0,0,0,0,1,6)
        self.assertEqual(h**3-t,b['taylor_remainder'])

    def test_zero_gap_does_not_remove_solver_error(self):
        eps=Q(7,10**12)
        b=second_order_error_budget(Q(0),eps,10,10,10,10,10)
        self.assertEqual(b['total'],eps)

    def test_center_excluded(self):
        with self.assertRaises(ValueError):
            step55_partials(0,1,1,1,1,1,1)

    def test_negative_envelopes_rejected(self):
        with self.assertRaises(ValueError):
            second_order_error_budget(Q(1,10),0,1,-1,0,1,1)

if __name__=='__main__':unittest.main()
