import unittest
from fractions import Fraction as Q
from hr_step68ad_c2d2e5b3b2c2a_gdust_parameter_tube import I, q, sqrt_bounds, parameters, evaluate, certificate

class GdustParameterTubeTests(unittest.TestCase):
    def test_sqrt_exact_square(self):
        self.assertTrue(sqrt_bounds(Q(9,16))[0] <= Q(3,4) <= sqrt_bounds(Q(9,16))[1])
    def test_sqrt_irrational_enclosed(self):
        a,b=sqrt_bounds(Q(2));self.assertLessEqual(a*a,2);self.assertGreaterEqual(b*b,2)
    def test_interval_square_cross_zero(self):
        v=I(-2,3)**2;self.assertEqual(v.lo,0);self.assertEqual(v.hi,9)
    def test_interval_negative_inverse(self):
        v=I(-3,-2).inv();self.assertEqual(v.lo,Q(-1,2));self.assertEqual(v.hi,Q(-1,3))
    def test_interval_reject_zero_division(self):
        with self.assertRaises(AssertionError):I(1)/I(-1,1)
    def test_center_baseline_exact_dust(self):
        x=evaluate(I(0),I(0),parameters())['rho_g'];target=Q(8856,10000)
        self.assertLessEqual(x.lo,target);self.assertGreaterEqual(x.hi,target)
    def test_center_perturbed_dust_positive(self):
        x=evaluate(I(0),I(Q(-1,1000),Q(1,1000)),parameters())['rho_g']
        self.assertGreater(x.lo,Q(22,25))
    def test_positive_g_denominator_at_center(self):
        x=evaluate(I(0),I(Q(-1,1000),Q(1,1000)),parameters())['beta_g']
        self.assertGreater(x.lo,0)
    def test_global_64_cells(self):
        x=certificate(64);self.assertGreater(Q(x['strict_lower_bounds']['rho_g']),Q(22,25))
    def test_global_256_cells(self):
        x=certificate(256);self.assertGreater(Q(x['strict_lower_bounds']['rho_g']),Q(22,25))
    def test_global_512_cells_refinement(self):
        a=certificate(256);b=certificate(512)
        self.assertGreaterEqual(Q(b['strict_lower_bounds']['rho_g']),Q(a['strict_lower_bounds']['rho_g']))
    def test_boundary_parameter_box(self):
        x=certificate(64);self.assertEqual(x['lambda_interval'],['-1/1000','1/1000'])
    def test_status_not_validated(self):
        x=certificate(64);self.assertEqual(x['JANUS_R'],'NOT_VALIDATED');self.assertFalse(x['source_original_modules_reexecuted'])

if __name__=='__main__':unittest.main()
