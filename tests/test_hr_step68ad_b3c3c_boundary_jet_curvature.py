"""Restricted endpoint-jet curvature regression, not a Dirac constraint test."""
import unittest
import sympy as s
from hr_step68ad_b3c3c_boundary_jet_curvature import (
    run, curvature, expected, alpha_pLgr, alpha_pLg,
    Lg, Lf, N, M, K, D, pLg
)

class BoundaryJetCurvature(unittest.TestCase):
    def test_exact_symbolic_derivation(self):
        self.assertEqual(run()['exact_sympy_assertions'],15)
        self.assertEqual(s.simplify(curvature-expected),0)
    def test_rational_nonstep55_witness(self):
        value=expected.subs({Lg:s.Rational(2,5),Lf:s.Rational(3,5),
                             N:1,M:1,K:4,D:3})
        self.assertEqual(value,-s.Rational(32,375))
    def test_boundary_conditions_can_remove_two_form(self):
        # On a one-dimensional endpoint slice (fix pLg OR pLg'),
        # every two-form vanishes. This does not establish admissibility.
        self.assertEqual(alpha_pLg,0)
        self.assertEqual(s.diff(alpha_pLgr,pLg)-curvature,0)
    def test_no_positive_lapse_cancellation(self):
        # N+M Lg/Lf > 0 for strictly positive N,M,Lg,Lf.
        self.assertEqual(s.simplify(expected.subs({N:1,M:1,Lg:2,Lf:3,K:4,D:3})),
                         -s.Rational(32,75))

if __name__=='__main__':unittest.main()
