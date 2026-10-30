import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_barrier_initial_bootstrap import (
    initial_error_from_barrier, propagated_initial_contribution)

class BootstrapTests(unittest.TestCase):
    def test_exact_center_candidate(self):
        self.assertEqual(initial_error_from_barrier(Q(1,10000),0,0),Q(1,10000))

    def test_opposite_edges_saturate(self):
        # Ustar=0, U=+delta, P=-delta gives |U-P|=2delta.
        d=Q(1,10000)
        self.assertEqual(initial_error_from_barrier(d,-d,-d),2*d)
        self.assertEqual(abs(d-(-d)),2*d)

    def test_interval_asymmetric(self):
        self.assertEqual(initial_error_from_barrier(Q(1,10),-Q(1,20),Q(1,40)),Q(3,20))

    def test_outside_candidate_fails_closed(self):
        with self.assertRaises(ArithmeticError):
            initial_error_from_barrier(Q(1,100),-Q(1,50),0)

    def test_without_guard_triangle_only(self):
        self.assertEqual(initial_error_from_barrier(Q(1,100),-Q(1,50),0,False),Q(3,100))

    def test_invalid_intervals(self):
        with self.assertRaises(ValueError): initial_error_from_barrier(-1,0,0)
        with self.assertRaises(ValueError): initial_error_from_barrier(1,2,1)

    def test_ideal_rational_endpoints(self):
        s0,sR=Q(1,10000),Q(289,400)
        self.assertEqual(propagated_initial_contribution(s0,sR,Q(2,10000)),Q(1,36125000))

    def test_actual_binary64_endpoints(self):
        from decimal import Decimal
        s0=Q.from_float(1e-4)
        sR=Q.from_float(float(Decimal('0.85')**2))
        self.assertEqual(propagated_initial_contribution(s0,sR,Q(2,10000)),
                         Q(819855292164869,29617272429455892480000))

    def test_stronger_integer_exponent(self):
        self.assertEqual(propagated_initial_contribution(Q(1,4),1,1,-2),Q(1,16))

    def test_noninteger_exponent_rejected(self):
        with self.assertRaises(ValueError):
            propagated_initial_contribution(Q(1,4),1,1,-1)

    def test_bad_time_and_contraction(self):
        for args in [(0,1,1,0),(2,1,1,0),(1,2,-1,0),(1,2,1,1)]:
            with self.assertRaises(ValueError): propagated_initial_contribution(*args)

if __name__=='__main__': unittest.main()
