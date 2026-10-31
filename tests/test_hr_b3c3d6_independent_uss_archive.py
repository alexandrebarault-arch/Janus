import copy
import unittest
from fractions import Fraction as F
from numerics.hr_b3c3d6_independent_uss_archive import derive, original_u0_interval, load_and_derive


class IndependentUssArchiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import json
        from pathlib import Path
        cls.report=json.loads((Path(__file__).resolve().parents[1]/'research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json').read_text())

    def test_exact_u0_sqrt_enclosure(self):
        lo,hi=original_u0_interval()
        self.assertLess(lo,hi)
        self.assertLess(hi-lo,F(1,10**35))

    def test_all_four_physical_pointwise_budgets(self):
        result=derive(self.report)
        self.assertEqual(len(result['radii']),4)
        for row in result['radii']:
            lo,hi=map(F,row['U_ss']);bound=F(row['U_ss_abs_strict_bound'])
            self.assertLess(-bound,lo)
            self.assertLess(hi,bound)
            self.assertEqual(row['U_ss_sign'],'UNRESOLVED')
        self.assertEqual(result['JANUS_R'],'NOT_VALIDATED')

    def test_original_archive_blob_when_present(self):
        from pathlib import Path
        import hashlib
        from numerics.hr_b3c3d6_independent_uss_archive import ARCHIVE, ARCHIVE_SHA
        raw=(Path(__file__).resolve().parents[1]/ARCHIVE).read_bytes()
        got=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if got != ARCHIVE_SHA:
            self.skipTest('local hand-transcribed fixture, not the authenticated repository archive')
        self.assertEqual(len(load_and_derive()['radii']),4)

    def test_tampered_G_U_rejected(self):
        data=copy.deepcopy(self.report)
        data['radii'][0]['G_U'][1]='1'
        with self.assertRaises(ValueError):derive(data)

    def test_wrong_radius_rejected(self):
        data=copy.deepcopy(self.report)
        data['radii'][3]['r']='0.8500000000000001'
        with self.assertRaises(ValueError):derive(data)

    def test_tampered_pLf_second_rejected(self):
        data=copy.deepcopy(self.report)
        data['radii'][2]['pLf_second'][1]='-1'
        with self.assertRaises(ArithmeticError):derive(data)

    def test_missing_record_rejected(self):
        data=copy.deepcopy(self.report)
        data['radii'].pop()
        with self.assertRaises(ValueError):derive(data)

if __name__=='__main__':unittest.main()
