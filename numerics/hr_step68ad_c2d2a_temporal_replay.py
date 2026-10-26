"""Center-safe seven-cell replay of the ORIGINAL Step58 temporal operator.

This module changes neither the original Step68o nor the original Step58/60.
All physical claims are conditional on the pinned reports verified by C2b.
An enclosure overlapping zero is INCOMPLETE, never a physical sign claim.

The run requires a complete checkout of the research branch. It must never
be represented as an executed Step58/60 certificate until actually run.
"""
from __future__ import annotations

from contextlib import contextmanager
from fractions import Fraction as F
from hashlib import sha1
from pathlib import Path
from unittest.mock import patch
import json
from .hr_step68ad_c2d2b_guard import assert_guard_binding, summarize_temporal_signs

PINNED = {
    "hr_step58_temporal_operator.py": "802c23aebd41780d8c462f1aa1711707fe4ee88f",
    "hr_step60_full_constraint_prolongation.py": "9693f0dbbea7e08b4c1a0a89a9b4617f4b6a9509",
    "hr_step68o_temporal_interval_annulus.py": "c99caebc17f243784450ddff94fb061767e6d8e7",
    "hr_step68n_interval_ode_jets.py": "96370e0599748c6dc07faf339ab3646ae3474e7d",
    "hr_step55_global_barrier.py": "a6e7004120d0a166a3a8973c2fbe1487a8eb70fe",
    "hr_step68ad_c2b_center_boxes.py": "94928e285f7e04deaf546abbeb9d3f05db33b213",
}


def git_blob(raw: bytes) -> str:
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def verify_original_files(folder: Path) -> dict[str, str]:
    result = {}
    for name, expected in PINNED.items():
        raw = (Path(folder) / name).read_bytes()
        actual = git_blob(raw)
        if actual != expected:
            raise ValueError(f"Source drift: {name}: expected {expected}, found {actual}")
        result[name] = actual
    return result


def outward_interval(pair, I):
    """Convert exact rational endpoints into the original outward integer lattice.

    I.hull performs floor(lower*10**28) and ceil(upper*10**28).
    Both endpoints are kept as exact Fractions until that operation.
    """
    if len(pair) != 2:
        raise ValueError("Expected two rational bounds")
    lo, hi = F(pair[0]), F(pair[1])
    if lo > hi:
        raise ValueError("Reversed physical interval")
    value = I.hull(lo, hi)
    if value.lo > value.hi:
        raise AssertionError("Invalid outward interval")
    return value


