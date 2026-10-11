import numpy as np
from numerics.reference_bim_solver_twin_input import reference_wall_rows


def test_reference_wall_rows_are_uniform_finite_and_positive_lapse():
    result = reference_wall_rows(n=20, delta_r=0.25, solve_points=80)
    rows = result["rows"]
    assert rows.shape == (20, 26)
    np.testing.assert_allclose(rows[:, 0], (np.arange(20) + 0.5) * 0.25)
    assert np.all(np.isfinite(rows))
    assert result["W_min"] > 0
    assert rows[0, 23] > rows[-1, 23]  # central f overdensity falls outward


def test_write_reference_wall_input_round_trips_text(tmp_path):
    from numerics.reference_bim_solver_twin_input import write_reference_wall_input

    path = tmp_path / "wall.txt"
    result = write_reference_wall_input(path, n=12, delta_r=0.25, solve_points=60)
    loaded = np.loadtxt(path)
    np.testing.assert_allclose(loaded, result["rows"], rtol=1e-12, atol=1e-14)
