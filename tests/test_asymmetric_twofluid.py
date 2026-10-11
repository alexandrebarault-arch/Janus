import numpy as np

from numerics.asymmetric_twofluid import coupling_matrix, integrate_equal_seed


def test_symmetric_limit_recovers_common_and_relative_modes():
    vals = np.sort(np.linalg.eigvals(coupling_matrix(0.5, 1.0)).real)
    assert np.allclose(vals, [1.0, 4.0 / 3.0], rtol=0, atol=1e-12)


def test_symmetric_equal_seed_does_not_generate_relative_mode():
    out = integrate_equal_seed(f_g=0.5, x=1.0, z_start=1100.0, seed=1e-5)
    assert abs(out["delta_g"] - out["delta_f"]) < 1e-10


def test_asymmetric_background_generates_relative_component_in_toy_limit():
    out = integrate_equal_seed(f_g=2.0 / 3.0, x=1.0, z_start=1100.0, seed=1e-5)
    assert abs(out["delta_g"] - out["delta_f"]) > 0.05
    assert out["delta_g"] > 0
    assert out["delta_f"] < 0
