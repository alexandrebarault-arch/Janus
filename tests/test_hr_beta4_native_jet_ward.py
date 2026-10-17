"""Integrate the *previously built* native HR 22-jet against exact beta4 Ward."""
import numpy as np
from numerics.hr_beta4_spacetime_ward import beta4_ward_control
from numerics.hr_beta4_native_jet_ward import native_beta4_mixed_ward


def test_native_hr_beta4_full_mixed_ward_both_chart_modes():
    jet=native_beta4_mixed_ward(order=24)
    oracle=beta4_ward_control(order=24)
    assert jet.jacobian_min>0
    np.testing.assert_allclose(jet.mixed_complete,0.,atol=1e-12)
    np.testing.assert_allclose(jet.mixed_complete,-oracle.mixed_exact,atol=1e-12)


def test_native_hr_beta4_without_field_transport_breaks_ward():
    jet=native_beta4_mixed_ward(order=24)
    oracle=beta4_ward_control(order=24)
    assert np.min(np.abs(jet.mixed_frozen_sampling))>1e-5
    np.testing.assert_allclose(jet.mixed_frozen_sampling,
                               -oracle.mixed_without_field_sampling,atol=1e-12)
    np.testing.assert_allclose(jet.mixed_sampling_contribution,
                               -oracle.mixed_field_sampling,atol=1e-12)
    np.testing.assert_allclose(jet.mixed_frozen_sampling+
                               jet.mixed_sampling_contribution,0.,atol=1e-12)


def test_native_hr_beta4_quadrature_refinement():
    lo=native_beta4_mixed_ward(order=18)
    hi=native_beta4_mixed_ward(order=30)
    np.testing.assert_allclose(lo.mixed_complete,hi.mixed_complete,atol=4e-12)
    np.testing.assert_allclose(lo.mixed_frozen_sampling,hi.mixed_frozen_sampling,atol=3e-12)


def test_native_hr_beta4_shifted_spacetime_domain():
    jet=native_beta4_mixed_ward(time_radius=.3,radial_radius=.75,order=30)
    oracle=beta4_ward_control(time_radius=.3,radial_radius=.75,order=30)
    np.testing.assert_allclose(jet.mixed_complete,0.,atol=2e-12)
    np.testing.assert_allclose(jet.mixed_frozen_sampling,
                               -oracle.mixed_without_field_sampling,atol=2e-12)
