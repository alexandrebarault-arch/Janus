import unittest
import sympy as sp
from numerics.hr_b3c3d6_cubic_quartic_step58_jet_invariance import certificate,source_order_contract

class CubicQuarticStep58Metamorphic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=certificate()
    def test_all_five_divided_differences(self):
        self.assertEqual(self.result['divided_differences_verified'],5)
    def test_fourth_jet_not_generally_equal(self):
        self.assertTrue(all(sp.simplify(v)!=0 for v in self.result['fourth_order_differences'].values()))
    def test_linear_pLf_fourth_jump(self):
        r0,u4=sp.symbols('r0 u4',positive=True)
        self.assertEqual(sp.simplify(self.result['fourth_order_differences']['pLf']-16*r0**6*u4),0)
    def test_U_fourth_jump(self):
        r0,u4=sp.symbols('r0 u4',positive=True)
        self.assertEqual(sp.simplify(self.result['fourth_order_differences']['U']-16*r0**4*u4),0)
    def test_source_order_contract_limited(self):
        v=source_order_contract()
        self.assertEqual((v['max_canonical_jet'],v['max_shift_jet']),(3,3))
        self.assertFalse(v['original_source_reexecuted'])
    def test_nonphysical_scope_explicit(self):
        self.assertFalse(self.result['original_step58_executed'])
        self.assertEqual(self.result['through_order'],3)
if __name__=='__main__':unittest.main()
