import unittest
import sympy as sp
from numerics.hr_b3c3d6_fourth_jet_holonomic_guard import (
    jets_through_four, polynomial_extension, endpoint_radial_residual_derivatives)

class FourthJetTests(unittest.TestCase):
    def setUp(self):
        self.s,self.u=sp.symbols('s u',positive=True)
        self.r,self.r0=sp.symbols('r r0',positive=True)
        self.s0=sp.Rational(1,4);self.u0=sp.Rational(1,2)
        self.G=self.s**2+self.u**2+self.s*self.u
        self.js=jets_through_four(self.G,self.s,self.u)
        self.vals=[sp.cancel(x.subs({self.s:self.s0,self.u:self.u0})) for x in self.js]

    def test_fourth_jet_nonzero(self):
        self.assertNotEqual(self.vals[3],0)

    def test_recursive_differentiation_identity(self):
        D=lambda expr:sp.diff(expr,self.s)+sp.diff(expr,self.u)*self.js[0]
        for k in range(1,4):
            self.assertEqual(sp.cancel(D(self.js[k-1])-self.js[k]),0)

    def test_cubic_residual_order_three_nonzero(self):
        v,js=endpoint_radial_residual_derivatives(self.G,self.s,self.u,self.s0,self.u0)
        self.assertEqual(v[3][:3],[0,0,0])
        self.assertNotEqual(v[3][3],0)

    def test_quartic_residual_order_three_zero(self):
        v,_=endpoint_radial_residual_derivatives(self.G,self.s,self.u,self.s0,self.u0)
        self.assertEqual(v[4],[0,0,0,0])

    def test_cubic_quartic_U_radial_jets_equal_0_3(self):
        c=polynomial_extension(self.r,self.r0,self.u0,self.vals,3)
        q=polynomial_extension(self.r,self.r0,self.u0,self.vals,4)
        for k in range(4):
            self.assertEqual(sp.factor(sp.diff(q-c,self.r,k).subs(self.r,self.r0)),0)

    def test_cubic_quartic_pLf_radial_jets_equal_0_3(self):
        c=polynomial_extension(self.r,self.r0,self.u0,self.vals,3)
        q=polynomial_extension(self.r,self.r0,self.u0,self.vals,4)
        for k in range(4):
            self.assertEqual(sp.factor(sp.diff(self.r**2*(q-c),self.r,k).subs(self.r,self.r0)),0)

    def test_derivative_dependent_field_third_jet_differs(self):
        c=polynomial_extension(self.r,self.r0,self.u0,self.vals,3)
        q=polynomial_extension(self.r,self.r0,self.u0,self.vals,4)
        pprime_diff=sp.diff(self.r**2*(q-c),self.r)
        got=sp.factor(sp.diff(pprime_diff,self.r,3).subs(self.r,self.r0))
        self.assertEqual(sp.factor(got-16*self.r0**6*self.vals[3]),0)
        self.assertNotEqual(got,0)

    def test_normalized_residual_cubic_third_jet(self):
        v,_=endpoint_radial_residual_derivatives(self.G,self.s,self.u,self.s0,self.u0)
        # d^3/dr^3 H = (2r)^3 * (-2s U_ssss) at the endpoint.
        self.assertEqual(sp.factor(v[3][3]+16*self.s0**sp.Rational(5,2)*self.vals[3]),0)

    def test_exact_polynomial_solution_u_s5(self):
        G=2*self.u+10*self.s**5  # U'=5*s^4, U=s^5+C.
        jets=jets_through_four(G,self.s,self.u)
        for k in range(1,5):
            self.assertEqual(sp.factor(jets[k-1]-sp.diff(self.s**5,self.s,k)),0)

    def test_radius_center_excluded(self):
        # This recurrence divides by 2s and is not a center proof.
        self.assertTrue(sp.denom(sp.together(self.js[0])).has(self.s))

    def test_negative_control_cubic_not_third_jet_exact(self):
        v,_=endpoint_radial_residual_derivatives(self.G,self.s,self.u,self.s0,self.u0)
        with self.assertRaises(AssertionError):self.assertEqual(v[3][3],0)

if __name__=='__main__':unittest.main()
