import unittest
from fractions import Fraction as Q
from numerics.hr_b3c3d6_global_piecewise_defect_budget import Piece,ledger,json_safe

class TestExactPiecewiseLedger(unittest.TestCase):
    def test_exact_zero_defect(self):
        c=ledger([Piece(Q(1,10),Q(1,2),Q(0)),Piece(Q(1,2),Q(1),Q(0))],Q(3))
        self.assertEqual(c['conditional_final_error'],Q(3,10))
        self.assertEqual(c['additive_error'],0)

    def test_constant_defect_saturates(self):
        # G=0, U=0, P=c*(1-a/s) on [a,b]. H=2c, e(a)=0.
        a,b,c=Q(1,4),Q(3,4),Q(7,5)
        bound=ledger([Piece(a,b,2*c)],0)['conditional_final_error']
        self.assertEqual(bound,c*(1-a/b))

    def test_jump_is_indispensable_and_weighted(self):
        # U=0, G=0; first piece P=0; at s=1/2 jump J=1;
        # second P(s)=J*(1/2)/s solves H=0 exactly.
        p=[Piece(Q(1,4),Q(1,2),0,1),Piece(Q(1,2),1,0)]
        v=ledger(p,0)
        self.assertEqual(v['jump_numerator'],Q(1,2))
        self.assertEqual(v['conditional_final_error'],Q(1,2))
        self.assertEqual(ledger([Piece(Q(1,4),1,0)],0)['conditional_final_error'],0)

    def test_defect_and_jump_saturate_together(self):
        # G=0, U=0; P1=2*(1-a/s), a=1/4, b=1/2; P1(b)=1.
        # Jump +1 at b. P2=2*(b/s)+3*(1-b/s), H2=6.
        ps=[Piece(Q(1,4),Q(1,2),4,1),Piece(Q(1,2),1,6)]
        out=ledger(ps,0)
        self.assertEqual(out['defect_numerator'],Q(2))
        self.assertEqual(out['jump_numerator'],Q(1,2))
        self.assertEqual(out['conditional_final_error'],Q(5,2))
        self.assertEqual(out['nonzero_jumps'],1)

    def test_missing_initial_error_is_explicit(self):
        out=ledger([Piece(Q(1,10000),Q(1,2),Q(1,100000))])
        self.assertNotIn('conditional_final_error',out)
        self.assertEqual(out['physical_initial_error'],'NOT_CERTIFIED')
        self.assertEqual(out['GATE_2B'],'OPEN')
        self.assertIsInstance(json_safe(out)['additive_error'],str)

    def test_disconnected_domains_rejected(self):
        with self.assertRaisesRegex(ValueError,'non-contiguous'):
            ledger([Piece(1,2,0),Piece(3,4,0)])

    def test_invalid_negative_defect_and_zero_start(self):
        for pieces in ([Piece(0,1,0)],[Piece(1,2,-1)],[Piece(1,1,0)]):
            with self.assertRaises(ValueError):ledger(pieces)

    def test_final_jump_rejected(self):
        with self.assertRaisesRegex(ValueError,'last piece'):
            ledger([Piece(1,2,0,1)])

    def test_float_is_exact_binary64(self):
        c=ledger([Piece(0.1,0.5,0.)])
        self.assertEqual(c['start'],Q.from_float(.1))
        self.assertNotEqual(c['start'],Q(1,10))

    def test_initial_error_validation(self):
        with self.assertRaises(ValueError):ledger([Piece(1,2,0)],-1)
        with self.assertRaises(TypeError):ledger([Piece('1',2,0)])

if __name__=='__main__':unittest.main()
