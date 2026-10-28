"""Regression: python -m unittest tests.test_hr_step68ad_b3c3a_diagonal_shift_covariance"""
import unittest
from numerics import hr_step68ad_b3c3a_diagonal_shift_covariance as a

class TestRadialCovariance(unittest.TestCase):
    def test_eight_source_faithful_objects(self):
        cases=[('Ag',a.Ag,1),('Bg',a.Bg,0),('Af',a.Am,1),('Bf',a.Bm,0),
               ('Dg',a.D,2),('K',a.K,2),('Fz',a.Fz,2),('C_zprime',a.Czr,0)]
        for name,expr,weight in cases:
            with self.subTest(name=name):
                a.verify(expr,weight)

if __name__=='__main__':
    unittest.main()
