import numpy as np
import pytest
from pathlib import Path

from numerics.upstream_baseline_input import (
    UPSTREAM_BIMINPUT_FIELDS,
    patched_to_upstream_rows,
    write_upstream_text_input,
)


def test_upstream_layout_is_patched_layout_without_twin_state():
    expected = (
        "gA", "gB", "gK", "gKD", "gDA", "gDB", "gSig",
        "fA", "fB", "fK", "fKD", "fDA", "fDB", "fSig",
        "q", "gAlp", "fAlp", "gDAlp", "p",
        "pfD", "pfS", "pftau",
    )
    assert UPSTREAM_BIMINPUT_FIELDS == expected


def test_zero_twin_rows_reduce_exactly_to_upstream_columns():
    rows = np.arange(2 * 26, dtype=float).reshape(2, 26)
    rows[:, -3:] = 0.0
    out = patched_to_upstream_rows(rows)
    assert out.shape == (2, 23)
    np.testing.assert_array_equal(out, rows[:, :23])


def test_nonzero_twin_state_is_rejected_for_upstream_regression():
    rows = np.zeros((2, 26), dtype=float)
    rows[:, 0] = [0.1, 0.2]
    rows[1, -3] = 1e-3
    with pytest.raises(ValueError, match="twin-fluid state must be zero"):
        patched_to_upstream_rows(rows)


def test_writer_emits_23_columns(tmp_path: Path):
    rows = np.zeros((3, 26), dtype=float)
    rows[:, 0] = [0.1, 0.2, 0.3]
    path = tmp_path / "baseline.dat"
    write_upstream_text_input(path, rows)
    loaded = np.loadtxt(path)
    assert loaded.shape == (3, 23)
