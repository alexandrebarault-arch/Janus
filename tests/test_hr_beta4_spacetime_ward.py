"""The beta4 f-only potential is an exact compact-coordinate volume."""
import numpy as np
import pytest
from numerics.hr_beta4_spacetime_ward import (
    beta4_ward_control, beta4_spacetime_volume,
)


def test_mixed_ward_zero_and_sampling_necessary():
    out=beta4_ward_control(order=40)
    np.testing.assert_allclose(out.mixed_exact,0.,atol=4e-13)
    np.testing.assert_allclose(out.mixed_without_field_sampling +
                               out.mixed_field_sampling,0.,atol=4e-13)
    assert np.min(np.abs(out.mixed_without_field_sampling))>1e-5
    assert out.jacobian_min>0


def test_exact_volume_invariant_under_two_chart_displacements():
    base=beta4_spacetime_volume(native_f_amp=.10,order=44)
    for eT,eR in ((.055,0),(-.04,0),(0,.06),(0,-.04),(.03,-.035)):
        val=beta4_spacetime_volume(eps_time=eT,eps_radial=eR,
                                   native_f_amp=.10,order=44)
        assert val==pytest.approx(base,abs=3e-12)


def test_ward_fails_if_native_perturbation_is_frozen():
    h=0.02
    def mixed(frozen):
        return (beta4_spacetime_volume(eps_time=h,native_f_amp=h,freeze_native_sampling=frozen)
                -beta4_spacetime_volume(eps_time=h,native_f_amp=-h,freeze_native_sampling=frozen)
                -beta4_spacetime_volume(eps_time=-h,native_f_amp=h,freeze_native_sampling=frozen)
                +beta4_spacetime_volume(eps_time=-h,native_f_amp=-h,freeze_native_sampling=frozen))/(4*h*h)
    full=mixed(False)
    broken=mixed(True)
    oracle=beta4_ward_control().mixed_without_field_sampling[0]
    assert abs(full)<3e-10
    assert broken==pytest.approx(oracle,rel=2e-3,abs=3e-7)
    assert abs(broken)>1e-5


def test_ward_quadrature_converges():
    lo=beta4_ward_control(order=28)
    hi=beta4_ward_control(order=40)
    np.testing.assert_allclose(lo.mixed_exact,hi.mixed_exact,atol=2e-12)
    np.testing.assert_allclose(lo.mixed_without_field_sampling,hi.mixed_without_field_sampling,atol=5e-12)
    assert lo.native_volume==pytest.approx(hi.native_volume,abs=5e-12)


def test_beta4_ward_respects_variable_domain_scales():
    out=beta4_ward_control(time_radius=.3,radial_radius=.75,order=48)
    np.testing.assert_allclose(out.mixed_exact,0.,atol=2e-12)
    assert np.min(np.abs(out.mixed_without_field_sampling))>1e-5


def test_ward_invalid_input_guards():
    with pytest.raises(ValueError): beta4_ward_control(time_radius=0)
    with pytest.raises(ValueError): beta4_ward_control(radial_radius=-1)
    with pytest.raises(ValueError): beta4_ward_control(order=5)
    with pytest.raises(ValueError): beta4_spacetime_volume(eps_time=float('nan'))
    with pytest.raises(ValueError): beta4_spacetime_volume(eps_radial=10.)
