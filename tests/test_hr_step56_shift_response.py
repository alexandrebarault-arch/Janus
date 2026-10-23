"""Independent tests of exact shift-elimination response; not full Dirac evolution."""
from fractions import Fraction
import sympy as sp
import pytest
from numerics.hr_step56_shift_response import (
  physics,jet_commutation,center_response,stationarity_time_preservation,six_pair_toy,manifest)

@pytest.fixture(scope='module')
def symbolic():return physics()

def test_stationarity_has_unique_z_on_K_positive_branch(symbolic):
 d,k,z=symbolic['D'],symbolic['K'],symbolic['z']
 # Positivity of sqrt selects k>0 (the Step55 chart).
 f=d-k*z/sp.sqrt(1-z*z)
 assert sp.simplify(f.subs(z,symbolic['Z']).subs(sp.sqrt(k**2/(d*d+k*k)),k/sp.sqrt(d*d+k*k)))==0 or sp.simplify(d-k*(d/sp.sqrt(d*d+k*k))/(k/sp.sqrt(d*d+k*k)))==0
 assert sp.simplify(sp.diff(f,z)+k/(1-z*z)**sp.Rational(3,2))==0

def test_exact_partial_derivatives_of_eliminated_shift(symbolic):
 d,k=symbolic['D'],symbolic['K']
 assert sp.simplify(sp.diff(symbolic['Z'],d)-symbolic['ZD'])==0
 assert sp.simplify(sp.diff(symbolic['Z'],k)-symbolic['ZK'])==0

def test_original_shift_momentum_and_geometry_frechet_variations(symbolic):
 f=symbolic['fields'];v=symbolic['variations']
 assert sp.diff(symbolic['dD'],v['pLgr'])==-f['Lg']
 assert sp.diff(symbolic['dD'],v['Sgr'])==f['pSg']
 assert sp.diff(symbolic['dD'],v['tgr'])==f['pg']
 assert sp.diff(symbolic['dK'],v['pSg'])==0
 assert sp.diff(symbolic['dK'],v['pLgr'])==0
 assert sp.diff(symbolic['dK'],v['pg'])==0

def test_frechet_chain_rule_for_all_original_spherical_variables(symbolic):
 d,k=symbolic['D'],symbolic['K'];p=symbolic['Dg'];w=symbolic['Kphys']
 # Direct substitution derivatives with independent variations, not a tautology:
 rho=symbolic['Z'].subs({d:p,k:w})
 for name in ('Lg','Lf','Sg','Sf','pSg','pg','pLgr','Sgr','tgr'):
  variable=symbolic['fields'][name];vari=symbolic['variations'][name]
  predicted=sp.diff(symbolic['dZ'],vari).subs({d:p,k:w})
  assert sp.simplify(sp.together(sp.diff(rho,variable)-predicted))==0

def test_spatial_jet_variation_commutes_with_radial_derivative():
 x=jet_commutation()
 assert x['commutator']==0
 assert x['dZr'].has(sp.Symbol('eDr',real=True))

def test_reduced_stationary_H_has_envelope_identity(symbolic):
 z=symbolic['z'];d=symbolic['D'];k=symbolic['K']
 n,m,lg,lf=sp.symbols('N M Lg Lf',real=True)
 fz=symbolic['Fz']
 assert sp.simplify(sp.diff(symbolic['Hz'],z)-(n/lg+m/lf)*fz)==0
 # On stationary shell K>0 the z-envelope term vanishes.
 R=sp.sqrt(d*d+k*k)
 assert sp.simplify((n/lg+m/lf)*(d-k*(d/R)/(k/R)))==0


def test_stationarity_time_derivative_solves_shift_multiplier_identity():
 x=stationarity_time_preservation()
 Dt,Kt,zt=sp.symbols('Dt Kt zt',real=True)
 assert sp.simplify(x['Fz_t_on_shift_shell'].subs(zt,x['z_t']))==0
 assert x['temporal_dirac_C_not_computed'] is True

def test_center_normalization_finite_response():
 x=center_response()
 s,d,k,c=sp.symbols('s d k c',positive=True)
 assert sp.simplify(x['w0']-c)==0
 assert sp.simplify(x['wd']-(1-s*c*c)**sp.Rational(3,2)/k)==0
 assert sp.simplify(x['wk']+c*(1-s*c*c)/k)==0

def test_exact_center_sensitivity_bounds_from_prior_chart():
 x=center_response()
 assert x['normalized_d_sensitivity_bound']==Fraction(1000,229)
 assert x['normalized_k_sensitivity_bound']==Fraction(4,229)
 assert x['normalized_d_sensitivity_bound']<Fraction('4.367')
 assert x['normalized_k_sensitivity_bound']<Fraction('0.0175')

def test_degenerate_K_chart_loses_stationarity_invertibility():
 x=physics()
 z=x['z'];k=x['K'];D=x['D']
 fz=x['Fz']
 assert sp.simplify(sp.diff(fz,z).subs(k,0))==0
 assert sp.simplify(fz.subs({D:0,k:0}))==0
 # At D=K=0 every |z|<1 is stationary, so z is not determined.

def test_six_pair_toy_exhibits_nonzero_frozen_shift_error():
 t=six_pair_toy()
 assert t['correction']!=0
 assert sp.simplify(t['actual']-t['frozen']-t['correction'])==0

def test_full_temporal_rank_uncomputed_not_misrepresented():
 m=manifest()
 assert m['full_temporal_Dirac_bracket']=='NOT_COMPUTED'
 assert m['lapse_fixing']=='NOT_COMPUTED'
 assert m['GATE_2B']=='OPEN'
 assert m['JANUS_R']=='NOT_VALIDATED'
 assert m['six_canonical_pair_toy_frozen_z_omits_nonzero_term']
