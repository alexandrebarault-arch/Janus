"""Exact arithmetic tests of Step68ad-C2c denominator lemma."""
from fractions import Fraction as F
import pytest
from numerics.hr_step68ad_c2c_shift_chart import (
    A, B, B2, B3, CG, CF, KF, M2, MG, RMAX, SMAX, Y, Z1,
    q, center_shift_chart, authenticate_sources,
)

U0HI = F('-26262134483803675020732891/5000000000000000000000000000')
USHI = F('7897452509337401302640553/10000000000000000000000000000')


def proof():
    return center_shift_chart(U0HI, USHI)


def test_u_negativity():
    assert U0HI + USHI * SMAX < 0


def test_ratio_y():
    d = proof()
    assert F(1, 2) < F(d['y_lower']) <= F(d['y_upper']) == Y


def test_quadratic_positive_and_increasing():
    d = proof()
    assert 2 * B2 + B3 > 0
    assert 0 < F(d['q_lower']) <= F(d['q_upper'])
    assert F(d['q_lower']) == q(F(d['y_lower']))


def test_K_bounds_and_chart():
    d = proof()
    lo, hi = F(d['K_over_r2_lower']), F(d['K_over_r2_upper'])
    assert 0 < lo < hi
    assert lo > F('0.2338')
    assert hi < F('0.234')


def test_original_K_at_three_radii():
    d = proof()
    lo, hi = F(d['K_over_r2_lower']), F(d['K_over_r2_upper'])
    for r in (F(1, 64), F(1, 48), RMAX):
        s = r * r
        lg = A * (1 + CG * s) ** 2
        lf = B * (1 + CF * s) ** 2
        K = M2 * MG * lg * lf * (lg ** 2 + 2 * B2 * lg * lf + B3 * lf ** 2) * r ** 2
        assert lo * r * r <= K <= hi * r * r


def test_stationary_shift_bound():
    d = proof()
    assert F(d['z_absolute_upper']) == F(1, 8000)
    assert F(d['r2_ZD_lower']) > F('4.276')
    assert F(d['r2_ZD_upper']) < F('4.277')
    assert F(d['r2_ZK_absolute_upper']) < F('0.000535')


def test_shift_ZD_pointwise_exact_fraction_squared():
    # Avoid irrational sqrt: square positive rational inequalities.
    d = proof()
    lo, hi = F(d['r2_ZD_lower']), F(d['r2_ZD_upper'])
    for r in (F(1, 64), F(1, 48), RMAX):
        s = r * r
        lg = A * (1 + CG * s) ** 2
        lf = B * (1 + CF * s) ** 2
        Kr2 = M2 * MG * lg ** 3 * lf * q(lf / lg)
        base = 1 - (Z1 * r) ** 2
        assert lo ** 2 <= base ** 3 / Kr2 ** 2 <= hi ** 2


def test_f_dust_denominator_sign():
    assert KF < 0 and 1 + 5 * CF * SMAX > 0
    assert proof()['f_dust_denominator_lower'] == '1'


def test_center_K_zero_and_no_false_regular_ZD():
    d = proof()
    assert d['K_center'] == '0'
    assert d['unscaled_ZD_at_center'] == 'SINGULAR_IN_RAW_FORMULA'
    assert d['seven_temporal_signs'] == 'PENDING'


def test_bad_input_rejected():
    with pytest.raises(ValueError):
        center_shift_chart(F(1), USHI)
    with pytest.raises(ValueError):
        center_shift_chart(U0HI, F(100))
    with pytest.raises(ValueError):
        center_shift_chart(U0HI, F(-1))


def test_authentication_rejects_missing_sources(tmp_path):
    with pytest.raises(FileNotFoundError):
        authenticate_sources(tmp_path)


def test_report_is_exact_rational_not_float():
    d = proof()
    assert all('/' in d[k] for k in ('y_lower', 'q_lower', 'K_over_r2_lower', 'r2_ZD_lower'))
    assert d['GATE_2B'] == 'OPEN' and d['JANUS_R'] == 'NOT_VALIDATED'
