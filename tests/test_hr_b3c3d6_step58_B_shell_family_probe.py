import unittest
from numerics.hr_b3c3d6_step58_B_shell_family_probe import check_blobs, exact_family, run, make_operator
import sympy as sp

class OriginalStep58ShellFactorProbes(unittest.TestCase):
    def test_byte_authentication(self):
        self.assertTrue(check_blobs())
    def test_rational_z_symbolic_family(self):
        row = exact_family('z_rational')
        self.assertTrue(all(row[k] for k in ('shell_zero','BM_zero','BN_minus_zC_over_Lg_zero','C_nonzero_as_expression')))
        self.assertEqual(row['symbolic_variables'], 6)
    def test_fixed_z_symbolic_family(self):
        row = exact_family('fixed_z')
        self.assertTrue(all(row[k] for k in ('shell_zero','BM_zero','BN_minus_zC_over_Lg_zero','C_nonzero_as_expression')))
        self.assertEqual(row['symbolic_variables'], 20)
    def test_original_E_shell_and_scientific_gate(self):
        report = run()
        self.assertEqual(report['E_N_E_M'], 'EXACT_ZERO_ON_Fz_Hg_FROM_ORIGINAL_STEP58')
        self.assertEqual(report['physical_Step55_four_radii_B_enclosures'], 'NOT_CERTIFIED')
        self.assertEqual(report['GATE_2B'], 'OPEN')
        self.assertEqual(report['JANUS_R'], 'NOT_VALIDATED')
    def test_derivative_shell_conditions_are_not_optional(self):
        op, original, q, qp, _ = make_operator()
        bm = op['operator']['M'][1]
        bn = op['operator']['N'][1]
        c = op['C']
        # C has no third canonical jets. The two sensitivities are
        # nonzero rational functions, so arbitrarily dropping Fz'/Hg'
        # is not justified by the algebraic family probes.
        self.assertNotEqual(sp.factor(sp.diff(bm, op['qpp'][1])), 0)
        self.assertNotEqual(sp.factor(sp.diff(bn-op['z']*c/q['Lg'], op['qppp'][2])), 0)
    def test_bad_family_rejected(self):
        with self.assertRaises(ValueError): exact_family('not_a_chart')

if __name__ == '__main__': unittest.main()
