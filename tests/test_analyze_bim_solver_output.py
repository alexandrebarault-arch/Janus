from pathlib import Path
import numpy as np

from tools.analyze_bim_solver_output import parse_text_output, short_run_summary


def make_output(path: Path):
    fields = [
        "t", "r", "gAlp", "fAlp", "gAlp_r", "fAlp_r",
        "C_1", "C_2", "C_3", "C_4", "p", "gB", "fB",
        "pfD", "pfS", "pftau", "pfD_t", "pfS_t", "pftau_t",
        "pfFD", "pfFS", "pfFtau", "pfFD_t", "pfFS_t", "pfFtau_t",
    ]
    lines = [f'{name} -> "{name}"' for name in fields]
    lines.append("*** DATA ***")

    def row(t, r, c, w, p, fs_rhs):
        vals = {
            "t": t, "r": r, "gAlp": 1.0, "fAlp": 1.0 / w,
            "gAlp_r": 0.0, "fAlp_r": 0.5,
            "C_1": c, "C_2": -c / 2, "C_3": c / 4, "C_4": -c / 8,
            "p": p, "gB": 1.0, "fB": 1.1,
            "pfD": 0.1, "pfS": 0.0, "pftau": 0.0,
            "pfD_t": 0.0, "pfS_t": 0.0, "pftau_t": 0.0,
            "pfFD": 0.2, "pfFS": 0.0, "pfFtau": 0.0,
            "pfFD_t": 0.0,
            "pfFS_t": -0.1 if t == 0 else fs_rhs,
            "pfFtau_t": 0.0,
        }
        return "\t".join(str(vals[f]) for f in fields)

    # One left ghost + two interior cells + one right ghost per frame.
    for r in (-0.1, 0.1, 0.3, 0.5):
        lines.append(row(0.0, r, 1e-5, 0.8, 0.0, 0.2))
    for r in (-0.1, 0.1, 0.3, 0.5):
        lines.append(row(0.01, r, 2e-4, 0.75, 0.03, 0.25))
    path.write_text("\n".join(lines) + "\n")


def test_parse_groups_frames_and_exposes_fields(tmp_path):
    path = tmp_path / "out.txt"
    make_output(path)
    out = parse_text_output(path)
    assert out.fields[0:2] == ("t", "r")
    assert len(out.frames) == 2
    assert out.frames[0].time == 0.0
    assert out.frames[1].time == 0.01
    assert out.frames[0].data.shape == (4, 25)
    np.testing.assert_allclose(out.column(0, "r", n_ghost=1), [0.1, 0.3])


def test_summary_uses_interior_and_does_not_require_f_momentum_rhs_zero(tmp_path):
    path = tmp_path / "out.txt"
    make_output(path)
    out = parse_text_output(path)
    s = short_run_summary(out, n_ghost=1)
    assert s["frame_count"] == 2
    assert s["all_finite"]
    assert s["same_oriented_lapse"]
    assert s["initial_rest_rhs_max"] == 0.0
    assert "pfFS_t" not in s["initial_rest_rhs_fields"]
    assert s["initial_g_momentum_identity_max"] == 0.0
    assert s["initial_f_momentum_identity_max"] == 0.0
    assert abs(s["frames"][0]["W_min"] - 0.8) < 1e-12
    assert abs(s["frames"][1]["W_min"] - 0.75) < 1e-12
    assert abs(s["frames"][1]["constraint_max"] - 2e-4) < 1e-15
    assert abs(s["frames"][1]["p_max_abs"] - 0.03) < 1e-15
    assert abs(s["frames"][0]["R_max"] - 1.1) < 1e-15


def test_parser_rejects_wrong_column_count(tmp_path):
    path = tmp_path / "bad.txt"
    path.write_text('t -> "t"\nr -> "r"\n*** DATA ***\n0 1 2\n')
    try:
        parse_text_output(path)
    except ValueError as exc:
        assert "columns" in str(exc)
    else:
        raise AssertionError("expected ValueError")
