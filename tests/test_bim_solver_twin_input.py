import numpy as np
import pytest

from numerics.bim_solver_twin_input import build_rows, uniform_centers, write_text_input


def test_uniform_centers_are_cell_centered():
    r = uniform_centers(4, 0.2)
    np.testing.assert_allclose(r, [0.1, 0.3, 0.5, 0.7])


def test_rows_match_patched_biminput_order_and_geometry(tmp_path):
    r = np.array([0.1, 0.3])
    pg = np.array([2.0, 1.5])
    dpg = np.array([0.2, -0.15])
    pf = np.array([1.2, 1.1])
    dpf = np.array([0.06, -0.11])
    Dg = np.array([0.01, 0.02])
    Df = np.array([0.03, 0.04])
    W = np.array([0.8, 1.25])

    rows = build_rows(r, pg, dpg, pf, dpf, Dg, Df, W)
    assert rows.shape == (2, 26)
    np.testing.assert_allclose(rows[:, 0], r)
    np.testing.assert_allclose(rows[:, 1], pg**2)
    np.testing.assert_allclose(rows[:, 2], pg**2)
    np.testing.assert_allclose(rows[:, 5], 2 * dpg / pg)
    np.testing.assert_allclose(rows[:, 6], 2 * dpg / pg)
    np.testing.assert_allclose(rows[:, 7], 0)
    np.testing.assert_allclose(rows[:, 8], pf**2)
    np.testing.assert_allclose(rows[:, 9], pf**2)
    np.testing.assert_allclose(rows[:, 12], 2 * dpf / pf)
    np.testing.assert_allclose(rows[:, 13], 2 * dpf / pf)
    np.testing.assert_allclose(rows[:, 14], 0)
    np.testing.assert_allclose(rows[:, 15], 0)
    np.testing.assert_allclose(rows[:, 16], 1)
    np.testing.assert_allclose(rows[:, 17], 1 / W)
    np.testing.assert_allclose(rows[:, 18], 0)
    np.testing.assert_allclose(rows[:, 19], 0)
    np.testing.assert_allclose(rows[:, 20], Dg)
    np.testing.assert_allclose(rows[:, 21:23], 0)
    np.testing.assert_allclose(rows[:, 23], Df)
    np.testing.assert_allclose(rows[:, 24:26], 0)

    path = tmp_path / "initial.txt"
    write_text_input(path, rows)
    np.testing.assert_allclose(np.loadtxt(path), rows, rtol=1e-12, atol=1e-14)


def test_invalid_lapse_or_conformal_factor_rejected():
    r = np.array([0.1])
    good = np.array([1.0])
    zero = np.array([0.0])
    with pytest.raises(ValueError):
        build_rows(r, good, zero, good, zero, zero, zero, np.array([0.0]))
    with pytest.raises(ValueError):
        build_rows(r, zero, zero, good, zero, zero, zero, good)
