import unittest
from fractions import Fraction as Q
from numerics import hr_b3c3d6_lapse_boundary_compatibility as c


class BoundaryCompatibility(unittest.TestCase):
    def test_strict_physical_ratios(self):
        self.assertEqual(len(c.audit()), 4)
        lo, hi = c.certified_pointwise_ratios()['17/20']
        self.assertLess(Q(1, 2), lo)
        self.assertLess(hi, Q(11, 20))

    def test_known_mismatch_outer_equal_lapses_excluded(self):
        for r in c.PHYSICAL_RATIONAL_BOXES:
            self.assertFalse(c.necessary_boundary_ratio(r, 1, 1))
            self.assertFalse(c.necessary_boundary_ratio(r, 11, 11))

    def test_positive_outer_ratios_admissible_at_point_only(self):
        for r in c.PHYSICAL_RATIONAL_BOXES:
            self.assertTrue(c.necessary_boundary_ratio(r, 1, c.toy_ratio(r)))
            self.assertFalse(c.necessary_boundary_ratio(r, 0, 1))
            self.assertFalse(c.necessary_boundary_ratio(r, 1, 0))

    def test_synthetic_coefficients_fit_original_four_strict_boxes(self):
        for r, ((nlo, nhi), (mlo, mhi)) in c.PHYSICAL_RATIONAL_BOXES.items():
            an, am = c.toy_coefficients(r)
            self.assertTrue(nlo < an < nhi)
            self.assertTrue(mlo < am < mhi)
            self.assertEqual(an + am * c.toy_ratio(r), 0)

    def test_center_jet_ratio_and_positive_even_lapses(self):
        self.assertTrue(c.CENTER_RHO_OPEN[0] < c.toy_ratio(0) < c.CENTER_RHO_OPEN[1])
        self.assertEqual(c.toy_ratio(0), Q(14, 27))
        self.assertEqual(c.toy_ratio_derivative_s_numerator(), 131250)
        for r in (Q(0), Q(1,4), Q(1,2), Q(7,10), Q(17,20)):
            self.assertGreater(c.toy_ratio(r), 0)
            self.assertEqual(c.toy_ratio(-r), c.toy_ratio(r))
            self.assertLess(c.toy_ratio(r), 1)
        self.assertLess(c.toy_ratio(0), c.toy_ratio(Q(17,20)))

    def test_two_true_endpoints_for_toy_algebraic_constraint(self):
        r = Q(17,20)
        self.assertTrue(c.compatible_two_boundary_dirichlet(1, c.toy_ratio(0), 1, c.toy_ratio(r), c.toy_ratio(0), c.toy_ratio(r)))
        self.assertFalse(c.compatible_two_boundary_dirichlet(1,c.toy_ratio(0),1,1,c.toy_ratio(0),c.toy_ratio(r)))
        self.assertFalse(c.compatible_two_boundary_dirichlet(1,1,1,c.toy_ratio(r),c.toy_ratio(0),c.toy_ratio(r)))

    def test_malformed_uncertainty_signs_rejected(self):
        for n,m in [((-1,2),(-5,-2)),((0,1),(-2,-1)),((1,2),(-2,1)),((2,1),(-3,-2))]:
            with self.assertRaises(ValueError): c.ratio_open_bounds(n,m)

    def test_unconstrained_physical_bvp_not_claimed(self):
        self.assertNotEqual(c.toy_ratio(Q(17,20)), 1)
        self.assertTrue(c.necessary_boundary_ratio(Q(17,20),1,c.toy_ratio(Q(17,20))))

if __name__ == '__main__':
    unittest.main()
