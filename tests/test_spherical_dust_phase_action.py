import math


def test_native_conformal_density_matches_cosmic_de_felice_dust_phase():
    from numerics.spherical_dust_phase_action import native_conformal_dust_phase_density
    a = 0.73
    r = 0.41
    H = 0.82
    rho = 2.7
    Phi = 0.013
    q = -0.021
    q_t = 0.034
    k = 5.2
    momentum = 0.17

    measured = native_conformal_dust_phase_density(
        scale_factor=a, conformal_H=H, r=r, rho=rho,
        Phi=Phi, q=q, q_t=q_t, q_r=k*q, momentum=momentum,
    )

    # q_D=a*q for the g-sector cosmic-time De Felice variable.  Therefore
    # q_Ddot=q_t+H q and the full conformal measure is a^4.
    q_D = a*q
    q_Ddot = q_t + H*q
    local = (
        momentum*q_Ddot - momentum*Phi + 0.5*rho*Phi*Phi
        - 0.5*rho/(a*a)*k*k*q_D*q_D
    )
    expected = a**4*r*r*local
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_native_dust_density_is_quadratic_and_zero_at_origin():
    from numerics.spherical_dust_phase_action import native_conformal_dust_phase_density
    kwargs = dict(scale_factor=0.8, conformal_H=0.6, r=0.5, rho=3.1)
    assert native_conformal_dust_phase_density(
        Phi=0.0, q=0.0, q_t=0.0, q_r=0.0, momentum=0.0, **kwargs,
    ) == 0.0
    one = native_conformal_dust_phase_density(
        Phi=0.01, q=0.02, q_t=-0.03, q_r=0.04, momentum=0.05, **kwargs,
    )
    two = native_conformal_dust_phase_density(
        Phi=0.02, q=0.04, q_t=-0.06, q_r=0.08, momentum=0.10, **kwargs,
    )
    assert math.isclose(two, 4.0*one, rel_tol=2e-14, abs_tol=2e-14)
