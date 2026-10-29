import unittest
import sympy as sp
from numerics.hr_b3c3d6_mixed_ode_jet_guard import example, composite_guard, jets_at

class MixedODEJetGuard(unittest.TestCase):
    def test_true_ode_identity(self):
        d=example();s=d['s'];u=d['u'];G=d['G'];f=d['uq']
        self.assertEqual(sp.simplify(2*s*sp.diff(f,s)-G.subs(u,f)+2*f),0)

    def test_cubic_matches_true_up_to_third(self):
        d=example();r=d['r'];r0=d['r0'];s=d['s']
        self.assertEqual(jets_at(d['uq'].subs(s,r*r)-d['uc'].subs(s,r*r),r,r0), (0,0,0,0))
        self.assertEqual(jets_at(d['vq']-d['vc'],r,r0),(0,0,0,0))

    def test_wrong_cubic_derivative_first_disagrees_at_third(self):
        d=example();r=d['r'];r0=d['r0']
        self.assertEqual(jets_at(d['D'],r,r0), (0,0,0,-6))
        self.assertEqual(sp.diff(d['D'],r,3).subs(r,r0),-16*r0**6*d['U4'])

    def test_dependent_fields_good_third_jets(self):
        d=composite_guard();r=d['r'];r0=d['r0']
        self.assertEqual(jets_at(d['good']-d['true'],r,r0),(0,0,0,0))

    def test_dependent_fields_wrong_third_jet(self):
        d=composite_guard();r=d['r'];r0=d['r0']
        j=jets_at(d['bad']-d['good'],r,r0)
        self.assertEqual(j[:3],(0,0,0))
        self.assertEqual(j[3],d['predicted'])
        self.assertNotEqual(j[3],0)

if __name__=='__main__': unittest.main()
