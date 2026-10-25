"""Rigorous cubic center comparison barrier, conditional on exact original U0–U3 recurrence."""
from fractions import Fraction as F
import pytest
from numerics.hr_step68u_cubic_center_barrier import third_derivative_certificate,KAPPA,STEP67B_U3_LO,STEP67B_U3_HI


def test_published_original_center_U3_strictly_inside_cubic_barrier():
    assert -KAPPA<STEP67B_U3_LO<STEP67B_U3_HI<KAPPA


def test_full_original_G_outward_interval_third_derivative_signs():
    d=third_derivative_certificate()
    assert F(d['upper_F_third_over_6_interval'][1])<0
    assert F(d['lower_F_third_over_6_interval'][0])>0
    assert d['s_range']==['0','1/1024']
    assert len(d['original_source_sha'])==4


def test_tighter_subdomain_preserves_signs():
    q=third_derivative_certificate(F(1,4096))
    assert F(q['upper_F_third_over_6_interval'][1])<0
    assert F(q['lower_F_third_over_6_interval'][0])>0


def test_too_narrow_barrier_fails_closed():
    with pytest.raises(ArithmeticError):third_derivative_certificate(kappa=F(1,100_000_000))


def test_domain_rejected_not_silently_extended():
    with pytest.raises(ValueError):third_derivative_certificate(smax=F(1,1000))
    with pytest.raises(ValueError):third_derivative_certificate(smax=0)


def test_no_temporal_rank_claim():
    m=third_derivative_certificate()
    assert m['temporal_A_N_A_M_near_center']=='NOT_YET_CERTIFIED'
    assert m['Dirac_rank']=='NOT_COMPUTED' and m['JANUS_R']=='NOT_VALIDATED'
