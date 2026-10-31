import unittest
import sympy as S
from numerics.hr_b3c3d6_step58_positive_dust_shell_v2 import authenticate,family,certificate

class TestStep58PositiveDustFamily(unittest.TestCase):
    def test_authenticated_originals(self):self.assertTrue(authenticate())
    def test_all_primary_and_jet_constraints(self):
        self.assertTrue(all(x==0 for x in family()['shell'].values()))
    def test_positive_chart(self):
        x=family();self.assertEqual((x['K'],x['z'],*x['dust']),(1,S.Rational(3,5),S.Rational(7,4),1))
    def test_exact_B_factor_on_entire_family(self):
        x=family();self.assertEqual(x['B_factor'],0);self.assertEqual(x['coeff']['M1'],0)
    def test_C_not_automatically_zero_on_primaries(self):
        x=family();self.assertEqual(x['C'].subs(x['a'],0),-S.Rational(9,5))
        self.assertEqual(x['coeff']['N1'].subs(x['a'],0),-S.Rational(27,25))
    def test_C_zero_all_high_lapse_jets(self):
        x=family();a0=-S.Rational(36,25)
        self.assertEqual(x['C'].subs(x['a'],a0),0)
        for key in ('N1','M1','N2','M2'):self.assertEqual(x['coeff'][key].subs(x['a'],a0),0)
    def test_negative_control_Fzr(self):
        x=family();v=dict(x['v']);op=x['op'];v[op['qpp'][1]]+=1
        self.assertNotEqual(S.cancel(op['Dt'](op['Fz']).subs(v)),0)
        self.assertNotEqual(S.cancel(op['operator']['M'][1].subs(v)),0)
    def test_negative_control_Hgr(self):
        x=family();v=dict(x['v']);op=x['op'];v[op['qppp'][2]]+=1
        self.assertEqual(S.cancel(op['Dt'](op['Fz']).subs(v)),0)
        self.assertNotEqual(S.cancel(op['Dt'](x['p']['Hg']).subs(v)),0)
        self.assertNotEqual(S.cancel((op['operator']['N'][1]-op['z']*op['C']/x['q']['Lg']).subs(v)),0)
    def test_no_false_validation(self):
        x=certificate();self.assertEqual((x['GATE_2B'],x['JANUS_R']),('OPEN','NOT_VALIDATED'))

if __name__=='__main__':unittest.main()
