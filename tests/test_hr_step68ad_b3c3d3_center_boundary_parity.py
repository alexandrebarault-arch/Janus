"""Non-independent reproducibility checks of b3c3d3 symbolic centre lemma."""
import unittest
import sympy as s
from numerics import hr_step68ad_b3c3d3_center_boundary_parity as c

class TestCenterBoundaryParity(unittest.TestCase):
    def test_all_symbolic(self):
        self.assertEqual(c.check()['symbolic_assertions_passed'],25)
    def test_leading_curvature_cancellation(self):
        e=c.terms['Sgr']+c.terms['Lg']+c.terms['Sfr']+c.terms['Lf']
        self.assertEqual(s.simplify(s.limit(e/c.r,c.r,0)),0)
    def test_nonregular_adversarial(self):
        dH0=s.symbols('dH0')
        e=c.coeff['Sgr']*dH0+c.coeff['Lg']*c.dL0
        self.assertEqual(s.simplify(s.limit(e/c.r,c.r,0)-2*c.mg*c.N0*(dH0-c.dL0)),0)
    def test_sharp_order(self):
        e=c.terms['Lg'].subs({c.dL0:0,c.dL2:1})
        self.assertEqual(s.simplify(s.limit(e/c.r**3,c.r,0)), -2*c.mg*c.N0)

if __name__=='__main__':unittest.main()
