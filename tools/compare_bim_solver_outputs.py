from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import numpy as np

from tools.analyze_bim_solver_output import BimTextOutput, parse_text_output


DEFAULT_IGNORE_FIELDS = frozenset({"sysStat"})


@dataclass(frozen=True)
class FieldDifference:
    field: str
    max_abs: float
    max_rel: float


@dataclass(frozen=True)
class OutputComparison:
    fields: tuple[FieldDifference, ...]
    worst_abs_field: str | None
    worst_abs: float
    worst_rel_field: str | None
    worst_rel: float

    def by_name(self) -> dict[str, FieldDifference]:
        return {x.field: x for x in self.fields}


def _interior(data: np.ndarray, n_ghost: int) -> np.ndarray:
    if n_ghost < 0 or 2 * n_ghost >= len(data):
        raise ValueError("invalid n_ghost for frame length")
    return data[n_ghost:-n_ghost] if n_ghost else data


def compare_outputs(
    reference: BimTextOutput,
    candidate: BimTextOutput,
    *,
    n_ghost: int = 0,
    ignore_fields=DEFAULT_IGNORE_FIELDS,
    time_atol: float = 1.0e-14,
    radius_atol: float = 1.0e-14,
    relative_floor: float = 1.0e-14,
) -> OutputComparison:
    """Compare all output fields shared by an upstream and patched zero-f run.

    Extra twin-fluid fields in the patched output are naturally excluded because
    they are not present in the upstream output.  Common geometric, g-fluid,
    bimetric-interaction and diagnostic fields are compared at every common
    interior cell and time frame.
    """
    if len(reference.frames) != len(candidate.frames):
        raise ValueError("frame-count mismatch")
    if relative_floor <= 0 or time_atol < 0 or radius_atol < 0:
        raise ValueError("invalid comparison tolerances")

    ignore = set(ignore_fields)
    common = sorted((set(reference.fields) & set(candidate.fields)) - ignore)
    if "t" not in common or "r" not in common:
        raise ValueError("both outputs must share t and r fields")

    ref_index = {name: i for i, name in enumerate(reference.fields)}
    cand_index = {name: i for i, name in enumerate(candidate.fields)}
    accum_abs = {name: 0.0 for name in common if name not in ("t", "r")}
    accum_rel = {name: 0.0 for name in common if name not in ("t", "r")}

    for iframe, (rf, cf) in enumerate(zip(reference.frames, candidate.frames)):
        if not np.isclose(rf.time, cf.time, rtol=0.0, atol=time_atol):
            raise ValueError(f"time mismatch at frame {iframe}: {rf.time} vs {cf.time}")
        rd = _interior(rf.data, n_ghost)
        cd = _interior(cf.data, n_ghost)
        if rd.shape[0] != cd.shape[0]:
            raise ValueError(f"row-count mismatch at frame {iframe}")

        rr = rd[:, ref_index["r"]]
        cr = cd[:, cand_index["r"]]
        if not np.allclose(rr, cr, rtol=0.0, atol=radius_atol):
            raise ValueError(f"radius-grid mismatch at frame {iframe}")

        for name in accum_abs:
            a = rd[:, ref_index[name]]
            b = cd[:, cand_index[name]]
            if not np.all(np.isfinite(a)) or not np.all(np.isfinite(b)):
                raise ValueError(f"non-finite value in common field {name}")
            delta = np.abs(b - a)
            max_abs = float(np.max(delta)) if delta.size else 0.0
            scale = np.maximum(np.abs(a), relative_floor)
            max_rel = float(np.max(delta / scale)) if delta.size else 0.0
            accum_abs[name] = max(accum_abs[name], max_abs)
            accum_rel[name] = max(accum_rel[name], max_rel)

    diffs = tuple(
        FieldDifference(name, accum_abs[name], accum_rel[name])
        for name in sorted(accum_abs)
    )
    if diffs:
        worst_abs_obj = max(diffs, key=lambda x: x.max_abs)
        worst_rel_obj = max(diffs, key=lambda x: x.max_rel)
        return OutputComparison(
            diffs,
            worst_abs_obj.field,
            worst_abs_obj.max_abs,
            worst_rel_obj.field,
            worst_rel_obj.max_rel,
        )
    return OutputComparison(tuple(), None, 0.0, None, 0.0)


def compare_output_files(reference_path: Path, candidate_path: Path, **kwargs) -> OutputComparison:
    return compare_outputs(
        parse_text_output(Path(reference_path)),
        parse_text_output(Path(candidate_path)),
        **kwargs,
    )


def require_regression(
    comparison: OutputComparison,
    *,
    abs_tol: float,
    rel_tol: float,
) -> None:
    """Raise when any common field exceeds both absolute and relative tolerances."""
    if abs_tol < 0 or rel_tol < 0:
        raise ValueError("regression tolerances must be non-negative")
    failed = [
        x for x in comparison.fields
        if x.max_abs > abs_tol and x.max_rel > rel_tol
    ]
    if failed:
        worst = max(failed, key=lambda x: max(x.max_abs / max(abs_tol, 1e-300), x.max_rel / max(rel_tol, 1e-300)))
        raise AssertionError(
            "zero-f regression failed: "
            f"field={worst.field} max_abs={worst.max_abs:.6g} "
            f"max_rel={worst.max_rel:.6g}"
        )
