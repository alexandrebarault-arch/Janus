"""Pure exact-rational regression tests; NOT physical Step55/58 execution."""
import unittest
from fractions import Fraction as F
from numerics.hr_b3c3d9_annular_direct_enclosure import uniform_r_cells, certify_cover, classify, ode_jets

class Box:
    def __init__(self,lo,hi):self.lo=F(lo);self.hi=F(hi)

class Tests(unittest.TestCase):
    def test_ode_jets_exact_analytic_solution(self):
        # U(s)=s², G(s,U)=2U+4s² along the solution.
        # Partial G_s=8s, G_U=2; U_s=2s, U_ss=2.
        for s in (F(1,16),F(1,4),F(289,400)):
            u=s*s;g=2*u+4*s*s
            self.assertEqual(ode_jets(s,u,g,8*s,F(2)),(2*s,F(2)))

    def test_exact_cover(self):
        cells=uniform_r_cells(256)
        self.assertEqual(cells[0][0],F(1,4))
        self.assertEqual(cells[-1][1],F(17,20))
        self.assertTrue(all(a[1]==b[0] for a,b in zip(cells,cells[1:])))
    def test_nonempty_r_domain(self):
        with self.assertRaises(ValueError):uniform_r_cells(2,0,1)
        with self.assertRaises(ValueError):uniform_r_cells(0)
    def test_positive_and_negative_sign(self):
        self.assertEqual(classify(Box(1,2),Box(-3,-1)),'CERTIFIED')
        self.assertEqual(classify(Box(-1,2),Box(-3,-1)),'INCONCLUSIVE')
        self.assertEqual(classify(Box(1,2),Box(-3,0)),'INCONCLUSIVE')
    def test_coverage_requires_every_cell(self):
        cells=uniform_r_cells(3)
        rows=[{'r':[str(a),str(b)],'A_N':['1','2'],'A_M':['-3','-1'],'status':'CERTIFIED'} for a,b in cells]
        self.assertTrue(certify_cover(rows))
        self.assertFalse(certify_cover(rows[:2]))
        rows[1]['status']='INCONCLUSIVE'
        self.assertFalse(certify_cover(rows))
    def test_coverage_rejects_gap_and_overlap(self):
        cells=uniform_r_cells(2)
        rows=[{'r':[str(a),str(b)],'A_N':['1','2'],'A_M':['-3','-1'],'status':'CERTIFIED'} for a,b in cells]
        rows[1]['r'][0]=str(F(rows[1]['r'][0])+F(1,100))
        self.assertFalse(certify_cover(rows))
        rows[1]['r'][0]=str(F(rows[1]['r'][0])-F(2,100))
        self.assertFalse(certify_cover(rows))
    def test_coverage_rejects_non_strict_signs(self):
        rows=[{'r':['1/4','17/20'],'A_N':['0','2'],'A_M':['-3','-1'],'status':'CERTIFIED'}]
        self.assertFalse(certify_cover(rows))
        rows[0]['A_N'][0]='1';rows[0]['A_M'][1]='0'
        self.assertFalse(certify_cover(rows))

if __name__=='__main__':unittest.main()
