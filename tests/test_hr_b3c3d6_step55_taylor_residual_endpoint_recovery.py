import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from tempfile import TemporaryDirectory
from numerics.hr_b3c3d6_step55_taylor_residual_endpoint_recovery import (
    ARCHIVE, certify, certify_rows, recover_center_from_endpoints)


class TestEndpointRecovery(unittest.TestCase):
    def test_physical_four_points_and_archive_sha(self):
        report=certify()
        self.assertEqual(len(report['four_points']),4)
        self.assertEqual(report['Step58_six_A_B_E'],'NOT_CERTIFIED')

    def test_exact_linear_toy(self):
        self.assertEqual(recover_center_from_endpoints(F(-1,10),F(1,10),-1,F(1,10)),(0,0))

    def test_nonlinear_monotone_toy(self):
        # G(u)=-u-u² on [-1/10,1/10], derivative <= -4/5.
        lo,hi=recover_center_from_endpoints(F(-11,100),F(9,100),F(-4,5),F(1,10))
        self.assertTrue(lo <= 0 <= hi)

    def test_positive_derivative_rejected(self):
        with self.assertRaises(ValueError):
            recover_center_from_endpoints(-1,1,0,F(1,10))

    def test_inconsistent_endpoint_certificate_rejected(self):
        with self.assertRaises(ValueError):
            recover_center_from_endpoints(-F(1,100),F(1,100),-1,F(1,10))

    def test_tampered_archive_sha_rejected(self):
        with TemporaryDirectory() as d:
            p=Path(d)/ARCHIVE
            p.parent.mkdir(parents=True)
            p.write_text('{"radii": []}',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'SHA mismatch'):
                certify(d)

    def test_radii_permutation_rejected(self):
        source=Path(__file__).resolve().parents[1]/ARCHIVE
        rows=json.loads(source.read_text())['radii']
        with self.assertRaisesRegex(ValueError,'radius mismatch'):
            certify_rows(rows[::-1])


if __name__=='__main__':
    unittest.main()
