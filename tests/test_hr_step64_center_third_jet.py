"""Step64 physical radial P''' full-center ODE-integrating-factor certificate."""
from fractions import Fraction as F
import sympy as sp
import pytest
from numerics import hr_step64_center_third_jet as a
from numerics import hr_step62_original_interval_ad as upstream

@pytest.fixture(scope='module')
def global_result():return a.full_radius_Pthird(256)

@pytest.fixture(scope='module')
def old_interior():return upstream.certify_radial_jet_bounds(256)


def test_four_exact_original_source_blob_gates():
    assert a.verify_original_blobs()==upstream.EXPECTED
    assert len(upstream.EXPECTED)==4


def test_uniform_U_hull_contains_every_moving_step55_tube():
    c=a.uniform_center_input(16)
    u=c['uniform_U']
    for i in range(257):
        s=a.I.c(a.SMAX*i/256)
        moving=a._tube_at_s(s)
        assert u.lo<=moving.lo and u.hi>=moving.hi


def test_uniform_geometry_aware_G_s_bound_positive_and_finite(global_result):
    g=global_result['uniform_Gs']
    assert F('0.0033')<F(g.lo,a.original.S)<F(g.hi,a.original.S)<F('0.0044')
    assert global_result['A_max']==F(g.hi,a.original.S)
    assert 0<global_result['Uprime_max']<F('0.00351')


def test_regular_singular_integrating_factor_manufactured_exact():
    s,u0,A=sp.symbols('s u0 A',positive=True)
    U=u0+A*s/5
    # This is an independent exact check of 2s (U-U0)' + 3(U-U0) = s*A,
    # not a substitute for the authentic physical G.
    assert sp.simplify(2*s*sp.diff(U,s)+3*(U-u0)-s*A)==0
    assert sp.simplify((U-u0)/s-A/5)==0
    assert sp.diff(U,s)==A/5


def test_regular_singular_uniform_bound_formula(global_result):
    B=global_result['A_max']
    assert global_result['W_over_s_max']==B/5
    assert global_result['Uprime_max']==4*B/5
    assert B>0


def test_step55_original_center_compatibility_at_two_values():
    # Interval confirmation of the independently derived original Step55
    # exact identity G(0,U)=3U0-U. Not offered as an independent symbolic proof.
    o=upstream.original
    s=upstream.I.c(0)
    for du in [F(0),F('0.0001'),F('-0.0001')]:
        u=o.U0+upstream.I.c(du)
        g=o.G(s,u)
        expected=3*o.U0-u
        assert g.lo<=expected.hi and g.hi>=expected.lo
        assert F(g.hi-g.lo,o.S)<F('1e-18')


def test_Pthird_first_cell_contains_center_zero_and_is_bounded(global_result):
    low,high=global_result['Pthird_first_cell']
    assert low<=0<=high<F('0.001646')
    assert global_result['first_cell_includes_center']


def test_full_original_radial_Pthird_strict_bound_including_center(global_result):
    lo,hi=global_result['Pthird_full']
    assert F('-.000252')<lo<0<hi<F('.025729')
    assert global_result['last_cell_includes_smax']


def test_full_radius_bound_subset_of_previous_interior_bound(global_result,old_interior):
    lo,hi=global_result['Pthird_full']
    prior_lo,prior_hi=old_interior['P_third_interior']
    assert prior_lo<lo<hi<prior_hi


def test_do_not_use_moving_tube_for_mean_value_cross_s():
    low=a._tube_at_s(a.I.c(0))
    high=a._tube_at_s(a.I.c(a.SMAX))
    # U(smax) is not enclosed by the tiny moving U(0) tube.
    assert high.hi>low.hi
    whole=a.uniform_center_input(8)['uniform_U']
    assert whole.hi>=high.hi and whole.lo<=low.lo


def test_invalid_partition_rejected():
    with pytest.raises(ValueError):a.uniform_center_input(7)
    with pytest.raises(ValueError):a.uniform_center_input(8193)


def test_manifest_truthful_dirac_status():
    x=a.manifest(8)
    assert x['GATE_2B']=='OPEN'
    assert x['lapse_rank']=='NOT_COMPUTED'
    assert x['JANUS_R']=='NOT_VALIDATED'
    assert len(x['Pthird_full'])==2
