"""Fail-closed provenance binding for Step68ad-C2d2a temporal input boxes.

This is an interface-safety check, NOT an evaluation of physical Step58/60.
"""
from fractions import Fraction as F

SCALE = 10**28
EXPECTED_SIGNS = {"N": "POSITIVE_CERTIFIED", "M": "NEGATIVE_CERTIFIED"}
VALID_SIGNS = {"POSITIVE_CERTIFIED", "NEGATIVE_CERTIFIED", "INCOMPLETE"}


def assert_guard_binding(box, expected_s):
    """Reject a stale or unguarded box before its derivatives enter Step68o."""
    if box.get("outward_s_lattice_guard") is not True:
        raise ValueError("Missing outward-s lattice guard")
    raw = box.get("s")
    if not isinstance(raw, (list, tuple)) or len(raw) != 2:
        raise ValueError("Missing or malformed guarded s interval")
    try:
        endpoints = (F(raw[0]), F(raw[1]))
    except (ValueError, TypeError, ZeroDivisionError) as exc:
        raise ValueError("Non-rational guarded s interval") from exc
    expected = (F(expected_s.lo, SCALE), F(expected_s.hi, SCALE))
    if endpoints != expected:
        raise ValueError("Guarded s interval does not match actual Step68o lattice cell")
    if not (0 <= endpoints[0] <= endpoints[1] <= F(1, 1024)):
        raise ValueError("Guarded s interval outside certified center chart")
    for key in ("U", "U_s", "U_ss", "U_sss"):
        pair = box.get(key)
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ValueError(f"Missing derivative interval: {key}")
        try:
            lo, hi = F(pair[0]), F(pair[1])
        except (ValueError, TypeError, ZeroDivisionError) as exc:
            raise ValueError(f"Non-rational derivative interval: {key}") from exc
        if lo > hi:
            raise ValueError(f"Reversed derivative interval: {key}")
    return True


def summarize_temporal_signs(rows):
    """Distinguish a certified nonzero sign from the historical N+/M- pattern."""
    if len(rows) != 7:
        raise ValueError("Expected exactly seven physical cells")
    incomplete = []
    contrary = []
    for i, row in enumerate(rows):
        temporal = row.get("temporal", {})
        if set(temporal) != set(EXPECTED_SIGNS):
            raise ValueError(f"Incomplete temporal operator labels in cell {i+1}")
        for label, expected in EXPECTED_SIGNS.items():
            sign = temporal[label].get("sign")
            if sign not in VALID_SIGNS:
                raise ValueError(f"Invalid temporal sign in cell {i+1}/{label}")
            if sign == "INCOMPLETE":
                incomplete.append(f"{i+1}/{label}")
            elif sign != expected:
                contrary.append(f"{i+1}/{label}")
    return {
        "all_nonzero_signs_certified": not incomplete,
        "all_expected_N_positive_M_negative": not incomplete and not contrary,
        "incomplete_coefficients": incomplete,
        "opposite_to_historical_pattern": contrary,
    }
