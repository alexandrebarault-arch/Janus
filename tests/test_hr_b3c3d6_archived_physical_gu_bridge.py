"""Exact tests; historical physical interval arithmetic is NOT rerun here."""
from fractions import Fraction as Q
from pathlib import Path
import json
import sympy as sp
import unittest
from numerics import hr_b3c3d6_archived_physical_gu_bridge as m

ROOT=Path(__file__).resolve().parents[1]

class ArchivedPhysicalGUBridge(unittest.TestCase):
    def test_01_real_report_blob_sha_and_physical_interval(self):
        self.assertEqual(m.read_authenticated_step63(ROOT), (m.ARCHIVED_GU_LO,m.ARCHIVED_GU_HI))

    def test_02_original_source_pins_and_256_cell_coverage(self):
        r=json.loads((ROOT/m.ARCHIVE).read_text())
        self.assertEqual(r['provenance']['original_byte_pins'],m.ORIGINAL_BLOBS)
        self.assertIn('256 continuous cells',r['coverage'])

    def test_03_physical_upper_strict_below_minus_99_over_100(self):
        self.assertGreater(m.CERTIFIED_GAMMA-m.ARCHIVED_GU_HI,0)
        self.assertLess(m.ARCHIVED_GU_LO,m.ARCHIVED_GU_HI)

    def test_04_tampered_report_rejected_by_git_blob(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/m.ARCHIVE;f.parent.mkdir(parents=True)
            f.write_bytes((ROOT/m.ARCHIVE).read_bytes()+b' ')
            with self.assertRaisesRegex(ValueError,'blob mismatch'):m.read_authenticated_step63(d)

    def test_05_forged_positive_derivative_rejected(self):
        r=json.loads((ROOT/m.ARCHIVE).read_text())
        r['rigorous_fractions']['G_U'][1]='1/10'
        with self.assertRaisesRegex(ValueError,'interval drift'):m.check_report_fields(r)

    def test_06_forged_tube_rejected(self):
        r=json.loads((ROOT/m.ARCHIVE).read_text());r['coverage']='sampled points'
        with self.assertRaisesRegex(ValueError,'coverage mismatch'):m.check_report_fields(r)

    def test_07_toy_saturates_rational_bound(self):
        # Toy G=0, exact U=0, v(s)=c*s, D=2c, E(ra)=c*ra^2.
        c=Q(3,7);a=Q(1,4);b=Q(17,20)
        self.assertEqual(m.rational_physical_cell(c*a*a,2*c,a,b),c*b*b)

    def test_08_exact_zero_defect_contraction(self):
        self.assertEqual(m.rational_physical_cell(1,0,Q(1,100),Q(17,20)),Q(1,7225))

    def test_09_chain_equals_one_cell_for_constant_defect(self):
        a=m.four_radius_rational(Q(7,11),[Q(2,5)]*4)
        b=m.rational_physical_cell(Q(7,11),Q(2,5),Q(1,100),Q(17,20))
        self.assertEqual(a,b)

    def test_10_chain_rejects_gap(self):
        with self.assertRaisesRegex(ValueError,'noncontiguous'):
            m.rational_chain(0,[(Q(1,100),Q(1,4),0),(Q(1,3),Q(1,2),0)])

    def test_11_rejects_invalid_radius_or_negative_defect(self):
        for e,d,a,b in [(0,0,0,Q(1,2)),(0,0,Q(1,2),Q(1,4)),(0,0,Q(1,2),1),(-1,0,Q(1,4),Q(1,2)),(0,-1,Q(1,4),Q(1,2))]:
            with self.assertRaises(ValueError):m.rational_physical_cell(e,d,a,b)

    def test_12_strong_exponent_toy_exact_saturation(self):
        # Toy G=gamma*U, gamma=-99/100; exact U=0, v(s)=c*s.
        # f=-299 U/(200s), so residual D=(499/200)c.
        c=Q(3,7);a=Q(1,4);b=Q(17,20)
        bound=m.stronger_physical_cell(c*a*a,Q(499,200)*c,a,b)
        self.assertEqual(sp.simplify(bound-sp.Rational(c.numerator,c.denominator)*sp.Rational(b*b)),0)

    def test_13_strong_decay_is_better_than_rational_decay(self):
        strong=m.stronger_physical_cell(1,0,Q(1,100),Q(17,20))
        weak=m.rational_physical_cell(1,0,Q(1,100),Q(17,20))
        self.assertLess(float(sp.N(strong,40)),float(weak))

    def test_14_zero_defect_and_zero_error(self):
        self.assertEqual(m.four_radius_rational(0,[0]*4),0)

    def test_15_four_radius_guard(self):
        with self.assertRaisesRegex(ValueError,'four continuous'):m.four_radius_rational(0,[0]*3)

if __name__=='__main__':unittest.main()
