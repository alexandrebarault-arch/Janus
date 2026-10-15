import math


def test_minkowski_reduced_eh_density_is_boundary_constant_four():
    from numerics.spherical_eh_reduced_action import reduced_eh_density
    out = reduced_eh_density(
        a=1.0, a_prime=0.0, a_second=0.0, r=1.7,
        phi=0.0, phi_t=0.0, phi_r=0.0, phi_rr=0.0,
        psi=0.0, psi_t=0.0, psi_tt=0.0, psi_r=0.0,
    )
    assert math.isclose(out, 4.0, rel_tol=0.0, abs_tol=1e-14)


def test_flat_flrw_reduced_density_matches_independent_closed_form():
    from numerics.spherical_eh_reduced_action import reduced_eh_density
    a=1.3; ap=0.47; app=-0.12; r=0.83
    out = reduced_eh_density(
        a=a, a_prime=ap, a_second=app, r=r,
        phi=0.0, phi_t=0.0, phi_r=0.0, phi_rr=0.0,
        psi=0.0, psi_t=0.0, psi_tt=0.0, psi_r=0.0,
    )
    Hc=ap/a
    Hcp=app/a-Hc*Hc
    expected=a*a*(4.0 + 2.0*r*r*(Hcp-Hc*Hc))
    assert math.isclose(out, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_static_rindler_radial_metric_has_zero_2d_curvature_contribution():
    from numerics.spherical_eh_reduced_action import two_dimensional_ricci_scalar
    r=1.4
    phi=math.log(r)
    out = two_dimensional_ricci_scalar(
        a=1.0, a_prime=0.0, a_second=0.0, r=r,
        phi=phi, phi_t=0.0, phi_r=1.0/r, phi_rr=-1.0/(r*r),
        psi=0.0, psi_t=0.0, psi_tt=0.0, psi_r=0.0,
    )
    assert abs(out) < 2e-14
