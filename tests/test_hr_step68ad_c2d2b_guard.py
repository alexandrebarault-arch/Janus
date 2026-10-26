"""Guard tests only: NO execution of the original Step58/60 physics."""
from fractions import Fraction as F
from types import SimpleNamespace
import pytest
from numerics.hr_step68ad_c2d2b_guard import assert_guard_binding, summarize_temporal_signs, SCALE


def fixture_box():
    lo, hi = F(1, 64), F(1, 56)
    a = lo*lo
    b = hi*hi
    cell = SimpleNamespace(lo=a.numerator*SCALE//a.denominator,
                           hi=-((-b.numerator*SCALE)//b.denominator))
    box = {"s": [str(F(cell.lo, SCALE)), str(F(cell.hi, SCALE))],
           "outward_s_lattice_guard": True,
           "U": ["-1/4", "-1/5"], "U_s": ["1/1000", "2/1000"],
           "U_ss": ["-1/100", "-1/200"],
           "U_sss": ["-1/1000", "-1/2000"]}
    return box, cell


def rows(N="POSITIVE_CERTIFIED", M="NEGATIVE_CERTIFIED"):
    return [{"temporal": {"N": {"sign": N}, "M": {"sign": M}}} for _ in range(7)]


def test_matching_guard_passes():
    b, cell = fixture_box()
    assert assert_guard_binding(b, cell)


def test_guard_missing_fails_closed():
    b, cell = fixture_box()
    del b["outward_s_lattice_guard"]
    with pytest.raises(ValueError, match="Missing outward"):
        assert_guard_binding(b, cell)


def test_stale_cell_rejected_even_when_jet_bounds_present():
    b, cell = fixture_box()
    cell.hi += 1
    with pytest.raises(ValueError, match="does not match"):
        assert_guard_binding(b, cell)


def test_missing_s_rejected():
    b, cell = fixture_box()
    del b["s"]
    with pytest.raises(ValueError, match="Missing or malformed"):
        assert_guard_binding(b, cell)


def test_reversed_derivative_rejected():
    b, cell = fixture_box()
    b["U_ss"] = ["-1/200", "-1/100"]
    with pytest.raises(ValueError, match="Reversed derivative"):
        assert_guard_binding(b, cell)


def test_bad_derivative_fraction_rejected():
    b, cell = fixture_box()
    b["U"] = ["NaN", "1"]
    with pytest.raises(ValueError, match="Non-rational derivative"):
        assert_guard_binding(b, cell)


def test_historical_pattern_reported_separately():
    out = summarize_temporal_signs(rows())
    assert out["all_nonzero_signs_certified"]
    assert out["all_expected_N_positive_M_negative"]
    assert out["incomplete_coefficients"] == []


def test_opposite_nonzero_signs_are_not_misreported_as_historical_pattern():
    out = summarize_temporal_signs(rows("NEGATIVE_CERTIFIED", "POSITIVE_CERTIFIED"))
    assert out["all_nonzero_signs_certified"]
    assert not out["all_expected_N_positive_M_negative"]
    assert len(out["opposite_to_historical_pattern"]) == 14


def test_zero_crossing_keeps_incomplete():
    out = summarize_temporal_signs(rows("INCOMPLETE", "NEGATIVE_CERTIFIED"))
    assert not out["all_nonzero_signs_certified"]
    assert not out["all_expected_N_positive_M_negative"]
    assert len(out["incomplete_coefficients"]) == 7


def test_missing_operator_label_rejected():
    a = rows()
    del a[0]["temporal"]["M"]
    with pytest.raises(ValueError, match="Incomplete temporal"):
        summarize_temporal_signs(a)


def test_incorrect_cell_count_rejected():
    with pytest.raises(ValueError, match="seven"):
        summarize_temporal_signs(rows()[:6])


def test_unrecognized_sign_rejected():
    with pytest.raises(ValueError, match="Invalid temporal sign"):
        summarize_temporal_signs(rows("POSSIBLE", "NEGATIVE_CERTIFIED"))
