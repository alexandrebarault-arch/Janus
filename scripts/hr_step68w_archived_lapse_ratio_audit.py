"""Independent exact-rational audit of archived Step68p/q/s temporal interval covers.

Does NOT recompute original Step58 enclosure or prove full Dirac rank.
Uses only Fraction, JSON and SHA-pinned source files (no SymPy or floats in proof).
"""
from __future__ import annotations
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

ARCHIVES = (
    ("p", "gate2b-step68p-adaptive-outer-cover.json", "1/8", "17/20", 265, "978d77d7dc8b30c3bdd78b25f1ca0d1c68900fe6"),
    ("q", "gate2b-step68q-inner-1over16-to-1over8-cover.json", "1/16", "1/8", 314, "82f5d046cd0ca0c342adabe8b8f13cfc3f99308d"),
    ("s", "gate2b-step68s-inner-1over32-to-1over16-cover.json", "1/32", "1/16", 1006, "e890998a2f925f881ab85b60a9027e5828e35ed5"),
)


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def check_covers(root: str | Path, archives=ARCHIVES) -> dict:
    root = Path(root)
    all_cells = []
    sources = []
    for tag, filename, start, end, count, expected_sha in archives:
        raw = (root / filename).read_bytes()
        actual_sha = git_blob(raw)
        if actual_sha != expected_sha:
            raise ValueError(f"Git blob authenticity failure: {filename}")
        doc = json.loads(raw)
        if (doc.get("status") != "CERTIFIED" or doc.get("queue") != []
                or doc.get("failures") != [] or doc.get("GATE_2B") != "OPEN"
                or doc.get("JANUS_R") != "NOT_VALIDATED"):
            raise ValueError(f"Unfinished or overclaimed cover: {filename}")
        if doc.get("coverage") != [start, end] or len(doc.get("certified", [])) != count:
            raise ValueError(f"Wrong cover extent or cell count: {filename}")
        cells = []
        for index, row in enumerate(doc["certified"]):
            lo, hi = F(row["lo"]), F(row["hi"])
            nl, nu = (F(x) for x in row["N"])
            ml, mu = (F(x) for x in row["M"])
            if not (F(0) < lo < hi and 0 < nl <= nu and ml <= mu < 0):
                raise ValueError(f"Invalid signed cell {filename}:{index}")
            cells.append((lo, hi, nl, nu, ml, mu, tag, index))
        cells.sort(key=lambda c: c[0])
        if cells[0][0] != F(start) or cells[-1][1] != F(end):
            raise ValueError(f"Missing cover endpoints: {filename}")
        if any(a[1] != b[0] for a, b in zip(cells, cells[1:])):
            raise ValueError(f"Gap or overlap in {filename}")
        all_cells.extend(cells)
        sources.append({"band": tag, "file": filename, "sha": actual_sha,
                        "cell_count": count, "processed": doc.get("processed")})
    all_cells.sort(key=lambda c: c[0])
    if all_cells[0][0] != F(1, 32) or all_cells[-1][1] != F(17, 20):
        raise ValueError("Incorrect global domain")
    if any(a[1] != b[0] for a, b in zip(all_cells, all_cells[1:])):
        raise ValueError("Gap or overlap at cross-band junction")
    extrema = {}
    for lo, hi, nl, nu, ml, mu, tag, index in all_cells:
        derived = {
            "ratio_low": nl / (-ml),
            "ratio_high": nu / (-mu),
            "A_N_per_r2_low": nl / hi**2,
            "A_N_per_r2_high": nu / lo**2,
            "A_M_per_r2_low": ml / lo**2,
            "A_M_per_r2_high": mu / hi**2,
        }
        for label, value in derived.items():
            minimize = label.endswith("_low")
            if (label not in extrema or (value < extrema[label][0] if minimize
                                        else value > extrema[label][0])):
                extrema[label] = (value, tag, lo, hi, index)
    # Publish only simple rational strict bounds that have been checked exactly.
    if not (F(1, 50000) < extrema["ratio_low"][0]
            and extrema["ratio_high"][0] < F(14)
            and F(7, 20) < extrema["A_N_per_r2_low"][0]
            and extrema["A_M_per_r2_high"][0] < -F(546)):
        raise ValueError("Published rational inequalities not established")
    return {
        "step": "68w", "status": "VERIFIED_ARCHIVED_INTERVAL_COVERS",
        "proof_scope": "Rational implications of existing SHA-pinned Step68p/q/s interval cells; no independent recalculation of Step58 dynamics",
        "cover": ["1/32", "17/20"], "number_of_cells": len(all_cells),
        "source_pins": sources,
        "extrema": {name: {"bound": str(x[0]), "source_band": x[1],
                             "radius_cell": [str(x[2]), str(x[3])],
                             "cell_index": x[4]}
                    for name, x in extrema.items()},
        "simple_exact_conclusions": {
            "ratio": "1/50000 < -A_N/A_M < 14",
            "A_N_normalized": "A_N/r^2 > 7/20",
            "A_M_normalized": "A_M/r^2 < -546",
            "temporal_single_row": "rank 1 pointwise on r in [1/32,17/20] if original algebraic lapse equation applies; NOT full Dirac rank",
        },
        "near_center_r_less_than_1_over_32": "NOT_CERTIFIED",
        "full_Dirac_rank": "NOT_COMPUTED",
        "GATE_2B": "OPEN", "JANUS_R": "NOT_VALIDATED",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python -m scripts.hr_step68w_archived_lapse_ratio_audit /path/to/research/reports", file=sys.stderr)
        return 2
    out = check_covers(sys.argv[1])
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
