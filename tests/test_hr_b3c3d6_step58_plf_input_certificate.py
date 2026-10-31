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


class CorrelatedPhysicalGCertificate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from numerics.hr_b3c3d6_step58_plf_input_certificate import certify_correlated_growth
        cls.root=Path(__file__).resolve().parents[1]
        cls.result=certify_correlated_growth(cls.root)

    def test_global_u_sign(self):
        lo,hi=map(F,self.result['global_U_actual'])
        self.assertTrue(-F(67,12500)<lo<=hi<-F(229,50000)<0)

    def test_four_positive_total_derivatives(self):
        self.assertEqual([F(x['r']) for x in self.result['four_exact_radii']],
                         [F(1,4),F(1,2),F(7,10),F(17,20)])
        for row in self.result['four_exact_radii']:
            self.assertGreater(F(row['dG_ds_total'][0]),F(1,2000))
            self.assertGreater(F(row['dG_dr'][0]),0)
            self.assertGreater(F(row['pLf_rr_minus_pLf_r_over_r'][0]),0)

    def test_first_us_sign_undetermined(self):
        lo,hi=map(F,self.result['four_exact_radii'][0]['U_s'])
        self.assertTrue(lo<0<hi)

    def test_independent_hulls_do_not_prove_first_sign(self):
        from numerics.hr_b3c3d6_independent_uss_archive import ARCHIVE
        row=json.loads((self.root/ARCHIVE).read_text())['radii'][0]
        p2=list(map(F,row['pLf_second']));g=list(map(F,row['G_monotone']))
        self.assertTrue(p2[0]-g[1]<0<p2[1]-g[0])

    def test_archive_tamper_rejected(self):
        import tempfile
        from numerics.hr_b3c3d6_independent_uss_archive import ARCHIVE
        from numerics.hr_b3c3d6_step58_plf_input_certificate import certify_correlated_growth
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/ARCHIVE;p.parent.mkdir(parents=True)
            p.write_bytes((self.root/ARCHIVE).read_bytes()+b'\n')
            with self.assertRaises(ValueError):certify_correlated_growth(tmp)
