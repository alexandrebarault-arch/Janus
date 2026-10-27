"""Regression replay for the exact primary-tangent witness (not full Dirac)."""
import importlib.util
import pathlib
import unittest


class PrimaryTangentWitness(unittest.TestCase):
    def test_exact_pointwise_constraints_and_curvature(self):
        source = pathlib.Path(__file__).resolve().parents[1] / 'numerics' / 'hr_step68ad_c2d2e5b3b2c2b2d2c_primary_tangent.py'
        spec = importlib.util.spec_from_file_location('janus_d2c_primary_tangent', source)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.run_checks()
        self.assertEqual(result['assertions_passed'], 19)
        self.assertEqual(result['assertions_failed'], 0)
        self.assertEqual(result['witness']['dTheta_dy_dx'], '6/25')
        self.assertEqual(result['scientific_status']['JANUS_R'], 'NOT_VALIDATED')


if __name__ == '__main__':
    unittest.main()
