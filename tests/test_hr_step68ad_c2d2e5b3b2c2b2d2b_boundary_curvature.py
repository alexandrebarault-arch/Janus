"""Regression: exact reduced-shift boundary curvature and restricted primitives."""
import importlib.util
import pathlib
import unittest


class BoundaryCurvatureTest(unittest.TestCase):
    def test_exact_curvature_and_restricted_counterterms(self):
        path = pathlib.Path(__file__).resolve().parents[1] / 'numerics' / 'hr_step68ad_c2d2e5b3b2c2b2d2b_boundary_curvature.py'
        spec = importlib.util.spec_from_file_location('janus_boundary_curvature', path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.run_checks(), 21)


if __name__ == '__main__':
    unittest.main()
