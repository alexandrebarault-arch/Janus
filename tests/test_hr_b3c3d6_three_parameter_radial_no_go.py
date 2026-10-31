"""On GitHub this imports authentic Step45/58; locally tested with labeled clone wrappers."""
import unittest
import sympy as S
from numerics.hr_b3c3d6_three_parameter_radial_no_go import (
    certificate,derive_from_operator,a,b,c,C,Hf,Frr,Cr,P,T,U,V,BEZOUT)
from numerics.hr_step45_exact_physical_ward import exact_physical_ward
from numerics.hr_step58_temporal_operator import physical_operator

class RestrictedRadialClosure(unittest.TestCase):
    def test_exact_bezout(self):
        self.assertEqual(S.expand(U*P+V*T),BEZOUT)
    def test_nonzero_resultant(self):
        self.assertEqual(S.resultant(P,T,b),4727954587584)
    def test_elimination(self):
        aa=-(24*b+12)/25;cc=(b*b-1)/(2*b)
        self.assertEqual(S.cancel(Frr.subs({a:aa,c:cc})-16*P/b),0)
        self.assertEqual(S.cancel(Cr.subs({a:aa,c:cc})+16*T/(5*b)),0)
    def test_groebner_unit_ideal(self):
        self.assertEqual(list(S.groebner([C,Hf,Frr,Cr],a,b,c,order='grevlex')),[S.S.One])
    def test_original_operator_polynomials(self):
        r=derive_from_operator(exact_physical_ward(),physical_operator())
        self.assertEqual(r['checked_polynomials'],9)
    def test_scientific_gate(self):
        r=certificate()
        self.assertEqual(r['GATE_2B'],'OPEN')
        self.assertEqual(r['JANUS_R'],'NOT_VALIDATED')
        self.assertIn('NOT_PHYSICAL',r['scope'])

if __name__=='__main__':unittest.main()
