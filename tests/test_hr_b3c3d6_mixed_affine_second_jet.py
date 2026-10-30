import unittest
import sympy as sp
from numerics.hr_b3c3d6_mixed_affine_second_jet import identities, rational_witness

class MixedAffineSecondJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d=identities()

    def test_zero_and_first_jet(self):
        self.assertEqual(self.d['gap0'],0)
        self.assertEqual(self.d['gap1'],0)

    def test_first_nonmatching_coefficient(self):
        h,s0,r0,u0,u1,gs,gu,*_=self.d['symbols']
        self.assertEqual(sp.simplify(self.d['gap2']+gu*self.d['u2']/2),0)

    def test_second_radial_jet(self):
        h,s0,r0,u0,u1,gs,gu,*_=self.d['symbols']
        self.assertEqual(sp.simplify(self.d['pLfr_second_gap']+4*r0**3*gu*self.d['u2']),0)

    def test_second_radial_jet_plf(self):
        h,s0,r0,*_=self.d['symbols']
        self.assertEqual(sp.simplify(self.d['pLf_second_gap']+4*r0**4*self.d['u2'].subs(s0,r0**2)),0)

    def test_direct_radial_differentiation(self):
        h,s0,r0,*_=self.d['symbols']
        r=sp.symbols('r',real=True,positive=True)
        diff_reduced=self.d['mixed_reduced']-self.d['cubic_reduced']
        diff_plfr=r*diff_reduced
        direct=sp.diff(diff_plfr.subs({h:r*r-r0*r0,s0:r0*r0}),r,2).subs(r,r0)
        expected=self.d['pLfr_second_gap'].subs(s0,r0*r0)
        self.assertEqual(sp.factor(direct-expected),0)

    def test_direct_radial_first_jet(self):
        h,s0,r0,*_=self.d['symbols']
        r=sp.symbols('r',real=True,positive=True)
        diff_plfr=r*(self.d['mixed_reduced']-self.d['cubic_reduced'])
        f=diff_plfr.subs({h:r*r-r0*r0,s0:r0*r0})
        self.assertEqual(sp.factor(f.subs(r,r0)),0)
        self.assertEqual(sp.factor(sp.diff(f,r).subs(r,r0)),0)

    def test_nonlinear_rational_witness_nonzero(self):
        w=rational_witness()
        self.assertNotEqual(w['u2'],0)
        self.assertNotEqual(w['second_pLfr'],0)
        self.assertNotEqual(w['second_pLf'],0)

    def test_vanishing_gu_control(self):
        h,s0,r0,u0,u1,gs,gu,*_=self.d['symbols']
        self.assertEqual(sp.simplify(self.d['pLfr_second_gap'].subs(gu,0)),0)

    def test_vanishing_curvature_control(self):
        h,s0,r0,u0,u1,gs,gu,*_=self.d['symbols']
        self.assertEqual(sp.simplify(self.d['pLfr_second_gap'].subs(gs,(4-gu)*u1)),0)

if __name__=='__main__':unittest.main()
