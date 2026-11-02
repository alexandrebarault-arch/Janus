"""Four exact radius outer-rounding Step58 A_N/A_M sign verification."""
import unittest
from fractions import Fraction as F
from pathlib import Path
from tempfile import TemporaryDirectory
from numerics import hr_b3c3d6_boundary_ANAM_interval_certificate as c

MARGINS={
    '1/4':(214,223,-430,-413,-215,-190),
    '1/2':(847,883,-1697,-1634,-850,-751),
    '7/10':(1639,1709,-3279,-3157,-1640,-1448),
    '17/20':(2385,2489,-4768,-4588,-2383,-2099),
}
class TestPhysicalStep58Interval(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.boxes=c.enclose_all()

    def test_radii(self):
        self.assertEqual(set(self.boxes),set(MARGINS))

    def test_all_sixteen_signs(self):
        for row in self.boxes.values():
            self.assertTrue(row['A_N'].strictly_positive())
            self.assertTrue(row['A_M'].strictly_negative())
            self.assertTrue(row['A_N_plus_A_M'].strictly_negative())

    def test_exact_integer_margins(self):
        for r,(nl,nh,ml,mh,sl,sh) in MARGINS.items():
            for key,lo,hi in [('A_N',nl,nh),('A_M',ml,mh),('A_N_plus_A_M',sl,sh)]:
                box=self.boxes[r][key]
                self.assertGreater(F(box.lo,c.S),F(lo), (r,key,'lower'))
                self.assertLess(F(box.hi,c.S),F(hi), (r,key,'upper'))

    def test_exact_dust_and_G_bounds(self):
        for row in self.boxes.values():
            self.assertTrue(row['U'].strictly_negative())
            self.assertTrue(row['U_ss'].lo <= row['U_ss'].hi)

    def test_archival_git_blob_and_entries(self):
        root=Path(__file__).resolve().parents[1]
        self.assertTrue(c.validate_archive(root))

    def test_archive_tamper_rejected(self):
        with TemporaryDirectory() as folder:
            target=Path(folder)/'research/reports/gate2b-b3c3d6-physical-monotone-G-four-exact-radii.json'
            target.parent.mkdir(parents=True)
            orig=(Path(__file__).resolve().parents[1]/'research/reports'/target.name).read_bytes()
            target.write_bytes(orig.replace(b'1/4',b'1/5',1))
            with self.assertRaises(ValueError):c.validate_archive(Path(folder))

    def test_outward_exact_interval_arithmetic(self):
        for q in (F(2,7),F(-5,11),F(19,30),F(-1,10)):
            x=c.I.c(q)
            self.assertLessEqual(F(x.lo,c.S),q)
            self.assertGreaterEqual(F(x.hi,c.S),q)
            if q:
                y=x.inv()
                self.assertLessEqual(F(y.lo,c.S),1/q)
                self.assertGreaterEqual(F(y.hi,c.S),1/q)
        root=c.I.c(2).sqrt()
        self.assertLessEqual(F(root.lo,c.S)**2,2)
        self.assertGreaterEqual(F(root.hi,c.S)**2,2)

    def test_holonomic_third_order_jet(self):
        x=c.Jet((F(2,3),1,F(1,2),F(1,6)))
        for n,factor in ((0,1),(1,1),(2,2),(3,6)):
            y=x.val(n)
            val=x.a[n]*factor
            self.assertEqual(y.lo,val.lo)
            self.assertEqual(y.hi,val.hi)
        inv=(x*x.inv()).a
        for n,y in enumerate(inv):
            target=1 if n==0 else 0
            self.assertLessEqual(F(y.lo,c.S),target)
            self.assertGreaterEqual(F(y.hi,c.S),target)

    def test_original_source_dependency_jet_ceiling(self):
        from numerics.hr_step58_temporal_operator import physical_operator
        from numerics.hr_step45_exact_physical_ward import exact_physical_ward
        p=exact_physical_ward();o=physical_operator()
        for label in ('N','M'):
            free=o['operator'][label][0].free_symbols
            for field in ('pLf','pSf','pf'):
                idx=p['Q'].index(field)
                for vec in (o['qpp'],o['qppp']):
                    self.assertNotIn(vec[idx],free)

    def test_conditional_nogo_only(self):
        self.assertLess(self.boxes['17/20']['A_N_plus_A_M'].hi,0)
        # No assertion of a generic two-lapse BVP or 4D Janus viability.

if __name__=='__main__':unittest.main()
