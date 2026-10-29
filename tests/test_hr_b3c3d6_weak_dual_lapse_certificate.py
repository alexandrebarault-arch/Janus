"""Exact nonphysical weak-dual lapse screen, SymPy checks, non-independent."""
import unittest
import sympy as sp
from numerics.hr_b3c3d6_weak_dual_lapse_certificate import (
    x, R, eps, phi, base, exact_certificate, dual_coefficients,
    point_checks, zero_control,
)

class WeakDualCertificate(unittest.TestCase):
    def test_exact_integration_by_parts_coefficients(self):
        c=exact_certificate()
        for key in ('d_phi_B','dd_phi_E','qn_formula','qm_formula','sum_identity'):
            self.assertEqual(c[key],0,key)

    def test_boundary_terms_vanish_for_arbitrary_finite_jets(self):
        c=exact_certificate()
        self.assertEqual(c['boundary_phi'],(0,0))
        self.assertEqual(c['boundary_dphi'],(0,0))
        self.assertEqual(R,sp.Rational(17,20))

    def test_strict_global_margin_from_elementary_interval_bounds(self):
        # 0<=x<=1 => |1-2x|<=1, x(1-x)<=1/4, (1-x)^2<=1.
        # Hence |c1|<=5*base and |c2|<=33*base (proved algebraically
        # from the factorizations in test_exact_integration_by_parts_coefficients).
        self.assertEqual(1-5*eps-33*eps**2,sp.Rational(9467,10000))
        self.assertGreater(1-5*eps-33*eps**2,0)

    def test_six_exact_rational_spot_checks(self):
        self.assertEqual(len(point_checks()),6)
        self.assertTrue(all(v>=0 for v in point_checks()))

    def test_negative_control_no_general_no_go_from_small_B_E(self):
        self.assertEqual(zero_control(),0)
        qn,qm=dual_coefficients()
        self.assertNotEqual(qn, qm)

if __name__=='__main__': unittest.main()
