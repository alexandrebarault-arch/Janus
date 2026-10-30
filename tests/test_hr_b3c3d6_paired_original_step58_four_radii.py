import unittest
from fractions import Fraction
from types import SimpleNamespace
from unittest.mock import Mock
import mpmath as mp
from numerics.hr_b3c3d6_paired_original_step58_four_radii import (
    MODES, RADII, compare_coefficients, run_radius, temporarily, truncate_jets)

class PairedRunnerTests(unittest.TestCase):
    def test_radii_exact_list(self):
        self.assertEqual(tuple(map(Fraction.from_float, RADII)),
                         (Fraction(1,4),Fraction(1,2),Fraction(3152519739159347,4503599627370496),Fraction(7656119366529843,9007199254740992)))
    def test_truncated_quadratic_jet(self):
        s=mp.mpf('0.25'); j=dict(U_value=mp.mpf('0.5'),U_s=mp.mpf('2'),
                                   U_ss=mp.mpf('3'),U_sss=mp.mpf('4'))
        q=truncate_jets(j,s,'holonomic_quadratic',mp)
        self.assertEqual(q['U_ss'],3)
        self.assertEqual(q['U_sss'],0)
        self.assertEqual(q['pLf_second'],mp.mpf('6.75'))
        self.assertEqual(q['pLf_third'],mp.mpf('37.5'))
        self.assertEqual(j['U_sss'],4)
    def test_affine_jet_is_holonomic(self):
        j=dict(U_value=mp.mpf('0.5'),U_s=mp.mpf('2'),U_ss=mp.mpf('3'),U_sss=mp.mpf('4'))
        q=truncate_jets(j,mp.mpf('0.25'),'holonomic_affine',mp)
        self.assertEqual(q['pLf_second'],6)
        self.assertEqual(q['pLf_third'],24)
    def test_replacement_restored_even_on_exception(self):
        obj=SimpleNamespace(value=1)
        with self.assertRaisesRegex(ValueError,'boom'):
            with temporarily(obj,value=2):
                self.assertEqual(obj.value,2)
                raise ValueError('boom')
        self.assertEqual(obj.value,1)
    def test_comparison_six_coefficients(self):
        reports={m:{'coefficients':{l:{str(k):float(k) for k in range(3)} for l in 'NM'}} for m in MODES}
        reports['holonomic_affine']['coefficients']['M']['0']=7.
        diff=compare_coefficients(reports)
        self.assertEqual(len(diff),3)
        self.assertEqual(len(diff['holonomic_affine']),6)
        self.assertEqual(diff['holonomic_affine']['M0'],7)
        self.assertEqual(diff['holonomic_quadratic']['M0'],0)
    def test_shared_state_four_modes(self):
        # Fake operators exercise orchestration only; NO physics implied.
        state=(mp.mpf('0.1'),mp.mpf('0.2'),SimpleNamespace(nfev=17))
        def fake_coeff(v):
            return {l:{str(k):float(v if l=='M' and k==0 else k) for k in range(3)} for l in 'NM'}
        affine=SimpleNamespace(u_solution=Mock(side_effect=AssertionError('independent affine solve')),
            main=None)
        cubic=SimpleNamespace(u_solution=Mock(return_value=state),F=mp.mpf,
            endpoint_jets=None,main=None)
        def jets(G,s,u):
            return {'U_s':mp.mpf('1'), 'U_ss':mp.mpf('2'), 'U_sss':mp.mpf('3'),
                    'pLf_second':0,'pLf_third':0,'holonomic_residuals':(0,0,0)}
        cubic.endpoint_jets=jets
        def affine_main(r):
            u,g,sol=affine.u_solution(r)
            return {'coefficients':fake_coeff(1),'ode_jet_map':'MIXED'}
        def cubic_main(r):
            u,g,sol=cubic.u_solution(r)
            j=cubic.endpoint_jets(None,mp.mpf(r)**2,u)
            return {'coefficients':fake_coeff(float(j['U_ss'])),
                    'ode_jet_map':'CUBIC','holonomic_residuals':(0,0,0)}
        affine.main=affine_main;cubic.main=cubic_main
        result=run_radius(0.5,affine,cubic,mp)
        self.assertEqual(cubic.u_solution.call_count,1)
        self.assertEqual(len(result['reports']),4)
        self.assertEqual(result['differences_from_historical_mixed_affine']['holonomic_cubic']['M0'],1)
        self.assertIs(cubic.endpoint_jets,jets)
        self.assertEqual(result['nfev'],17)
    def test_reject_other_radius(self):
        with self.assertRaises(ValueError):
            run_radius(0.6,None,None,mp)

if __name__=='__main__': unittest.main()
