"""Original Step45/58 default; explicit offline transcription mode is NOT original replay."""
import hashlib, os, unittest
from pathlib import Path
import sympy as s
OFFLINE = os.getenv('JANUS_TRANSCRIPTION_ONLY') == '1'
if OFFLINE:
    from step45clone import exact_physical_ward
    from step58clone import physical_operator
    from hr_b3c3d6_bn_high_jet_elimination import verify_high_jet_elimination
else:
    from numerics.hr_step45_exact_physical_ward import exact_physical_ward
    from numerics.hr_step58_temporal_operator import physical_operator
    from numerics.hr_b3c3d6_bn_high_jet_elimination import verify_high_jet_elimination

class TestHighJetReduction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=exact_physical_ward();cls.o=physical_operator()

    def test_original_blob_sha(self):
        if OFFLINE:self.skipTest('offline transcription, not original replay')
        root=Path(__file__).resolve().parents[1]/'numerics'
        for name,sha in [('hr_step45_exact_physical_ward.py','66aa43841dccfe4a5d586a49be9c10af3a67a10e'),('hr_step58_temporal_operator.py','802c23aebd41780d8c462f1aa1711707fe4ee88f')]:
            data=(root/name).read_bytes()
            self.assertEqual(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),sha)

    def test_four_exact_factors(self):
        c=verify_high_jet_elimination(self.p,self.o)
        self.assertEqual(c['coefficient_identities_proved'],4)

    def test_support_and_affinity(self):
        c=verify_high_jet_elimination(self.p,self.o)
        self.assertEqual(len(c['high_jet_dependencies_before_Fz']),5)
        q=dict(zip(self.p['Q'],self.p['q']));z=self.o['z']
        R=self.o['operator']['N'][1]-z*self.o['C']/q['Lg']+(1-z*z)/(q['Lg']*q['Lf'])*self.o['Dt'](self.p['Hg'])
        self.assertEqual(s.diff(R,self.o['qpp'][2],2),0)

    def test_Hg_nonzero_slope(self):
        q=dict(zip(self.p['Q'],self.p['q']))
        self.assertEqual(s.cancel(s.diff(self.p['Hg'],self.o['qpp'][2])-2*self.p['parameters'][0]*q['Sg']/q['Lg']),0)

    def test_not_universal_BN_or_physical_BVP(self):
        c=verify_high_jet_elimination(self.p,self.o)
        self.assertIn('NOT proved'.upper(),c['conclusion'].upper())
        self.assertEqual(c['physical_step55_enclosures'],'NOT_CERTIFIED')
        self.assertEqual(c['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
