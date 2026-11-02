import json
import tempfile
import unittest
from fractions import Fraction as Q
from pathlib import Path
from numerics import hr_b3c3d7_annular_lipschitz_sign_gate as c


class AnnularLipschitzSignGate(unittest.TestCase):
    def test_pinned_original_report_and_sha(self):
        self.assertEqual(c.git_blob((Path(__file__).resolve().parents[1] / c.ARCHIVE).read_bytes()),c.ARCHIVE_BLOB)
        self.assertEqual(len(c.pinned_boxes()),4)

    def test_tampered_report_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/c.ARCHIVE
            p.parent.mkdir(parents=True)
            p.write_bytes((Path(__file__).resolve().parents[1]/c.ARCHIVE).read_bytes()+b' ')
            with self.assertRaisesRegex(ValueError,'blob mismatch'):
                c.pinned_boxes(td)

    def test_normalized_sign_margins(self):
        rows=c.normalized_rows()
        self.assertEqual(rows[0],(Q(1,16),(Q(3424),Q(3568)),(Q(6608),Q(6880))))
        self.assertEqual(rows[-1][0],Q(289,400))
        self.assertEqual(rows[-1][1][0],Q(954000,289))
        self.assertEqual(rows[-1][2][0],Q(1835200,289))

    def test_exact_sharp_thresholds(self):
        t=c.sharp_lipschitz_thresholds()
        self.assertEqual(t['A_N_over_s'],Q(4123900,147))
        self.assertEqual(t['minus_A_M_over_s'],Q(378550,7))
        self.assertEqual(len(t['by_gap']),3)

    def test_conditional_strict_positive_ratio_everywhere_on_annulus(self):
        result=c.conditional_continuum_certificate(1000,1000)
        self.assertGreater(result['a_strict'][0],0)
        self.assertGreater(result['q_strict'][0],0)
        self.assertGreater(result['rho_strict'][0],0)
        self.assertLess(result['rho_strict'][0],result['rho_strict'][1])
        self.assertGreater(result['rho_strict'][0],Q(46,100))
        self.assertLess(result['rho_strict'][1],Q(59,100))
        self.assertEqual(result['scope'],'CONDITIONAL_ONLY_NOT_ACTUAL_PHYSICAL_CONTINUUM_ENCLOSURE')

    def test_gate_fails_closed_at_or_above_threshold(self):
        t=c.sharp_lipschitz_thresholds()
        for n,m in [(t['A_N_over_s'],0),(0,t['minus_A_M_over_s']),(-1,0),(0,-1)]:
            with self.assertRaises(ValueError):c.conditional_continuum_certificate(n,m)

    def test_two_analytic_models_same_four_exact_samples(self):
        for s,(anlo,anhi),(qlo,qhi) in c.normalized_rows():
            self.assertEqual(c.bad_m(s),c.toy_m(s))
            self.assertTrue(anlo<c.toy_a(s)<anhi)
            self.assertTrue(qlo<-c.bad_m(s)<qhi)

    def test_bad_model_preserves_center_first_two_coefficients(self):
        self.assertEqual(c.bad_m(0),-6750)
        self.assertEqual(c.toy_m(0),-6750)
        self.assertEqual(c.toy_m(1)-c.toy_m(0),375)
        for s in (Q(1,100),Q(1,10**9)):
            self.assertEqual((c.bad_m(s)-c.bad_m(0)-375*s)/s**2, c.PERTURBATION*c.sample_vanishing_polynomial(s))
        self.assertEqual(Q(3500,6750),Q(14,27))

    def test_bad_model_interior_zero_blocks_positive_lapse(self):
        s=c.INTERIOR_S
        self.assertEqual(s,Q(9,64))
        self.assertEqual(c.bad_m(s),0)
        self.assertGreater(c.toy_a(s),0)
        self.assertGreater(s*c.toy_a(s),0)
        self.assertEqual(s*c.bad_m(s),0)

    def test_mvt_lower_bound_exceeds_gate(self):
        bound=-c.bad_m(Q(1,16))/(c.INTERIOR_S-Q(1,16))
        self.assertEqual(bound,86100)
        self.assertGreater(bound,c.sharp_lipschitz_thresholds()['minus_A_M_over_s'])

    def test_full_audit_explicit_limits(self):
        a=c.audit()
        self.assertFalse(a['physical_continuum_derivative_bound_computed'])
        self.assertFalse(a['physical_center_0_to_1_over_4_certified'])
        self.assertFalse(a['physical_dirac_BVP_certified'])
        self.assertEqual(a['JANUS_R'],'NOT_VALIDATED')

if __name__=='__main__': unittest.main()
