import unittest
from numerics.hr_step68ad_b3c3d6_sharp_amplitude_reachability import symbolic_checks,toy_checks

class TestSharpAmplitude(unittest.TestCase):
    def test_symbolic(self): self.assertEqual(symbolic_checks(),5)
    def test_exact_toys(self): self.assertEqual(toy_checks()[0],11)
    def test_strict_endpoints(self): self.assertEqual(toy_checks()[1],2)
    def test_not_physical(self):
        import numerics.hr_step68ad_b3c3d6_sharp_amplitude_reachability as mod
        self.assertIn('NOT Step55',mod.__doc__)

if __name__=='__main__': unittest.main()
