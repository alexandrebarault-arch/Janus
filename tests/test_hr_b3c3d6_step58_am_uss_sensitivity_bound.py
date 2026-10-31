import unittest
from fractions import Fraction as F
from numerics.hr_b3c3d6_step58_am_uss_sensitivity_bound import (
    S, RADII, U_GLOBAL_LO, geometry, global_guards,
    sensitivity_magnitude_bounds, four_point_budgets,
)

class ExactStep58SensitivityBudget(unittest.TestCase):
    def test_global_polynomial_T_and_denominator_guards(self):
        g=global_guards()
        self.assertGreater(g['T_lo'],F(1,10))
        self.assertLess(g['T_hi'],F(1,9))
        self.assertLess(g['qmax'],F(1,500))

    def test_all_four_exact_physical_radius_bounds(self):
        for r in RADII:
            lo,hi=sensitivity_magnitude_bounds(r)
            self.assertLess(F(0),lo)
            self.assertLess(lo,hi)

    def test_certified_previous_uss_budget_transfer(self):
        out=four_point_budgets()
        self.assertEqual([x['r'] for x in out],list(map(str,RADII)))
        self.assertEqual([x['conditional_abs_AM_Uss_contribution_less_than'] for x in out],
                         ['1/1000','1/300','1/150','1/100'])

    def test_radial_domain_guards(self):
        for r in (0,-F(1,4),F(9,10)):
            with self.assertRaises(ValueError):sensitivity_magnitude_bounds(r)
        with self.assertRaises(ValueError):geometry(S+F(1,100))

    def test_exact_t_at_endpoint(self):
        self.assertTrue(geometry(S)[3]>F(1,10))

    def test_sign_reversal_not_silently_allowed(self):
        self.assertTrue(U_GLOBAL_LO<0)
        self.assertTrue(all(sensitivity_magnitude_bounds(r)[0]>0 for r in RADII))

if __name__=='__main__':unittest.main()
