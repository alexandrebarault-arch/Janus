import unittest
import sympy as S
from numerics.hr_b3c3d6_uniform_frozen_slice_gap import (
    b,x,P,T,FZ_RR,C_R,GAP,NEGATIVE_H,CELLS,bernstein_cubic,certificate)

class UniformFrozenSliceGap(unittest.TestCase):
    def test_polynomials_and_normalization(self):
        self.assertEqual(S.cancel(FZ_RR+P/(64*b)),0)
        self.assertEqual(S.cancel(C_R-T/(100*b)),0)
    def test_negative_branch_identity(self):
        self.assertEqual(S.cancel(FZ_RR.subs(b,-x)+GAP+NEGATIVE_H/(64*x)),0)
    def test_bernstein_cells_exact_positive(self):
        self.assertEqual(len(CELLS),6)
        for lo,hi in CELLS:
            coeff=bernstein_cubic(NEGATIVE_H,lo,hi)
            self.assertTrue(all(v>0 for v in coeff))
            self.assertEqual(coeff[0],NEGATIVE_H.subs(x,lo))
            self.assertEqual(coeff[-1],NEGATIVE_H.subs(x,hi))
    def test_negative_tail(self):
        self.assertEqual(S.expand(NEGATIVE_H-x*(204*x*x+72*x-197)-56),0)
        self.assertGreater(204*4+72*2-197,0)
    def test_positive_small_branch(self):
        # For 0<b<=1/2, P<-56, so |Fz_rr|>7/4.
        self.assertEqual(S.expand((P+56)-b*(204*b*b-72*b-141)),0)
        self.assertLess(204*S.Rational(1,2)**2-72*S.Rational(1,2)-141,0)
    def test_positive_large_branch(self):
        self.assertEqual(C_R.subs(b,S.Rational(1,2)),S.Rational(109,100))
        self.assertEqual(S.cancel(S.diff(C_R,b)-(S.Rational(72,25)*b+S.Rational(56,25)+S.Rational(1,5)/b**2)),0)
    def test_sampled_negative_guard_not_proof(self):
        for q in [S.Rational(-1,10),S.Rational(-1,4),S.Rational(-1,2),-1,-2,-10]:
            self.assertGreater(-FZ_RR.subs(b,q),GAP)
    def test_scientific_scope(self):
        out=certificate()
        self.assertIn('NONPHYSICAL',out['scope'])
        self.assertEqual(out['physical_Step55_six_enclosures'],0)
        self.assertFalse(out['original_engines_executed_this_run'])
        self.assertEqual(out['GATE_2B'],'OPEN')
        self.assertEqual(out['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__':unittest.main()
