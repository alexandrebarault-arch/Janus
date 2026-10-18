"""Independent native FLRW EH coordinate-change Ward tests."""
import numpy as np
import pytest
from numerics.hr_eh_spacetime_ward import (
    eh_flat_native_spacetime_ward,eh_flat_native_spacetime_action
)


def test_complete_eh_ward_both_compact_chart_modes():
    z=eh_flat_native_spacetime_ward(order=36)
    np.testing.assert_allclose(z.full_mixed,0.,atol=2e-13)
    np.testing.assert_allclose(z.frozen_mixed+z.sampling_mixed,0.,atol=2e-13)
    assert z.chart_min_determinant>0
    assert np.linalg.norm(z.frozen_mixed)>1e-5


def test_exact_f_native_eh_action_invariant_to_finite_chart_motion():
    v=.04
    ref=eh_flat_native_spacetime_action(lapse_amp=v,order=46)
    for et,er in ((.045,0),(-.035,0),(0,.045),(0,-.035),(.035,-.025)):
        out=eh_flat_native_spacetime_action(eps_time=et,eps_radial=er,lapse_amp=v,order=46)
        assert out==pytest.approx(ref,abs=2e-12)


def test_frozen_lapse_sampling_fails_mixed_eh_ward():
    h=.015
    def mixed(frozen,mode):
        def f(e,v):
            kw={'eps_time':e} if mode=='time' else {'eps_radial':e}
            return eh_flat_native_spacetime_action(lapse_amp=v,freeze_native_sampling=frozen,order=44,**kw)
        return (f(h,h)-f(h,-h)-f(-h,h)+f(-h,-h))/(4*h*h)
    diag=eh_flat_native_spacetime_ward(order=44)
    for i,mode in enumerate(('time','radial')):
        assert abs(mixed(False,mode))<3e-10
        assert mixed(True,mode)==pytest.approx(diag.frozen_mixed[i],rel=2e-3,abs=2e-7)


def test_eh_ward_quad_and_background_sign():
    lo=eh_flat_native_spacetime_ward(order=28)
    hi=eh_flat_native_spacetime_ward(order=44)
    np.testing.assert_allclose(lo.full_mixed,hi.full_mixed,atol=3e-13)
    np.testing.assert_allclose(lo.frozen_mixed,hi.frozen_mixed,atol=4e-12)
    assert lo.baseline_action<0


def test_eh_ward_with_changed_time_radial_support():
    x=eh_flat_native_spacetime_ward(time_radius=.3,radial_radius=.7,order=38)
    np.testing.assert_allclose(x.full_mixed,0.,atol=3e-13)
    assert np.linalg.norm(x.frozen_mixed)>1e-5


def test_eh_ward_guards():
    with pytest.raises(ValueError):eh_flat_native_spacetime_ward(time_radius=0)
    with pytest.raises(ValueError):eh_flat_native_spacetime_ward(radial_radius=-1)
    with pytest.raises(ValueError):eh_flat_native_spacetime_ward(order=5)
    with pytest.raises(ValueError):eh_flat_native_spacetime_action(eps_time=float('nan'))
    with pytest.raises(ValueError):eh_flat_native_spacetime_action(eps_radial=5)
    with pytest.raises(ValueError):eh_flat_native_spacetime_action(lapse_amp=-1)
