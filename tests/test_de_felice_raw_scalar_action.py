import math

from numerics.de_felice_raw_scalar_action import eh_scalar_quadratic_density_flat


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
