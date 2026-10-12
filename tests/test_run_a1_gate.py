from pathlib import Path
import numpy as np

from tools.run_a1_gate import (
    std_build_command,
    make_zero_f_inputs,
    physical_domain_ok,
)


def test_std_build_command_matches_pinned_codeblocks_release_flags(tmp_path):
    root = tmp_path / "bim"
    binary = tmp_path / "bin" / "bim-solver-std"
    cmd = std_build_command(root, binary, compiler="g++")
    assert cmd == [
        "g++", "-std=c++14", "-O3", "-fopenmp", "-m64",
        "-DV_SIGN=-", "-DCFDS_ORDER=4",
        f"-I{root / 'include'}",
        str(root / "src" / "bim-solver-std.cpp"),
        "-o", str(binary),
    ]


def test_make_zero_f_inputs_keeps_common_columns_identical(tmp_path):
    rows = np.arange(3 * 26, dtype=float).reshape(3, 26)
    rows[:, -3:] = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    patched, upstream = make_zero_f_inputs(rows)
    assert patched.shape == (3, 26)
    assert upstream.shape == (3, 23)
    np.testing.assert_array_equal(patched[:, :23], rows[:, :23])
    np.testing.assert_array_equal(upstream, rows[:, :23])
    np.testing.assert_array_equal(patched[:, -3:], 0.0)


def test_physical_domain_gate_requires_all_hard_flags():
    healthy = {
        "all_finite": True,
        "same_oriented_lapse": True,
        "metric_positive": True,
        "density_nonnegative": True,
        "fluid_subluminal": True,
    }
    assert physical_domain_ok(healthy)
    for key in tuple(healthy):
        broken = dict(healthy)
        broken[key] = False
        assert not physical_domain_ok(broken)
