import unittest
import sympy as sp
from numerics.hr_b3c3d6_original_step58_minimum_jet import source_guard,certify,sensitivity


class OriginalStep58JetAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.deps=certify();cls.slope=sensitivity()

    def test_original_sha(self):
        self.assertEqual(len(source_guard()),2)

    def test_six_coefficients(self):
        self.assertEqual(set(self.deps),{'N0','N1','N2','M0','M1','M2'})

    def test_U_fields_maximum_first_radial_jet(self):
        self.assertTrue(all(max(v,default=-1)<=1 for d in self.deps.values() for v in d.values()))

    def test_M0_has_unique_pSf_prime(self):
        self.assertEqual(self.deps['M0']['pSf'],[0,1])
        self.assertTrue(all(1 not in d['pSf'] for k,d in self.deps.items() if k!='M0'))

    def test_affine_vs_quadratic_nonzero_sensitivity(self):
        x=self.slope
        values={s:sp.Rational(2) for s in x.free_symbols}
        for s in values:
            if str(s)=='z':values[s]=sp.Rational(1,5)
            if str(s)=='r':values[s]=sp.Rational(1,2)
        self.assertLess(x.subs(values),0)

    def test_zero_shift_limit(self):
        z=next(s for s in self.slope.free_symbols if str(s)=='z')
        self.assertEqual(self.slope.subs(z,0),0)


if __name__=='__main__':unittest.main()
