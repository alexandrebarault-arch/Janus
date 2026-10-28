import unittest
import sympy as sp
from numerics.hr_step68ad_b3c3d6_integrating_factor_bvp import certificate, transform


class IntegratingFactorBVP(unittest.TestCase):
    def test_symbolic_certificate(self):
        self.assertEqual(certificate()['symbolic_zero_residuals'],13)

    def test_nonconstant_q(self):
        r=sp.symbols('r');q,p,a,h=transform(0,0,2+r,3,r)
        self.assertEqual(sp.simplify(h-sp.Rational(1,3)),0)
        self.assertEqual(p,0)

    def test_zero_BM_rejected(self):
        with self.assertRaises(ValueError):transform(1,2,3,0,sp.symbols('r'))

    def test_status_not_dirac(self):
        c=certificate()
        self.assertFalse(c['original_step58_probe_executed'])
        self.assertEqual(c['JANUS_R'],'NOT_VALIDATED')


if __name__=='__main__':unittest.main()
