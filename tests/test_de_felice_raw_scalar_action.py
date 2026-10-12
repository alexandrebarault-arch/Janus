import math

from numerics.de_felice_raw_scalar_action import (
    eh_scalar_quadratic_density_flat,
    hr_scalar_quadratic_density_g_flat,
)


def test_eq44_g_flat_constraint_slice():
    N = 1.0; a = 0.7; H = 1.3; k = 2.1; Phi = 0.11; B = -0.08
    measured = eh_scalar_quadratic_density_flat(
        lapse=N, scale_factor=a, H=H, Hdot_over_lapse=-0.4, k=k,
        Phi=Phi, B=B, psi=0.0, E=0.0, psi_dot=0.0, E_dot=0.0,
    )
    expected = -9*H**2*Phi**2 + 4*H*k**2/a*Phi*B + 3*H**2*k**2*B**2
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_eq44_pure_trace_kinetic_slice():
    N = 1.2; a = 0.9; H = 0.0; k = 1.7; psid = 0.23
    measured = eh_scalar_quadratic_density_flat(
        lapse=N, scale_factor=a, H=H, Hdot_over_lapse=0.0, k=k,
        Phi=0.0, B=0.0, psi=0.0, E=0.0, psi_dot=psid, E_dot=0.0,
    )
    assert math.isclose(measured, -6*psid**2/N**2, rel_tol=2e-14, abs_tol=2e-14)


def test_eq44_pure_traceless_kinetic_slice():
    N = 1.2; a = 0.9; H = 0.0; k = 1.7; Ed = -0.31
    measured = eh_scalar_quadratic_density_flat(
        lapse=N, scale_factor=a, H=H, Hdot_over_lapse=0.0, k=k,
        Phi=0.0, B=0.0, psi=0.0, E=0.0, psi_dot=0.0, E_dot=Ed,
    )
    expected = k**4*Ed**2/(6*N**2)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_eq44_shift_velocity_cross_slice():
    N = 1.2; a = 0.9; H = 0.0; k = 1.7; B = .13; psid = -.21; Ed = .17
    measured = eh_scalar_quadratic_density_flat(
        lapse=N, scale_factor=a, H=H, Hdot_over_lapse=0.0, k=k,
        Phi=0.0, B=B, psi=0.0, E=0.0, psi_dot=psid, E_dot=Ed,
    )
    expected = B*(2*k**4*Ed/(3*N*a)-4*k**2*psid/(N*a)) - 6*psid**2/N**2 + k**4*Ed**2/(6*N**2)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_eq45_g_flat_hr_pure_g_lapse_and_shift_slice():
    Phi = .13; B = -.09; k = 2.2; mu_g = .7
    measured = hr_scalar_quadratic_density_g_flat(
        xi=1.2, ctilde=.8, k=k, mu_g=mu_g, mu_f=0.0,
        zeta=0.0, gamma_m=0.0, Phi=Phi, B=B,
        varphi=0.0, b=0.0, Sigma=0.0, S=0.0,
    )
    expected = mu_g*(.5*Phi**2-.5*k**2*B**2)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_eq46_relative_shift_square():
    xi = 1.1; c = .73; k = 1.9; zeta = .62; B = .14; b = -.05
    measured = hr_scalar_quadratic_density_g_flat(
        xi=xi, ctilde=c, k=k, mu_g=0.0, mu_f=0.0,
        zeta=zeta, gamma_m=0.0, Phi=0.0, B=B,
        varphi=0.0, b=b, Sigma=0.0, S=0.0,
    )
    expected = .5*zeta*k**2*(B-c*b)**2/(c+1)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)


def test_eq45_gamma_spatial_difference_slice():
    k = 1.9; gm = .42; Sig = .12; S = -.07
    measured = hr_scalar_quadratic_density_g_flat(
        xi=1.1, ctilde=1.0, k=k, mu_g=0.0, mu_f=0.0,
        zeta=0.0, gamma_m=gm, Phi=0.0, B=0.0,
        varphi=0.0, b=0.0, Sigma=Sig, S=S,
    )
    tr = 6*Sig
    h2 = 12*Sig**2 + (2/3)*k**4*S**2
    expected = .125*gm*(tr**2-h2)
    assert math.isclose(measured, expected, rel_tol=2e-14, abs_tol=2e-14)
