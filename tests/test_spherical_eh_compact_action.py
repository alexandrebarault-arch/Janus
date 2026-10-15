import math
import numpy as np


def _ricci(**kw):
    from numerics.spherical_eh_compact_action import spherical_ricci_scalar
    base=dict(r=1.3,phi=0.0,phi_t=0.0,phi_r=0.0,phi_rr=0.0,
              psi=0.0,psi_t=0.0,psi_tt=0.0,psi_r=0.0)
    base.update(kw)
    return spherical_ricci_scalar(**base)


def test_unperturbed_flat_flrw_ricci_scalar_is_6_app_over_a3():
    a=1.7; ap=0.42; app=-0.13
    got=_ricci(a=a,ap=ap,app=app)
    assert math.isclose(got,6.0*app/a**3,rel_tol=0,abs_tol=3e-14)


def test_minkowski_background_has_zero_ricci_scalar():
    assert abs(_ricci(a=1.0,ap=0.0,app=0.0)) < 1e-14


def test_constant_spatial_metric_rescaling_matches_exact_warped_geometry():
    psi=0.17; r=1.8
    got=_ricci(a=1.0,ap=0.0,app=0.0,r=r,psi=psi)
    expected=2.0*(1.0-math.exp(-2.0*psi))/r**2
    assert math.isclose(got,expected,rel_tol=0,abs_tol=3e-14)


def test_density_is_finite_for_generic_fields():
    from numerics.spherical_eh_compact_action import eh_radial_density
    val=eh_radial_density(a=1.2,ap=0.3,app=-0.07,r=0.8,
        phi=0.02,phi_t=-0.03,phi_r=0.04,phi_rr=-0.05,
        psi=-0.01,psi_t=0.06,psi_tt=0.07,psi_r=-0.02)
    assert np.isfinite(val)
