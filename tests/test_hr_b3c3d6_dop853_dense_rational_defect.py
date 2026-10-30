import unittest
from fractions import Fraction as Q
import numpy as np
from scipy.integrate import solve_ivp
from numerics.hr_b3c3d6_dop853_dense_rational_defect import (
    add, mul, value, dop853_dense_coefficients, residual_polynomial,
    bernstein_enclosure, polynomial_defect_certificate, center_initial_error_bound, interval_step_defect, dense_exact_domain, dense_boundary_jump)


class TestDop853RationalDefect(unittest.TestCase):
    def test_true_scipy_dense_reconstruction(self):
        sol=solve_ivp(lambda s,y:[2*s],(0.1,0.7),[0.01],method='DOP853',
                      rtol=1e-12,atol=1e-14,dense_output=True)
        self.assertTrue(sol.success)
        self.assertGreater(len(sol.sol.interpolants),0)
        for dense in sol.sol.interpolants:
            p=dop853_dense_coefficients(dense)
            for x in (0.,0.125,0.3,0.5,0.875,1.):
                reconstructed=float(value(p,Q.from_float(x)))
                actual=float(dense(dense.t_old+dense.h*x)[0])
                self.assertLess(abs(reconstructed-actual),3e-14)

    def test_exact_polynomial_residual_cancellation(self):
        # p=(s-1)^2=x^2 on t_old=1,h=1; G=6s^2-8s+2.
        p=[Q(0),Q(0),Q(1)]
        cert=polynomial_defect_certificate(p,1,1,{(2,0):Q(6),(1,0):Q(-8),(0,0):Q(2)},8)
        self.assertEqual(cert['residual_polynomial'],[Q(0)])
        self.assertEqual(cert['max_abs_bound'],0)

    def test_nonlinear_polynomial_rhs(self):
        # p=x, s=1+x; G=2s*p_s+2p=2+4x=4s-2.
        p=[Q(0),Q(1)]
        cert=polynomial_defect_certificate(p,1,1,{(1,0):Q(4),(0,0):Q(-2)},4)
        self.assertEqual(cert['max_abs_bound'],0)
        # A nonzero perturbation must not pass.
        wrong=polynomial_defect_certificate(p,1,1,{(1,0):Q(4)},4)
        self.assertEqual(wrong['max_abs_bound'],2)

    def test_three_point_sampling_can_miss_continuous_defect(self):
        # x(x-1/2)(x-1) vanishes at 0,1/2,1, not between.
        p=mul(mul([Q(0),Q(1)],[Q(-1,2),Q(1)]),[Q(-1),Q(1)])
        for x in (Q(0),Q(1,2),Q(1)):self.assertEqual(value(p,x),0)
        lo,hi=bernstein_enclosure(p)
        self.assertLess(lo,0);self.assertGreater(hi,0)
        self.assertNotEqual(value(p,Q(1,4)),0)

    def test_center_weighted_bound_and_invalid_gu(self):
        # G_U <= -99/100, residual <= C*s^3: coefficient 100/899.
        b=center_initial_error_bound(Q(1,10000),Q(1),Q(3),Q(-99,100))
        self.assertEqual(b,Q(100,899)*Q(1,10000)**3)
        with self.assertRaises(ValueError):center_initial_error_bound(Q(1,10000),1,3,2)

    def test_center_bound_exact_toy(self):
        # Exact toy G(s,U)= -U + 3*s^3, P=0, U(0)=0:
        # 2s U_s=-3U+3s^3 => U=(1/3)s^3; H=3s^3.
        # The general bound gives 3*s^3/(6+3)=s^3/3, attained.
        b=center_initial_error_bound(Q(1,10),3,3,-1)
        self.assertEqual(b,Q(1,3000))

    def test_interval_continuous_step_defect_and_tube_guard(self):
        # Exact interval extension of polynomial G=6s^2 for y=s^2.
        class Interval:
            def __init__(self,lo,hi):self.lo,self.hi=lo,hi
            @classmethod
            def hull(cls,a,b):return cls(Q(a),Q(b))
            @classmethod
            def c(cls,a):return cls(Q(a),Q(a))
            def __add__(self,o):
                o=o if isinstance(o,Interval) else Interval.c(o)
                return Interval(self.lo+o.lo,self.hi+o.hi)
            __radd__=__add__
            def __neg__(self):return Interval(-self.hi,-self.lo)
            def __sub__(self,o):return self+-o
            def __mul__(self,o):
                o=o if isinstance(o,Interval) else Interval.c(o)
                vs=(self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi)
                return Interval(min(vs),max(vs))
            __rmul__=__mul__
        sol=solve_ivp(lambda s,y:[2*s],(0.1,0.2),[0.01],method='DOP853',
                      rtol=1e-12,atol=1e-14,dense_output=True)
        dense=sol.sol.interpolants[0]
        def g(s,u):return 6*s*s
        bounds=interval_step_defect(dense,g,Interval,subcells=256)
        self.assertEqual(len(bounds),256)
        self.assertTrue(all(b.lo<=b.hi for b in bounds))
        # Interval inclusion of residual at interior points (not certification by sampling).
        p=dop853_dense_coefficients(dense)
        H=residual_polynomial(p,float(dense.t_old),float(dense.h),{(2,0):Q(6)})
        for i,b in enumerate(bounds):
            x=Q(2*i+1,512)
            self.assertLessEqual(b.lo,value(H,x));self.assertLessEqual(value(H,x),b.hi)
        with self.assertRaises(ArithmeticError):
            interval_step_defect(dense,g,Interval,1,
                                 tube_guard=lambda s,p:(_ for _ in ()).throw(ArithmeticError()))

    def test_exact_binary_step_gap_and_jump_budget(self):
        import math
        sol=solve_ivp(lambda s,y:[(math.sin(s)+y[0])/(1+s)],
                      (1e-4,.7225),[.01],method='DOP853',
                      rtol=1e-12,atol=1e-14,dense_output=True)
        pieces=sol.sol.interpolants
        gaps=[]
        for dense in pieces:
            t0,t1,h,xmax=dense_exact_domain(dense)
            self.assertEqual(t0+h*xmax,t1)
            gaps.append(xmax-Q(1))
        self.assertTrue(any(g!=0 for g in gaps),
                        'fixture should exercise non-exact h=t-t_old')
        jumps=[dense_boundary_jump(a,b) for a,b in zip(pieces,pieces[1:])]
        self.assertEqual(len(jumps),len(pieces)-1)
        # The rational jumps may be small but cannot be silently discarded.
        self.assertTrue(any(j!=0 for j in jumps))
        with self.assertRaises(ValueError):dense_boundary_jump(pieces[0],pieces[-1])

    def test_binary_float_exactness_and_input_guards(self):
        sol=solve_ivp(lambda s,y:[0],(0.,1.),[1.],method='DOP853',dense_output=True)
        self.assertEqual(dop853_dense_coefficients(sol.sol.interpolants[0]),[Q(1)])
        with self.assertRaises(TypeError):bernstein_enclosure([Q(1)],'0','1')
        with self.assertRaises(ValueError):polynomial_defect_certificate([Q(1)],0,1,{},0)

if __name__=='__main__':unittest.main()
