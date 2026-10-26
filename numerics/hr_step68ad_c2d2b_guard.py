"""Fail-closed binding and certificate verification for the seven-cell Step58 replay.

This is NOT a physical Step58/Step60 evaluation. The sign metadata is never
accepted as evidence without a matching, exact-rational interval enclosure.
"""
from fractions import Fraction as F

SCALE = 10**28
EXPECTED_SIGNS = {"N": "POSITIVE_CERTIFIED", "M": "NEGATIVE_CERTIFIED"}
VALID_SIGNS = {"POSITIVE_CERTIFIED", "NEGATIVE_CERTIFIED", "INCOMPLETE"}


def _rational_pair(raw, context):
    if not isinstance(raw, (list, tuple)) or len(raw) != 2:
        raise ValueError(f"Missing or malformed interval: {context}")
    try:
        lo, hi = F(raw[0]), F(raw[1])
    except (ValueError, TypeError, ZeroDivisionError) as exc:
        raise ValueError(f"Non-rational interval: {context}") from exc
    if lo > hi:
        raise ValueError(f"Reversed interval: {context}")
    return lo, hi


def assert_guard_binding(box, expected_s):
    """Reject stale/unverified domain binding before injecting physical jets."""
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


def _classify_enclosure(enclosure, context):
    lo, hi = _rational_pair(enclosure, context)
    if lo > 0:
        return "POSITIVE_CERTIFIED"
    if hi < 0:
        return "NEGATIVE_CERTIFIED"
    return "INCOMPLETE"


def summarize_temporal_signs(rows):
    """Validate the entire seven-cell cover and independently verify all 14 signs.

    N/M are labels for the *coefficients* A_N/A_M of the lapse-zero-order
    temporal operator, NOT claims about the values/signs of lapses N/M.
    """
    if not isinstance(rows, list) or len(rows) != 7:
        raise ValueError("Expected exactly seven physical cells")
    incomplete, contrary = [], []
    previous_right = F(1, 64)
    for i, row in enumerate(rows):
        left, right = _rational_pair(row.get("r"), f"cell {i+1} radius")
        if left != previous_right or left == right or right > F(1, 32):
            raise ValueError(f"Seven-cell radius cover has a gap/overlap in cell {i+1}")
        previous_right = right
        temporal = row.get("temporal", {})
        if not isinstance(temporal, dict) or set(temporal) != set(EXPECTED_SIGNS):
            raise ValueError(f"Incomplete temporal operator labels in cell {i+1}")
        for label, expected in EXPECTED_SIGNS.items():
            entry = temporal[label]
            if not isinstance(entry, dict):
                raise ValueError(f"Malformed temporal entry in cell {i+1}/{label}")
            sign = entry.get("sign")
            if sign not in VALID_SIGNS:
                raise ValueError(f"Invalid temporal sign in cell {i+1}/{label}")
            computed = _classify_enclosure(entry.get("enclosure"), f"cell {i+1}/{label}")
            if sign != computed:
                raise ValueError(f"Sign/enclosure mismatch in cell {i+1}/{label}")
            if computed == "INCOMPLETE":
                incomplete.append(f"{i+1}/{label}")
            elif computed != expected:
                contrary.append(f"{i+1}/{label}")
    if previous_right != F(1, 32):
        raise ValueError("Seven-cell radius cover does not reach 1/32")
    all_nonzero = not incomplete
    expected_orientation = not incomplete and not contrary
    return {
        "all_nonzero_signs_certified": all_nonzero,
        "all_expected_N_positive_M_negative": expected_orientation,  # historical alias, labels are coefficients
        "all_expected_A_N_positive_A_M_negative": expected_orientation,
        "labels_are_lapse_coefficients_not_lapse_values": True,
        "incomplete_coefficients": incomplete,
        "opposite_to_historical_pattern": contrary,
        "exact_rational_enclosures_checked": 14,
        "radius_coverage_verified": ["1/64", "1/32"],
    }
