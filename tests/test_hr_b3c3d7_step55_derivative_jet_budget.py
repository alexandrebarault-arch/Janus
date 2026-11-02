import unittest
import sympy as sp
from numerics import hr_b3c3d7_step55_derivative_jet_budget as m

class JetBudget(unittest.TestCase):
    def test_ode_closure_polynomial(self):
        G=2*m.u+2*m.s*(1+2*m.s+3*m.s**2)
        self.assertTrue(all(sp.simplify(a-b)==0 for a,b in zip(m.ode_jet_closure(G),
                         (1+2*m.s+3*m.s**2,2+6*m.s,sp.Integer(6)))))

    def test_normalized_chain_rule(self):
        A=m.s*(3500-175*m.s)+7*m.s*m.w
        G=2*m.u+2*m.s*(1+2*m.s+3*m.s**2)
        j=m.ode_jet_closure(G)
        derivative=m.normalized_coefficient_derivative(A,j[2])
        got=sp.factor(derivative.subs({m.v:j[0],m.w:j[1]}))
        self.assertEqual(got,sp.Integer(-175+42))

    def test_jet_formula_independent_of_U_value(self):
        G=2*m.u+2*m.s*(3+5*m.s+7*m.s**2)
        self.assertEqual(m.ode_jet_closure(G)[2],sp.Integer(14))

    def test_second_partial_missing_witness(self):
        self.assertEqual(m.missing_second_partial_witness(sp.Rational(1,4)),4)
        self.assertEqual(m.missing_second_partial_witness(sp.Rational(1,2),3),6)

    def test_witness_rejects_center(self):
        with self.assertRaises(ValueError):m.missing_second_partial_witness(0)

    def test_center_recursion(self):
        G=2*m.u+2*m.s*(1+2*m.s+3*m.s**2)
        self.assertEqual(m.center_coefficients(G,0),(sp.Integer(1),sp.Integer(1)))

    def test_center_inconsistent_rejected(self):
        with self.assertRaises(ValueError):m.center_coefficients(2*m.u+1,0)

    def test_center_resonance_rejected(self):
        with self.assertRaises(ValueError):m.center_coefficients(4*m.u,0)

    def test_audit_keeps_scientific_gate_open(self):
        a=m.audit()
        self.assertFalse(a['physical_derivative_bounds_certified'])
        self.assertEqual(a['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
