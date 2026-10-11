from pathlib import Path
import pytest

from tools.compare_bim_solver_outputs import (
    compare_output_files,
    require_regression,
)


def _write(path: Path, fields, frames):
    lines = [f'{name} -> "{name}"' for name in fields]
    lines.append("*** DATA ***")
    for frame in frames:
        for row in frame:
            lines.append(" ".join(str(row[name]) for name in fields))
    path.write_text("\n".join(lines) + "\n")


def _frames(delta=0.0):
    out = []
    for t in (0.0, 0.01):
        frame = []
        for r in (-0.1, 0.1, 0.3, 0.5):
            frame.append({
                "t": t,
                "r": r,
                "gA": 1.0 + delta,
                "C_1": 1e-6,
                "pfD": 0.2,
                "pfFD": 0.0,
            })
        out.append(frame)
    return out


def test_comparator_uses_all_shared_fields_and_ignores_candidate_extras(tmp_path):
    ref = tmp_path / "ref.txt"
    cand = tmp_path / "cand.txt"
    _write(ref, ("t", "r", "gA", "C_1", "pfD"), _frames())
    _write(cand, ("t", "r", "gA", "C_1", "pfD", "pfFD"), _frames(delta=2e-8))

    c = compare_output_files(ref, cand, n_ghost=1)
    by_name = c.by_name()
    assert set(by_name) == {"C_1", "gA", "pfD"}
    assert abs(by_name["gA"].max_abs - 2e-8) < 1e-15
    assert by_name["C_1"].max_abs == 0.0
    assert c.worst_abs_field == "gA"


def test_regression_gate_accepts_roundoff_and_rejects_real_difference(tmp_path):
    ref = tmp_path / "ref.txt"
    tiny = tmp_path / "tiny.txt"
    bad = tmp_path / "bad.txt"
    _write(ref, ("t", "r", "gA", "C_1", "pfD"), _frames())
    _write(tiny, ("t", "r", "gA", "C_1", "pfD", "pfFD"), _frames(delta=1e-13))
    _write(bad, ("t", "r", "gA", "C_1", "pfD", "pfFD"), _frames(delta=1e-4))

    require_regression(
        compare_output_files(ref, tiny, n_ghost=1),
        abs_tol=1e-12,
        rel_tol=1e-12,
    )
    with pytest.raises(AssertionError, match="gA"):
        require_regression(
            compare_output_files(ref, bad, n_ghost=1),
            abs_tol=1e-12,
            rel_tol=1e-12,
        )


def test_comparator_rejects_coordinate_or_time_mismatch(tmp_path):
    ref = tmp_path / "ref.txt"
    cand = tmp_path / "cand.txt"
    fields = ("t", "r", "gA", "C_1", "pfD")
    _write(ref, fields, _frames())
    shifted = _frames()
    shifted[1][1]["r"] = 0.1001
    _write(cand, fields, shifted)
    with pytest.raises(ValueError, match="radius-grid mismatch"):
        compare_output_files(ref, cand, n_ghost=1)
