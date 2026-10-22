"""Interval-sound pointwise nonzero C for the frozen Step41 correction."""
from fractions import Fraction as F
import pytest
from numerics.hr_step45_secondary_point_certificate import (
    FDELTA,IV,evaluate_expr,frozen_primary_at,certify_frozen_C)
from numerics.hr_step45_exact_physical_ward import exact_physical_ward

@pytest.mark.parametrize('r,sign',[
    ('.11',1),('.21',-1),('.43',1),('.71',1),('.83',1),('.85',1)])
def test_actual_frozen_profile_exact_C_excludes_zero(r,sign):
    z=certify_frozen_C(F(r))
    assert z['verdict']==('STRICTLY_POSITIVE_CERTIFIED' if sign>0 else 'STRICTLY_NEGATIVE_CERTIFIED')
    assert sign*z['C_lower_float']>0 if sign>0 else sign*z['C_upper_float']>0
    assert abs(z['C_lower_float']-z['C_upper_float'])<1e-30


def test_actual_endpoint_strictly_nonzero_not_just_a_float():
    z=certify_frozen_C(F('.85'))
    assert F(z['C_interval_lower_exact'])>F('6.55e-11')
    assert F(z['C_interval_upper_exact'])<F('6.56e-11')
    assert z['GATE_2B']=='OPEN' and z['JANUS_R']=='NOT_VALIDATED'


def test_original_g_shift_primary_Fz_contains_zero_at_endpoint():
    th=exact_physical_ward()
    val=evaluate_expr(th['Fz'],frozen_primary_at(F('.85')))
    assert val.lo<=0<=val.hi
    assert val.hi-val.lo<F('1e-50')


def test_immutable_frozen_coefficients_have_odd_parity_and_small_amplitude():
    assert len(FDELTA)==9
    assert all(FDELTA[i]==0 for i in (1,3,5,7))
    assert max(abs(FDELTA[i]) for i in (0,2,4,6,8))<F('1/200')


def test_rational_interval_sqrt_and_cross_zero_gates():
    z=IV.p(2).sqrt()
    assert z.lo*z.lo<=2<=z.hi*z.hi
    with pytest.raises(ZeroDivisionError):IV(F(-1),F(2)).inv()
    with pytest.raises(ValueError):IV.p(-1).sqrt()


def test_radii_chart_validity_rejected():
    with pytest.raises(ValueError):frozen_primary_at(F(0))
    with pytest.raises(ValueError):frozen_primary_at(F('0.9'))


def test_real_C_nonzero_does_not_refute_a_different_exact_profile():
    s=certify_frozen_C(F('.85'))
    assert 'frozen' in s['physical_inference']
    assert 'does not rule out' in s['physical_inference']
