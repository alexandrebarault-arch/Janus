"""Authentic four-provider radial geometry-aware derivative proof tests."""
from fractions import Fraction as F
import pathlib
import sympy as sp
import pytest
import numerics.hr_step62_original_interval_ad as a
from numerics import hr_step55_normalized_secondary as normalized
from numerics import hr_step55_global_barrier as original

@pytest.fixture(scope='module')
def bounds():return a.cover_derivatives(256)

@pytest.fixture(scope='module')
def radial():return a.certify_radial_jet_bounds(256)


def test_four_original_exact_github_hashes():
 assert a.verify_original_blobs()==a.EXPECTED
 assert len(a.EXPECTED)==4


def test_original_step55_exact_256_cell_barrier_reproduced():
 d=original.certify_global_barrier(256)
 assert d['strict_max_Fupper_rational']=='-1480966474499367232302129/10000000000000000000000000000'
 assert d['strict_min_Flower_rational']=='295653233337826329055403/2000000000000000000000000000'
 assert d['Step54_positive_two_dust_and_JK_signs_apply']


def test_jet2_bivariate_exact_polynomial_with_mixed_derivative():
 s,u=sp.symbols('s u')
 expression=sp.Rational(3,7)+s*u+5*s**2-7*u**2+s**2*u
 j=a.Jet2.s(a.I.c(F(1,4)));k=a.Jet2.u(a.I.c(F(-1,8)))
 p=F(3,7)+j*k+5*j**2-7*k**2+j**2*k
 for name,derivative in [('G',expression),('G_s',sp.diff(expression,s)),
     ('G_U',sp.diff(expression,u)),('G_ss',sp.diff(expression,s,2)),
     ('G_sU',sp.diff(expression,s,u)),('G_UU',sp.diff(expression,u,2))]:
  exact=F(derivative.subs({s:sp.Rational(1,4),u:sp.Rational(-1,8)}))
  d=p.derivatives()[name]
  assert F(d.lo,a.original.S)<=exact<=F(d.hi,a.original.S),(name,d,exact)


def test_jet2_sqrt_division_matches_independent_sympy():
 s,u=sp.symbols('s u')
 expr=sp.sqrt(2+s*u+s**2)/(5+u)
 j=a.Jet2.s(a.I.c(F(1,9)));k=a.Jet2.u(a.I.c(F(1,7)))
 out=(2+j*k+j*j).sqrt()/(5+k)
 for name,v in [('G',expr),('G_s',sp.diff(expr,s)),('G_U',sp.diff(expr,u)),
  ('G_ss',sp.diff(expr,s,2)),('G_sU',sp.diff(expr,s,u)),('G_UU',sp.diff(expr,u,2))]:
  exact=F(str(sp.N(v.subs({s:sp.Rational(1,9),u:sp.Rational(1,7)}),60)))
  got=out.derivatives()[name]
  assert F(got.lo,a.original.S)<=exact<=F(got.hi,a.original.S),name


def test_actual_original_G_at_points_is_enclosed_by_jet_constant():
 for site in ['0','.2','.7225']:
  ss=a.I.c(site);uu=a._tube_at_s(ss)
  old=original.G(ss,uu)
  new=a.physical_G_jet(ss,uu)['G']
  assert new.lo<=old.lo and new.hi>=old.hi


def test_physical_geometry_chain_rule_differs_from_frozen_geometry():
 expr,s,U,v=normalized.normalized_symbolic()
 point=a.I.c('.2');star=original.stars(point)[0]
 u=a.I.c(F(star.lo+star.hi,2*original.S))
 real=a.physical_G_jet(point,u)['G_s']
 xs=sorted(expr.free_symbols,key=str)
 fn=sp.lambdify(xs,sp.diff(expr,s),modules=[{'sqrt':lambda x:x.sqrt(),'Abs':abs},'math'],cse=True)
 inputs=original.geometry(point);inputs.update(s=point,U=u)
 frozen=fn(*[inputs[str(sym)] for sym in xs])
 # The frozen-geometry partial is provably a DIFFERENT physical derivative.
 assert real.lo>frozen.hi


def test_256_cell_full_interval_G_u_strict_negative(bounds):
 low,high=bounds['G_U'];assert F('-1.003')<low<high<F('-.992')


def test_256_cell_G_s_positive_and_G_ss_negative(bounds):
 assert bounds['G_s'][0]>F('.00370')
 assert bounds['G_s'][1]<F('.00409')
 assert bounds['G_ss'][1]<0


def test_256_cell_G_sU_positive_and_G_UU_bounded(bounds):
 assert bounds['G_sU'][0]>F('.00318')
 assert bounds['G_UU'][0]>F('-.020')
 assert bounds['G_UU'][1]<F('.655')


def test_full_range_original_P_second_outward_certified(radial):
 low,hi=radial['P_second']
 assert F('-.01471')<low<hi<F('.000685')


def test_only_interior_original_P_third_interval_certified(radial):
 low,hi=radial['P_third_interior']
 assert F('-.117')<low<hi<F('.120')
 assert radial['P_third_over_r_interior'][0]>F('-1.548')


def test_step55_tube_center_not_claimed_to_bound_P_third():
 x=a.manifest(8)
 assert x['P_third_first_cell'].startswith('NOT CERTIFIED')
 assert x['Dirac_rank']=='NOT COMPUTED' and x['GATE_2B']=='OPEN'


def test_fail_closed_if_historic_original_G_source_changed(monkeypatch):
 bad=dict(a.EXPECTED);bad['hr_step55_normalized_secondary.py']='0'*40
 monkeypatch.setattr(a,'EXPECTED',bad)
 with pytest.raises(ValueError,match='Original changed'):
  a.verify_original_blobs()


def test_interval_ad_refuses_invalid_chart_and_partition():
 with pytest.raises(ValueError):a.Jet2.s(a.I.c(-1)).sqrt()
 with pytest.raises(ValueError):a.cover_derivatives(0)
 with pytest.raises(ValueError):a.certify_radial_jet_bounds(7)


def test_original_global_step55_sources_remain_byte_unchanged_after_AD():
 pre=a.verify_original_blobs()
 _=a.physical_G_jet(a.I.c('.2'),a._tube_at_s(a.I.c('.2')))
 assert a.verify_original_blobs()==pre
 assert isinstance(original.MG,a.I)
