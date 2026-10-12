import pytest

from numerics.two_matter_flrw import Beta, Model, regression_model, track_from_today


def test_calibrated_model_tracks_branch_without_name_error():
    model = regression_model()
    a, y = track_from_today(model, a_min=0.5, points=8)
    assert len(a) == 8
    assert len(y) == 8
    assert y[0] == pytest.approx(model.y0)


def test_uncalibrated_model_is_rejected_explicitly():
    model = Model(beta=Beta(beta1=1.0), alpha=1.0, y0=1.0)
    with pytest.raises(ValueError, match="calibrated"):
        track_from_today(model, a_min=0.5, points=4)
