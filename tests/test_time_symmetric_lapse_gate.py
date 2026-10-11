import numpy as np

from numerics.time_symmetric_lapse_gate import (
    reference_initial_lapse_profile,
    time_symmetric_w,
)


def test_exact_symmetric_state_has_unit_lapse_ratio():
    state = dict(
        r=2.3,
        Ag=1.12,
        Af=1.12,
        Bg=1.12,
        Bf=1.12,
        gDB=0.04,
        fDB=0.04,
        b0=-0.024,
        b1=0.01,
        b2=0.004,
        b3=0.01,
        b4=-0.024,
        kg=1.0,
        kf=1.0,
        Dg=0.03,
        Df=0.03,
    )
    W, _, _ = time_symmetric_w(**state)
    assert np.isfinite(W)
    assert abs(W - 1.0) < 1.0e-11


def test_reference_initial_slice_has_positive_finite_lapse_ratio():
    out = reference_initial_lapse_profile(points=420, tol=2.0e-7)
    assert out["solution"].success
    W = out["W"]
    assert np.all(np.isfinite(W))
    assert np.min(W) > 0.0
    assert 0.75 < float(np.min(W)) < 0.85
    assert 1.10 < float(np.max(W)) < 1.22


def test_reference_outer_lapse_ratio_returns_to_one():
    out = reference_initial_lapse_profile(points=420, tol=2.0e-7)
    assert abs(float(out["W"][-1]) - 1.0) < 2.0e-4
