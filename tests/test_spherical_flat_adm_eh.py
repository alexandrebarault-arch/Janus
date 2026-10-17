import math


def test_flat_flrw_background_adm_density_is_minus_six_a3_h2_r2():
    from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density
    a=1.7; adot=0.23; r=0.8; n=1.3
    out=flat_spherical_adm_eh_density(
        scale_factor=a, scale_rate=adot, background_lapse=n, r=r,
        Phi=0.0, shift=0.0, shift_r=0.0)
    Hn=adot/(a*n)
    expected=-6.0*n*a**3*r**2*Hn**2
    assert math.isclose(out,expected,rel_tol=0,abs_tol=1e-14)


def test_constant_lapse_perturbation_matches_exact_adm_rescaling():
    from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density
    a=1.4; adot=-0.17; r=0.9; n=0.8; phi=0.07
    out=flat_spherical_adm_eh_density(
        scale_factor=a, scale_rate=adot, background_lapse=n, r=r,
        Phi=phi, shift=0.0, shift_r=0.0)
    N=n*math.sqrt(1+2*phi)
    expected=-6.0*a**3*r**2*(adot/a)**2/N
    assert math.isclose(out,expected,rel_tol=2e-15,abs_tol=1e-14)


def test_radial_shift_uses_both_radial_and_angular_extrinsic_curvatures():
    from numerics.spherical_flat_adm_eh import flat_spherical_adm_eh_density
    a=1.0; r=0.7; q=0.12
    U=q*r
    out=flat_spherical_adm_eh_density(
        scale_factor=a, scale_rate=0.0, background_lapse=1.0, r=r,
        Phi=0.0, shift=U, shift_r=q)
    N=math.sqrt(1+U*U)
    expected=-6.0*r*r*q*q/N
    assert math.isclose(out,expected,rel_tol=2e-15,abs_tol=1e-14)
