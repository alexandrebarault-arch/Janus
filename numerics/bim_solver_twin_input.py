from __future__ import annotations

from pathlib import Path
import numpy as np

PATCHED_BIMINPUT_FIELDS = (
    "gA", "gB", "gK", "gKD", "gDA", "gDB", "gSig",
    "fA", "fB", "fK", "fKD", "fDA", "fDB", "fSig",
    "q", "gAlp", "fAlp", "gDAlp", "p",
    "pfD", "pfS", "pftau",
    "pfFD", "pfFS", "pfFtau",
)


def uniform_centers(n: int, delta_r: float) -> np.ndarray:
    if n <= 0 or delta_r <= 0:
        raise ValueError("n and delta_r must be positive")
    return (np.arange(n, dtype=float) + 0.5) * float(delta_r)


def _vector(value, n: int, name: str) -> np.ndarray:
    arr = np.asarray(value, dtype=float)
    if arr.shape != (n,):
        raise ValueError(f"{name} must have shape ({n},), got {arr.shape}")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} contains non-finite values")
    return arr


def build_rows(r, psi_g, dpsi_g, psi_f, dpsi_f, Dg, Df, W) -> np.ndarray:
    r = np.asarray(r, dtype=float)
    if r.ndim != 1 or len(r) == 0 or not np.all(np.isfinite(r)) or np.any(r <= 0):
        raise ValueError("r must be a positive finite 1D array")
    n = len(r)
    pg = _vector(psi_g, n, "psi_g")
    dpg = _vector(dpsi_g, n, "dpsi_g")
    pf = _vector(psi_f, n, "psi_f")
    dpf = _vector(dpsi_f, n, "dpsi_f")
    dg = _vector(Dg, n, "Dg")
    df = _vector(Df, n, "Df")
    w = _vector(W, n, "W")
    if np.any(pg <= 0) or np.any(pf <= 0):
        raise ValueError("conformal factors must be positive")
    if np.any(w <= 0):
        raise ValueError("same-oriented lapse ratio W must be positive")

    zero = np.zeros(n)
    one = np.ones(n)
    gA = pg**2
    fA = pf**2
    gD = 2.0 * dpg / pg
    fD = 2.0 * dpf / pf

    # Column order: r, followed exactly by patched fld::bimInput.
    columns = (
        r,
        gA, gA, zero, zero, gD, gD, zero,
        fA, fA, zero, zero, fD, fD, zero,
        zero, one, 1.0 / w, zero, zero,
        dg, zero, zero,
        df, zero, zero,
    )
    rows = np.column_stack(columns)
    if rows.shape[1] != 1 + len(PATCHED_BIMINPUT_FIELDS):
        raise AssertionError("internal bimInput column-count mismatch")
    return rows


def write_text_input(path: Path, rows: np.ndarray) -> None:
    rows = np.asarray(rows, dtype=float)
    expected = 1 + len(PATCHED_BIMINPUT_FIELDS)
    if rows.ndim != 2 or rows.shape[1] != expected:
        raise ValueError(f"rows must have {expected} columns")
    np.savetxt(Path(path), rows, fmt="%.17g")
