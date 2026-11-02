import unittest
import sympy as sp
from numerics.hr_b3c3d7_step58_reduced_jet_order_audit import (
    audit, verify_sources, dependency_rows, exact_shell_sensitivity, SOURCE_SHA)
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
from numerics.hr_step58_temporal_operator import physical_operator


class TestOriginalStep58JetOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = dependency_rows()
        cls.operator = physical_operator()

    def test_source_hashes(self):
        self.assertEqual(verify_sources(), SOURCE_SHA)

    def test_step46_original_identities(self):
        self.assertTrue(all(v == 0 for v in exact_f_momentum_ode()['identity_residuals'].values()))

    def test_original_operator_has_both_zero_lapse_coefficients(self):
        self.assertTrue(all(0 in self.operator['operator'][k] for k in ('N', 'M')))

    def test_N_only_zeroth_order_U_dependent_fields(self):
        self.assertEqual(self.rows['N']['U_dependent_fields_and_U_order'], (('pLf',0),('pSf',1)))

    def test_M_has_exact_second_order_path(self):
        self.assertEqual(self.rows['M']['U_dependent_fields_and_U_order'],
                         (('pLf',0),('pSf',1),('pf',1),('pLf',1),('pSf',2)))

    def test_max_U_order(self):
        self.assertEqual((self.rows['N']['max_U_derivative_order'],
                          self.rows['M']['max_U_derivative_order']), (1,2))

    def test_no_U_dependent_second_or_third_radial_jets(self):
        for row in self.rows.values():
            for order in (2,3,4):
                self.assertFalse(set(row['all_fields_by_radial_jet_order'][order]) & {'pLf','pSf','pf'})

    def test_no_fourth_radial_jets_any_field(self):
        self.assertTrue(all(not row['all_fields_by_radial_jet_order'][4] for row in self.rows.values()))

    def test_N_has_no_pSfr(self):
        self.assertEqual(sp.diff(self.operator['operator']['N'][0],sp.Symbol('pSfr')),0)

    def test_M_affine_in_pSfr(self):
        e=self.operator['operator']['M'][0];x=sp.Symbol('pSfr')
        self.assertNotEqual(sp.diff(e,x),0)
        self.assertEqual(sp.diff(e,x,2),0)

    def test_exact_on_shell_identity_and_dust_chain(self):
        self.assertEqual(exact_shell_sensitivity()['dA_M_dUss_on_Fz_primary'], '4*r**4*z*C1/Lf')

    def test_pLf_radial_third_jet_would_need_Usss_but_not_used(self):
        r,r0=sp.symbols('r r0',positive=True)
        u0,u1,u2,u3=sp.symbols('u0 u1 u2 u3')
        h=r*r-r0*r0
        p=r*r*(u0+u1*h+u2*h*h/2+u3*h*h*h/6)
        self.assertEqual(sp.simplify(sp.diff(sp.diff(p,r,3),u3).subs(r,r0)-8*r0**5),0)

    def test_manifest_conservative(self):
        report=audit()
        self.assertFalse(report['direct_interval_gate_requires_G_second_partials'])
        self.assertTrue(report['direct_interval_gate_requires_G_first_partials'])
        self.assertEqual(report['GATE_2B'],'OPEN')
        self.assertEqual(report['JANUS_R'],'NOT_VALIDATED')


if __name__ == '__main__':
    unittest.main()
