"""Original-source, parameter-uniform Step55 spatial f/g dust tests."""
import unittest
from fractions import Fraction as F
from unittest.mock import patch
import sympy as sp
from numerics.hr_step68ad_c2d2e5b3b2c2b2_authentic_parameter_tube import (
 ORIGINAL_BLOBS, authenticate_sources, f_density_normalized, certificate)
from numerics import hr_step55_global_barrier as b
from numerics.hr_step55_normalized_secondary import normalized_symbolic
from numerics.hr_step46_exact_secondary_ode import exact_f_momentum_ode
from numerics.hr_step45_exact_physical_ward import exact_certificate_summary

class AuthenticParameterTubeTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.cert=certificate()

 def test_original_four_git_blobs(self):
  self.assertEqual(authenticate_sources(),ORIGINAL_BLOBS)

 def test_reject_tampered_source_expectation(self):
  with patch.dict(ORIGINAL_BLOBS, {'numerics/hr_step55_global_barrier.py':'0'*40}):
   with self.assertRaises(AssertionError): authenticate_sources()

 def test_true_ward_six_pair_original(self):
  self.assertTrue(exact_certificate_summary()['exact_symbolic_residuals_all_zero'])

 def test_true_step46_affine_identity(self):
  self.assertTrue(all(x==0 for x in exact_f_momentum_ode()['identity_residuals'].values()))

 def test_inward_barrier_256(self):
  q=self.cert['original_step55_inward_barrier']
  self.assertLess(F(q['strict_max_Fupper_rational']),0)
  self.assertGreater(F(q['strict_min_Flower_rational']),0)

 def test_dust_both_positive(self):
  self.assertGreater(F(self.cert['rho_f_lower']),F(1,10))
  self.assertGreater(F(self.cert['rho_g_lower']),F(22,25))

 def test_denominators_and_central_chart(self):
  self.assertGreater(F(self.cert['f_dust_denominator_lower']),F(3,4))
  self.assertGreater(F(self.cert['g_dust_beta_lower']),F(999,1000))
  self.assertGreater(F(self.cert['T_lower']),0)

 def test_uniform_u_and_g(self):
  self.assertGreater(F(self.cert['U_lower']),-1)
  self.assertLess(F(self.cert['U_upper']),1)
  q=self.cert['original_step55_inward_barrier']
  self.assertGreater(F(q['V_minus_Vstar_lower_rational']),-F(1,100))
  self.assertLess(F(q['V_minus_Vstar_upper_rational']),F(1,100))

 def test_original_pf_normalization_symbolic(self):
  x=exact_f_momentum_ode();q=x['symbols']['q'];dq=x['symbols']['dq'];mf=x['symbols']['params'][1]
  r=sp.symbols('r',positive=True)
  u,v,lf,sfr,db,wfb,rf,kf,z1=sp.symbols('u v lf sfr db wfb rf kf z1',real=True)
  subs={q['Lf']:lf,q['Sf']:r*lf,q['pLf']:r*r*u,dq['Sf']:sfr,
    dq['tf']:r*kf*lf,x['V']:r*v,x['original_primary_f_shift']:r**3*db,
    x['original_primary_f_potential']:r*r*wfb,x['original_R3f']:rf,
    x['symbols']['params'][-3]:r*z1}
  actual=x['p_f'].subs(subs)/r**2
  den=sp.sqrt(1+kf*kf*r*r)+kf*r*r*u/(2*mf*sfr)
  expected=-(u*u/(4*mf*lf)-u/(2*mf*sfr)*(v-r*r*db/lf)-mf*lf**3*rf/2+r*r*z1*db/lf+wfb)/den
  self.assertEqual(sp.cancel(sp.together(actual-expected)),0)

 def test_original_center_parameter_identity(self):
  expr,s,U,vs=normalized_symbolic();P=sp.Symbol('P',real=True)
  a=sp.Rational(2,5);y=sp.Rational('0.5787707228025044');lf=a*y
  mf=sp.Rational('0.10879548725')**2;m2=sp.Rational('23.3348939346')
  cg=sp.Rational('0.0015');cf=sp.Rational('-0.0012')
  z1=sp.Rational('0.004');kg=sp.Rational('0.0012');kf=sp.Rational('-0.0016')
  beta=tuple(map(sp.Rational,('0','1','-4.2383993109','13.6801214252','-38.5117901844')))
  t=beta[1]*a*a+2*beta[2]*a*lf+beta[3]*lf*lf
  t0=beta[0]*a*a+2*beta[1]*a*lf+beta[2]*lf*lf
  tf=beta[2]*a*a+2*beta[3]*a*lf+beta[4]*lf*lf
  rg=-48*cg/a**2;rf=-48*cf/lf**2
  wgb=m2*(a*t0+lf*t);wfb=m2*(lf*tf+a*t)
  rhog=-(P**2/(4*a)-P**2/a-a**3*rg/2+wgb)
  sub={vs['Lg']:a,vs['Lf']:lf,vs['Sgr']:a,vs['Sfr']:lf,
    vs['Gmom']:P,vs['Psg']:2*P,vs['Rhog']:rhog,vs['Gprime']:2*P,
    vs['tg']:kg*a,vs['tf']:kf*lf,vs['z1']:z1,vs['Dbar']:m2*a*lf*t*z1,
    vs['Wfbar']:wfb,vs['Rf']:rf,vs['Lgr']:4*a*cg,vs['Lfr']:4*lf*cf,
    vs['mg']:1,vs['mf']:mf,vs['m2']:m2}
  sub.update(dict(zip(vs['beta'],beta)))
  self.assertEqual(sp.cancel(sp.together(expr.subs(sub).subs(s,0)-(3*mf*lf*(P/a-2*z1)-U))),0)

 def test_512_cells_revalidate(self):
  c=certificate(cells=512)
  self.assertGreater(F(c['rho_f_lower']),F(1,10))

 def test_128_cell_failure_is_interval_resolution_only(self):
  with self.assertRaisesRegex(ArithmeticError,'invariance NOT certified'):
   certificate(cells=128)

 def test_radius_smaller_and_reject_larger(self):
  self.assertGreater(F(certificate(radius='0.0001')['rho_f_lower']),F(1,10))
  with self.assertRaises(ValueError):certificate(radius='0.0003')

if __name__=='__main__':unittest.main()
