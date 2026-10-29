import unittest
import sympy as sp
from numerics.hr_b3c3d6_step55_jet_holonomicity import ode_jets,certificate,toy_witness

class TestHolonomicJets(unittest.TestCase):
    def test_exact_ode_recurrence(self):
        x=certificate()
        self.assertEqual(sp.simplify(x['pLf_second_jet_defect']-4*sp.Symbol('s',positive=True)**2*x['U_ss']),0)

    def test_nonzero_toy_second_and_third_defects(self):
        x=toy_witness()
        self.assertNotEqual(sp.Rational(x['pLf_second_jet_defect']),0)
        self.assertNotEqual(sp.Rational(x['pLf_third_jet_defect']),0)

    def test_zero_defect_for_affine_exact_solution(self):
        s,u=sp.symbols('s u',positive=True)
        # G=2u+2s*c gives U_s=c and U_ss=U_sss=0.
        c=sp.Rational(3,7)
        j=ode_jets(2*u+2*s*c,s,u)
        self.assertEqual(j[0],c)
        self.assertEqual(j[1],0)
        self.assertEqual(j[2],0)

    def test_nonzero_defect_does_not_claim_step55(self):
        s,u=sp.symbols('s u',positive=True)
        j=ode_jets(s*s+u*u,s,u)
        self.assertNotEqual(sp.factor(j[1].subs({s:sp.Rational(1,4),u:sp.Rational(1,2)})),0)

    def test_true_third_derivative_identity(self):
        r=sp.symbols('r',positive=True)
        U=sp.Function('U')
        p=r*r*U(r*r)
        d=sp.diff(p,r,3)
        x=sp.symbols('x',positive=True)
        expected=24*r*sp.Derivative(U(x),x)+36*r**3*sp.Derivative(U(x),x,2)+8*r**5*sp.Derivative(U(x),x,3)
        self.assertEqual(sp.simplify(d-expected.subs(x,r*r).doit()),0)

if __name__=='__main__': unittest.main()
