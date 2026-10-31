import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from numerics.hr_b3c3d6_step58_plf_input_certificate import certify

class InputJetCertificate(unittest.TestCase):
    def test_exact_physical_archive_and_three_jets(self):
        out=certify(Path(__file__).resolve().parents[1])
        self.assertEqual([x['r'] for x in out['pointwise_radii']],['1/4','1/2','7/10','17/20'])
        for row in out['pointwise_radii']:
            for key in ('pLf','pLf_r','pLf_rr'):
                lo,hi=map(F,row[key]);self.assertLessEqual(lo,hi);self.assertLess(hi,0)
        self.assertEqual(out['six_Step58_A_B_E'],'NOT_CERTIFIED')

    def test_third_jet_not_identified_by_first_partials(self):
        import sympy as sp
        s,u,s0,lam=sp.symbols('s u s0 lam',nonzero=True)
        g=sp.Symbol('a')+sp.Symbol('b')*s+sp.Symbol('c')*u
        d=lam*(s-s0)**2
        self.assertEqual(d.subs(s,s0),0)
        self.assertEqual(sp.diff(d,s).subs(s,s0),0)
        self.assertEqual(sp.diff(d,u),0)
        self.assertEqual(sp.diff(d,s,2).subs(s,s0),2*lam)
        # 2s U_sss = G_ss+2G_sU U_s+G_UU U_s²+(G_U-6)U_ss
        self.assertEqual(sp.simplify((2*lam)/(2*s0)),lam/s0)

if __name__=='__main__':unittest.main()
