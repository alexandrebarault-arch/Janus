import unittest
from fractions import Fraction as Q
import sympy as sp
from numerics.hr_b3c3d6_endpoint_ode_jet_transfer import (
    GU_LO,GU_HI,EPS,S_END,endpoint_bounds,ode_jet_maps,
    exact_physical_endpoint_record)

class TestEndpointTransfer(unittest.TestCase):
    def test_physical_rational_bounds(self):
        b=endpoint_bounds()
        self.assertTrue(GU_LO<GU_HI<0)
        self.assertTrue(EPS<Q(1,200000))
        self.assertEqual(b['pLf=sU'],S_END*EPS)
        self.assertEqual(b['pLf_prime_over_r=G'],abs(GU_LO)*EPS)
        self.assertLess(b['U_s_vs_ODE_jet_at_P'],Q(11,1000000))
        self.assertLess(b['pLf_prime_over_r=G'],Q(51,10000000))
        self.assertEqual(len(exact_physical_endpoint_record()),4)

    def test_ode_jets_exact_toy(self):
        s,u=sp.symbols('s u',positive=True)
        G=2*u+2*s*(u**2+s)
        d=ode_jet_maps(G,s,u)
        self.assertEqual(sp.simplify(d['F']-(u**2+s)),0)
        self.assertEqual(sp.simplify(d['Q']-(2*u*(u**2+s)+1)),0)
        self.assertEqual(sp.simplify(d['Q_u']-d['Q_u_expanded']),0)
        self.assertEqual(sp.simplify(d['Q_u']-(6*u**2+2*s)),0)

    def test_dense_derivative_not_inferred(self):
        # P(sR)=U(sR), yet P_s(sR) can be arbitrarily wrong.
        s=sp.symbols('s',real=True)
        U=sp.Integer(1); P=1+10**9*(s-1)
        self.assertEqual((U-P).subs(s,1),0)
        self.assertEqual(abs(sp.diff(U-P,s).subs(s,1)),10**9)
        self.assertEqual(endpoint_bounds(eps=Q(0),s=Q(1),gu_lo=Q(2),gu_hi=Q(2))['U_s_vs_ODE_jet_at_P'],0)

    def test_second_jet_needs_more_than_gu(self):
        s,u,k=sp.symbols('s u k',positive=True)
        # At s=1, G_U=0 for every k, but G_sU=k is unbounded.
        G=k*(s-1)*u
        d=ode_jet_maps(G,s,u)
        self.assertEqual(sp.diff(G,u).subs(s,1),0)
        self.assertEqual(sp.simplify(d['Q_u'].subs(s,1)-k/2-2),0)

    def test_input_guards(self):
        for args in [dict(eps=-1),dict(s=0),dict(gu_lo=3,gu_hi=2)]:
            with self.assertRaises(ValueError):endpoint_bounds(**args)

if __name__=='__main__':unittest.main()
