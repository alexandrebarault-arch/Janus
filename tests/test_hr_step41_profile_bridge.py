"""Step41 exact coefficient-box logic and corrected-profile targeted gates."""
from fractions import Fraction as F
import math
import json
import pytest
from numerics.hr_step41_profile_bridge import (
    BALL,RMAX,coefficient_membership,certified_step41_profile)

@pytest.fixture(scope='module')
def result():return certified_step41_profile()

def test_actual_highorder_f_delta_enters_exact_interval_ball(result):
    p=result['membership']
    assert p['inside_closed_ball'] and p['all_odd_exact_zero']
    assert p['max_abs_even_float']<.0016<.005
    assert F(p['strict_margin_exact'])>F('.0034')

def test_all_five_actual_coefficients_persisted_and_reproducible(result):
    c=result['membership']['coefficients_float']
    assert len(c)==9
    assert c[2]==pytest.approx(.0015479757723131573,abs=1e-12)
    assert all(c[i]==0 for i in (1,3,5,7))
    assert len(result['coefficient_sha256'])==64

def test_actual_profile_dust_interval_transfer_is_not_sampling(result):
    d=result['continuous_dust_certificate']
    assert d['ncells']==256
    assert F(d['strict_pg_over_r2_lower'])>F('0.885')
    assert F(d['strict_pf_over_r2_lower'])>F('0.039')
    assert result['actual_profile_continuum_positive_two_dust']

def test_chart_box_proof_and_center_domain_guard(result):
    c=result['continuous_spatial_chart_certificate']
    assert F(c['J_uniform_lower_exact'])>F('0.5')
    assert F(c['K_div_r2_uniform_lower_exact'])>0
    assert RMAX==F('.85')

def test_independent_off_fit_dense_local_residual_stays_small(result):
    r=result['dense_sample_diagnostics']
    assert r['radii']==73 and r['r_max']==.85
    assert r['max_abs_local_C']<2e-10
    assert r['max_abs_primary']<1e-12
    assert r['sampled_min_pg_over_r2']>.8
    assert r['sampled_min_pf_over_r2']>.1

def test_binary64_membership_is_exactly_rational():
    x=[0.,0.,.001,0.,0.,0.,0.,0.,0.]
    z=coefficient_membership(x)
    assert F(z['strict_margin_exact'])==BALL-F.from_float(.001)

def test_fail_closed_on_nonzero_odd_generator():
    with pytest.raises(ValueError,match='odd'):
        coefficient_membership([0.,.000001,0.,0.,0.,0.,0.,0.,0.])

def test_fail_closed_on_out_of_ball_correction():
    with pytest.raises(ArithmeticError,match='exits'):
        coefficient_membership([0.,0.,.0050001,0.,0.,0.,0.,0.,0.])

def test_invalid_membership_shapes_nonfinite_and_limits():
    for x in ([0.], [0.]*8+[float('nan')], [0.]*8+[float('inf')]):
        with pytest.raises(ValueError):coefficient_membership(x)
    with pytest.raises(ValueError):coefficient_membership([0.]*9,0)

def test_binary64_boundary_is_rejected_if_above_exact_decimal_limit():
    # float(.005) is slightly ABOVE the exact rational 1/200.
    x=[.005,0.,-.005,0.,0.,0.,0.,0.,0.]
    with pytest.raises(ArithmeticError):coefficient_membership(x)
    safer=math.nextafter(.005,0.)
    assert coefficient_membership([safer,0.,-safer,0.,0.,0.,0.,0.,0.])['inside_closed_ball']

def test_no_ghost_freedom_claim_in_manifest(result):
    assert result['secondary_exact_zero']=='NOT_PROVED'
    assert result['Dirac_time_preservation']=='NOT_DERIVED'
    assert result['lapse_fixing']=='NOT_DERIVED'
    assert result['GATE_2B']=='OPEN' and result['JANUS_R']=='NOT_VALIDATED'
