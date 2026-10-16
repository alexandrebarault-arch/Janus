import math
import numpy as np


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


def test_pulled_back_dust_reduces_to_native_for_identity_map():
    from numerics.spherical_dust_phase_action import (
        native_conformal_dust_phase_density,
        pulled_back_conformal_dust_phase_density,
    )
    kwargs = dict(
        scale_factor=0.9, conformal_H=0.7, native_r=0.4, rho=2.2,
        Phi=-0.01, q=0.03, q_t_common=0.04, q_r_common=-0.05,
        momentum=0.08,
    )
    actual = pulled_back_conformal_dust_phase_density(
        jacobian=np.eye(2), **kwargs,
    )
    expected = native_conformal_dust_phase_density(
        scale_factor=kwargs["scale_factor"],
        conformal_H=kwargs["conformal_H"],
        r=kwargs["native_r"], rho=kwargs["rho"], Phi=kwargs["Phi"],
        q=kwargs["q"], q_t=kwargs["q_t_common"], q_r=kwargs["q_r_common"],
        momentum=kwargs["momentum"],
    )
    assert math.isclose(actual, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_background_nonhomothetic_pullback_matches_f_sector_prefactor():
    from numerics.spherical_dust_phase_action import pulled_back_conformal_dust_phase_density
    a = 0.63
    xi = 0.74
    c = 0.58
    b = a*xi
    r = 0.37
    H = 0.91
    rho = 3.2
    Phi = 0.014
    q = -0.026
    q_t = 0.033
    q_r = 0.071
    momentum = 0.12

    actual = pulled_back_conformal_dust_phase_density(
        scale_factor=b, conformal_H=H, native_r=r,
        rho=rho, Phi=Phi, q=q,
        q_t_common=q_t, q_r_common=q_r, momentum=momentum,
        jacobian=np.diag([c, 1.0]),
    )
    expected = b**4*r*r*(
        momentum*q_t + c*H*momentum*q
        - c*momentum*Phi + 0.5*c*rho*Phi*Phi
        - 0.5*c*rho*q_r*q_r
    )
    assert math.isclose(actual, expected, rel_tol=2e-14, abs_tol=2e-14)
