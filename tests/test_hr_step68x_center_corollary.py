"""Regression checks for exact central spatial ODE corollary Step68x."""
from pathlib import Path
from fractions import Fraction as F
import pytest
from numerics.hr_step68x_normalized_center_ode_envelope import coefficient, tube_at_s, manifest

ROOT = Path(__file__).resolve().parents[1]/'research'/'reports'


def test_authentic_original_bound_loaded():
    c = coefficient(ROOT)
    assert c == F(551901551914723209073991119,1600000000000000000000000000000000)


def test_very_small_radius_cubic_bound():
    m=manifest(ROOT)
    x=m['at_r_1_over_32']
    assert F(x['U_minus_Ustar_absolute'])==F(1,10737418240000000)
    assert F(x['U_s_minus_Ustar_s_absolute'])<F(1,10**12)


def test_full_inner_chart_stronger_than_old_constant():
    m=manifest(ROOT)
    assert F(m['at_r_1_over_8']['spatial_shrink_factor_vs_1e_minus_6'])==2621440
    assert m['temporal_A_N_A_M_signs_for_r_lt_1_over_32']=='NOT_COMPUTED'
    assert m['JANUS_R']=='NOT_VALIDATED'


@pytest.mark.parametrize('s', [-1,F(1,63)])
def test_invalid_central_radius(s):
    with pytest.raises(ValueError):
        tube_at_s(s,F(1))
