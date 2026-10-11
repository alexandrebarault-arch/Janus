from pathlib import Path
import math

from tools.analyze_bim_solver_output import parse_text_output, short_run_summary


FIELDS = (
    "t", "r", "gAlp", "fAlp",
    "gA", "gB", "fA", "fB", "p", "pfv", "pfFv",
    "pfD", "pfFD", "C_1", "C_2", "C_3", "C_4",
)


def _write(path: Path, frames):
    lines = [f'{name} -> "{name}"' for name in FIELDS]
    lines.append("*** DATA ***")
    for frame in frames:
        for row in frame:
            lines.append(" ".join(str(row[name]) for name in FIELDS))
    path.write_text("\n".join(lines) + "\n")


def _frame(t, *, Dg=0.1, Df=0.2, gA=1.2, fA=1.1, vg=0.5, vf=0.4):
    rows = []
    for r in (-0.1, 0.1, 0.3, 0.5):
        rows.append(
            {
                "t": t,
                "r": r,
                "gAlp": 1.0,
                "fAlp": 1.25,
                "gA": gA,
                "gB": 1.0,
                "fA": fA,
                "fB": 1.05,
                "p": 0.01,
                "pfv": vg,
                "pfFv": vf,
                "pfD": Dg,
                "pfFD": Df,
                "C_1": 1e-6,
                "C_2": -2e-6,
                "C_3": 3e-6,
                "C_4": -4e-6,
            }
        )
    return rows


def test_summary_tracks_metric_domain_speeds_density_and_two_rest_masses(tmp_path):
    path = tmp_path / "healthy.txt"
    _write(path, [_frame(0.0), _frame(0.01, Dg=0.101, Df=0.198)])
    s = short_run_summary(parse_text_output(path), n_ghost=1)

    assert s["metric_positive"]
    assert s["density_nonnegative"]
    assert s["fluid_subluminal"]
    assert abs(s["frames"][0]["g_speed_max"] - 0.6) < 1e-15
    assert abs(s["frames"][0]["f_speed_max"] - 0.44) < 1e-15
    assert s["frames"][0]["rest_mass_g"] > 0.0
    assert s["frames"][0]["rest_mass_f"] > 0.0
    assert abs(s["rest_mass_g_rel_drift_max"] - 0.01) < 1e-12
    assert abs(s["rest_mass_f_rel_drift_max"] - 0.01) < 1e-12


def test_summary_rejects_negative_metric_negative_density_and_superluminal_speed(tmp_path):
    path = tmp_path / "bad.txt"
    _write(
        path,
        [
            _frame(0.0),
            _frame(0.01, Df=-0.01, fA=-1.1, vf=1.2),
        ],
    )
    s = short_run_summary(parse_text_output(path), n_ghost=1)

    assert not s["metric_positive"]
    assert not s["density_nonnegative"]
    assert not s["fluid_subluminal"]
    assert not s["frames"][1]["metric_positive"]
    assert not s["frames"][1]["density_nonnegative"]


def test_zero_sector_mass_is_stable_only_if_it_stays_zero(tmp_path):
    path = tmp_path / "zero_f.txt"
    _write(path, [_frame(0.0, Df=0.0), _frame(0.01, Df=0.0)])
    s = short_run_summary(parse_text_output(path), n_ghost=1)
    assert s["rest_mass_f_rel_drift_max"] == 0.0

    leaked = tmp_path / "leaked_f.txt"
    _write(leaked, [_frame(0.0, Df=0.0), _frame(0.01, Df=1e-8)])
    s2 = short_run_summary(parse_text_output(leaked), n_ghost=1)
    assert math.isinf(s2["rest_mass_f_rel_drift_max"])
