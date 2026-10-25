"""Original G center cubic comparison + global radial U_s positive proof."""
from fractions import Fraction as F
import pytest
from numerics.hr_step68v_global_monotone_U import certificate,MAX_S,KAPPA,authentic


def test_four_originals_and_two_pinned_previous_theorems():
    assert len(authentic())==4


def test_cubic_barrier_signs_strict_on_full_center_r_le_one_eighth():
    a=certificate()
    assert F(a['Fplus_third_over6'][1])<0<F(a['Fminus_third_over6'][0])
    assert a['center_s_range']==['0','1/64']


def test_mean_value_G_U_ODE_slope_enclosure_is_positive():
    a=certificate()
    assert F(a['U_s_center_lower_rational'])>0
    assert F(a['U_s_center_upper_rational'])>F(a['U_s_center_lower_rational'])
    assert a['U_s_strict_positive_inner'] is True


def test_joining_at_one_eighth_to_step68m_exact_coverage():
    a=certificate()
    assert a['outer_proof_step68m_domain'].startswith('s in [1/64,289/400]')
    assert a['new_full_radius_radial_U_monotonicity'].startswith('U_s>0')


def test_reject_unsupported_domain_or_width():
    with pytest.raises(ValueError):certificate(F(1,32))
    with pytest.raises(ValueError):certificate(kappa=F(1,100000000))


def test_refuse_temporal_rank_claim():
    a=certificate()
    assert a['time_coefficient_A_N_A_M_at_r0']=='NOT_CERTIFIED'
    assert a['JANUS_R']=='NOT_VALIDATED'
