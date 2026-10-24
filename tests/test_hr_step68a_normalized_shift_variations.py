"""Targeted algebra tests, not the historical physical Dirac test suite."""
import pytest
import sympy as sp
from fractions import Fraction as F
from numerics.hr_step68a_normalized_shift_variations import (
 exact_variation_jets,exact_certificates,manifest,RMAX,KMIN,W0)

@pytest.fixture(scope='module')
def v():return exact_variation_jets()

def test_implicit_stationarity_frechet(v):
 s,w,k=v['s'],v['w'],v['k'];t=v['t']
 assert sp.simplify(v['ed']-w*v['ek']/sp.sqrt(t)-k*v['delta_w']/t**sp.Rational(3,2))==0

def test_undeformed_step58_delta_D_pullback(v):
 r=v['r'];A,B=v['A'],v['B'];t=v['t'];w=v['w'];k=v['k']
 assert sp.simplify(t**sp.Rational(3,2)/(r*r*k)*r**3*v['ed']-r*A*v['ed'])==0
 assert sp.simplify(-r*w*t/(r*r*k)*r**2*v['ek']-r*B*v['ek'])==0

def test_A_s(v):
 s,k,k1,w,t=[v[q] for q in ('s','k','k1','w','t')]
 assert sp.simplify(v['A1']+3*w*w*sp.sqrt(t)/(2*k)+t**sp.Rational(3,2)*k1/k**2)==0

def test_B_s(v):
 k,k1,w,t=[v[q] for q in ('k','k1','w','t')]
 assert sp.simplify(v['B1']-w**3/k-w*t*k1/k**2)==0

def test_A_ss(v):
 k,k1,k2,w,t=[v[q] for q in ('k','k1','k2','w','t')]
 ans=(3*w**4/(4*k*sp.sqrt(t))+3*w*w*sp.sqrt(t)*k1/k**2 +
      t**sp.Rational(3,2)*(2*k1**2/k**3-k2/k**2))
 assert sp.simplify(v['A2']-ans)==0

def test_B_ss(v):
 k,k1,k2,w,t=[v[q] for q in ('k','k1','k2','w','t')]
 ans=-2*w**3*k1/k**2+w*t*(k2/k**2-2*k1**2/k**3)
 assert sp.simplify(v['B2']-ans)==0

def test_radial_first_chain_rule(v):
 s,w=v['s'],v['w']
 assert sp.simplify(v['delta_zprime']-(v['delta_w']+2*s*v['delta_w_s']))==0

def test_radial_second_chain_rule(v):
 s=v['s'];assert sp.simplify(v['delta_zsecond_over_r']-6*v['delta_w_s']-4*s*v['delta_w_ss'])==0

def test_second_variation_hessian_of_normalized_root(v):
 s=v['s'];k=sp.Function('k')(s);w=v['w']
 ed,ek=sp.Function('ed')(s),sp.Function('ek')(s)
 expr=(1-s*w*w)**sp.Rational(3,2)/k*ed-w*(1-s*w*w)/k*ek
 out=sp.diff(expr,s,2)
 sub={k:v['k'],sp.diff(k,s):v['k1'],sp.diff(k,s,2):v['k2'],
      ed:v['ed'],ek:v['ek'],sp.diff(ed,s):v['ed1'],
      sp.diff(ek,s):v['ek1'],sp.diff(ed,s,2):v['ed2'],sp.diff(ek,s,2):v['ek2']}
 assert sp.simplify(out.subs(sub)-v['delta_w_ss'])==0

def test_spatial_center_linear_coefficient(v):
 s,w,k=v['s'],v['w'],v['k']
 assert sp.simplify(v['delta_zprime'].subs(s,0)-(v['ed']-w*v['ek'])/k)==0

def test_second_jet_center_parity(v):
 assert sp.simplify(v['delta_zsecond_over_r'].subs(v['s'],0)-6*v['delta_w_s'].subs(v['s'],0))==0

def test_nonzero_hamiltonian_profile_variation_negative_control(v):
 q={v['s']:0,v['w']:sp.Rational(1,250),v['k']:sp.Rational(1,2),v['k1']:0,
    v['k2']:0,v['ed']:1,v['ek']:0,v['ed1']:0,v['ek1']:0,v['ed2']:0,v['ek2']:0}
 assert v['delta_zprime'].subs(q)==2
 assert v['delta_zsecond_over_r'].subs(q)==-sp.Rational(9,31250)

def test_zero_variations_give_zero(v):
 zeros={v[k]:0 for k in ('ed','ek','ed1','ek1','ed2','ek2')}
 for x in ('delta_w','delta_w_s','delta_w_ss','delta_zprime','delta_zsecond_over_r'):
  assert sp.simplify(v[x].subs(zeros))==0

def test_delta_k_only_is_not_ignored(v):
 e=v['delta_w'].subs({v['ed']:0,v['ek']:1})
 assert e==v['B'] and e!=0

def test_derivative_k_s_contribution_nonzero(v):
 assert sp.simplify(sp.diff(v['A1'],v['k1'])+v['A']/v['k'])==0
 assert sp.simplify(sp.diff(v['B1'],v['k1'])+v['B']/v['k'])==0

def test_fail_at_nonpositive_k_chart(v):
 assert v['A'].has(v['k'])
 assert v['B'].has(v['k'])
 # Limit k->0 invalid: no bound or IFT in original K=0 chart
 assert sp.limit(v['A'].subs({v['s']:0,v['w']:W0}),v['k'],0,dir='+')==sp.oo

def test_exact_benchmark_t_lower():
 assert 1-RMAX**2*W0**2==F(24999711,25000000)>F(9999,10000)
 assert KMIN>0

def test_manifest_provenance():
 out=manifest(); assert out['step']=='68a'
 assert out['original_HR_provider_imported'] is False
 assert out['full_temporal_operator_assembled'] is False
 assert out['GATE_2B']=='OPEN' and out['JANUS_R']=='NOT_VALIDATED'

def test_center_example_must_not_freeze_variations():
 out=exact_certificates()
 assert out['center_delta_zprime_for_ed_1_k_half']=='2'
 assert out['center_delta_zsecond_over_r_for_ed_1_k_half']=='-9/31250'

def test_exact_reduction_coefficients_on_fixed_background(v):
 # Explicit omission of the k_s term would yield an incorrect nonzero
 # residual: it must survive for arbitrary stationary k(s).
 assert sp.simplify(sp.diff(v['delta_w_s'],v['k1'])+(v['A']*v['ed']+v['B']*v['ek'])/v['k'])==0


def test_k_derivatives_can_have_both_signs(v):
 assert v['k1'].is_positive is None
 assert v['k2'].is_positive is None
 assert sp.simplify(v['delta_zprime'].subs({v['s']:sp.Rational(1,4),v['w']:W0,
                    v['k']:sp.Rational(1,2),v['k1']:-sp.Rational(1,10),
                    v['ed']:1,v['ek']:0,v['ed1']:0,v['ek1']:0})).is_finite
