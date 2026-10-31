import unittest
import sympy as S
from numerics.hr_b3c3d6_step58_B_jet_triangular import authenticate,certificate
from numerics.hr_step58_temporal_operator import physical_operator
from numerics.hr_step45_exact_physical_ward import exact_physical_ward

class TestBJetTriangular(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.x=certificate()
    def test_original_sources_byte_authentic(self):self.assertTrue(authenticate())
    def test_three_exact_off_shell_derivative_residuals(self):
        self.assertEqual(self.x['off_shell_high_jet_partial_identities'],3)
    def test_universal_BM_full_shell_remainder(self):
        self.assertEqual(self.x['universal_BM_on_Fz_and_Fzr_zero'],'EXACT_ZERO')
        self.assertIn('Fz_r',self.x['universal_BM_on_Fz_zero'])
    def test_bm_v_shell(self):self.assertEqual(self.x['on_Fz_zero_derivatives']['bm_v'],'3*z*(1 - z**2)/Lf**2')
    def test_delta_v_shell(self):self.assertEqual(self.x['on_Fz_zero_derivatives']['delta_v'],'z*(1 - z**2)/(Lf*Lg)')
    def test_delta_w_shell(self):self.assertEqual(self.x['on_Fz_zero_derivatives']['delta_w'],'-2*Mg2*Sg*(1 - z**2)/(Lf*Lg**2)')
    def test_negative_control_Fz_off_shell(self):
        o=physical_operator();p=exact_physical_ward();q=dict(zip(p['Q'],p['q']));qp=dict(zip(p['Q'],p['dq']))
        v={a:S.S.One for a in (*o['q'],*o['qp'],*o['qpp'],*o['qppp'],*o['q4'],*p['parameters'][:8])}
        v[o['z']]=S.Rational(3,5);v[o['zr']]=S.S.Zero;v[o['zrr']]=S.S.Zero
        v[p['parameters'][3]]=S.S.Zero;v[p['parameters'][4]]=S.S.One
        v[p['parameters'][5]]=S.S.Zero;v[p['parameters'][6]]=S.S.Zero
        v[qp['pLg']]=S.S.Zero
        self.assertNotEqual(S.simplify(o['Fz'].subs(v)),0)
        bm_v=S.diff(o['operator']['M'][1],o['qpp'][1])
        self.assertNotEqual(S.simplify(bm_v.subs(v)-3*o['z'].subs(v)*(1-o['z'].subs(v)**2)/q['Lf'].subs(v)**2),0)
    def test_no_false_global_claim(self):
        self.assertEqual(self.x['universal_B_factorization'],'B_M PROVED; B_N-z*C/Lg NOT_PROVED')
        self.assertEqual((self.x['GATE_2B'],self.x['JANUS_R']),('OPEN','NOT_VALIDATED'))

if __name__=='__main__':unittest.main()
