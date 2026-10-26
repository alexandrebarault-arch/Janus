"""Independent regression tests for the exact K=0 chart lemma."""
import unittest
from fractions import Fraction as F
import hr_step68ad_c2d2e5b3_k0_chart as m

class TestK0Chart(unittest.TestCase):
    def test_rational_domain(self):
        b=m.rational_chart_bounds();self.assertEqual(b['r_domain'],['0','17/20'])
    def test_y_interval(self):
        b=m.rational_chart_bounds();self.assertTrue(0<F(b['y_lower'])<=F(b['y_upper']))
    def test_positive_t_lower(self):
        self.assertGreater(F(m.rational_chart_bounds()['T_over_Lg_squared_lower']),0)
    def test_positive_k_lower(self):
        self.assertGreater(F(m.rational_chart_bounds()['K_over_r_squared_lower']),F(22,100))
    def test_small_shift(self):
        self.assertEqual(F(m.rational_chart_bounds()['max_abs_z']),F(17,5000))
    def test_sampled_k_above_uniform_lower(self):
        low=F(m.rational_chart_bounds()['K_over_r_squared_lower'])
        for s in (F(0),F(1,4096),F(1,1024),m.SMAX):
            self.assertGreaterEqual(m.physical_k(s),low)
    def test_stationarity_symbolic(self):
        self.assertTrue(m.exact_symbolic_checks()['shift_stationarity'])
    def test_k_sign_branches(self):
        c=m.exact_symbolic_checks();self.assertTrue(all(c[k] for k in ('positive_K_root','negative_K_root','negative_K_wrong_sign')))
    def test_k_zero_nonzero_d(self):
        self.assertTrue(m.exact_symbolic_checks()['K_zero_D_nonzero_no_root'])
    def test_nonunique_origin(self):
        c=m.exact_symbolic_checks();self.assertTrue(c['origin_shift_flat'] and c['origin_implicit_rank_zero'])
    def test_noncontinuous_ambient(self):
        c=m.exact_symbolic_checks();self.assertTrue(c['ray_z_3_4'] and c['ray_z_1_0'])
    def test_derivative_blowup(self):
        self.assertTrue(m.exact_symbolic_checks()['ray_derivative_diverges'])
    def test_physical_path_regular(self):
        c=m.exact_symbolic_checks();self.assertTrue(all(c[k] for k in ('physical_path_Fz','physical_path_zprime','physical_path_zsecond')))
    def test_no_dirac_claim(self):
        x=m.manifest();self.assertEqual(x['GATE_2B'],'OPEN');self.assertEqual(x['JANUS_R'],'NOT_VALIDATED')
        self.assertIn('Dirac rank, tertiary constraints, boundary admissibility',x['not_proved'])
    def test_outside_domain_rejected(self):
        with self.assertRaises(AssertionError):m.physical_k(m.SMAX+F(1,100))

if __name__=='__main__':unittest.main()
