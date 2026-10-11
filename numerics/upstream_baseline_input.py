from __future__ import annotations

from pathlib import Path
import numpy as np

UPSTREAM_BIMINPUT_FIELDS = (
    "gA", "gB", "gK", "gKD", "gDA", "gDB", "gSig",
    "fA", "fB", "fK", "fKD", "fDA", "fDB", "fSig",
    "q", "gAlp", "fAlp", "gDAlp", "p",
    "pfD", "pfS", "pftau",
)

PATCHED_COLUMN_COUNT = 26  # r + 25 patched input fields
UPSTREAM_COLUMN_COUNT = 23  # r + 22 upstream input fields


def patched_to_upstream_rows(rows: np.ndarray, *, atol: float = 0.0) -> np.ndarray:
    """Project patched zero-f initial rows onto the exact upstream input layout.

    The twin-fluid patch appends `pfFD,pfFS,pfFtau` after the original
    standard-3+1 `bimInput` fields.  Therefore a zero-f baseline must differ
    only by removal of these three trailing columns; all metric/gauge/g-fluid
    data stay bitwise identical before text serialization.
    """
    rows = np.asarray(rows, dtype=float)
    if rows.ndim != 2 or rows.shape[1] != PATCHED_COLUMN_COUNT:
        raise ValueError(f"rows must have {PATCHED_COLUMN_COUNT} columns")
    if not np.all(np.isfinite(rows)):
        raise ValueError("rows contain non-finite values")
    if atol < 0:
        raise ValueError("atol must be non-negative")
    twin = rows[:, -3:]
    if np.any(np.abs(twin) > atol):
        raise ValueError("twin-fluid state must be zero for upstream regression")
    return np.array(rows[:, :UPSTREAM_COLUMN_COUNT], copy=True)


def write_upstream_text_input(path: Path, patched_rows: np.ndarray, *, atol: float = 0.0) -> None:
    upstream = patched_to_upstream_rows(patched_rows, atol=atol)
    np.savetxt(Path(path), upstream, fmt="%.17g")