def box_for_rounded_s(reports, si, original_box, Q, validate_reports):
    """Re-enclose U on the ACTUAL rounded interval used by Step68o.

    Crucial: Step68o constructs R=I.hull(rlo,rhi), si=R**2. For rational
    edges with a factor 7, the lattice widens R and then si. Feeding the
    unexpanded C2b box would not be a formally valid interval proof.
    """
    if not (0 <= si.lo <= si.hi <= 10**28 // 1024):
        raise ValueError("Rounded s domain escapes the certified center chart")
    u0,u1,u2,us,uss,usss = validate_reports(reports)
    s = Q(F(si.lo,10**28),F(si.hi,10**28))
    k=F(1,10**7)
    star=u0+u1*s+u2*s**2
    err=Q(-k*s.hi**3,k*s.hi**3)
    candidate=star+err
    monotone=Q(u0.lo+us.lo*s.lo,u0.hi+us.hi*s.hi)
    U=Q(max(candidate.lo,monotone.lo),min(candidate.hi,monotone.hi))
    if U.lo>U.hi:
        raise ArithmeticError("Inconsistent center enclosures after outward rounding")
    return {"r":original_box["r"], "s":s.pair(),
            "U":U.pair(), "U_s":us.pair(), "U_ss":uss.pair(),
            "U_sss":usss.pair(),"outward_s_lattice_guard":True}


def validated_s_jet(box, Jet, I):
    """s-jet: U, U_s, U_ss/2, U_sss/6, NOT a radial jet."""
    coeff = [outward_interval(box[key], I) for key in ("U", "U_s", "U_ss", "U_sss")]
    return Jet([coeff[0], coeff[1], coeff[2] / 2, coeff[3] / 6])


@contextmanager
def inject_s_jet(original_annulus, box, Jet, I, expected_s):
    """Scoped, checked replacement of only Step68o's singular ODE jet.

    Original canonical reconstruction and original non-frozen Step58 Cdot
    are called unmodified. The injected coefficient intervals enclose the
    physical derivatives on the WHOLE closed cell, not just at its midpoint.
    """
    used = []
    def replacement(si):
        if si.lo != expected_s.lo or si.hi != expected_s.hi:
            raise AssertionError("Unexpected radial cell in Step68o replay")
        used.append(True)
        return validated_s_jet(box, Jet, I)
    with patch.object(original_annulus, "_ode_coeff", replacement):
        yield used
    if len(used) != 1:
        raise AssertionError(f"Expected one original canonical replay; got {len(used)}")


def classify_sign(iv):
    if iv.lo > 0:
        return "POSITIVE_CERTIFIED"
    if iv.hi < 0:
        return "NEGATIVE_CERTIFIED"
    return "INCOMPLETE"


def evaluate_original_step58(box, annulus, Jet, I):
    lo, hi = map(F, box["r"])
    if not (F(0) < lo < hi <= F(1, 32)):
        raise ValueError("Only seven positive center cells are supported")
    expected_s = I.hull(lo, hi) ** 2
    assert_guard_binding(box, expected_s)
    with inject_s_jet(annulus, box, Jet, I, expected_s):
        coeff = annulus.evaluate_cell(lo, hi)
    return {label: {"enclosure": [str(F(v.lo, 10**28)), str(F(v.hi, 10**28))],
                    "sign": classify_sign(v)} for label, v in coeff.items()}


def run(repo: Path):
    """Execute ONLY with all original files and pinned reports on disk."""
    repo = Path(repo).resolve()
    verified = verify_original_files(repo / "numerics")
    from numerics.hr_step68ad_c2b_center_boxes import load_pinned, certify_cells, Q, validate_reports
    from numerics.hr_step68n_interval_ode_jets import Jet, I
    from numerics import hr_step68o_temporal_interval_annulus as annulus
    reports = load_pinned(repo / "research" / "reports")
    boxes = certify_cells(reports)
    if boxes["cell_count"] != 7 or boxes["closed_radius_domain"] != ["1/64", "1/32"]:
        raise AssertionError("Unexpected physical domain or incomplete seven-cell cover")
    rows = []
    for box in boxes["cells"]:
        lo,hi=map(F,box["r"])
        rounded_s=I.hull(lo,hi)**2
        guarded=box_for_rounded_s(reports,rounded_s,box,Q,validate_reports)
        rows.append({"r": box["r"], "outward_s":guarded["s"],
                     "temporal": evaluate_original_step58(guarded, annulus, Jet, I)})
    assert len(rows) == 7
    sign_summary = summarize_temporal_signs(rows)
    return {"step": "68ad-C2d2a", "kind": "EXECUTED_ORIGINAL_STEP58_NONFROZEN_SHIFT",
            "provenance": verified, "input_report_blobs": boxes["pinned_original_report_git_blobs"],
            "cells": rows,
            "seven_temporal_signs_certified": sign_summary["all_nonzero_signs_certified"],
            "temporal_sign_pattern_audit": sign_summary,
            "Step60_quotient": "NOT_EVALUATED",
            "GATE_2B": "OPEN", "JANUS_R": "NOT_VALIDATED"}


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.repo)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"cells": len(result["cells"]),
                      "certified": result["seven_temporal_signs_certified"],
                      "out": str(args.out)}))

if __name__ == "__main__":
    main()
