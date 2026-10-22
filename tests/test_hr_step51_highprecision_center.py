"""Step51 checks: original two historical providers, 80/120-digit U1 estimates.

These are precision/stability checks, NEVER rigorous interval certificates.
"""
import pytest
from numerics.hr_step51_highprecision_center_coefficient import (
    GIT_BLOBS,verify_historical_providers,calculation,richardson_u1_at_decade)


def test_two_real_original_symbolic_providers_byte_for_byte():
    assert verify_historical_providers()==GIT_BLOBS


def test_fail_closed_if_original_source_hash_is_wrong(monkeypatch):
    import numerics.hr_step51_highprecision_center_coefficient as s
    corrupted=dict(GIT_BLOBS)
    corrupted['numerics/hr_step46_exact_secondary_ode.py']='0'*40
    monkeypatch.setattr(s,'GIT_BLOBS',corrupted)
    with pytest.raises(ValueError,match='historical source mismatch'):
        s.verify_historical_providers()


def test_high_precision_coefficient_consistent_with_old_low_precision():
    s=richardson_u1_at_decade(7,90)
    v=float(s['u1_extrapolated_unenclosed'])
    from decimal import Decimal
    assert Decimal("0.0007897451667202464909324") < Decimal(s["u1_extrapolated_unenclosed"]) < Decimal("0.0007897451667202464909326")
    assert abs(v-float(s['historical_step49_double_estimate']))<2e-13


def test_two_radius_decade_refinements_stable_but_not_proved():
    a=richardson_u1_at_decade(7,110)
    b=richardson_u1_at_decade(9,110)
    # cancellation of O(r²) gives O(r^4) asymptotic *estimate*, no enclosure
    from decimal import Decimal
    assert abs(Decimal(a['u1_extrapolated_unenclosed'])-Decimal(b['u1_extrapolated_unenclosed']))<Decimal('2e-30')
    assert a['scientific_status']=='HIGH_PRECISION_NUMERICAL_ONLY, NOT PROVED/CERTIFIED'


def test_80_vs_120_decimal_precision_same_small_radius_value():
    from decimal import Decimal
    a=richardson_u1_at_decade(9,80)
    b=richardson_u1_at_decade(9,120)
    assert abs(Decimal(a['u1_extrapolated_unenclosed'])-Decimal(b['u1_extrapolated_unenclosed']))<Decimal('1e-40')


def test_never_promote_U1_numeric_to_global_constraint_result():
    s=richardson_u1_at_decade()
    assert s['GATE_2B']=='OPEN' and s['JANUS_R']=='NOT_VALIDATED'
    assert s['global_secondary']=='OPEN'
    assert s['Dirac_time_preservation']=='NOT_COMPUTED'


def test_requested_precision_and_radius_guards():
    with pytest.raises(ValueError):richardson_u1_at_decade(2)
    with pytest.raises(ValueError):richardson_u1_at_decade(20)
    with pytest.raises(ValueError):richardson_u1_at_decade(8,20)
    with pytest.raises(ValueError):calculation(20)
