import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_endpoint_jet_budget import (endpoint_budget, operator_residual,
                                                     verify_necessary_inequality)

class EndpointJetBudget(unittest.TestCase):
    def test_toy_singular_layer_saturates_exact_bound(self):
        r, eps = Q(17,20), Q(1,10**8)
        coeff = (r*r, -2*r*r, -eps*r**4, 0, 0, 0)
        jets = (-1/(eps*r*r), 0, 0, 0)
        self.assertEqual(operator_residual(coeff, 1, jets), 0)
        self.assertEqual(endpoint_budget(*coeff)['min_common_jet_cap'], abs(jets[0]))

    def test_two_derivative_orders_both_count(self):
        coeff = (1,0,Q(1,4),0,0,Q(3,4))
        self.assertEqual(operator_residual(coeff,1,(-1,0,0,-1)),0)
        self.assertEqual(endpoint_budget(*coeff)['min_common_jet_cap'],1)

    def test_exact_zero_B_E_obstruction_and_zero_defect(self):
        self.assertTrue(endpoint_budget(1,-2,0,0,0,0)['incompatible_with_finite_jets'])
        self.assertFalse(endpoint_budget(1,-1,0,0,0,0)['incompatible_with_finite_jets'])

    def test_residual_cap_and_input_guards(self):
        self.assertEqual(endpoint_budget(1,0,Q(1,2),0,0,0,residual_cap=Q(1,4))['min_common_jet_cap'],Q(3,2))
        with self.assertRaises(ValueError): endpoint_budget(1,0,0,0,0,0,u=0)
        with self.assertRaises(ValueError): endpoint_budget(1,0,0,0,0,0,residual_cap=-1)

    def test_exact_triangle_and_negative_control(self):
        coeff = (Q(13,7),-Q(19,5),Q(1,9),-Q(1,11),Q(1,13),-Q(1,17))
        jets = (Q(7,3),-Q(2,3),Q(4,5),-Q(9,8))
        self.assertTrue(verify_necessary_inequality(coeff,Q(3,2),jets))
        b=endpoint_budget(*coeff,u=Q(3,2),residual_cap=abs(operator_residual(coeff,Q(3,2),jets)))
        self.assertLessEqual(b['min_common_jet_cap'],max(map(abs,jets)))

if __name__=='__main__': unittest.main()
