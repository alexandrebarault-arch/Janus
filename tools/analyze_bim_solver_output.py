from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import numpy as np

_HEADER_RE = re.compile(r'^\s*([^\s]+)\s*->\s*"')


@dataclass(frozen=True)
class OutputFrame:
    time: float
    data: np.ndarray


@dataclass(frozen=True)
class BimTextOutput:
    fields: tuple[str, ...]
    frames: tuple[OutputFrame, ...]

    def field_index(self, name: str) -> int:
        try:
            return self.fields.index(name)
        except ValueError as exc:
            raise KeyError(f"field not found: {name}") from exc

    def column(
        self,
        frame: int,
        name: str,
        *,
        n_ghost: int = 0,
    ) -> np.ndarray:
        data = self.frames[frame].data
        if n_ghost < 0 or 2 * n_ghost >= len(data):
            raise ValueError("invalid n_ghost for frame length")
        if n_ghost:
            data = data[n_ghost:-n_ghost]
        return data[:, self.field_index(name)]


def parse_text_output(path: Path) -> BimTextOutput:
    """Parse text output produced by upstream GridOutputWriter."""
    lines = Path(path).read_text().splitlines()
    fields: list[str] = []
    data_start = None
    for i, line in enumerate(lines):
        if line.strip() == "*** DATA ***":
            data_start = i + 1
            break
        if not line.strip():
            continue
        match = _HEADER_RE.match(line)
        if not match:
            raise ValueError(f"invalid output header line: {line!r}")
        fields.append(match.group(1))
    if data_start is None:
        raise ValueError("missing *** DATA *** marker")
    if not fields:
        raise ValueError("output contains no fields")
    if len(set(fields)) != len(fields):
        raise ValueError("output header contains duplicate fields")
    if "t" not in fields:
        raise ValueError("output header is missing t")

    rows: list[np.ndarray] = []
    for lineno, line in enumerate(lines[data_start:], start=data_start + 1):
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) != len(fields):
            raise ValueError(
                f"line {lineno}: expected {len(fields)} columns, got {len(parts)}"
            )
        try:
            row = np.asarray([float(x) for x in parts], dtype=float)
        except ValueError as exc:
            raise ValueError(f"line {lineno}: invalid numeric value") from exc
        rows.append(row)
    if not rows:
        raise ValueError("output contains no data rows")

    t_index = fields.index("t")
    frames: list[OutputFrame] = []
    current_time = float(rows[0][t_index])
    current_rows: list[np.ndarray] = []
    for row in rows:
        t = float(row[t_index])
        if t != current_time:
            frames.append(OutputFrame(current_time, np.vstack(current_rows)))
            current_time = t
            current_rows = []
        current_rows.append(row)
    frames.append(OutputFrame(current_time, np.vstack(current_rows)))

    return BimTextOutput(tuple(fields), tuple(frames))


def _interior(frame: OutputFrame, n_ghost: int) -> np.ndarray:
    data = frame.data
    if n_ghost < 0 or 2 * n_ghost >= len(data):
        raise ValueError("invalid n_ghost for frame length")
    return data[n_ghost:-n_ghost] if n_ghost else data


def _rest_mass(data: np.ndarray, field_index: dict[str, int], density_name: str) -> float:
    """Return the spherical Valencia rest-mass integral 4*pi*int D r^2 dr.

    The absolute value is a grid diagnostic rather than an ADM mass.  Its
    relative drift is the useful short-run conservation test.  For the
    cell-centred uniform grids used by the reference experiment, `gradient(r)`
    is exactly the cell width away from floating-point roundoff.
    """
    if "r" not in field_index or density_name not in field_index or len(data) < 2:
        return float("nan")
    r = data[:, field_index["r"]]
    D = data[:, field_index[density_name]]
    if not np.all(np.isfinite(r)) or not np.all(np.isfinite(D)):
        return float("nan")
    if np.any(np.diff(r) <= 0.0):
        return float("nan")
    dr = np.gradient(r)
    return float(4.0 * np.pi * np.sum(D * r**2 * dr))


def _relative_drift(values: list[float], *, zero_tol: float = 1.0e-30) -> float:
    arr = np.asarray(values, dtype=float)
    if arr.size == 0 or not np.all(np.isfinite(arr)):
        return float("nan")
    ref = float(arr[0])
    if abs(ref) <= zero_tol:
        return 0.0 if bool(np.all(np.abs(arr) <= zero_tol)) else float("inf")
    return float(np.max(np.abs(arr - ref)) / abs(ref))


