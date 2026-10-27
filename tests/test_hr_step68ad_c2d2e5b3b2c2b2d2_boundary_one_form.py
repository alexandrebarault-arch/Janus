"""Regression for the bare six-pair non-IBP radial boundary one-form."""
import contextlib
import io
import pathlib
import runpy
import unittest

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / 'numerics' / 'hr_step68ad_c2d2e5b3b2c2b2d2_boundary_one_form.py'

class BoundaryOneFormTests(unittest.TestCase):
    def test_symbolic_boundary_one_form(self):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            runpy.run_path(str(SCRIPT))
        output = stream.getvalue()
        self.assertIn('TOTAL: 27 substantive symbolic/rational assertions PASS', output)
        self.assertIn('11 independent original-minus-IBP boundary one-form identities PASS', output)
        self.assertIn('HR interaction shift derivative identity PASS', output)

if __name__ == '__main__':
    unittest.main()
