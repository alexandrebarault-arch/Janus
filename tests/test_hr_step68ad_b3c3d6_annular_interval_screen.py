import unittest
from fractions import Fraction
from numerics.hr_step68ad_b3c3d6_annular_interval_screen import exact_checks, screen_constant_p_q_h


class AnnularIntervalScreen(unittest.TestCase):
    def test_exact_certificate(self):
        self.assertEqual(exact_checks()['exact_assertions'],10)

    def test_rejection(self):
        result=screen_constant_p_q_h(Fraction(1,4),Fraction(17,20),0,-1,-1,Fraction(-1,2),Fraction(1,2),2,1)
        self.assertTrue(result['excluded'])

    def test_non_rejection_is_not_proof(self):
        result=screen_constant_p_q_h(Fraction(1,4),Fraction(17,20),0,-1,1,Fraction(-1,2),Fraction(1,2),2,Fraction(5,6))
        self.assertFalse(result['excluded'])

    def test_guards(self):
        with self.assertRaises(ValueError):
            screen_constant_p_q_h(0,1,0,-1,1,0,1,2,1)
        with self.assertRaises(ValueError):
            screen_constant_p_q_h(Fraction(1,4),1,1,-1,1,0,1,2,1)


if __name__=='__main__':unittest.main()
