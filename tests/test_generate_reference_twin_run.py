from pathlib import Path
import numpy as np

from tools.generate_reference_twin_run import generate_reference_run


def test_generate_reference_run_creates_matching_input_and_config(tmp_path: Path):
    result = generate_reference_run(
        tmp_path,
        n=16,
        delta_r=0.25,
        solve_points=70,
        steps=8,
    )
    initial = tmp_path / "initial.txt"
    config = tmp_path / "config.ini"
    assert initial.is_file()
    assert config.is_file()
    rows = np.loadtxt(initial)
    assert rows.shape == (16, 26)
    text = config.read_text()
    assert "grid.nLen = 16" in text
    assert "grid.delta_r = 0.25" in text
    assert "input.file = initial.txt" in text
    assert "output.file = output.txt" in text
    assert "integ.t_1 = 0.2" in text
    assert result["W_min"] > 0


def test_cli_default_grid_preserves_reference_outer_radius(monkeypatch, tmp_path):
    import sys
    import tools.generate_reference_twin_run as mod

    seen = {}

    def fake(directory, **kwargs):
        seen.update(kwargs)
        return {
            "initial_path": tmp_path / "initial.txt",
            "config_path": tmp_path / "config.ini",
            "W_min": 1.0,
            "W_max": 1.0,
        }

    monkeypatch.setattr(mod, "generate_reference_run", fake)
    monkeypatch.setattr(sys, "argv", ["generate_reference_twin_run.py", str(tmp_path)])
    assert mod.main() == 0
    assert seen["n"] == 500
    assert seen["delta_r"] == 0.05
    assert seen["n"] * seen["delta_r"] == 25.0
