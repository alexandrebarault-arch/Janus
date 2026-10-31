import unittest
from fractions import Fraction as Q
import sympy as sp
from numerics.hr_b3c3d6_radial_second_jet_budget import (
    S_STAR, GU_LO, GU_HI, exact_radius_epsilon,
    max_abs_g_times_g_minus_one, radial_second_jet_error_bound,
    physical_known_component, symbolic_identities)

class RadialSecondJetTests(unittest.TestCase):
    def test_three_symbolic_ode_identities(self):
        identities=symbolic_identities()
        for name in ('pLf_prime_over_r','pLf_second_derivative','radial_sensitivity'):
            with self.subTest(name=name):
                self.assertEqual(identities[name],0)

    def test_exact_physical_prefix_known_term_only(self):
        d=physical_known_component()
        self.assertEqual(d['epsilon'],exact_radius_epsilon())
        self.assertGreater(d['known_term'],0)
        self.assertLess(d['known_term'],Q(1,100000))
        self.assertGreater(d['unknown_multiplier'],0)
        self.assertLess(d['epsilon'],Q(1,200000))
        self.assertLess(GU_HI,0)

    def test_exact_maximum_with_interior_vertex(self):
        self.assertEqual(max_abs_g_times_g_minus_one(0,1),Q(1,4))
        self.assertEqual(max_abs_g_times_g_minus_one(-1,0),2)
        self.assertEqual(max_abs_g_times_g_minus_one(2,3),6)

    def test_toy_sharp_linear_G(self):
        e=Q(1,1000)
        self.assertEqual(radial_second_jet_error_bound(e,S_STAR,-1,-1,0,0,2),2*e)
        # G=-u: D=G+G_u*(G-2u)=2u, so this bound is attained.

    def test_toy_mixed_exact_bound(self):
        s=Q(1,2); eps=Q(1,100);u0=Q(1,3);u1=u0+eps
        # G=(1+s)u, G_su=1, G_uu=0, F=(s-1)u/(2s)
        def d(u):
            g=(1+s)*u;gu=1+s;gs=u
            return g+2*s*gs+gu*(g-2*u)
        b=radial_second_jet_error_bound(eps,s,Q(3,2),Q(3,2),1,0,1)
        self.assertLessEqual(abs(d(u1)-d(u0)),b)

    def test_chebyshev_uniform_Gu_does_not_control_Gsu(self):
        s,u=sp.symbols('s u',real=True)
        S=sp.Rational(289,400);alpha=sp.Rational(1,10)
        vals=[]
        for n in (3,5,9):
            g=alpha*sp.chebyshevt(n,2*s/S-1)*u
            gu=sp.diff(g,u);gsu=sp.diff(g,s,u)
            self.assertEqual(gu.subs(s,S),alpha)
            self.assertEqual(gsu.subs(s,S),2*alpha*n*n/S)
            # |T_n(x)|<=1 for x in [-1,1], so |G_u|<=alpha on [0,S].
            f=(g-2*u)/(2*s)
            d=g+2*s*sp.diff(g,s)+gu*(g-2*u)
            du=sp.diff(d,u).subs(s,S)
            self.assertEqual(sp.simplify(du-(alpha*(alpha-1)+4*alpha*n*n)),0)
            vals.append(du)
        self.assertTrue(vals[0]<vals[1]<vals[2])

    def test_input_validation(self):
        for args in [(-1,S_STAR,-1,0,0,0,1),(1,0,-1,0,0,0,1),
                     (1,S_STAR,1,-1,0,0,1),(1,S_STAR,-1,0,-1,0,1),
                     (1,S_STAR,-1,0,0,0,-1)]:
            with self.assertRaises(ValueError):radial_second_jet_error_bound(*args)
        with self.assertRaises(ValueError):max_abs_g_times_g_minus_one(1,0)

    def test_sensitivity_identity_on_polynomial(self):
        s,u=sp.symbols('s u',positive=True)
        g=s*u*u+s*s*u
        f=(g-2*u)/(2*s)
        d=g+2*s*sp.diff(g,s)+sp.diff(g,u)*(g-2*u)
        du=sp.diff(g,u)*(sp.diff(g,u)-1)+2*s*(sp.diff(g,s,u)+sp.diff(g,u,2)*f)
        self.assertEqual(sp.simplify(sp.diff(d,u)-du),0)

if __name__=='__main__':unittest.main()
