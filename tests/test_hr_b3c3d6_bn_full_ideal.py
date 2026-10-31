"""Original engines by default; offline mode is an independent transcription."""
import hashlib,os,unittest
from pathlib import Path
from hr_b3c3d6_bn_full_ideal import certify
OFFLINE=os.getenv('JANUS_TRANSCRIPTION_ONLY')=='1'
if OFFLINE:
    from step45clone import exact_physical_ward
    from step58clone import physical_operator
else:
    from numerics.hr_step45_exact_physical_ward import exact_physical_ward
    from numerics.hr_step58_temporal_operator import physical_operator
class TestBNIdeal(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=certify(exact_physical_ward(),physical_operator())
    def test_sha_originals(self):
        if OFFLINE:self.skipTest('transcription only, no original replay')
        root=Path(__file__).resolve().parents[1]/'numerics'
        for name,sha in [('hr_step45_exact_physical_ward.py','66aa43841dccfe4a5d586a49be9c10af3a67a10e'),('hr_step58_temporal_operator.py','802c23aebd41780d8c462f1aa1711707fe4ee88f')]:
            data=(root/name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),sha)
    def test_four_high_jets(self):self.assertEqual(self.c['four_high_jet_factors'],'EXACT')
    def test_shift_high_jets(self):self.assertEqual(self.c['shift_zrr_zrrr'],'ABSENT')
    def test_two_eliminations(self):self.assertEqual(self.c['Fz_and_Hg_elimination'],'EXACT')
    def test_first_jet_ideal(self):self.assertEqual(self.c['first_jet_remainder'],'ZERO')
    def test_off_shell_negative_control(self):
        import sympy as sp
        p=exact_physical_ward();o=physical_operator()
        q=dict(zip(p['Q'],p['q']));dq=dict(zip(p['Q'],p['dq']))
        sub={x:sp.S.Zero for x in (*p['q'],*p['dq'],*p['ddq'],*o['qppp'],*o['q4'],o['z'],o['zr'],o['zrr'],o['zrrr'],*p['parameters'][:8])}
        for name in ('Lg','Lf','Sg','Sf','pLg','pg','pf'):sub[q[name]]=sp.S.One
        for name,value in [('Sg',1),('pLg',sp.Rational(-3,4)),('Sf',sp.Rational(1,2))]:sub[dq[name]]=value
        sub[o['qpp'][2]]=sp.Rational(-5,4)
        for k in ('Mg2','Mf2','m2'):sub[next(x for x in p['parameters'] if str(x)==k)]=sp.S.One
        sub[next(x for x in p['parameters'] if str(x)=='beta1')]=sp.S.One
        sub[o['z']]=sp.Rational(3,5);sub[o['zr']]=sp.Rational(1,3)
        R=o['operator']['N'][1]-o['z']*o['C']/q['Lg']+(1-o['z']**2)/(q['Lg']*q['Lf'])*o['Dt'](p['Hg'])
        self.assertEqual(sp.cancel(o['Fz'].subs(sub)),0)
        self.assertEqual(sp.cancel(p['Hg'].subs(sub)),2)
        self.assertEqual(sp.cancel(R.subs(sub)),sp.Rational(244,125))
    def test_no_physical_overclaim(self):
        self.assertEqual(self.c['physical_six_A_B_E_enclosures'],'NOT_CERTIFIED')
        self.assertEqual(self.c['JANUS_R'],'NOT_VALIDATED')
if __name__=='__main__':unittest.main()
