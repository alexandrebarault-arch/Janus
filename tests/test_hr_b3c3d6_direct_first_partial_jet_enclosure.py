import unittest
from fractions import Fraction as Q
import sympy as sp
from numerics.hr_b3c3d6_direct_first_partial_jet_enclosure import (
    RInterval as I, exact_ode_jet, enclose_second_jet,
    total_s_derivative, symbolic_residuals)


class FirstPartialJet(unittest.TestCase):
    def test_symbolic_ode_identities(self):
        self.assertEqual(symbolic_residuals(),[0,0])

    def test_geometry_chain_rule_not_naive_partial(self):
        s,u,a,b=sp.symbols('s u a b')
        e=a*u**2+b*s
        geo={a:1+s*s,b:1/(1+s)}
        gs,g=total_s_derivative(e,s,u,geo)
        self.assertEqual(sp.simplify(gs-sp.diff(g,s)),0)
        self.assertEqual(sp.simplify(gs-sp.diff(e,s).subs(geo)),2*s*u*u-s/(1+s)**2)

    def test_geometry_u_derivative_fixed(self):
        s,u,a=sp.symbols('s u a')
        gs,g=total_s_derivative(a*u**2,s,u,{a:1+s*s})
        self.assertEqual(sp.diff(gs,u),4*s*u)
        self.assertEqual(sp.simplify(sp.diff(g,u,2)-2*(1+s*s)),0)

    def test_rational_jets_consistent(self):
        out=exact_ode_jet(Q(289,400),Q(3,7),Q(9,8),Q(-2,3),Q(-1,2))
        self.assertEqual(out['pLf_second'],2*Q(3,7)+10*Q(289,400)*out['U_s']+4*Q(289,400)**2*out['U_ss'])

    def test_degenerate_exact_box(self):
        s,u,g,gs,gu=Q(1,4),Q(3,2),Q(7,3),Q(-2,7),Q(5,9)
        out=exact_ode_jet(s,u,g,gs,gu)
        boxes=enclose_second_jet(s,I(u),I(g),I(gs),I(gu))
        for k,v in out.items(): self.assertEqual((boxes[k].lo,boxes[k].hi),(v,v))

    def test_dependency_safe_for_polynomial_toy(self):
        # Physical G(s,u)=(1+s^2)*u^2+s/(1+s); all inputs exact rational.
        s=Q(1,2); ub=I(Q(1,3),Q(2,3))
        g=(I(1)+s*s)*ub*ub+I(s)/(1+s)
        gs=2*s*ub*ub+I(1)/(1+s)**2
        gu=2*(1+s*s)*ub
        out=enclose_second_jet(s,ub,g,gs,gu)
        for k in range(101):
            u=Q(1,3)+Q(k,300)
            gv=(1+s*s)*u*u+s/(1+s)
            gsv=2*s*u*u+1/(1+s)**2
            guv=2*(1+s*s)*u
            actual=exact_ode_jet(s,u,gv,gsv,guv)
            for name,v in actual.items(): self.assertTrue(out[name].contains(v),(name,k))

    def test_negative_gu_does_not_imply_gs_bound(self):
        # G=-u+a*s*u; G_U near -1 while G_s=a*u needs independent bound.
        s=Q(1,4);u=Q(1,2)
        a=Q(1,100)
        out=exact_ode_jet(s,u,(-1+a*s)*u,a*u,-1+a*s)
        self.assertNotEqual(out['pLf_second'],(-1+a*s)*u+(-1+a*s)*((-1+a*s)*u-2*u))

    def test_invalid_center(self):
        with self.assertRaises(ValueError): enclose_second_jet(0,I(1),I(2),I(3),I(4))
        with self.assertRaises(ValueError): exact_ode_jet(0,1,2,3,4)

    def test_division_zero(self):
        with self.assertRaises(ZeroDivisionError): _=I(1)/I(-1,1)

    def test_reversed_box(self):
        with self.assertRaises(ValueError): I(2,1)


if __name__=='__main__': unittest.main()