def short_run_summary(out: BimTextOutput, *, n_ghost: int = 10) -> dict:
    """Summarize short-run health without assigning a physics verdict.

    `pfFS_t` is deliberately excluded from the initial-rest zero-RHS control:
    the f lapse is spatially varying on the reference slice, so f momentum can
    start accelerating even though both fluids initially have zero velocity.

    The summary also monitors quantities that must stay in the physical domain
    before any Janus interpretation is allowed: positive spatial metric factors,
    non-negative conserved dust densities, subluminal physical radial speeds and
    independent g/f rest-mass conservation.
    """
    constraint_names = [x for x in ("C_1", "C_2", "C_3", "C_4") if x in out.fields]
    rest_zero_rhs = tuple(
        x
        for x in ("pfD_t", "pfS_t", "pftau_t", "pfFD_t", "pfFtau_t")
        if x in out.fields
    )
    field_index = {name: i for i, name in enumerate(out.fields)}

    frame_summaries = []
    all_finite = True
    same_oriented = True
    metric_positive = True
    density_nonnegative = True
    fluid_subluminal = True
    global_constraint = 0.0
    rest_mass_g: list[float] = []
    rest_mass_f: list[float] = []

    for frame in out.frames:
        data = _interior(frame, n_ghost)
        all_finite = all_finite and bool(np.all(np.isfinite(data)))
        item = {"time": frame.time, "rows": len(data)}

        if constraint_names:
            vals = np.column_stack([data[:, field_index[x]] for x in constraint_names])
            cmax = float(np.max(np.abs(vals)))
            item["constraint_max"] = cmax
            global_constraint = max(global_constraint, cmax)
        else:
            item["constraint_max"] = float("nan")

        if "gAlp" in field_index and "fAlp" in field_index:
            galp = data[:, field_index["gAlp"]]
            falp = data[:, field_index["fAlp"]]
            with np.errstate(divide="ignore", invalid="ignore"):
                W = galp / falp
            item["W_min"] = float(np.nanmin(W))
            item["W_max"] = float(np.nanmax(W))
            good = bool(np.all(np.isfinite(W)) and np.all(W > 0.0))
            item["same_oriented_lapse"] = good
            same_oriented = same_oriented and good
        else:
            item["W_min"] = item["W_max"] = float("nan")
            item["same_oriented_lapse"] = False
            same_oriented = False

        if "p" in field_index:
            item["p_max_abs"] = float(np.max(np.abs(data[:, field_index["p"]])))
        else:
            item["p_max_abs"] = float("nan")

        if "gB" in field_index and "fB" in field_index:
            with np.errstate(divide="ignore", invalid="ignore"):
                R = data[:, field_index["fB"]] / data[:, field_index["gB"]]
            item["R_min"] = float(np.nanmin(R))
            item["R_max"] = float(np.nanmax(R))
        else:
            item["R_min"] = item["R_max"] = float("nan")

        metric_fields = [x for x in ("gA", "gB", "fA", "fB") if x in field_index]
        if len(metric_fields) == 4:
            metric_values = np.column_stack([data[:, field_index[x]] for x in metric_fields])
            item["metric_min_factor"] = float(np.min(metric_values))
            good_metric = bool(np.all(np.isfinite(metric_values)) and np.all(metric_values > 0.0))
            item["metric_positive"] = good_metric
            metric_positive = metric_positive and good_metric
        else:
            item["metric_min_factor"] = float("nan")
            item["metric_positive"] = False
            metric_positive = False

        frame_speed_good = True
        for prefix, A_name, v_name in (
            ("g", "gA", "pfv"),
            ("f", "fA", "pfFv"),
        ):
            if A_name in field_index and v_name in field_index:
                physical_speed = np.abs(
                    data[:, field_index[A_name]] * data[:, field_index[v_name]]
                )
                vmax = float(np.max(physical_speed))
                item[f"{prefix}_speed_max"] = vmax
                frame_speed_good = frame_speed_good and bool(
                    np.all(np.isfinite(physical_speed)) and np.all(physical_speed < 1.0)
                )
            else:
                item[f"{prefix}_speed_max"] = float("nan")
        item["fluid_subluminal"] = frame_speed_good
        fluid_subluminal = fluid_subluminal and frame_speed_good

        frame_density_good = True
        for name in ("pfD", "pfFD"):
            if name in field_index:
                density = data[:, field_index[name]]
                item[f"{name}_min"] = float(np.min(density))
                item[f"{name}_max_abs"] = float(np.max(np.abs(density)))
                frame_density_good = frame_density_good and bool(
                    np.all(np.isfinite(density)) and np.all(density >= 0.0)
                )
            else:
                item[f"{name}_min"] = float("nan")
        item["density_nonnegative"] = frame_density_good
        density_nonnegative = density_nonnegative and frame_density_good

        mg = _rest_mass(data, field_index, "pfD")
        mf = _rest_mass(data, field_index, "pfFD")
        item["rest_mass_g"] = mg
        item["rest_mass_f"] = mf
        rest_mass_g.append(mg)
        rest_mass_f.append(mf)

        frame_summaries.append(item)

    first = _interior(out.frames[0], n_ghost)
    initial_rhs_max = 0.0
    if rest_zero_rhs:
        rhs = np.column_stack([first[:, field_index[x]] for x in rest_zero_rhs])
        initial_rhs_max = float(np.max(np.abs(rhs)))

    def momentum_identity(momentum_rhs, lapse_r, density, tau):
        needed = (momentum_rhs, lapse_r, density, tau)
        if not all(x in field_index for x in needed):
            return float("nan")
        err = (
            first[:, field_index[momentum_rhs]]
            + first[:, field_index[lapse_r]]
            * (first[:, field_index[density]] + first[:, field_index[tau]])
        )
        return float(np.max(np.abs(err)))

    initial_g_momentum_identity_max = momentum_identity(
        "pfS_t", "gAlp_r", "pfD", "pftau"
    )
    initial_f_momentum_identity_max = momentum_identity(
        "pfFS_t", "fAlp_r", "pfFD", "pfFtau"
    )

    return {
        "frame_count": len(out.frames),
        "times": tuple(float(f.time) for f in out.frames),
        "all_finite": all_finite,
        "same_oriented_lapse": same_oriented,
        "metric_positive": metric_positive,
        "density_nonnegative": density_nonnegative,
        "fluid_subluminal": fluid_subluminal,
        "rest_mass_g_rel_drift_max": _relative_drift(rest_mass_g),
        "rest_mass_f_rel_drift_max": _relative_drift(rest_mass_f),
        "constraint_fields": tuple(constraint_names),
        "constraint_global_max": global_constraint if constraint_names else float("nan"),
        "initial_rest_rhs_fields": rest_zero_rhs,
        "initial_rest_rhs_max": initial_rhs_max,
        "initial_g_momentum_identity_max": initial_g_momentum_identity_max,
        "initial_f_momentum_identity_max": initial_f_momentum_identity_max,
        "frames": frame_summaries,
    }
