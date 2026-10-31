"""Exact nonphysical Step45/58 two-branch pointwise diagnostic."""
import unittest
import sympy as S
from numerics.hr_b3c3d6_step58_two_branch_secondary_lapse import authenticate,exact_family,certificate

class TwoBranchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.a,cls.b,cls.solved,cls.r=exact_family()

    def test_authentic_sources(self):
        self.assertTrue(authenticate())

    def test_full_primary_first_jets(self):
        for k in ('Fz','Fz_r','Hg','Hg_r'):
            self.assertEqual(self.r[k],0)

    def test_hf_branches_only(self):
        self.assertEqual(S.expand(self.r['Hf']),self.b**2-1)
        self.assertEqual(set(S.solve(self.r['Hf'],self.b)),{-1,1})

    def test_secondary_transverse(self):
        self.assertEqual(S.cancel(self.r['C']+(25*self.a+24*self.b+12)/20),0)
        self.assertEqual(S.diff(self.r['C'],self.a),-S.Rational(5,4))
        self.assertEqual(S.diff(self.r['C'],self.b),-S.Rational(6,5))

    def test_temporal_polynomials(self):
        a,b=self.a,self.b
        self.assertEqual(S.cancel(self.r['A_N']-(1200*a*b-3775*a-2048*b*b+2952*b+4408)/1000),0)
        self.assertEqual(S.cancel(self.r['A_M']-(625*a*a-9600*a*b+3600*a+2400*b*b-4704*b-22336)/4000),0)

    def test_B_E_reduction(self):
        self.assertEqual(S.cancel(self.r['B_N']-S.Rational(3,5)*self.r['C']),0)
        for k in ('B_M','E_N','E_M'):
            self.assertEqual(self.r[k],0)

    def test_positive_pointwise_branch(self):
        a,b=self.a,self.b
        v={a:-S.Rational(36,25),b:S.S.One}
        self.assertEqual(self.r['A_N'].subs(v),S.Rational(451,50))
        self.assertEqual(self.r['A_M'].subs(v),-S.Rational(919,250))
        self.assertEqual(-self.r['A_N'].subs(v)/self.r['A_M'].subs(v),S.Rational(2255,919))

    def test_negative_pointwise_branch(self):
        a,b=self.a,self.b
        v={a:S.Rational(12,25),b:-S.S.One}
        self.assertEqual(self.r['A_N'].subs(v),-S.Rational(149,50))
        self.assertEqual(self.r['A_M'].subs(v),-S.Rational(547,250))
        self.assertEqual(-self.r['A_N'].subs(v)/self.r['A_M'].subs(v),-S.Rational(745,547))

    def test_nonholonomic_obstruction(self):
        a,b=self.a,self.b
        for v,expected in [({a:-S.Rational(36,25),b:1},('65/64','-51/16','349/100')),
                           ({a:S.Rational(12,25),b:-1},('-191/64','113/16','-59/100'))]:
            self.assertEqual(tuple(str(self.r[k].subs(v)) for k in ('Fz_rr','Hf_r','C_r')),expected)
            self.assertTrue(all(self.r[k].subs(v)!=0 for k in ('Fz_rr','Hf_r','C_r')))

    def test_certificate_consistency(self):
        c=certificate()
        self.assertEqual(c['GATE_2B'],'OPEN')
        self.assertEqual(c['JANUS_R'],'NOT_VALIDATED')
        self.assertTrue(c['two_pointwise_branches'][0]['positive_lapses_pointwise'])
        self.assertFalse(c['two_pointwise_branches'][1]['positive_lapses_pointwise'])

if __name__=='__main__':unittest.main()
